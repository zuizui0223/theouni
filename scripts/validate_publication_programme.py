#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROGRAMME = ROOT / "universe" / "PUBLICATION_PROGRAMME_2026-09-11.json"
PORTFOLIO = ROOT / "universe" / "PORTFOLIO_GOVERNANCE_2026-09-11.json"
THESIS = ROOT / "thesis" / "final_chapter_architecture.json"
LIVE_RULES = ROOT / "universe" / "LIVE_JOURNAL_RULES_2026-09-12.md"
PROPOSAL = ROOT / "proposals" / "C2_MORE_MEASUREMENT_NOT_MORE_EVIDENCE_TREE_PROPOSAL.md"
C2_LEDGER = ROOT / "proposals" / "C2_SOURCE_LEDGER.json"
C2_PRIOR_ART = ROOT / "proposals" / "C2_PRIOR_ART_MAP.md"
C2_EDITOR_PITCH = ROOT / "proposals" / "C2_TREE_EDITOR_PITCH.md"
C2_AUTHORSHIP = ROOT / "proposals" / "C2_AUTHORSHIP_LEDGER.json"
C2_SEND_READINESS = ROOT / "proposals" / "C2_SEND_READINESS.json"
C2_AUTHOR_METADATA = ROOT / "proposals" / "C2_TREE_AUTHOR_METADATA_TEMPLATE.md"
C2_SEND_CANDIDATE = ROOT / "proposals" / "C2_TREE_SEND_CANDIDATE.md"
C2_OUTSIDE_READER = ROOT / "proposals" / "C2_OUTSIDE_READER_PACKET.md"
C2_RED_TEAM = ROOT / "proposals" / "C2_TREE_RED_TEAM.md"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _assert_blob_pin(value: str) -> None:
    assert isinstance(value, str)
    assert len(value) == 40
    int(value, 16)


def _assert_any(text: str, *aliases: str) -> None:
    lower = text.lower()
    assert any(alias.lower() in lower for alias in aliases), aliases


def main() -> None:
    programme = load(PROGRAMME)
    portfolio_governance = load(PORTFOLIO)
    thesis = load(THESIS)
    ledger = load(C2_LEDGER)
    authorship = load(C2_AUTHORSHIP)
    readiness = load(C2_SEND_READINESS)

    assert portfolio_governance["status"] == "canonical_portfolio_governance"
    assert portfolio_governance["scope"]["repository_count"] == 38

    # PUBLICATION_PROGRAMME is intentionally track-local, not whole-owner governance.
    assert programme["status"] == "canonical_track_publication_programme"
    assert programme["scope"]["track_id"] == "observation_evidence"
    assert programme["scope"]["whole_owner_portfolio"] is False
    assert programme["scope"]["parent_governance"] == "universe/PORTFOLIO_GOVERNANCE_2026-09-11.json"
    assert programme["governance"]["portfolio_governance"] == "universe/PORTFOLIO_GOVERNANCE_2026-09-11.json"
    assert programme["governance"]["thesis_architecture"] == "thesis/final_chapter_architecture.json"
    assert thesis["status"] == "final_editorial_order_forbidden_inference_spine"
    assert len(thesis["chapters"]) == 10

    portfolio = programme["portfolio"]
    assert portfolio["scope"] == "observation_evidence_track_only"
    assert portfolio["confirmed_submission_units"] == 5
    assert portfolio["conditional_submission_units"] == 1
    assert portfolio["maximum_submission_units"] == 6
    assert portfolio["whole_owner_count_claim"] is False

    local_contract = portfolio_governance["local_router_contract"]
    assert local_contract["path"] == "universe/PUBLICATION_PROGRAMME_2026-09-11.json"
    assert local_contract["track"] == "observation_evidence"
    assert local_contract["confirmed"] == 5
    assert local_contract["conditional"] == 1
    assert set(local_contract["paper_units"]) == set(portfolio_governance["tracks"]["observation_evidence"])

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
    for path in (
        PROPOSAL,
        C2_PRIOR_ART,
        C2_EDITOR_PITCH,
        C2_AUTHORSHIP,
        C2_SEND_READINESS,
        C2_AUTHOR_METADATA,
        C2_SEND_CANDIDATE,
        C2_OUTSIDE_READER,
        C2_RED_TEAM,
        LIVE_RULES,
    ):
        assert path.exists()

    live_rules = LIVE_RULES.read_text(encoding="utf-8")
    for required in (
        "7000–8000 words",
        "continuous line numbering",
        "3–5 bullets",
        "85 characters",
        "immediately before References",
        "Ecological Modelling",
        "Ecological Informatics",
        "Trends in Ecology & Evolution",
        "must not be guessed",
    ):
        assert required in live_rules

    prior_art_text = C2_PRIOR_ART.read_text(encoding="utf-8")
    for required in (
        "Structural Identifiability",
        "targeted experiment design",
        "Pseudoreplication",
        "site occupancy",
        "Calibration of probability predictions",
        "four-way synthesis",
    ):
        assert required.lower() in prior_art_text.lower()

    pitch_text = C2_EDITOR_PITCH.read_text(encoding="utf-8")
    _assert_any(pitch_text, "Geometry failure", "Same-dimension failure")
    _assert_any(pitch_text, "Objective failure", "Wrong-target failure")
    _assert_any(pitch_text, "Dependence failure", "False-independence failure")
    _assert_any(pitch_text, "Pipeline failure", "Too-late failure")
    for required in ("Prior-art position", "Selected external anchors"):
        assert required.lower() in pitch_text.lower()

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

    # C2 proposal-stage authorship is evidence-based but remains a human decision.
    assert authorship["status"] == "provisional-author-evidence-complete-human-decision-open"
    assert authorship["working_default"]["author_list"] == ["Ruiqi Zhang"]
    assert authorship["working_default"]["corresponding_author"] == "Ruiqi Zhang"
    documented = authorship["documented_people"]
    assert len(documented) == 1
    assert documented[0]["name"] == "Ruiqi Zhang"
    assert documented[0]["provisional_corresponding_author"] is True
    _assert_blob_pin(documented[0]["evidence"]["source_blob_sha1"])
    assert "repository commits" in authorship["additional_author_rule"]["insufficient_alone"]

    # Machine preparation is complete; actual sending stays blocked on explicit human gates.
    assert readiness["status"] == "machine-ready-human-decisions-open"
    assert readiness["machine_checks"]["machine_blockers"] == 0
    assert readiness["machine_checks"]["frozen_send_candidate_written"] is True
    assert readiness["machine_checks"]["outside_reader_packet_written"] is True
    assert readiness["machine_checks"]["tree_editorial_red_team_completed"] is True
    assert readiness["machine_checks"]["internal_red_team_decision"].startswith("GO")
    assert readiness["authorship_state"]["working_author_list"] == ["Ruiqi Zhang"]
    assert readiness["authorship_state"]["working_corresponding_author"] == "Ruiqi Zhang"
    expected_assets = {
        "author_metadata_template": "proposals/C2_TREE_AUTHOR_METADATA_TEMPLATE.md",
        "send_candidate": "proposals/C2_TREE_SEND_CANDIDATE.md",
        "outside_reader_packet": "proposals/C2_OUTSIDE_READER_PACKET.md",
        "editorial_red_team": "proposals/C2_TREE_RED_TEAM.md",
    }
    for key, value in expected_assets.items():
        assert readiness["proposal_assets"][key] == value
    human_ids = {row["id"] for row in readiness["human_blockers_before_send"] if row["required"]}
    assert human_ids == {"authorship", "broad_interest_read", "live_contact_check"}

    print("PUBLICATION_PROGRAMME TRACK PASS")


if __name__ == "__main__":
    main()
