from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "thesis" / "typed_synthesis_matrix.json"
ARCH = ROOT / "thesis" / "final_chapter_architecture.json"
RECOVERY = ROOT / "thesis" / "verification_recovery_registry.json"
PROVED = ROOT / "thesis" / "proved_condition_registry.json"
NOTE = ROOT / "thesis" / "TYPED_SYNTHESIS_RECOVERY.md"

EXPECTED_CHAPTERS = [f"chapter:{i}" for i in range(1, 9)]
EXPECTED_SOURCES = [
    "boundary",
    "EGWE",
    "mrod",
    "eco-genetic-criticality",
    "CCOC",
    "CREST",
    "MLTR",
    "CED",
]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    matrix = load(MATRIX)
    architecture = load(ARCH)
    recovery = load(RECOVERY)
    proved = load(PROVED)
    note = NOTE.read_text(encoding="utf-8")

    assert matrix["schema_version"] == "theouni-typed-synthesis-matrix.v2"
    assert matrix["status"] == "proved_condition_backed_bounded_cross_chapter_synthesis"
    assert len(matrix["claim_ceiling"]) >= 5
    assert any("not a theorem" in item for item in matrix["claim_ceiling"])
    assert any("may not be pooled" in item for item in matrix["claim_ceiling"])
    assert any("proved_condition_registry" in item for item in matrix["claim_ceiling"])

    rows = matrix["rows"]
    assert len(rows) == 8
    assert [row["chapter"] for row in rows] == EXPECTED_CHAPTERS
    assert [row["source"] for row in rows] == EXPECTED_SOURCES
    assert len({row["axis_id"] for row in rows}) == 8
    assert len({row["richness_proxy"] for row in rows}) == 8
    assert len({row["responsibility_type"] for row in rows}) == 8

    proved_by_chapter = {u["chapter"]: u for u in proved["units"]}
    assert set(EXPECTED_CHAPTERS).issubset(proved_by_chapter)

    for row in rows:
        for key in (
            "responsibility_type",
            "richness_proxy",
            "forbidden_monotone_inference",
            "condition_class",
            "proved_condition",
            "proof_source",
            "verification_source",
            "decisive_application",
            "safe_conclusion",
        ):
            assert row[key].strip(), f"{row['chapter']} missing {key}"
        source_condition = proved_by_chapter[row["chapter"]]
        assert source_condition["source_status"] == "merged"
        assert row["condition_class"] == source_condition["condition_class"]
        assert row["proved_condition"] == source_condition["proved_condition"]

    # Sharp theorem-level details that must not regress to older slogans.
    by_chapter = {row["chapter"]: row for row in rows}
    assert "row span" in by_chapter["chapter:1"]["proved_condition"]
    assert "AUC=(1+specificity)/2" in by_chapter["chapter:2"]["proved_condition"]
    assert "intersection of branchwise argmax sets is empty" in by_chapter["chapter:3"]["proved_condition"]
    assert "chain under coordinatewise product order" in by_chapter["chapter:4"]["proved_condition"]
    assert "K_open-K_closed=m" in by_chapter["chapter:5"]["proved_condition"]
    assert "no finite upper bound" in by_chapter["chapter:6"]["proved_condition"]
    assert "necessary and sufficient" in by_chapter["chapter:7"]["proved_condition"]
    assert "2-2^(1/k)" in by_chapter["chapter:8"]["proved_condition"]

    chapter9 = architecture["chapters"][9]
    assert chapter9["id"] == "chapter:synthesis"
    assert "特権的な方向" in chapter9["title"]
    assert chapter9["primary_forbidden_inference"] == (
        "より詳細にする／より多く測る／より長く記憶する／より多く介入する ⇒ より妥当になる"
    )

    recovery9 = recovery["chapters"][9]
    assert recovery9["id"] == "chapter:synthesis"
    assert recovery9["verification_status"] == (
        "synthesis_supported_by_tu1_plus_cross_chapter_counterexamples"
    )
    assert "does not yet prove one global theorem" in recovery9["claim_ceiling"]

    rule = matrix["synthesis_rule"]
    assert "automatic certificate" in rule["permitted"]
    assert "condition" in rule["permitted"]
    assert "universal scalar law" in rule["forbidden"]
    assert "TU-1" in rule["exact_substrate"]
    assert "not special cases" in rule["exact_substrate"]

    assert "Eight typed proved conditions" in note
    assert "What Chapter 9 may not say" in note
    assert "one scalar information axis" in note
    assert "Exact substrate versus synthesis" in note
    assert "proved-condition registry" in note

    print(
        "Validated typed synthesis v2: all 8 source-owned rows match the merged proved-condition registry; "
        "Chapter 9 remains a bounded TU-1-backed synthesis rather than a global scalar theorem."
    )


if __name__ == "__main__":
    main()
