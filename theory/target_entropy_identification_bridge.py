"""Finite bridge between set-valued target identification and target entropy.

For a finite admissible support in which every stored world/row carries positive
weight, the declared target is point-identified exactly when its entropy is zero.
This is a bridge theorem between representations, not a transfer of ownership
from boundary or MROD into Theory Universe.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from math import isfinite, log2
from typing import Hashable, Sequence


@dataclass(frozen=True)
class TargetEntropyIdentificationAudit:
    n_rows: int
    target_image_size: int
    entropy_bits: float
    point_identified: bool
    entropy_zero: bool
    equivalence_holds: bool


def weighted_target_entropy(
    target_values: Sequence[Hashable],
    *,
    weights: Sequence[float] | None = None,
) -> float:
    """Entropy of a finite declared target under strictly positive row weights."""
    values = tuple(target_values)
    if not values:
        raise ValueError("target_values must be non-empty")
    if weights is None:
        w = (1.0,) * len(values)
    else:
        w = tuple(float(x) for x in weights)
        if len(w) != len(values):
            raise ValueError("weights and target_values must have equal length")
    if any((not isfinite(x)) or x <= 0.0 for x in w):
        raise ValueError("all weights must be finite and strictly positive")

    counts: dict[Hashable, float] = defaultdict(float)
    for value, weight in zip(values, w):
        try:
            hash(value)
        except TypeError as exc:
            raise ValueError("target values must be hashable") from exc
        counts[value] += weight
    total = sum(counts.values())
    return -sum(
        (mass / total) * log2(mass / total)
        for mass in counts.values()
    )


def audit_target_entropy_identification(
    target_values: Sequence[Hashable],
    *,
    weights: Sequence[float] | None = None,
    tolerance: float = 1e-12,
) -> TargetEntropyIdentificationAudit:
    """Audit ``|T(A)|=1 iff H(T|A)=0`` on a finite positive-weight support."""
    if tolerance < 0.0:
        raise ValueError("tolerance must be non-negative")
    values = tuple(target_values)
    if not values:
        raise ValueError("target_values must be non-empty")
    entropy = weighted_target_entropy(values, weights=weights)
    image_size = len(set(values))
    point = image_size == 1
    zero = abs(entropy) <= tolerance
    return TargetEntropyIdentificationAudit(
        n_rows=len(values),
        target_image_size=image_size,
        entropy_bits=entropy,
        point_identified=point,
        entropy_zero=zero,
        equivalence_holds=(point == zero),
    )
