# Source map — Chapter 3 v0.1: 境界の内側で、次に何を測るか

This map supports `thesis/drafts/final/03_next_measurement_v0.1.md` and is locked to merged MROD snapshot `689ba17d14fec2218e9e96f4c9e432eb8b71fb58`.

## Snapshot and chapter contract

- owning repository: `zuizui0223/mrod`
- current theorem snapshot: `689ba17d14fec2218e9e96f4c9e432eb8b71fb58`
- verification class: `verified_adaptive_iff_plus_controlled_truth_peek_free_benchmark`
- forbidden inference: `測れるものは測る価値がある ⇒ 測る順序に良し悪しはない`
- chapter claim ceiling: the adaptive theorem is exact for a finite two-step design with a fixed first observation and finite candidate set; the G2 result validates one declared information-guided policy on a controlled synthetic family. Neither result proves global multi-step optimality or a natural-system causal mechanism.

## A. Headline theorem: when recomputation has strict value

### A1 — `docs/adaptive_recomputation_theorem_2026-09-03.md`

Let `X` be the realised outcome of a fixed first observation and let `U_q(x)=I(S;Q_q|X=x)` be the second-step mechanism-information value of remaining candidate `q` in branch `x`.

Define

- adaptive value: `V_adapt = E[max_q U_q(X)]`;
- best static value: `V_static = max_q E[U_q(X)]`.

The theorem proves:

1. `V_adapt >= V_static` for every finite design of this form;
2. equality holds **if and only if** at least one candidate is branchwise optimal on every positive-probability first-outcome branch;
3. strict adaptive advantage holds **if and only if** the intersection of positive-branch argmax sets is empty;
4. different unique best candidates in two positive-probability branches are sufficient for strict advantage;
5. if one candidate is common-best everywhere, recomputation cannot improve expected second-step value over precommitting that candidate.

This is the chapter's anti-obviousness result. “Recompute after each observation” is no longer an algorithmic instruction masquerading as a contribution; the theorem says exactly when the recomputation changes achievable expected value.

## B. Proof, sharpness, and minimal witness

### B1 — written proof

The lower bound follows pointwise from `max_j U_j(x) >= U_q(x)` and expectation. The iff equality condition follows by taking a best static candidate `q*`, defining the nonnegative branchwise gap `D(x)=max_q U_q(x)-U_q*(x)`, and using `E[D]=0` iff `D=0` on every positive-probability branch.

### B2 — four-world sharp witness

Four equally likely mechanism states are split by the first observation into two two-state branches. `Q1` resolves only the first branch; `Q2` resolves only the second.

Then:

- branch 0: `(Q1,Q2) = (1,0)` bit;
- branch 1: `(Q1,Q2) = (0,1)` bit;
- adaptive second-step value = `1.0` bit;
- best static second candidate = `0.5` bit.

The source also proves minimality within this deterministic branch-switch class: strict branch switching requires at least two positive-probability branches with at least two compatible states each, hence at least four states.

### B3 — `tests/test_adaptive_recomputation_theorem.py`

Executable obligations cover:

- exhaustive small utility tables;
- `V_adapt >= V_static`;
- the common-argmax iff condition;
- strict rank-reversal cases;
- equality cases with a common tied optimum;
- the four-world mutual-information witness;
- exhaustive exclusion of an equivalent three-world branch-switch witness.

## C. MROD information value and fail-closed candidate contract

### C1 — `docs/mainline.md` and `paper/manuscript.md`

MROD retains an admissible mechanism region `A_epsilon` and, for verified candidate outcome partitions, uses

`V(Q)=I(S;Q|A_epsilon)/K`.

The candidate partition must be mutually exclusive and exhaustive over the current admissible region. A candidate whose predictive partition is unavailable is non-estimable for the validated value; an external prior is not silently relabelled as stored-region information value.

Sequential design then conditions on the realised outcome and recomputes all remaining values.

The theorem in A1 does not depend on the historical project name. It is a condition on the branchwise values of the publication-facing Mechanism-Resolving Observation Design.

## D. Frozen G2 controlled validation

### D1 — `paper/results/g2_frozen_v2_summary.json`

The frozen truth-peek-free challenge remains empirical/computational validation of the policy, not proof of A1–A2.

Budget 2:

- guided edge resolution `1.000` vs random `0.6045`;
- guided convergence `0.990` vs random `0.435`;
- guided nuisance selections `0.001` vs random `0.974`;
- hidden-truth false exclusion `0` in both policies.

Budget 4:

- both reach mean edge resolution `1.000`;
- guided observations `1.518` vs random `2.673`;
- guided nuisance selections `0.014` vs random `1.169`;
- descriptive nuisance ratio `83.5-fold`; report absolute values with the ratio.

G2's comparator is random order. The adaptive theorem is deliberately stronger because its comparator is the **best precommitted static second measurement**.

## E. CI recovery and Figure 1 contract

The theorem PR initially exposed a stale test importing the retired `causal_model.confound_demo`. The scientific submission-boundary checks had already passed. The fix did not restore retired code: the test was migrated to the current canonical `controlled_confounding_demo` / information-value implementation. Python 3.10, 3.11 and 3.12 then passed.

This matters for provenance because the chapter should not cite a retired heuristic implementation as proof of current observation value.

## F. TU-2 learning/licensing firewall

### F1 — `theory/TU2_LEARNING_LICENSING.md`

TU-2 proves that mechanism-learning information and target licensing can vary independently. It prevents the MROD value function from becoming a universal observation score.

The adaptive theorem therefore means:

> adaptive recomputation can strictly improve the declared **mechanism-learning** objective under its iff branch condition.

It does not mean:

> adaptive MROD is universally the best observation policy for every scientific target.

## G. Transition boundaries

### G1 — Chapter 2 → 3

EGWE supplies no candidate ranking theorem and MROD is not a rescue of failed warning thresholds. The handoff is from a failed warning shortcut to a separate observation-design question.

### G2 — Chapter 3 → 4

MROD requires the object of learning to be declared. Chapter 4 asks whether several target responsibilities even admit one common scalar state. The adaptive theorem does not prove state scalarizability or non-scalarizability.

## Section-to-source matrix

| Draft section | Primary source | Proof/verification | Main boundary |
|---|---|---|---|
| 1. Measurement order problem | C1 | recovery registry | no universal ranking |
| 2. Admissible mechanism region | C1 | source tests | declared model family only |
| 3. Current observation value | C1 | canonical information implementation | verified partition required |
| 4. Adaptive iff theorem | A1 | B1/B3 | fixed-first, two-step finite design |
| 5. Sharp witness | B2 | B3 | deterministic branch-switch class |
| 6. Sequential design | C1 | source implementation | greedy global optimality not claimed |
| 7–8. G2 | D1 | submission bundle | controlled synthetic benchmark |
| 9. Truth retention | D1 | frozen summary | no misspecification guarantee |
| 10. Learning ≠ licensing | F1 | `theory/verify_tu2.py` | target-specific responsibility |
| 11. Scope | A1/C1/D1 | recovery registry | no natural mechanism claim |
| 12. Transition | G2 | transition validator | question handoff |

## Drafting gate

1. Put the adaptive iff theorem before the G2 random-order benchmark.
2. Make the best-static comparator explicit; do not sell “beats random” as the theorem.
3. Keep the four-world witness because it demonstrates strict value, and keep the three-world lower-bound argument because it establishes minimality in the declared class.
4. Preserve G2 as an independent controlled validation layer, not the proof of adaptive advantage.
5. Preserve TU-2 so mechanism-learning value is never relabelled as universal scientific utility.
