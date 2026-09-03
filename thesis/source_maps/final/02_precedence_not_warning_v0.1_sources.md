# Source map — Chapter 2 v0.1: 先行することは、警告することではない

This map supports `thesis/drafts/final/02_precedence_not_warning_v0.1.md` and is locked to merged EGWE snapshot `ef545bfa871c1a2b01daca1fc86e6db67f6e8c95`.

## Snapshot and chapter contract

- owning repository: `zuizui0223/eco-genetic-warning-extensions`
- current theorem snapshot: `ef545bfa871c1a2b01daca1fc86e6db67f6e8c95`
- verification class: `verified_exact_denominator_theorem_plus_locked_full_denominator_audit`
- forbidden inference: `損失に先行した ⇒ 損失を予告する`
- chapter claim ceiling: the exact theorem concerns binary markers at a common administrative horizon, while the locked empirical conclusion rejects predictive-warning validity only for the six frozen diversity-threshold rules in the two tested finite-model ensembles; neither result says that genetic diversity contains no predictive information generally.

## A. Headline theorem: what perfect precedence actually determines

### A1 — `docs/PRECEDENCE_DISCRIMINATION_THEOREM_2026-09-03.md`

Fix event status `Y` and a binary marker `M` at a common horizon. If the marker strictly precedes every observed event, then every event is marker-positive by the horizon.

The theorem proves:

1. perfect event-conditioned precedence forces `sensitivity = 1`;
2. precedence imposes **no restriction** on marker firing among non-events;
3. with `n0` non-events, every specificity value on `{0, 1/n0, ..., 1}` is compatible with the same perfect event lead result;
4. for a binary marker,
   `AUC = (sensitivity + specificity)/2`, hence under perfect precedence `AUC = (1 + specificity)/2`;
5. the same perfect event precedence can therefore coexist with binary AUC from `0.5` to `1`;
6. if every non-event also fires, specificity is zero, AUC is `0.5`, and PPV equals event prevalence.

This is the non-obvious result. The chapter is not merely advising readers to “remember false positives”; it identifies exactly what an event-conditioned lead result determines and exactly which predictive dimensions it deletes.

## B. Proof and independent oracle

### B1 — written proof

The proof has two parts:

- P1 constructs arbitrary non-event firing count `f` while keeping all event trajectories unchanged, proving the specificity grid is free under fixed perfect precedence;
- P2 derives the binary-score ROC area by trapezoidal integration and obtains `AUC=(sensitivity+specificity)/2`.

### B2 — `tests/test_precedence_discrimination_theorem.py`

The executable obligations verify:

- every finite specificity grid point under perfect event sensitivity;
- the binary-AUC identity against an independent pairwise-ranking oracle;
- the full `0.5..1` AUC range while event precedence remains fixed;
- the `f=n0` sharp endpoint;
- direct parsing of the locked warning table after filtering the two source ensembles, without treating the six `combined_descriptive` rows as a third replicate ensemble.

The final point is deliberate: inherited and fresh ensembles remain separate evidence sources. Their pooled descriptive rows do not create an additional replication denominator.

## C. Locked EGWE evidence attains the sharp endpoint

### C1 — `manuscript/warning_validity.md`

Six frozen baseline-relative rules are audited separately in two ensembles.

Inherited ensemble:

- baseline eligible: `83`
- events: `35`
- non-events: `48`
- event leads: `35/35`
- non-event firings: `48/48`

Fresh ensemble:

- baseline eligible: `82`
- events: `33`
- non-events: `49`
- event leads: `33/33`
- non-event firings: `49/49`

For every frozen rule in both source ensembles:

- sensitivity `1`
- specificity `0`
- false-positive rate `1`
- binary-marker AUC `0.5`
- PPV equal to event prevalence (`35/83≈0.422`, `33/82≈0.402`).

The empirical result therefore lands at the theorem's **sharp minimum-discrimination endpoint compatible with perfect event sensitivity**.

## D. Frozen provenance and no-rescue boundary

### D1 — `REPRODUCIBILITY.md`

Supports the warning-blind event definition, independent inherited/fresh source architecture, frozen thresholds, common horizon, and absence of post-result endpoint/seed retuning.

### D2 — publication lane guards

The warning-validity manuscript is the sole active owner of this denominator result. State-validity and natural-data lanes do not supply alternative warning endpoints.

A negative result does not authorize a threshold search inside the same claim. A new warning statistic would require a separately declared development and validation programme.

## E. Source precondition: Chapter 2 does not derive loss from Chapter 4

Warning event/non-event labels and loss endpoints are imported from frozen source contracts. The dissertation's editorial order does not create a scientific dependency in which Chapter 4 must generate Chapter 2's target.

Do not:

- recalibrate loss from warning behaviour;
- derive event labels from the later state-separation chapter;
- treat chapter order as provenance order.

## F. TU-4 warning-state firewall

### F1 — `theory/TU4_WARNING_STATE_PORTABILITY.md`

TU-4 establishes a separate representation condition:

- `WarningEvaluationState` refines `LossGeneratingState`;
- the two are equal exactly when the warning signature factors through the loss quotient;
- warning portability requires its own correspondence condition.

TU-4 does not generate the 35/48 or 33/49 empirical denominators. It prevents a fixed loss representation from being mistaken for a sufficient warning-evaluation representation.

## G. Statistical boundary

Allowed:

- binary horizon discrimination because event/non-event status is known at the common administrative horizon;
- right-censoring remains relevant for event-time questions;
- event-conditioned timing and predictive discrimination are different estimands.

Not allowed:

- treating six endpoints within one trajectory as independent biological replicates;
- generalizing the binary-marker AUC theorem to arbitrary continuous time-dependent ROC objects;
- using `AUC=0.5` here to claim all genetic information is useless.

## H. Transition boundaries

### H1 — Chapter 1 → 2

Mechanism identification and warning discrimination are different estimands. The Boundary rank theorem does not predict warning performance.

### H2 — Chapter 2 → 3

MROD does not rescue the six failed thresholds. The transition asks a new question: when several explanations remain compatible, under what condition is adaptive next-measurement choice actually better than fixed ordering?

## Section-to-source matrix

| Draft section | Primary source | Proof/verification | Main boundary |
|---|---|---|---|
| 1. Lead ≠ warning | A1 | B1/B2 | theorem replaces slogan |
| 2. Exact denominator condition | A1 | B1/B2 | binary common-horizon marker only |
| 3. Frozen target/rules | C1/D1 | provenance guards | no retuning |
| 4. Event lead reproduction | C1 | locked table test | event-conditioned fact |
| 5. Non-event denominator | C1 | theorem application | sharp AUC 0.5 endpoint |
| 6. Why conditioning loses information | A1 | specificity construction | no universal continuous-score claim |
| 7. TU-4 | F1 | `theory/verify_tu4.py` | representation firewall |
| 8. Secondary summaries | C1 | — | no post-result rescue |
| 9. Scope | A1/C1 | recovery registry | no “genetics never predicts” converse |
| 10. Transition | H2 | transition validator | question handoff, not rescue |

## Drafting gate

1. Put Theorems P1–P2 before the empirical counts so the chapter answers “what follows exactly?” before showing the endpoint case.
2. Keep `35/35 ↔ 48/48` and `33/33 ↔ 49/49` visibly paired.
3. Keep inherited and fresh ensembles separate; `combined_descriptive` is not a third replication ensemble.
4. Preserve TU-4 as a different theorem layer from the full-denominator audit.
5. Do not introduce a new warning score as a rescue of the six frozen rules.
