from __future__ import annotations

from math import log2

from contract_revision import (
    audit_revision,
    build_minimal_revision_code,
    code_is_revision_sufficient,
    revision_alphabet_size,
    state_only_revisable,
)


def divergence_family(m: int, n_old_blocks: int):
    """One old block splits into 2**m revised blocks; all others stay unsplit."""
    k = 2**m
    exceptional = tuple(range(k))
    old = [exceptional]
    new = [(i,) for i in range(k)]

    start = k
    for j in range(n_old_blocks - 1):
        world = start + j
        old.append((world,))
        new.append((world,))
    return tuple(old), tuple(new)


def main() -> None:
    # TU-1A: exact state-only factorization boundary.
    old = ((0, 1), (2, 3))
    coarser_new = ((0, 1, 2, 3),)
    finer_new = ((0,), (1,), (2, 3))
    assert state_only_revisable(old, coarser_new)
    assert not state_only_revisable(old, finer_new)

    # TU-1B: exact auxiliary alphabet and constructive sufficiency.
    audit = audit_revision(old, finer_new)
    assert audit.split_multiplicities == (2, 1)
    assert audit.minimum_auxiliary_alphabet == 2
    assert audit.ideal_revision_debt_bits == 1.0
    code = build_minimal_revision_code(old, finer_new)
    assert len(set(code.values())) == revision_alphabet_size(old, finer_new)
    assert code_is_revision_sufficient(old, finer_new, code)

    # TU-1D: average debt <= worst-case revision debt.
    assert audit.average_refinement_debt_bits <= audit.ideal_revision_debt_bits

    # Equality when every old block has the same split multiplicity.
    balanced_old = ((0, 1), (2, 3))
    balanced_new = ((0,), (1,), (2,), (3,))
    balanced = audit_revision(balanced_old, balanced_new)
    assert balanced.average_refinement_debt_bits == balanced.ideal_revision_debt_bits == 1.0

    # TU-1E: m bits of worst-case revision debt with arbitrarily small average debt.
    epsilon = 0.01
    for m in range(1, 9):
        k = 2**m
        # Sufficient strict choice from N > (2^m - 1)/(2^epsilon - 1).
        n = int((k - 1) / (2**epsilon - 1)) + 2
        p, q = divergence_family(m, n)
        result = audit_revision(p, q)
        assert result.ideal_revision_debt_bits == float(m)
        assert result.average_refinement_debt_bits < epsilon
        minimal_code = build_minimal_revision_code(p, q)
        assert code_is_revision_sufficient(p, q, minimal_code)
        assert len(set(minimal_code.values())) == k

    print(
        "TU-1 verified: factorization boundary, exact auxiliary alphabet, "
        "average<=worst debt, balanced equality, and divergence family m=1..8."
    )


if __name__ == "__main__":
    main()
