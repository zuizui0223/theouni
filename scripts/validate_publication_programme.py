#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRAMME = ROOT / "universe" / "PUBLICATION_PROGRAMME_2026-09-11.json"
THESIS = ROOT / "thesis" / "final_chapter_architecture.json"
PROPOSAL = ROOT / "proposals" / "C2_MORE_MEASUREMENT_NOT_MORE_EVIDENCE_TREE_PROPOSAL.md"
C2_LEDGER = ROOT / "proposals" / "C2_SOURCE_LEDGER.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _assert_blob_pin(value: str) -> None:
    assert isinstance(value, str)
    assert len(value) == 40
    int(value, 16)


def main() -> None:
    programme = load(PROGRAMME)
    thesis = load(THESIS)
    ledger = load(C2_LEDGER)

    assert programme["status"] == "canonical_publication_programme"
    assert programme["governance"]["thesis_architecture"] == "thesis/final_chapter_architecture.json"
    assert thesis["status"] == "final_editorial_order_forbidden_inference_spine"
    assert len(thesis["chapters"]) == 10

    portfolio = programme["portfolio"]
    assert portfolio["confirmed_submission_units"] == 5
    assert portfolio["conditional_submission_units"] == 1
    assert portfolio["maximum_submission_units"] == 6

    concept = {row["id"]: row for row in programme["concept_track"]}
    methods = {row["id"]: row for row in programme["method_track"]}
    assert set(concept) == {"C1", "C2"}
    assert set(methods) == {"M1", "M2", "M3", "M4"}
    assert concept["C2"]["status"] == "primary_concept_pitch"
    assert concept["C1"]["status"] == "proposal_ready_parked_conditional"
    assert len(concept["C2"]["four_failures"]) == 4
    assert [row["id"] for row in concept["C2"]["four_failures"]] == [
        "geometry",
        "objective",
        "dependence",
        "pipeline",
    ]
    assert PROPOSAL.exists()

    assert methods["M1"]["repository"] == "zuizui0223/tnoa"
    assert methods["M2"]["repository"] == "zuizui0223/mrod"
    assert methods["M3"]["repository"] == "zuizui0223/ced"
    assert methods["M4"]["repositories"] == ["zuizui0223/v3", "zuizui0223/rec"]
    assert "TNOA is excluded" in methods["M4"]["firewall"]

    superseded = set(programme["governance"]["superseded_publication_plans"])
    assert superseded == {
        "universe/SUBMISSION_ARCHITECTURE_2026-09-08.md",
        "universe/TWO_PAPER_EXECUTION_STATUS_2026-09-08.md",
    }

    assert ledger["status"] == "proposal-source-pins"
    assert ledger["proposal"] == concept["C2"]["proposal"]
    assert set(ledger["failure_classes"]) == {
        "geometry",
        "objective",
        "dependence",
        "pipeline_rec",
        "pipeline_tnoa",
    }
    assert set(ledger["worked_examples"]) == {
        "campanula_izu",
        "example_status_registry",
        "island_pollination_translation",
    }
    for row in list(ledger["failure_classes"].values()) + list(ledger["worked_examples"].values()):
        _assert_blob_pin(row["source_blob_sha1"])
        assert row.get("claim_ceiling")

    objective = ledger["failure_classes"]["objective"]["anchors"]
    assert objective["nuisance_detail_mechanism_information_bits"] == 2.0
    assert objective["nuisance_detail_target_resolution_probability"] == 0.0
    assert objective["target_split_mechanism_information_bits"] == 1.0
    assert objective["target_split_target_resolution_probability"] == 1.0

    birdvox = ledger["failure_classes"]["pipeline_rec"]["anchors"]
    assert birdvox["truth_late_minus_early"] > 0.13
    assert abs(birdvox["oracle_downstream_true_entry_late_minus_early"]) < 0.001

    tnoa = ledger["failure_classes"]["pipeline_tnoa"]["anchors"]
    assert tnoa["inherited_raw_threshold"] == 0.55
    assert tnoa["nuisance_recall_after_representation_change"] == 0.23125

    print("PUBLICATION_PROGRAMME PASS")


if __name__ == "__main__":
    main()
