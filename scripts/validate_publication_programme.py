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
C2_LIVE_ROUTE = ROOT / "proposals" / "C2_TREE_LIVE_ROUTE_CHECK_20260912.md"
C2_FIGURE1 = ROOT / "proposals" / "C2_FIGURE1_DECISION_MAP_SPEC.md"
C2_MANUSCRIPT = ROOT / "manuscript" / "C2_TREE_OPINION_DRAFT_V8.md"
C2_MANUSCRIPT_STATUS = ROOT / "manuscript" / "C2_MANUSCRIPT_STATUS_2026-09-24.json"
C2_REFERENCE_AUDIT = ROOT / "manuscript" / "C2_REFERENCE_METADATA_AUDIT_2026-09-24.json"
C2_MANUSCRIPT_VALIDATOR = ROOT / "scripts" / "validate_c2_manuscript.py"
C2_CITATION_AUDIT_VALIDATOR = ROOT / "scripts" / "audit_c2_citations.py"


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
    c2_status = load(C2_MANUSCRIPT_STATUS)
    reference_audit = load(C2_REFERENCE_AUDIT)

    assert portfolio_governance["status"] == "canonical_portfolio_governance"
    assert portfolio_governance["scope"]["repository_count"] == 38

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

    c1 = concept["C1"]
    assert c1["home"] == "zuizui0223/boundary"
    assert c1["role_contract"] == "paper/BOUNDARY_ROLE_CONTRACT_2026-09-12.json"
    assert c1["machine_blockers"] == 0
    assert "k-rank(M)" in c1["exclusive_owner"]
    assert "geometry-failure exemplar" in c1["c2_interface"]
    assert "does not own Boundary rank geometry" in c1["ced_interface"]
    assert "C2 is declined" in c1["activation_rule"]

    assert len(concept["C2"]["four_failures"]) == 4
    assert [row["id"] for row in concept["C2"]["four_failures"]] == [
        "geometry",
        "objective",
        "dependence",
        "pipeline",
    ]
    geometry = concept["C2"]["four_failures"][0]
    assert geometry["owner"] == "zuizui0223/boundary"

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
        C2_LIVE_ROUTE,
        C2_FIGURE1,
        C2_MANUSCRIPT,
        C2_MANUSCRIPT_STATUS,
        C2_REFERENCE_AUDIT,
        C2_MANUSCRIPT_VALIDATOR,
        C2_CITATION_AUDIT_VALIDATOR,
        LIVE_RULES,
    ):
        assert path.exists(), path

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
        "Ecology Letters Perspective / Boundary",
        "no more than 300 words",
        "ecolets@cefe.cnrs.fr",
        "ecolets2@cefe.cnrs.fr",
        "same novelty expectation as a Letter",
        "must not be guessed",
    ):
        assert required in live_rules

    prior_art_text = C2_PRIOR_ART.read_text(encoding="utf-8")
    _assert_any(prior_art_text, "structural identification", "structural-identifiability", "identifiability")
    _assert_any(prior_art_text, "goal-oriented design", "targeted experiment design")
    _assert_any(prior_art_text, "pseudoreplication")
    _assert_any(prior_art_text, "occupancy", "imperfect detection")
    _assert_any(prior_art_text, "calibration", "operating-semantics drift")
    _assert_any(prior_art_text, "shared conditional structure", "four interacting interfaces")

    proposal_text = PROPOSAL.read_text(encoding="utf-8")
    for boundary_owned_surface in (
        "k-rank(M)",
        "Gamma/kappa",
        "breakdown factor",
        "anchor-ladder",
    ):
        assert boundary_owned_surface not in proposal_text
    assert "same-direction failure" in proposal_text.lower()
    assert "exact rank theorem" in proposal_text.lower()
    assert "remain exclusively in the Boundary/C1 paper" in proposal_text
    assert "measurement escalation should be diagnostic-first, not quantity-first" in proposal_text.lower()
    assert "remedy-matched decision rule" in proposal_text.lower()
    assert "C2_FIGURE1_DECISION_MAP_SPEC.md" in proposal_text
    for required in (
        "Chadwick et al. (2024)",
        "Williams & Brown (2019)",
        "does **not** claim novelty for a four-part observation taxonomy",
        "measurement intervention class",
        "correctly specified full value-of-information or optimal-design model",
    ):
        assert required.lower() in proposal_text.lower(), required

    pitch_text = C2_EDITOR_PITCH.read_text(encoding="utf-8")
    for required in (
        "local quantities conditioned on earlier choices and losses",
        "timely preservation",
        "separation",
        "relevance",
        "failure diversity",
        "## What is new",
        "measure a new distinction",
        "target-relevant information",
        "diversify failure domains",
        "capture earlier",
        "not another observation-process typology",
        "Chadwick et al. (2024)",
        "Williams & Brown (2019)",
        "intervention-class ranking",
        "correctly specified full VoI/OED",
    ):
        assert required.lower() in pitch_text.lower(), required
    for external_anchor in (
        "Chamberlin 1890",
        "Platt 1964",
        "Hurlbert 1984",
        "MacKenzie et al. 2002",
    ):
        assert external_anchor.lower() in pitch_text.lower(), external_anchor
    assert "Boundary paper retains the full identification theorem" in pitch_text
    assert "same-dimension/separation lesson" in pitch_text

    outside_reader_text = C2_OUTSIDE_READER.read_text(encoding="utf-8")
    for required in (
        "direct-neighbour differentiation check",
        "LIES",
        "VoI/OED",
        "prospective intervention-class prediction",
        "When more measurement is not more evidence",
    ):
        assert required.lower() in outside_reader_text.lower(), required
    assert "four failures of monotonic reasoning" not in outside_reader_text.lower()

    send_text = C2_SEND_CANDIDATE.read_text(encoding="utf-8")
    for boundary_owned_surface in (
        "k-rank(M)",
        "breakdown factor",
        "anchor-ladder",
    ):
        assert boundary_owned_surface not in send_text
    assert "separates an unresolved explanation" in send_text
    assert "C1/Boundary remains parked" in send_text

    figure_text = C2_FIGURE1.read_text(encoding="utf-8")
    for required in (
        "measurement-to-evidence",
        "biological opportunity / live alternatives",
        "retained record",
        "distinguishable alternatives",
        "declared target",
        "timely preservation",
        "separation",
        "relevance",
        "failure diversity is not a fourth sequential arrow",
        "measure a new distinction",
        "measure target-relevant information",
        "diversify failure domains",
        "capture earlier",
        "the four interfaces are exhaustive",
        "diagnostic-first, not quantity-first",
        "preferred TREE Opinion v8",
        "conditioned on earlier measurement choices and losses",
    ):
        assert required.lower() in figure_text.lower(), required

    assert methods["M1"]["repository"] == "zuizui0223/tnoa"
    assert methods["M2"]["repository"] == "zuizui0223/mrod"
    assert methods["M3"]["repository"] == "zuizui0223/ced"
    assert methods["M4"]["repositories"] == ["zuizui0223/v3", "zuizui0223/rec"]
    assert "TNOA is excluded" in methods["M4"]["firewall"]
    assert "Boundary retains structural identification geometry" in methods["M3"]["boundary_interface"]
    assert "not k-rank(M)" in methods["M3"]["boundary_interface"]

    superseded = set(programme["governance"]["superseded_publication_plans"])
    assert superseded == {
        "universe/SUBMISSION_ARCHITECTURE_2026-09-08.md",
        "universe/TWO_PAPER_EXECUTION_STATUS_2026-09-08.md",
    }

    non_claims = "\n".join(programme["non_claims"])
    assert "does not transfer Boundary theorem ownership" in non_claims
    assert "does not transfer Boundary rank-geometry ownership" in non_claims

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

    assert authorship["status"] == "provisional-author-evidence-complete-human-decision-open"
    assert authorship["working_default"]["author_list"] == ["Ruiqi Zhang"]
    assert authorship["working_default"]["corresponding_author"] == "Ruiqi Zhang"
    documented = authorship["documented_people"]
    assert len(documented) == 1
    assert documented[0]["name"] == "Ruiqi Zhang"
    assert documented[0]["provisional_corresponding_author"] is True
    _assert_blob_pin(documented[0]["evidence"]["source_blob_sha1"])
    assert "repository commits" in authorship["additional_author_rule"]["insufficient_alone"]

    assert readiness["schema"] == "c2-tree-send-readiness-v2"
    assert readiness["status"] == "machine-ready-human-decisions-open"
    checks = readiness["machine_checks"]
    assert checks["machine_blockers"] == 0
    assert checks["four_failure_structure_fixed"] is True
    assert checks["diagnostic_first_opinion_position_fixed"] is True
    assert checks["shared_conditional_locality_thesis_explicit"] is True
    assert checks["cross_interface_interactions_explicit"] is True
    assert checks["prospective_equal_cost_intervention_ranking_test_explicit"] is True
    assert checks["remedy_matched_diagnosis_explicit"] is True
    assert checks["geometry_remedy_new_identification_direction"] is True
    assert checks["objective_remedy_target_relevant_information"] is True
    assert checks["dependence_remedy_independent_failure_opportunity"] is True
    assert checks["pipeline_remedy_earlier_capture_before_irreversible_loss"] is True
    assert checks["figure1_is_decision_map_not_taxonomy"] is True
    assert checks["frozen_send_candidate_written"] is True
    assert checks["outside_reader_packet_written"] is True
    assert checks["tree_editorial_red_team_completed"] is True
    assert checks["internal_red_team_decision"].startswith("GO")
    assert checks["direct_neighbour_lies_acknowledged"] is True
    assert checks["sampling_inference_conditionality_acknowledged"] is True
    assert checks["formal_voi_oed_ranking_prior_art_acknowledged"] is True
    assert checks["novelty_narrowed_to_claim_specific_intervention_class_prediction"] is True
    assert checks["outside_reader_direct_neighbour_gate_written"] is True
    assert checks["current_live_journal_contact_independently_confirmed"] is True
    assert checks["current_live_journal_contact_checked_on"] == "2026-09-12"
    assert checks["current_live_journal_contact"] == "tree@cell.com"
    assert checks["current_live_editor"] == "Andrea Stephens"
    assert checks["dispatch_time_recheck_still_required"] is True
    assert checks["preferred_full_manuscript_version"] == "v8"
    assert checks["full_manuscript_written"] is True
    assert checks["full_manuscript_validated"] is True
    assert checks["full_manuscript_word_count_before_references"] == 4439
    assert checks["full_manuscript_external_reference_count"] == 22
    assert checks["full_manuscript_validation_run"] == 35971077395
    assert checks["full_manuscript_validation_head"] == "9f6b8fe1057496068b5d5edbdfbe1bd912cfefcd"
    assert checks["full_manuscript_citation_audit_pass"] is True
    assert checks["full_manuscript_all_external_references_cited"] is True
    assert checks["full_manuscript_section_citation_coverage_pass"] is True
    assert checks["reference_metadata_audit_pass"] is True
    assert checks["reference_metadata_discrepancies_requiring_edit"] == 0
    assert checks["figure1_machine_validated"] is True
    assert checks["figure1_validation_run"] == 35971077395
    assert readiness["authorship_state"]["working_author_list"] == ["Ruiqi Zhang"]
    assert readiness["authorship_state"]["working_corresponding_author"] == "Ruiqi Zhang"

    expected_assets = {
        "author_metadata_template": "proposals/C2_TREE_AUTHOR_METADATA_TEMPLATE.md",
        "send_candidate": "proposals/C2_TREE_SEND_CANDIDATE.md",
        "outside_reader_packet": "proposals/C2_OUTSIDE_READER_PACKET.md",
        "editorial_red_team": "proposals/C2_TREE_RED_TEAM.md",
        "live_route_check": "proposals/C2_TREE_LIVE_ROUTE_CHECK_20260912.md",
        "figure1_decision_map_spec": "proposals/C2_FIGURE1_DECISION_MAP_SPEC.md",
        "full_manuscript": "manuscript/C2_TREE_OPINION_DRAFT_V8.md",
        "full_manuscript_status": "manuscript/C2_MANUSCRIPT_STATUS_2026-09-24.json",
        "manuscript_validator": "scripts/validate_c2_manuscript.py",
        "citation_audit_validator": "scripts/audit_c2_citations.py",
        "reference_metadata_audit": "manuscript/C2_REFERENCE_METADATA_AUDIT_2026-09-24.json",
        "figure1_vector": "manuscript/figures/C2_FIGURE1_MEASUREMENT_TO_EVIDENCE.svg",
    }
    for key, value in expected_assets.items():
        assert readiness["proposal_assets"][key] == value

    # Canonical-pointer consistency guard: future manuscript promotions must move
    # readiness, status, metadata audit and validators together.
    manuscript_rel = str(C2_MANUSCRIPT.relative_to(ROOT))
    status_rel = str(C2_MANUSCRIPT_STATUS.relative_to(ROOT))
    reference_audit_rel = str(C2_REFERENCE_AUDIT.relative_to(ROOT))
    assert readiness["proposal_assets"]["full_manuscript"] == manuscript_rel
    assert readiness["proposal_assets"]["full_manuscript_status"] == status_rel
    assert readiness["proposal_assets"]["reference_metadata_audit"] == reference_audit_rel
    assert c2_status["preferred_manuscript"] == manuscript_rel
    assert reference_audit["manuscript"] == manuscript_rel
    assert c2_status["word_count_before_references"] == checks["full_manuscript_word_count_before_references"]
    assert c2_status["external_reference_count"] == checks["full_manuscript_external_reference_count"]
    assert c2_status["validation"]["run_id"] == checks["full_manuscript_validation_run"]
    assert c2_status["validation"]["head_sha"] == checks["full_manuscript_validation_head"]
    assert c2_status["validation"]["reference_metadata_audit"] == reference_audit_rel
    assert reference_audit["reference_count"] == c2_status["external_reference_count"]
    assert reference_audit["status"] == "pass"
    assert reference_audit["discrepancies_requiring_manuscript_edit"] == 0
    assert reference_audit["v8_additions_verified"] == [21, 22]
    assert reference_audit["direct_neighbour_positioning_verified"] is True
    assert c2_status["status"] == "preferred-full-manuscript-v8-machine-validated"
    assert c2_status["revision_history"]["v7_to_v8"]["reference_count_to"] == 22

    human_ids = {row["id"] for row in readiness["human_blockers_before_send"] if row["required"]}
    assert human_ids == {"authorship", "broad_interest_read", "dispatch_time_route_recheck"}

    route_text = C2_LIVE_ROUTE.read_text(encoding="utf-8")
    for required in (
        "Andrea Stephens",
        "tree@cell.com",
        "proposal by email",
        "dispatch-time recheck still required",
    ):
        assert required.lower() in route_text.lower()

    print("PUBLICATION_PROGRAMME TRACK PASS")


if __name__ == "__main__":
    main()
