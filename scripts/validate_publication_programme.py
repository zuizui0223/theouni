#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRAMME = ROOT / "universe" / "PUBLICATION_PROGRAMME_2026-09-11.json"
THESIS = ROOT / "thesis" / "final_chapter_architecture.json"
PROPOSAL = ROOT / "proposals" / "C2_MORE_MEASUREMENT_NOT_MORE_EVIDENCE_TREE_PROPOSAL.md"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    programme = load(PROGRAMME)
    thesis = load(THESIS)

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

    print("PUBLICATION_PROGRAMME PASS")


if __name__ == "__main__":
    main()
