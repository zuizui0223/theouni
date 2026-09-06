# Three-series dependency audit — 2026-09-06

## Decision

The ten source-owned research units should **not** be read as ten sequential theorem chapters. The preferred dissertation has three integrated research series. The key reason is dependency structure: most links among the source programmes are conceptual handoffs or shared model contracts, not proof dependencies.

This audit distinguishes four relations:

- **hard theorem dependency** — result B cannot be stated or proved without result A;
- **shared precondition** — two results use a common frozen model/data/semantic contract but neither proves the other;
- **conceptual handoff** — A motivates the scientific question asked by B, while B remains mathematically independent;
- **forbidden implication** — a tempting cross-result inference that is not licensed.

## 1. Eco-genetic series

### Included sources

- `eco-genetic-criticality`: state separation, fragmentation responses, common-scalar representability condition;
- `eco-genetic-warning-extensions`: state-validity transition contrast and propagation experiment;
- `eco-genetic-warning-extensions`: warning-validity full-denominator audit and precedence/discrimination theorem.

### Internal dependency table

| From | To | Relation | Verdict |
|---|---|---|---|
| finite eco-genetic source contract | EGC state separation | shared precondition | required model semantics, not a prior theorem |
| finite eco-genetic source contract | state-validity contrast | shared precondition | required state/transition semantics, not EGC theorem dependence |
| frozen event/non-event definitions | warning-validity | shared precondition | warning labels are imported from frozen source contracts |
| EGC common-scalar theorem | state-validity propagation | hard theorem dependency | **none** |
| state-validity propagation | warning-validity AUC result | hard theorem dependency | **none** |
| EGC state separation | warning-validity failure | implication | **forbidden** |
| warning-validity failure | EGC state separation | implication | **forbidden** |

### Why integration is still scientifically coherent

The common paper-level question is not that one result causes the next. It is:

> **What different scientific responsibilities can the same eco-genetic representation legitimately support?**

The three results interrogate different responsibilities:

1. cross-target scalar representation;
2. next-transition and downstream risk prediction;
3. predictive warning discrimination.

That makes them horizontal tests of adequacy inside one scientific programme, not a theorem chain.

### Nontrivial numerical recovery retained

- locked fragmentation crossing: interaction and effective size decrease while realised high-trait mass increases from the 2-patch to 16-patch comparison;
- exact transition witness: maximum generation-1 patchwise interaction difference `0.2543` under identical declared coarse marginals;
- propagation: at 1,500 pairs anti-aligned minus aligned loss-risk difference is approximately `0`, `+0.33`, `+5.33`, and `+5.20` percentage points at generations `5`, `10`, `20`, and `40`;
- warning: all frozen event trajectories lead but all frozen non-events also fire, giving specificity `0` and binary-marker AUC `0.5` in both ensembles.

### Publication implication

One integrated domain paper is defensible because the results share a scientific system and one higher-level question while retaining explicit non-implication firewalls. Separate source manuscripts remain useful fallback artifacts but should not be submitted automatically.

## 2. CREST series

### Included sources

- `crest`: world/contract-relative ecological state, finite state construction, capacity-versus-knowledge no-bound theorem;
- `ccoc`: future/composition obstruction and open-future memory gap;
- `mltr`: inherited macro-law portability, least repair, route coherence, minimum history completion;
- `mrm`: retained-mechanism response ambiguity, minimal candidate-safe state, active discrimination;
- `ced`: evidence licensing, target-safe reporting, failure-domain and calibration bounds.

### Correct dependency graph

```text
temporally extended ecological worlds + declared scientific contract
        |
        |-- CCOC: future/composition makes a hidden distinction addressable
        |-- MLTR: inherited structure/history makes an old label incoherent
        |-- MRM : retained mechanisms disagree on a required future response
        |
        v
required state distinction / CREST quotient
        |
        v
CED: does available evidence identify/license that required distinction?
```

### Internal dependency table

| Relation | Status |
|---|---|
| CCOC -> MLTR | no hard theorem dependency |
| MLTR -> MRM | no hard theorem dependency |
| MRM -> CCOC | no hard theorem dependency |
| CCOC/MLTR/MRM -> CREST no-bound theorem | no hard theorem dependency; they are independent obstruction modules/worked realizations |
| declared required distinction -> CED | **hard semantic dependency**: evidence licensing requires something already declared as scientifically relevant |
| CED -> existence of ecological distinction | **forbidden**: evidence does not create the underlying required distinction |
| microdonta/Boundary ecological channel example -> CREST theorem | conceptual worked bridge only, not proof |

### Consequence for manuscript architecture

The current CREST repository already states the correct hierarchy: CCOC, MLTR, and MRM are parallel structural reasons for snapshot insufficiency; CED is downstream evidence licensing. Therefore the old dissertation order `CCOC -> CREST -> MLTR -> CED` imposed false sequentiality.

The integrated flagship should use one headline theorem rather than five competing headlines:

> **A small increase in management capability can force an arbitrarily large increase in the state/monitoring resolution required for scientifically licensed action.**

The other modules answer *why a previously legitimate merge can split*:

- wider future grammar;
- replacement/history semantics;
- retained mechanism response;
- insufficient evidence for the resulting distinction.

Detailed theorem families can remain source-owned and move to Supplementary Information without losing provenance.

## 3. Identification and observation-design series

### Included sources

- `boundary`: structural identification boundary and observation-rank criterion;
- `mrod`: admissible mechanism region and information-guided sequential observation design.

### Internal dependency table

| From | To | Relation | Verdict |
|---|---|---|---|
| Boundary | MROD | hard theorem dependency | **none** |
| Boundary | MROD | conceptual handoff | strong: first ask whether a measurement changes the exact observation map / rank; then compare informative candidates inside remaining ambiguity |
| MROD | Boundary | proof dependency | none |
| product-factorization assumptions | MROD general method | implication | **forbidden**: MROD is not restricted to multiplicative ecological chains |

### Why integration improves the paper

Boundary by itself is a Perspective about when more measurement does not change structural identification. MROD by itself is a methods paper about what to measure next after mechanism ambiguity remains. In one paper they form a clean design sequence:

```text
Can this measurement possibly resolve the ambiguity?
        -> structural identification gate
If several resolving measurements remain, which is most informative now?
        -> MROD sequential design
```

The primary validation remains the frozen MROD truth-peek-free benchmark; the Boundary pollination-style witness functions as an interpretable structural-identification example rather than a second validation dataset.

## 4. Cross-series dependency audit

There are **no hard theorem dependencies among the three research chapters**.

### Eco-genetic -> CREST

Relation: worked-problem-to-general-theory.

The eco-genetic results demonstrate several ways that a single representation fails across tasks. CREST generalizes the notion of responsibility-relative state. The eco-genetic results do not prove CREST, and CREST is not needed to calculate the frozen eco-genetic results.

### CREST -> Observation design

Relation: required-distinction-to-learning-design.

CREST clarifies that the appropriate inferential target can be task-specific. Current MROD, however, resolves a declared mechanism vector and is not yet a theorem for arbitrary CREST target-conditioned monitoring. Therefore the dissertation may hand off from CREST to observation design conceptually without claiming that MROD is already the universal CREST learning algorithm.

### Observation design -> synthesis

Relation: epistemic completion of the reuse problem.

The final synthesis asks whether a new responsibility can be recovered from what an earlier representation retained. Boundary/MROD supply examples of when observation maps do or do not recover the required distinction, but TU-1 remains the formal revision-after-compression theorem.

## 5. Submission strategy implied by the dependency audit

### Default: two primary papers

1. **CREST flagship theory paper** — CREST + CCOC + MLTR + MRM + CED.
2. **Integrated methods paper** — Boundary + MROD.

### Conditional third paper

3. **Eco-genetic state-validity paper** — EGC + transition/propagation state-validity + warning-validity, only if this material is too domain-specific or too large to function as a substantial worked layer around the flagship theory.

### Retain but do not automatically submit

- standalone Warning-validity submission bundle;
- standalone state-validity lane;
- EGC manuscript;
- Boundary Perspective;
- separate CCOC, MLTR, MRM, CED manuscripts.

These remain source-owned provenance, reviewer, and contingency assets. Their existence does not create an obligation to fragment the publication programme.

## 6. Dissertation payoff

The three-series order is vertical only at the level of scientific questioning:

```text
1. Eco-genetic: the same system needs different representations for different jobs.
2. CREST: why and when do scientific jobs force different state partitions?
3. Observation design: how can the required distinctions be identified and measured efficiently?
```

Because the cross-series theorem dependency set is empty, each research chapter can also stand alone as a paper. This is the desired combination: **horizontal publication independence with vertical dissertation coherence**.
