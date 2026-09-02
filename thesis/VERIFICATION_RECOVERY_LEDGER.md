# Thesis verification-recovery ledger — 2026-09-02

## Decision

Verification is organized by **forbidden inference**, not by chapter title or repository count.

For each chapter, the recovery chain is:

`forbidden inference → source-owned result → direct theorem / locked result / executable witness → claim ceiling`

All eight source-owned research chapters now have a direct source-backed basis for their primary forbidden inference at the recorded snapshot. Chapters 0 and 9 are intentionally different: Chapter 0 is framing, and Chapter 9 is a synthesis built from TU-1 plus the eight source-owned counterexamples rather than a standalone global theorem.

## Recovery status

| # | Chapter | Source | Verification | Core recovered basis |
|---:|---|---|---|---|
| 0 | 再利用問題 | theouni | synthesis framing | TU-1 factorization/revision debt + later chapter counterexamples |
| 1 | 観測が原理的に届かない範囲 | boundary | exact analytic + executable | `k-1-r` residual dimension + calibration/breakdown tests |
| 2 | 先行することは、警告することではない | EGWE | full-denominator locked audit | 35/35 & 33/33 events plus 48/48 & 49/49 non-events; specificity 0, AUC 0.5 |
| 3 | 境界の内側で、次に何を測るか | mrod | controlled truth-peek-free benchmark | information-guided ordering versus random ordering; nuisance/effort contrast |
| 4 | 一つの系に、状態は一つではない | eco-genetic-criticality | finite-model state separation | fragmentation gradient + cross-layer alignment counterexample |
| 5 | 未来を開くと、記憶が要る | CCOC | exact extremal synthetic witness | narrow physical cut with `2^m` open distinctions / `m` response bits |
| 6 | 能力は知識を追い越す | CREST | exact finite existence theorem | one added action, 1→`2^m` required states, exactly `m` monitoring bits |
| 7 | 法則は構造置換を越えない | MLTR | exact source-relative transport/history | route coherence + necessary/sufficient minimum history completion |
| 8 | 反復は、多様性の代わりにならない | CED | exact failure-architecture result | shared failure-domain ceiling + equal-effort independent-mode contrast |
| 9 | 総合 — 妥当性に特権的な方向はない | theouni / TU-1 | synthesis | TU-1 exact revisability + Chapters 1–8 as typed counterexamples |

## Recovered claims and ceilings

### 1. Observation boundary

`boundary` supplies a mathematical identification boundary, not a generic warning about hidden mechanisms. For `k` multiplicative channels with `r` independent direct anchors, the residual unidentified dimension is `k-1-r`; calibration transport and reciprocal-reference breakdown factors make assumption dependence explicit. The claim remains conditional on the declared channel/calibration model.

### 2. Precedence versus warning

The warning chapter has a complete denominator recovery. Each frozen threshold leads every observed loss in both audited ensembles, but the same thresholds also fire in every audited non-event. The paired denominators must remain visible; event-only lead fractions are never enough to support warning validity.

### 3. Measurement ordering

MROD has a frozen controlled benchmark in which candidate measurements are not equally useful. At budget two, information-guided ordering resolves all initial confounding edges on average while random ordering resolves `0.6045`; at budget four the guided policy uses `1.518` versus `2.673` observations and selects `0.014` versus `1.169` nuisance measurements. False exclusion remains zero in all policy-by-budget cells. This is controlled-method validation, not universal optimality.

### 4. Multiple states

The eco-genetic parent explicitly separates potential viability, realised occupancy, demographic state, diversity, and allele persistence. In the fresh fragmentation gradient, potential high-trait viability is absent across tested subdivided outcomes while realised occupancy persists at the finite endpoint. A separate alignment construction shows that common marginals can match while the exact next interaction transition differs. The chapter must not upgrade this to a claim that all five states are pairwise distinct in every configuration or that the five-state taxonomy is sufficient in nature.

### 5. Open futures and memory

CCOC directly supports the ecological wording of the chapter: a narrow physical cut is not a bound on exact causal-interface memory. The fixed-regular relay has uniformly bounded local implementation while the open grammar distinguishes `2^m` exterior patterns. This remains a synthetic finite witness; it is not evidence that a real island or corridor has large causal memory.

### 6. Capacity and knowledge

CREST supplies the strongest existence theorem in the spine. For every `m`, one newly admitted controllable action can add one viable world while refining a retained present slice from one state to `2^m` states and creating exactly `m` bits of monitoring debt under unchanged evidence. It does not claim that every small real intervention causes a large monitoring burden.

### 7. Structural replacement

MLTR now centers route coherence and minimum history completion. A single carried terminal law exists when complete carried terminal maps agree across declared routes. When they disagree, one immutable mode per distinct carried map is necessary and sufficient. These are declared structural histories and inherited semantics, not inferred natural history variables.

### 8. Repetition and failure diversity

CED Result 3 states the chapter claim almost verbatim: repetition inside one shared failure domain is not equivalent to independent failure diversity. Under the declared availability/reliability contract, within-mode repeats face a worst-case guarantee ceiling, whereas equal effort across independent modes can support a stronger guarantee. The conclusion is not that repetition is useless; it is that raw replicate count cannot generally substitute for independent failure opportunities.

## Two synthesis safeguards

### Chapter 0 is not a theorem that reuse always fails

TU-1 proves a precise state-only revisability criterion and exact revision debt after compression. Chapter 0 uses that as the cleanest formal example of the reuse problem, but the actual family of reuse failures is supplied by Chapters 1–8.

### Chapter 9 is not yet a single global non-monotonicity theorem

`Adequacy has no privileged direction` is currently a **synthesis claim**. TU-1 is exact, but the broader statement is supported by typed counterexamples across distinct scientific responsibilities: richer observation can leave mechanism unidentified; earlier signals can fail warning discrimination; measurable variables can be poor next measurements; one summary need not represent all target states; narrow physical boundaries need not limit future-response memory; a small capability change can cause large monitoring debt; source laws can fail after replacement; and repeated effort can fail to diversify failure opportunities.

A future global theorem would require a common carrier and a common typed order on both `richness` and `adequacy`. Until then, the dissertation must not collapse these dimensions into one scalar monotonicity theorem.

## Recovery gate for drafting

Before prose drafting resumes for a chapter:

1. use the source snapshot and evidence paths in `thesis/verification_recovery_registry.json`;
2. copy the chapter claim ceiling into its source map;
3. preserve negative, bounded, conditional, and synthetic-witness language from the source;
4. do not upgrade Chapter 0 or Chapter 9 into independent global theorems;
5. if a source repository changes its headline result, rerun this recovery before importing new prose.
