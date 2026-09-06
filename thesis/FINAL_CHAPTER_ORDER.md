# Preferred dissertation chapter order — three research series

Status: **preferred five-chapter architecture**.

The dissertation is no longer organized as one source repository per chapter. **Repositories own proofs, code, evidence, and frozen provenance; chapters are organized by scientific question.** The previous ten-unit forbidden-inference order remains in `thesis/final_chapter_architecture.json` as a component/provenance map and is not deleted.

| # | 章題 | Research series | Main source repositories |
|---:|---|---|---|
| **0** | **再利用問題** | Introduction / TU-1 | `theouni` |
| **1** | **生態遺伝状態は、何を予測するための状態か** | Eco-genetic state validity | `eco-genetic-criticality`, `eco-genetic-warning-extensions` |
| **2** | **未来が変わると、必要な状態も変わる** | CREST | `crest`, `ccoc`, `mltr`, `mrm`, `ced` |
| **3** | **必要な区別を、どう観測で回収するか** | Identification and observation design | `boundary`, `mrod` |
| **4** | **総合 — 妥当性に特権的な方向はない** | Typed synthesis / TU-1 | `theouni` |

The machine-readable source of truth for this preferred architecture is `thesis/series_architecture.json`.

## Why the old ten-chapter order was too fine

The previous order made source repositories look like sequential theorem dependencies even when the actual science was parallel.

- `CCOC`, `MLTR`, and `MRM` are **parallel reasons a present-state merge can fail**: a newly addressable future, inherited structural/history semantics, or retained mechanism disagreement.
- `CED` is not a fourth ontic obstruction at the same level. It is **downstream evidence licensing**: once a distinction is scientifically required, does the observation contract identify it well enough to report?
- `Boundary` and `MROD` form a genuine design handoff, but not a hard proof dependency: Boundary asks whether the observation map can reduce structural ambiguity at all; MROD asks which verified measurement is most informative inside a declared ambiguity set.
- The eco-genetic source papers share one model/programme context, but state separation, transition sufficiency, and warning discrimination are separate adequacy tests rather than theorem implications.

The preferred chapter structure therefore preserves proof ownership while removing false sequentiality.

## Chapter 1 — Eco-genetic state validity

Central question:

> **Can one eco-genetic representation stand in for potential viability, realised occupancy, transition dynamics, and predictive warning?**

The chapter combines three source-owned results:

1. **state separation:** one common monotone sufficient scalar exists iff the distinct target vectors form a product-order chain; the locked fragmentation crossing violates that condition;
2. **transition sufficiency:** identical declared coarse marginals can produce different exact next transitions, and the locked propagation experiment shows little loss-risk contrast at generations 5–10 but about five percentage points by generations 20–40 under the declared forcing path;
3. **warning validity:** perfect event-conditioned precedence fixes sensitivity but not specificity; the frozen full-denominator audit reaches specificity `0` and binary-marker AUC `0.5`.

These results are deliberately **not** written as `state separation -> warning failure`. They share a scientific system and ask different responsibilities of a representation.

The natural-data four-gate programme remains an empirical measurement-validation companion, not empirical validation of the finite eco-genetic closure.

## Chapter 2 — CREST

Central question:

> **When does a previously adequate ecological state cease to be adequate after the relevant future changes?**

Canonical structure:

```text
temporally extended ecological worlds + scientific contract
        |
        +-- CCOC: newly addressable future/composition
        +-- MLTR: inherited structure/history semantics
        +-- MRM: retained mechanism response disagreement
        |
        v
required CREST state / quotient
        |
        v
CED: evidence licensing and honest report
```

`CCOC`, `MLTR`, and `MRM` are parallel obstruction modules, not Chapters 5–7 in a theorem chain. The flagship CREST theorem remains the capacity-versus-knowledge no-bound construction. Detailed CCOC/MLTR/MRM/CED proofs can sit in sections or Supplementary Information without forcing separate default submissions.

## Chapter 3 — Identification and observation design

Central question:

> **Given a distinction that matters, can the current observation map identify it, and what should be measured next?**

The chapter begins with Boundary's rank criterion and field-like same-observation/different-mechanism witness, then moves to MROD's admissible mechanism region and sequential observation-information design.

This is a conceptual handoff, not a theorem dependency: MROD is not restricted to multiplicative Boundary models, and Boundary does not require MROD's synthetic benchmark.

## Publication strategy

The default is no longer `one repository = one paper`.

Preferred strategy:

1. **CREST flagship theory paper** — integrate CREST + CCOC + MLTR + MRM + CED around one state-adequacy question.
2. **Integrated methods paper** — Boundary + MROD, with the identification theorem as the theory layer and the frozen MROD benchmark as the primary validation.
3. **Conditional eco-genetic paper** — integrate EGC + state-validity + warning-validity only if the material is too large or too domain-specific to serve as a worked layer around the flagship theory.

Existing standalone manuscripts and frozen bundles are retained as **fallback assets**, not automatic obligations to submit many small papers.

## Vertical dissertation logic

The three research chapters remain readable independently, because there are **no cross-series hard theorem dependencies**.

The dissertation-level handoff is instead:

```text
Eco-genetic series
  shows that adequacy changes with the scientific responsibility
        ->
CREST
  generalizes why required state changes under future/structure/mechanism/evidence changes
        ->
Observation design
  asks how the needed distinction can be identified and efficiently measured
```

The final synthesis then returns to TU-1: when a later responsibility needs a different quotient, can the revised state be recovered from what the earlier representation retained?
