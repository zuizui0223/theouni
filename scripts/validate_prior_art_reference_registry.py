from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT / "thesis" / "prior_art_reference_registry.json"
RISKS = ROOT / "thesis" / "prior_art_risk_registry.json"
PROVED = ROOT / "thesis" / "proved_condition_registry.json"
MATRIX = ROOT / "thesis" / "PRIOR_ART_COMPARISON_MATRIX_2026-09-04.md"

EXPECTED_RESEARCH = [f"chapter:{i}" for i in range(1, 9)]
EXPECTED_UNLINKED = ["chapter:introduction", "chapter:synthesis"]
ALLOWED_ROLES = {
    "foundational_classical_substrate",
    "direct_nearest_neighbour",
    "adjacent_methodological_substrate",
    "direct_ecological_precedent",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    registry = load(REFS)
    risks = load(RISKS)
    proved = load(PROVED)
    matrix = MATRIX.read_text(encoding="utf-8")

    assert registry["schema_version"] == "theouni-prior-art-reference-registry.v1"
    assert registry["status"] == "citation_ready_core_neighbours_with_priority_unresolved"
    assert registry["verified_on"] == "2026-09-04"
    assert "No entry" in registry["policy"]["priority_rule"]

    refs = registry["references"]
    ids = [ref["id"] for ref in refs]
    assert len(refs) >= 19
    assert len(ids) == len(set(ids))
    by_id = {ref["id"]: ref for ref in refs}

    for ref in refs:
        assert ref["authors"]
        assert isinstance(ref["year"], int) and 1900 <= ref["year"] <= 2026
        assert ref["title"].strip()
        assert ref["venue"].strip()
        assert ref["metadata_status"].startswith("verified_")
        assert ref["role"] in ALLOWED_ROLES
        doi = ref.get("doi")
        if doi is not None:
            assert doi.startswith("10.")
            assert ref.get("identifier_url", "").startswith("https://doi.org/")
        else:
            assert ref.get("identifier_url") or ref.get("alternate_identifier") or ref["id"] in {
                "debreu_1954",
                "ashby_1956",
            }

    links = registry["chapter_links"]
    assert [link["chapter"] for link in links] == EXPECTED_RESEARCH
    assert len({link["chapter"] for link in links}) == 8

    risk_by_chapter = {u["chapter"]: u for u in risks["units"]}
    proved_by_chapter = {u["chapter"]: u for u in proved["units"]}
    used_ids: set[str] = set()
    for link in links:
        chapter = link["chapter"]
        assert link["reference_ids"]
        assert link["comparison_status"].strip()
        assert link["what_remains"].strip()
        for ref_id in link["reference_ids"]:
            assert ref_id in by_id, f"{chapter} cites unknown prior-art id {ref_id}"
            used_ids.add(ref_id)
        assert risk_by_chapter[chapter]["firstness_allowed"] is False
        assert proved_by_chapter[chapter]["source_status"] == "merged"

    # Every citation-ready entry in this core registry is actually used by at least one chapter.
    assert used_ids == set(ids)

    # Pin the strongest nearest-neighbour sets.
    refs_by_chapter = {link["chapter"]: set(link["reference_ids"]) for link in links}
    assert refs_by_chapter["chapter:1"] == {"bellman_astrom_1970"}
    assert {"boettiger_hastings_2012", "boettiger_hastings_2013"} <= refs_by_chapter["chapter:2"]
    assert {"lindley_1956", "golovin_krause_2011"} <= refs_by_chapter["chapter:3"]
    assert {"debreu_1954", "herden_levin_2012"} <= refs_by_chapter["chapter:4"]
    assert {
        "crutchfield_young_1989",
        "krohn_mateosian_rhodes_1967",
        "domosi_nehaniv_2000",
        "baburin_cotterell_2024",
    } <= refs_by_chapter["chapter:5"]
    assert {"ashby_1956", "conant_ashby_1970", "givan_dean_greig_2003"} <= refs_by_chapter["chapter:6"]
    assert {"givan_dean_greig_2003", "ravindran_barto_2003"} <= refs_by_chapter["chapter:7"]
    assert {
        "mackenzie_nichols_et_al_2002",
        "mackenzie_royle_2005",
        "bailey_hines_nichols_mackenzie_2007",
        "littlewood_1996",
    } <= refs_by_chapter["chapter:8"]

    # Tier-A chapters need more than one direct nearest neighbour, not one token citation.
    for chapter in ("chapter:5", "chapter:6", "chapter:7"):
        direct = [
            ref_id
            for ref_id in refs_by_chapter[chapter]
            if by_id[ref_id]["role"] == "direct_nearest_neighbour"
        ]
        assert len(direct) >= 2, f"{chapter} lacks multiple direct nearest-neighbour anchors"
        assert "unresolved" in risk_by_chapter[chapter]["priority_status"]

    unlinked = registry["unlinked_units"]
    assert [u["chapter"] for u in unlinked] == EXPECTED_UNLINKED
    assert all(u["reason"].strip() for u in unlinked)

    # Human-readable matrix must explicitly preserve the priority boundary.
    assert "not the same quantifier" in matrix.lower()
    assert "historical priority remains blocked" in matrix.lower()
    for chapter in range(1, 9):
        assert f"## Chapter {chapter}" in matrix
    assert "package_distinctness_plausible_but_priority_unresolved" in matrix
    assert "p*_k = 2 - 2^(1/k)" in matrix

    print(
        f"Validated prior-art references: {len(refs)} citation-ready core entries linked to "
        "all 8 source-owned research chapters; Tier-A chapters have multiple direct neighbours "
        "and all historical-priority gates remain unresolved/blocked."
    )


if __name__ == "__main__":
    main()
