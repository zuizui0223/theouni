from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TYPES = ROOT / "empirical" / "system_types.json"
TEMPLATE = ROOT / "empirical" / "project_manifest.template.json"
TYPING_MAP = ROOT / "empirical" / "project_typing_map.json"


def main() -> None:
    registry = json.loads(TYPES.read_text(encoding="utf-8"))
    template = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    typing_map = json.loads(TYPING_MAP.read_text(encoding="utf-8"))

    assert registry["schema_version"] == "theouni-concrete-research-universe.v0.1"
    assert registry["depends_on"]["theory_core"] == "theouni-theory-core.v0.5"
    assert registry["depends_on"]["projection_gate"] == "theouni-empirical-projection-gate.v0.1"

    programmes = registry["programme_types"]
    ids = [item["id"] for item in programmes]
    assert ids == ["CR-1", "CR-2", "CR-3", "CR-4", "CR-5"]
    assert len(ids) == len(set(ids))

    required_fields = {
        "id",
        "name",
        "layer",
        "primary_projection_fields",
        "allowed_outputs",
        "forbidden_upgrades",
        "theory_handoffs",
    }
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

    # Concrete repository typing is a role assignment only, never a projection result.
    assert typing_map["schema_version"] == "theouni-project-typing-map.v0.1"
    assert typing_map["status"] == "typing_only_no_projection_success_claim"

    typed_projects = typing_map["typed_projects"]
    typed_repo_names = [item["repository"] for item in typed_projects]
    assert len(typed_repo_names) == len(set(typed_repo_names)), "duplicate typed repository"
    assert len(typed_projects) == 13

    for project in typed_projects:
        assert project["primary_type"] in programme_ids
        assert all(item in programme_ids for item in project["secondary_types"])
        assert project["primary_type"] not in project["secondary_types"]
        assert project["projection_status"] == "not_instantiated_here"
        assert project["role"].strip()
        assert project["forbidden_upgrade"].strip()

    expected_primary = {
        "island": "CR-1",
        "izu-core": "CR-1",
        "hotarubukuro": "CR-3",
        "fcp": "CR-1",
        "azami": "CR-3",
        "EAzami": "CR-2",
        "chun": "CR-2",
        "shimahotarubukuro": "CR-3",
        "eog": "CR-4",
        "sdmr": "CR-4",
        "acsp": "CR-4",
        "pollipi": "CR-5",
        "insepi": "CR-5",
    }
    actual_primary = {item["repository"]: item["primary_type"] for item in typed_projects}
    assert actual_primary == expected_primary

    excluded = {
        repo
        for group in typing_map["excluded_from_cr_v0_1"]
        for repo in group["repositories"]
    }
    theory_core_repos = {
        "crest",
        "ccoc",
        "mltr",
        "mrm",
        "ced",
        "microdonta",
        "eco-genetic-criticality",
        "eco-genetic-warning-extensions",
        "theouni",
    }
    assert theory_core_repos <= excluded
    assert not (set(typed_repo_names) & theory_core_repos)
    assert "bita" in excluded
    assert "odsp" in excluded

    print(
        "Concrete Research Universe v0.1 validated: "
        f"{len(programmes)} programme types, {len(registry['composition_edges'])} typed composition edges, "
        f"{len(typed_projects)} provisionally typed repositories, and one projection-gated project manifest template."
    )


if __name__ == "__main__":
    main()
