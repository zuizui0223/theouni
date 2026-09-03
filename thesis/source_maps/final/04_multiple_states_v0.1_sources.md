# Source map — Chapter 4 v0.1: 一つの系に、状態は一つではない

This map supports `thesis/drafts/final/04_multiple_states_v0.1.md`. It preserves the original verification-recovery baseline `290663cd25dd2ab06ef8913f97696fd29370f7f2` and refreshes the theorem-level chapter source to merged eco-genetic-criticality snapshot `2a35b2d2b11f4b8a00b8a4346bdba90773511a71`.

## Snapshot and chapter contract

- owning repository: `zuizui0223/eco-genetic-criticality`
- previous recovered evidence baseline: `290663cd25dd2ab06ef8913f97696fd29370f7f2`
- current theorem snapshot: `2a35b2d2b11f4b8a00b8a4346bdba90773511a71`
- verification class: `verified_scalar_iff_plus_locked_finite_crossing`
- forbidden inference: `生態遺伝的に要約した ⇒ 五つの側面を代表した`
- chapter claim ceiling: exact scalar representability for a declared finite oriented target set plus bounded finite-model counterexamples; no universal natural-state ontology or rejection of approximate indices.

## A. Headline theorem: when one scalar state exists

### A1 — `docs/common_scalar_state_theorem_2026-09-03.md`

For finite target vectors `T(omega)=(T_1,...,T_m)` whose coordinates are oriented so higher means no worse, the source defines an exact directionally coherent sufficient scalar `h` by the existence of nondecreasing functions `f_j` with `T_j=f_j∘h`.

The theorem proves:

> an exact directionally coherent sufficient scalar exists **if and only if** the distinct target vectors form a chain under coordinatewise product order.

### Necessity

If `h(omega)<=h(omega')`, monotonicity of every `f_j` forces `T_j(omega)<=T_j(omega')` for every target. Therefore every pair of target vectors must be comparable.

### Sufficiency

If the finite distinct target vectors form a chain, rank the vectors along that chain. Each target coordinate is then nondecreasing with rank, so its coordinate function reconstructs the target from one scalar exactly.

### Consequence

One crossing pair is an exact impossibility certificate for one common monotone scalar. This is stronger than reporting that two variables have different response curves.

## B. Independent theorem verification

### B1 — `tests/test_common_scalar_state_theorem.py`

Supports:

- constructive scalar recovery on chain-ordered tables;
- rejection of crossing pairs;
- duplicate target-vector handling;
- exhaustive independent search over scalar labelings for all small three-state/two-target binary tables;
- direct parsing of the locked H3 summary and verification of the two-versus-sixteen-patch crossing.

The brute-force oracle is independent of the constructive theorem implementation at the small finite scale used for proof-obligation checks.

## C. Locked H3 crossing applies the theorem

### C1 — `docs/H3_FRAGMENTATION_GRADIENT_SENSITIVITY_RESULTS.md`

The frozen finite-model evidence contains the following paired retained medians:

| target | 2 patches | 16 patches | direction |
|---|---:|---:|---|
| interaction | `0.001744` | `0.001244` | down |
| local effective size | `0.221311` | `0.033058` | down |
| realised high-trait mass | `0.282918` | `0.393880` | up |

After orienting higher as no worse, these target vectors cross. Therefore the product-order chain condition fails on the locked state set. Authorized conclusion:

> no exact directionally coherent scalar can simultaneously preserve the crossed declared targets over that finite evidence set.

Forbidden upgrades:

- no claim that every possible five-target table is non-scalarizable;
- no claim that approximate health indices are impossible;
- no claim that real ecosystems universally exhibit this crossing.

## D. Potential viability versus realised occupancy remains a second direct separation

The same H3 gradient supports:

- one-patch potential high-trait viability present in `1037/1037` supported outcomes;
- every tested subdivision 2–16 patches: potential viability absent in `1037/1037` outcomes;
- realised high-trait occupancy nevertheless present at the 30-generation endpoint in approximately `99.6–100%` of supported trajectories.

This supports finite state separation but not a universal lag law.

## E. Primary manuscript and evidence taxonomy

### E1 — `manuscript/main_text.md`

Supports:

- Type T / C / H / S separation;
- potential viability versus realised occupancy;
- interaction/effective-size/high-trait response-shape divergence;
- migration and branch-dependent viability results at their declared theorem/closure levels;
- the five target-facing synthesis: potential viability, realised occupancy, demographic state, genetic diversity, allele persistence.

The new scalar theorem sharpens but does not replace these source-owned ecological results.

## F. Alignment representation boundary

The source's alignment counterexample supports a separate statement: simulator states can match common coarse marginals—including census, interaction and allele-frequency marginals, realised trait-bin state, `H_alpha`, `H_gamma`, and `F_ST`—while differing in patchwise cross-layer alignment and exact next interaction response.

Authorized conclusion:

> matching common coarse marginals need not imply transition equivalence.

Do not upgrade this to a universal direction of alignment-induced long-term loss; the fixed campaign did not establish that stronger claim.

## G. TU-3 representation firewall

### G1 — `theory/TU3_LOSS_STATE_INVARIANCE.md`

Supports:

- target/loss-response quotient indexed by declared responsibility;
- fiber-homogeneity criterion for safe forgetting;
- arbitrary nuisance inflation with unchanged required quotient;
- one hidden response-relevant coordinate invalidating a coarse projection.

TU-3 answers a different question from the scalar theorem. The scalar theorem asks whether several targets share one monotone sufficient axis. TU-3 asks whether one raw coordinate may be omitted for one target signature.

## Section-to-source matrix

| Draft section | Primary source | Verification | Main boundary |
|---|---|---|---|
| 1. Single-summary problem | E1 | recovery registry | target-relative, not ontology |
| 2. Common-scalar theorem | A1 | B1 | exact finite oriented targets |
| 3. Locked crossing | C1 | B1 locked-data test | finite Type S application |
| 4. Viability ≠ occupancy | C1/E1 | frozen campaign | no universal lag |
| 5. Evidence types | E1 | — | T/C/H/S separated |
| 6–7. Response/genetic distinctions | E1 | source tests | no universal dose-response |
| 8. Alignment | F | source certificate | no directional long-horizon risk law |
| 9. TU-3 | G1 | `theory/verify_tu3.py` | raw detail ≠ required state |
| 10. Scope | A1/C1/E1 | recovery registry | finite/declaration bounded |
| 11. Transition | transition recovery matrix | transition validator | handoff, not proof implication |

## Drafting gate

1. Keep the scalar iff theorem before the descriptive fragmentation results.
2. Keep the 2-vs-16 crossing values explicit so the impossibility conclusion is visibly data-connected.
3. Keep `1037/1037` potential viability paired with `99.6–100%` occupancy to retain the independent state-separation result.
4. Do not treat the five target names as a universal ontology.
5. Keep H2 warning evidence out of this chapter; predictive warning validity belongs to Chapter 2/EGWE.
