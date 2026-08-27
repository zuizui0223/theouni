from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "thesis" / "chapter_registry.json"
DRAFT_STATUS = ROOT / "thesis" / "draft_status.json"
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
ALLOWED_DRAFT_STAGES = {
    "brief_only",
    "draft_v0_1",
    "draft_v0_2",
    "citation_ready",
    "chapter_integrated",
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


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE))


def main() -> None:
    registry = load(REGISTRY)
    draft_status = load(DRAFT_STATUS)
    architecture = load(ARCHITECTURE)
    universe = load(UNIVERSE)

    units = registry["units"]
    assert len(units) == 10
    assert [unit["order"] for unit in units] == list(range(10))
    assert [unit["id"] for unit in units] == architecture["preferred_sequence"]
    assert len({unit["id"] for unit in units}) == len(units)
    assert len({unit["file"] for unit in units}) == len(units)
    assert len({unit["forbidden_inference"] for unit in units}) == len(units)

    unit_ids = {unit["id"] for unit in units}
    assert set(draft_status["units"]) == unit_ids

    arch_by_id = architecture_units(architecture)
    assert set(arch_by_id) == unit_ids

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

    drafted_units = 0
    draft_word_counts: dict[str, int] = {}
    for unit in units:
        progress = draft_status["units"][unit["id"]]
        assert progress["stage"] in ALLOWED_DRAFT_STAGES
        assert progress["next_action"].strip()

        if progress["stage"] == "brief_only":
            assert progress["draft_file"] is None
            assert progress["source_map_file"] is None
            continue

        drafted_units += 1
        assert progress["draft_file"]
        assert progress["source_map_file"]
        draft_path = ROOT / progress["draft_file"]
        source_map_path = ROOT / progress["source_map_file"]
        assert draft_path.is_file(), progress["draft_file"]
        assert source_map_path.is_file(), progress["source_map_file"]

        draft_text = draft_path.read_text(encoding="utf-8")
        source_map_text = source_map_path.read_text(encoding="utf-8")
        assert f"<!-- draft-id: {unit['id']}:" in draft_text
        assert unit["title"] in draft_text
        assert "## Internal source keys" in draft_text
        assert "## Section-to-source matrix" in source_map_text

        word_count = count_words(draft_text)
        assert word_count >= progress.get("minimum_words", 0)
        draft_word_counts[unit["id"]] = word_count

    assert drafted_units >= 1

    source_counts = sum(len(unit["canonical_sources"]) for unit in units)
    draft_summary = ", ".join(f"{unit_id}={words} words" for unit_id, words in draft_word_counts.items())
    print(
        f"Validated thesis workspace: {len(units)} units, {len(research_units)} source-owned research chapters, "
        f"{source_counts} canonical source handoffs, {drafted_units} drafted unit(s) ({draft_summary}), "
        "unique forbidden inferences, TU allocation, and Loss->Warning dependency."
    )


if __name__ == "__main__":
    main()
