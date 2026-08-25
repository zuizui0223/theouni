from __future__ import annotations

from dataclasses import dataclass
from math import ceil, log2
from typing import Hashable, Iterable, Mapping, Sequence

World = Hashable
Partition = Sequence[Sequence[World]]


def _block_index(partition: Partition) -> dict[World, int]:
    out: dict[World, int] = {}
    for block_id, block in enumerate(partition):
        for world in block:
            if world in out:
                raise ValueError(f"world appears in multiple blocks: {world!r}")
            out[world] = block_id
    return out


def _carrier(partition: Partition) -> set[World]:
    return set(_block_index(partition))


def validate_same_carrier(old: Partition, new: Partition) -> None:
    old_carrier = _carrier(old)
    new_carrier = _carrier(new)
    if old_carrier != new_carrier:
        raise ValueError("TU-1 v1 requires old and new partitions on the same finite carrier")
    if not old_carrier:
        raise ValueError("carrier must be non-empty")


def split_multiplicities(old: Partition, new: Partition) -> tuple[int, ...]:
    """Number of revised-state blocks intersecting each old-state block."""
    validate_same_carrier(old, new)
    new_index = _block_index(new)
    return tuple(len({new_index[w] for w in block}) for block in old)


def state_only_revisable(old: Partition, new: Partition) -> bool:
    """Whether the new state factors through the old state label alone."""
    return max(split_multiplicities(old, new)) == 1


def revision_alphabet_size(old: Partition, new: Partition) -> int:
    """Exact minimum auxiliary alphabet size for deterministic exact revision."""
    return max(split_multiplicities(old, new))


def revision_debt_bits(old: Partition, new: Partition, *, fixed_length: bool = False) -> float | int:
    k = revision_alphabet_size(old, new)
    if fixed_length:
        return ceil(log2(k))
    return log2(k)


def common_refinement_size(old: Partition, new: Partition) -> int:
    """Number of non-empty intersections of old and new blocks."""
    return sum(split_multiplicities(old, new))


def average_refinement_debt_bits(old: Partition, new: Partition) -> float:
    validate_same_carrier(old, new)
    return log2(common_refinement_size(old, new)) - log2(len(old))


def build_minimal_revision_code(old: Partition, new: Partition) -> dict[World, int]:
    """Construct a revision-sufficient code using exactly K_rev labels.

    Labels are reusable across old-state blocks because the decoder also knows
    the old-state label.
    """
    validate_same_carrier(old, new)
    new_index = _block_index(new)
    code: dict[World, int] = {}
    for block in old:
        target_ids = sorted({new_index[w] for w in block})
        local_code = {target_id: label for label, target_id in enumerate(target_ids)}
        for world in block:
            code[world] = local_code[new_index[world]]
    return code


def code_is_revision_sufficient(
    old: Partition,
    new: Partition,
    code: Mapping[World, Hashable],
) -> bool:
    """Check whether (old-state block, code label) determines new-state block."""
    validate_same_carrier(old, new)
    old_index = _block_index(old)
    new_index = _block_index(new)
    seen: dict[tuple[int, Hashable], int] = {}
    for world in old_index:
        if world not in code:
            return False
        key = (old_index[world], code[world])
        target = new_index[world]
        if key in seen and seen[key] != target:
            return False
        seen[key] = target
    return True


@dataclass(frozen=True)
class RevisionAudit:
    split_multiplicities: tuple[int, ...]
    state_only_revisable: bool
    minimum_auxiliary_alphabet: int
    ideal_revision_debt_bits: float
    fixed_length_revision_bits: int
    average_refinement_debt_bits: float


def audit_revision(old: Partition, new: Partition) -> RevisionAudit:
    splits = split_multiplicities(old, new)
    k = max(splits)
    return RevisionAudit(
        split_multiplicities=splits,
        state_only_revisable=(k == 1),
        minimum_auxiliary_alphabet=k,
        ideal_revision_debt_bits=log2(k),
        fixed_length_revision_bits=ceil(log2(k)),
        average_refinement_debt_bits=average_refinement_debt_bits(old, new),
    )
