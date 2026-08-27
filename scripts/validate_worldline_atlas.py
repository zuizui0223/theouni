from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def unique_ids(items: list[dict]) -> set[str]:
    ids = [item["id"] for item in items]
    assert len(ids) == len(set(ids))
    return set(ids)


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
    atlas = load("universe/worldline_atlas.json")
    assert atlas["schema_version"] == "theouni-worldline-atlas.v1"
    assert atlas["presentation"]["privileged_narrative_order"] is False

    registry = load("universe/registry.json")
    repo_ids = {repo["id"] for repo in registry["repositories"]}

    worldline_ids = unique_ids(atlas["worldlines"])
    invariant_ids = unique_ids(atlas["invariants"])
    observable_ids = unique_ids(atlas["perspective_observables"])
    intersection_ids = unique_ids(atlas["intersections"])
    unique_ids(atlas["bridge_types"])
    unique_ids(atlas["termination_modes"])
    failure_ids = unique_ids(atlas["failure_modes"])

    assert len(worldline_ids) == 9
    assert len(invariant_ids) == 7
    assert "failure:global_consistency_failure" in failure_ids

    observables = {item["id"]: item for item in atlas["perspective_observables"]}
    for worldline in atlas["worldlines"]:
        assert all(repo in repo_ids for repo in worldline["source_repositories"])
        assert worldline["question"] and worldline["forbidden_inference"]
        for observable in worldline["perspective_observables"]:
            assert observable in observable_ids
            assert worldline["id"] in observables[observable]["visible_in"]

    for item in atlas["perspective_observables"]:
        assert item["visible_in"]
        assert all(worldline in worldline_ids for worldline in item["visible_in"])

    for intersection in atlas["intersections"]:
        assert len(intersection["worldlines"]) >= 2
        assert all(worldline in worldline_ids for worldline in intersection["worldlines"])

    dependencies = [(item["source"], item["target"]) for item in atlas["hard_dependencies"]]
    assert ("worldline:loss", "worldline:warning") in dependencies
    assert all(a in worldline_ids and b in worldline_ids and a != b for a, b in dependencies)

    nodes = [item["id"] for item in atlas["worldlines"]]
    order_count = count_orders(nodes, dependencies)
    assert order_count > 1

    for name, order in atlas["presentation"]["example_orders"].items():
        assert len(order) == len(worldline_ids), name
        assert set(order) == worldline_ids, name
        pos = {node: i for i, node in enumerate(order)}
        assert all(pos[a] < pos[b] for a, b in dependencies), name

    contradiction = load("theory/contradiction_matrix.json")
    triadic = load("theory/triadic_screen.json")
    ref = atlas["consistency_reference"]
    assert len(contradiction["modules"]) == ref["pairwise_modules"] == 12
    assert len(contradiction["pairs"]) == ref["pairwise_pairs"] == 66
    assert sum(p["relation"] == "actual-conflict" for p in contradiction["pairs"]) == 0
    assert ref["registered_actual_conflicts"] == 0
    assert triadic["counts"]["unordered_triples"] == ref["triads"] == 220
    assert triadic["counts"]["executable_assessments"]["verified-in-bounded-witness"] == 2
    assert ref["bounded_executable_triads"] == 2

    print(
        f"Validated {len(worldline_ids)} worldlines, {len(invariant_ids)} invariants, "
        f"{len(intersection_ids)} intersections, and {order_count} allowed scientific topological orders."
    )


if __name__ == "__main__":
    main()
