from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TYPES = ROOT / "empirical" / "system_types.json"
TEMPLATE = ROOT / "empirical" / "project_manifest.template.json"


def main() -> None:
    registry = json.loads(TYPES.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))

    assert registry["schema_version"] == "theouni-concrete-research-universe.v0.1"
    assert registry["depends_on"]["theory_core"] == "theouni-theory-core.v0.5"
    assert registry["depends_on"]["projection_gate"] == "theouni-empirical-projection-gate.v0.1"

    programmes = registry["programme_types"]
    ids = [item["id"] for item in programmes]
    assert ids == ["CR-1", "CR-2", "CR-3", "CR-4", "CR-5"]
    assert len(ids) == len(set(ids))

    required_fields = {"id", "name", "layer", "primary_projection_fields", "allowed_outputs", "forbidden_upgrades", "theory_handoffs"}
    for programme in programmes:
        assert required_fields <= set(programme)
        assert programme["primary_projection_fields"]
        assert programme["allowed_outputs"]
        assert programme["forbidden_upgrades"]
        assert programme["theory_handoffs"]

    programme_ids = set(ids)
    for edge in registry["composition_edges"]:
        assert edge["source"] in programme_ids
        assert edge["target"] in programme_ids
        assert edge["source"] != edge["target"]
        assert edge["relation"].strip()
        assert edge["meaning"].strip()

    assert {
        "ProgrammeType!=RequiredState",
        "MethodType!=BiologicalState",
        "ContextLabel!=StateByDefault",
        "Predictor!=EmpiricalPartialState",
        "ObservationRecord!=BiologicalEventWithoutReliabilityBridge",
        "WorldSupport!=OccupancyOrTruth",
    } <= set(registry["global_firewalls"])

    assert template["schema_version"] == "theouni-concrete-project-manifest.v0.1"
    primary = template["programme_typing"]["primary_type"]
    assert primary in programme_ids

    contract = template["empirical_projection_contract"]
    assert set(contract) == {"U", "tau", "Z", "H", "A", "Y", "O", "V", "Delta", "epsilon"}

    gate = template["projection_gate_status"]
    assert set(gate) == {
        "G0_provenance_synchronization",
        "G1_candidate_predictive_adequacy",
        "G2_residual_context_redundancy",
        "G3_ecological_unit_validation",
        "G4_observation_reliability",
        "G5_target_action_stress",
        "decision",
    }
    assert all(value == "unassessed" for value in gate.values())

    non_claims = set(template["explicit_non_claims"])
    assert any("programme type is not an ecological state" in item.lower() for item in non_claims)
    assert any("projection gate" in item.lower() for item in non_claims)

    print(
        "Concrete Research Universe v0.1 validated: "
        f"{len(programmes)} programme types, {len(registry['composition_edges'])} typed composition edges, "
        "and one projection-gated project manifest template."
    )


if __name__ == "__main__":
    main()
