from __future__ import annotations

from evidence_admissible_transition import audit_evidence_admissible_transition


def main() -> None:
    same_target_worlds = (
        (("mechanism-A", 0), "positive"),
        (("mechanism-B", 1), "positive"),
    )
    mixed_target_worlds = (
        (("mechanism-A", 0), "positive"),
        (("mechanism-B", 1), "negative"),
    )
    target = lambda world: world[1]

    admissible = audit_evidence_admissible_transition(
        same_target_worlds,
        target=target,
        proposed_value="positive",
        reliability_satisfied=True,
    )
    assert admissible.compatible_world_count == 2
    assert admissible.target_point_identified
    assert admissible.admissible

    unreliable = audit_evidence_admissible_transition(
        same_target_worlds,
        target=target,
        proposed_value="positive",
        reliability_satisfied=False,
    )
    assert unreliable.target_point_identified
    assert not unreliable.admissible
    assert unreliable.reason == "reliability_requirement_not_satisfied"

    unresolved = audit_evidence_admissible_transition(
        mixed_target_worlds,
        target=target,
        proposed_value="positive",
        reliability_satisfied=True,
    )
    assert not unresolved.target_point_identified
    assert not unresolved.admissible
    assert unresolved.reason == "target_not_point_identified"

    wrong_proposal = audit_evidence_admissible_transition(
        same_target_worlds,
        target=target,
        proposed_value="negative",
        reliability_satisfied=True,
    )
    assert not wrong_proposal.admissible
    assert wrong_proposal.reason == "proposal_disagrees_with_identified_target"

    print(
        "Evidence-admissible transition witness verified: mechanism multiplicity "
        "can coexist with target identification, but reliability failure, target "
        "multiplicity, or proposal mismatch each withhold the transition."
    )


if __name__ == "__main__":
    main()
