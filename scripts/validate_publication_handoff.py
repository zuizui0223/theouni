#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HANDOFF_JSON = ROOT / "universe" / "PUBLICATION_HANDOFF_2026-09-12.json"
HANDOFF_MD = ROOT / "universe" / "PUBLICATION_HANDOFF_2026-09-12.md"
INTEGRATION = ROOT / "universe" / "REPOSITORY_PAPER_INTEGRATION_CONTRACT_2026-09-15.json"
LIVE_RULES = ROOT / "universe" / "LIVE_JOURNAL_RULES_2026-09-12.md"
HUMAN_JSON = ROOT / "universe" / "HUMAN_SUBMISSION_INPUTS_2026-09-12.json"
HUMAN_MD = ROOT / "universe" / "HUMAN_SUBMISSION_INPUTS_2026-09-12.md"
PROPAGATION = ROOT / "universe" / "HUMAN_INPUT_PROPAGATION_MAP_2026-09-12.json"
C2_READINESS = ROOT / "proposals" / "C2_SEND_READINESS.json"
C2_MANUSCRIPT = ROOT / "manuscript" / "C2_TREE_OPINION_DRAFT_V8.md"
C2_MANUSCRIPT_STATUS = ROOT / "manuscript" / "C2_MANUSCRIPT_STATUS_2026-09-24.json"
C2_REFERENCE_AUDIT = ROOT / "manuscript" / "C2_REFERENCE_METADATA_AUDIT_2026-09-24.json"
C2_FIGURE_VISUAL_AUDIT = ROOT / "manuscript" / "C2_FIGURE1_VISUAL_AUDIT_2026-09-15.json"
C2_MANUSCRIPT_VALIDATOR = ROOT / "scripts" / "validate_c2_manuscript.py"
C2_CITATION_AUDIT_VALIDATOR = ROOT / "scripts" / "audit_c2_citations.py"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    for path in (
        HANDOFF_JSON,
        HANDOFF_MD,
        INTEGRATION,
        LIVE_RULES,
        HUMAN_JSON,
        HUMAN_MD,
        PROPAGATION,
        C2_READINESS,
        C2_MANUSCRIPT,
        C2_MANUSCRIPT_STATUS,
        C2_REFERENCE_AUDIT,
        C2_FIGURE_VISUAL_AUDIT,
        C2_MANUSCRIPT_VALIDATOR,
        C2_CITATION_AUDIT_VALIDATOR,
    ):
        assert path.exists(), path

    handoff = load(HANDOFF_JSON)
    integration = load(INTEGRATION)
    human = load(HUMAN_JSON)
    propagation = load(PROPAGATION)
    readiness = load(C2_READINESS)
    c2_status = load(C2_MANUSCRIPT_STATUS)
    reference_audit = load(C2_REFERENCE_AUDIT)
    figure_visual_audit = load(C2_FIGURE_VISUAL_AUDIT)

    assert handoff["schema"] == "publication-handoff-v2"
    assert handoff["status"] == "machine-work-closed-human-completion-open"
    assert handoff["scope"] == "observation_evidence_track_only"
    assert handoff["last_scientific_surface_sync"] == "2026-09-24"
    assert handoff["repository_paper_integration_contract"] == "universe/REPOSITORY_PAPER_INTEGRATION_CONTRACT_2026-09-15.json"
    assert handoff["live_rules"] == "universe/LIVE_JOURNAL_RULES_2026-09-12.md"
    assert handoff["human_input_ledger"] == "universe/HUMAN_SUBMISSION_INPUTS_2026-09-12.json"

    assert integration["status"] == "canonical-integration-contract"
    rules = set(integration["ownership_rules"])
    assert "one repository may own multiple paper units" in rules
    assert "one paper may span multiple repositories" in rules
    assert "export to a synthesis does not transfer theorem or empirical-result ownership unless explicitly recorded" in rules
    boundary_decision = integration["boundary_decision"]
    assert boundary_decision["repository"] == "zuizui0223/boundary"
    assert boundary_decision["paper_unit"] == "BOUNDARY_C1"
    assert boundary_decision["decision"] == "retain as independent conditional C1; do not absorb into C2 or CED"
    assert boundary_decision["c2_export_ceiling"] == "qualitative same-direction/separation lesson only"
    assert boundary_decision["ced_export_ceiling"] == "external identification boundary/contrast only"

    units = handoff["units"]
    assert set(units) == {"C1", "C2", "M1", "M2", "M3", "M4"}

    c1 = units["C1"]
    assert c1["state"] == "machine-ready-strategically-parked"
    assert c1["repository"] == "zuizui0223/boundary"
    assert c1["role_contract"] == "zuizui0223/boundary/paper/BOUNDARY_ROLE_CONTRACT_2026-09-12.json"
    assert c1["send_readiness"] == "zuizui0223/boundary/paper/C1_SEND_READINESS_2026-09-12.json"
    assert c1["exclusive_owner"] == "structural identification geometry"
    assert "mechanistic proximity != mechanism identification" in c1["headline_claim"]
    assert "k-rank(M)" in c1["primary_surface"]
    assert "row-rank gain criterion" in c1["primary_surface"]
    assert "Gamma/kappa" in c1["secondary_extension"]
    assert "qualitative geometry exemplar only" in c1["c2_role"]
    assert "exact theorem surface stays in Boundary" in c1["c2_role"]
    assert "external identification-geometry" in c1["ced_role"]
    assert c1["machine_blocker"] is False
    assert c1["proposal_max_words"] == 300
    assert c1["proposal_word_count"] == 210
    assert c1["proposal_word_headroom"] == 90
    assert c1["current_strategy_decision"] == "keep parked until C2 editorial outcome"
    assert c1["current_human_blockers"] == []
    assert set(c1["human_gates_if_activated"]) == {
        "authorship",
        "author qualification",
        "contact metadata",
        "live rule recheck",
    }
    assert "C2 is declined/too broad" in c1["activation_gate"]

    c2 = units["C2"]
    assert c2["machine_state"] == "proposal-and-full-manuscript-ready"
    assert c2["sent"] is False
    assert c2["preferred_full_manuscript"] == "manuscript/C2_TREE_OPINION_DRAFT_V8.md"
    assert c2["full_manuscript_status"] == "manuscript/C2_MANUSCRIPT_STATUS_2026-09-24.json"
    assert c2["full_manuscript_words_before_references"] == 4439
    assert c2["full_manuscript_external_references"] == 22
    assert c2["full_manuscript_validation_run"] == 35971077395
    assert c2["full_manuscript_validation_head"] == "9f6b8fe1057496068b5d5edbdfbe1bd912cfefcd"
    assert c2["citation_audit_validator"] == "scripts/audit_c2_citations.py"
    assert c2["citation_audit_pass"] is True
    assert c2["all_external_references_cited"] is True
    assert c2["section_level_citation_coverage_pass"] is True
    assert c2["reference_metadata_audit"] == "manuscript/C2_REFERENCE_METADATA_AUDIT_2026-09-24.json"
    assert c2["reference_metadata_audit_pass"] is True
    assert c2["reference_metadata_discrepancies_requiring_edit"] == 0
    assert c2["figure1_machine_validated"] is True
    assert c2["figure1_visual_audit"] == "manuscript/C2_FIGURE1_VISUAL_AUDIT_2026-09-15.json"
    assert c2["figure1_assistant_visual_audit_pass"] is True
    assert c2["figure1_human_visual_approval"] is False
    assert "do not attach" in c2["full_manuscript_dispatch_policy"].lower()
    assert c2["live_route_verified_on"] == "2026-09-12"
    assert c2["current_live_contact"] == "tree@cell.com"
    assert c2["current_live_editor"] == "Andrea Stephens"
    assert "proposal by email" in c2["current_public_route"]
    assert "LIES" in c2["main_editorial_risk"] and "VoI/OED" in c2["main_editorial_risk"]
    assert c2["direct_neighbour_positioning"]["lies"].startswith("explicitly acknowledged")
    assert "Williams & Brown 2019" in c2["direct_neighbour_positioning"]["sampling_inference"]
    assert "does not claim superiority" in c2["direct_neighbour_positioning"]["voi_oed"]
    assert "intervention class" in c2["direct_neighbour_positioning"]["residual_claim"]
    assert set(c2["human_gates"]) == {
        "authorship approval",
        "broad-interest outside read",
        "dispatch-time route recheck",
    }

    assert readiness["schema"] == "c2-tree-send-readiness-v2"
    assert readiness["machine_checks"]["preferred_full_manuscript_version"] == "v8"
    assert readiness["machine_checks"]["machine_blockers"] == 0
    assert readiness["machine_checks"]["direct_neighbour_lies_acknowledged"] is True
    assert readiness["machine_checks"]["formal_voi_oed_ranking_prior_art_acknowledged"] is True
    assert readiness["machine_checks"]["novelty_narrowed_to_claim_specific_intervention_class_prediction"] is True

    assert c2_status["status"] == "preferred-full-manuscript-v8-machine-validated"
    assert c2_status["preferred_manuscript"] == "manuscript/C2_TREE_OPINION_DRAFT_V8.md"
    assert c2_status["word_count_before_references"] == 4439
    assert c2_status["external_reference_count"] == 22
    assert c2_status["validation"]["run_id"] == 35971077395
    assert c2_status["validation"]["head_sha"] == "9f6b8fe1057496068b5d5edbdfbe1bd912cfefcd"
    assert c2_status["validation"]["conclusion"] == "success"
    assert c2_status["validation"]["citation_audit_status"] == "pass"
    assert c2_status["validation"]["all_external_references_cited"] is True
    assert c2_status["validation"]["section_level_citation_coverage"] is True
    assert c2_status["validation"]["reference_metadata_audit"] == "manuscript/C2_REFERENCE_METADATA_AUDIT_2026-09-24.json"
    assert c2_status["validation"]["reference_metadata_audit_status"] == "pass"
    assert c2_status["validation"]["reference_metadata_discrepancies_requiring_edit"] == 0
    assert c2_status["figure1"]["machine_generated"] is True
    assert c2_status["figure1"]["machine_validated"] is True
    assert c2_status["figure1"]["validation_run"] == 35971077395
    assert c2_status["figure1"]["assistant_visual_audit"] == "manuscript/C2_FIGURE1_VISUAL_AUDIT_2026-09-15.json"
    assert c2_status["figure1"]["assistant_visual_audit_status"] == "pass"
    assert c2_status["figure1"]["human_visual_inspection_complete"] is False
    assert c2_status["revision_history"]["v5_to_v6"]["reduction_words"] == 1393
    assert c2_status["revision_history"]["v6_to_v7"]["change_words"] == 593
    assert c2_status["revision_history"]["v6_to_v7"]["reference_count_to"] == 20
    assert c2_status["revision_history"]["v7_to_v8"]["from_words_before_references"] == 4096
    assert c2_status["revision_history"]["v7_to_v8"]["to_words_before_references"] == 4439
    assert c2_status["revision_history"]["v7_to_v8"]["change_words"] == 343
    assert c2_status["revision_history"]["v7_to_v8"]["reference_count_from"] == 20
    assert c2_status["revision_history"]["v7_to_v8"]["reference_count_to"] == 22
    assert c2_status["claim_firewalls"]["observation_process_typology_novelty_claim_absent"] is True
    assert c2_status["claim_firewalls"]["formal_voi_oed_superiority_claim_absent"] is True
    assert c2_status["journal_route"]["proposal_first"] is True
    assert c2_status["journal_route"]["full_manuscript_should_not_be_dispatched_with_presubmission_pitch_unless_requested"] is True

    assert reference_audit["status"] == "pass"
    assert reference_audit["manuscript"] == "manuscript/C2_TREE_OPINION_DRAFT_V8.md"
    assert reference_audit["reference_count"] == 22
    assert reference_audit["discrepancies_requiring_manuscript_edit"] == 0
    assert len(reference_audit["records"]) == 22
    assert reference_audit["v7_additions_verified"] == [15, 16, 17, 18, 19, 20]
    assert reference_audit["v8_additions_verified"] == [21, 22]
    assert reference_audit["direct_neighbour_positioning_verified"] is True
    assert all(row["status"] == "match" for row in reference_audit["records"])

    assert figure_visual_audit["status"] == "assistant-visual-pass-human-final-check-open"
    assert figure_visual_audit["render_checked"] is True
    assert figure_visual_audit["post_correction_checks"]["obvious_text_overlap"] is False
    assert figure_visual_audit["post_correction_checks"]["obvious_clipping"] is False
    assert figure_visual_audit["human_visual_inspection_complete"] is False

    # Cross-layer canonical-pointer guard. This prevents a future v9-style promotion
    # from updating the manuscript while leaving readiness/handoff/status stale.
    manuscript_rel = str(C2_MANUSCRIPT.relative_to(ROOT))
    status_rel = str(C2_MANUSCRIPT_STATUS.relative_to(ROOT))
    reference_rel = str(C2_REFERENCE_AUDIT.relative_to(ROOT))
    assert readiness["proposal_assets"]["full_manuscript"] == manuscript_rel
    assert handoff["units"]["C2"]["preferred_full_manuscript"] == manuscript_rel
    assert c2_status["preferred_manuscript"] == manuscript_rel
    assert reference_audit["manuscript"] == manuscript_rel
    assert readiness["proposal_assets"]["full_manuscript_status"] == status_rel
    assert handoff["units"]["C2"]["full_manuscript_status"] == status_rel
    assert readiness["proposal_assets"]["reference_metadata_audit"] == reference_rel
    assert handoff["units"]["C2"]["reference_metadata_audit"] == reference_rel
    assert c2_status["validation"]["reference_metadata_audit"] == reference_rel
    assert readiness["machine_checks"]["full_manuscript_word_count_before_references"] == c2_status["word_count_before_references"] == c2["full_manuscript_words_before_references"]
    assert readiness["machine_checks"]["full_manuscript_external_reference_count"] == c2_status["external_reference_count"] == c2["full_manuscript_external_references"] == reference_audit["reference_count"]
    assert readiness["machine_checks"]["full_manuscript_validation_run"] == c2_status["validation"]["run_id"] == c2["full_manuscript_validation_run"]

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
        "REPOSITORY_PAPER_INTEGRATION_CONTRACT_2026-09-15.json",
        "validated full manuscript v8",
        "4,439 words",
        "22/22 external references cited",
        "reference metadata audit",
        "0 discrepancies requiring manuscript edit",
        "LIES",
        "equal-cost measurement expansions",
        "Figure 1 machine-generated and machine-validated",
        "assistant visual audit PASS",
        "human final visual approval remains open",
        "C1 — Boundary / Ecology Letters Perspective",
        "Boundary is **not archived material and is not absorbed into C2 or CED**",
        "mechanistic proximity != mechanism identification",
        "210/300 words",
        "90 words",
        "BOUNDARY_ROLE_CONTRACT_2026-09-12.json",
        "qualitative geometry exemplar only",
        "keep C1 parked until the C2 editorial outcome",
        "There is no theorem-ownership transfer",
        "human metadata, visual review and dispatch decisions",
        "Do not reopen frozen science or transfer Boundary theorem ownership",
        "HUMAN_SUBMISSION_INPUTS_2026-09-12",
    ):
        assert required in text, required

    print("PUBLICATION_HANDOFF PASS")


if __name__ == "__main__":
    main()
