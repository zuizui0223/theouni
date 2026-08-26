from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Hashable, Iterable

World = Hashable
Label = Hashable


def partition(worlds: Iterable[World], fn: Callable[[World], Label]) -> frozenset[frozenset[World]]:
    blocks: dict[Label, set[World]] = {}
    for w in worlds:
        blocks.setdefault(fn(w), set()).add(w)
    return frozenset(frozenset(block) for block in blocks.values())


def refines(fine: frozenset[frozenset[World]], coarse: frozenset[frozenset[World]]) -> bool:
    """Return whether every fine block lies inside one coarse block."""
    return all(any(block <= target for target in coarse) for block in fine)


def factors_through(
    worlds: Iterable[World],
    target: Callable[[World], Label],
    representation: Callable[[World], Label],
) -> bool:
    """Set-theoretic exact factorization criterion: target = f o representation."""
    seen: dict[Label, Label] = {}
    for w in worlds:
        r = representation(w)
        t = target(w)
        if r in seen and seen[r] != t:
            return False
        seen[r] = t
    return True


@dataclass(frozen=True)
class WorldBits:
    a: int
    b: int
    nuisance: int = 0


def verify_general_factorization() -> None:
    worlds = [WorldBits(a, b) for a in (0, 1) for b in (0, 1)]

    sigma_a = lambda w: w.a
    sigma_b = lambda w: w.b
    sigma_joint = lambda w: (w.a, w.b)
    rep_joint = sigma_joint
    rep_a = sigma_a

    assert factors_through(worlds, sigma_a, rep_joint)
    assert not factors_through(worlds, sigma_b, rep_a)

    q_a = partition(worlds, sigma_a)
    q_joint = partition(worlds, sigma_joint)
    assert refines(q_joint, q_a)
    assert not refines(q_a, q_joint)


def verify_tu1_specialization() -> None:
    worlds = [WorldBits(a, b) for a in (0, 1) for b in (0, 1)]
    old_state = lambda w: w.a
    revised_task = lambda w: (w.a, w.b)
    weaker_future_task = lambda w: w.a

    assert not factors_through(worlds, revised_task, old_state)
    assert factors_through(worlds, weaker_future_task, old_state)


def verify_tu3_specialization() -> None:
    worlds = [WorldBits(a, b, n) for a in (0, 1) for b in (0, 1) for n in range(4)]

    # Nuisance can be forgotten for a loss task depending only on a.
    loss_signature = lambda w: w.a
    representation = lambda w: (w.a, w.b)
    assert factors_through(worlds, loss_signature, representation)

    # A hidden target-relevant coordinate breaks faithfulness.
    richer_loss_signature = lambda w: (w.a, w.nuisance % 2)
    assert not factors_through(worlds, richer_loss_signature, representation)


def verify_tu4_specialization() -> None:
    worlds = [WorldBits(a, b) for a in (0, 1) for b in (0, 1)]
    loss = lambda w: w.a
    warning = lambda w: w.b
    warning_joint = lambda w: (w.a, w.b)

    assert factors_through(worlds, loss, warning_joint)
    assert not factors_through(worlds, warning_joint, loss)

    q_loss = partition(worlds, loss)
    q_warn = partition(worlds, warning_joint)
    assert refines(q_warn, q_loss)


def verify_tu2_exact_endpoints() -> None:
    worlds = [WorldBits(a, b) for a in (0, 1) for b in (0, 1)]
    causal_task = lambda w: w.a
    report_task = lambda w: w.b

    observe_causal = lambda w: w.a
    observe_target = lambda w: w.b

    assert factors_through(worlds, causal_task, observe_causal)
    assert not factors_through(worlds, report_task, observe_causal)

    assert factors_through(worlds, report_task, observe_target)
    assert not factors_through(worlds, causal_task, observe_target)


def main() -> None:
    verify_general_factorization()
    verify_tu1_specialization()
    verify_tu3_specialization()
    verify_tu4_specialization()
    verify_tu2_exact_endpoints()
    print(
        "Contract-indexed quotient transport draft verified: general factorization, "
        "TU-1/TU-3/TU-4 exact specializations, and TU-2 exact endpoint analogue."
    )


if __name__ == "__main__":
    main()
