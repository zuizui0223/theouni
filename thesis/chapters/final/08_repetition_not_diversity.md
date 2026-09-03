<!-- chapter-id: chapter:8 -->
# 反復は、多様性の代わりにならない

*English working title: Repetition Does Not Substitute for Diversity*

## Problem

同じ手法を繰り返した ⇒ 証拠が強くなった という推論を、「独立failure modeの方が常に良い」という逆のスローガンにも置き換えず、有限の観測努力を同一mode内の反復と独立modeへの分散のどちらに使うべきかという条件問題として問う。

## Headline result

Under the declared one-sided detection contract, compare equal effort of exactly two reads per truly present coordinate: one shared mode with two within-mode repeats versus two independent modes with one read each. For `k` coordinates, equal mode availability `a` with `0<a<1`, per-read sensitivity `p>0`, independent mode failures and no false positives, diversity is better for joint detection of all `k` coordinates **if and only if**

`p > p*_k = 2 - 2^(1/k)`.

Deeper within-mode repetition is better below this threshold, and the two allocations tie at the threshold. Thus the design choice has an exact sensitivity-by-target-size boundary rather than a universal ordering.

## Why the result is nontrivial

shared failure means that many repeats can hit an availability ceiling, so raw replicate count is not equivalent to failure diversity. But at a small fixed budget, diversity can also spread low-sensitivity reads too thinly when every one of many coordinates must be detected. The theorem proves both directions. For `k=3`, the threshold is about `0.7401`: at `a=0.8,p=0.6` deeper repetition has the larger joint guarantee, whereas at `p=0.9` the two-mode diverse allocation is better. As `k` increases, `p*_k` approaches one, so the all-coordinate target makes low-sensitivity depth increasingly valuable at this two-read budget even though independent modes remain essential for escaping the long-run common-mode availability ceiling.

## Ecological payoff

調査設計を単に「replicateを増やす」または「methodを多様化する」という処方箋から、target dimensionality・per-read sensitivity・failure independenceを宣言したallocation problemへ変えられる。camera-weather domains、sampling dates、observer routesなどを追加する価値は、現在の感度と必要なjoint targetに依存して定量的に判定できる。

## Claim ceiling

- repetition 一般が無価値とは言わない。今回の定理では、閾値以下で実際にwithin-mode repetitionが優位になる。
- failure diversity 一般が常に優位とも言わない。
- `p*_k` はequal `a,p`、independent modes、conditionally independent reads、zero false positives、two reads per coordinate、all-`k` joint detectionというdeclared contractに対する境界である。
- heterogeneous costs、correlated failure、false positives、adaptive allocationには別解析が必要。
- exact compatible set と risk-limited singleton report を混同しない。

## Canonical source handoff

- `zuizui0223/ced@590f6459a7c3ef31e8a527319771fd3d736a704a:docs/repeat_vs_mode_allocation_theorem_2026-09-03.md`
- `zuizui0223/ced@590f6459a7c3ef31e8a527319771fd3d736a704a:tests/test_repeat_vs_mode_allocation_boundary.py`
- `zuizui0223/ced@590f6459a7c3ef31e8a527319771fd3d736a704a:docs/mode_diverse_detection_theorem.md`
- `zuizui0223/ced@590f6459a7c3ef31e8a527319771fd3d736a704a:docs/paper_b_theorem_consolidation.md`

## Transition

ここまでで、より多く測ることだけでなく、どのfailure architectureへ努力を配分するかにも条件付きの逆転境界がある。総合章では、こうした異なる条件を一つの“more is better”軸へ潰さず、各科学的責任ごとのadequacy conditionとして並べ直す。
