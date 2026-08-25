from __future__ import annotations

from dataclasses import dataclass
from math import log2
from typing import Iterable


CausalState = tuple[int, ...]
World = tuple[CausalState, int]


def worlds(m: int) -> tuple[World, ...]:
    if m < 1:
        raise ValueError("m must be >= 1")
    out: list[World] = []
    for value in range(2**m):
        state = tuple((value >> shift) & 1 for shift in reversed(range(m)))
        for target in (0, 1):
            out.append((state, target))
    return tuple(out)


def observe(world: World, k: int, reveal_target: bool):
    state, target = world
    if not 0 <= k <= len(state):
        raise ValueError("k outside causal-state dimension")
    prefix = state[:k]
    if reveal_target:
        return prefix + (target,)
    return prefix


def evidence_classes(m: int, k: int, reveal_target: bool):
    classes: dict[tuple[int, ...], list[World]] = {}
    for world in worlds(m):
        record = observe(world, k, reveal_target)
        classes.setdefault(record, []).append(world)
    return classes


def target_licensed_for_every_record(m: int, k: int, reveal_target: bool) -> bool:
    for compatible in evidence_classes(m, k, reveal_target).values():
        if len({target for _, target in compatible}) != 1:
            return False
    return True


def causal_information_bits(m: int, k: int, reveal_target: bool) -> float:
    """Exact I(S;Q) under the uniform product-world construction.

    The target is independent of S, and Q reveals exactly k causal bits.
    The closed form is k; this implementation also makes that contract explicit.
    """
    if not 0 <= k <= m:
        raise ValueError("k outside causal-state dimension")
    return float(k)


def normalized_nov(m: int, k: int, reveal_target: bool) -> float:
    return causal_information_bits(m, k, reveal_target) / m


@dataclass(frozen=True)
class ExperimentAudit:
    m: int
    k: int
    reveal_target: bool
    causal_information_bits: float
    normalized_causal_nov: float
    target_licensed_every_record: bool
    record_count: int


def audit_experiment(m: int, k: int, reveal_target: bool) -> ExperimentAudit:
    classes = evidence_classes(m, k, reveal_target)
    return ExperimentAudit(
        m=m,
        k=k,
        reveal_target=reveal_target,
        causal_information_bits=causal_information_bits(m, k, reveal_target),
        normalized_causal_nov=normalized_nov(m, k, reveal_target),
        target_licensed_every_record=target_licensed_for_every_record(
            m, k, reveal_target
        ),
        record_count=len(classes),
    )
