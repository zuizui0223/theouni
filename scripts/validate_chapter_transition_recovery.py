from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "thesis" / "transition_recovery_matrix.json"
ARCH = ROOT / "thesis" / "final_chapter_architecture.json"
LEDGER = ROOT / "thesis" / "TRANSITION_RECOVERY_LEDGER.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    matrix = load(MATRIX)
    architecture = load(ARCH)
    ledger = LEDGER.read_text(encoding="utf-8")

    assert matrix["schema_version"] == "theouni-chapter-transition-recovery.v1"
    assert matrix["status"] == "editorial_question_handoffs_verified"
    assert matrix["relation_type"] == "editorial_question_handoff"
    assert len(matrix["relation_firewall"]) >= 4
    assert any("not a theorem implication" in item for item in matrix["relation_firewall"])
    assert any("No transition transfers theorem" in item for item in matrix["relation_firewall"])

    preferred = architecture["preferred_sequence"]
    transitions = matrix["transitions"]
    assert len(preferred) == 10
    assert len(transitions) == 9

    expected_pairs = list(zip(preferred[:-1], preferred[1:]))
    observed_pairs = [(item["from"], item["to"]) for item in transitions]
    assert observed_pairs == expected_pairs

    estimands = []
    for item in transitions:
        for key in (
            "previous_closes",
            "open_question",
            "next_estimand",
            "handoff_reason",
            "forbidden_bridge",
        ):
            assert item[key].strip(), f"{item['from']}->{item['to']} missing {key}"
        assert item["open_question"].strip().endswith("?")
        assert item["forbidden_bridge"].startswith("Do not")
        estimands.append(item["next_estimand"])

    assert len(set(estimands)) == len(estimands), "chapter handoffs collapsed distinct next estimands"

    preconditions = {item["chapter"]: item["condition"] for item in matrix["source_preconditions"]}
    assert set(preconditions) == {"chapter:2", "chapter:3", "chapter:7", "chapter:8"}
    architecture_preconditions = {
        item["chapter"]: item["condition"] for item in architecture["source_preconditions"]
    }
    for text in (preconditions["chapter:2"], architecture_preconditions["chapter:2"]):
        assert "EGWE/parent source contracts" in text
        assert "Chapter 2" in text and "Chapter 4" in text
    assert "MROD" in preconditions["chapter:3"]
    assert "MLTR" in preconditions["chapter:7"]
    assert "CED" in preconditions["chapter:8"]

    # High-risk adjacent pairs must remain explicitly separated by estimand/type.
    by_pair = {(item["from"], item["to"]): item for item in transitions}
    assert "orthogonal" in by_pair[("chapter:1", "chapter:2")]["handoff_reason"]
    assert "different" in by_pair[("chapter:5", "chapter:6")]["handoff_reason"]
    assert "different transports" in by_pair[("chapter:6", "chapter:7")]["handoff_reason"]
    assert "different bottleneck" in by_pair[("chapter:7", "chapter:8")]["handoff_reason"]

    assert "question handoffs" in ledger
    assert "not theorem implications" in ledger
    assert "identification and warning discrimination are orthogonal" in ledger
    assert "CCOC relay is not the proof of the CREST theorem" in ledger
    assert "Replacement histories are not failure domains" in ledger
    assert "write the transition as a question, not an implication" in ledger

    print(
        "Validated 9 editorial question handoffs: sequential chapter order is preserved, "
        "next estimands remain typed and distinct, and source preconditions are local rather than created by editorial order."
    )


if __name__ == "__main__":
    main()
