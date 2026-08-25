from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GRAPH_PATH = ROOT / "empirical" / "reality_theory_graph.json"


def all_simple_paths(adjacency: dict[str, list[str]], source: str, target: str, node_count: int) -> list[list[str]]:
    paths: list[list[str]] = []

    def visit(node: str, path: list[str], seen: set[str]) -> None:
        if len(path) > node_count:
            raise AssertionError("cycle or malformed path traversal")
        if node == target:
            paths.append(path[:])
            return
        for nxt in adjacency.get(node, []):
            if nxt in seen:
                continue
            visit(nxt, path + [nxt], seen | {nxt})

    visit(source, [source], {source})
    return paths


def main() -> None:
    graph = json.loads(GRAPH_PATH.read_text(encoding="utf-8"))
    assert graph["schema_version"] == "theouni-reality-theory-bridge-graph.v0.1"
    assert graph["directed"] is True

    nodes = graph["nodes"]
    node_ids = [node["id"] for node in nodes]
    assert len(node_ids) == len(set(node_ids)), "duplicate graph node"
    node_set = set(node_ids)

    edges = graph["edges"]
    edge_pairs: list[tuple[str, str]] = []
    adjacency: dict[str, list[str]] = defaultdict(list)
    for edge in edges:
        source = edge["source"]
        target = edge["target"]
        assert source in node_set and target in node_set
        assert source != target
        assert edge["relation"].strip()
        pair = (source, target)
        assert pair not in edge_pairs, f"duplicate edge {pair}"
        edge_pairs.append(pair)
        adjacency[source].append(target)

    forbidden = {tuple(pair) for pair in graph["forbidden_direct_edges"]}
    assert not (set(edge_pairs) & forbidden), "forbidden shortcut edge present"

    # Every declared invariant must have at least one route and every route must pass the gate.
    for invariant in graph["path_invariants"]:
        target = invariant["target"]
        required = invariant["must_include"]
        assert target in node_set and required in node_set
        for source in invariant["source_set"]:
            assert source in node_set
            paths = all_simple_paths(adjacency, source, target, len(node_ids))
            assert paths, f"no path from {source} to {target} for {invariant['id']}"
            assert all(required in path for path in paths), (
                f"{invariant['id']} violated: a path from {source} to {target} bypasses {required}: "
                f"{[path for path in paths if required not in path]}"
            )

    # CR-4 support cannot masquerade as a state by any alternate route.
    support_paths = all_simple_paths(adjacency, "CandidateWorldSupport", "RequiredState", len(node_ids))
    assert support_paths
    assert all("EmpiricalProjectionGate" in path for path in support_paths)

    # CR-5 raw observation cannot become a biological event directly or by bypassing reliability.
    sensor_paths = all_simple_paths(adjacency, "ObservationRecord", "BiologicalEventRecord", len(node_ids))
    assert sensor_paths
    assert all("ReliabilityQualification" in path for path in sensor_paths)

    print(
        "Reality-to-Theory bridge graph v0.1 validated: "
        f"{len(nodes)} nodes, {len(edges)} edges, {len(graph['path_invariants'])} path firewalls, "
        "and no forbidden direct shortcuts."
    )


if __name__ == "__main__":
    main()
