#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOVERNANCE = ROOT / "universe" / "PORTFOLIO_GOVERNANCE_2026-09-11.json"
TRACK_PROGRAMME = ROOT / "universe" / "PUBLICATION_PROGRAMME_2026-09-11.json"

EXPECTED_REPOSITORIES = {
    "284b", "acsp", "adaptive-gain", "aza3", "azami", "balance", "bita",
    "boundary", "ccoc", "ced", "chun", "crest", "EAzami", "egc", "egwe",
    "egwee", "eog", "fcp", "hotarubukuro", "insepi", "island", "izu-core",
    "mltr", "mrm", "mrod", "odsp", "payoff", "pollipi", "rec", "sch",
    "sdmr", "shimahotarubukuro", "slk", "theouni", "tnoa", "TTF", "v3",
    "zuizui0223.github.io",
}

EXPECTED_PAPER_STATE_COUNTS = {
    "ACTIVE_SUBMISSION": 2,
    "SUBMISSION_READY": 19,
    "ACTIVE_MANUSCRIPT": 7,
    "PAPER_ASSET": 2,
    "CONDITIONAL": 1,
    "FUTURE": 3,
}

TRACK_ID_MAP = {
    "C2": "C2_TREE",
    "C1": "BOUNDARY_C1",
    "M1": "TNOA_M1",
    "M2": "MROD_M2",
    "M3": "CED_M3",
    "M4": "V3_REC_M4",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    governance = load(GOVERNANCE)
    programme = load(TRACK_PROGRAMME)

    assert governance["status"] == "canonical_portfolio_governance"
    assert governance["scope"]["owner"] == "zuizui0223"
    assert governance["scope"]["repository_count"] == 38
    assert set(governance["scope"]["repository_inventory"]) == EXPECTED_REPOSITORIES
    assert set(governance["repositories"]) == EXPECTED_REPOSITORIES

    paper_units = governance["paper_units"]
    paper_ids = [row["id"] for row in paper_units]
    assert len(paper_ids) == 34
    assert len(set(paper_ids)) == len(paper_ids)
    assert Counter(row["paper_state"] for row in paper_units) == EXPECTED_PAPER_STATE_COUNTS
    assert set(governance["paper_states"]) == set(EXPECTED_PAPER_STATE_COUNTS)

    flattened_tracks = [pid for rows in governance["tracks"].values() for pid in rows]
    assert len(flattened_tracks) == len(paper_ids)
    assert len(set(flattened_tracks)) == len(flattened_tracks)
    assert set(flattened_tracks) == set(paper_ids)

    by_id = {row["id"]: row for row in paper_units}
    for row in paper_units:
        assert row["paper_state"] in governance["paper_states"]
        assert row["track"] in governance["tracks"] or row["track"] in {
            "standalone_theory", "standalone_methods", "flower_colour_methods",
            "observation_system_validation",
        }
        for repo in row.get("homes", []) + row.get("sources", []):
            assert repo in EXPECTED_REPOSITORIES, (row["id"], repo)

    # Repository-to-paper and paper-to-home consistency.
    for repo, meta in governance["repositories"].items():
        assert meta["roles"]
        for pid in meta["paper_units"]:
            assert pid in by_id
            assert repo in by_id[pid]["homes"]
    for row in paper_units:
        for repo in row["homes"]:
            assert row["id"] in governance["repositories"][repo]["paper_units"]

    # Regression guards for the governance errors that motivated this layer.
    assert governance["repositories"]["fcp"]["paper_units"] == [
        "FCP_SPATIAL", "FCP_COMPARATIVE"
    ]
    assert by_id["V3_REC_M4"]["homes"] == ["v3", "rec"]
    assert governance["repositories"]["balance"]["paper_units"] == []
    assert "module_only" in governance["repositories"]["balance"]["roles"]
    assert governance["repositories"]["egc"]["paper_units"] == []
    assert "source_only" in governance["repositories"]["egc"]["roles"]
    assert governance["repositories"]["pollipi"]["paper_units"] == []
    assert "infrastructure" in governance["repositories"]["pollipi"]["roles"]
    assert governance["repositories"]["azami"]["paper_units"] == ["AZAMI_CH1"]
    assert by_id["P284B_P1"]["paper_state"] == "ACTIVE_SUBMISSION"
    assert by_id["P284B_P1"]["homes"] == ["284b"]

    # The former 5+1 global-looking router is now explicitly track-local.
    contract = governance["local_router_contract"]
    assert contract["track"] == "observation_evidence"
    assert contract["confirmed"] == 5
    assert contract["conditional"] == 1
    assert "not the whole-owner" in contract["forbidden"]

    assert programme["status"] == "canonical_track_publication_programme"
    assert programme["scope"]["track_id"] == "observation_evidence"
    assert programme["scope"]["whole_owner_portfolio"] is False
    assert programme["scope"]["parent_governance"] == "universe/PORTFOLIO_GOVERNANCE_2026-09-11.json"
    assert programme["portfolio"]["scope"] == "observation_evidence_track_only"
    assert programme["portfolio"]["whole_owner_count_claim"] is False

    local_ids = {
        **{row["id"]: TRACK_ID_MAP[row["id"]] for row in programme["concept_track"]},
        **{row["id"]: TRACK_ID_MAP[row["id"]] for row in programme["method_track"]},
    }
    assert set(local_ids.values()) == set(contract["paper_units"])
    assert set(local_ids.values()) == set(governance["tracks"]["observation_evidence"])

    print("PORTFOLIO_GOVERNANCE PASS")


if __name__ == "__main__":
    main()
