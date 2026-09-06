from __future__ import annotations

from itertools import product

from target_entropy_identification_bridge import audit_target_entropy_identification


def main() -> None:
    audited = 0
    for alphabet_size in (2, 3):
        alphabet = tuple(range(alphabet_size))
        for n in range(1, 7):
            for values in product(alphabet, repeat=n):
                audit = audit_target_entropy_identification(values)
                assert audit.equivalence_holds
                assert audit.point_identified == (len(set(values)) == 1)
                audited += 1

    # Positive unequal weights do not change the zero-entropy/singleton equivalence.
    weighted_singleton = audit_target_entropy_identification(
        ("same", "same", "same"),
        weights=(0.1, 2.0, 7.0),
    )
    assert weighted_singleton.point_identified
    assert weighted_singleton.entropy_zero

    weighted_multiple = audit_target_entropy_identification(
        ("a", "a", "b"),
        weights=(100.0, 1.0, 0.001),
    )
    assert not weighted_multiple.point_identified
    assert not weighted_multiple.entropy_zero

    print(
        f"target entropy-identification bridge verified on {audited} finite supports "
        "plus unequal positive-weight witnesses"
    )


if __name__ == "__main__":
    main()
