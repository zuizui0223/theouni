from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Hashable, Mapping


World = Hashable
Signature = Hashable


def _groups(signatures: Mapping[World, Signature]) -> dict[Signature, frozenset[World]]:
    if not signatures:
        raise ValueError("signature map must be non-empty")
    out: dict[Signature, set[World]] = defaultdict(set)
    for world, signature in signatures.items():
        out[signature].add(world)
    return {signature: frozenset(worlds) for signature, worlds in out.items()}


def warning_factors_through_loss_state(
    loss_signatures: Mapping[World, Signature],
    warning_signatures: Mapping[World, Signature],
) -> bool:
    if set(loss_signatures) != set(warning_signatures):
        raise ValueError("loss and warning signature domains must match")
    for worlds in _groups(loss_signatures).values():
        if len({warning_signatures[w] for w in worlds}) != 1:
            return False
    return True


def induced_warning_on_loss_states(
    loss_signatures: Mapping[World, Signature],
    warning_signatures: Mapping[World, Signature],
) -> dict[Signature, Signature]:
    if not warning_factors_through_loss_state(loss_signatures, warning_signatures):
        raise ValueError("warning response does not factor through the loss state")
    result: dict[Signature, Signature] = {}
    for loss_signature, worlds in _groups(loss_signatures).items():
        world = next(iter(worlds))
        result[loss_signature] = warning_signatures[world]
    return result


def loss_state_count(loss_signatures: Mapping[World, Signature]) -> int:
    return len(set(loss_signatures.values()))


def warning_state_count(
    loss_signatures: Mapping[World, Signature],
    warning_signatures: Mapping[World, Signature],
) -> int:
    if set(loss_signatures) != set(warning_signatures):
        raise ValueError("loss and warning signature domains must match")
    return len(
        {
            (loss_signatures[world], warning_signatures[world])
            for world in loss_signatures
        }
    )


def warning_state_equals_loss_state(
    loss_signatures: Mapping[World, Signature],
    warning_signatures: Mapping[World, Signature],
) -> bool:
    return warning_factors_through_loss_state(loss_signatures, warning_signatures)


def warning_portable_on_loss_states(
    loss_map_b_to_a: Mapping[Signature, Signature],
    warning_on_loss_a: Mapping[Signature, Signature],
    warning_on_loss_b: Mapping[Signature, Signature],
) -> bool:
    """TU-4C commutation check: gamma_B = gamma_A o h."""
    if set(loss_map_b_to_a) != set(warning_on_loss_b):
        raise ValueError("portability map must cover every B loss state")
    if set(loss_map_b_to_a.values()) != set(warning_on_loss_a):
        raise ValueError("portability map must be bijective onto A loss states")
    if len(set(loss_map_b_to_a.values())) != len(loss_map_b_to_a):
        raise ValueError("portability map must be injective")
    return all(
        warning_on_loss_b[b_state] == warning_on_loss_a[a_state]
        for b_state, a_state in loss_map_b_to_a.items()
    )


@dataclass(frozen=True)
class WarningStateAudit:
    loss_state_count: int
    warning_evaluation_state_count: int
    warning_factors_through_loss_state: bool
    warning_state_equals_loss_state: bool


def audit_warning_state(
    loss_signatures: Mapping[World, Signature],
    warning_signatures: Mapping[World, Signature],
) -> WarningStateAudit:
    factors = warning_factors_through_loss_state(loss_signatures, warning_signatures)
    return WarningStateAudit(
        loss_state_count=loss_state_count(loss_signatures),
        warning_evaluation_state_count=warning_state_count(
            loss_signatures, warning_signatures
        ),
        warning_factors_through_loss_state=factors,
        warning_state_equals_loss_state=factors,
    )
