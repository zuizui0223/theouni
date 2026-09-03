<!-- chapter-id: chapter:4 -->
# 一つの系に、状態は一つではない

*English working title: One System Does Not Have One State*

## Problem

生態遺伝的に要約した ⇒ 五つの側面を代表した という推論を、「変数が違うから違う」という説明で終わらせず、複数の生態遺伝的責任を一つの方向付きscalar stateで正確に保存できる条件として問う。

## Headline result

For a finite set of declared target vectors whose coordinates are oriented so that higher means no worse, an exact directionally coherent sufficient scalar state exists **if and only if** the distinct target vectors form a chain under coordinatewise product order. A single crossing pair is therefore an exact impossibility certificate for one common monotone state axis. The locked H3 fragmentation gradient contains such a crossing: from two to sixteen patches, retained interaction and local effective size decrease while realised high-trait mass increases.

## Why the result is nontrivial

「potential viabilityとrealised occupancyは別概念」「diversityとdemographyは別指標」という定義だけでは、一つの総合indexが作れないことは示せない。必要十分条件は逆に、target vectorsがすべて同じproduct-order chain上に並ぶなら一つのrank scalarを構成できることも証明する。したがって結論は“scalarは常に悪い”ではなく、**scalarが正確に成立する条件と、成立しないことを証明するcrossing condition**である。

locked H3ではこの条件違反が抽象例ではなく実際に回収される。2 patchesから16 patchesへ、interaction retainedは約0.001744→0.001244、local effective size retainedは約0.221311→0.033058と低下する一方、realised high-trait mass retainedは約0.282918→0.393880へ上昇する。この二方向性により、少なくともこれらのdeclared targetsを同時に保存するexact monotone scalarは存在しない。

## Ecological payoff

「系の状態」を一つのhealth indexへ押し込めるかどうかを、好みや可視化上の便宜ではなく検証可能な条件にできる。crossingがなければscalarizationの可能性が残り、crossingがあればその責任集合についてexact scalarizationを棄却できる。どのtargetを保存したいかを先に宣言する必要性も明確になる。

## Claim ceiling

- この定理はdeclared finite target setとdirection orientationに対するexact scalar representabilityを扱う。approximate index、target-specific index、任意のinjective numeric encodingを否定しない。
- locked H3 crossingはdeclared finite model closureの結果であり、自然界の全eco-genetic stateに一つのscalarが存在しないことを証明しない。
- complete simulator state を自然界の最小十分状態と呼ばない。
- five-state taxonomyがあらゆる系で必要十分とは主張しない。
- TU-3はrepresentation/loss-state firewallであり、locked H3 evidenceの所有者ではない。

## Canonical source handoff

- `zuizui0223/eco-genetic-criticality@2a35b2d2b11f4b8a00b8a4346bdba90773511a71:docs/common_scalar_state_theorem_2026-09-03.md`
- `zuizui0223/eco-genetic-criticality@2a35b2d2b11f4b8a00b8a4346bdba90773511a71:tests/test_common_scalar_state_theorem.py`
- `zuizui0223/eco-genetic-criticality@2a35b2d2b11f4b8a00b8a4346bdba90773511a71:docs/H3_FRAGMENTATION_GRADIENT_SENSITIVITY_RESULTS.md`
- `theory/TU3_LOSS_STATE_INVARIANCE.md`

## Transition

一つの共通state axisが成立する条件と、その破れ方を定めた後でも、そのstateを将来の別責任へ持ち越せるとは限らない。次章では、現在の物理的境界が小さいことから、未来を開いたとき必要な因果記憶まで小さいと推論できる条件があるのかを問う。
