from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SERIES = ROOT / "thesis" / "series_architecture.json"
LEGACY = ROOT / "thesis" / "final_chapter_architecture.json"
SOURCE_MAP = ROOT / "thesis" / "series_source_map.json"
ORDER = ROOT / "thesis" / "FINAL_CHAPTER_ORDER.md"
AUDIT = ROOT / "thesis" / "SERIES_DEPENDENCY_AUDIT_2026-09-06.md"

DRAFTS = {
    "chapter:eco-genetic": ROOT / "thesis" / "drafts" / "series" / "01_eco_genetic_state_validity_v0.1.md",
    "chapter:crest": ROOT / "thesis" / "drafts" / "series" / "02_crest_state_under_changing_futures_v0.1.md",
    "chapter:observation-design": ROOT / "thesis" / "drafts" / "series" / "03_learning_the_state_you_need_v0.1.md",
}


def _load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _chapter_map(series: dict) -> dict[str, dict]:
    return {row["id"]: row for row in series["chapters"]}


def main() -> int:
    series = _load(SERIES)
    legacy = _load(LEGACY)
    source_map = _load(SOURCE_MAP)
    order_text = ORDER.read_text(encoding="utf-8")
    audit_text = AUDIT.read_text(encoding="utf-8")

    assert series["schema_version"] == "theouni-series-architecture.v1"
    assert series["status"] == "preferred_five_chapter_three_series_architecture"
    assert series["legacy_component_architecture"] == "thesis/final_chapter_architecture.json"
    assert "not_preferred_chapter_order" in series["legacy_component_status"]

    chapters = series["chapters"]
    assert len(chapters) == 5
    assert [row["order"] for row in chapters] == list(range(5))
    expected_ids = [
        "chapter:introduction",
        "chapter:eco-genetic",
        "chapter:crest",
        "chapter:observation-design",
        "chapter:synthesis",
    ]
    assert [row["id"] for row in chapters] == expected_ids

    by_id = _chapter_map(series)
    research_ids = ["chapter:eco-genetic", "chapter:crest", "chapter:observation-design"]
    assert all(by_id[cid]["kind"] == "integrated_research_chapter" for cid in research_ids)

    # Legacy component architecture remains intact as the detailed provenance layer.
    legacy_chapters = legacy["chapters"]
    legacy_ids = [row["id"] for row in legacy_chapters]
    assert len(legacy_ids) == 10
    assert legacy_ids[0] == "chapter:introduction"
    assert legacy_ids[-1] == "chapter:synthesis"

    # The eight old research units must be partitioned exactly once across the
    # three integrated research chapters. This is the key no-loss/no-double-count rule.
    mapped: list[str] = []
    for cid in research_ids:
        mapped.extend(by_id[cid]["legacy_component_ids"])
    expected_legacy_research = {f"chapter:{i}" for i in range(1, 9)}
    assert set(mapped) == expected_legacy_research
    assert len(mapped) == len(set(mapped)) == 8

    # Source repository grouping is deliberate and exact.
    assert set(by_id["chapter:eco-genetic"]["primary_repositories"]) == {
        "zuizui0223/eco-genetic-criticality",
        "zuizui0223/eco-genetic-warning-extensions",
    }
    assert set(by_id["chapter:crest"]["primary_repositories"]) == {
        "zuizui0223/crest",
        "zuizui0223/ccoc",
        "zuizui0223/mltr",
        "zuizui0223/mrm",
        "zuizui0223/ced",
    }
    assert set(by_id["chapter:observation-design"]["primary_repositories"]) == {
        "zuizui0223/boundary",
        "zuizui0223/mrod",
    }

    # Cross-series order is conceptual, not a hidden theorem chain.
    assert series["cross_series_hard_dependencies"] == []
    handoffs = {(row["from"], row["to"]): row for row in series["cross_series_handoffs"]}
    assert ("chapter:eco-genetic", "chapter:crest") in handoffs
    assert ("chapter:crest", "chapter:observation-design") in handoffs
    assert "do not prove CREST" in handoffs[("chapter:eco-genetic", "chapter:crest")]["claim_ceiling"]
    assert "not yet a general target-conditioned CREST optimizer" in handoffs[("chapter:crest", "chapter:observation-design")]["claim_ceiling"]

    # Eco-genetic integration must preserve non-implication firewalls.
    eco = by_id["chapter:eco-genetic"]
    forbidden_eco = " ".join(eco["forbidden_dependency_claims"]).lower()
    assert "state separation theorem implies warning failure" in forbidden_eco
    assert "warning failure validates the common-scalar theorem" in forbidden_eco
    assert eco["hard_dependencies"] == []

    # CREST: CCOC/MLTR/MRM are parallel obstruction classes; CED is downstream.
    crest = by_id["chapter:crest"]
    dep = crest["dependency_graph"]
    assert dep["parallel_required_state_obstructions"] == ["CCOC", "MLTR", "MRM"]
    assert dep["downstream_licensing"] == "CED"
    assert "not a linear theorem chain" in dep["note"]
    assert any("CED licensing presupposes" in item for item in crest["hard_dependencies"])
    nondeps = " ".join(crest["non_dependencies"])
    assert "CCOC, MLTR and MRM do not prove one another" in nondeps

    # Observation-design integration is a handoff, not a proof import.
    obs = by_id["chapter:observation-design"]
    assert obs["hard_dependencies"] == []
    obs_nondeps = " ".join(obs["non_dependencies"])
    assert "MROD does not mathematically require the multiplicative Boundary model" in obs_nondeps
    assert "Boundary does not require MROD's synthetic benchmark" in obs_nondeps

    # Publication strategy must explicitly prefer consolidation.
    policy = series["submission_policy"]
    assert policy["preferred_count"] == 2
    assert len(policy["preferred_primary_papers"]) == 2
    assert policy["conditional_third_paper"]
    not_default = " ".join(policy["not_default"]).lower()
    assert "one paper per source repository" in not_default
    assert "separate ccoc, mltr, mrm and ced submissions" in not_default

    # Series source map must cover exactly the three research chapters and use
    # the same source repository sets as the architecture.
    assert source_map["schema_version"] == "theouni-series-source-map.v1"
    source_rows = {row["chapter"]: row for row in source_map["series"]}
    assert set(source_rows) == set(research_ids)
    for cid in research_ids:
        repo_set = {row["repository"] for row in source_rows[cid]["sources"]}
        assert repo_set == set(by_id[cid]["primary_repositories"])
        assert source_rows[cid]["forbidden_transfer"]

    # Integrated drafts must be substantial, standalone, and explicit about
    # dependency/ownership boundaries rather than simple concatenations.
    required_common = ["## Problem", "## Standalone contribution", "## Claim ceiling", "## Source ownership", "## Dissertation handoff"]
    for cid, path in DRAFTS.items():
        text = path.read_text(encoding="utf-8")
        assert len(text) >= 7000, (cid, len(text))
        for heading in required_common:
            assert heading in text, (cid, heading)

    eco_text = DRAFTS["chapter:eco-genetic"].read_text(encoding="utf-8")
    for token in ["0.2543", "+5.33", "35/35", "48/48", "specificity is `0`", "product-order chain"]:
        assert token in eco_text, token
    assert "does **not** establish" in eco_text

    crest_text = DRAFTS["chapter:crest"].read_text(encoding="utf-8")
    for token in ["2^m", "CCOC", "MLTR", "MRM", "CED", "parallel obstruction classes", "0.7401"]:
        assert token in crest_text, token
    assert "do not prove one another" in crest_text

    obs_text = DRAFTS["chapter:observation-design"].read_text(encoding="utf-8")
    for token in ["rowspan", "1.000", "0.6045", "83.5", "best precommitted", "does **not** mathematically require"]:
        assert token in obs_text, token

    # Human-facing order and dependency audit must expose the same decision.
    for token in [
        "preferred five-chapter architecture",
        "repo",  # keeps the ownership-vs-chapter distinction visible
        "CCOC`, `MLTR`, and `MRM` are **parallel",
        "Boundary + MROD",
        "fallback assets",
    ]:
        assert token in order_text, token

    for token in [
        "There are **no hard theorem dependencies among the three research chapters**",
        "horizontal publication independence with vertical dissertation coherence",
        "Default: two primary papers",
        "state separation theorem implies warning failure",
        "CED -> existence of ecological distinction",
    ]:
        assert token in audit_text, token

    print("Three-series dissertation architecture validation passed.")
    print("Legacy research components partitioned exactly once:", sorted(mapped))
    print("Preferred research chapters:", ", ".join(research_ids))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
