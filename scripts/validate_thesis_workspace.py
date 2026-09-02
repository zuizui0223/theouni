from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "thesis" / "chapter_registry.json"
DRAFT_STATUS = ROOT / "thesis" / "draft_status.json"
ARCHITECTURE = ROOT / "thesis" / "final_chapter_architecture.json"
RECOVERY = ROOT / "thesis" / "verification_recovery_registry.json"

REQUIRED_HEADINGS = (
    "## Problem",
    "## Headline result",
    "## Why the result is nontrivial",
    "## Ecological payoff",
    "## Claim ceiling",
    "## Canonical source handoff",
    "## Transition",
)
EXPECTED_PRIMARY = [
    "repo:theouni",
    "repo:boundary",
    "repo:eco-genetic-warning-extensions",
    "repo:mrod",
    "repo:eco-genetic-criticality",
    "repo:ccoc",
    "repo:crest",
    "repo:mltr",
    "repo:ced",
    "repo:theouni",
]
EXPECTED_EMBEDDED = {"TU-1":"chapter:synthesis","TU-2":"chapter:3","TU-3":"chapter:4","TU-4":"chapter:2"}
ALLOWED_DRAFT_STAGES = {"brief_only", "draft_v0_1", "draft_v0_2", "citation_ready", "chapter_integrated"}
INTERNAL_SOURCE_TAG = re.compile(r"\[(?:[A-Z][A-Z0-9]*)(?:\s*,\s*[A-Z][A-Z0-9]*)*\]")


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE))


def main() -> None:
    registry = load(REGISTRY)
    draft_status = load(DRAFT_STATUS)
    architecture = load(ARCHITECTURE)
    recovery = load(RECOVERY)

    assert architecture["schema_version"] == "theouni-final-chapter-architecture.v1"
    assert architecture["status"] == "final_editorial_order_forbidden_inference_spine"
    assert registry["architecture_source"] == "thesis/final_chapter_architecture.json"
    assert draft_status["schema_version"] == "theouni-thesis-draft-status.v3"
    assert draft_status["status"] == "progressive_source_bounded_redraft_under_final_architecture"

    chapters = architecture["chapters"]
    units = registry["units"]
    assert len(chapters) == len(units) == 10
    assert [c["order"] for c in chapters] == list(range(10))
    assert [u["order"] for u in units] == list(range(10))
    assert [c["id"] for c in chapters] == architecture["preferred_sequence"]
    assert [u["id"] for u in units] == architecture["preferred_sequence"]
    assert [u["primary_source_repositories"][0] for u in units] == EXPECTED_PRIMARY
    assert len({u["forbidden_inference"] for u in units}) == 10
    assert units[-1]["forbidden_inference"] == "より詳細にする／より多く測る／より長く記憶する／より多く介入する ⇒ より妥当になる"

    source_map = architecture["source_repository_map"]
    assert source_map["repo:boundary"] == "zuizui0223/boundary"
    assert source_map["repo:mrod"] == "zuizui0223/mrod"
    assert architecture["companion_programmes"]["MRM"]["repository"] == "repo:mrm"
    assert architecture["companion_programmes"]["RACH"]["repository"] == "repo:microdonta"
    primary_modules = [u["primary_modules"][0] for u in units]
    assert "MRM" not in primary_modules and "RACH" not in primary_modules

    observed_embedded = {module: unit["id"] for unit in units for module in unit["embedded_modules"]}
    observed_embedded["TU-1"] = "chapter:synthesis"
    assert observed_embedded == EXPECTED_EMBEDDED
    assert registry["embedded_module_allocation"] == EXPECTED_EMBEDDED
    assert architecture["embedded_module_allocation"] == EXPECTED_EMBEDDED

    assert registry["hard_dependencies"] == []
    assert architecture["source_preconditions"] == registry["source_preconditions"]
    assert architecture["source_preconditions"][0]["chapter"] == "chapter:2"
    assert "frozen" in architecture["source_preconditions"][0]["condition"].lower()

    arch_by_id = {c["id"]: c for c in chapters}
    recovery_by_id = {c["id"]: c for c in recovery["chapters"]}
    assert set(draft_status["units"]) == {u["id"] for u in units}
    assert set(recovery_by_id) == {u["id"] for u in units}

    drafted_ids: list[str] = []
    for unit in units:
        arch = arch_by_id[unit["id"]]
        assert unit["title"] == arch["title"]
        assert unit["english_title"] == arch["english_title"]
        assert unit["primary_source_repositories"] == arch["primary_source_repositories"]
        assert unit["primary_modules"] == arch["primary_modules"]
        assert unit["embedded_modules"] == arch["embedded_theouni_modules"]
        assert unit["forbidden_inference"] == arch["primary_forbidden_inference"]
        assert unit["canonical_sources"] == arch["canonical_sources"]

        chapter_path = ROOT / unit["file"]
        assert chapter_path.is_file(), unit["file"]
        text = chapter_path.read_text(encoding="utf-8")
        assert f"<!-- chapter-id: {unit['id']} -->" in text
        assert unit["title"] in text
        assert unit["forbidden_inference"] in text
        for heading in REQUIRED_HEADINGS:
            assert heading in text, f"{unit['file']} missing {heading}"

        progress = draft_status["units"][unit["id"]]
        assert progress["stage"] in ALLOWED_DRAFT_STAGES
        assert progress["next_action"].strip()

        if progress["stage"] == "brief_only":
            assert progress["draft_file"] is None and progress["source_map_file"] is None
            continue

        drafted_ids.append(unit["id"])
        assert progress["draft_file"] and progress["source_map_file"]
        assert progress["draft_file"].startswith("thesis/drafts/final/")
        assert progress["source_map_file"].startswith("thesis/source_maps/final/")

        draft_path = ROOT / progress["draft_file"]
        source_map_path = ROOT / progress["source_map_file"]
        assert draft_path.is_file(), progress["draft_file"]
        assert source_map_path.is_file(), progress["source_map_file"]

        draft_text = draft_path.read_text(encoding="utf-8")
        source_text = source_map_path.read_text(encoding="utf-8")
        assert f"<!-- draft-id: {unit['id']}:" in draft_text
        assert unit["title"] in draft_text
        assert "## Section-to-source matrix" in source_text
        assert unit["forbidden_inference"] in source_text
        assert "claim ceiling" in source_text.lower()
        assert count_words(draft_text) >= progress.get("minimum_words", 0)

        recovered = recovery_by_id[unit["id"]]
        assert recovered["forbidden_inference"] == unit["forbidden_inference"]
        if unit["kind"] == "research_chapter":
            assert recovered["source_snapshot_sha"] in source_text
            assert recovered["claim_ceiling"][:45] in source_text or "chapter claim ceiling" in source_text.lower()

        if progress["stage"] == "draft_v0_1":
            assert "## Internal source keys" in draft_text
        else:
            assert "## References" in draft_text
            assert "## Internal source keys" not in draft_text
            assert not INTERNAL_SOURCE_TAG.search(draft_text)

    # Progressive drafting is sequential under the final editorial order.
    drafted_positions = [architecture["preferred_sequence"].index(i) for i in drafted_ids]
    if drafted_positions:
        assert drafted_positions == list(range(max(drafted_positions) + 1)), (
            "drafted chapters must form a contiguous prefix of the final chapter order"
        )

    # Current recovery milestone: Chapters 0 and 1 are the first rebuilt units.
    assert drafted_ids[:2] == ["chapter:introduction", "chapter:1"]

    forbidden_chain = [u["forbidden_inference"] for u in units]
    assert "観測を豊かにした ⇒ 潜在機構に近づいた" in forbidden_chain
    assert "損失に先行した ⇒ 損失を予告する" in forbidden_chain
    assert "同じ手法を繰り返した ⇒ 証拠が強くなった" in forbidden_chain

    print(
        "Validated final ten-chapter forbidden-inference spine with progressive source-bounded drafting: "
        f"{len(drafted_ids)} current draft(s) ({', '.join(drafted_ids) or 'none'}); MRM/RACH retained as companions."
    )


if __name__ == "__main__":
    main()
