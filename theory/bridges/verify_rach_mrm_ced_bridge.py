from __future__ import annotations

from collections import defaultdict


PROGRAMMES = ("m1", "m2", "m3", "m4")
RESPONSE = {
    "m1": "R0",
    "m2": "R0",
    "m3": "R1",
    "m4": "R1",
}
TARGET = {
    "m1": 0,
    "m2": 0,
    "m3": 1,
    "m4": 1,
}


def classes(mapping: dict[str, object]) -> list[set[str]]:
    grouped: dict[object, set[str]] = defaultdict(set)
    for item, label in mapping.items():
        grouped[label].add(item)
    return list(grouped.values())


def constant_on(block: set[str], mapping: dict[str, object]) -> bool:
    return len({mapping[item] for item in block}) <= 1


def verify_response_class_is_enough() -> None:
    evidence = classes(RESPONSE)
    assert {frozenset(x) for x in evidence} == {
        frozenset({"m1", "m2"}),
        frozenset({"m3", "m4"}),
    }
    for block in evidence:
        assert len(block) == 2  # causal multiplicity remains
        assert constant_on(block, RESPONSE)
        assert constant_on(block, TARGET)


def verify_uninformative_evidence_requires_ambiguity() -> None:
    block = set(PROGRAMMES)
    assert not constant_on(block, RESPONSE)
    assert not constant_on(block, TARGET)
    assert {TARGET[item] for item in block} == {0, 1}


def verify_causal_singleton_not_required() -> None:
    block = {"m1", "m2"}
    assert len(block) > 1
    assert constant_on(block, RESPONSE)
    assert constant_on(block, TARGET)


def verify_target_can_be_coarser_than_response() -> None:
    response = {
        "m1": "R0a",
        "m2": "R0b",
        "m3": "R1",
        "m4": "R1",
    }
    target = TARGET
    block = {"m1", "m2"}
    assert not constant_on(block, response)
    assert constant_on(block, target)


def main() -> None:
    verify_response_class_is_enough()
    verify_uninformative_evidence_requires_ambiguity()
    verify_causal_singleton_not_required()
    verify_target_can_be_coarser_than_response()
    print(
        "Positive RACH->MRM->CED bridge verified: causal multiplicity may remain while "
        "response/target reporting is deterministic, and evidence need only resolve "
        "report-relevant disagreement."
    )


if __name__ == "__main__":
    main()
