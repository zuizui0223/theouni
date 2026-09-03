# Source map — Chapter 9 v0.1: 総合 — 妥当性に特権的な方向はない

This map supports `thesis/drafts/final/09_no_privileged_direction_v0.1.md`. Chapter 9 is an internal synthesis unit. Its exact mathematical substrate is TU-1; Chapters 1–8 remain source-owned proved conditions and are imported only through their verified theorem contracts.

## Snapshot and chapter contract

- owning repository: `zuizui0223/theouni`
- dissertation baseline before this synthesis draft: `15dcd4f89be4144fbdd7284197251a430b5eecc7`
- verification class: `typed_synthesis_backed_by_tu1_and_eight_merged_proved_conditions`
- forbidden inference: `より詳細にする／より多く測る／より長く記憶する／より多く介入する ⇒ より妥当になる`
- chapter claim ceiling: Chapter 9 does not prove one scalar or global partial order of scientific adequacy. It states that none of the listed, differently typed richness proxies automatically certifies adequacy outside the condition attached to its scientific responsibility.

## A. Exact theorem owned by theouni: TU-1

### A1 — `theory/TU1_CONTRACT_REVISION.md`

Let old scientific state `P` and revised required state `Q` be partitions of the same finite carrier.

TU-1 proves state-only revision is possible **if and only if** the revised quotient factors through the retained old quotient:

`q_Q = f ∘ q_P`.

Equivalent formulations are:

- worlds sharing an old state also share the revised state;
- every old block is contained in one revised block;
- the old partition retains every distinction required by the revised responsibility.

If the factorization fails, the exact minimum auxiliary alphabet is

`K_rev(P→Q) = max_B r_B(P,Q)`,

where `r_B(P,Q)` is the number of revised-state blocks intersecting old block `B`. The minimum fixed-length side code is

`ceil(log2 K_rev)` bits.

TU-1 also proves that average refinement debt can be arbitrarily small while worst-case local revision debt is arbitrarily large. This is an exact statement about scientific representation after forgetting, not an empirical law about ecological memory.

### A2 — `theory/verify_tu1.py`

Executable verification covers:

- the factorization/revision boundary;
- exact auxiliary alphabet size;
- average debt ≤ worst-case debt;
- balanced equality cases;
- divergence family for `m=1..8`.

The executable layer checks the finite implementation; it does not create the theorem or empiricalize the partitions.

## B. The authoritative eight-chapter proved-condition registry

### B1 — `thesis/proved_condition_registry.json`

This registry is authoritative for the theorem-level condition imported from each source-owned research chapter.

For Chapters 1–8 it stores:

- scientific question;
- condition class;
- exact `proved_condition` text;
- proof source;
- verification source;
- merged source status/SHA where applicable;
- sharpness or locked application;
- claim ceiling.

Chapter 9 must not paraphrase a source theorem into a weaker slogan when a sharper merged condition is available.

The current eight conditions are:

1. **Boundary:** new exact scalar observation reduces ambiguity iff it increases observation rank.
2. **EGWE:** perfect event-conditioned binary precedence fixes sensitivity but leaves specificity free; binary AUC follows the full denominator.
3. **MROD:** strict adaptive second-step advantage iff no candidate is optimal on every positive-probability branch.
4. **Eco-genetic criticality:** one exact directionally coherent scalar exists iff target vectors form a product-order chain.
5. **CCOC:** fixed local/static resources can coexist with arbitrary `m`-bit open-future response innovation; separate coherence premises give positive portability.
6. **CREST:** +1 carrier world under one new action can coexist with arbitrary `m`-bit state/monitoring burden, so carrier gain alone gives no finite burden bound.
7. **MLTR:** portability has an iff fiber criterion, repair is unique coarsest, and distinct carried maps determine necessary/sufficient history modes.
8. **CED:** equal two-read depth/diversity allocation reverses at `p*=2-2^(1/k)`; fixed mode count separately imposes an availability ceiling.

These conditions remain owned by the source repositories. Chapter 9 compares their logical roles; it does not transfer theorem ownership to theouni.

## C. Typed synthesis matrix v2

### C1 — `thesis/typed_synthesis_matrix.json`

Schema `theouni-typed-synthesis-matrix.v2` maps each source theorem to one cross-chapter synthesis row with:

- responsibility type;
- richness proxy;
- forbidden monotone shortcut;
- condition class;
- exact proved condition;
- proof/verification source;
- decisive application;
- safe conclusion.

For every Chapter 1–8 row, `condition_class` and `proved_condition` must match the authoritative proved-condition registry exactly.

The matrix therefore cannot silently retain an older statement such as `k-1-r` as the Chapter 1 headline after Boundary has proved the sharper rank criterion, or “diversity beats repetition” after CED has proved the threshold reversal.

### C2 — `scripts/validate_typed_synthesis_matrix.py`

The validator enforces:

- eight unique research rows and eight distinct scientific responsibility types;
- exact condition-class and proved-condition equality with `proved_condition_registry.json`;
- theorem-specific non-regression markers for Chapters 1–8;
- Chapter 9's bounded synthesis status;
- the prohibition on a universal scalar adequacy theorem;
- TU-1 as exact substrate rather than a theorem that absorbs the source programmes.

## D. Synthesis interpretation note

### D1 — `thesis/TYPED_SYNTHESIS_RECOVERY.md`

This note defines the prose discipline for Chapter 9.

Allowed synthesis:

> Across the distinct responsibilities studied here, none of the recorded richness proxies is an automatic certificate of adequacy; each responsibility instead has a condition specifying when reuse, refinement, measurement, transport, or reporting is licensed.

Forbidden synthesis:

- “more information is worse”;
- “more information is always better”;
- all eight quantities form one scalar information axis;
- the eight source theorems are special cases of TU-1;
- the eight counterexamples prove one universal non-monotonicity theorem;
- the source programmes lose their independent theorem/evidence ownership.

## E. Typed row boundaries

The eight rows must remain distinct.

| Chapter | Responsibility | Mathematical object that decides adequacy | Do not substitute |
|---:|---|---|---|
| 1 | mechanism identification | rank / row span of observation operator | observation count or biological proximity |
| 2 | warning discrimination | event + non-event denominator, specificity/AUC | event lead consistency alone |
| 3 | adaptive mechanism-learning | branchwise candidate utility and argmax intersection | candidate count or adaptivity slogan |
| 4 | multi-target state | product-order comparability of target vectors | state-detail count |
| 5 | open-future interface memory | exact future-response quotient / decoder addressability | physical cut width |
| 6 | capability-dependent knowledge | required partition/evidence refinement | carrier-size gain |
| 7 | source-relative transport | carried-fiber exactness / carried-map equality | source fit or unlabeled partition shape |
| 8 | failure-aware evidence | sensitivity, target dimension, mode availability | raw replicate count |

No arithmetic pooling across these rows is authorized.

## F. Exact substrate versus source-owned conditions

TU-1 is not the common mathematical theorem of Chapters 1–8.

It provides one exact meta-level reuse criterion after a representation has already been compressed on the same carrier.

The source chapters can create situations that motivate a revised responsibility or reveal a failed reuse, but their theorem objects differ:

- Boundary changes observation rank;
- EGWE changes prediction denominators;
- MROD changes branch-conditioned experiment choice;
- eco-genetic-criticality changes target-order representability;
- CCOC changes future grammar;
- CREST changes capability and required state/evidence;
- MLTR changes carrier/replacement semantics;
- CED changes failure architecture and reportability.

Do not write `Ch1–8 follow from TU-1` or an equivalent statement.

## G. Constructive synthesis: revision-aware compression

The dissertation may recommend a bounded workflow:

1. declare the present scientific responsibility;
2. identify the minimum distinctions needed for it;
3. declare plausible future changes in responsibility;
4. test whether the revised response factors through the retained representation when TU-1 applies;
5. retain or acquire the minimum auxiliary distinction needed for the foreseeable revision;
6. use the source chapter's own adequacy condition when the scientific object is observation rank, warning discrimination, adaptive design, state scalarization, future memory, capability resolution, law transport, or failure-aware evidence.

This is not a recommendation to retain all raw detail forever.

## H. Worldline and editorial-order boundary

### H1 — `universe/WORLDLINE_ATLAS.md`

The worldline atlas remains the non-ordered theory map. The ten-chapter order is editorial and does not convert adjacent chapters into logical dependencies.

### H2 — `thesis/transition_recovery_matrix.json`

All chapter transitions are typed question handoffs. Chapter 9 may summarize the sequence, but it must not write it as one theorem-proof chain in which Chapter 1 logically implies Chapter 2, and so on.

## Section-to-source matrix

| Draft section | Primary source | Formal/validator support | Main boundary |
|---|---|---|---|
| 1. Reuse framing | D1 | chapter/proved-condition registries | not anti-information |
| 2–3. TU-1 theorem/debt | A1 | A2 | exact same-carrier theorem only |
| 4. TU-1 ≠ Ch1–8 | B1/C1 | C2 | no source absorption |
| 5–11. Eight chapter conditions | B1 | source proof/verification paths in registry | retain each theorem type and ceiling |
| 12. No scalar adequacy order | C1/D1 | C2 | no pooling or global partial order |
| 13–15. Relational adequacy / revision-aware compression | A1/D1 | TU-1 + synthesis validators | constructive synthesis, not universal metric |
| 16. Scope | B1/C1/D1 | recovery/proved-condition validators | no intrinsic state or global theorem |
| 17. Closing loop | A1/B1 | chapter source maps | reuse only through responsibility-specific condition |

## Drafting gate

1. Keep TU-1 as the only exact theorem owned by Chapter 9.
2. Keep all eight source rows matched exactly to the proved-condition registry.
3. Name both the richness type and the adequacy responsibility in every cross-chapter comparison.
4. Do not introduce a scalar adequacy score or pooled effect.
5. Verify philosophy-of-science, sufficient-statistic/representation, model adequacy, transferability, and measurement-validity literature before citation-ready status.
6. Keep `not evaluable`, partial identification, set-valued reporting and STOP as legitimate endpoints when the relevant condition fails.
