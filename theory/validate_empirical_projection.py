from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THEORY = ROOT / "theory"
SCHEMA = THEORY / "empirical_projection_contract.schema.json"
TEMPLATE = THEORY / "empirical_projection_template.json"


def main() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))

    assert schema["$schema"].endswith("draft/2020-12/schema")
    assert schema["properties"]["schema_version"]["const"] == "theouni-empirical-projection.v0.1"
    assert template["schema_version"] == "theouni-empirical-projection.v0.1"

    required = set(schema["required"])
    assert required <= set(template), f"template missing required keys: {sorted(required - set(template))}"

    expected_order = [
        "G0_provenance_sync",
        "G1_candidate_predictive_adequacy",
        "G2_residual_context_redundancy",
        "G3_unit_holdout",
        "G4_reliability",
        "G5_target_action_stress",
    ]
    assert template["decision_rules"]["decision_order"] == expected_order
    assert schema["properties"]["decision_rules"]["properties"]["decision_order"]["const"] == expected_order

    assert template["time_alignment"]["future_leakage_forbidden"] is True
    assert template["validation"]["split_fixed_before_outcome_inspection"] is True
    assert template["observation_reliability"]["source_provenance_fixed"] is True
    assert template["observation_reliability"]["schema_repair_after_outcome_forbidden"] is True

    candidate_items = template["candidate_state"]
    assert candidate_items
    measurement_kinds = set(
        schema["properties"]["candidate_state"]["items"]["properties"]["measurement_kind"]["enum"]
    )
    calibration_statuses = set(
        schema["properties"]["candidate_state"]["items"]["properties"]["calibration_status"]["enum"]
    )
    for item in candidate_items:
        assert item["measurement_kind"] in measurement_kinds
        assert item["calibration_status"] in calibration_statuses
        assert item["selected_before_target_inspection"] is True

    decision_enum = set(schema["properties"]["decision"]["enum"])
    required_decisions = {
        "not_identifiable",
        "candidate_state_not_predictively_supported",
        "predictive_candidate_context_open",
        "empirical_partial_state_supported",
        "portable_empirical_partial_state_supported",
        "not_yet_evaluated",
    }
    assert required_decisions <= decision_enum
    assert template["decision"] == "not_yet_evaluated"

    assert template["decision_rules"]["minimum_candidate_gain_delta"] >= 0
    assert template["decision_rules"]["maximum_residual_context_gain_epsilon"] >= 0
    assert template["claim_ceiling"]["allowed"]
    assert template["claim_ceiling"]["forbidden"]

    forbidden_text = " ".join(template["claim_ceiling"]["forbidden"]).lower()
    for phrase in (
        "complete natural state",
        "causal mechanism",
        "portability",
    ):
        assert phrase in forbidden_text

    gate_doc = (THEORY / "EMPIRICAL_PROJECTION_GATE.md").read_text(encoding="utf-8")
    for label in ("Gate G0", "Gate G1", "Gate G2", "Gate G3", "Gate G4", "Gate G5", "E3", "E4"):
        assert label in gate_doc, f"empirical projection gate missing {label}"

    freeze = json.loads((THEORY / "FREEZE_v0.5.json").read_text(encoding="utf-8"))
    frozen_paths = {item["path"] for item in freeze["semantic_core_files"]}
    assert "theory/EMPIRICAL_PROJECTION_GATE.md" not in frozen_paths
    assert "theory/empirical_projection_contract.schema.json" not in frozen_paths
    assert "theory/empirical_projection_template.json" not in frozen_paths

    print(
        "Empirical projection gate v0.1 validated: "
        f"{len(required)} required contract fields, {len(expected_order)} ordered gates, "
        f"{len(required_decisions)} decision classes."
    )


if __name__ == "__main__":
    main()
