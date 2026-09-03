from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = ROOT / "thesis" / "chapter_registry.json"
RECOVERY = ROOT / "thesis" / "verification_recovery_registry.json"
LEDGER = ROOT / "thesis" / "VERIFICATION_RECOVERY_LEDGER.md"

REPO_MAP = {
    "repo:theouni": "zuizui0223/theouni",
    "repo:boundary": "zuizui0223/boundary",
    "repo:eco-genetic-warning-extensions": "zuizui0223/eco-genetic-warning-extensions",
    "repo:mrod": "zuizui0223/mrod",
    "repo:eco-genetic-criticality": "zuizui0223/eco-genetic-criticality",
    "repo:ccoc": "zuizui0223/ccoc",
    "repo:crest": "zuizui0223/crest",
    "repo:mltr": "zuizui0223/mltr",
    "repo:ced": "zuizui0223/ced",
}

REFRESHED = {
    "chapter:1": "2919842f19bdd93221363b9f39f2ba1ebb146d17",
    "chapter:2": "ef545bfa871c1a2b01daca1fc86e6db67f6e8c95",
    "chapter:3": "689ba17d14fec2218e9e96f4c9e432eb8b71fb58",
    "chapter:4": "2a35b2d2b11f4b8a00b8a4346bdba90773511a71",
    "chapter:8": "590f6459a7c3ef31e8a527319771fd3d736a704a",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    chapters = load(CHAPTERS)
    recovery = load(RECOVERY)
    ledger = LEDGER.read_text(encoding="utf-8")

    assert recovery["schema_version"] == "theouni-thesis-verification-recovery.v1"
    assert recovery["status"] == "source_snapshot_recovered"
    assert recovery["recovered_on"] == "2026-09-02"

    units = chapters["units"]
    records = recovery["chapters"]
    assert len(units) == len(records) == 10
    assert [unit["id"] for unit in units] == [record["id"] for record in records]
    assert [unit["order"] for unit in units] == [record["order"] for record in records]

    by_id = {record["id"]: record for record in records}
    for unit in units:
        record = by_id[unit["id"]]
        assert record["title"] == unit["title"]
        assert record["forbidden_inference"] == unit["forbidden_inference"]
        expected_repo = REPO_MAP[unit["primary_source_repositories"][0]]
        assert record["source_repository"] == expected_repo
        assert len(record["source_snapshot_sha"]) == 40
        int(record["source_snapshot_sha"], 16)
        assert record["evidence_paths"]
        assert all(path.strip() for path in record["evidence_paths"])
        assert record["claim_ceiling"].strip()

    research = records[1:9]
    assert len(research) == 8
    assert all(record["verification_status"].startswith("verified_") for record in research)
    assert all(record["remaining_recovery"] == [] for record in research)

    for chapter, sha in REFRESHED.items():
        assert by_id[chapter]["source_snapshot_sha"] == sha

    # Newly sharpened chapters must point to theorem-level proof and executable obligations.
    assert "docs/observation_rank_identification_theorem_2026-09-03.md" in by_id["chapter:1"]["evidence_paths"]
    assert "docs/PRECEDENCE_DISCRIMINATION_THEOREM_2026-09-03.md" in by_id["chapter:2"]["evidence_paths"]
    assert "docs/adaptive_recomputation_theorem_2026-09-03.md" in by_id["chapter:3"]["evidence_paths"]
    assert "docs/common_scalar_state_theorem_2026-09-03.md" in by_id["chapter:4"]["evidence_paths"]
    assert "docs/repeat_vs_mode_allocation_theorem_2026-09-03.md" in by_id["chapter:8"]["evidence_paths"]

    intro = records[0]
    synthesis = records[9]
    assert intro["verification_status"] == "synthesis_framing_verified_not_independent_theorem"
    assert synthesis["verification_status"] == "synthesis_supported_by_tu1_plus_cross_chapter_counterexamples"
    assert intro["remaining_recovery"]
    assert synthesis["remaining_recovery"]

    summary = recovery["summary"]
    assert summary["research_chapters"] == 8
    assert summary["directly_verified"] == 8
    assert summary["unresolved_research_core"] == 0
    assert summary["synthesis_units"] == 2
    assert "merged theorem/condition" in summary["critical_finding"]

    # Claim ceilings stay fail-closed after sharpening.
    assert "all five state variables are pairwise distinct" in by_id["chapter:4"]["claim_ceiling"]
    assert "finite synthetic" in by_id["chapter:5"]["claim_ceiling"]
    assert "does not say that repetition is never useful" in by_id["chapter:8"]["claim_ceiling"]
    assert "does not yet prove one global theorem" in synthesis["claim_ceiling"]

    assert "All eight source-owned research chapters" in ledger
    assert "Chapter 0 is not a theorem that reuse always fails" in ledger
    assert "Chapter 9 is not yet a single global non-monotonicity theorem" in ledger
    assert "forbidden inference → source-owned result" in ledger

    print(
        "Verified chapter recovery: 8/8 research chapters have direct source evidence and refreshed theorem-level snapshots where strengthened; "
        "Chapter 0 remains framing and Chapter 9 remains TU-1-backed typed synthesis rather than a global theorem."
    )


if __name__ == "__main__":
    main()
