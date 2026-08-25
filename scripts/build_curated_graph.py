import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def slug(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    return value.strip("_") or "item"


def main() -> None:
    registry_path = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "universe" / "registry.json"
    output_path = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else ROOT / "graphify-out" / ".curated_extraction.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    nodes: list[dict] = []
    edges: list[dict] = []
    node_ids: set[str] = set()

    def add_node(node: dict) -> None:
        if node["id"] in node_ids:
            return
        node_ids.add(node["id"])
        nodes.append(node)

    def add_edge(source: str, target: str, relation: str, *, confidence: str = "EXTRACTED", context: str = "registry", location: str = "") -> None:
        edges.append(
            {
                "source": source,
                "target": target,
                "relation": relation,
                "context": context,
                "confidence": confidence,
                "source_file": str(registry_path),
                "source_location": location,
                "weight": 1.0,
            }
        )

    program_id = "program:ecological_research_universe"
    add_node(
        {
            "id": program_id,
            "label": "Zuizui0223 ecological research universe",
            "file_type": "program",
            "source_file": str(registry_path),
            "source_location": "/scope",
            "_origin": "curated_registry",
            "repo": "portfolio",
        }
    )

    class_ids = {}
    for name, definition in registry["classification_vocabulary"].items():
        node_id = f"classification:{name}"
        class_ids[name] = node_id
        add_node(
            {
                "id": node_id,
                "label": name.replace("_", " ").title(),
                "description": definition,
                "file_type": "classification",
                "source_file": str(registry_path),
                "source_location": f"/classification_vocabulary/{name}",
                "_origin": "curated_registry",
                "repo": "portfolio",
            }
        )
        add_edge(program_id, node_id, "uses_classification", location=f"/classification_vocabulary/{name}")

    for index, concept in enumerate(registry["ontology"]):
        add_node(
            {
                "id": concept["id"],
                "label": concept["label"],
                "description": concept["definition"],
                "condition": concept.get("condition", ""),
                "file_type": "ontology_concept",
                "source_file": str(registry_path),
                "source_location": f"/ontology/{index}",
                "_origin": "curated_registry",
                "repo": ",".join(owner.removeprefix("repo:") for owner in concept["owned_by"]),
            }
        )
        add_edge(program_id, concept["id"], "contains_concept", location=f"/ontology/{index}")
        for owner in concept["owned_by"]:
            add_edge(owner, concept["id"], "defines", location=f"/ontology/{index}/owned_by")
        for classification in concept["classification"]:
            add_edge(concept["id"], class_ids[classification], "classified_as", location=f"/ontology/{index}/classification")

    evidence_nodes: dict[str, str] = {}
    layer_nodes: dict[str, str] = {}
    status_nodes: dict[str, str] = {}

    for index, repo in enumerate(registry["repositories"]):
        repo_id = repo["id"]
        add_node(
            {
                "id": repo_id,
                "label": repo["name"],
                "description": "; ".join(repo["owns"]),
                "file_type": "repository",
                "source_file": str(registry_path),
                "source_location": f"/repositories/{index}",
                "_origin": "curated_registry",
                "repo": repo["name"],
                "url": repo["url"],
                "snapshot_sha": repo["snapshot_sha"],
                "status": repo["status"],
            }
        )
        add_edge(program_id, repo_id, "contains_repository", location=f"/repositories/{index}")

        status_id = status_nodes.setdefault(repo["status"], f"repo_status:{slug(repo['status'])}")
        add_node(
            {
                "id": status_id,
                "label": repo["status"].replace("_", " ").title(),
                "file_type": "repository_status",
                "source_file": str(registry_path),
                "source_location": f"/repositories/{index}/status",
                "_origin": "curated_registry",
                "repo": "portfolio",
            }
        )
        add_edge(repo_id, status_id, "has_status", location=f"/repositories/{index}/status")

        for layer in repo["layer"]:
            layer_id = layer_nodes.setdefault(layer, f"layer:{slug(layer)}")
            add_node(
                {
                    "id": layer_id,
                    "label": layer.replace("_", " ").title(),
                    "file_type": "research_layer",
                    "source_file": str(registry_path),
                    "source_location": f"/repositories/{index}/layer",
                    "_origin": "curated_registry",
                    "repo": "portfolio",
                }
            )
            add_edge(repo_id, layer_id, "works_in_layer", location=f"/repositories/{index}/layer")

        for object_index, label in enumerate(repo["objects"]):
            object_id = f"object:{repo['name']}:{slug(label)}"
            add_node(
                {
                    "id": object_id,
                    "label": f"{repo['name']}: {label}",
                    "file_type": "ontology_object",
                    "source_file": str(registry_path),
                    "source_location": f"/repositories/{index}/objects/{object_index}",
                    "_origin": "curated_registry",
                    "repo": repo["name"],
                }
            )
            add_edge(repo_id, object_id, "owns_object", location=f"/repositories/{index}/objects/{object_index}")

        for claim_index, claim in enumerate(repo["claims"]):
            claim_id = f"claim:{repo['name']}:{claim_index + 1}"
            add_node(
                {
                    "id": claim_id,
                    "label": claim["summary"],
                    "claim_status": claim["status"],
                    "file_type": "claim",
                    "source_file": str(registry_path),
                    "source_location": f"/repositories/{index}/claims/{claim_index}",
                    "_origin": "curated_registry",
                    "repo": repo["name"],
                }
            )
            add_edge(repo_id, claim_id, "supports_claim", location=f"/repositories/{index}/claims/{claim_index}")

        nonclaim_id = f"nonclaim:{repo['name']}"
        add_node(
            {
                "id": nonclaim_id,
                "label": "Explicit non-claims: " + "; ".join(repo["non_claims"]),
                "file_type": "non_claim",
                "source_file": str(registry_path),
                "source_location": f"/repositories/{index}/non_claims",
                "_origin": "curated_registry",
                "repo": repo["name"],
            }
        )
        add_edge(repo_id, nonclaim_id, "explicitly_does_not_claim", location=f"/repositories/{index}/non_claims")

        for evidence in repo["evidence_types"]:
            evidence_id = evidence_nodes.setdefault(evidence, f"evidence:{slug(evidence)}")
            add_node(
                {
                    "id": evidence_id,
                    "label": evidence,
                    "file_type": "evidence_type",
                    "source_file": str(registry_path),
                    "source_location": f"/repositories/{index}/evidence_types",
                    "_origin": "curated_registry",
                    "repo": "portfolio",
                }
            )
            add_edge(repo_id, evidence_id, "uses_evidence", location=f"/repositories/{index}/evidence_types")

    for index, relation in enumerate(registry["relations"]):
        status = relation.get("status", "declared")
        confidence = "EXTRACTED"
        if status in {
            "proposed",
            "schema_missing",
            "missing",
            "conceptual",
            "external_case_only",
            "partial_bounded_witness_only",
        }:
            confidence = "INFERRED"
        if status in {"not_implemented"}:
            confidence = "AMBIGUOUS"
        add_edge(
            relation["source"],
            relation["target"],
            relation["type"],
            confidence=confidence,
            context=relation["contract"],
            location=f"/relations/{index}",
        )

    for index, item in enumerate(registry["definability_ledger"]):
        question_id = f"definability_question:{index + 1:02d}"
        add_node(
            {
                "id": question_id,
                "label": item["question"],
                "description": item["reason"],
                "file_type": "definability_question",
                "source_file": str(registry_path),
                "source_location": f"/definability_ledger/{index}",
                "_origin": "curated_registry",
                "repo": "portfolio",
            }
        )
        add_edge(program_id, question_id, "asks", location=f"/definability_ledger/{index}")
        add_edge(question_id, class_ids[item["classification"]], "classified_as", location=f"/definability_ledger/{index}/classification")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(
            {
                "nodes": nodes,
                "edges": edges,
                "hyperedges": [],
                "input_tokens": 0,
                "output_tokens": 0,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    print(f"Curated extraction: {len(nodes)} nodes, {len(edges)} edges")


if __name__ == "__main__":
    main()
