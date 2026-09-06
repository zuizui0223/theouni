"""Finite witness for an evidence-admissible scientific transition.

This is a draft bridge utility, not a human informed-consent model and not an
addition to the frozen Theory Universe core. It composes three conditions:
structural target constancy, reliability/evidence satisfaction, and agreement
between the proposed report value and the identified target value.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, Iterable, TypeVar

W = TypeVar("W")
T = TypeVar("T")


def _unique_equal(values: Iterable[T]) -> tuple[T, ...]:
    out: list[T] = []
    for value in values:
        if not any(value == old for old in out):
            out.append(value)
    return tuple(out)


@dataclass(frozen=True)
class TransitionAudit(Generic[T]):
    compatible_world_count: int
    target_values: tuple[T, ...]
    target_point_identified: bool
    reliability_satisfied: bool
    proposal_matches_identified_target: bool
    admissible: bool
    reason: str

    @property
    def identified_target(self) -> T:
        if not self.target_point_identified:
            raise ValueError("target is not point-identified")
        return self.target_values[0]


def audit_evidence_admissible_transition(
    compatible_worlds: Iterable[W],
    *,
    target: Callable[[W], T],
    proposed_value: T,
    reliability_satisfied: bool,
) -> TransitionAudit[T]:
    """Audit one proposed transition from evidence class to target report."""
    worlds = tuple(compatible_worlds)
    if not worlds:
        raise ValueError("compatible_worlds must be non-empty")

    target_values = _unique_equal(target(world) for world in worlds)
    identified = len(target_values) == 1
    proposal_matches = identified and proposed_value == target_values[0]

    if not reliability_satisfied:
        admissible = False
        reason = "reliability_requirement_not_satisfied"
    elif not identified:
        admissible = False
        reason = "target_not_point_identified"
    elif not proposal_matches:
        admissible = False
        reason = "proposal_disagrees_with_identified_target"
    else:
        admissible = True
        reason = "structural_and_reliability_requirements_satisfied"

    return TransitionAudit(
        compatible_world_count=len(worlds),
        target_values=target_values,
        target_point_identified=identified,
        reliability_satisfied=bool(reliability_satisfied),
        proposal_matches_identified_target=proposal_matches,
        admissible=admissible,
        reason=reason,
    )
