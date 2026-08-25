from __future__ import annotations

from warning_state_portability import (
    audit_warning_state,
    induced_warning_on_loss_states,
    warning_portable_on_loss_states,
)


def main() -> None:
    # TU-4A equality case: warning is homogeneous inside loss-state classes.
    loss = {
        "a0": "persist",
        "a1": "persist",
        "b0": "loss@10",
        "b1": "loss@10",
    }
    warning_homogeneous = {
        "a0": "no-loss/no-warning",
        "a1": "no-loss/no-warning",
        "b0": "lead",
        "b1": "lead",
    }
    same = audit_warning_state(loss, warning_homogeneous)
    assert same.warning_factors_through_loss_state
    assert same.warning_state_equals_loss_state
    assert same.loss_state_count == same.warning_evaluation_state_count == 2

    # TU-4B: same loss state, opposite warning ordering -> strict refinement.
    warning_split = dict(warning_homogeneous)
    warning_split["b1"] = "lag"
    split = audit_warning_state(loss, warning_split)
    assert not split.warning_factors_through_loss_state
    assert not split.warning_state_equals_loss_state
    assert split.loss_state_count == 2
    assert split.warning_evaluation_state_count == 3

    # TU-4C: portability iff warning signatures commute with loss-state map.
    warning_a = induced_warning_on_loss_states(loss, warning_homogeneous)
    loss_b = {
        "x0": "survive",
        "x1": "survive",
        "y0": "fail@10",
        "y1": "fail@10",
    }
    warning_b_ok = {
        "x0": "no-loss/no-warning",
        "x1": "no-loss/no-warning",
        "y0": "lead",
        "y1": "lead",
    }
    warning_b_bad = dict(warning_b_ok)
    warning_b_bad["y0"] = "lag"
    warning_b_bad["y1"] = "lag"

    warning_b_ok_state = induced_warning_on_loss_states(loss_b, warning_b_ok)
    warning_b_bad_state = induced_warning_on_loss_states(loss_b, warning_b_bad)
    h = {"survive": "persist", "fail@10": "loss@10"}
    assert warning_portable_on_loss_states(h, warning_a, warning_b_ok_state)
    assert not warning_portable_on_loss_states(h, warning_a, warning_b_bad_state)

    print(
        "TU-4 verified: warning-state equality criterion, strict refinement, "
        "and positive/negative portability across matched loss states."
    )


if __name__ == "__main__":
    main()
