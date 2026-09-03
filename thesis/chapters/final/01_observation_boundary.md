<!-- chapter-id: chapter:1 -->
# 観測が原理的に届かない範囲

*English working title: Where Observation Cannot Reach in Principle*

## Problem

観測を豊かにした ⇒ 潜在機構に近づいた という推論を、単なる注意ではなく、どの追加観測なら本当に機構識別力を増やすかという条件問題として問う。

## Headline result

For exact compatible log-linear observations `M x = y`, the mechanism-compatible set has dimension `k-rank(M)`. A new scalar observation reduces structural ambiguity **if and only if** its observation row lies outside the current row span; when it helps, the residual dimension falls by exactly one. The familiar `k-1-r` product/channel-anchor result is a corollary of this rank criterion.

## Why the result is nontrivial

「観測を追加した」「より精密に測った」「より生物学的に近い量を測った」こと自体は条件ではない。重複、rescaling、既存観測の線形結合、同じoperatorの高精度化はstructural rankを増やさない。一方、現在のrow spanの外を測る一つの観測は、測定レベルにかかわらず未同定次元を一つ減らす。したがって識別改善の条件は観測量ではなく、現在の観測写像に対する独立性として証明される。

## Ecological payoff

高価な測定を増やす前に、候補測定が既存データにない識別方向を本当に追加するかを判定できる。pollinationのquantity/effectiveness/dependencyのようなjoint-measurement chainでは、「データが多いか」ではなく「競合機構を分けるmissing directionを測っているか」が設計条件になる。

## Claim ceiling

- この必要十分条件はdeclared positive multiplicative/log-linear observation classについてのstructural identification結果であり、自然界の真の機構への一般的距離を測るものではない。
- 測定精度の向上がsampling uncertaintyを減らすことは否定しない。row spanを変えない限りstructural identification dimensionを変えない、とだけ主張する。
- `k-1-r` は独立coordinate anchorsという特殊ケースであり、anchorの本数だけを一般的識別条件にしない。
- partial identification を完全同定と呼ばない。

## Canonical source handoff

- `zuizui0223/boundary@2919842f19bdd93221363b9f39f2ba1ebb146d17:docs/observation_rank_identification_theorem_2026-09-03.md`
- `zuizui0223/boundary@2919842f19bdd93221363b9f39f2ba1ebb146d17:tests/test_observation_rank_theorem.py`
- `zuizui0223/boundary@2919842f19bdd93221363b9f39f2ba1ebb146d17:paper/manuscript.md`

## Transition

機構識別が改善する条件を厳密に定めても、それは予測能力の条件ではない。次章では、機構を同定しなくても再現可能な先行信号が、損失を本当に識別するwarningになる条件を別に問う。
