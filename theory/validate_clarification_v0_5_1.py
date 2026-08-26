from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLAR = ROOT / "theory" / "clarification_v0.5.1.json"
CURRENT = ROOT / "theory" / "CURRENT.json"
FREEZE = ROOT / "theory" / "FREEZE_v0.5.json"


def main() -> None:
    clar = json.loads(CLAR.read_text(encoding="utf-8"))
    current = json.loads(CURRENT.read_text(encoding="utf-8"))
    freeze = json.loads(FREEZE.read_text(encoding="utf-8"))

    assert clar["schema_version"] == "theouni-theory-clarification.v0.5.1"
    assert clar["base_freeze"] == "theouni-theory-core.v0.5"
    assert current["current_version"] == "v0.5.1"
    assert current["base_frozen_core"]["version"] == "v0.5"
    assert freeze["schema_version"] == "theouni-theory-freeze.v0.5"
    assert freeze["status"] == "semantic_core_frozen"

    types = {item["id"]: item for item in clar["types"]}
    required = {
        "clarified:EvidenceRequirement",
        "clarified:RealizedEvidenceClass",
        "clarified:FullLossContractResponseSignature",
    }
    assert required <= set(types)
    assert types["clarified:EvidenceRequirement"]["canonical_symbol"] == "D_req"
    assert types["clarified:RealizedEvidenceClass"]["canonical_symbol"] == "E_y^{D_req}"
    assert types["clarified:FullLossContractResponseSignature"]["canonical_symbol"] == "Sigma_{C_L}"

    distinctions = {
        (item["left"], item["right"]): item["rule"]
        for item in clar["hard_distinctions"]
    }
    assert (
        "clarified:EvidenceRequirement",
        "clarified:RealizedEvidenceClass",
    ) in distinctions
    assert (
        "clarified:FullLossContractResponseSignature",
        "single_loss_summary",
    ) in distinctions

    equations = clar["equations"]
    assert "E_y^{D_req}" in equations["realized_evidence"]
    assert "Sigma_{C_L}" in equations["loss_equivalence"]
    assert "Q_L=Omega/ker(Sigma_{C_L})" == equations["loss_quotient"]
    assert "Sigma_W=(Sigma_{C_L},Sigma_G)" == equations["warning_joint_signature"]

    effect = clar["theorem_effect"]
    assert effect["dependency_graph_changed"] is False
    assert effect["TU1_semantics_changed"] is False
    assert effect["TU2_semantics_changed"] is False
    assert effect["TU3_result_changed"] is False
    assert effect["TU3_signature_interpretation_narrowed"] is True
    assert effect["TU4_result_changed"] is False
    assert effect["TU4_signature_interpretation_narrowed"] is True
    assert effect["claim_ceiling_expanded"] is False

    assert current["theorem_dependency_graph_changed"] is False
    assert current["claim_ceiling_expanded"] is False

    anti = "\n".join(clar["anti_upgrade_rules"]).lower()
    assert "do not treat realized evidence" in anti
    assert "one convenient loss statistic" in anti
    assert "warningevaluationstate" in anti

    print(
        "Theory Universe v0.5.1 clarification validated: "
        "D_req is separated from E_y, full loss-contract signature is enforced, "
        "and v0.5 theorem/dependency claims remain unchanged."
    )


if __name__ == "__main__":
    main()
