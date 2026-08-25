from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "theory" / "core_universe.json"


def main() -> None:
    core = json.loads(CORE.read_text(encoding="utf-8"))

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
        "type:EvidenceClass",
        "type:Report",
        "type:AdmissibleCausalSet",
        "type:LossGeneratingState",
        "type:WarningStatistic",
        "type:WarningValidity",
    }
    assert required_types <= set(type_ids), "missing canonical type"

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

    # Constitutional anti-collapse checks.
    forbidden_pairs = {
        (item["left"], item["right"])
        for item in core["forbidden_collapses"]
    }
    assert ("type:Reality", "type:World") in forbidden_pairs
    assert ("type:Snapshot", "type:RequiredState") in forbidden_pairs
    assert ("type:EvidenceClass", "type:RequiredState") in forbidden_pairs
    assert ("type:WarningStatistic", "type:LossGeneratingState") in forbidden_pairs

    assert core["empirical_boundary"]["included"] is False
    assert core["open_obligations"], "theory v0.1 must preserve open obligations"

    print(
        "Theory Universe v0.1 validated: "
        f"{len(types)} types, {len(operators)} operators, "
        f"{len(core['forbidden_collapses'])} forbidden collapses, "
        f"{len(core['open_obligations'])} open obligations."
    )


if __name__ == "__main__":
    main()
