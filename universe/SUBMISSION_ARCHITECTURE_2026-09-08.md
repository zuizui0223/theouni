# Submission architecture — two-paper consolidation

Status: **canonical portfolio submission plan, 2026-09-08**.

## Decision

The observation/evidence programme is consolidated into exactly **two submission papers**.

```text
                         compatible worlds
                               |
              +----------------+----------------+
              |                                 |
              v                                 v
        PAPER 1: OBSERVATION               PAPER 2: EVIDENCE
     how records gain/lose meaning       what distinctions are licensed
              |                                 |
       V3 + REC + TNOA                 Boundary + MROD + CED
```

The source repositories remain independent for theorem provenance, code, frozen results, and reproducibility. They are **not separate near-term submission targets**.

`theouni` remains the ontology / claim-firewall / provenance layer and does not acquire ownership of source theorems or empirical evidence.

---

# Paper 1 — OBSERVATION

## Working title

**Refine before loss: an information-order theory for ecological observation**

Alternative descriptive title:

**Observation before inference: refinement, record-entry selection and semantic coarsening in ecological sensing**

## Scientific question

> How does an observation system change the set of latent worlds compatible with the scientific record as information is added, opportunities are selected into or out of the record, and retained evidence is semantically coarsened?

## Source ownership

### V3 — retained-information refinement

Contributes:

- compatible-world refinement by retained side/reference information;
- reversible decomposition versus destructive suppression;
- general forward-model contraction;
- physical-proxy realizability and reference-portfolios;
- frozen synthetic strict-refinement evidence.

Primary synthetic anchor already available:

- matched temporal reference balanced utility `0.8327` versus `0.5688` without reference;
- nuisance false-frame rate `0.0272` versus `0.2986` without reference;
- time-broken controls show that reference presence alone is insufficient.

V3 does **not** remain a separate submission target under this two-paper plan.

### REC — record-entry selection

Contributes:

- external exposure/reference denominator;
- shadow / no-row support;
- non-identifiability of omitted biology from a selected event table alone;
- downstream irreversibility after upstream omission;
- partial recovery and the calibration/transport domain of correction;
- external-data validation.

Primary empirical anchors:

- fox/badger CCTV-reference result: true-pass badger proportion `0.3598`, trigger `0.4393`, confirmed capture `0.4828`;
- position-standardized trigger and capture shifts remain positive in `3/4` positions;
- BirdVox protected result shows a true temporal contrast lost after upstream omission even under oracle true-entry-only downstream semantics;
- broad camera+position transport of correction is falsified rather than rescued.

REC does **not** remain a separate submission target under this two-paper plan. Its external-data results become the field-facing validation block of Observation.

### TNOA — semantic preservation / coarsening

Contributes:

- positive non-complementary target and nuisance evidence;
- separate observability and attribution evidence;
- explicit unresolved state rather than forced complement labels;
- information loss under deterministic semantic collapse;
- closed-world quantitative validation.

Primary quantitative anchor:

- median compatible target-prevalence width about `0.030` with B/T/N/U retained versus `0.266` after binary target/not-target coarsening;
- median relative width reduction about `84.45%` among non-zero binary widths;
- the richer representation is never structurally wider than its deterministic coarsening.

TNOA does **not** remain a separate submission target under this two-paper plan.

## Observation paper spine

```text
possible worlds / observation opportunities
        |
        v
primary retained observation
        |
        +-- V3: add justified retained information
        |         -> compatible-set refinement
        |
        +-- REC: support may disappear before row entry
        |         -> shadow/no-row non-identifiability
        |
        +-- TNOA: rich retained evidence may be collapsed
                  -> semantic coarsening / manufactured certainty risk
```

The paper's common object is the compatible-world fibre / identified set of the retained record.

## Main results

### O1 — Retained augmentation is refinement, not automatic correction

A non-destructive additional channel weakly refines compatible worlds. Strict benefit depends on whether the channel actually separates target-relevant worlds. Projection/subtraction is not licensed merely by correlation with nuisance.

### O2 — Support selection is a different information loss

When an opportunity leaves no row, downstream semantics cannot identify the omitted biological composition from the selected table alone. Independent exposure/reference information is required to audit the shadow support.

### O3 — Semantic coarsening can destroy distinctions that survived acquisition

A deterministic coarse label cannot contain more identification information than the rich retained evidence from which it was computed. Unresolved states are therefore scientific representations of non-identification, not merely classifier abstention.

### O4 — Information loss is irreversible without independent new information

Reversible transforms preserve the observation partition; non-injective replacement, support deletion, and semantic collapse do not. Downstream processing of the collapsed object alone cannot recreate a lost distinction.

## Validation hierarchy

Observation deliberately mixes validation levels, but labels them explicitly:

1. **exact finite/synthetic worlds** — structural and strictness witnesses;
2. **larger controlled synthetic stress tests** — V3/TNOA frozen results;
3. **external empirical datasets** — REC camera-trap and acoustic results;
4. **future prospective same-system validation** — PolliPi / InsePi, not required for the initial paper claim.

## What Observation must not claim

- universal physical benefit of reference channels;
- universal numerical thresholds;
- natural pollinator detection accuracy;
- that a denominator ledger alone identifies omitted biological truth;
- universal transport of entry correction;
- that T/N/O/C/U semantics are uniquely optimal among all possible rich vocabularies;
- optimal future measurement choice or target-safe reportability. Those belong to Evidence.

## Canonical manuscript home

`zuizui0223/v3` becomes the submission-facing home for **Observation**.

`rec` and `tnoa` remain pinned source/evidence repositories. Their current standalone manuscripts are retained for provenance and source text but are superseded as independent submission targets.

---

# Paper 2 — EVIDENCE

## Working title

**From identification limits to evidence-directed measurement: learning, licensing and adaptive observation in ecology**

Alternative concise title:

**Evidence for ecological distinctions: identification boundaries, measurement choice and honest reporting**

## Scientific question

> Given the worlds still compatible with the current record, which distinctions are identifiable now, which distinctions matter for the declared scientific target, what should be measured next, and when is a deterministic report actually licensed?

## Source ownership

### Boundary — current identification limit

Contributes:

- observational-equivalence / identified-set boundary under the current observation map;
- distinction between precision and structural identification;
- exact log-linear unidentified dimension `k - rank(M)`;
- a new scalar measurement changes structural rank iff it adds an observation direction outside the current row span;
- calibration/transport boundary and joint-set reporting logic.

Boundary does **not** remain a separate submission target under this plan. It becomes Evidence Part I: current-state identification.

### MROD — mechanism-learning observation design

Contributes:

- admissible mechanism region;
- residual mechanism entropy / resolvability;
- normalized observation information value `I(S;Q | A)/K`;
- sequential recomputation of candidate value;
- controlled benchmark showing more efficient mechanism resolution than random ordering.

MROD supplies **learning value**: how much a candidate is expected to reduce residual mechanism ambiguity.

MROD does **not** remain a separate submission target under this plan.

### CED — target licensing / reportability

Contributes:

- experiment-induced quotient and sharp compatible target set;
- target-safe quotient: only distinctions needed for the declared future target must be resolved;
- failure architecture determining whether a nominal distinction is evidentially trustworthy;
- explicit false-resolution / cost contract;
- adaptive target-safe experiment choice and stopping/reporting.

CED supplies **licensing value**: whether the evidence justifies the requested target report under the declared risk contract.

CED does **not** remain a separate submission target under this plan. Its current Paper B is the strongest existing manuscript skeleton for Evidence and becomes the canonical drafting base.

## Critical synthesis: two values, not one

Evidence must preserve the distinction already formalized in `theouni`:

```text
CausalLearningValue != TargetLicensingStatus
```

A candidate observation can be highly informative about mechanism while irrelevant to the declared target. Conversely, a target-safe observation may license the report without maximizing full mechanism entropy reduction.

Therefore Evidence should not seek one universal observation-value scalar. It has two declared utilities:

1. **learning utility** — MROD mechanism information;
2. **licensing utility** — CED target-safe reportability under false-resolution/cost constraints.

This distinction is a central integrated contribution rather than an overlap problem.

## Evidence paper spine

```text
current evidence
      |
      v
Boundary
what distinctions remain structurally unresolved?
      |
      v
CED target-safe requirement
which unresolved distinctions can change the declared target?
      |
      +----------------------+
      |                      |
      v                      v
MROD learning value      CED licensing value
reduce mechanism         resolve target-relevant
ambiguity                distinctions safely
      |                      |
      +----------+-----------+
                 v
        choose next observation
                 |
                 v
        update compatible worlds
                 |
                 v
       stop / remain ambiguous / report
```

## Main results

### E1 — Current structural boundary

More precise repetition is not the same as a new identification direction. The current observation map determines the equivalence/identified set that any downstream analysis must respect.

### E2 — Full identification is neither necessary nor sufficient for a declared target

CED's target-safe quotient formalizes the minimum distinctions that matter for the requested future report. A current record may still fail to identify the required target-safe block; honest output then remains set-valued.

### E3 — Observation value is objective-relative

MROD and CED expose two distinct values. Mechanism-learning information and target-licensing value can disagree. Evidence should include a unified finite-world counterexample demonstrating this divergence directly.

### E4 — Reliability architecture governs whether refinement can be credited

Nominally distinct records are not automatically trustworthy when observation modes share failure structure. CED's failure-aware results determine whether a candidate split is evidentially licensed.

### E5 — Adaptive acquisition and stopping

Candidate observations are selected under the declared utility and reliability contract, outcomes are revealed only after selection, compatible worlds are updated, and the process stops at target resolution, information limits, or budget/risk boundaries.

## What Evidence must not claim

- that mechanism entropy and target licensing are numerically interchangeable;
- universal optimality over undeclared experiment vocabularies;
- that precision alone changes structural identification rank;
- natural causal identification without declared world/model assumptions;
- that every target-safe report requires full mechanism identification;
- field performance of PolliPi/InsePi before their prospective validation completes.

## Canonical manuscript home

`zuizui0223/ced` becomes the submission-facing home for **Evidence**, because its Paper B already contains the most mature integrated reportability manuscript and MEE production machinery.

`boundary` and `mrod` remain pinned theorem/software/result repositories. Their current standalone manuscripts are retained for provenance but superseded as independent submission targets.

---

# Relationship between the two papers

The papers are sequential but non-overlapping.

```text
OBSERVATION
What record do we actually have, and what information did the observation system add or lose?
        |
        v
retained compatible-world set
        |
        v
EVIDENCE
What may that record identify/license, and what should be measured next?
```

The firewall is:

```text
Observation operation
    !=
Evidence entitlement
```

Observation owns **how the record changes information**.
Evidence owns **what conclusions/actions that information licenses**.

A richer observation may exist without licensing a deterministic target report. Conversely, Evidence cannot license a distinction that Observation has already irreversibly discarded unless genuinely independent new information is acquired.

---

# Physical and natural validation

`pollipi` and `insepi` become shared empirical platforms for the two-paper programme, not additional theory papers by default.

## InsePi V13

Primary role:

- physical test of whether controlled observation/intervention channels create reproducible real-camera distinctions;
- can update Observation's physical strict-refinement boundary and Evidence's measurement/identification boundary after the frozen held-out result exists.

Do not delay either initial theory/synthetic submission solely for V13 unless the target editor requests physical validation.

## PolliPi

Primary role:

- prospective natural observation data with fixed primary record, shadow/provenance logging, natural nuisance and real biological targets;
- later same-system validation of V3/REC/TNOA and evidence-directed additional acquisition.

---

# Submission plan

## Paper 1 — Observation

Build first from `v3/manuscript/LAYER1_SYNTHETIC_PAPER_DRAFT_V2.md`, but revise it so:

- U1–U3 are the common synthetic spine;
- REC external empirical results become the principal reality-facing validation;
- TNOA's closed-world quantitative coarsening result remains a large synthetic stress test;
- U4 prospective design and U5 intervention are removed from headline novelty and used only as the bridge to Evidence.

## Paper 2 — Evidence

Build from the current CED Paper B manuscript, adding:

- Boundary as the explicit current-identification opening layer;
- MROD as the mechanism-learning branch;
- a new learning-versus-licensing divergence benchmark;
- one shared adaptive acquisition diagram and stopping contract.

CED's existing target-safe quotient, failure architecture, and risk-limited reporting remain the reportability backbone.

## Submission timing

The two papers may be prepared in parallel. Submit **Observation first**, then Evidence after the cross-paper overlap audit is clean. They may target the same journal only if the editor is told explicitly that they answer different questions and neither manuscript depends on unpublished results from the other.

Preferred practical route:

1. Observation — methods/theory paper with synthetic + external empirical validation.
2. Evidence — follow-on methods/theory paper on identification, learning versus licensing, and adaptive experiment design.

No standalone submission of V3, REC, TNOA, Boundary, MROD or CED Paper B remains in the canonical plan unless this two-paper strategy is later explicitly revoked.

---

# One-sentence programme map

**Observation asks how scientific records gain, lose and collapse distinctions; Evidence asks which surviving distinctions support a scientific claim and which new measurements should be acquired to license it.**
