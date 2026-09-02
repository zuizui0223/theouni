from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "thesis" / "typed_synthesis_matrix.json"
ARCH = ROOT / "thesis" / "final_chapter_architecture.json"
RECOVERY = ROOT / "thesis" / "verification_recovery_registry.json"
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
    note = NOTE.read_text(encoding="utf-8")

    assert matrix["schema_version"] == "theouni-typed-synthesis-matrix.v1"
    assert matrix["status"] == "bounded_cross_chapter_synthesis"
    assert len(matrix["claim_ceiling"]) >= 4
    assert any("not a theorem" in item for item in matrix["claim_ceiling"])
    assert any("may not be pooled" in item for item in matrix["claim_ceiling"])

    rows = matrix["rows"]
    assert len(rows) == 8
    assert [row["chapter"] for row in rows] == EXPECTED_CHAPTERS
    assert [row["source"] for row in rows] == EXPECTED_SOURCES
    assert len({row["axis_id"] for row in rows}) == 8
    assert len({row["richness_proxy"] for row in rows}) == 8

    for row in rows:
        assert row["richness_proxy"].strip()
        assert row["forbidden_monotone_inference"].strip()
        assert row["counterexample_type"].strip()
        assert row["decisive_result"].strip()
        assert row["safe_conclusion"].strip()

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
    assert "universal scalar law" in rule["forbidden"]
    assert "TU-1" in rule["exact_substrate"]

    assert "Eight typed failures of monotone shortcuts" in note
    assert "What Chapter 9 may not say" in note
    assert "one scalar information axis" in note
    assert "Exact substrate versus synthesis" in note

    print(
        "Validated typed synthesis: 8 source-owned monotone shortcuts are separated by type; "
        "Chapter 9 remains a bounded TU-1-backed synthesis, not a global scalar theorem."
    )


if __name__ == "__main__":
    main()
