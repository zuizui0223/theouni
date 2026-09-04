from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "thesis" / "prior_art_risk_registry.json"
PROVED = ROOT / "thesis" / "proved_condition_registry.json"
CHAPTERS = ROOT / "thesis" / "chapter_registry.json"
DRAFT_STATUS = ROOT / "thesis" / "draft_status.json"
AUDIT = ROOT / "thesis" / "PROVED_CONDITION_PRIOR_ART_AUDIT_2026-09-04.md"
DEEP = ROOT / "thesis" / "PRIOR_ART_DEEP_AUDIT_TIER_A_2026-09-04.md"

EXPECTED_TIERS = {
    "chapter:introduction": "C",
    "chapter:1": "B",
    "chapter:2": "B",
    "chapter:3": "B",
    "chapter:4": "B",
    "chapter:5": "A",
    "chapter:6": "A",
    "chapter:7": "A",
    "chapter:8": "B",
    "chapter:synthesis": "C",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def scan_priority_language(paths: list[Path], blocked: list[str]) -> None:
    for path in paths:
        text = path.read_text(encoding="utf-8").casefold()
        for phrase in blocked:
            assert phrase.casefold() not in text, (
                f"priority language '{phrase}' is not cleared in {path.relative_to(ROOT)}"
            )


def main() -> None:
    registry = load(REGISTRY)
    proved = load(PROVED)
    chapters = load(CHAPTERS)
    draft_status = load(DRAFT_STATUS)
    audit = AUDIT.read_text(encoding="utf-8")
    deep = DEEP.read_text(encoding="utf-8")

    assert registry["schema_version"] == "theouni-prior-art-risk-registry.v1"
    assert registry["status"] == "priority_claims_blocked_pending_chapter_specific_audit"
    assert registry["audit_date"] == "2026-09-04"
    policy = registry["policy"]
    assert policy["priority_language_blocked_without_explicit_clearance"]
    assert "Correctness of a theorem" in policy["rule"]
    assert "failure to find" in policy["rule"].lower()

    units = registry["units"]
    proved_units = proved["units"]
    chapter_units = chapters["units"]
    expected_ids = [u["id"] for u in chapter_units]
    assert [u["chapter"] for u in units] == expected_ids
    assert [u["chapter"] for u in proved_units] == expected_ids
    assert len(units) == 10

    by_chapter = {u["chapter"]: u for u in units}
    assert len(by_chapter) == 10

    required_nonboolean = (
        "source",
        "risk_tier",
        "classical_substrate",
        "direct_prior_motifs",
        "defensible_contribution",
        "forbidden_priority_claims",
        "priority_status",
        "audit_sources",
        "remaining_gate",
    )
    for unit in units:
        chapter = unit["chapter"]
        for key in required_nonboolean:
            assert key in unit, f"{chapter} missing {key}"
            assert unit[key], f"{chapter} empty {key}"
        assert "firstness_allowed" in unit, f"{chapter} missing firstness_allowed"
        assert unit["risk_tier"] == EXPECTED_TIERS[chapter]
        assert unit["firstness_allowed"] is False
        assert len(unit["classical_substrate"]) >= 1
        assert len(unit["forbidden_priority_claims"]) >= 2
        assert unit["defensible_contribution"].strip()
        assert unit["remaining_gate"].strip()

    # Tier A cannot silently acquire a priority-clear status after a focused search.
    for chapter in ("chapter:5", "chapter:6", "chapter:7"):
        unit = by_chapter[chapter]
        assert unit["risk_tier"] == "A"
        assert "PRIOR_ART_DEEP_AUDIT_TIER_A_2026-09-04.md" in " ".join(unit["audit_sources"])
        assert "unresolved" in unit["priority_status"]
        assert len(unit["direct_prior_motifs"]) >= 3

    # Pin the most important downward novelty corrections semantically rather than
    # by one fragile wording choice.
    ch5 = by_chapter["chapter:5"]
    motifs5 = " ".join(ch5["direct_prior_motifs"]).lower()
    assert "transition" in motifs5 and "blow-up" in motifs5
    assert "outerplanar" in motifs5
    assert "krohn" in motifs5
    assert "package" in ch5["priority_status"]

    ch6 = by_chapter["chapter:6"]
    motifs6 = " ".join(ch6["direct_prior_motifs"]).lower()
    assert "conant" in motifs6
    assert "state minimization" in motifs6
    assert "neighbour_not_found" in ch6["priority_status"]

    ch7 = by_chapter["chapter:7"]
    motifs7 = " ".join(ch7["direct_prior_motifs"]).lower()
    assert "ravindran" in motifs7
    assert "givan" in motifs7
    assert "neighbour_not_found" in ch7["priority_status"]

    ch8 = by_chapter["chapter:8"]
    assert "formula_priority_unresolved" in ch8["priority_status"]
    assert "2-2^(1/k)" in ch8["defensible_contribution"]

    # Framing/synthesis never seek theorem priority.
    assert "no_firstness" in by_chapter["chapter:introduction"]["priority_status"]
    assert "no_firstness" in by_chapter["chapter:synthesis"]["priority_status"]

    # Every source-owned chapter condition remains merged before novelty positioning.
    proved_by_chapter = {u["chapter"]: u for u in proved_units}
    for chapter in [f"chapter:{i}" for i in range(1, 9)]:
        assert proved_by_chapter[chapter]["source_status"] == "merged"

    # Scan the current final prose surfaces. Narrow phrases avoid false positives such as
    # 'first observation' while blocking actual historical-priority language.
    prose_paths: list[Path] = []
    for chapter, status in draft_status["units"].items():
        assert status["stage"] == "draft_v0_1", f"{chapter} is not current prose"
        prose_paths.append(ROOT / status["draft_file"])
    prose_paths.extend(ROOT / unit["file"] for unit in chapter_units)
    assert all(path.exists() for path in prose_paths)
    scan_priority_language(
        prose_paths,
        policy["priority_language_blocked_without_explicit_clearance"],
    )

    # Human-readable audit must retain its own fail-closed warning.
    assert "novelty firewall, not a firstness certificate" in audit.lower()
    assert "Correctness of a theorem licenses the result" in audit
    assert "Tier A" in audit
    assert "package-only novelty posture" in deep
    assert "failure to find an exact match cannot establish historical firstness" in deep
    assert "Baburin & Cotterell" in deep
    assert "Dömösi & Nehaniv" in deep
    assert "Conant & Ashby" in deep
    assert "Ravindran & Barto" in deep

    print(
        "Validated prior-art firewall: 10 chapter units, all priority claims blocked; "
        "Tier-A CCOC/CREST/MLTR remain explicitly unresolved after focused nearest-neighbour audit, "
        "and current final prose contains no uncleared priority phrases."
    )


if __name__ == "__main__":
    main()
