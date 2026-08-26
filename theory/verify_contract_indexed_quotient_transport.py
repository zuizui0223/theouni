from __future__ import annotations

import json
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Callable, Hashable, Iterable, Sequence

World = Hashable
Label = Hashable
Partition = frozenset[frozenset[World]]

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "theory" / "contract_indexed_adequacy_registry.json"


def partition(worlds: Iterable[World], fn: Callable[[World], Label]) -> Partition:
    blocks: dict[Label, set[World]] = {}
    for world in worlds:
        blocks.setdefault(fn(world), set()).add(world)
    return frozenset(frozenset(block) for block in blocks.values())


def refines(fine: Partition, coarse: Partition) -> bool:
    """Return whether every fine block lies inside one coarse block."""
    return all(any(block <= target for target in coarse) for block in fine)


def factors_through(
    worlds: Iterable[World],
    target: Callable[[World], Label],
    representation: Callable[[World], Label],
) -> bool:
    """Set-theoretic exact factorization criterion: target = f o representation."""
    seen: dict[Label, Label] = {}
    for world in worlds:
        retained = representation(world)
        response = target(world)
        if retained in seen and seen[retained] != response:
            return False
        seen[retained] = response
    return True


def task_leq(
    worlds: Iterable[World],
    alpha: Callable[[World], Label],
    beta: Callable[[World], Label],
) -> bool:
    """alpha <=task beta iff Sigma_alpha factors through Sigma_beta."""
    return factors_through(worlds, alpha, beta)


def restricted_growth_partitions(size: int) -> list[tuple[int, ...]]:
    """Enumerate every set partition as a canonical restricted-growth label tuple."""
    if size < 1:
        return []
    labels: list[tuple[int, ...]] = []

    def extend(prefix: tuple[int, ...]) -> None:
        if len(prefix) == size:
            labels.append(prefix)
            return
        for label in range(max(prefix) + 2):
            extend(prefix + (label,))

    extend((0,))
    return labels


def label_map(labels: Sequence[Label]) -> Callable[[int], Label]:
    return lambda world: labels[world]


def joint_map(
    alpha: Callable[[World], Label], beta: Callable[[World], Label]
) -> Callable[[World], tuple[Label, Label]]:
    return lambda world: (alpha(world), beta(world))


def verify_registry_contract(registry: dict) -> None:
    assert registry["schema_version"] == "theouni-contract-indexed-adequacy.v0.6-draft"
    assert registry["status"] == "draft_machine_readable_theory_spine"
    assert registry["base_contract"]["current_interpretation"] == "v0.5.1"
    assert registry["base_contract"]["semantic_core_changed"] is False
    assert registry["base_contract"]["claim_ceiling_expanded"] is False

    result_ids = [result["id"] for result in registry["results"]]
    assert result_ids == ["CIRA-1", "CIRA-2", "CIRA-3", "CIRA-4", "CIRA-5"]

    branches = {item["module"]: item["branch"] for item in registry["specializations"]}
    assert {module for module, branch in branches.items() if branch == "exact"} == {
        "TU-1",
        "TU-3",
        "TU-4",
    }
    assert branches["TU-2"] == "graded_epistemic_analogue"

    for item in registry["specializations"]:
        assert (ROOT / item["source"]).is_file(), item["source"]
    for path in registry["preserved_artifacts"]:
        assert (ROOT / path).is_file(), path
    for field in (
        "documentation",
        "verifier",
        "contradiction_registry",
        "contradiction_certificate",
    ):
        assert (ROOT / registry[field]).is_file(), registry[field]


def verify_registry_witnesses(registry: dict) -> None:
    witnesses = registry["finite_witnesses"]
    worlds = list(range(len(witnesses["worlds"])))
    tasks = {
        name: label_map(labels) for name, labels in witnesses["task_signatures"].items()
    }

    weak, middle, strong = (tasks[name] for name in witnesses["preorder_chain"])
    assert task_leq(worlds, weak, middle)
    assert task_leq(worlds, middle, strong)
    assert task_leq(worlds, weak, strong)
    assert not task_leq(worlds, strong, middle)

    left_name, right_name = witnesses["incomparable_pair"]
    left, right = tasks[left_name], tasks[right_name]
    assert not task_leq(worlds, left, right)
    assert not task_leq(worlds, right, left)
    assert not factors_through(worlds, right, left)
    assert not factors_through(worlds, left, right)

    alpha_name, beta_name = witnesses["joint_pair"]
    alpha, beta = tasks[alpha_name], tasks[beta_name]
    joint = joint_map(alpha, beta)
    assert factors_through(worlds, alpha, joint)
    assert factors_through(worlds, beta, joint)
    assert partition(worlds, joint) == partition(worlds, tasks["joint"])


def verify_exhaustive_partition_laws() -> None:
    """Exhaust every partition on four worlds (Bell(4)=15)."""
    worlds = tuple(range(4))
    labelings = restricted_growth_partitions(len(worlds))
    assert len(labelings) == 15
    maps = [label_map(labels) for labels in labelings]

    for alpha, representation in product(maps, repeat=2):
        exact = factors_through(worlds, alpha, representation)
        kernel_inclusion = refines(
            partition(worlds, representation), partition(worlds, alpha)
        )
        assert exact == kernel_inclusion
        assert factors_through(worlds, alpha, alpha)

    for alpha, beta, gamma in product(maps, repeat=3):
        if task_leq(worlds, alpha, beta) and task_leq(worlds, beta, gamma):
            assert task_leq(worlds, alpha, gamma)

        canonical_alpha = alpha
        assert factors_through(worlds, beta, canonical_alpha) == task_leq(
            worlds, beta, alpha
        )

        joint = joint_map(alpha, beta)
        joint_adequate = factors_through(worlds, joint, gamma)
        componentwise = factors_through(worlds, alpha, gamma) and factors_through(
            worlds, beta, gamma
        )
        assert joint_adequate == componentwise
        assert partition(worlds, joint) == frozenset(
            left & right
            for left in partition(worlds, alpha)
            for right in partition(worlds, beta)
            if left & right
        )


@dataclass(frozen=True)
class WorldBits:
    a: int
    b: int
    nuisance: int = 0


def verify_tu1_specialization() -> None:
    worlds = [WorldBits(a, b) for a in (0, 1) for b in (0, 1)]
    old_state = lambda world: world.a
    revised_task = lambda world: (world.a, world.b)
    weaker_future_task = lambda world: world.a
    assert not factors_through(worlds, revised_task, old_state)
    assert factors_through(worlds, weaker_future_task, old_state)


def verify_tu3_specialization() -> None:
    worlds = [
        WorldBits(a, b, nuisance)
        for a in (0, 1)
        for b in (0, 1)
        for nuisance in range(4)
    ]
    loss_signature = lambda world: world.a
    representation = lambda world: (world.a, world.b)
    assert factors_through(worlds, loss_signature, representation)
    richer_loss_signature = lambda world: (world.a, world.nuisance % 2)
    assert not factors_through(worlds, richer_loss_signature, representation)


def verify_tu4_specialization() -> None:
    worlds = [WorldBits(a, b) for a in (0, 1) for b in (0, 1)]
    loss = lambda world: world.a
    warning_joint = lambda world: (world.a, world.b)
    assert task_leq(worlds, loss, warning_joint)
    assert not task_leq(worlds, warning_joint, loss)
    assert refines(partition(worlds, warning_joint), partition(worlds, loss))


def verify_tu2_exact_endpoints_only() -> None:
    worlds = [WorldBits(a, b) for a in (0, 1) for b in (0, 1)]
    causal_task = lambda world: world.a
    report_task = lambda world: world.b
    assert not task_leq(worlds, causal_task, report_task)
    assert not task_leq(worlds, report_task, causal_task)


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    verify_registry_contract(registry)
    verify_registry_witnesses(registry)
    verify_exhaustive_partition_laws()
    verify_tu1_specialization()
    verify_tu3_specialization()
    verify_tu4_specialization()
    verify_tu2_exact_endpoints_only()
    print(
        "v0.6 draft spine verified: machine-readable CIRA-1..5, all 15 partitions "
        "on four worlds, TU-1/TU-3/TU-4 exact specializations, and TU-2 graded branch."
    )


if __name__ == "__main__":
    main()
