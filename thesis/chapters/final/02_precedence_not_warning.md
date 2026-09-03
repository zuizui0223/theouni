<!-- chapter-id: chapter:2 -->
# 先行することは、警告することではない

*English working title: Precedence Is Not Warning*

## Problem

損失に先行した ⇒ 損失を予告する という推論を、禁止するだけでなく、perfect precedence が何を同定し何を同定しないかを問う。

## Headline result

For a binary marker at a common horizon, perfect event-conditioned precedence forces sensitivity `1` but leaves specificity free. Consequently `AUC=(1+specificity)/2`, so the same perfect lead result is compatible with binary AUC from `0.5` to `1`. The locked EGWE ensembles attain the sharp chance-discrimination endpoint: `35/35` leads with `48/48` non-event firings and `33/33` with `49/49`, giving specificity `0` and AUC `0.5`.

## Why the result is nontrivial

これは「false positive も見よう」という助言ではない。イベント系列を固定したまま非イベント発火数だけを変えることで、specificity の全有限gridと chance-to-perfect AUC が構成できる。EGWE はその下端を独立2 ensembleで実現する。

## Ecological payoff

early signal を warning と呼ぶ前に、event-conditioned timing が保持する情報と、full-denominator discrimination に必要な情報を厳密に分けられる。

## Claim ceiling

- binary common-horizon marker の定理を任意のcontinuous time-dependent scoreへ拡張しない。
- genetic diversity 一般に予測情報がないとは言わない。
- frozen loss/event definitions をこの章が新たに生成したとは扱わない。

## Canonical source handoff

- `zuizui0223/eco-genetic-warning-extensions:docs/PRECEDENCE_DISCRIMINATION_THEOREM_2026-09-03.md`
- `zuizui0223/eco-genetic-warning-extensions:tests/test_precedence_discrimination_theorem.py`
- `zuizui0223/eco-genetic-warning-extensions:manuscript/warning_validity.md`
- `theory/TU4_WARNING_STATE_PORTABILITY.md`

## Transition

先行性の情報限界が分かったとしても、次に何を測るべきかは決まらない。次章は、観測結果に応じて次測定を変えることが fixed ordering より厳密に有利になる条件を問う。
