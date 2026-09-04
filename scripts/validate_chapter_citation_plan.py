from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "thesis" / "chapter_citation_plan.json"
REFS = ROOT / "thesis" / "prior_art_reference_registry.json"
RISKS = ROOT / "thesis" / "prior_art_risk_registry.json"
PROVED = ROOT / "thesis" / "proved_condition_registry.json"
DRAFT_STATUS = ROOT / "thesis" / "draft_status.json"

EXPECTED = ["chapter:introduction", *[f"chapter:{i}" for i in range(1, 9)], "chapter:synthesis"]
BLOCKED = (
    "we are the first",
    "for the first time",
    "first-ever",
    "novel theorem",
    "new mathematical principle",
    "previously unknown",
    "first proof of",
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    plan = load(PLAN)
    refs = load(REFS)
    risks = load(RISKS)
    proved = load(PROVED)
    draft_status = load(DRAFT_STATUS)

    assert plan["schema_version"] == "theouni-chapter-citation-plan.v1"
    assert plan["status"] == "citation_ready_for_research_chapters_pending_prose_integration"
    assert len(plan["writing_rule"]) >= 5

    units = plan["units"]
    assert [u["chapter"] for u in units] == EXPECTED
    assert len(units) == 10
    by_chapter = {u["chapter"]: u for u in units}

    ref_by_id = {r["id"]: r for r in refs["references"]}
    ref_links = {x["chapter"]: x for x in refs["chapter_links"]}
    risk_by_chapter = {u["chapter"]: u for u in risks["units"]}
    proved_by_chapter = {u["chapter"]: u for u in proved["units"]}

    for unit in units:
        chapter = unit["chapter"]
        for key in (
            "draft_file",
            "status",
            "reference_ids",
            "insertion_location",
            "concession_sentence",
            "contribution_sentence",
            "claim_ceiling",
            "v0_2_gate",
        ):
            assert key in unit, f"{chapter} missing {key}"
        assert unit["draft_file"] == draft_status["units"][chapter]["draft_file"]
        assert (ROOT / unit["draft_file"]).exists()
        for key in ("insertion_location", "concession_sentence", "contribution_sentence", "claim_ceiling", "v0_2_gate"):
            assert str(unit[key]).strip(), f"{chapter} empty {key}"
        combined = " ".join(
            [unit["concession_sentence"], unit["contribution_sentence"], unit["claim_ceiling"]]
        ).casefold()
        for phrase in BLOCKED:
            assert phrase not in combined, f"uncleared priority phrase in {chapter}: {phrase}"
        assert risk_by_chapter[chapter]["firstness_allowed"] is False
        for ref_id in unit["reference_ids"]:
            assert ref_id in ref_by_id, f"{chapter} unknown reference {ref_id}"

    # Research chapters must use exactly the citation-ready reference set already audited.
    for chapter in [f"chapter:{i}" for i in range(1, 9)]:
        unit = by_chapter[chapter]
        assert set(unit["reference_ids"]) == set(ref_links[chapter]["reference_ids"])
        assert unit["status"] in {"citation_ready", "citation_ready_priority_unresolved"}
        assert proved_by_chapter[chapter]["source_status"] == "merged"

    # Ch0 and Ch9 are deliberately different: Ch0 still needs its own prior-art audit;
    # Ch9 inherits chapter-specific literatures instead of inventing a global one.
    assert by_chapter["chapter:introduction"]["status"] == "pending_specific_prior_art_audit"
    assert by_chapter["chapter:introduction"]["reference_ids"] == []
    assert "functional coding" in by_chapter["chapter:introduction"]["v0_2_gate"].lower()
    assert by_chapter["chapter:synthesis"]["status"] == "synthesis_uses_chapter_specific_references"
    assert by_chapter["chapter:synthesis"]["reference_ids"] == []
    assert "chapter-specific" in by_chapter["chapter:synthesis"]["v0_2_gate"]

    # Priority-unresolved theorem-heavy chapters must say so in their prose plan.
    for chapter in ("chapter:5", "chapter:6", "chapter:7", "chapter:8"):
        unit = by_chapter[chapter]
        assert "unresolved" in (unit["status"] + " " + unit["claim_ceiling"]).lower()

    # Pin chapter-specific contribution anchors so the citation concession cannot swallow the result.
    assert "row-span" in by_chapter["chapter:1"]["contribution_sentence"]
    assert "sharp chance-discrimination endpoint" in by_chapter["chapter:2"]["contribution_sentence"]
    assert "branchwise condition" in by_chapter["chapter:3"]["contribution_sentence"]
    assert "locked eco-genetic" in by_chapter["chapter:4"]["contribution_sentence"]
    assert "simultaneous response-interface package" in by_chapter["chapter:5"]["contribution_sentence"]
    assert "one action and one added carrier world" in by_chapter["chapter:6"]["contribution_sentence"]
    assert "complete carried-map equality classes" in by_chapter["chapter:7"]["contribution_sentence"]
    assert "p*=2-2^(1/k)" in by_chapter["chapter:8"]["contribution_sentence"]

    print(
        "Validated chapter citation plan: Ch1-8 use exactly the audited reference sets, "
        "all concession/contribution pairs preserve claim ceilings, Ch0 remains pending its own audit, "
        "and Ch9 inherits chapter-specific literature rather than claiming a global priority surface."
    )


if __name__ == "__main__":
    main()
