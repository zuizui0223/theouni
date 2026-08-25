from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Hashable, Mapping


World = Hashable
Signature = Hashable


def partition_by_signature(signatures: Mapping[World, Signature]) -> tuple[frozenset[World], ...]:
    if not signatures:
        raise ValueError("signature map must be non-empty")
    groups: dict[Signature, set[World]] = defaultdict(set)
    for world, signature in signatures.items():
        groups[signature].add(world)
    return tuple(
        sorted(
            (frozenset(block) for block in groups.values()),
            key=lambda block: repr(sorted(map(repr, block))),
        )
    )


def validate_surjective_projection(
    projection: Mapping[World, World],
    source_signatures: Mapping[World, Signature],
    target_worlds: set[World],
) -> None:
    if set(projection) != set(source_signatures):
        raise ValueError("projection domain must equal the richer/source carrier")
    if set(projection.values()) != set(target_worlds):
        raise ValueError("projection must be surjective onto the target/base carrier")


def fibers(
    projection: Mapping[World, World],
) -> dict[World, frozenset[World]]:
    out: dict[World, set[World]] = defaultdict(set)
    for source, target in projection.items():
        out[target].add(source)
    return {target: frozenset(source_set) for target, source_set in out.items()}


def fibers_are_signature_homogeneous(
    projection: Mapping[World, World],
    source_signatures: Mapping[World, Signature],
) -> bool:
    if set(projection) != set(source_signatures):
        raise ValueError("projection and signature domains must match")
    for source_set in fibers(projection).values():
        if len({source_signatures[source] for source in source_set}) != 1:
            return False
    return True


def induced_base_signatures(
    projection: Mapping[World, World],
    source_signatures: Mapping[World, Signature],
) -> dict[World, Signature]:
    """Factor richer/source loss signatures through a surjective projection.

    Raises ValueError exactly when a projection fiber contains different loss
    response signatures, i.e. when the proposed omitted coordinate is target-relevant.
    """
    if set(projection) != set(source_signatures):
        raise ValueError("projection and signature domains must match")
    if not fibers_are_signature_homogeneous(projection, source_signatures):
        raise ValueError("loss response does not factor through the proposed projection")

    result: dict[World, Signature] = {}
    for base, source_set in fibers(projection).items():
        source = next(iter(source_set))
        result[base] = source_signatures[source]
    return result


def projection_is_loss_faithful(
    projection: Mapping[World, World],
    richer_signatures: Mapping[World, Signature],
    base_signatures: Mapping[World, Signature],
) -> bool:
    validate_surjective_projection(projection, richer_signatures, set(base_signatures))
    return all(
        richer_signatures[source] == base_signatures[target]
        for source, target in projection.items()
    )


def quotient_signature_set(signatures: Mapping[World, Signature]) -> frozenset[Signature]:
    return frozenset(signatures.values())


@dataclass(frozen=True)
class RepresentationAudit:
    richer_world_count: int
    base_world_count: int
    richer_loss_state_count: int
    base_loss_state_count: int
    projection_surjective: bool
    fiber_homogeneous: bool
    loss_faithful: bool
    quotient_signature_sets_equal: bool


def audit_representation(
    projection: Mapping[World, World],
    richer_signatures: Mapping[World, Signature],
    base_signatures: Mapping[World, Signature],
) -> RepresentationAudit:
    projection_surjective = (
        set(projection) == set(richer_signatures)
        and set(projection.values()) == set(base_signatures)
    )
    homogeneous = fibers_are_signature_homogeneous(projection, richer_signatures)
    faithful = False
    if projection_surjective:
        faithful = projection_is_loss_faithful(
            projection, richer_signatures, base_signatures
        )

    richer_states = quotient_signature_set(richer_signatures)
    base_states = quotient_signature_set(base_signatures)
    return RepresentationAudit(
        richer_world_count=len(richer_signatures),
        base_world_count=len(base_signatures),
        richer_loss_state_count=len(richer_states),
        base_loss_state_count=len(base_states),
        projection_surjective=projection_surjective,
        fiber_homogeneous=homogeneous,
        loss_faithful=faithful,
        quotient_signature_sets_equal=(richer_states == base_states),
    )


def nuisance_inflation_family(
    base_signatures: Mapping[World, Signature],
    m: int,
) -> tuple[dict[tuple[World, int], World], dict[tuple[World, int], Signature]]:
    if m < 1:
        raise ValueError("m must be >= 1")
    projection: dict[tuple[World, int], World] = {}
    richer: dict[tuple[World, int], Signature] = {}
    for base_world, signature in base_signatures.items():
        for nuisance in range(2**m):
            richer_world = (base_world, nuisance)
            projection[richer_world] = base_world
            richer[richer_world] = signature
    return projection, richer
