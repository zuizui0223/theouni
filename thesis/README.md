# Thesis writing workspace

This directory now separates **scientific ownership** from **chapter/paper organization**.

- Source repositories own proofs, code, evidence, frozen numerical results, and reproducibility.
- `theouni` owns the cross-repository dependency audit, dissertation traversal, and synthesis.
- A repository is **not** automatically a chapter or a paper.

## Central thesis

> **When does a scientific representation that is adequate for one ecological responsibility cease to be reusable when the responsibility, future, structure, mechanism, evidence, or target changes?**

The preferred dissertation architecture is now five chapters, with three paper-scale research chapters.

## Preferred five-chapter order

| # | Chapter | Research scale |
|---:|---|---|
| 0 | **再利用問題 — The Reuse Problem** | General introduction / TU-1 framing |
| 1 | **生態遺伝状態は、何を予測するための状態か — Eco-genetic State Is Responsibility-Specific** | Integrated eco-genetic paper-scale chapter |
| 2 | **未来が変わると、必要な状態も変わる — CREST: State under Changing Futures** | Integrated flagship theory chapter |
| 3 | **必要な区別を、どう観測で回収するか — Learning the State You Need** | Integrated identification / observation-design methods chapter |
| 4 | **総合 — 妥当性に特権的な方向はない** | General synthesis / TU-1 return |

The machine-readable source of truth is [`series_architecture.json`](series_architecture.json). The detailed dependency audit is [`SERIES_DEPENDENCY_AUDIT_2026-09-06.md`](SERIES_DEPENDENCY_AUDIT_2026-09-06.md).

## What happened to the previous ten units?

Nothing is deleted.

`final_chapter_architecture.json`, `chapter_registry.json`, the existing `chapters/final/`, `drafts/final/`, `source_maps/final/`, proved-condition registries, prior-art audits, and recovery ledgers remain valid as **component-level provenance and writing material**.

The change is editorial:

> **old rule:** one source repository / forbidden inference tends to become one chapter;
>
> **new rule:** source repositories remain evidence modules, while chapters and papers are organized around one scientific question that can absorb several modules without transferring ownership.

The old ten-unit architecture is therefore a component map, not the preferred dissertation traversal.

## Research Chapter 1 — Eco-genetic state validity

### Question

Can one eco-genetic representation simultaneously stand in for potential viability, realised occupancy, transition dynamics, and predictive warning?

### Source modules

- `eco-genetic-criticality` — state separation, fragmentation response, common-scalar representability;
- `eco-genetic-warning-extensions` state-validity — exact next-transition counterexample plus locked horizon/replication propagation experiment;
- `eco-genetic-warning-extensions` warning-validity — full-denominator warning audit and precedence/discrimination theorem.

### Internal logic

These are **horizontal adequacy tests**, not a theorem chain.

```text
same scientific programme / source contracts
    |-- Can different biological targets share one scalar state?
    |-- Do coarse marginals preserve the next transition and downstream risk?
    `-- Does temporal precedence constitute predictive warning?
```

The warning result is not derived from the scalar-state theorem. The state-propagation result does not validate the warning statistic. The natural-data four-gate programme remains a companion measurement-validation paper and is not empirical validation of the finite closure.

### Publication role

Default: one integrated eco-genetic domain-theory paper **only if needed**. Existing EGC, warning-only, and state-validity manuscripts/bundles are retained as fallback assets rather than automatic separate submissions.

## Research Chapter 2 — CREST

### Question

When does a previously adequate ecological state cease to be adequate after the relevant future changes?

### Correct dependency architecture

```text
temporally extended ecological worlds + declared scientific contract
        |
        |-- CCOC: future/composition obstruction
        |-- MLTR: structural replacement/history obstruction
        |-- MRM : retained-mechanism response obstruction
        |
        v
required CREST state / quotient
        |
        v
CED: evidence licensing and honest report
```

This replaces the misleading dissertation sequence in which CCOC, CREST, MLTR, and CED appeared as successive theorem chapters.

- `CCOC`, `MLTR`, and `MRM` are parallel ways a present-state merge can become inadequate.
- CREST supplies the world/contract-relative state framework and the flagship capacity-versus-knowledge theorem.
- `CED` is downstream: evidence may or may not license a distinction already required by the task.

### Publication role

This is the preferred **flagship theory paper**. Detailed CCOC/MLTR/MRM/CED theorem families can remain source-owned and appear as supporting sections or Supplementary Information instead of becoming four default papers.

Working title:

> **When Conservation Capacity Outgrows Conservation Knowledge: A Contract-Relative Theory of Ecological State**

## Research Chapter 3 — Identification and observation design

### Question

Given a distinction that matters, can the current observation map identify it, and what should be measured next?

### Source modules

- `boundary` — structural identification boundary, rank criterion, and field-like same-observation/different-mechanism witness;
- `mrod` — admissible mechanism region, observation information value, sequential recomputation, and frozen truth-peek-free benchmark.

### Internal logic

```text
Can this observation change structural identifiability at all?
        -> Boundary
If ambiguity remains and several candidate observations are available,
which should be acquired next?
        -> MROD
```

This is a strong conceptual handoff, but there is no hard theorem dependency: MROD is not restricted to the multiplicative Boundary model.

### Publication role

Preferred integrated methods paper:

> **From Identifiability Limits to Mechanism-Resolving Observation Design**

The frozen MROD benchmark remains the principal method validation. The Boundary theorem and pollination-style witness become the structural-identification theory layer. Standalone Boundary and frozen MROD submission assets remain fallback versions until the integrated manuscript passes length and journal-format review.

## Vertical dissertation logic versus horizontal paper independence

There are **no hard theorem dependencies among the three research chapters**.

The dissertation connects them by questions:

```text
Eco-genetic
  demonstrates that adequacy changes with the job assigned to a representation
        ->
CREST
  generalizes why future/structure/mechanism/evidence changes split required states
        ->
Observation design
  asks how those required distinctions can be identified and measured efficiently
```

This gives the desired architecture:

- **horizontal:** each research chapter can stand alone as a paper;
- **vertical:** the dissertation has a coherent progression without pretending that one paper proves the next.

## Publication strategy

The default is now a **small-paper-count strategy**.

1. CREST flagship theory paper.
2. Boundary + MROD integrated methods paper.
3. Conditional eco-genetic integrated paper only if that material is too large or domain-specific to serve as a substantial worked layer around the flagship programme.

Do **not** default to one submission per source repository.

## Source-of-truth hierarchy

1. Source repository manuscripts, proofs, evidence ledgers, code, frozen artifacts, and source CI own scientific claims.
2. [`series_architecture.json`](series_architecture.json) owns the preferred five-chapter / three-series traversal and publication grouping.
3. [`SERIES_DEPENDENCY_AUDIT_2026-09-06.md`](SERIES_DEPENDENCY_AUDIT_2026-09-06.md) owns hard-dependency, shared-precondition, handoff, and forbidden-implication decisions.
4. `final_chapter_architecture.json`, `chapter_registry.json`, `proved_condition_registry.json`, and the existing final drafts remain the detailed component/provenance layer.
5. The Worldline Atlas remains non-linear and does not inherit the dissertation order.

## Writing rule for an integrated research chapter

Each integrated chapter must contain:

- **One scientific question**, not one repository per section;
- **Standalone contribution** — why the chapter is publishable without reading the preceding chapter;
- **Internal dependency map** — which components are parallel, which are preconditions, and which are hard dependencies;
- **Headline theorem/result** — one foreground result, with supporting theorem families demoted appropriately;
- **Numerical or constructive recovery** — preserve the source-owned nontriviality evidence;
- **Claim ceiling / forbidden implications** — especially where source modules share a system but do not prove one another;
- **Source ownership map** — every proof and dataset continues to point to its source repository;
- **Dissertation handoff** — why the next question follows conceptually without becoming a proof dependency.

## Legacy workspace validation

The existing ten-unit validators continue to protect the detailed component drafts while the integrated series drafts are built. A separate series validator checks the new preferred architecture. This staged migration prevents editorial regrouping from weakening source provenance or proved-condition contracts.
