<!-- chapter-id: chapter:7 -->
# 法則は構造置換を越えない

*English working title: Laws Do Not Automatically Survive Structural Replacement*

## Problem

ある構造で成り立った法則 ⇒ 置換後の構造でも成り立つ法則 という推論を、なぜこの章では許してはいけないのかを問う。

## Headline result

MLTR gives an exact source-relative transport chain. An inherited law is portable **iff** output, legal-action rows, and successor carried labels are constant within every carried target fiber. Failure has a finite within-fiber witness; iterative refinement gives the unique coarsest exact source-relative repair. Across replacement routes, one route-independent inherited semantics exists **iff** the complete carried terminal maps agree; otherwise one immutable history mode per distinct carried map is necessary and sufficient.

## Why the result is nontrivial

「構造が変われば法則も変わりうる」という一般論ではない。変更後もそのまま再利用できる条件、失敗時の最小修復、history を追加せずに済む条件と必要最小mode数まで証明している。異なるcarried mapsが同じunlabeled repair形状へ収束しうる場合も明示的に分離する。

## Ecological payoff

turnover・rewiring・species replacement・management change後の法則再利用を、単なるfitや名称の連続性ではなく、継承した意味・許される作用・後継状態が保存されるかで監査できる。壊れた場合も全面的に作り直すのではなく、source provenanceを保つ最小の追加区別を特定できる。

## Claim ceiling

- source–target replacement relation を自然データから自動推定したとは言わない。
- positive transport defect から target-only の小さな別表現が存在しないとは言わない。
- route incoherence から unlabeled repaired partition が必ず異なるとは主張しない。
- generic partition refinement / lumpability / bisimulation / path dependence の新規性を主張しない。

## Canonical source handoff

- `zuizui0223/mltr:docs/master_theorem_proof.md`
- `zuizui0223/mltr:manuscript/paper_a_main.tex`
- `zuizui0223/mltr:docs/publication_completion_spine.md`
- `zuizui0223/mltr:tests/test_section5_proof_obligations.py`

## Transition

構造を越えたlaw reuseはexact conditionで監査できる。では、同じ観測手法を何度も再利用することは、それだけで独立な証拠を増やすのか？ Chapter 8は意味のtransportではなくfailure-domainの独立性を問う。
