# Typed synthesis recovery — Chapter 9

## Purpose

Chapter 9 uses the phrase **“妥当性に特権的な方向はない”**. This is a bounded synthesis, not a single global theorem that information richness is always good, always bad, or universally non-monotone.

The synthesis is now backed directly by `thesis/proved_condition_registry.json`. Every Chapter 1–8 row must reproduce the merged source-owned proved condition exactly. The matrix is therefore not allowed to drift back into weaker slogans after the source theorem has become sharper.

## Eight typed proved conditions

| Chapter | Scientific responsibility | Proved condition replacing the shortcut |
|---:|---|---|
| 1 | structural mechanism identification | compatible-set dimension is `k-rank(M)`; a new scalar observation reduces ambiguity **iff** its row lies outside the existing row span |
| 2 | predictive warning discrimination | perfect binary event precedence forces sensitivity 1 but leaves specificity free; `AUC=(1+specificity)/2`, and the same perfect precedence can range from chance to perfect discrimination |
| 3 | sequential mechanism-learning design | adaptive second-step value exceeds the best precommitted static candidate **iff** no candidate is branchwise optimal on every positive-probability first-outcome branch |
| 4 | multi-target eco-genetic state | one exact directionally coherent scalar exists **iff** the finite target vectors form a chain under coordinatewise product order |
| 5 | open-future response memory | a bounded-local, one-edge-cut family attains `K_open-K_closed=m` for arbitrary `m`; separate coherence conditions give a positive portability boundary |
| 6 | capability versus required knowledge | one new action and +1 robust-carrier world can force `1→2^m` required states and exactly `m` monitoring bits; hence carrier gain alone gives no finite burden bound |
| 7 | source-relative law transport | carried law exactness has an iff within-fiber condition; repair is unique coarsest; one history mode per distinct carried map is necessary and sufficient across routes |
| 8 | failure-aware evidence allocation | with two reads per coordinate, independent-mode diversity beats within-mode depth **iff** `p>2-2^(1/k)`; fixed mode count separately imposes an availability ceiling |

These rows answer different questions. They do not share one carrier, one adequacy function, one resource unit, or one ordering relation.

## Why this is stronger than eight “not necessarily” statements

The dissertation may introduce each chapter through a tempting forbidden inference, but Chapter 9 should synthesize the **replacement conditions**, not the negations.

The scientific pattern is:

```text
shortcut
  -> exact question
  -> necessary/sufficient, sharp, or no-bound condition
  -> executable / locked witness
  -> bounded permitted inference
```

Examples:

- Chapter 1 does not merely say “more observations may fail.” It says exactly when another observation changes structural identification: when it adds rank.
- Chapter 3 does not merely say “adaptive design can help.” It gives the exact common-argmax condition separating equality from strict adaptive advantage.
- Chapter 4 does not merely say “states can differ.” It gives an iff condition for one common directional scalar and a locked crossing that violates it.
- Chapter 8 does not merely say “replicates are dependent.” It proves a finite-effort ordering reversal and a separate asymptotic ceiling.

The synthesis is therefore condition-based even though it is not a single theorem.

## What Chapter 9 may say

> Across the distinct scientific responsibilities studied here, none of the recorded richness proxies is an automatic certificate of adequacy. Each responsibility instead has a condition specifying when reuse, refinement, measurement, transport, or reporting is licensed.

This claim is supported by eight source-owned proved conditions plus TU-1. It remains weaker than a universal monotonicity theorem because the rows are typed differently.

A second permitted claim is methodological:

> Scientific adequacy should be stated as a relation between a representation/evidence object and a declared responsibility, not inferred from an untyped notion of “more information.”

This is a synthesis of the programme architecture, not a claim that one universal adequacy metric has been mathematically derived.

## What Chapter 9 may not say

Do not claim:

- that “more information” universally reduces adequacy;
- that more information universally improves adequacy either;
- that all eight rows live on one scalar information axis;
- that observation rank, AUC, mutual information, product-order scalarizability, memory bits, carrier gain, history modes, and detection guarantee are interchangeable quantities;
- that the source programmes jointly prove one global partial order over ecological representations;
- that every future scientific responsibility must exhibit one of these eight failure forms;
- that the eight source theorems are special cases of TU-1;
- that TU-1 proves the empirical or source-specific conclusions of Chapters 1–8.

The phrase “no privileged direction” is therefore a statement about **automatic certification**, not a theorem that every direction of enrichment is bad.

## Exact substrate versus synthesis

The exact theorem owned by `theouni` remains TU-1. Let an old scientific contract store partition `P` and a revised contract require partition `Q` on the same finite carrier.

State-only revision is possible exactly when

`q_Q = f ∘ q_P`

for some deterministic recoding `f`, equivalently when every old-state block lies inside one revised-state block.

When state-only revision fails, TU-1 also gives the exact minimum auxiliary alphabet:

`K_rev(P→Q) = max_B r_B(P,Q)`,

where `r_B` is the number of revised-state blocks intersecting old block `B`. The corresponding fixed-length side memory is `ceil(log2 K_rev)` bits.

TU-1 therefore supplies an exact answer to the dissertation's opening reuse question:

> a representation may be reused after responsibility changes only when the revised response factors through what was retained, or when sufficient auxiliary information repairs the distinctions that were forgotten.

This theorem is the synthesis substrate, but not the proof of every later chapter.

```text
TU-1
  = exact same-carrier revision / forgetting theorem

proved-condition registry, Chapters 1–8
  = eight source-owned conditions under different scientific types

Chapter 9
  = typed synthesis: adequacy has no untyped privileged richness direction
```

## Relation between Chapter 0 and Chapter 9

Chapter 0 asks whether a successful representation can be reused for a later responsibility. TU-1 answers that question exactly for same-carrier revision.

Chapters 1–8 then show eight scientifically different ways in which seemingly stronger or reusable objects require their own adequacy conditions:

- another measurement must add an independent identification direction;
- an early marker must discriminate non-events;
- an adaptive measurement must face branch-specific optima to gain strictly over static choice;
- one state scalar requires order-compatible targets;
- narrow locality does not bound open-future memory without coherence;
- small capability gain does not bound resolution debt;
- a source law must preserve target operational semantics and route coherence;
- repeated effort must be allocated relative to sensitivity, target dimension, and failure modes.

Chapter 9 closes the loop: the correct object to reuse is not “the richer one” but the one whose retained distinctions are sufficient for the responsibility now being asked.

## The proved-condition registry is authoritative

`thesis/proved_condition_registry.json` is the theorem-level source of truth. `thesis/typed_synthesis_matrix.json` must match its `condition_class` and `proved_condition` fields for Chapters 1–8 exactly.

This gives Chapter 9 a fail-closed rule:

> If a source programme sharpens or changes its theorem, the synthesis cannot retain an older paraphrase and still pass validation.

The typed synthesis matrix adds only the cross-chapter fields: responsibility type, richness proxy, forbidden shortcut, decisive application, and safe conclusion.

## Writing rule

When comparing rows, name the type of richness and the type of adequacy every time. Avoid bare sentences such as “more information is not better.” Prefer:

- more **endpoint precision** does not improve **structural mechanism identification** unless the observation operator gains rank;
- more **event-conditioned temporal consistency** does not determine **warning discrimination** because specificity remains unconstrained;
- more **available candidate measurements** do not create strict **adaptive design value** unless branchwise optimal choices conflict;
- more **state detail** cannot be compressed into one directional scalar when target vectors cross;
- a smaller **physical cut** does not bound **open-future response memory**;
- a smaller **carrier gain** does not bound **required state/monitoring resolution**;
- stronger **source-law confidence** does not determine **replacement portability** without target coherence;
- more **replicate effort** does not determine **failure-aware guarantee strength** without knowing how effort is distributed across modes.

The machine-readable source of truth for this chapter is the proved-condition registry plus the v2 typed synthesis matrix.
