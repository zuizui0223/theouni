from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "thesis" / "chapter_registry.json"
DRAFT_STATUS = ROOT / "thesis" / "draft_status.json"
ARCHITECTURE = ROOT / "thesis" / "final_chapter_architecture.json"

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


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    registry = load(REGISTRY)
    draft_status = load(DRAFT_STATUS)
    architecture = load(ARCHITECTURE)

    assert architecture["schema_version"] == "theouni-final-chapter-architecture.v1"
    assert architecture["status"] == "final_editorial_order_forbidden_inference_spine"
    assert registry["architecture_source"] == "thesis/final_chapter_architecture.json"

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
    assert set(draft_status["units"]) == {u["id"] for u in units}
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
        assert progress["stage"] == "brief_only"
        assert progress["draft_file"] is None and progress["source_map_file"] is None
        assert progress["next_action"].strip()

    forbidden_chain = [u["forbidden_inference"] for u in units]
    assert "観測を豊かにした ⇒ 潜在機構に近づいた" in forbidden_chain
    assert "損失に先行した ⇒ 損失を予告する" in forbidden_chain
    assert "同じ手法を繰り返した ⇒ 証拠が強くなった" in forbidden_chain

    print("Validated final ten-chapter forbidden-inference spine: 0 Reuse, 1 Boundary, 2 EGWE, 3 MROD, 4 EcoGenCriticality, 5 CCOC, 6 CREST, 7 MLTR, 8 CED, 9 TU-1 synthesis; MRM/RACH retained as companions.")


if __name__ == "__main__":
    main()
