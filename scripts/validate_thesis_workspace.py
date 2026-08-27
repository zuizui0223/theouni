from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "thesis" / "chapter_registry.json"
ARCHITECTURE = ROOT / "universe" / "dissertation_architecture.json"
UNIVERSE = ROOT / "universe" / "registry.json"

REQUIRED_HEADINGS = (
    "## Problem",
    "## Headline result",
    "## Why the result is nontrivial",
    "## Ecological payoff",
    "## Claim ceiling",
    "## Canonical source handoff",
    "## Transition",
)
EXPECTED_EMBEDDED = {
    "TU-1": "chapter:synthesis",
    "TU-2": "chapter:6",
    "TU-3": "chapter:7",
    "TU-4": "chapter:8",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def architecture_units(architecture: dict) -> dict[str, dict]:
    units: dict[str, dict] = {
        architecture["general_introduction"]["id"]: architecture["general_introduction"]
    }
    for part in architecture["parts"]:
        for chapter in part["chapters"]:
            units[chapter["id"]] = chapter
    units[architecture["general_synthesis"]["id"]] = architecture["general_synthesis"]
    return units


def main() -> None:
    registry = load(REGISTRY)
    architecture = load(ARCHITECTURE)
    universe = load(UNIVERSE)

    units = registry["units"]
    assert len(units) == 10
    assert [unit["order"] for unit in units] == list(range(10))
    assert [unit["id"] for unit in units] == architecture["preferred_sequence"]
    assert len({unit["id"] for unit in units}) == len(units)
    assert len({unit["file"] for unit in units}) == len(units)
    assert len({unit["forbidden_inference"] for unit in units}) == len(units)

    arch_by_id = architecture_units(architecture)
    assert set(arch_by_id) == {unit["id"] for unit in units}

    repo_ids = {repo["id"] for repo in universe["repositories"]}
    research_units = [unit for unit in units if unit["kind"] == "research_chapter"]
    assert len(research_units) == 8
    assert len({unit["primary_source_repositories"][0] for unit in research_units}) == 8
    assert all(unit["primary_source_repositories"][0] != "repo:theouni" for unit in research_units)

    allowed_statuses = {
        "brief_ready",
        "source_manuscript_available",
        "source_manuscript_in_conversion",
        "source_results_drafted",
        "source_theorem_core_available",
        "source_paper_core_available",
        "source_submission_frozen",
        "source_scientific_campaign_closed",
        "source_integrated_manuscript_active",
    }

    for unit in units:
        assert unit["status"] in allowed_statuses
        assert unit["primary_source_repositories"]
        assert all(repo in repo_ids for repo in unit["primary_source_repositories"])
        assert unit["headline_result"].strip()
        assert unit["forbidden_inference"].strip()
        assert unit["canonical_sources"]

        arch = arch_by_id[unit["id"]]
        assert unit["title"] == arch["title"]
        if unit["id"].startswith("chapter:") and unit["id"] not in {"chapter:introduction", "chapter:synthesis"}:
            assert unit["primary_source_repositories"] == arch["primary_source_repositories"]
            assert unit["primary_modules"] == arch["primary_modules"]
            assert unit["embedded_modules"] == arch["embedded_theouni_modules"]
            assert unit["forbidden_inference"] == arch["primary_forbidden_inference"]
        elif unit["id"] == "chapter:synthesis":
            assert unit["primary_source_repositories"] == arch["primary_source_repositories"]
            assert unit["primary_modules"] == arch["primary_modules"]
            assert unit["forbidden_inference"] == arch["primary_forbidden_inference"]

        path = ROOT / unit["file"]
        assert path.is_file(), unit["file"]
        text = path.read_text(encoding="utf-8")
        assert f"<!-- chapter-id: {unit['id']} -->" in text
        assert unit["title"] in text
        for heading in REQUIRED_HEADINGS:
            assert heading in text, f"{unit['file']} missing {heading}"

    assert registry["embedded_module_allocation"] == EXPECTED_EMBEDDED
    observed_embedded = {
        module: unit["id"]
        for unit in units
        for module in unit["embedded_modules"]
    }
    observed_embedded["TU-1"] = "chapter:synthesis"
    assert observed_embedded == EXPECTED_EMBEDDED

    assert registry["hard_dependencies"] == [
        {
            "source": "chapter:7",
            "target": "chapter:8",
            "relation": "loss domain must be fixed warning-blind before warning evaluation",
        }
    ]

    source_counts = sum(len(unit["canonical_sources"]) for unit in units)
    print(
        f"Validated thesis workspace: {len(units)} units, {len(research_units)} source-owned research chapters, "
        f"{source_counts} canonical source handoffs, unique forbidden inferences, TU allocation, and Loss->Warning dependency."
    )


if __name__ == "__main__":
    main()
