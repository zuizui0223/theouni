#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "universe" / "PORTFOLIO_GOVERNANCE_2026-09-11.json"
OVERLAY = ROOT / "universe" / "PORTFOLIO_TARGET_ROUTING_2026-09-13.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    base = load(BASE)
    overlay = load(OVERLAY)

    assert base["status"] == "canonical_portfolio_governance"
    assert overlay["status"] == "canonical_target_routing_overlay"
    assert overlay["base_governance"] == "universe/PORTFOLIO_GOVERNANCE_2026-09-11.json"

    by_id = {row["id"]: row for row in base["paper_units"]}
    assert len(by_id) == 34

    changes = overlay["changes"]
    assert len(changes) == 1
    change = changes[0]
    assert change["paper_id"] == "ADAPTIVE_GAIN"

    base_row = by_id["ADAPTIVE_GAIN"]
    assert base_row["homes"] == ["adaptive-gain"]
    assert base_row["paper_state"] == "SUBMISSION_READY"
    assert base_row["target"] == "Theoretical Ecology"

    assert change["home"] == "adaptive-gain"
    assert change["previous_first_target"] == base_row["target"]
    assert change["first_target"] == "Evolution Letters"
    assert change["submission_sequence"] == [
        "Evolution Letters",
        "The American Naturalist",
        "Theoretical Ecology",
    ]
    assert change["paper_state"] == base_row["paper_state"]
    assert "4a58f485d7a5920f0af62b4847ec2e3f3f340d2b" in change["scientific_trigger"]
    assert "Do not add theorem families" in change["stop_rule"]
    assert "journal-target questions" in overlay["resolution_rule"]

    # Routing overlays may change venue order, not portfolio ontology.
    assert set(by_id) == {row["id"] for row in base["paper_units"]}
    assert base["repositories"]["adaptive-gain"]["paper_units"] == ["ADAPTIVE_GAIN"]

    print("PORTFOLIO_TARGET_ROUTING PASS")


if __name__ == "__main__":
    main()
