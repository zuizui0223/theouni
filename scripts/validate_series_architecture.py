from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SERIES = ROOT / "thesis" / "series_architecture.json"
LEGACY = ROOT / "thesis" / "final_chapter_architecture.json"
SOURCE_MAP = ROOT / "thesis" / "series_source_map.json"
ORDER = ROOT / "thesis" / "FINAL_CHAPTER_ORDER.md"
AUDIT = ROOT / "thesis" / "GRAPHIFY_EDGE_AUDIT_2026-09-06.md"

DRAFTS = {
    "chapter:eco-genetic": ROOT / "thesis" / "drafts" / "series" / "01_eco_genetic_state_validity_v0.1.md",
    "chapter:crest": ROOT / "thesis" / "drafts" / "series" / "02_crest_state_under_changing_futures_v0.1.md",
    "chapter:observation-design": ROOT / "thesis" / "drafts" / "series" / "03_learning_the_state_you_need_v0.1.md",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    series = load(SERIES)
    legacy = load(LEGACY)
    source_map = load(SOURCE_MAP)
    order_text = ORDER.read_text(encoding="utf-8")
    audit_text = AUDIT.read_text(encoding="utf-8")

    assert series["schema_version"] == "theouni-series-architecture.v2"
    assert series["status"] == "preferred_parallel_three_series_architecture_graphify_corrected"
    assert series["research_chapters_parallel"] is True
    assert series["cross_series_hard_dependencies"] == []
    assert series["graphify_basis"]["registry_generated_on"] == "2026-08-25"
    assert "Boundary and MROD" in series["graphify_basis"]["registry_warning"]

    chapters = series["chapters"]
    assert len(chapters) == 5
    assert [row["order"] for row in chapters] == list(range(5))
    expected_ids = ["chapter:introduction", "chapter:eco-genetic", "chapter:crest", "chapter:observation-design", "chapter:synthesis"]
    assert [row["id"] for row in chapters] == expected_ids
    by_id = {row["id"]: row for row in chapters}

    legacy_ids = [row["id"] for row in legacy["chapters"]]
    assert len(legacy_ids) == 10
    mapped = []
    for cid in ["chapter:eco-genetic", "chapter:crest", "chapter:observation-design"]:
        mapped.extend(by_id[cid]["legacy_component_ids"])
    assert set(mapped) == {f"chapter:{i}" for i in range(1, 9)}
    assert len(mapped) == len(set(mapped)) == 8

    eco = by_id["chapter:eco-genetic"]
    edge = eco["graphify_core_edge"]
    assert (edge["source"], edge["target"], edge["type"], edge["confidence"]) == (
        "repo:eco-genetic-criticality",
        "repo:eco-genetic-warning-extensions",
        "mechanistic_parent_to_condition_extension",
        "EXTRACTED",
    )
    assert eco["hard_dependencies"] and "LossGeneratingState" in eco["hard_dependencies"][0]

    crest = by_id["chapter:crest"]
    edge_types = {(e["source"], e["target"], e["type"], e["confidence"]) for e in crest["graphify_core_edges"]}
    assert edge_types == {
        ("repo:ccoc", "repo:crest", "conceptual_obstruction_input", "EXTRACTED"),
        ("repo:mltr", "repo:crest", "conceptual_obstruction_input", "EXTRACTED"),
        ("repo:mrm", "repo:crest", "conceptual_obstruction_input", "EXTRACTED"),
        ("repo:ced", "repo:crest", "downstream_evidence_licensing", "EXTRACTED"),
    }
    assert "hub-and-spoke" in crest["dependency_graph"]["note"]
    assert "CED also receives" in " ".join(crest["cross_series_junctions_not_owned_by_crest"])

    learning = by_id["chapter:observation-design"]
    assert learning["graphify_legacy_node"] == "repo:microdonta"
    assert learning["graphify_legacy_community"] == "RACH Causal Learning"
    assert learning["graphify_split_mapping"]["channel_identifiability"] == "zuizui0223/boundary"
    assert learning["graphify_split_mapping"]["admissible_causal_hypotheses_and_next_observation_value"] == "zuizui0223/mrod"
    statuses = {(row["target"], row["type"], row["status"]) for row in learning["external_graphify_bridges"]}
    assert statuses == {
        ("CED", "missing_evidence_risk_bridge", "proposed/inferred"),
        ("MRM", "missing_candidate_family_bridge", "proposed/inferred"),
    }

    cross = {(row["from"], row["to"], row["type"]): row for row in series["cross_series_edges"]}
    assert cross[("eco-genetic-warning-extensions", "crest", "full_warning_domain_state_quotient_bridge")]["status"].startswith("partial")
    assert cross[("microdonta/RACH legacy stream", "CED", "missing_evidence_risk_bridge")]["status"] == "proposed/inferred"
    assert cross[("microdonta/RACH legacy stream", "MRM", "missing_candidate_family_bridge")]["status"] == "proposed/inferred"

    logic = series["dissertation_logic"]
    assert logic["form"] == "three_parallel_research_pillars_plus_junction_synthesis"
    assert "not_allowed" in logic and "eco-genetic→CREST→observation-design" in logic["not_allowed"]
    assert "LossGeneratingState" in logic["junctions"]["loss_warning"]

    policy = series["submission_policy"]
    assert policy["preferred_count"] == 3
    assert len(policy["preferred_primary_papers"]) == 3
    assert "one mega-paper" in " ".join(policy["not_default"]).lower()

    source_rows = {row["chapter"]: row for row in source_map["series"]}
    assert set(source_rows) == {"chapter:eco-genetic", "chapter:crest", "chapter:observation-design"}
    for cid in source_rows:
        assert source_rows[cid]["forbidden_transfer"]

    # Existing integrated drafts remain component reservoirs while their framing is revised.
    for cid, path in DRAFTS.items():
        text = path.read_text(encoding="utf-8")
        assert len(text) >= 7000, (cid, len(text))
        for heading in ["## Problem", "## Standalone contribution", "## Claim ceiling", "## Source ownership"]:
            assert heading in text, (cid, heading)

    for token in ["parallel research pillars", "Eco-genetic", "CREST", "microdonta", "junction"]:
        assert token.lower() in order_text.lower(), token
    for token in [
        "mechanistic_parent_to_condition_extension",
        "conceptual_obstruction_input",
        "downstream_evidence_licensing",
        "missing_evidence_risk_bridge",
        "missing_candidate_family_bridge",
        "2026-08-25",
        "Boundary",
        "MROD",
    ]:
        assert token in audit_text, token

    print("Graphify-corrected three-series architecture validation passed.")
    print("Legacy research components partitioned exactly once:", sorted(mapped))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
