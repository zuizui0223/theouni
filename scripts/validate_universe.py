from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    registry = load("universe/registry.json")
    repositories = registry["repositories"]
    repo_ids = {repo["id"] for repo in repositories}
    expected_count = registry["scope"]["repository_count"]
    assert len(repositories) == expected_count
    assert (
        registry["scope"]["scientific_repository_count"]
        + registry["scope"]["meta_repository_count"]
        == expected_count
    )
    assert len(repo_ids) == expected_count
    assert "repo:theouni" in repo_ids
    assert all(
        relation["source"] in repo_ids and relation["target"] in repo_ids
        for relation in registry["relations"]
    )
    assert all(
        owner in repo_ids
        for concept in registry["ontology"]
        for owner in concept["owned_by"]
    )

    graph = load("graphify-out/graph.json")
    graph_ids = {node["id"] for node in graph["nodes"]}
    assert graph.get("directed") is True
    assert len(graph_ids) == len(graph["nodes"])
    assert "repo:theouni" in graph_ids
    assert all(
        edge["source"] in graph_ids and edge["target"] in graph_ids
        for edge in graph["links"]
    )
    assert not any(edge["source"] == edge["target"] for edge in graph["links"])
    graph_audit = registry["architecture_diagnostics"]["graphify"]
    assert len(graph["nodes"]) == graph_audit["curated_universe_nodes"]
    assert len(graph["links"]) == graph_audit["curated_universe_edges"]
    assert len({node["community"] for node in graph["nodes"]}) == graph_audit["curated_universe_communities"]
    assert len(registry["definability_ledger"]) == 32

    bridge = load("universe/bridges/eco_genetic_crest_bridge_registry.json")
    coarse = bridge["audits"]["coarse_evidence"]["result"]
    detailed = bridge["audits"]["joint_patch_alignment_evidence"]["result"]
    assert bridge["ownership"]["physical_merge"] is False
    assert bridge["source_verification"]["verified"] is True
    assert coarse["required_state_count"] == detailed["required_state_count"] == 2
    assert coarse["coarse_summary_sufficient"] is False
    assert coarse["full_state_licensed"] is False
    assert coarse["monitoring_debt_bits"] == 1.0
    assert detailed["full_state_licensed"] is True
    assert detailed["target_report_licensed"] is True
    assert detailed["monitoring_debt_bits"] == 0.0

    architecture = (ROOT / "universe" / "ARCHITECTURE.md").read_text(encoding="utf-8")
    assert all(repo["name"] in architecture for repo in repositories)
    html = (ROOT / "graphify-out" / "graph.html").read_text(encoding="utf-8")
    assert "Bounded eco-genetic CREST quotient" in html
    assert "theouni" in html

    provenance = load("universe/PROVENANCE.json")
    for item in provenance["managed_files"]:
        path = ROOT / item["path"]
        assert path.stat().st_size == item["bytes"]
        assert sha256(path) == item["sha256"]

    print(
        f"Validated {len(repositories)} repositories, {len(graph['nodes'])} graph nodes, "
        f"{len(graph['links'])} directed edges, bridge claim ceilings, and provenance hashes."
    )


if __name__ == "__main__":
    main()
