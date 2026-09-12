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
PROPAGATION = ROOT / "universe" / "HUMAN_INPUT_PROPAGATION_MAP_2026-09-12.json"


def main() -> None:
    for path in (HANDOFF_JSON, HANDOFF_MD, LIVE_RULES, HUMAN_JSON, HUMAN_MD, PROPAGATION):
        assert path.exists(), path

    handoff = json.loads(HANDOFF_JSON.read_text(encoding="utf-8"))
    human = json.loads(HUMAN_JSON.read_text(encoding="utf-8"))
    propagation = json.loads(PROPAGATION.read_text(encoding="utf-8"))

    assert handoff["status"] == "machine-work-closed-human-completion-open"
    assert handoff["scope"] == "observation_evidence_track_only"
    assert handoff["live_rules"] == "universe/LIVE_JOURNAL_RULES_2026-09-12.md"
    assert handoff["human_input_ledger"] == "universe/HUMAN_SUBMISSION_INPUTS_2026-09-12.json"

    units = handoff["units"]
    assert set(units) == {"C1", "C2", "M1", "M2", "M3", "M4"}

    c1 = units["C1"]
    assert c1["state"] == "machine-ready-strategically-parked"
    assert c1["repository"] == "zuizui0223/boundary"
    assert c1["role_contract"] == "zuizui0223/boundary/paper/BOUNDARY_ROLE_CONTRACT_2026-09-12.json"
    assert c1["send_readiness"] == "zuizui0223/boundary/paper/C1_SEND_READINESS_2026-09-12.json"
    assert c1["exclusive_owner"] == "structural identification geometry"
    assert "qualitative geometry exemplar only" in c1["c2_role"]
    assert "exact theorem surface stays in Boundary" in c1["c2_role"]
    assert "external identification-geometry" in c1["ced_role"]
    assert c1["machine_blocker"] is False
    assert c1["proposal_max_words"] == 300
    assert c1["proposal_word_count"] == 226
    assert c1["proposal_word_headroom"] == 74
    assert c1["current_strategy_decision"] == "keep parked until C2 editorial outcome"
    assert c1["current_human_blockers"] == []
    assert set(c1["human_gates_if_activated"]) == {
        "authorship",
        "author qualification",
        "contact metadata",
        "live rule recheck",
    }
    assert "C2 is declined/too broad" in c1["activation_gate"]

    assert units["C2"]["machine_state"] == "ready"
    assert units["C2"]["sent"] is False
    assert units["C2"]["live_route_verified_on"] == "2026-09-12"
    assert units["C2"]["current_live_contact"] == "tree@cell.com"
    assert units["C2"]["current_live_editor"] == "Andrea Stephens"
    assert "proposal by email" in units["C2"]["current_public_route"]
    assert set(units["C2"]["human_gates"]) == {
        "authorship approval",
        "broad-interest outside read",
        "dispatch-time route recheck",
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
    assert human["papers"]["C1"]["activation_decision"] == "keep parked until C2 editorial outcome"
    assert human["papers"]["M4"]["raw_findlay_redistribution_allowed"] is False

    assert propagation["source"] == "universe/HUMAN_SUBMISSION_INPUTS_2026-09-12.json"
    assert set(propagation["destinations"]) == {"C2", "M1", "M2", "M3", "M4"}
    blocked = set(propagation["blocked_automatic_actions"])
    assert "copy MROD affiliation into another paper without confirmation" in blocked
    assert "derive authorship from Git commits or repository ownership" in blocked
    assert "guess ChatGPT application/model versions from repository dates or assistant model identity" in blocked
    assert "mark a visual inspection complete without human review" in blocked

    text = HANDOFF_MD.read_text(encoding="utf-8")
    for required in (
        "science and machine production closed for M1–M4",
        "C1 — Boundary / Ecology Letters Perspective",
        "Boundary is **not archived material and is not absorbed into C2 or CED**",
        "BOUNDARY_ROLE_CONTRACT_2026-09-12.json",
        "qualitative geometry exemplar only",
        "keep C1 parked until the C2 editorial outcome",
        "There is no theorem-ownership transfer",
        "human metadata, visual review and dispatch decisions",
        "Do not reopen frozen science or transfer Boundary theorem ownership",
        "HUMAN_SUBMISSION_INPUTS_2026-09-12",
    ):
        assert required in text

    print("PUBLICATION_HANDOFF PASS")


if __name__ == "__main__":
    main()
