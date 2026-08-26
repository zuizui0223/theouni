from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> None:
    reserve = load("theory/revision_reserve.json")
    assert reserve["schema_version"] == "theouni-revision-reserve.v0.1"
    guarantees = reserve["guarantees"]
    assert guarantees["freeze_identity"] is True
    assert guarantees["source_provenance"] is True
    assert guarantees["known_source_reopenability"] is True
    assert guarantees["arbitrary_future_contract_revisability"] is False
    for item in reserve["reserve_sources"]:
        path = item["path"]
        if path == ".git":
            continue
        assert (ROOT / path).exists(), path
    assert reserve["explicit_non_claims"]

    bridge = load("theory/bridges/rach_mrm_ced_bridge.json")
    assert bridge["schema_version"] == "theouni-positive-bridge.v0.1"
    assert bridge["status"] == "finite_exact_implemented"
    assert set(bridge["source_snapshots"]) == {"microdonta", "mrm", "ced"}
    assert len(bridge["positive_claims"]) >= 3
    assert len(bridge["firewalls_preserved"]) >= 3
    assert (ROOT / bridge["verification"]).exists()
    assert (ROOT / bridge["documentation"]).exists()
    assert "no canonical natural-world embedding" in bridge["claim_ceiling"].lower()

    print(
        "Revision reserve and positive bridge validated: freeze identity remains distinct from "
        "future revisability, and RACH->MRM->CED has an implemented finite positive composition."
    )


if __name__ == "__main__":
    main()
