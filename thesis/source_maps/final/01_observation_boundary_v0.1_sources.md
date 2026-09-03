# Source map — Chapter 1 v0.1: 観測が原理的に届かない範囲

This map supports `thesis/drafts/final/01_observation_boundary_v0.1.md`. The original dissertation draft was written from Boundary snapshot `d950cf9fe4d21d4677f1e16f29e8fbe3c7af8f84`; the theorem-level identification condition is now refreshed to merged Boundary snapshot `2919842f19bdd93221363b9f39f2ba1ebb146d17`.

## Snapshot and chapter contract

- owning repository: `zuizui0223/boundary`
- current theorem snapshot: `2919842f19bdd93221363b9f39f2ba1ebb146d17`
- original prose-base snapshot: `d950cf9fe4d21d4677f1e16f29e8fbe3c7af8f84`
- verification class: `verified_exact_rank_condition_and_executable_oracle`
- forbidden inference: `観測を豊かにした ⇒ 潜在機構に近づいた`
- chapter claim ceiling: exact identification statements are conditional on the declared positive multiplicative/log-linear observation class. They do not establish that biological proximity, dimensionality, or measurement precision generally approaches the true mechanism in nature.

## A. Headline theorem: when a new observation changes identification

### A1 — `docs/observation_rank_identification_theorem_2026-09-03.md`

Let positive latent channels be represented in log coordinates by `x in R^k`. Let the current exact observation map be

`M x = y`.

For a compatible observation record, the theorem proves:

1. the compatible mechanism set is an affine translate of `ker(M)`;
2. therefore its structural dimension is exactly `k-rank(M)`;
3. point identification holds exactly when `rank(M)=k`;
4. adding one scalar observation with row `a` reduces structural ambiguity **if and only if** `a` lies outside the current row span of `M`;
5. because a single row can increase rank by at most one, every useful scalar observation reduces the residual dimension by exactly one.

### Proof logic

Rank-nullity gives `dim ker(M)=k-rank(M)`. Appending `a` changes the compatible-set dimension only through `rank([M;a])`. The appended rank rises by one exactly when `a` is not already in `rowspan(M)`. This gives both necessity and sufficiency.

### Immediate corollaries

- exact repetition of an existing observation does not improve structural identification;
- rescaling an existing row does not improve structural identification;
- any new observation that is a linear combination of existing rows does not improve structural identification;
- improving numerical precision without changing the observation operator can reduce statistical uncertainty but cannot change this structural rank;
- a biologically less proximal measurement can be more identifying if it supplies a missing independent observation direction.

These are no longer rhetorical claims. They are consequences of the iff rank condition.

## B. `k-1-r` is now a proved special case, not the main theorem

### B1 — product endpoint plus channel anchors

For a `k`-channel positive product

`W = prod_j F_j`,

the log endpoint is the row `(1,...,1)`. Direct measurement of `r` distinct channels supplies `r` coordinate rows. These `r+1` rows are independent for `0<=r<=k-1`, so the general rank theorem gives

`residual dimension = k-(r+1)=k-1-r`.

Thus the older channel-anchor rule is recovered as a corollary of the general observation-design condition.

The important scientific upgrade is that **anchor count alone is not the criterion**. Independence relative to the current observation span is the criterion. Two biologically different measurements can still be structurally redundant; one strategically chosen measurement can remove exactly one unresolved dimension.

## C. Executable verification and independent oracle

### C1 — `tests/test_observation_rank_theorem.py`

The source tests verify:

- exact rational-valued rank calculations;
- `k-rank(M)` residual dimensions;
- point identification iff full rank;
- dependent versus independent candidate observations;
- duplicate/rescaled/linear-combination rows with zero structural gain;
- exhaustive coordinate-anchor recovery of `k-1-r`;
- agreement with an independent determinant/minor rank oracle over small integer matrices.

The executable layer verifies proof obligations; it does not substitute for the written proof and it does not empirically validate the ecological factorization.

## D. Primary ecological manuscript and field bottleneck

### D1 — `paper/manuscript.md`

The manuscript remains the source for:

- biological proximity versus identification strength;
- positive multiplicative ecological chains;
- the joint-measurement bottleneck;
- proxy calibration transport;
- sharp identified sets and breakdown factors;
- channel-anchor versus calibration-anchor design.

The joint-measurement bottleneck supplies the ecological interpretation of the rank theorem. A field programme may contain many measurements yet lack an independent row that separates the declared mechanisms. More records along already observed directions cannot replace the missing identifying direction.

Allowed output when the alternatives remain inseparable is `not evaluable` or an identified set—not post-hoc assignment from a nearby proxy.

## E. Calibration transport remains a second identification problem

For `W_i=F_iE_i`, `X_i=q_iF_i`, `kappa=q_1/q_0`, Boundary gives

- `rho_F=rho_X/kappa`;
- `rho_E=(rho_W/rho_X)kappa`;
- symmetric sensitivity bound `1/Gamma <= kappa <= Gamma`;
- a sharp coupled joint identified set;
- `Gamma=1` point identification, finite `Gamma>1` partial identification, unrestricted transport non-identification;
- reference-invariant breakdown factor `Gamma*=max(rho_hat,1/rho_hat)`.

The rank theorem does not replace this calibration result. Rank addresses whether declared exact observation directions separate log channels; calibration transport addresses uncertainty in the mapping from a proxy to a channel across regimes.

## F. Claim hierarchy for dissertation prose

Use this order in Chapter 1:

1. **Question:** when does another measurement actually improve mechanism identification?
2. **Necessary-and-sufficient condition:** iff it increases observation rank.
3. **Consequence:** repeated/precise but rank-redundant measurement cannot change structural identification.
4. **Special case:** product endpoint plus `r` independent channel anchors gives `k-1-r`.
5. **Field implication:** measure the missing independent direction, not merely more variables.
6. **Second boundary:** proxy transport can still leave partial identification even after a channel direction is observed.

Do **not** lead with `k-1-r` as though the contribution were merely counting factors in a product.

## G. Transition boundary to Chapter 2

Source: `thesis/transition_recovery_matrix.json`.

The Chapter 1→2 relation remains an editorial question handoff:

- Chapter 1 identifies exactly when an observation map gains mechanism-separating power.
- Chapter 2 asks whether a signal discriminates future loss.
- mechanism identification and warning discrimination are orthogonal estimands.

Forbidden bridge:

> Do not infer that failure of mechanism identification implies failure of prediction, or that predictive success identifies mechanism.

## Section-to-source matrix

| Draft section | Primary source | Proof/verification | Main boundary |
|---|---|---|---|
| 1. Mechanistic proximity vs identification | D1 | recovery registry | no generic molecular/field ranking |
| 2. General rank condition | A1 | C1 | declared exact log-linear observation class |
| 3. Product/channel corollary | B1 | C1 | `k-1-r` only when anchor rows are independent |
| 4. Joint-measurement bottleneck | D1 | — | field-design implication, not empirical dataset claim |
| 5. Calibration transport | E | source calibration tests | external/sensitivity bound required |
| 6. Breakdown factor | E | source tests | breakpoint, not estimate of actual drift |
| 7. Anchor distinctions | D1/E | source implementation | channel vs calibration information kept separate |
| 8. Scope | A–E | recovery registry | no universal natural mechanism claim |
| 9. Transition | G | transition validator | question handoff, not prediction theorem |

## Drafting gate

Before Chapter 1 is promoted beyond the current v0.1 prose:

1. rewrite the headline and Section 3 around the rank iff theorem;
2. present `k-1-r` only as a product/coordinate-anchor corollary;
3. retain the calibration-transport family as a distinct second boundary;
4. preserve `not evaluable` as a valid field-design outcome;
5. verify structural-identifiability and partial-identification citations against primary sources.
