import json
import subprocess
import sys
from pathlib import Path

from graphify.analyze import god_nodes, suggest_questions, surprising_connections
from graphify.build import build_from_json
from graphify.cluster import cluster, score_all
from graphify.diagnostics import diagnose_extraction, format_diagnostic_report
from graphify.export import to_json
from graphify.report import generate


ROOT = Path(__file__).resolve().parents[1]


LABELS = {
    0: "Definability and Shared Ontology",
    1: "Phenotype Geography",
    2: "Future Worlds and Forecasting",
    3: "Eco-genetic Conditions and Island Dynamics",
    4: "CREST and Evidence Licensing",
    5: "Evolutionary and Pigment History",
    6: "Sensor Observability and Capture",
    7: "Transport and Mechanism Robustness",
    8: "Eco-genetic Mechanistic Parent",
    9: "Trait Interaction Architecture",
    10: "RACH Causal Learning",
    11: "Specimen Measurement",
    12: "Candidate Survey Patches",
    13: "SDM Candidate-Universe Learning",
    14: "Theory Universe Meta Registry",
    15: "Island Macroecology and Evidence",
}


def main() -> None:
    extraction_path = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "graphify-out" / ".curated_extraction.json"
    output_dir = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else ROOT / "graphify-out"
    registry_path = Path(sys.argv[3]).resolve() if len(sys.argv) > 3 else ROOT / "universe" / "registry.json"
    output_dir.mkdir(parents=True, exist_ok=True)

    extraction = json.loads(extraction_path.read_text(encoding="utf-8"))
    diagnostic = diagnose_extraction(extraction, directed=True, root=registry_path.parent)
    print(format_diagnostic_report(diagnostic))
    fatal_keys = (
        "non_object_edges",
        "missing_endpoint_edges",
        "dangling_endpoint_edges",
        "self_loop_edges",
        "exact_duplicate_edges",
        "directed_same_endpoint_collapsed_edges",
    )
    failures = {key: diagnostic[key] for key in fatal_keys if diagnostic[key]}
    if failures:
        raise RuntimeError(f"Curated extraction failed integrity gate: {failures}")

    graph = build_from_json(extraction, root=str(registry_path.parent), directed=True)
    communities = cluster(graph)
    cohesion = score_all(graph, communities)
    if set(communities) != set(LABELS):
        raise RuntimeError(f"Community IDs changed: {sorted(communities)}")

    gods = god_nodes(graph)
    surprises = surprising_connections(graph, communities)
    questions = suggest_questions(graph, communities, LABELS)
    graph_path = output_dir / "graph.json"
    if not to_json(
        graph,
        communities,
        str(graph_path),
        force=True,
        community_labels=LABELS,
    ):
        raise RuntimeError("Graphify refused to write the curated directed graph")

    detection = {
        "total_files": 1,
        "total_words": 0,
        "files": {"code": [], "document": [str(registry_path)], "paper": [], "image": [], "video": []},
        "skipped_sensitive": [],
    }
    report = generate(
        graph,
        communities,
        cohesion,
        LABELS,
        gods,
        surprises,
        detection,
        {"input": 0, "output": 0},
        str(registry_path.parent),
        suggested_questions=questions,
    )
    marker = "## Knowledge Gaps\n"
    note = (
        "## Knowledge Gaps\n"
        "Registry note: Graphify labels degree-one owner objects, claims, non-claims, and evidence leaves as "
        "isolated. These leaves are intentional provenance terminals, not dangling nodes; the integrity audit found "
        "zero dangling or missing endpoints.\n\n"
    )
    report = report.replace(marker, note, 1)
    (output_dir / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
    (output_dir / ".graphify_labels.json").write_text(
        json.dumps({str(key): value for key, value in LABELS.items()}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (output_dir / ".graphify_analysis.json").write_text(
        json.dumps(
            {
                "communities": {str(key): value for key, value in communities.items()},
                "cohesion": {str(key): value for key, value in cohesion.items()},
                "gods": gods,
                "surprises": surprises,
                "questions": questions,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    subprocess.run([sys.executable, "-m", "graphify", "export", "html"], cwd=ROOT, check=True)
    print(f"Directed curated graph: {graph.number_of_nodes()} nodes, {graph.number_of_edges()} edges")


if __name__ == "__main__":
    main()
