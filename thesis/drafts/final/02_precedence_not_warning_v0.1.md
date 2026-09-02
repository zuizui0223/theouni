<!-- draft-id: chapter:2:v0.1 -->
# 先行することは、警告することではない

*English working title: Precedence Is Not Warning*

> **Draft status:** source-bounded v0.1 from EGWE snapshot `7b2ca69b398d32071fd92d1da1d3b169c18a5d84`. Loss/event definitions are imported from the source-frozen warning-blind contracts; this chapter does not derive them from Chapter 4. The chapter evaluates predictive warning validity for six frozen rules in two tested finite-model ensembles.

## 1. A perfect lead count can still be a useless warning

Early-warning analysis contains an unusually seductive shortcut. If a signal repeatedly appears before an undesirable event, it is natural to call the signal a warning. The temporal statement may be perfectly correct. The predictive conclusion can still fail.

The forbidden inference of this chapter is:

> **損失に先行した ⇒ 損失を予告する**

The distinction is a denominator problem. Event-conditioned ordering asks whether the signal occurs before the event among trajectories in which the relevant signal and event are both observed. Predictive warning validity asks a different question: does the signal distinguish trajectories that reach the event from trajectories that remain event-free through a common evaluation horizon? [E1]

A rule can therefore achieve perfect temporal precedence among events while firing just as reliably in non-events. In that case the statement “the signal comes first” is reproducible, but the statement “the signal warns which units will fail” is unsupported.

This chapter uses a deliberately severe case. Six pre-existing baseline-relative genetic-diversity rules were frozen before the predictive audit. In two independently seeded finite-model ensembles, every rule preceded every observed realized functional-trait loss. Yet every rule also fired in every baseline-eligible non-event trajectory by the same horizon. [E1]

The result is useful precisely because no subtle statistical interpretation is required. Event-conditioned temporal ordering succeeds maximally while horizon-level discrimination fails maximally.

## 2. The loss process must be fixed before warning is evaluated

Warning analysis is not meaningful without a declared target event. A threshold can appear early only relative to something that counts as the event, and the event definition itself can become circular if it is tuned after warning behaviour is inspected.

The EGWE warning-validity lane therefore inherits a warning-blind loss process and fixed eligibility/horizon contracts from the source programme. The inherited ensemble comes from the pinned parent scientific commit and its frozen validation run. The fresh ensemble comes from an independently seeded extension run. No threshold, seed, deterioration schedule, eligibility rule or loss endpoint was changed for the full-denominator warning audit. [E2]

This source precondition matters for the dissertation's chapter order. Chapter 2 appears before the later eco-genetic state-separation chapter for editorial reasons. It does not infer its loss labels from that later chapter. The event/non-event labels used here are imported from the already frozen EGWE/parent contracts. [TR0]

The rule is methodological rather than chronological:

> **Fix the target event without warning outcomes, then evaluate the warning against the full eligible denominator.**

Loss calibration is therefore necessary for a non-circular warning test. It is not sufficient for warning validity. Once the loss domain is fixed, the signal still has to discriminate.

## 3. Six frozen genetic-diversity rules

The warning rules were based on baseline-relative declines in two diversity quantities, \(H_\alpha\) and \(H_\gamma\). For each quantity, the first post-baseline generation reaching a 5%, 10% or 20% relative decline defined a threshold-crossing time. This yielded six frozen endpoints. [E1]

The historical replication decision concerned ordering among valid warning/loss pairs. If a threshold crossed before the loss in all valid pairs, the event-conditioned ordering was classified as reproduced. That historical protocol did not claim to be a predictive classifier over event and non-event trajectories.

The full-denominator audit asks the missing predictive question. For every baseline-eligible trajectory, it records two horizon-level facts:

1. did the frozen warning rule fire by the common horizon?
2. did realized functional-trait loss occur by that horizon?

These two binary outcomes support sensitivity, false-positive rate, specificity, positive predictive value, negative predictive value and binary-marker AUC. Non-events remain right-censored for event-time analysis, but they are legitimate event-free controls at the common administrative horizon. [E1]

The distinction between event-time censoring and horizon-level classification is crucial. A non-event trajectory does not tell us when loss would have occurred after the horizon. It does tell us that a useful horizon-level warning rule should not indiscriminately fire in every such trajectory before the horizon.

## 4. Event-conditioned temporal precedence reproduced perfectly

The inherited ensemble attempted 100 trajectories and retained 83 that were baseline-eligible under the frozen rule. Thirty-five of those trajectories reached realized functional-trait loss; 48 remained event-free through the common horizon. [E1]

For every one of the six warning thresholds, the threshold crossed before all 35 observed losses. There were no ties and no lags among those valid event pairs:

\[
35/35\quad\text{event leads.}
\]

The independently seeded fresh ensemble attempted 100 trajectories, retained 82 baseline-eligible trajectories, observed 33 losses and retained 49 horizon non-events. Every one of the same six thresholds again crossed before every observed loss:

\[
33/33\quad\text{event leads.}
\]

Thus the event-conditioned result reproduces exactly in the sense for which it was originally designed. This is not a failed replication. The temporal statement is real within the frozen domains.

That fact makes the predictive failure more informative, not less. If the lead ordering had simply failed to reproduce, one could dismiss the warning because the precursor was unstable. Instead, the precursor is maximally reproducible among events and still fails as a classifier.

## 5. Restoring the non-event denominator reverses the interpretation

The same six thresholds fired by the common horizon in all non-event trajectories:

\[
48/48\quad\text{inherited non-events,}
\]

and

\[
49/49\quad\text{fresh non-events.}
\]

For every threshold in each ensemble, the horizon-level binary marker therefore had

\[
\text{sensitivity}=1,
\]

\[
\text{false-positive rate}=1,
\]

\[
\text{specificity}=0,
\]

and

\[
\text{AUC}=0.5.
\]

The positive predictive value collapses to event prevalence because every eligible trajectory is marker-positive. It is 0.422 in the inherited ensemble and 0.402 in the fresh ensemble. Negative predictive value is undefined because no trajectory remains marker-negative. [E1]

The outcome is the strongest possible separation between lead ordering and predictive discrimination. The event-conditioned statement “all observed losses were preceded by the threshold” is true. The predictive statement “threshold crossing distinguishes future loss by the horizon” is false for these six rules in these two tested ensembles.

The denominator is therefore not a reporting detail. It changes the scientific estimand.

## 6. Why event-only success can be misleading

A biologically plausible precursor may be common under general deterioration. If both eventual events and horizon non-events experience the same precursor, then the precursor can look compelling when only event trajectories are plotted. Its temporal relation to the event may even be extremely stable.

But a warning has to do more than belong to the deterioration process. It must separate relevant futures under its declared evaluation contract. A precursor that fires everywhere is not a horizon-level discriminator.

This point generalizes conceptually beyond genetics without generalizing the empirical result. Event-conditioned case series answer a conditional timing question. Prospective warning claims require information about false alarms, non-events or another design that can evaluate discrimination. The exact metrics and appropriate time-to-event methods can differ across applications, but the denominator distinction remains.

For this dissertation, the key lesson is narrower:

> **temporal earliness is one kind of richness, and it is not an automatic certificate of predictive adequacy.**

Chapter 1 showed that observation richness does not automatically buy mechanism identification. Chapter 2 now shows that temporal richness—being consistently earlier—does not automatically buy warning discrimination. The estimands differ, so the two results should not be collapsed into one theorem. [TR1]

## 7. TU-4: loss-generating state and warning-evaluation state need not coincide

The empirical audit is complemented by a formal firewall. TU-4 distinguishes the state required to generate the loss process from the state required to represent the joint warning/loss relation. [T4]

Let a loss-response signature be

\[
\lambda:\Omega\to\Lambda,
\]

and let the associated loss-generating quotient be \(Q_L\). Let the warning-response signature be

\[
\gamma:\Omega\to\Gamma_W.
\]

The warning-evaluation signature is

\[
\eta(\omega)=(\lambda(\omega),\gamma(\omega)),
\]

with quotient \(Q_W\).

Because equality of the joint signature implies equality of the loss signature,

\[
Q_W\text{ refines }Q_L.
\]

The two states are equal exactly when warning behaviour factors through the loss quotient:

\[
\gamma=\bar\gamma\circ q_L.
\]

Thus a loss-generating state is sufficient for warning evaluation only if warning behaviour is homogeneous within every loss-state class. Otherwise warning evaluation requires a finer representation. [T4]

This theorem prevents another shortcut. Fixing the loss process warning-blind is necessary to avoid circularity, but it does not imply that the loss-state representation itself determines warning validity.

TU-4 also separates within-state replication from portability. A warning law that is reproducible in one calibrated domain does not automatically transport to another. Even if two domains have matching loss-state structures, warning behaviour must satisfy its own correspondence condition. [T4]

## 8. Secondary summaries do not rescue the frozen rules

The audit also retained fixed ramp-end summaries as secondary descriptions. Their AUC values ranged only from 0.500 to 0.538 in the inherited ensemble and 0.500 to 0.510 in the fresh ensemble. [E1]

These values are not the headline result because the frozen warning rules are horizon-level threshold events, not a common-time continuous score designed for ROC analysis. Introducing a new continuous score after seeing the negative result would change the scientific question.

The appropriate response to the failed frozen rules is therefore not to search post hoc for another threshold, seed subset or transformed score within the same claim. A genuinely new warning statistic would require a separately declared development and validation programme.

This is part of the chapter's fail-closed logic: a negative result closes the tested rule; it does not authorize retuning until a warning appears.

## 9. What this chapter establishes—and what it does not

The chapter establishes that, for six frozen 5%, 10% and 20% baseline-relative \(H_\alpha\)/\(H_\gamma\) rules in two tested symmetric finite-model ensembles:

1. event-conditioned lead ordering reproduced perfectly;
2. all eligible horizon non-events also crossed every rule;
3. horizon-level specificity was zero;
4. binary-marker AUC was 0.5;
5. therefore perfect temporal precedence did not establish predictive warning validity.

It does **not** establish that genetic diversity is never predictive. It does not test all possible genetic statistics, multivariate warning systems or continuous scores. It does not establish a universal threshold. It does not imply that no early warning can exist in a different model or ecological system. It does not identify a causal mechanism for diversity decline. It does not authorize a post-result threshold search. [E3]

The correct negative claim is precise:

> **These six frozen rules are not valid predictive warnings under the declared horizon-level contract in the two tested finite-model ensembles.**

That precision matters for the dissertation's larger argument. A forbidden inference is useful only if blocking it does not create an equally unjustified converse.

## 10. Transition: after a warning fails, what should be measured next?

The negative warning result leaves a practical problem. If a plausible, reproducibly early signal does not discriminate the target event, collecting more of the same signal is not automatically the best next move.

But Chapter 2 does not determine which measurement should replace it. The failed warning thresholds and the observation-design problem are different scientific objects. MROD does not rescue these thresholds or use their negative result as its benchmark. It asks, within a declared set of still-admissible mechanisms and verified candidate observations, which measurement currently carries the most information about unresolved mechanism identity. [TR2]

The handoff is therefore a question, not an implication:

> **If temporal precedence is insufficient for warning, how should we choose what to measure next when several explanations remain compatible?**

Chapter 3 answers that measurement-ordering question under its own controlled benchmark and claim ceiling.

## Internal source keys

- **[E1]** EGWE `manuscript/warning_validity.md` — full-denominator design, counts, metrics, interpretation and claim boundary.
- **[E2]** EGWE `REPRODUCIBILITY.md` and source manifests — frozen parent/fresh provenance, no endpoint or trajectory rerun.
- **[E3]** `thesis/verification_recovery_registry.json`, Chapter 2 claim ceiling; EGWE Discussion claim boundary.
- **[T4]** `theory/TU4_WARNING_STATE_PORTABILITY.md` — WarningEvaluationState refinement, equality factorization and portability firewall.
- **[TR0]** `thesis/final_chapter_architecture.json` and `thesis/transition_recovery_matrix.json` — Chapter 2 imports frozen loss/event labels; editorial order does not create source prerequisites.
- **[TR1]** transition recovery: identification and warning discrimination remain distinct estimands.
- **[TR2]** transition recovery: EGWE→MROD is an editorial question handoff; MROD is not a rescue analysis of failed warning thresholds.
