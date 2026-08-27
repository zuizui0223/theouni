from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCHITECTURE = ROOT / "universe" / "dissertation_architecture.json"
ATLAS = ROOT / "universe" / "worldline_atlas.json"
REGISTRY = ROOT / "universe" / "registry.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    architecture = load(ARCHITECTURE)
    atlas = load(ATLAS)
    registry = load(REGISTRY)

    assert architecture["schema_version"] == "theouni-dissertation-architecture.v1"
    assert architecture["status"] == "preferred_editorial_traversal_not_privileged_theory_order"
    assert architecture["source_atlas"] == "universe/worldline_atlas.json"
    assert "Stop Travelling" in architecture["title"]

    worldline_ids = {item["id"] for item in atlas["worldlines"]}
    invariant_ids = {item["id"] for item in atlas["invariants"]}
    repository_ids = {item["id"] for item in registry["repositories"]}

    intro = architecture["general_introduction"]
    assert intro["id"] == "chapter:introduction"
    assert set(intro["invariants_imported"]) == invariant_ids
    assert len(intro["must_not_do"]) >= 3

    parts = sorted(architecture["parts"], key=lambda item: item["order"])
    assert [part["order"] for part in parts] == [1, 2, 3, 4]
    assert len({part["id"] for part in parts}) == 4
    assert all(len(part["chapters"]) == 2 for part in parts)

    chapters = [
        chapter
        for part in parts
        for chapter in sorted(part["chapters"], key=lambda item: item["order"])
    ]
    assert len(chapters) == 8
    assert [chapter["order"] for chapter in chapters] == list(range(1, 9))
    assert [chapter["id"] for chapter in chapters] == [f"chapter:{i}" for i in range(1, 9)]

    forbidden_inferences: set[str] = set()
    primary_modules: set[str] = set()
    covered_worldlines: set[str] = set()
    embedded_locations: dict[str, str] = {}

    for chapter in chapters:
        assert chapter["primary_worldlines"]
        assert set(chapter["primary_worldlines"]) <= worldline_ids
        covered_worldlines.update(chapter["primary_worldlines"])

        assert chapter["primary_source_repositories"]
        assert set(chapter["primary_source_repositories"]) <= repository_ids
        assert "repo:theouni" not in chapter["primary_source_repositories"]

        assert len(chapter["primary_modules"]) == 1
        module = chapter["primary_modules"][0]
        assert module not in primary_modules
        primary_modules.add(module)

        inference = chapter["primary_forbidden_inference"].strip()
        assert inference
        assert inference not in forbidden_inferences
        forbidden_inferences.add(inference)

        assert chapter["headline_result"].strip()
        assert chapter["novelty_role"].strip()
        assert chapter["ecological_payoff"].strip()
        assert chapter["transition_question"].strip().endswith("?")

        for embedded in chapter["embedded_theouni_modules"]:
            assert embedded in {"TU-2", "TU-3", "TU-4"}
            assert embedded not in embedded_locations
            embedded_locations[embedded] = chapter["id"]

    synthesis = architecture["general_synthesis"]
    assert synthesis["id"] == "chapter:synthesis"
    assert synthesis["primary_worldlines"] == ["worldline:revision"]
    assert synthesis["primary_source_repositories"] == ["repo:theouni"]
    assert "TU-1" in synthesis["primary_modules"]
    assert synthesis["primary_forbidden_inference"].strip()
    assert synthesis["independent_chapter_upgrade_condition"].strip()
    covered_worldlines.update(synthesis["primary_worldlines"])
    embedded_locations["TU-1"] = synthesis["id"]

    assert covered_worldlines == worldline_ids
    assert embedded_locations == architecture["embedded_module_allocation"]
    assert architecture["embedded_module_allocation"] == {
        "TU-1": "chapter:synthesis",
        "TU-2": "chapter:6",
        "TU-3": "chapter:7",
        "TU-4": "chapter:8",
    }

    preferred = architecture["preferred_sequence"]
    expected = [
        "chapter:introduction",
        *[chapter["id"] for chapter in chapters],
        "chapter:synthesis",
    ]
    assert preferred == expected
    position = {item: index for index, item in enumerate(preferred)}

    dependencies = architecture["scientific_dependencies"]
    assert dependencies == [
        {
            "source": "chapter:7",
            "target": "chapter:8",
            "relation": "loss_domain_must_be_fixed_warning_blind_before_warning_evaluation",
        }
    ]
    assert all(position[item["source"]] < position[item["target"]] for item in dependencies)

    chapter_by_worldline = {
        worldline: chapter["id"]
        for chapter in chapters
        for worldline in chapter["primary_worldlines"]
    }
    assert chapter_by_worldline["worldline:loss"] == "chapter:7"
    assert chapter_by_worldline["worldline:warning"] == "chapter:8"
    assert "worldline:revision" not in chapter_by_worldline

    assert len(architecture["novelty_firewalls"]) >= 7
    assert any("purpose relativity" in item for item in architecture["novelty_firewalls"])
    assert any("global consistency" in item for item in architecture["novelty_firewalls"])

    print(
        "Validated preferred dissertation architecture: "
        f"4 parts, {len(chapters)} source-owned research chapters, "
        "TU-2/TU-3/TU-4 embedded, TU-1 in synthesis, all 9 worldlines covered, "
        "and Loss -> Warning dependency preserved."
    )


if __name__ == "__main__":
    main()
