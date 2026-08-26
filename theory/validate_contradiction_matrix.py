from __future__ import annotations

import json
from collections import Counter
from itertools import combinations
from pathlib import Path

from build_contradiction_certificate import render_certificate

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "theory" / "contradiction_matrix.json"

EXPECTED_MODULES = [
    "CREST",
    "CCOC",
    "MLTR",
    "MRM",
    "CED",
    "RACH",
    "EGC",
    "EGW",
    "TU-1",
    "TU-2",
    "TU-3",
    "TU-4",
]
ALLOWED_RELATIONS = {
    "compatible",
    "conditional-on-common-carrier-or-map",
    "orthogonal-estimand",
    "open-bridge",
    "actual-conflict",
}


def main() -> None:
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    assert matrix["schema_version"] == "theouni-pairwise-contradiction-matrix.v0.6-draft"
    assert set(matrix["relation_vocabulary"]) == ALLOWED_RELATIONS

    modules = [item["id"] for item in matrix["modules"]]
    assert modules == EXPECTED_MODULES
    assert len(modules) == len(set(modules))

    for path in matrix["base"].values():
        if path.startswith("theory/"):
            assert (ROOT / path).is_file(), path
    for module in matrix["modules"]:
        assert module["owner"].strip()
        assert module["estimand"].strip()
        assert module["sources"]
        for path in module["sources"]:
            assert (ROOT / path).is_file(), path

    expected_pairs = list(combinations(modules, 2))
    actual_pairs = [(item["left"], item["right"]) for item in matrix["pairs"]]
    assert actual_pairs == expected_pairs, "pairs must be complete, unique, and in module order"

    for item in matrix["pairs"]:
        assert item["relation"] in ALLOWED_RELATIONS
        assert item["rationale"].strip()

    counts = Counter(item["relation"] for item in matrix["pairs"])
    policy = matrix["certificate_policy"]
    assert policy["expected_module_count"] == len(modules) == 12
    assert policy["expected_unordered_pair_count"] == len(actual_pairs) == 66
    assert policy["required_actual_conflict_count"] == 0
    assert counts["actual-conflict"] == policy["required_actual_conflict_count"]
    assert policy["fail_closed"] is True
    assert policy["higher_order_consistency_claimed"] is False
    assert policy["empirical_truth_claimed"] is False

    certificate_path = ROOT / matrix["certificate_document"]
    validator_path = ROOT / matrix["validator"]
    assert certificate_path.is_file()
    assert validator_path.resolve() == Path(__file__).resolve()
    assert certificate_path.read_text(encoding="utf-8") == render_certificate(matrix)

    print(
        "Draft v0.6 contradiction certificate validated: "
        f"{len(modules)} modules, {len(actual_pairs)} unordered pairs, "
        f"relation counts={dict(sorted(counts.items()))}, actual-conflict=0."
    )


if __name__ == "__main__":
    main()
