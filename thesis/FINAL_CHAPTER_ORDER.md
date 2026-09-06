# Preferred dissertation architecture — three parallel research pillars

Status: **Graphify-corrected preferred architecture**.

The dissertation is not one repository per chapter and is not one `state` spine. **Repositories own proofs, code, evidence, and provenance; the three research chapters are parallel paper-scale series.** Their displayed order is editorial only.

| # | Chapter | Research pillar | Main source repositories |
|---:|---|---|---|
| **0** | **再利用問題** | Introduction / TU-1 | `theouni` |
| **1** | **生態遺伝機構から損失と警告へ** | Eco-genetic | `eco-genetic-criticality`, `eco-genetic-warning-extensions` |
| **2** | **未来・構造・機構が変わると表現はどう壊れるか** | CREST | `crest`, `ccoc`, `mltr`, `mrm`, `ced` |
| **3** | **原因の候補を残したまま、次に何を測るか** | microdonta/RACH causal learning | current `boundary`, `mrod`; legacy Graphify node `microdonta` |
| **4** | **総合 — 三系列をつなぐjunction** | Required-State / Knowledge / Loss-Warning / Reality-to-Theory junctions | `theouni` |

The machine-readable source of truth is `thesis/series_architecture.json`. The detailed ten-unit architecture remains a provenance/component map.

## The crucial correction

The earlier v1 series draft incorrectly suggested:

```text
Eco-genetic -> CREST -> Observation design
```

Graphify does **not** contain that hard or privileged spine.

The edge-faithful view is:

```text
                 +-- Eco-genetic pillar
Introduction ----+-- CREST pillar
                 +-- microdonta/RACH pillar
                         |
                         v
              typed junctions in synthesis
```

The research pillars are independently readable and publishable. Cross-pillar travel is licensed only by an explicit registered bridge or junction condition.

## Pillar 1 — Eco-genetic

This is the one series with a direct extracted parent-to-extension edge:

```text
eco-genetic-criticality
  --mechanistic_parent_to_condition_extension-->
eco-genetic-warning-extensions
```

The scientific direction is:

```text
mechanistic eco-genetic parent
    -> warning-blind loss-generating domain
    -> warning evaluation / portability
```

The Worldline Atlas also fixes the Loss-Warning Junction:

```text
LossGeneratingState <= WarningEvaluationState
```

This does **not** mean that the common-scalar theorem mathematically implies warning failure. It means the warning experiment requires a loss-generating domain to be fixed first.

Preferred paper: **From Eco-genetic Mechanism to Conditional Warning under Fragmentation**. EGC, state-validity, and warning-only assets remain fallback/source surfaces rather than three default submissions.

## Pillar 2 — CREST

Graphify gives a hub-and-spoke architecture:

```text
CCOC --conceptual_obstruction_input--\
MLTR --conceptual_obstruction_input----> CREST
MRM  --conceptual_obstruction_input--/
CED  --downstream_evidence_licensing-->
```

`CCOC`, `MLTR`, and `MRM` are parallel structural inputs. They do not prove one another. `CED` is an evidence/reportability junction and is not ontically owned by CREST: evidence does not create the ecological distinction being licensed.

Graphify clustering also keeps important separation:

- `CREST and Evidence Licensing` is one community;
- `Transport and Mechanism Robustness` is another;
- future/open-composition is a distinct structural line.

Therefore a CREST flagship is defensible only as a **hub paper** with one core theorem/story and typed supporting modules, not as five coequal theorem papers stapled together.

Preferred paper: **When Conservation Capacity Outgrows Conservation Knowledge**. Full CCOC/MLTR/MRM/CED proofs remain supplements or fallback manuscripts.

## Pillar 3 — microdonta/RACH causal learning

The current Graphify registry was generated on **2026-08-25**, before the publication split into Boundary and MROD. Its legacy `microdonta` node is therefore stale as a physical repository label but still scientifically informative.

Graphify Community 10, `RACH Causal Learning`, already co-clusters:

- `W`-only/channel non-identifiability;
- admissible causal hypotheses;
- next-observation value / RACH-SEQ;
- controlled synthetic observation-selection validation.

Current publication mapping:

```text
channel-identifiability material -> Boundary
causal-set / next-observation material -> MROD
```

This is strong graph support for one integrated methods paper, not merely an editorial convenience.

Preferred paper: **From Identifiability Limits to Mechanism-Resolving Observation Design**.

Two outward bridges remain explicitly incomplete:

```text
microdonta --missing_evidence_risk_bridge--> CED   [proposed / inferred]
microdonta --missing_candidate_family_bridge--> MRM [proposed / inferred]
```

So causal-learning value is not already a CED license, and an admissible causal set is not automatically an MRM response-type family.

## The junction synthesis

The final chapter should not say that one concept—especially unqualified `state`—runs through everything. Graphify itself treats `state` as overloaded across repositories.

Instead the synthesis is organized around explicit intersections:

### Required-State Junction

```text
capability + future + history + mechanism
```

A joint required representation exists only under a compatible carrier/lift and typed response obligations.

### Knowledge Junction

```text
capability + evidence + causal learning
```

Required distinctions, evidence classes, causal programmes, and report target must be typed on compatible model worlds. This is the conditional meeting point of CREST/CED and the microdonta/RACH learning line.

### Loss-Warning Junction

```text
LossGeneratingState <= WarningEvaluationState
```

This is the strongest directed dependency among the three pillar programmes and belongs within the eco-genetic paper.

### Reality-to-Theory Junction

Every model-world result returns to empirical admission and a claim ceiling. Cross-repository integration never supplies natural-system validation by itself.

## Cross-series bridges are not merger licenses

The graph contains a bounded eco-genetic-to-CREST adapter, and the warning-domain-to-CREST edge is only `partial_bounded_witness_only` / inferred. Likewise the microdonta-to-CED/MRM edges are proposed/inferred.

Therefore these edges belong in synthesis and future adapter work. They are **not** reasons to merge all three pillars into one paper.

## Publication strategy

Default: **three strong papers, one per Graphify-supported pillar**.

1. Eco-genetic mechanism -> loss -> warning.
2. CREST hub-and-spoke flagship theory paper.
3. Boundary + MROD causal-learning / observation-design methods paper.

Not default:

- one paper per repository;
- one mega-paper spanning all three hubs;
- separate CCOC/MLTR/MRM/CED submissions unless the flagship fails scope;
- separate EGC/state-validity/warning submissions unless the integrated eco-genetic paper fails scope or length review.
