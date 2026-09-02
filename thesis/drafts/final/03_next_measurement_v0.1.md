<!-- draft-id: chapter:3:v0.1 -->
# 境界の内側で、次に何を測るか

*English working title: What to Measure Next Inside the Boundary*

> **Draft status:** source-bounded v0.1 from MROD snapshot `5a89c3f77b3987751652541086816231507edf9d`. The chapter concerns observation ordering under a declared admissible mechanism family and verified candidate measurements. It is not a rescue analysis of the failed EGWE warning thresholds and does not claim universal optimality over ecological experimental design.

## 1. “Collect more data” is not an observation design

Once a scientific analysis admits that several mechanisms remain compatible with existing observations, one practical question becomes unavoidable: what should be measured next?

The tempting shortcut is to treat measurability itself as evidence of value. If a variable can be collected, is biologically interesting, or has high technical precision, it may be added to the measurement programme without asking which unresolved mechanism distinction it can actually resolve. Under limited budgets, this can be wasteful even when every measurement is perfectly valid.

The forbidden inference of this chapter is:

> **測れるものは測る価値がある ⇒ 測る順序に良し悪しはない**

The first half is intentionally phrased as a temptation rather than a theorem: a measurable variable may be worth measuring for many scientific reasons. The error is the second step—assuming that all available measurements are equally useful for the particular ambiguity that remains.

MROD changes the object of inference. Instead of forcing a single “best” mechanism from data that do not distinguish the candidates, it retains the admissible mechanism region and asks which candidate observation carries information about that retained ambiguity. [M1]

This chapter therefore begins where Chapter 2 leaves us, but it does not repair Chapter 2. The failed genetic warning thresholds are not candidate observations inside the MROD benchmark, and the negative warning result does not supply MROD's hidden truth. The handoff is only a question: after one easy measurement shortcut fails, how should a new observation be selected under unresolved explanation? [TR0]

## 2. Keep the compatible mechanisms before choosing among measurements

Let

\[
S\in\{0,1\}^K
\]

be a declared binary mechanism vector and let \(\theta\) denote continuous or discrete parameters. Let \(G(\theta)\) be a pre-data biological constraint grammar, \(x_{obs}\) fixed context, \(y_{obs}\) observed targets, \(f\) a simulator or predictive model, \(P_{sim},P_{obs}\) mappings into a shared pattern space, \(d\) a predeclared discrepancy, and \(\epsilon\) an acceptance tolerance.

MROD defines the admissible mechanism region

\[
A_\epsilon(y_{obs},x_{obs})=
\{(\theta,s):G(\theta)=1,
\ d(P_{sim}(f(x_{obs};\theta,s)),P_{obs}(y_{obs}))\le\epsilon\}.
\]

The implementation approximates this set by prior sampling and rejection. The important conceptual choice is that multiplicity in the retained region is not treated as a nuisance to be hidden behind a modal row. It is the scientific object needed for the observation-design problem. [M1]

If several mechanism programmes survive the current evidence, then the design problem is not “which one should we declare correct?” but “which prospective measurement separates the surviving programmes?”

This is a different response to ambiguity from ranking alone. A highest posterior or likelihood model may be useful when evidence genuinely separates candidates. But a modal label does not remove structural overlap among the remaining programmes. MROD preserves the overlap first, then acts on it.

The method also fixes evidence roles before inference:

- `observed_target` may enter the acceptance discrepancy;
- `input_context` conditions the simulator but is not recycled as independent target evidence;
- `diagnostic_only` checks inference/software behaviour after fitting;
- `future_observation` is withheld and evaluated as a prospective measurement.

This role discipline prevents a variable from being used to define the initial state, fit the mechanism and then appear again as independent validation. [M1]

## 3. Residual mechanism ambiguity is an explicit output

For the retained mechanism vector \(S\), MROD uses the joint entropy

\[
D=H(S\mid A_\epsilon)
\]

as residual mechanism entropy and defines normalized resolvability

\[
R=1-\frac{D}{K}.
\]

Because a \(K\)-bit switch vector has at most \(K\) bits of entropy,

\[
0\le D\le K,
\qquad
0\le R\le1.
\]

The normalization uses the maximum switch entropy rather than the realized prior entropy. Thus \(R=1\) means the declared switch vector is fully resolved inside the accepted region, while lower values preserve joint ambiguity. [M1]

This does not turn entropy into a universal measure of ecological uncertainty. It is the declared mechanism-state uncertainty for this method. Parameter uncertainty, model-family misspecification, target uncertainty and observation failure remain distinct objects.

The key move is methodological: unresolved ambiguity is reported instead of silently discarded. That makes it possible to ask which future observation can change the ambiguity.

## 4. Observation value is conditional on what remains unresolved now

Let \(Q\) be a candidate future measurement with finite outcomes \(q\). For a validated stored-region calculation, the candidate's outcome maps must form a mutually exclusive and exhaustive partition of the current admissible region.

MROD defines the observation information value as the expected gain in normalized resolvability:

\[
V(Q)=E_Q[R(A_\epsilon\mid Q)-R(A_\epsilon)].
\]

Using the entropy definition,

\[
V(Q)=\frac{I(S;Q\mid A_\epsilon)}{K}.
\]

Therefore

\[
0\le V(Q)\le1-R(A_\epsilon)\le1.
\]

A candidate has \(V(Q)=0\) exactly when it carries no information about the residual mechanism identity under the current admissible region. [M2]

This provides the direct answer to the chapter's forbidden inference. Two measurable variables can have very different values for the current scientific responsibility. A candidate can be biologically meaningful and technically valid while having zero information about the mechanism distinctions that remain.

The value is state-dependent in an epistemic sense: it must be recomputed after each realized measurement because the admissible region changes. An observation that is valuable before one measurement may become redundant after that measurement. Conversely, a candidate that was initially modest may become decisive once another ambiguity is removed.

A candidate is reported as non-estimable when its predictive outcomes do not form a valid partition of the stored region, fail to cover it, overlap, or require unavailable outputs. MROD does not silently insert an external outcome prior and relabel the result as validated information value. [M1]

Thus “not estimable” is part of the scientific output rather than an invitation to improvise a score.

## 5. Sequential design makes ordering consequential

The design is adaptive:

\[
A_0=A_\epsilon.
\]

At step \(t\):

1. compute \(V_t(Q)=I(S;Q\mid A_t)/K\) for every verified remaining candidate;
2. select the candidate with maximum positive current value;
3. reveal or obtain its realized outcome only after selection;
4. condition \(A_t\) on that outcome to obtain \(A_{t+1}\);
5. recompute all remaining candidate values.

The procedure stops when the observation budget is exhausted, the declared confounding structure is resolved, or every remaining verified candidate has zero current information value. [M1]

The final stop condition is important. Mechanism ambiguity may remain even when no available candidate can resolve it. That is not algorithmic failure; it is a limitation of the declared measurement vocabulary.

The method therefore distinguishes two statements that are often conflated:

> unresolved mechanism remains

and

> a currently available measurement can resolve it.

The first does not imply the second.

## 6. The frozen benchmark tests selection without truth peeking

MROD's primary validation is not a natural ecological mechanism claim. It is a controlled benchmark designed to test the observation-selection policy itself.

The frozen G2 protocol uses five predeclared seeds and 200 generated systems per seed. Each system contains \(K\in\{4,5,6\}\) mechanism switches, one or two disjoint two-driver confounds, randomized pre-data coefficients, 1,500 prior draws, and one explicit resolving quantitative observation for each confound. Two additional binary nuisance measurements are generated independently of the mechanism vector. [M3]

These nuisance measurements are deliberately important. They are valid candidate observations: their outcomes are mutually exclusive and exhaustive. They simply contain no designed information about the mechanism identity. The benchmark therefore distinguishes “valid to measure” from “valuable for the current ambiguity.”

The same seed-defined systems, hidden truths, candidate sets and budgets 0–4 are supplied to two policies:

- **information-guided:** select the remaining candidate with maximum current \(V(Q)\);
- **random order:** select uniformly among remaining candidates.

Neither policy sees a hidden candidate outcome before selection. Hidden truth is used only after a policy selects a measurement, to materialize that benchmark outcome. The accepted region is then conditioned and the guided policy recomputes values. [M3]

This truth-peek-free structure matters because a measurement policy can look optimal if candidate outcomes are inspected before selection. The benchmark prohibits that shortcut.

## 7. Under a limited budget, ordering changes what is resolved

At budget two, the information-guided policy resolved all initial confounding edges on average:

\[
\text{mean fraction resolved}=1.000.
\]

It converged to an empty confounding graph in 0.990 of systems across the five frozen seeds, used 1.505 observations on average, and selected only 0.001 nuisance measurements per system. [M3]

Random ordering, on the identical generated systems and budget, resolved only

\[
0.6045
\]

of the initial confounding edges on average and converged in 0.435 of systems. It used 1.821 observations and selected 0.974 nuisance measurements per system. [M3]

Thus the measurements were not interchangeable under a constrained budget. The guided policy did not gain an advantage by adding more measurement opportunities; both policies had the same candidates. The advantage came from ordering candidates according to their current relation to the unresolved mechanism set.

At budget one, convergence was 0.495 for information-guided design and 0.179 for random order. The gap reflects the fact that a first measurement can either attack a current confound or spend the only available opportunity on a nuisance candidate.

These policy contrasts were designated descriptive in the frozen protocol. There was no favourable-result threshold that the guided policy had to pass for the analysis to be retained. [M3]

## 8. When both policies have enough budget, nuisance selection exposes efficiency

Budget four is particularly informative because both policies resolved all initial confounding edges on average. At that point the headline distinction is no longer whether one policy can eventually remove the declared confounds, but how much irrelevant measurement effort it spends on the way.

The information-guided policy converged in 0.999 of systems and used 1.518 observations. Random order converged in 0.940 and used 2.673 observations. [M3]

Most visibly, random ordering selected

\[
1.169
\]

mechanism-independent nuisance measurements per system, whereas information-guided selection used

\[
0.014.
\]

The ratio is approximately 83.5-fold, corresponding descriptively to about 98.8% fewer nuisance selections relative to random order. The absolute difference is more stable and remains visible without relying on a ratio with a small denominator. [M3]

The result is not “information theory always saves 98.8% of measurements.” It is a benchmark-specific demonstration that a policy tied to residual mechanism information can avoid valid but mechanism-irrelevant observations when candidate order matters.

## 9. Truth retention prevents a trivial route to apparent resolution

A method could achieve impressive resolution numbers simply by conditioning so aggressively that it excludes the true generating explanation. The G2 benchmark therefore records false exclusion of hidden truth.

Hidden-truth false exclusion was zero in every policy-by-budget cell. All 10,000 stored system–policy–budget records retained the generating explanation. [M3]

This matters for interpretation. The guided policy's ambiguity reduction was not obtained by manufacturing confidence through deletion of the hidden true mechanism. The benchmark tests selection within a declared candidate family, not arbitrary model misspecification, but within that family the generating programme remains admissible throughout.

## 10. Candidate value is not identical to target licensing

MROD's observation value is explicitly about residual mechanism identity. That scientific responsibility must not be confused with every other reason to measure something.

TU-2 makes this distinction exact. Let \(S\in\{0,1\}^m\) be a causal programme state and let \(T\in\{0,1\}\) be an independent report target. For experiments \(Q_{k,b}\), where \(k\) controls how many causal bits are revealed and \(b\) controls whether \(T\) is also observed, TU-2 constructs pairs with the same causal information gain but opposite target-licensing status. [T2]

For every \(k\),

\[
I(S;Q_{k,0})=I(S;Q_{k,1})=k,
\]

while the target remains unlicensed for \(Q_{k,0}\) and fully licensed for \(Q_{k,1}\).

At one extreme, observing all of \(S\) gives maximal mechanism-learning value while leaving the independent target unresolved. At the other, observing \(T\) directly gives zero information about \(S\) while completely licensing the target. [T2]

The lesson is not that MROD's value function is wrong. It is that it is correctly typed. It ranks observations for learning the declared mechanism vector. A different scientific responsibility can rank the same measurements differently.

This prevents the dissertation from upgrading

> high observation information value for mechanism learning

into

> universally best observation.

## 11. What this chapter establishes—and what it does not

The chapter establishes that, under MROD's declared mechanism vocabulary, admissible-region construction and verified candidate outcome partitions:

1. unresolved mechanism multiplicity can be retained as an inferential output;
2. candidate observation value is normalized mutual information about the residual mechanism vector;
3. value must be recomputed after each realized observation;
4. a valid measurable candidate can have zero value for the current mechanism ambiguity;
5. in the frozen truth-peek-free G2 benchmark, information-guided ordering resolves confounding more efficiently than random ordering under limited budgets;
6. the selection advantage does not arise from excluding the hidden generating explanation;
7. mechanism-learning value remains distinct from target licensing.

It does **not** establish universal optimality over all experimental-design algorithms, priors, simulator families or ecological systems. It does not identify a true natural mechanism. It does not imply that low-\(V(Q)\) observations are scientifically useless for other targets. It does not say the declared mechanism vocabulary is complete. It does not rescue the failed EGWE warning thresholds. [M4]

The safe conclusion is:

> **When the scientific responsibility is resolution of a declared mechanism ambiguity, measurement order can be evaluated by the information each candidate carries about what remains unresolved, and valid candidates need not be equally valuable.**

## 12. Transition: what exactly is the state being learned?

MROD provides a disciplined answer to “what should be measured next?” only after the object of learning has been declared. Its mechanism vector, admissible region and candidate outcomes are typed by the scientific model.

This creates the next question. If measurement value depends on which distinctions matter for the declared responsibility, can one eco-genetic summary represent all relevant states of a system? Or can potential viability, realized occupancy, demographic condition, genetic diversity and allele persistence respond differently even under one fragmentation contrast?

Chapter 4 therefore asks:

> **Once we can choose measurements intelligently, is there one context-free ecological state that those measurements are trying to recover?**

The transition is again a question handoff. MROD does not prove the eco-genetic five-state separation; the next chapter supplies its own finite-model evidence and TU-3 firewall. [TR1]

## Internal source keys

- **[M1]** MROD `paper/manuscript.md`, Sections 1–2 — admissible region, evidence roles, entropy/resolvability, information value and sequential design.
- **[M2]** MROD information-value identity `V(Q)=I(S;Q|A_epsilon)/K`; independent implementation checks described in Methods/Results.
- **[M3]** MROD frozen G2 benchmark and `paper/results/g2_frozen_v2_summary.json` — five seeds, 1,000 systems per policy, budget outcomes, nuisance selections, false exclusion.
- **[M4]** `thesis/verification_recovery_registry.json`, Chapter 3 claim ceiling; MROD manuscript limitations.
- **[T2]** `theory/TU2_LEARNING_LICENSING.md` and `theory/verify_tu2.py` — causal learning and target licensing are orthogonal; policy reversal.
- **[TR0]** `thesis/transition_recovery_matrix.json`, Chapter 2→3 — MROD is not a rescue analysis of failed warning thresholds.
- **[TR1]** transition recovery, Chapter 3→4 — next-observation value and target-dependent state separation are different estimands; the next chapter owns the latter result.
