# Source map — Chapter 3 v0.1: 境界の内側で、次に何を測るか

This map supports `thesis/drafts/final/03_next_measurement_v0.1.md` and is locked to MROD snapshot `5a89c3f77b3987751652541086816231507edf9d` unless the verification-recovery registry is deliberately refreshed.

## Snapshot and chapter contract

- owning repository: `zuizui0223/mrod`
- recovered snapshot: `5a89c3f77b3987751652541086816231507edf9d`
- verification class: `verified_controlled_truth_peek_free_benchmark`
- forbidden inference: `測れるものは測る価値がある ⇒ 測る順序に良し悪しはない`
- chapter claim ceiling: controlled validation of observation selection over the declared synthetic mechanism/candidate family; no universal optimality and no natural-system causal-mechanism claim.

## A. Primary methods manuscript

### A1 — `paper/manuscript.md`

Supports:

- retaining the full admissible mechanism region rather than forcing a winner;
- role separation among `observed_target`, `input_context`, `diagnostic_only`, and `future_observation`;
- residual mechanism entropy `D=H(S|A_epsilon)` and normalized resolvability `R=1-D/K`;
- observation information value `V(Q)=I(S;Q|A_epsilon)/K` when candidate outcomes form a verified partition;
- sequential recomputation after each realised observation;
- fail-closed `non-estimable` treatment when a candidate partition is unavailable;
- controlled validation and limitations.

## B. Frozen G2 evidence

### B1 — `paper/results/g2_frozen_v2_summary.json`

The frozen result record identifies protocol `rach-g2-truth-peek-free-v2` and stores five-seed aggregates.

Authorized headline values:

### Budget 2

Information-guided:

- fraction converged: `0.990`
- mean fraction of initial confounding edges resolved: `1.000`
- mean observations: `1.505`
- mean nuisance/distractor selections: `0.001`
- false exclusion: `0`

Random order:

- fraction converged: `0.435`
- mean fraction resolved: `0.6045`
- mean observations: `1.821`
- mean nuisance selections: `0.974`
- false exclusion: `0`

### Budget 4

Information-guided:

- fraction converged: `0.999`
- mean fraction resolved: `1.000`
- mean observations: `1.518`
- mean nuisance selections: `0.014`

Random order:

- fraction converged: `0.940`
- mean fraction resolved: `1.000`
- mean observations: `2.673`
- mean nuisance selections: `1.169`

Descriptive ratio: `1.169/0.014 = 83.5`; use with absolute values because ratios are unstable near zero.

All policy-by-budget cells have zero hidden-truth false exclusion.

### B2 — `paper/supporting_information.md`

Supports the frozen table, uncertainty summaries, truth-peek-free benchmark design, and explicit statement that the methods submission excludes the separate Boundary Perspective and natural mechanism claims.

### B3 — `paper/check_submission_bundle.py`

Machine guard that freezes expected benchmark values and submission inventory. Use as provenance/consistency support, not an independent scientific dataset.

## C. Interpretation of candidate value

Allowed:

- a measurable, valid candidate can have zero mechanism information under the current admissible region;
- values change after conditioning, so measurement order can matter;
- unresolved ambiguity may remain when the declared candidate vocabulary has no further positive-value observation;
- `non-estimable` is a legitimate output when candidate predictions do not define a valid stored-region partition.

Do not:

- label an external prior as validated `V(Q)` without a supported predictive partition;
- interpret low mechanism-information value as general scientific uselessness;
- call mechanism entropy a universal uncertainty metric across every dissertation chapter;
- claim the mechanism vocabulary is complete because the benchmark resolves declared confounds.

## D. TU-2 learning/licensing firewall

### D1 — `theory/TU2_LEARNING_LICENSING.md`

Supports:

- exact finite examples with the same `I(S;Q)` but opposite target-licensing status;
- maximal causal learning with zero target licensing;
- zero causal learning with complete target licensing;
- policy reversal between causal-learning and target-licensing objectives.

### D2 — `theory/verify_tu2.py`

Executable verification for the TU-2 family across `m=1..8`.

TU-2 prevents the Chapter 3 value function from becoming a universal observation-ranking score. MROD ranks for a declared mechanism-learning responsibility.

## E. Transition boundaries

### E1 — Chapter 2 → 3

Source: `thesis/transition_recovery_matrix.json`.

- EGWE warning failure and MROD observation selection are different estimands.
- MROD is not a rescue analysis of the six failed warning rules.
- no warning threshold, event label, or EGWE trajectory enters the G2 benchmark as a hidden source of favourable selection.

### E2 — Chapter 3 → 4

- MROD assumes a declared object of mechanism learning.
- Chapter 4 asks whether one eco-genetic summary can represent multiple target-dependent states.
- MROD does not prove the Chapter 4 state-separation result.

## F. Naming and provenance boundary

Historical protocol/store keys retain earlier RACH labels for frozen provenance, but the current publication-facing method is **Mechanism-Resolving Observation Design / information-guided sequential design**. Do not use historical implementation naming to merge current MROD and RACH programme identities.

RACH remains a companion programme in the dissertation architecture, not the owner of Chapter 3.

## Section-to-source matrix

| Draft section | Primary source | Frozen/formal support | Main boundary |
|---|---|---|---|
| 1. More data ≠ design | A1 | recovery registry | no universal measurement ranking |
| 2. Admissible region | A1 | — | declared model/constraint/tolerance only |
| 3. Residual ambiguity | A1 | — | entropy of declared mechanism vector only |
| 4. Observation value | A1 | information identity checks | requires verified candidate partition |
| 5. Sequential design | A1 | — | recompute after realised outcome |
| 6. Truth-peek-free benchmark | A1 | B1, B2 | controlled synthetic validation |
| 7. Budget-2 result | B1 | B3 | descriptive frozen contrast |
| 8. Budget-4 efficiency | B1 | B2, B3 | report absolute values with 83.5 ratio |
| 9. Truth retention | B1 | B2 | no misspecification guarantee |
| 10. Learning ≠ licensing | D1 | D2 | distinct scientific responsibilities |
| 11. Scope | A1 | recovery registry | no natural mechanism or universal optimality claim |
| 12. Transition | E2 | transition validator | question handoff, not implication |

## Drafting gate to v0.2

1. Verify bibliography metadata for ABC model choice, Bayesian/optimal experimental design, active learning, mutual information, and ecological value-of-information literature.
2. Decide whether the G2 budget-2 and budget-4 comparisons share one figure or separate panels.
3. Keep nuisance measurements visible because they operationalize the chapter's forbidden inference: valid/measurable candidates need not be equally valuable.
4. Preserve zero false exclusion as a guardrail rather than turning it into a guarantee under model misspecification.
5. Keep TU-2 as a type firewall; do not let target licensing compete with MROD's mechanism-learning objective inside one unlabeled score.
