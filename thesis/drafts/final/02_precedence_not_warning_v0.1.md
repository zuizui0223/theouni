<!-- draft-id: chapter:2:v0.1 -->
# 先行することは、警告することではない

*English working title: Precedence Is Not Warning*

> **Draft status:** source-bounded v0.1 from merged EGWE snapshot `ef545bfa871c1a2b01daca1fc86e6db67f6e8c95`. Loss/event definitions are imported from warning-blind frozen source contracts. The chapter combines an exact finite-denominator theorem for binary horizon markers with the locked inherited/fresh warning audit; it does not derive the target event from Chapter 4 or generalize the result to every warning statistic.

## 1. The question is not whether false positives are possible

A statement such as “a precursor can occur before an event and still have false positives” is true but too weak to carry a chapter. It sounds like generic advice about classification. The scientifically useful question is sharper:

> **If a frozen binary marker precedes every observed event, what predictive quantities are mathematically forced by that success, and what quantities remain unconstrained?**

The forbidden inference motivating this chapter is

> **損失に先行した ⇒ 損失を予告する**

but the result of the chapter is not merely the negation of that implication. The result is an exact characterization of the information contained in perfect event-conditioned precedence.

Fix a common administrative horizon. Let `Y=1` indicate that the target event occurs by the horizon, and let `M=1` indicate that the frozen marker has fired by the horizon. Perfect event-conditioned precedence means that on every event trajectory the marker fires strictly before the event. Therefore every event trajectory is necessarily marker-positive by the common horizon. What remains open is the marker status of the non-event trajectories. [E0]

This distinction is the point at which a timing result becomes a denominator problem. Conditioning on event trajectories retains information about sensitivity, because every event contributes to the numerator and denominator of sensitivity. The same conditioning deletes the observations needed to determine specificity, because non-events have been removed from the calculation.

The chapter therefore asks exactly how large that deletion can be.

## 2. Theorem P1: perfect precedence fixes sensitivity and leaves specificity free

Let `n1>0` be the number of event trajectories and `n0>0` the number of horizon non-events. Let `f` be the number of non-events in which the marker also fires by the horizon.

Under perfect event-conditioned precedence all `n1` events satisfy `M=1`. There are no marker-negative events. Hence

\[
\boxed{\mathrm{sensitivity}=1.}
\]

This part is forced.

The event-conditioned statement, however, places no condition on the `n0` non-events. For any integer

\[
f\in\{0,1,\ldots,n_0\},
\]

we may keep the event trajectories unchanged and choose exactly `f` non-events to be marker-positive. The resulting specificity is

\[
\mathrm{specificity}=\frac{n_0-f}{n_0}.
\]

As `f` ranges from zero to `n0`, specificity ranges over the full finite grid

\[
\boxed{\left\{0,\frac1{n_0},\ldots,1\right\}}.
\]

Thus the exact result is:

> **Perfect event-conditioned precedence identifies sensitivity but does not identify specificity.** [E0]

This is stronger than saying that false positives “can occur.” The construction proves sharp freedom: every specificity value allowed by the finite denominator is compatible with exactly the same perfect event lead result.

The scientific consequence is that replication of event-conditioned precedence cannot, by itself, move us even one grid point toward knowing specificity. More event trajectories can make the event-conditioned timing result increasingly precise while leaving the missing non-event dimension structurally untouched.

## 3. Theorem P2: the same perfect precedence spans binary AUC from chance to perfect

For a binary score the ROC curve contains the points

\[
(0,0),\quad(\mathrm{FPR},\mathrm{TPR}),\quad(1,1).
\]

Its trapezoidal area is

\[
\frac12\mathrm{FPR}\,\mathrm{TPR}
+\frac12(1-\mathrm{FPR})(1+\mathrm{TPR})
=\frac12(1+\mathrm{TPR}-\mathrm{FPR}).
\]

Since `TPR=sensitivity` and `1-FPR=specificity`,

\[
\boxed{\mathrm{AUC}=\frac{\mathrm{sensitivity}+\mathrm{specificity}}2.}
\]

Substituting Theorem P1 gives, under perfect precedence,

\[
\boxed{\mathrm{AUC}=\frac{1+\mathrm{specificity}}2
=1-\frac{f}{2n_0}.}
\]

Therefore one and the same perfect event-conditioned result is compatible with binary AUC from `0.5` to `1` on the corresponding finite grid. [E0]

At one endpoint, no non-event fires (`f=0`): specificity is one and binary AUC is one. At the opposite endpoint, every non-event fires (`f=n0`): specificity is zero and binary AUC is `0.5`.

The latter case is particularly important because it is not a contradiction. A marker can precede every event and nevertheless be no better than chance at ranking an event trajectory above a non-event trajectory when the horizon marker is binary.

The theorem therefore replaces the vague phrase “precedence is not prediction” with a quantitative statement:

> **holding perfect precedence fixed, full-denominator discrimination can vary over its entire binary range.**

## 4. A third consequence: PPV is also absent from the event-only result

Under perfect precedence every event is marker-positive, so

\[
\mathrm{PPV}=\frac{n_1}{n_1+f}.
\]

The event-conditioned lead count does not determine `f`, and therefore does not determine PPV. When all non-events fire,

\[
\mathrm{PPV}=\frac{n_1}{n_1+n_0},
\]

which is exactly event prevalence. The marker then provides no horizon-level enrichment beyond knowing how common the event is. [E0]

This matters because an apparently impressive lead rate can coexist not only with poor specificity but also with a positive predictive value that is nothing more than base rate.

Again the issue is not that timing is scientifically irrelevant. Timing answers a real question. It simply answers a different question from prospective separation of event and non-event futures.

## 5. The loss target was frozen before the warning audit

These theorems are useful only if the target event itself is not adjusted in response to the warning behaviour. EGWE therefore separates loss-process definition from warning evaluation.

The inherited ensemble is tied to a pinned parent scientific state and frozen validation run. The fresh ensemble uses an independently seeded extension run. The six relative-diversity thresholds, deterioration schedule, eligibility rule, administrative horizon and functional-loss endpoint were not changed for the full-denominator audit. [E1]

This source precondition is important because Chapter 2 appears before Chapter 4 in the dissertation's editorial order. Chapter 2 does **not** obtain its loss labels from Chapter 4. The event and non-event classes are imported from source-frozen warning-blind contracts. [TR0]

The sequence is therefore:

1. define the target event independently of warning performance;
2. freeze the warning rules;
3. restore the entire baseline-eligible event/non-event denominator;
4. evaluate discrimination.

Loss calibration avoids circularity. It does not guarantee warning validity.

## 6. The locked EGWE result attains the theorem's sharp worst-discrimination endpoint

The empirical/computational audit uses six frozen rules: first post-baseline declines of 5%, 10% and 20% in either `H_alpha` or `H_gamma`.

In the inherited ensemble, 100 trajectories were attempted and 83 were baseline eligible. Of these, 35 reached realised functional-trait loss and 48 remained event-free through the common horizon. Every one of the six markers preceded every one of the 35 observed losses:

\[
35/35\quad\text{event leads.}
\]

The fresh ensemble independently retained 82 baseline-eligible trajectories: 33 events and 49 horizon non-events. Again all six rules preceded every observed loss:

\[
33/33\quad\text{event leads.}
\]

Thus the event-conditioned result genuinely replicated. It is not being dismissed as unstable or irreproducible. [E1]

The decisive result appears when the non-event denominator is restored. Every frozen marker also fired in every inherited non-event,

\[
48/48,
\]

and in every fresh non-event,

\[
49/49.
\]

Therefore `f=n0` in both source ensembles. Theorem P1 and P2 then force, for every rule,

\[
\mathrm{sensitivity}=1,
\qquad
\mathrm{specificity}=0,
\qquad
\mathrm{AUC}=0.5.
\]

PPV is exactly prevalence:

\[
35/83\approx0.422
\]

for the inherited ensemble and

\[
33/82\approx0.402
\]

for the fresh ensemble. [E1]

The locked result is therefore more informative than “we found false positives.” It realizes the theorem's **sharp minimum-discrimination endpoint compatible with perfect event sensitivity** in two separately audited ensembles.

## 7. Why the two source ensembles stay separate

The warning audit table also contains six `combined_descriptive` rows. These rows summarize the source ensembles together for description; they are not a third independently seeded experiment.

The theorem regression test initially exposed this distinction because a new test incorrectly assumed the publication table itself had 12 rows. It has 18: six inherited, six fresh and six combined descriptive. The corrected test explicitly filters the inherited and fresh source ensembles and verifies the theorem against those 12 source rows. [E2]

This is not bookkeeping trivia. Treating the pooled descriptive rows as a third replicate would inflate the evidence architecture. The chapter therefore keeps the paired denominators visible:

> **35/35 with 48/48; 33/33 with 49/49.**

The two full-denominator source results are replicated; their pooled re-expression is not additional replication.

## 8. TU-4: a loss-generating state need not be sufficient for warning evaluation

The full-denominator theorem concerns classification information. TU-4 addresses a different representation question.

Let a loss-response signature be `lambda` and a warning-response signature be `gamma`. The warning-evaluation signature retains their joint value. Its quotient therefore refines the loss quotient. The two quotients are equal exactly when warning behaviour factors through the loss quotient. [T4]

Thus even a correct loss-generating state is not automatically a sufficient state for evaluating warning. Worlds that are equivalent for loss can still differ in warning ordering or warning records.

This prevents a subtle replacement of one shortcut with another. Freezing loss warning-blind is necessary to avoid circularity, but it does not imply that the loss representation contains all information needed for warning validity.

TU-4 also separates within-domain warning replication from cross-domain portability. Warning transport requires a warning-law correspondence of its own.

## 9. Secondary summaries cannot retroactively redefine the tested rule

The audit retains fixed ramp-end summaries. Their AUC values remain close to chance: `0.500–0.538` in the inherited ensemble and `0.500–0.510` in the fresh ensemble. [E1]

These summaries do not rescue the frozen horizon rules. More importantly, the negative result does not license a post hoc search through alternative thresholds or transformed scores and then call the winner a validation of the original warning.

A genuinely new continuous or multivariate warning statistic is scientifically possible, but it is a different development programme. It needs its own target, training/selection rule, holdout structure and claim ceiling.

The fail-closed outcome here is therefore substantive: the tested rule is closed at the result actually obtained.

## 10. What the chapter establishes

The chapter establishes two levels of result.

**Exact finite-denominator result.** For a binary marker at a shared horizon, perfect event-conditioned precedence forces sensitivity one but leaves specificity unconstrained. The resulting binary AUC can range from chance to perfect while the event-conditioned lead result remains unchanged. [E0]

**Locked source result.** For the six frozen relative-diversity markers in the two tested finite-model ensembles, every event was led and every non-event also fired. The rules therefore attain specificity zero and binary AUC `0.5` in both source ensembles. [E1]

The chapter does **not** establish that genetic diversity never predicts ecological loss. It does not characterize continuous time-dependent ROC curves, competing-risk scores or every early-warning statistic. It does not infer a causal mechanism for diversity decline. It does not authorize post-result threshold optimization. [E3]

The precise conclusion is:

> **Perfect precedence answers an event-conditioned timing question. Predictive warning requires the missing non-event denominator; in the locked EGWE case, restoring that denominator places all six rules at the sharp chance-discrimination endpoint.**

## 11. Transition: warning validity does not tell us which observation to collect next

Once the frozen warning shortcut is closed, a practical problem remains. If several mechanism explanations remain compatible, which future measurement should be collected?

Nothing in Theorem P1 or P2 ranks candidate observations for mechanism learning. Conversely, an observation-design method cannot rescue the six failed warning rules simply by ranking another measurement highly. The scientific objects differ. [TR1]

Chapter 3 therefore asks a new question:

> **When does adapting the identity of the next measurement to the result of the first measurement produce strictly more information than any precommitted second measurement?**

That question is owned by MROD and answered by a separate necessary-and-sufficient condition.

## Internal source keys

- **[E0]** EGWE `docs/PRECEDENCE_DISCRIMINATION_THEOREM_2026-09-03.md` and `tests/test_precedence_discrimination_theorem.py` — P1/P2/P3, specificity construction, binary-AUC oracle, locked-table application.
- **[E1]** EGWE `manuscript/warning_validity.md` and `REPRODUCIBILITY.md` — frozen source architecture, 35/48 and 33/49 denominators, metrics, secondary summaries and claim boundary.
- **[E2]** EGWE theorem regression recovery — inherited/fresh source rows are verified separately; `combined_descriptive` rows are not a third replicate ensemble.
- **[E3]** `thesis/verification_recovery_registry.json`, Chapter 2 claim ceiling.
- **[T4]** `theory/TU4_WARNING_STATE_PORTABILITY.md` and `theory/verify_tu4.py` — loss-state versus warning-state factorization and portability firewall.
- **[TR0]** `thesis/final_chapter_architecture.json` — frozen event labels are source preconditions, not derived from Chapter 4.
- **[TR1]** `thesis/transition_recovery_matrix.json` — Chapter 2→3 is an editorial question handoff, not a rescue implication.
