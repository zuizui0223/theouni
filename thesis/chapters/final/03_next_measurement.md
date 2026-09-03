<!-- chapter-id: chapter:3 -->
# 境界の内側で、次に何を測るか

*English working title: What to Measure Next Inside the Boundary*

## Problem

測れるものは測る価値がある ⇒ 測る順序に良し悪しはない という推論を禁じるだけでなく、first outcome を見て next measurement を変えることが固定順序より本当に有利になる条件を問う。

## Headline result

For a fixed first observation, adaptive second-step mechanism-information value is `E[max_q U_q(X)]` and the strongest precommitted static value is `max_q E[U_q(X)]`. Adaptive value is never smaller, and it is strictly larger **if and only if** no remaining candidate is branchwise optimal on every positive-probability first-outcome branch. A minimal four-world witness gives `1.0` bit adaptively versus `0.5` bit for the best static second measurement.

## Why the result is nontrivial

「information-guided が random より良い」ではなく、最強のstatic comparatorに対する必要十分条件である。ranking が動くだけでは不十分で、全branchに共通するargmaxがなくなることが strict advantage の正確な条件になる。

## Ecological payoff

限られた調査予算の中で、いつ事前固定の採集計画で十分で、いつ最初の結果を見て次測定を変える価値があるかを区別できる。

## Claim ceiling

- 二段階有限設計の定理を任意のmulti-step greedy policyのglobal optimalityへ拡張しない。
- verified outcome partition がない候補を推測的priorで補わない。
- mechanism-learning information をtarget licensingや普遍的scientific utilityと同一視しない。

## Canonical source handoff

- `zuizui0223/mrod:docs/adaptive_recomputation_theorem_2026-09-03.md`
- `zuizui0223/mrod:tests/test_adaptive_recomputation_theorem.py`
- `zuizui0223/mrod:docs/mainline.md`
- `zuizui0223/mrod:paper/results/g2_frozen_v2_summary.json`
- `theory/TU2_LEARNING_LICENSING.md`

## Transition

次測定を適応的に選ぶ条件が分かっても、何を「状態」として学ぶべきかは別問題である。次章は、複数のeco-genetic responsibilityを一つのscalar stateに潰せる必要十分条件を問う。
