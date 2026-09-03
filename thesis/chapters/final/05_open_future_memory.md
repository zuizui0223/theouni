<!-- chapter-id: chapter:5 -->
# 未来を開くと、記憶が要る

*English working title: Opening the Future Requires Memory*

## Problem

物理的境界が狭い ⇒ 必要な因果記憶も小さい という推論を禁じるだけでなく、local/static resourceを固定したまま future grammar の小さな変更が exact response memory をどこまで増やせるかを問う。

## Headline result

For every `m>=1`, CCOC gives a finite deterministic system with a fixed four-symbol action alphabet, one-state closed/open grammars differing by one legal `fire` transition, a bounded-degree tree, one-edge focal/exterior cut, bounded local alphabets and radius-one dynamics, yet the exact response quotient grows from `2` closed classes to `2^(m+1)` open classes. The exact interface gap is therefore `m` bits, attains the finite-domain upper bound, and proves that no finite bound based only on those static/local resources can control open-future interface inflation.

## Why the result is nontrivial

「可能な未来を増やせば記憶も増える」ではない。action alphabet・grammar size・cut width・degree・local stateを全部固定し、grammar editを一つに限定しても gap を任意の `m` にできる。さらに同じsourceは、common macro dynamicsとlabel-coherent embeddingsがあればportable lawが保たれる十分条件も与える。

## Ecological payoff

現在の空間的・network的な細い境界だけから将来の因果インターフェース容量を予算化せず、将来のlegal responseが旧summaryを通じてfactorizeするかを問える。

## Claim ceiling

- 実際の島・corridor・sparse networkが大きなhidden memoryを持つとは推論しない。
- generic finite-state minimization・bounded-local compilation・regular-language machineryの歴史的新規性を主張しない。
- future grammar expansion と CREST の capability expansion を同一視しない。

## Canonical source handoff

- `zuizui0223/ccoc:docs/fixed_regular_extremal_theorem_2026-08-13.md`
- `zuizui0223/ccoc:docs/theorem_spine.md`
- `zuizui0223/ccoc:docs/coherent_portable_macrolaw.md`
- `zuizui0223/ccoc:tests/test_extremal_open_composition.py`

## Transition

future legality の一遷移追加が unbounded response-memory gapを許すとしても、それは management capability の増加とは別操作である。次章は、一つの新actionでviable worldが一つだけ増えるときにも required state / monitoring burden を任意に大きくできるかを問う。
