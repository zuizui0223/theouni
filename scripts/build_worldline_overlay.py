from __future__ import annotations

import json
import sys
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "universe" / "worldline_atlas.json"
DEFAULT_OUTPUT = ROOT / "graphify-out" / ".worldline_extraction.json"
REPORT = ROOT / "graphify-out" / "WORLDLINE_REPORT.md"


def count_orders(nodes: list[str], edges: list[tuple[str, str]]) -> int:
    idx = {node: i for i, node in enumerate(nodes)}
    prereq = [0] * len(nodes)
    for source, target in edges:
        prereq[idx[target]] |= 1 << idx[source]

    @lru_cache(maxsize=None)
    def dp(mask: int) -> int:
        if mask == (1 << len(nodes)) - 1:
            return 1
        total = 0
        for i in range(len(nodes)):
            bit = 1 << i
            if mask & bit or prereq[i] & ~mask:
                continue
            total += dp(mask | bit)
        return total

    return dp(0)


def main() -> None:
    atlas = json.loads(ATLAS.read_text(encoding="utf-8"))
    output = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_OUTPUT
    registry = json.loads((ROOT / "universe" / "registry.json").read_text(encoding="utf-8"))
    repo_labels = {repo["id"]: repo["name"] for repo in registry["repositories"]}

    nodes: list[dict] = []
    edges: list[dict] = []
    node_ids: set[str] = set()
    edge_keys: set[tuple[str, str, str, str]] = set()

    def add_node(node_id: str, label: str, node_type: str, **extra: object) -> None:
        if node_id in node_ids:
            return
        node_ids.add(node_id)
        nodes.append({"id": node_id, "label": label, "file_type": node_type, **extra})

    def add_edge(source: str, target: str, relation: str, context: str = "worldline_atlas") -> None:
        key = (source, target, relation, context)
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
                "source_file": str(ATLAS),
                "source_location": "/",
                "weight": 1.0,
            }
        )

    root = "atlas:theory_universe_worldlines"
    add_node(root, atlas["title"], "worldline_atlas", description=atlas["principle"])

    for item in atlas["origin"]["nodes"]:
        add_node(item["id"], item["label"], "worldline_origin")
    add_edge(root, "origin:reality", "begins_from")
    for edge in atlas["origin"]["edges"]:
        add_edge(edge["source"], edge["target"], edge["relation"])

    for invariant in atlas["invariants"]:
        add_node(invariant["id"], invariant["label"], "universe_invariant", description=invariant["statement"])
        add_edge(root, invariant["id"], "governed_by_invariant")

    for worldline in atlas["worldlines"]:
        add_node(
            worldline["id"],
            worldline["label"],
            "scientific_worldline",
            description=worldline["question"],
            forbidden_inference=worldline["forbidden_inference"],
            output_type=worldline["output_type"],
        )
        add_edge(root, worldline["id"], "contains_worldline")
        add_edge("origin:task", worldline["id"], "branches_into_task_view")
        for repo_id in worldline["source_repositories"]:
            add_node(repo_id, repo_labels[repo_id], "source_repository")
            add_edge(root, repo_id, "references_source_owner")
            add_edge(repo_id, worldline["id"], "owns_or_contributes_to_worldline")

    for observable in atlas["perspective_observables"]:
        add_node(observable["id"], observable["label"], "perspective_observable")
        for worldline_id in observable["visible_in"]:
            add_edge(worldline_id, observable["id"], "reveals_under_perspective")

    for intersection in atlas["intersections"]:
        add_node(
            intersection["id"],
            intersection["label"],
            "worldline_intersection",
            description=intersection["result"],
            condition=intersection["condition"],
        )
        add_edge(root, intersection["id"], "contains_intersection")
        for worldline_id in intersection["worldlines"]:
            add_edge(worldline_id, intersection["id"], "meets_at")

    for bridge in atlas["bridge_types"]:
        add_node(bridge["id"], bridge["label"], "bridge_type", description=bridge["purpose"])
        add_edge(root, bridge["id"], "recognizes_bridge_type")

    for termination in atlas["termination_modes"]:
        add_node(termination["id"], termination["label"], "termination_mode", description=termination["definition"])
        add_edge(root, termination["id"], "allows_termination")

    for failure in atlas["failure_modes"]:
        add_node(failure["id"], failure["label"], "universe_failure_mode", description=failure["definition"])
        add_edge(root, failure["id"], "recognizes_failure_mode")

    dependencies: list[tuple[str, str]] = []
    for dependency in atlas["hard_dependencies"]:
        dependencies.append((dependency["source"], dependency["target"]))
        add_edge(dependency["source"], dependency["target"], dependency["relation"], dependency["reason"])

    assert all(edge["source"] in node_ids and edge["target"] in node_ids for edge in edges)
    assert not any(edge["source"] == edge["target"] for edge in edges)

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(
            {"nodes": nodes, "edges": edges, "hyperedges": [], "input_tokens": 0, "output_tokens": 0},
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    worldline_ids = [item["id"] for item in atlas["worldlines"]]
    order_count = count_orders(worldline_ids, dependencies)
    report = f"""# Graphify Worldline Overlay Report\n\n## Purpose\n\nThis is the focused task/perspective overlay for `theouni`. It complements the full portfolio Graphify graph; it does not replace repository provenance, source theorem ownership, or evidence leaves.\n\n## Summary\n\n- worldlines: {len(atlas['worldlines'])}\n- universe-wide invariants: {len(atlas['invariants'])}\n- perspective-specific observables: {len(atlas['perspective_observables'])}\n- worldline intersections: {len(atlas['intersections'])}\n- bridge types: {len(atlas['bridge_types'])}\n- legitimate termination modes: {len(atlas['termination_modes'])}\n- genuine universe failure modes: {len(atlas['failure_modes'])}\n- hard scientific dependency edges: {len(dependencies)}\n- topological chapter orders under those hard dependencies: {order_count}\n- Graphify-compatible overlay nodes: {len(nodes)}\n- Graphify-compatible overlay edges: {len(edges)}\n\n## Hard dependency\n\nThe current atlas declares one chapter-level scientific prerequisite:\n\n```text\nLoss / Dynamic State -> Warning / Portability\n```\n\nWarning remains free to appear early in a narrative only if its loss prerequisite is restated locally; presentation does not reverse the theorem dependency.\n\n## Main intersections\n\n- Required-State Junction — Capability, Future, History, Mechanism.\n- Knowledge Junction — Required state, Evidence/Licensing, Causal Learning.\n- Revision Junction — a stored old representation meets a revised scientific task.\n- Loss-Warning Junction — `LossGeneratingState <= WarningEvaluationState`.\n- Reality-to-Theory Junction — every model-world worldline returns to empirical admission and claim ceilings.\n\n## Consistency ceiling\n\nThe overlay inherits the v0.6 pairwise result (`12` modules, `66` pairs, `actual-conflict = 0`) and the triadic screen (`220` triples, `2` bounded executable shared-carrier witnesses). It does not turn either audit into a global consistency theorem.\n\n## Interpretation\n\n```text\nPortfolio graph = provenance / ownership / evidence / repository topology\nWorldline atlas = task / perspective / intersection / invariant / termination topology\n```\n\nThe theory has a dependency structure, but no privileged narrative order.\n"""
    REPORT.write_text(report, encoding="utf-8")
    print(f"Worldline overlay: {len(nodes)} nodes, {len(edges)} edges, {order_count} topological orders")


if __name__ == "__main__":
    main()
