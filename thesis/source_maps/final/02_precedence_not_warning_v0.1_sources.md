# Source map — Chapter 2 v0.1: 先行することは、警告することではない

This map supports `thesis/drafts/final/02_precedence_not_warning_v0.1.md` and is locked to the recovered EGWE warning-validity snapshot `7b2ca69b398d32071fd92d1da1d3b169c18a5d84` unless the verification-recovery registry is deliberately refreshed.

## Snapshot and chapter contract

- owning repository: `zuizui0223/eco-genetic-warning-extensions`
- recovered snapshot: `7b2ca69b398d32071fd92d1da1d3b169c18a5d84`
- verification class: `verified_full_denominator_empirical_model_audit`
- forbidden inference: `損失に先行した ⇒ 損失を予告する`
- chapter claim ceiling: the result rejects predictive-warning validity for the six frozen diversity-threshold rules in the two tested finite-model ensembles; it does not show that genetic diversity contains no predictive information generally.

## A. Primary warning-validity manuscript

### A1 — `manuscript/warning_validity.md`

Supports:

- distinction between event-conditioned ordering and predictive warning validity;
- frozen parent/fresh ensemble structure;
- six baseline-relative `H_alpha`/`H_gamma` thresholds at 5%, 10%, and 20%;
- inherited counts: 83 eligible, 35 losses, 48 horizon non-events;
- fresh counts: 82 eligible, 33 losses, 49 horizon non-events;
- event-conditioned leads `35/35` and `33/33` with zero ties/lags;
- non-event firings `48/48` and `49/49`;
- sensitivity 1, false-positive rate 1, specificity 0, binary-marker AUC 0.5;
- PPV equal to prevalence, 0.422 inherited and 0.402 fresh; NPV undefined because all eligible trajectories are marker-positive;
- secondary fixed ramp-end AUC ranges `0.500–0.538` inherited and `0.500–0.510` fresh;
- exact claim boundary and prohibition on post-result threshold rescue.

## B. Frozen provenance and reproducibility

### B1 — `REPRODUCIBILITY.md`

Supports the frozen warning-blind parent/fresh source architecture and the full-denominator paired reporting. It confirms that the warning-validity conclusion is derived from existing locked trajectories rather than endpoint, seed, or schedule retuning.

### B2 — warning-validity artifacts and source manifest

The source manuscript identifies:

- `artifacts/warning_validity/trajectory_endpoint_records.csv`
- `artifacts/warning_validity/source_manifest.json`
- `artifacts/prepublication_review/warning_validity_audit.json`
- `manuscript/tables/warning_validity_audit.csv`

The compact 1,200-row record table is source-manifest locked. The dissertation does not need to duplicate the artifact but must preserve the denominators.

### B3 — `scripts/validate_publication_lanes.py`

Machine guard for the paired warning denominators, specificity/AUC wording, and separation of warning-validity claims from state-validity and natural-data publication lanes.

## C. Source precondition: loss/event labels are imported, not created by chapter order

Source: `thesis/final_chapter_architecture.json` and `thesis/transition_recovery_matrix.json`.

Required statement:

> Warning event/non-event labels and loss endpoints are imported from the frozen EGWE/parent source contracts; Chapter 2 does not infer them from Chapter 4.

This permits Chapter 2 to appear before Chapter 4 editorially without turning the dissertation order into a scientific dependency inversion.

Do not:

- recalibrate the loss process from warning outcomes;
- derive event labels from the later eco-genetic chapter;
- interpret the chapter order as chronological provenance.

## D. TU-4 warning-state firewall

### D1 — `theory/TU4_WARNING_STATE_PORTABILITY.md`

Supports:

- `LossGeneratingState` and `WarningEvaluationState` as distinct typed objects;
- warning-evaluation quotient `Q_W` refines loss quotient `Q_L`;
- equality iff warning signature factors through the loss quotient;
- exact counterexample where identical loss state supports opposite warning ordering;
- within-state replication ≠ cross-state portability;
- portability requires a warning-law correspondence, not merely matching loss states.

TU-4 does not create the empirical full-denominator result. It prevents the weaker source claim “fix loss warning-blind” from being inflated to “loss state determines warning validity.”

## E. Statistical/interpretive boundary

Allowed:

- horizon-level binary discrimination because event/non-event status is known at the common administrative horizon;
- event-time non-events remain right-censored;
- event-conditioned lead counts and predictive metrics are different estimands;
- secondary fixed-time summaries remain secondary.

Not allowed:

- treating six endpoints within one trajectory as six independent biological replicates;
- inventing a common-time continuous score after the negative frozen-rule result;
- selecting a new threshold, seed subset, or transformation and calling it validation of the same frozen rule;
- converting `AUC=0.5` for these binary markers into “all genetic information is useless.”

## F. Transition boundaries

### F1 — Chapter 1 → 2

Identification and warning discrimination are orthogonal estimands. Failure to identify mechanism does not prove failure of prediction; predictive success would not identify mechanism.

### F2 — Chapter 2 → 3

MROD is not a rescue analysis of the failed EGWE thresholds. The transition is an editorial question handoff:

> after a frozen warning rule fails discrimination, what observation should be chosen next when several explanations remain compatible?

Chapter 3 owns a separate controlled observation-design benchmark.

## Section-to-source matrix

| Draft section | Primary source | Formal/validator support | Main boundary |
|---|---|---|---|
| 1. Lead ≠ warning | A1 | B3 | denominator/estimand distinction |
| 2. Warning-blind target | A1, B1 | C | source precondition, not Chapter 4 derivation |
| 3. Six frozen rules | A1 | B1, B3 | no retuning |
| 4. Event lead reproduction | A1 | B1 | event-conditioned protocol fact only |
| 5. Non-event denominator | A1 | B2, B3 | specificity/AUC interpretation limited to frozen rules |
| 6. Why event-only can mislead | A1 | — | conceptual generalization, not empirical universal law |
| 7. TU-4 | D1 | `theory/verify_tu4.py` | formal firewall, not source of empirical counts |
| 8. Secondary summaries | A1 | — | no post-result score rescue |
| 9. Scope | A1 | recovery registry | no “genetics never predicts” converse |
| 10. Transition | F2 | transition validator | question handoff, not rescue analysis |

## Drafting gate to v0.2

1. Verify bibliography metadata for early-warning evaluation, censoring, ROC/discrimination, and genetic-warning context against primary sources.
2. Decide whether the main dissertation figure should show the 2×2 horizon denominator table, the event/non-event flow, or both.
3. Keep the paired denominators visible in every summary of the headline result.
4. Preserve the distinction between source-frozen loss calibration and TU-4 warning-state sufficiency.
5. Any alternative warning statistic belongs to a separately declared development/validation programme and must not be introduced as a rescue of the six frozen rules.
