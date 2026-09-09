from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PATH = ROOT / "theory_hierarchy_2026-09-08.json"

REQUIRED_NODES = {
    "crest", "ccoc", "mltr", "mrm",
    "method_qualification", "deployment_adequacy", "observation_support", "ttf_bridge_witness",
    "rec", "v3", "tnoa", "boundary", "mrod", "ced",
    "egc", "egwe_state", "egwe_warning", "egwee", "theouni",
}

REQUIRED_EDGES = {
    ("ccoc", "crest", "normative_obstruction"),
    ("mltr", "crest", "normative_obstruction"),
    ("mrm", "crest", "normative_obstruction"),
    ("crest", "method_qualification", "required_distinction_to_inferential_design"),
    ("method_qualification", "deployment_adequacy", "qualified_method_to_geometry"),
    ("deployment_adequacy", "observation_support", "predeclared_geometry_to_realized_support"),
    ("ttf_bridge_witness", "observation_support", "bounded_empirical_witness_not_theorem_transfer"),
    ("observation_support", "v3", "admitted_retained_evidence_handoff"),
    ("observation_support", "ced", "fail_closed_abstention_handoff"),
    ("crest", "ced", "required_distinction_handoff"),
    ("rec", "v3", "operational_flow"),
    ("v3", "tnoa", "operational_flow"),
    ("tnoa", "boundary", "operational_flow"),
    ("boundary", "mrod", "unresolved_set_handoff"),
    ("mrod", "v3", "realized_future_observation_becomes_refinement"),
    ("boundary", "ced", "structural_identification_handoff"),
    ("egc", "egwe_state", "domain_state_candidate_handoff"),
    ("egwe_state", "egwe_warning", "conditional_warning_evaluation"),
    ("egwe_state", "egwee", "measurement_validation_handoff"),
}

REQUIRED_INEQUALITIES = {
    "RequiredState != MethodValidity",
    "MethodValidity != DeploymentDetectability",
    "DeploymentDetectability != ObservationSupport",
    "ObservationSupport != CompatibleWorldSet",
    "CompatibleWorldSet != ReportableTarget",
}


def main() -> None:
    data = json.loads(PATH.read_text(encoding="utf-8"))

    nodes = data.get("nodes", [])
    ids = [n["id"] for n in nodes]
    assert len(ids) == len(set(ids)), "duplicate node ids"
    assert REQUIRED_NODES <= set(ids), f"missing required nodes: {sorted(REQUIRED_NODES - set(ids))}"

    layers = {x["id"] for x in data.get("layers", [])}
    for node in nodes:
        assert node["layer"] in layers, f"unknown layer for {node['id']}: {node['layer']}"

    edge_rows = data.get("edges", [])
    edge_keys = {(e["from"], e["to"], e["type"]) for e in edge_rows}
    assert REQUIRED_EDGES <= edge_keys, f"missing required edges: {sorted(REQUIRED_EDGES - edge_keys)}"
    for edge in edge_rows:
        assert edge["from"] in ids, f"unknown edge source: {edge['from']}"
        assert edge["to"] in ids, f"unknown edge target: {edge['to']}"

    inequalities = set(data.get("worldview", {}).get("core_inequalities", []))
    assert REQUIRED_INEQUALITIES <= inequalities, (
        "missing observation-support inequalities: "
        f"{sorted(REQUIRED_INEQUALITIES - inequalities)}"
    )

    firewall_pairs = {tuple(x["pair"]) for x in data.get("overlap_firewalls", [])}
    for pair in [
        ("method_qualification", "observation_support"),
        ("deployment_adequacy", "observation_support"),
        ("observation_support", "ced"),
        ("observation_support", "rec"),
        ("boundary", "ced"),
        ("mrod", "ced"),
        ("tnoa", "ced"),
        ("v3", "boundary"),
        ("v3", "mrod"),
        ("crest", "egwe_state"),
    ]:
        assert pair in firewall_pairs, f"missing overlap firewall: {pair}"

    witness = next(n for n in nodes if n["id"] == "ttf_bridge_witness")
    ceiling = witness.get("claim_ceiling", "")
    assert "not a theorem proof" in ceiling, "TTF witness theorem firewall missing"
    assert "not an empirical flower-colour sharedness result" in ceiling, "TTF empirical claim firewall missing"

    loop = data.get("canonical_loop", [])
    for required_step in [
        "qualify_method_on_declared_world_family",
        "qualify_detectability_on_predeclared_deployment_geometry",
        "apply_realized_observation_support_gate_before_opening_empirical_statistic",
    ]:
        assert required_step in loop, f"missing canonical admission step: {required_step}"
    assert len(loop) >= 10, "canonical loop is unexpectedly incomplete"

    print(
        "theory hierarchy valid:",
        len(ids), "nodes,",
        len(edge_rows), "edges,",
        len(firewall_pairs), "overlap firewalls,",
        "observation-support bridge enforced",
    )


if __name__ == "__main__":
    main()
