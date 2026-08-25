from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "theory" / "core_universe.json"
TU1 = ROOT / "theory" / "tu1_registry.json"
TU2 = ROOT / "theory" / "tu2_registry.json"


def main() -> None:
    core = json.loads(CORE.read_text(encoding="utf-8"))
    tu1 = json.loads(TU1.read_text(encoding="utf-8"))
    tu2 = json.loads(TU2.read_text(encoding="utf-8"))

    assert core["schema_version"] == "theouni-theory-core.v0.3"

    types = core["types"]
    type_ids = [item["id"] for item in types]
    assert len(type_ids) == len(set(type_ids)), "duplicate type id"

    operators = core["operators"]
    operator_ids = [item["id"] for item in operators]
    assert len(operator_ids) == len(set(operator_ids)), "duplicate operator id"

    ownership = core["ownership"]
    owner_layers = [item["layer"] for item in ownership]
    assert len(owner_layers) == len(set(owner_layers)), "duplicate ownership layer"

    required_types = {
        "type:Reality",
        "type:ModelWorldUniverse",
        "type:World",
        "type:Snapshot",
        "type:ScientificContract",
        "type:RequiredState",
        "type:StoredStateRepresentation",
        "type:RevisionSideInformation",
        "type:EvidenceClass",
        "type:Report",
        "type:AdmissibleCausalSet",
        "type:CausalLearningValue",
        "type:TargetLicensingStatus",
        "type:LossGeneratingState",
        "type:WarningStatistic",
        "type:WarningValidity",
    }
    assert required_types <= set(type_ids), "missing canonical type"

    assert {
        "op:ContractRevision",
        "op:CausalLearningScore",
        "op:TargetLicensing",
    } <= set(operator_ids)

    for collapse in core["forbidden_collapses"]:
        assert collapse["left"] in type_ids, collapse
        assert collapse["right"] in type_ids, collapse
        assert collapse["left"] != collapse["right"], collapse
        assert collapse["unless"].strip(), collapse

    obstruction_owners = {item["owner"] for item in core["structural_obstructions"]}
    assert {
        "repo:ccoc",
        "repo:mltr",
        "repo:mrm",
        "repo:ced",
        "repo:theouni",
    } <= obstruction_owners

    ownership_owners = {item["owner"] for item in ownership}
    assert {
        "repo:crest",
        "repo:ccoc",
        "repo:mltr",
        "repo:mrm",
        "repo:ced",
        "repo:microdonta",
        "repo:eco-genetic-criticality",
        "repo:eco-genetic-warning-extensions",
        "repo:theouni",
    } <= ownership_owners

    forbidden_pairs = {
        (item["left"], item["right"])
        for item in core["forbidden_collapses"]
    }
    assert ("type:Reality", "type:World") in forbidden_pairs
    assert ("type:Snapshot", "type:RequiredState") in forbidden_pairs
    assert ("type:EvidenceClass", "type:RequiredState") in forbidden_pairs
    assert ("type:WarningStatistic", "type:LossGeneratingState") in forbidden_pairs
    assert ("type:StoredStateRepresentation", "type:RequiredState") in forbidden_pairs
    assert ("type:CausalLearningValue", "type:TargetLicensingStatus") in forbidden_pairs

    modules = {item["id"]: item for item in core["theorem_modules"]}
    assert set(modules) == {"TU-1", "TU-2"}
    assert modules["TU-1"]["status"] == "finite_exact_same_carrier"
    assert modules["TU-2"]["status"] == "finite_exact_bridge_firewall"

    assert tu1["schema_version"] == "theouni-tu1.v1"
    assert tu1["boundary"]["same_finite_carrier_required"] is True
    assert tu1["boundary"]["information_theory_novelty_claim"] is False
    assert [item["id"] for item in tu1["results"]] == [
        "TU-1A", "TU-1B", "TU-1C", "TU-1D", "TU-1E"
    ]

    assert tu2["schema_version"] == "theouni-tu2.v1"
    assert tu2["status"] == "finite_exact_bridge_firewall"
    assert [item["id"] for item in tu2["results"]] == [
        "TU-2A", "TU-2B", "TU-2C", "TU-2-policy-reversal"
    ]

    assert core["empirical_boundary"]["included"] is False
    assert core["open_obligations"], "theory core must preserve open obligations"

    print(
        "Theory Universe v0.3 validated: "
        f"{len(types)} types, {len(operators)} operators, "
        f"{len(core['forbidden_collapses'])} forbidden collapses, "
        f"{len(core['theorem_modules'])} theorem modules, "
        f"{len(core['open_obligations'])} open obligations."
    )


if __name__ == "__main__":
    main()
