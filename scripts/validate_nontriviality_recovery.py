from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "thesis" / "nontriviality_recovery_registry.json"
PROVED = ROOT / "thesis" / "proved_condition_registry.json"
AUDIT = ROOT / "thesis" / "NONTRIVIALITY_RECOVERY_AUDIT_2026-09-04.md"

HARD_MODES = {
    "contradiction_or_impossibility",
    "sharpness",
    "minimality",
    "locked_source_numeric",
    "exhaustive_or_independent_oracle",
}

LOCKED_NUMERIC = {"chapter:2", "chapter:3", "chapter:4"}
EXACT_NUMERIC = {
    "chapter:introduction",
    "chapter:1",
    "chapter:5",
    "chapter:6",
    "chapter:7",
    "chapter:8",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    registry = load(REGISTRY)
    proved = load(PROVED)
    audit = AUDIT.read_text(encoding="utf-8")

    assert registry["schema_version"] == "theouni-nontriviality-recovery.v1"
    assert registry["status"] == "definition_only_recovery_disallowed_for_research_chapters"
    assert registry["audit_date"] == "2026-09-04"
    assert len(registry["principle"]) >= 4

    units = registry["units"]
    proved_units = proved["units"]
    expected = [u["chapter"] for u in proved_units]
    assert [u["chapter"] for u in units] == expected
    assert len(units) == 10

    by_chapter = {u["chapter"]: u for u in units}
    assert len(by_chapter) == 10

    for unit in units:
        for key in (
            "chapter",
            "source",
            "role",
            "triviality_risk",
            "definition_only",
            "numeric_class",
            "numeric_anchor",
            "recovery_modes",
            "contradiction_anchor",
            "sharp_or_minimal_anchor",
            "verification",
            "remaining_gap",
        ):
            assert key in unit, f"{unit.get('chapter')} missing {key}"
        assert unit["definition_only"] is False
        assert unit["triviality_risk"].strip()
        assert unit["numeric_anchor"].strip()
        assert unit["verification"].strip()
        assert unit["remaining_gap"].strip()

    # Every source-owned research chapter must have more than one independent
    # recovery mode and at least one hard non-definitional recovery mode.
    for i in range(1, 9):
        chapter = f"chapter:{i}"
        unit = by_chapter[chapter]
        modes = set(unit["recovery_modes"])
        assert unit["role"] == "source_owned_research"
        assert len(modes) >= 2, f"{chapter} has too few recovery modes"
        assert modes & HARD_MODES, f"{chapter} lacks a hard non-definitional recovery mode"
        assert unit["contradiction_anchor"].strip()
        assert unit["sharp_or_minimal_anchor"].strip()

    # Numerical evidence is typed rather than pooled.
    for chapter in LOCKED_NUMERIC:
        assert "locked_source_numeric" in by_chapter[chapter]["numeric_class"]
    for chapter in EXACT_NUMERIC:
        assert "exact_finite_numeric_witness" in by_chapter[chapter]["numeric_class"]
    assert by_chapter["chapter:synthesis"]["numeric_class"] == "no_independent_numeric_claim"

    # Pin decisive numerical anchors so they cannot disappear during prose edits.
    assert "35/35" in by_chapter["chapter:2"]["numeric_anchor"]
    assert "48/48" in by_chapter["chapter:2"]["numeric_anchor"]
    assert "33/33" in by_chapter["chapter:2"]["numeric_anchor"]
    assert "49/49" in by_chapter["chapter:2"]["numeric_anchor"]
    assert "1.0 bit" in by_chapter["chapter:3"]["numeric_anchor"]
    assert "0.5 bit" in by_chapter["chapter:3"]["numeric_anchor"]
    assert "1.000" in by_chapter["chapter:3"]["numeric_anchor"]
    assert "0.6045" in by_chapter["chapter:3"]["numeric_anchor"]
    assert "0.001744" in by_chapter["chapter:4"]["numeric_anchor"]
    assert "0.393880" in by_chapter["chapter:4"]["numeric_anchor"]
    assert "1037/1037" in by_chapter["chapter:4"]["numeric_anchor"]
    assert "0.74008" in by_chapter["chapter:8"]["numeric_anchor"]
    assert "0.47416" in by_chapter["chapter:8"]["numeric_anchor"]
    assert "0.85427" in by_chapter["chapter:8"]["numeric_anchor"]

    # Pin the main contradiction/no-bound recoveries.
    assert "null" in by_chapter["chapter:1"]["contradiction_anchor"].lower()
    assert "all non-events" in by_chapter["chapter:2"]["contradiction_anchor"].lower()
    assert "nonnegative" in by_chapter["chapter:3"]["contradiction_anchor"].lower()
    assert "crossing" in by_chapter["chapter:4"]["contradiction_anchor"].lower()
    assert "choose" in by_chapter["chapter:5"]["contradiction_anchor"].lower()
    assert "f(1)" in by_chapter["chapter:6"]["contradiction_anchor"]
    assert "incompatible" in by_chapter["chapter:7"]["contradiction_anchor"].lower()
    assert "opposite sides" in by_chapter["chapter:8"]["contradiction_anchor"].lower()

    # Framing/synthesis stay bounded instead of faking empirical support.
    assert by_chapter["chapter:introduction"]["role"] == "framing_with_exact_substrate"
    assert by_chapter["chapter:synthesis"]["role"] == "bounded_synthesis"
    assert "No pooled number" in by_chapter["chapter:synthesis"]["numeric_anchor"]

    # Human-readable audit must expose the remaining weak points, not just successes.
    for phrase in (
        "Chapter 1 application layer",
        "Chapter 3 stronger implementation comparators",
        "do not chase fake empirical numerics",
        "The programme has moved materially beyond definition-level claims",
    ):
        assert phrase in audit

    print(
        "Validated nontriviality recovery: Chapters 1-8 are not definition-only; "
        "Ch2-4 retain locked numerical recoveries, Ch1/5-8 retain exact finite witnesses, "
        "and every research chapter has a hard contradiction/sharpness/minimality/oracle layer."
    )


if __name__ == "__main__":
    main()
