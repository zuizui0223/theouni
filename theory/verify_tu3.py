from __future__ import annotations

from loss_state_invariance import (
    audit_representation,
    fibers_are_signature_homogeneous,
    induced_base_signatures,
    nuisance_inflation_family,
    projection_is_loss_faithful,
    quotient_signature_set,
)


def main() -> None:
    base = {
        "a": "persist",
        "b": "early_loss",
        "c": "late_loss",
        "d": "persist",
    }
    base_state_count = len(quotient_signature_set(base))
    assert base_state_count == 3

    # TU-3A/C: arbitrary nuisance inflation leaves loss-state quotient unchanged.
    for m in range(1, 9):
        projection, richer = nuisance_inflation_family(base, m)
        assert len(richer) == len(base) * (2**m)
        assert fibers_are_signature_homogeneous(projection, richer)
        assert induced_base_signatures(projection, richer) == base
        assert projection_is_loss_faithful(projection, richer, base)
        audit = audit_representation(projection, richer, base)
        assert audit.loss_faithful
        assert audit.richer_loss_state_count == audit.base_loss_state_count == base_state_count
        assert audit.quotient_signature_sets_equal

    # TU-3B/D: a hidden target-relevant coordinate breaks factorization.
    projection, richer = nuisance_inflation_family(base, 1)
    richer[("b", 1)] = "catastrophic_loss"
    assert not fibers_are_signature_homogeneous(projection, richer)
    try:
        induced_base_signatures(projection, richer)
    except ValueError:
        pass
    else:
        raise AssertionError("inhomogeneous fiber must reject induced base signature")

    assert not projection_is_loss_faithful(projection, richer, base)
    broken = audit_representation(projection, richer, base)
    assert broken.richer_loss_state_count == base_state_count + 1
    assert broken.base_loss_state_count == base_state_count
    assert not broken.loss_faithful
    assert not broken.quotient_signature_sets_equal

    print(
        "TU-3 verified: quotient invariance under nuisance inflation m=1..8 "
        "and failure under one hidden loss-relevant coordinate."
    )


if __name__ == "__main__":
    main()
