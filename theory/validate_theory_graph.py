from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THEORY = ROOT / "theory"


def load(name: str) -> dict:
    return json.loads((THEORY / name).read_text(encoding="utf-8"))


def assert_acyclic(nodes: set[str], edges: list[dict]) -> None:
    adjacency = {node: [] for node in nodes}
    indegree = {node: 0 for node in nodes}
    for edge in edges:
        source = edge["source"]
        target = edge["target"]
        adjacency[source].append(target)
        indegree[target] += 1

    queue = [node for node, degree in indegree.items() if degree == 0]
    visited = 0
    while queue:
        node = queue.pop()
        visited += 1
        for target in adjacency[node]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)

    assert visited == len(nodes), "theorem dependency graph contains a directed cycle"


def main() -> None:
    core = load("core_universe.json")
    graph = load("theorem_graph.json")

    assert core["schema_version"] == "theouni-theory-core.v0.5"
    assert graph["schema_version"] == "theouni-theorem-graph.v0.5"
    assert graph["orientation"] == "prerequisite_to_dependent"

    graph_nodes = graph["nodes"]
    node_ids = [node["id"] for node in graph_nodes]
    assert len(node_ids) == len(set(node_ids)), "duplicate theorem-graph node id"
    node_set = set(node_ids)

    for edge in graph["edges"]:
        assert edge["source"] in node_set, edge
        assert edge["target"] in node_set, edge
        assert edge["source"] != edge["target"], edge
        assert edge["relation"].strip(), edge

    assert_acyclic(node_set, graph["edges"])

    theorem_modules = {item["id"]: item for item in core["theorem_modules"]}
    assert set(theorem_modules) == {"TU-1", "TU-2", "TU-3", "TU-4"}

    graph_modules = {
        node["id"].split(":", 1)[1]
        for node in graph_nodes
        if node["type"] == "theouni_theorem_module"
    }
    assert graph_modules == set(theorem_modules), "core/graph theorem-module drift"

    for module_id, module in theorem_modules.items():
        source = ROOT / module["source"]
        registry = ROOT / module["registry"]
        verification = ROOT / module["verification"]
        assert source.is_file(), source
        assert registry.is_file(), registry
        assert verification.is_file(), verification

        registry_payload = json.loads(registry.read_text(encoding="utf-8"))
        registry_text = json.dumps(registry_payload, ensure_ascii=False)
        assert module_id in registry_text, f"{module_id} absent from its registry"
        assert module["claim_ceiling"].strip(), module_id

    required_types = {
        "type:RequiredState",
        "type:StoredStateRepresentation",
        "type:EvidenceClass",
        "type:AdmissibleCausalSet",
        "type:CausalLearningValue",
        "type:TargetLicensingStatus",
        "type:LossGeneratingState",
        "type:WarningEvaluationState",
        "type:WarningPortability",
    }
    core_types = {item["id"] for item in core["types"]}
    assert required_types <= core_types

    canonical_edges = {
        (edge["source"], edge["target"], edge["relation"])
        for edge in graph["edges"]
    }
    must_exist = {
        ("concept:StoredState", "theorem:TU-1", "input"),
        ("concept:EvidenceClass", "theorem:TU-2", "licensing_input"),
        ("concept:AdmissibleCausalSet", "theorem:TU-2", "learning_input"),
        ("theorem:TU-3", "concept:LossGeneratingState", "formalizes"),
        ("concept:LossGeneratingState", "theorem:TU-4", "conditioning_input"),
        ("theorem:TU-4", "concept:WarningEvaluationState", "formalizes"),
    }
    assert must_exist <= canonical_edges, "missing canonical theorem dependencies"

    open_nodes = [node for node in graph_nodes if node["type"] == "open_problem"]
    assert open_nodes, "theory graph must preserve explicit open problems"
    assert all(node["status"] == "open" for node in open_nodes)

    assert (THEORY / "CONSTITUTION.md").is_file()
    constitution = (THEORY / "CONSTITUTION.md").read_text(encoding="utf-8")
    for label in ("A0", "A12", "TU-1", "TU-2", "TU-3", "TU-4"):
        assert label in constitution, f"constitution missing {label}"

    print(
        "Theory graph v0.5 validated: "
        f"{len(node_ids)} nodes, {len(graph['edges'])} dependency edges, "
        f"{len(theorem_modules)} theouni theorem modules, {len(open_nodes)} open problems."
    )


if __name__ == "__main__":
    main()
