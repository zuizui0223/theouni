from __future__ import annotations

from learning_licensing import audit_experiment


def main() -> None:
    for m in range(1, 9):
        for k in range(m + 1):
            no_target = audit_experiment(m, k, False)
            with_target = audit_experiment(m, k, True)

            # TU-2A: same causal information, opposite target licensing.
            assert no_target.causal_information_bits == with_target.causal_information_bits == float(k)
            assert no_target.normalized_causal_nov == with_target.normalized_causal_nov == k / m
            assert no_target.target_licensed_every_record is False
            assert with_target.target_licensed_every_record is True

        # TU-2B: maximal causal learning, zero target licensing.
        causal = audit_experiment(m, m, False)
        assert causal.normalized_causal_nov == 1.0
        assert causal.target_licensed_every_record is False

        # TU-2C: zero causal learning, complete target licensing.
        target = audit_experiment(m, 0, True)
        assert target.normalized_causal_nov == 0.0
        assert target.target_licensed_every_record is True

        # Equal-cost policy reversal between causal-learning and target-licensing objectives.
        assert causal.normalized_causal_nov > target.normalized_causal_nov
        assert int(causal.target_licensed_every_record) < int(target.target_licensed_every_record)

    print(
        "TU-2 verified for m=1..8: score-matched opposite licensing, "
        "max-learning/no-license, zero-learning/full-license, and policy reversal."
    )


if __name__ == "__main__":
    main()
