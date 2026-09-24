#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
READINESS = ROOT / "proposals" / "C2_SEND_READINESS.json"
DISPATCH = ROOT / "proposals" / "C2_DISPATCH_GATE_2026-09-13.json"
REQUEST = ROOT / "proposals" / "C2_OUTSIDE_READER_REQUEST_DRAFT.md"
PACKET = ROOT / "proposals" / "C2_OUTSIDE_READER_PACKET.md"
SEND = ROOT / "proposals" / "C2_TREE_SEND_CANDIDATE.md"
PRESUB = ROOT / "proposals" / "C2_TREE_PRESUBMISSION_EMAIL_DRAFT.md"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    for path in (READINESS, DISPATCH, REQUEST, PACKET, SEND, PRESUB):
        assert path.exists(), path

    readiness = load(READINESS)
    gate = load(DISPATCH)

    assert readiness["status"] == "machine-ready-human-decisions-open"
    assert readiness["machine_checks"]["machine_blockers"] == 0
    assert readiness["machine_checks"]["outside_reader_request_written"] is True
    assert readiness["machine_checks"]["fail_closed_dispatch_gate_written"] is True
    assert readiness["proposal_assets"]["outside_reader_request"] == "proposals/C2_OUTSIDE_READER_REQUEST_DRAFT.md"
    assert readiness["proposal_assets"]["dispatch_gate"] == "proposals/C2_DISPATCH_GATE_2026-09-13.json"

    assert gate["status"] == "not-authorized-to-send"
    assert gate["machine_ready"] is True
    assert gate["machine_blockers"] == 0
    assert gate["current_working_author"] == "Ruiqi Zhang"
    assert gate["current_working_corresponding_author"] == "Ruiqi Zhang"
    assert gate["c1_boundary_state"] == "parked behind C2 editorial outcome"
    assert gate["send_candidate"] == "proposals/C2_TREE_SEND_CANDIDATE.md"

    expected = {"authorship_approval", "outside_reader", "dispatch_time_route_recheck"}
    assert set(gate["gates"]) == expected
    for key in expected:
        row = gate["gates"][key]
        assert row["required"] is True
        assert row["closed"] is False

    assert gate["gates"]["outside_reader"]["request_draft"] == "proposals/C2_OUTSIDE_READER_REQUEST_DRAFT.md"
    assert gate["gates"]["outside_reader"]["reader_packet"] == "proposals/C2_OUTSIDE_READER_PACKET.md"
    assert gate["gates"]["dispatch_time_route_recheck"]["dated_receipt"] == "proposals/C2_TREE_LIVE_ROUTE_CHECK_20260912.md"
    assert gate["gates"]["dispatch_time_route_recheck"]["current_contact_from_receipt"] == "tree@cell.com"
    assert "every required gate has closed=true" in gate["send_rule"]
    assert "Do not reopen Boundary/CED/MROD/REC/TNOA/V3 science" in gate["stop_rule"]

    request = REQUEST.read_text(encoding="utf-8")
    for required in (
        "first concrete reason to reject",
        "local quantities conditioned on earlier measurement choices and losses",
        "prospective intervention-ranking prediction",
        "C2_TREE_SEND_CANDIDATE.md",
        "C2_TREE_EDITOR_PITCH.md",
        "C2_OUTSIDE_READER_PACKET.md",
        "score 9–10",
        "score <=6",
    ):
        assert required.lower() in request.lower()

    packet = PACKET.read_text(encoding="utf-8")
    assert "Maximum = 10" in packet
    assert "9–10" in packet
    assert "7–8" in packet
    assert "≤6" in packet
    assert "Conditional-locality thesis check blocks send" in packet
    assert "Prospective-prediction check blocks send" in packet
    assert "Figure-logic check blocks send" in packet
    assert "When more measurement is not more evidence" in packet
    assert "four failures of monotonic reasoning" not in packet.lower()

    presub = PRESUB.read_text(encoding="utf-8")
    assert "Opinion proposal — When more measurement is not more evidence" in presub
    assert "local quantities conditioned on earlier choices and losses" in presub.lower()
    assert "equal-cost measurement expansions" in presub.lower()
    assert "validated full Opinion draft as a downstream asset" in presub
    assert "four failures of monotonic reasoning" not in presub.lower()

    send = SEND.read_text(encoding="utf-8")
    assert "content-ready, not authorized to send" in send
    assert "When more measurement is not more evidence" in send
    assert "Final authorship approved" in send
    assert "One ecologist outside the immediate theory/methods niche has read the pitch" in send
    assert "Live TREE contact route checked immediately before dispatch" in send

    print("C2_DISPATCH_GATE PASS")


if __name__ == "__main__":
    main()
