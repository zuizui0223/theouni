from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

from bridges.verify_rach_mrm_ced_bridge import (
    verify_causal_singleton_not_required,
    verify_response_class_is_enough,
    verify_target_can_be_coarser_than_response,
    verify_uninformative_evidence_requires_ambiguity,
)
from build_triadic_screen import (
    DOCUMENT,
    MATRIX,
    SCREEN,
    build_screen,
    render_document,
    render_json,
)
from verify_contract_indexed_quotient_transport import (
    WorldBits,
    factors_through,
    partition,
    task_leq,
)

ROOT = Path(__file__).resolve().parents[1]


def verify_complete_screen(matrix: dict, screen: dict) -> None:
    expected = build_screen(matrix)
    assert screen == expected
    assert SCREEN.read_text(encoding="utf-8") == render_json(expected)
    assert DOCUMENT.read_text(encoding="utf-8") == render_document(expected)

    modules = [item["id"] for item in matrix["modules"]]
    expected_triples = [list(triple) for triple in combinations(modules, 3)]
    actual_triples = [item["modules"] for item in screen["triads"]]
    assert actual_triples == expected_triples
    assert len(actual_triples) == 220

    method = screen["method"]
    assert method["pairwise_relation_truth_revalidated"] is False
    assert method["emergent_three_way_conflict_excluded"] is False
    assert screen["counts"]["screen_classes"]["contains-declared-pair-conflict"] == 0
    assert sum(screen["counts"]["screen_classes"].values()) == 220
    assert screen["counts"]["executable_assessments"] == {
        "not-executably-assessed": 218,
        "verified-in-bounded-witness": 2,
    }


def verify_rach_mrm_ced_witness() -> None:
    verify_response_class_is_enough()
    verify_uninformative_evidence_requires_ambiguity()
    verify_causal_singleton_not_required()
    verify_target_can_be_coarser_than_response()


def verify_tu1_tu3_tu4_witness() -> None:
    worlds = [WorldBits(a, b) for a in (0, 1) for b in (0, 1)]
    old_state_and_loss = lambda world: world.a
    revised_task_and_warning = lambda world: (world.a, world.b)
    loss_faithful_representation = lambda world: (world.a, world.b)

    # TU-1: the canonical weaker state cannot be reused in the reverse direction.
    assert not factors_through(worlds, revised_task_and_warning, old_state_and_loss)

    # TU-3: the declared representation retains the full loss response.
    assert factors_through(worlds, old_state_and_loss, loss_faithful_representation)

    # TU-4: the warning task strictly refines the loss task on this carrier.
    assert task_leq(worlds, old_state_and_loss, revised_task_and_warning)
    assert not task_leq(worlds, revised_task_and_warning, old_state_and_loss)
    assert partition(worlds, revised_task_and_warning) == partition(
        worlds, loss_faithful_representation
    )


def main() -> None:
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    screen = json.loads(SCREEN.read_text(encoding="utf-8"))
    verify_complete_screen(matrix, screen)
    verify_rach_mrm_ced_witness()
    verify_tu1_tu3_tu4_witness()
    print(
        "Draft v0.6 triadic screen validated: all 220 unordered triples are present; "
        "2 bounded shared-carrier witnesses pass and 218 triples remain without an "
        "executable higher-order assessment."
    )


if __name__ == "__main__":
    main()
