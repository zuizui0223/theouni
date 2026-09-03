# Source map — Chapter 7 v0.1: 法則は構造置換を越えない

This map supports `thesis/drafts/final/07_law_replacement_v0.1.md` and is locked to merged MLTR snapshot `d9e23d27c385759b9e1fea93a556f30618122fe1`.

## Snapshot and chapter contract

- owning repository: `zuizui0223/mltr`
- recovered theorem snapshot: `d9e23d27c385759b9e1fea93a556f30618122fe1`
- verification class: `verified_portability_iff_unique_coarsest_repair_and_history_iff`
- forbidden inference: `ある構造で成り立った法則 ⇒ 置換後の構造でも成り立つ法則`
- chapter claim ceiling: exact finite source-relative transport under declared source–target relations and inherited label semantics; no inference of real replacement history and no claim that positive source-relative defect rules out compact target-only abstractions.

## A. Master theorem

### A1 — `docs/master_theorem_proof.md`

The source master theorem proves the full chapter chain.

### Portability

The carried target partition is exact **if and only if** the following are constant within every carried target fiber:

1. output;
2. legal-action row;
3. successor carried label under every declared legal action.

Necessity follows because an exact quotient requires representative-independent quotient functions. Sufficiency follows because those uniform quantities define well-defined quotient functions on the carried labels.

### Local obstruction

If portability fails, one within-fiber pair differing in output, action legality, or successor carried block is a finite certificate of failure.

### Unique coarsest repair

Starting from the carried source labels, iterative splitting by output, legal-action row and successor block stabilizes on a finite target. Any exact partition refining the carried labels must refine every iteration, so the fixed point is the **unique coarsest exact source-relative repair**.

### Minimal defect

Because every exact source-relative target partition refines the fixed point, the repaired state-count and log-state increases are minimal among source-relative exact target descriptions. Transport defect is therefore interpreted only through this proved minimal repair.

### Route coherence and history

For a rooted finite replacement graph:

- one route-independent inherited terminal label map exists iff all declared root-to-terminal paths induce the same complete carried terminal map;
- if carried maps differ, one immutable history mode per distinct carried map is necessary and sufficient to preserve all declared path-specific inherited label semantics before exact relative repair.

The theorem explicitly does **not** say distinct carried maps force distinct unlabeled final repair partitions.

## B. Publication architecture and novelty boundary

### B1 — `manuscript/paper_a_main.tex`

Supports the publication-facing ecological framing:

- exact portability under structural change;
- source-relative rather than target-only abstraction;
- target-only intervention as an operational obstruction;
- history coherence as the route-level headline;
- classical exactness/refinement machinery kept as infrastructure.

### B2 — `docs/publication_completion_spine.md`

Supports the intended explanatory sequence:

1. carry source labels;
2. test portability;
3. expose a local obstruction;
4. repair only the failed inherited distinctions;
5. quantify the minimum source-relative defect;
6. test complete carried terminal maps across routes;
7. add history only when map equality fails.

### B3 — `docs/novelty_and_journal_strategy.md`

Required priority firewall:

- do not claim novelty for partition refinement, bisimulation, lumpability, quotient construction or generic path dependence;
- do not present transport defect as a standalone theorem;
- keep the central claim on source-relative route coherence and the exact equality classes of complete carried maps.

## C. Executable history proof obligations

### C1 — `tests/test_section5_proof_obligations.py`

The source tests verify over exhaustive small carried-map families that:

- minimum history-mode count equals the number of distinct complete carried maps;
- two paths share a mode exactly when their carried maps are identical;
- any assignment using fewer modes than the number of distinct maps is incompatible;
- the minimum assignment is invariant to path ordering up to arbitrary mode renaming;
- repeated identical maps need only one mode;
- distinct inherited label maps remain distinct even when they have the same unlabeled partition shape;
- a known coherent route witness gives exactly one history mode.

These tests verify the finite implementation/semantic obligations. The quantified theorem remains owned by the written proof.

## D. Source-relative versus target-only claim boundary

Allowed conclusion:

> if the carried source law fails the exactness test, MLTR returns the least exact target refinement that still respects inherited source labels.

Forbidden upgrade:

> the target has no alternative compact law.

A target-only abstraction that discards source provenance is a different estimand and may be coarser than the source-relative repair.

Likewise, a route disagreement in inherited labels does not imply the physical target differs or that the unlabeled repaired partitions differ. It implies that no one route-free **inherited label map** preserves all declared path-specific source semantics.

## E. Three distinct questions that must not be collapsed

### E1 — portability

Question: can the source law be reused unchanged on one target relation?

Answer: yes iff the three within-fiber uniformity conditions hold.

### E2 — repair

Question: if unchanged reuse fails, what is the least exact repair that retains source semantics?

Answer: the unique coarsest fixed-point refinement of the carried partition.

### E3 — history

Question: if several routes reach one terminal target, can they share one inherited semantics?

Answer: yes iff their complete carried terminal maps agree; otherwise the equality classes of those maps are exactly the required immutable history modes.

The dissertation must keep these three layers separate.

## F. Ecological interpretation boundary

The source uses turnover, rewiring, species replacement and target-only intervention as ecological interpretations of the finite theorem.

Allowed use:

- a source ecological state label remains portable only if target members sharing it remain equivalent for the declared output/action/successor responsibility;
- a new target intervention can reveal a previously hidden within-label difference;
- only the exposed inherited distinction need be retained in the unique coarsest source-relative repair;
- historical context is required only when declared replacement routes carry incompatible source label maps.

Do not:

- infer replacement relations from observational similarity;
- call the history mode an observed ecological variable;
- infer chronology from route labels;
- claim portability because target fits the same regression form while inherited transition semantics differ.

## G. Relation to Chapters 6 and 8

### G1 — Chapter 6 → 7

CREST asks how a capability change can increase required present-state and monitoring resolution. MLTR asks whether an already defined inherited law remains exact after a declared structural replacement.

Capability expansion is not structural replacement. The transition is an editorial question handoff, not a theorem implication.

### G2 — Chapter 7 → 8

MLTR concerns semantic transport of a law across target structure/history. CED concerns evidence strength under shared versus independent failure opportunities.

A transported law being exact says nothing about evidential independence of repeated measurements.

## Section-to-source matrix

| Draft section | Primary source | Executable/formal support | Main boundary |
|---|---|---|---|
| 1. Reuse question | B1/B2 | proved-condition registry | source-relative transfer, not generic context dependence |
| 2. Source/target relation | B1 | source relation contract | relation declared, not inferred |
| 3. Portability iff | A1 | source tests | exact finite carried fibers |
| 4. Local obstruction | A1/B2 | finite witness machinery | one pair certifies failure |
| 5. Coarsest repair | A1 | fixed-point implementation | classical machinery, source-relative constraint |
| 6. Defect | A1/B3 | accumulating witnesses | definition tied to minimal repair |
| 7. Route coherence | A1/B1 | path transport implementation | complete maps, not block counts |
| 8–9. History modes | A1 | C1 | inherited semantics, not unlabeled partition shape |
| 10. Three questions | A1/B2 | — | portability ≠ repair ≠ history |
| 11. Proof obligations | C1 | exhaustive small families | tests do not replace proof |
| 12. Ecology | B1/B2 | conceptual worked case | no inferred natural history |
| 13. Scope | A1/B3 | proved-condition registry | finite source-relative theorem only |
| 14. Transition | G2 | transition validator | question handoff to evidence reliability |

## Drafting gate

1. Keep the portability iff theorem before any ecological example.
2. Keep the unique coarsest repair proof visible so `transport defect` never floats as an unsupported metric.
3. Make the route-level result the chapter peak: equality of complete carried maps gives route independence; equality classes give minimum history modes.
4. Retain the same-partition-shape/different-label warning explicitly.
5. Verify ecological transferability, lumpability/bisimulation and historical-contingency literature before citation-ready status.
