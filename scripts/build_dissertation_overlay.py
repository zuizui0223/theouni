from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCHITECTURE = ROOT / "universe" / "dissertation_architecture.json"
ATLAS = ROOT / "universe" / "worldline_atlas.json"
DEFAULT_OUTPUT = ROOT / "graphify-out" / ".dissertation_extraction.json"
REPORT = ROOT / "graphify-out" / "DISSERTATION_REPORT.md"


def main() -> None:
    architecture = json.loads(ARCHITECTURE.read_text(encoding="utf-8"))
    atlas = json.loads(ATLAS.read_text(encoding="utf-8"))
    output = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_OUTPUT

    nodes: list[dict] = []
    edges: list[dict] = []
    node_ids: set[str] = set()
    edge_keys: set[tuple[str, str, str]] = set()

    def add_node(node_id: str, label: str, node_type: str, **extra: object) -> None:
        if node_id in node_ids:
            return
        node_ids.add(node_id)
        nodes.append(
            {
                "id": node_id,
                "label": label,
                "file_type": node_type,
                "source_file": str(ARCHITECTURE),
                "source_location": "/",
                "_origin": "curated_dissertation_architecture",
                **extra,
            }
        )

    def add_edge(source: str, target: str, relation: str, context: str = "dissertation_architecture") -> None:
        key = (source, target, relation)
        if key in edge_keys:
            return
        edge_keys.add(key)
        edges.append(
            {
                "source": source,
                "target": target,
                "relation": relation,
                "context": context,
                "confidence": "EXTRACTED",
                "source_file": str(ARCHITECTURE),
                "source_location": "/",
                "weight": 1.0,
            }
        )

    root = "dissertation:transport_failure"
    add_node(
        root,
        architecture["title"],
        "dissertation",
        description=architecture["core_question"],
        status=architecture["status"],
    )

    intro = architecture["general_introduction"]
    add_node(intro["id"], intro["title"], "general_introduction", description=intro["role"])
    add_edge(root, intro["id"], "begins_with")

    atlas_invariants = {item["id"]: item for item in atlas["invariants"]}
    for invariant_id in intro["invariants_imported"]:
        invariant = atlas_invariants[invariant_id]
        add_node(invariant_id, invariant["label"], "universe_invariant", description=invariant["statement"])
        add_edge(intro["id"], invariant_id, "imports_invariant")

    worldline_labels = {item["id"]: item["label"] for item in atlas["worldlines"]}

    research_chapters: list[dict] = []
    for part in sorted(architecture["parts"], key=lambda item: item["order"]):
        add_node(part["id"], part["title"], "dissertation_part", order=part["order"])
        add_edge(root, part["id"], "contains_part")
        for chapter in sorted(part["chapters"], key=lambda item: item["order"]):
            research_chapters.append(chapter)
            add_node(
                chapter["id"],
                chapter["title"],
                "research_chapter",
                order=chapter["order"],
                headline_result=chapter["headline_result"],
            )
            add_edge(part["id"], chapter["id"], "contains_chapter")

            for worldline_id in chapter["primary_worldlines"]:
                add_node(worldline_id, worldline_labels[worldline_id], "scientific_worldline")
                add_edge(chapter["id"], worldline_id, "traverses_worldline")

            for repo_id in chapter["primary_source_repositories"]:
                add_node(repo_id, repo_id.removeprefix("repo:"), "source_repository")
                add_edge(chapter["id"], repo_id, "source_owned_by")

            for module in chapter["primary_modules"]:
                module_id = f"module:{module}"
                add_node(module_id, module, "primary_source_module")
                add_edge(chapter["id"], module_id, "uses_primary_module")

            for module in chapter["embedded_theouni_modules"]:
                module_id = f"module:{module}"
                add_node(module_id, module, "embedded_bridge_module")
                add_edge(chapter["id"], module_id, "embeds_firewall_module")

            forbidden_id = f"forbidden:{chapter['id'].split(':')[-1]}"
            add_node(
                forbidden_id,
                chapter["primary_forbidden_inference"],
                "forbidden_inference",
            )
            add_edge(chapter["id"], forbidden_id, "forbids_inference")

            novelty_id = f"novelty:{chapter['id'].split(':')[-1]}"
            add_node(novelty_id, chapter["novelty_role"], "novelty_role")
            add_edge(chapter["id"], novelty_id, "earns_novelty_by")

    synthesis = architecture["general_synthesis"]
    add_node(
        synthesis["id"],
        synthesis["title"],
        "general_synthesis",
        headline_result=synthesis["headline_result"],
    )
    add_edge(root, synthesis["id"], "ends_with")
    for worldline_id in synthesis["primary_worldlines"]:
        add_node(worldline_id, worldline_labels[worldline_id], "scientific_worldline")
        add_edge(synthesis["id"], worldline_id, "traverses_worldline")
    for repo_id in synthesis["primary_source_repositories"]:
        add_node(repo_id, repo_id.removeprefix("repo:"), "source_repository")
        add_edge(synthesis["id"], repo_id, "source_owned_by")
    for module in synthesis["primary_modules"]:
        module_id = f"module:{module}"
        add_node(module_id, module, "synthesis_module")
        add_edge(synthesis["id"], module_id, "uses_synthesis_module")

    synthesis_forbidden = "forbidden:synthesis"
    add_node(synthesis_forbidden, synthesis["primary_forbidden_inference"], "forbidden_inference")
    add_edge(synthesis["id"], synthesis_forbidden, "forbids_inference")
    synthesis_novelty = "novelty:synthesis"
    add_node(synthesis_novelty, synthesis["novelty_role"], "novelty_role")
    add_edge(synthesis["id"], synthesis_novelty, "earns_novelty_by")

    preferred = architecture["preferred_sequence"]
    for source, target in zip(preferred, preferred[1:]):
        add_edge(source, target, "preferred_editorial_transition")
    for dependency in architecture["scientific_dependencies"]:
        add_edge(
            dependency["source"],
            dependency["target"],
            "hard_scientific_dependency",
            dependency["relation"],
        )

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(
            {
                "nodes": nodes,
                "edges": edges,
                "hyperedges": [],
                "input_tokens": 0,
                "output_tokens": 0,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    lines = [
        "# Graphify Dissertation Architecture Report",
        "",
        "## Purpose",
        "",
        "This focused overlay records the novelty-first dissertation traversal. It does not replace the non-linear Worldline Atlas, change the source theorem DAG, or transfer source theorem ownership to `theouni`.",
        "",
        "## Thesis",
        "",
        f"> **{architecture['core_question']}**",
        "",
        "## Summary",
        "",
        f"- research parts: {len(architecture['parts'])}",
        f"- source-owned research chapters: {len(research_chapters)}",
        f"- general introduction: 1",
        f"- general synthesis: 1",
        f"- covered worldlines: {len({w for c in research_chapters for w in c['primary_worldlines']} | set(synthesis['primary_worldlines']))}",
        f"- embedded bridge/firewall modules: {len(architecture['embedded_module_allocation'])}",
        f"- hard scientific dependencies: {len(architecture['scientific_dependencies'])}",
        f"- Graphify-compatible overlay nodes: {len(nodes)}",
        f"- Graphify-compatible overlay edges: {len(edges)}",
        "",
        "## Preferred traversal",
        "",
        "```text",
    ]
    lines.extend(architecture["preferred_sequence"])
    lines.extend(["```", ""])

    lines.extend(["## Research parts and chapters", ""])
    for part in sorted(architecture["parts"], key=lambda item: item["order"]):
        lines.append(f"### Part {part['order']} — {part['title']}")
        lines.append("")
        for chapter in sorted(part["chapters"], key=lambda item: item["order"]):
            lines.append(f"- **Chapter {chapter['order']} — {chapter['title']}**")
            lines.append(f"  - worldline: {', '.join(chapter['primary_worldlines'])}")
            lines.append(f"  - source owner: {', '.join(chapter['primary_source_repositories'])}")
            embedded = chapter["embedded_theouni_modules"]
            lines.append(f"  - embedded module: {', '.join(embedded) if embedded else 'none'}")
            lines.append(f"  - forbidden inference: `{chapter['primary_forbidden_inference']}`")
        lines.append("")

    lines.extend(
        [
            "## General synthesis",
            "",
            f"- title: **{synthesis['title']}**",
            f"- worldline: {', '.join(synthesis['primary_worldlines'])}",
            f"- modules: {', '.join(synthesis['primary_modules'])}",
            f"- forbidden inference: `{synthesis['primary_forbidden_inference']}`",
            "",
            "## Embedded module allocation",
            "",
        ]
    )
    for module, location in architecture["embedded_module_allocation"].items():
        lines.append(f"- `{module}` -> `{location}`")

    lines.extend(["", "## Hard scientific dependency", ""])
    for dependency in architecture["scientific_dependencies"]:
        lines.append(
            f"- `{dependency['source']}` -> `{dependency['target']}`: `{dependency['relation']}`"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "```text",
            "Worldline Atlas",
            "    = all scientifically allowed task-indexed traversals",
            "",
            "Dissertation architecture",
            "    = the editorial traversal that best exposes non-obvious transport failures",
            "```",
            "",
            "The architecture is preferred for novelty, but it is not promoted to a privileged theory order.",
            "",
        ]
    )
    REPORT.write_text("\n".join(lines), encoding="utf-8")

    print(f"Dissertation overlay: {len(nodes)} nodes, {len(edges)} edges, {len(research_chapters)} research chapters")


if __name__ == "__main__":
    main()
