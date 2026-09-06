from __future__ import annotations

from itertools import product
from math import log2

from target_entropy_identification_bridge import audit_target_entropy_identification


def main() -> None:
    audited = 0
    for alphabet_size in (2, 3):
        alphabet = tuple(range(alphabet_size))
        for n in range(1, 7):
            for values in product(alphabet, repeat=n):
                audit = audit_target_entropy_identification(values)
                assert audit.equivalence_holds
                assert audit.cardinality_entropy_bound_holds
                assert audit.point_identified == (len(set(values)) == 1)
                assert 1.0 - 1e-12 <= audit.effective_target_count <= audit.target_image_size + 1e-12
                audited += 1

    weighted_singleton = audit_target_entropy_identification(
        ("same", "same", "same"),
        weights=(0.1, 2.0, 7.0),
    )
    assert weighted_singleton.point_identified
    assert weighted_singleton.entropy_zero
    assert weighted_singleton.effective_target_count == 1.0

    weighted_multiple = audit_target_entropy_identification(
        ("a", "a", "b"),
        weights=(100.0, 1.0, 0.001),
    )
    assert not weighted_multiple.point_identified
    assert not weighted_multiple.entropy_zero
    assert 1.0 < weighted_multiple.effective_target_count < 2.0

    # Equal total mass on three target values reaches the cardinality bound even
    # when row multiplicities differ before weighting.
    uniform_target_mass = audit_target_entropy_identification(
        ("a", "a", "b", "c"),
        weights=(0.5, 0.5, 1.0, 1.0),
    )
    assert uniform_target_mass.target_image_size == 3
    assert abs(uniform_target_mass.entropy_bits - log2(3.0)) < 1e-12
    assert abs(uniform_target_mass.effective_target_count - 3.0) < 1e-12
    assert abs(uniform_target_mass.effective_to_image_ratio - 1.0) < 1e-12

    print(
        f"target entropy-identification bridge verified on {audited} finite supports "
        "plus weighted singleton, skewed-multiple, and uniform-target-mass witnesses"
    )


if __name__ == "__main__":
    main()
