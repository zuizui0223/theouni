#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HANDOFF_JSON = ROOT / "universe" / "PUBLICATION_HANDOFF_2026-09-12.json"
HANDOFF_MD = ROOT / "universe" / "PUBLICATION_HANDOFF_2026-09-12.md"
LIVE_RULES = ROOT / "universe" / "LIVE_JOURNAL_RULES_2026-09-12.md"
HUMAN_JSON = ROOT / "universe" / "HUMAN_SUBMISSION_INPUTS_2026-09-12.json"
HUMAN_MD = ROOT / "universe" / "HUMAN_SUBMISSION_INPUTS_2026-09-12.md"


def main() -> None:
    for path in (HANDOFF_JSON, HANDOFF_MD, LIVE_RULES, HUMAN_JSON, HUMAN_MD):
        assert path.exists(), path

    handoff = json.loads(HANDOFF_JSON.read_text(encoding="utf-8"))
    human = json.loads(HUMAN_JSON.read_text(encoding="utf-8"))

    assert handoff["status"] == "machine-work-closed-human-completion-open"
    assert handoff["scope"] == "observation_evidence_track_only"
    assert handoff["live_rules"] == "universe/LIVE_JOURNAL_RULES_2026-09-12.md"
    assert handoff["human_input_ledger"] == "universe/HUMAN_SUBMISSION_INPUTS_2026-09-12.json"

    units = handoff["units"]
    assert set(units) == {"C1", "C2", "M1", "M2", "M3", "M4"}
    assert units["C1"]["state"] == "parked-conditional"
    assert units["C2"]["machine_state"] == "ready"
    assert units["C2"]["sent"] is False
    assert set(units["C2"]["human_gates"]) == {
        "authorship approval",
        "broad-interest outside read",
        "live contact route check",
    }

    for paper in ("M1", "M2", "M3", "M4"):
        assert units[paper]["science_blocker"] is False
        assert units[paper]["machine_production_blocker"] is False
        assert units[paper]["remaining_class"].startswith("human-")

    assert units["M3"]["citation_missing"] == 0
    assert units["M3"]["citation_unused"] == 0
    assert units["M4"]["findlay_raw_csv_redistribution_allowed"] is False
    assert "Do not reopen frozen science" in handoff["stop_rule"]

    assert human["status"] == "human-input-open-machine-work-closed"
    assert human["working_author_record"]["department_or_unit"] is None
    assert human["working_author_record"]["correspondence_email"] is None
    assert human["working_author_record"]["orcid"] is None
    assert human["ai_assistance"]["exact_application_model_versions"] is None
    assert human["ai_assistance"]["do_not_infer_from_repository_history"] is True
    assert human["papers"]["C1"]["human_metadata_effort_now"] is False
    assert human["papers"]["M4"]["raw_findlay_redistribution_allowed"] is False

    text = HANDOFF_MD.read_text(encoding="utf-8")
    for required in (
        "science and machine production closed for M1–M4",
        "human metadata, visual review and dispatch decisions",
        "Do not reopen frozen science",
        "HUMAN_SUBMISSION_INPUTS_2026-09-12",
    ):
        assert required in text

    print("PUBLICATION_HANDOFF PASS")


if __name__ == "__main__":
    main()
