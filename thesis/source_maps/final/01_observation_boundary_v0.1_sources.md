# Source map — Chapter 1 v0.1: 観測が原理的に届かない範囲

This map supports `thesis/drafts/final/01_observation_boundary_v0.1.md` and is locked to Boundary snapshot `d950cf9fe4d21d4677f1e16f29e8fbe3c7af8f84` unless the verification-recovery registry is deliberately refreshed.

## Snapshot and chapter contract

- owning repository: `zuizui0223/boundary`
- recovered snapshot: `d950cf9fe4d21d4677f1e16f29e8fbe3c7af8f84`
- verification class: `verified_exact_analytic_and_executable`
- forbidden inference: `観測を豊かにした ⇒ 潜在機構に近づいた`
- chapter claim ceiling: identification under a declared multiplicative/channel model and calibration assumptions; no generic claim that richer biological measurements approach the true mechanism in nature.

## A. Primary manuscript source

### A1 — `paper/manuscript.md`

Supports the complete chapter narrative:

- biological proximity and identification strength are distinct axes;
- positive multiplicative observation model;
- Theorem N1 two-channel product invariance;
- Theorem N1-k: `k-1` endpoint-only dimensions and `k-1-r` after `r` direct anchors;
- joint-measurement bottleneck in ecological chains;
- proxy calibration transport family;
- sharp joint identified set;
- reference-invariant breakdown factor;
- channel-anchor versus calibration-anchor design ladder;
- explicit discussion limits.

The dissertation may condense and reorder this material, but must not strengthen the source claim.

## B. Executable proof obligations

### B1 — `tests/test_identification_obligations.py`

Supports:

- fail-closed anchor-count boundary;
- reciprocal-reference invariance of breakdown factor across a range of ratios;
- proof-obligation coverage added for the Paper A strengthening pass.

### B2 — `tests/test_boundary_core.py`

Supports:

- concrete residual-dimension checks such as five channels with two anchors → residual dimension two and four anchors → zero;
- `log_gauge_basis(k)` dimension `k-1`;
- calibration family and breakdown reference invariance.

The tests certify implementation consistency for the declared finite/analytic objects; they do not empirically validate the ecological factorization.

## C. Joint-measurement bottleneck

The Chapter 1 introduction uses the source's field-design bottleneck as an ecological bridge from algebra to measurement design.

Allowed claim:

> a data-rich system can still be mechanism-nonidentifying if effective service, reproductive dependency or another distinguishing channel is absent from the same inferential chain.

Required output when the declared alternatives cannot be separated:

> `not evaluable` / bounded identified set, rather than post-hoc mechanism assignment from a nearby proxy.

Do not convert this into a claim that any particular field dataset in the dissertation has such a bottleneck unless that dataset's own measurement contract is opened.

## D. Exact equations authorized for the chapter

### D1 — positive `k`-stage product

`W=prod_j F_j`, with positive channels and product-preserving log perturbations summing to zero.

Authorized conclusion:

`residual dimension = k - 1 - r`, for `0 <= r <= k-1` independent channel anchors.

### D2 — proxy calibration transport

For `W_i=F_iE_i`, `X_i=q_iF_i`, `kappa=q_1/q_0`:

- `rho_F=rho_X/kappa`
- `rho_E=(rho_W/rho_X)kappa`
- symmetric bound `1/Gamma <= kappa <= Gamma`
- sharp joint set `J_Gamma`
- `Gamma=1` point identification; finite `Gamma>1` partial identification; unrestricted transport non-identification.

### D3 — breakdown factor

`Gamma*=max(rho_hat,1/rho_hat)` and `eta*=|log rho_hat|`.

Authorized interpretation: sensitivity threshold for calibration transport, not an estimate of actual calibration drift.

## E. Literature boundary

Boundary positions the algebra inside established structural-identifiability and partial-identification traditions. The dissertation should retain this priority firewall. It may claim an ecological/evidentiary synthesis and field-design consequence, but not invention of identifiability algebra, ratios, or quotient reasoning.

Before citation-ready status, verify the source manuscript's bibliographic metadata against primary publications rather than copying references blindly.

## F. Transition boundary to Chapter 2

Source: `thesis/transition_recovery_matrix.json`.

The transition is an `editorial_question_handoff`:

- Chapter 1 closes the shortcut that biological proximity/precision certifies mechanism identification.
- Chapter 2 asks whether a signal can discriminate future loss.
- mechanism identification and warning discrimination are orthogonal estimands.

Forbidden bridge:

> Do not infer that failure of mechanism identification implies failure of prediction, or that predictive success would identify mechanism.

## Section-to-source matrix

| Draft section | Primary source | Executable support | Claim ceiling |
|---|---|---|---|
| 1. Two axes | A1 intro | — | no ranking of molecular vs field evidence in general |
| 2. Endpoint equivalence | A1 N1/N1-k | B1, B2 | declared positive product only |
| 3. Channel anchors | A1 N1-k | B1, B2 | independent anchors only |
| 4. Joint bottleneck | A1 intro | — | design principle, not new empirical result |
| 5. Proxy transport | A1 T1 | B2 | Gamma externally declared or sensitivity parameter |
| 6. Breakdown | A1 §6 | B1, B2 | sensitivity threshold, not truth of calibration |
| 7. Two anchor ladders | A1 §7 | — | channel and calibration anchors remain distinct |
| 8. Scope | A1 Discussion | recovery registry | no universal natural mechanism claim |
| 9. Transition | transition recovery matrix | transition validator | question handoff, not implication |

## Drafting gate to v0.2

1. Add verified citations for the structural-identifiability, partial-identification, pollination effectiveness and seed-dispersal quantity/quality literature.
2. Decide whether the worked `Gamma*=1.34` example belongs in main dissertation text or a boxed sidebar.
3. Keep the joint identified set visual if a Boundary figure is reused; do not replace it with independent marginal intervals.
4. Preserve `not evaluable` as an admissible scientific outcome in any field-design example.
5. Do not introduce a new natural-system application inside this chapter without a separate empirical admission contract.
