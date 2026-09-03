from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "thesis" / "proved_condition_registry.json"
CHAPTERS = ROOT / "thesis" / "chapter_registry.json"
LEDGER = ROOT / "thesis" / "PROVED_CONDITION_LEDGER.md"

PENDING = {"chapter:2": 140, "chapter:3": 101}
MERGED_RESEARCH = {"chapter:1", "chapter:4", "chapter:5", "chapter:6", "chapter:7", "chapter:8"}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    registry = load(REGISTRY)
    chapters = load(CHAPTERS)
    ledger = LEDGER.read_text(encoding="utf-8")

    assert registry["schema_version"] == "theouni-proved-condition-registry.v1"
    assert registry["status"] == "proof_conditions_recovered_with_fail_closed_source_status"
    assert "definition" in registry["principle"].lower() or "defines" in registry["principle"].lower()
    assert "theorem" in registry["principle"].lower()

    units = registry["units"]
    chapter_ids = [u["id"] for u in chapters["units"]]
    assert [u["chapter"] for u in units] == chapter_ids
    assert len(units) == 10
    by_chapter = {u["chapter"]: u for u in units}
    assert len(by_chapter) == 10

    for unit in units:
        for key in ("source", "condition_class", "question", "proved_condition", "proof_source", "verification_source", "source_status", "claim_ceiling"):
            assert str(unit[key]).strip(), f"{unit['chapter']} missing {key}"
        assert unit["question"].endswith("?")
        assert unit["source_status"] in {"merged", "pending_ci_merge"}
        assert "definition_only" not in unit["condition_class"]

    assert by_chapter["chapter:introduction"]["condition_class"] == "iff"
    assert "framing" in by_chapter["chapter:introduction"]["claim_ceiling"]
    assert by_chapter["chapter:synthesis"]["condition_class"] == "typed_synthesis_not_global_iff"
    assert "global" in by_chapter["chapter:synthesis"]["proved_condition"]

    for chapter, pr in PENDING.items():
        unit = by_chapter[chapter]
        assert unit["source_status"] == "pending_ci_merge"
        assert unit["source_pr"] == pr
        assert "source_snapshot_sha" not in unit

    for chapter in MERGED_RESEARCH:
        assert by_chapter[chapter]["source_status"] == "merged"

    assert by_chapter["chapter:1"]["source_snapshot_sha"] == "2919842f19bdd93221363b9f39f2ba1ebb146d17"
    assert by_chapter["chapter:1"]["proof_source"] == "docs/observation_rank_identification_theorem_2026-09-03.md"
    assert by_chapter["chapter:1"]["verification_source"] == "tests/test_observation_rank_theorem.py"
    assert "if and only if" in by_chapter["chapter:1"]["proved_condition"]
    assert "k-1-r" in by_chapter["chapter:1"]["special_case"]

    assert by_chapter["chapter:4"]["source_snapshot_sha"] == "2a35b2d2b11f4b8a00b8a4346bdba90773511a71"
    assert by_chapter["chapter:4"]["proof_source"] == "docs/common_scalar_state_theorem_2026-09-03.md"
    assert by_chapter["chapter:4"]["verification_source"] == "tests/test_common_scalar_state_theorem.py"

    assert by_chapter["chapter:8"]["source_snapshot_sha"] == "590f6459a7c3ef31e8a527319771fd3d736a704a"
    assert by_chapter["chapter:8"]["proof_source"] == "docs/repeat_vs_mode_allocation_theorem_2026-09-03.md"
    assert by_chapter["chapter:8"]["verification_source"] == "tests/test_repeat_vs_mode_allocation_boundary.py"

    assert "AUC=(1+specificity)/2" in by_chapter["chapter:2"]["proved_condition"]
    assert "if and only if" in by_chapter["chapter:3"]["proved_condition"]
    assert "if and only if" in by_chapter["chapter:4"]["proved_condition"]
    assert "no finite upper bound" in by_chapter["chapter:6"]["proved_condition"]
    assert "necessary and sufficient" in by_chapter["chapter:7"]["proved_condition"]
    assert "2-2^(1/k)" in by_chapter["chapter:8"]["proved_condition"]

    assert "35/35" in by_chapter["chapter:2"]["locked_evidence"] and "49/49" in by_chapter["chapter:2"]["locked_evidence"]
    assert "2-patch" in by_chapter["chapter:4"]["locked_evidence"] and "16-patch" in by_chapter["chapter:4"]["locked_evidence"]

    assert "A formula without this chain is not counted" in ledger
    assert "Fail-closed import rule" in ledger
    assert "`pending_ci_merge`" in ledger

    print(
        "Validated proved-condition registry: 10 chapter units; 6 research condition sources merged, "
        "2 fail-closed pending source PRs, and Chapters 0/9 kept as framing/synthesis boundaries."
    )


if __name__ == "__main__":
    main()
