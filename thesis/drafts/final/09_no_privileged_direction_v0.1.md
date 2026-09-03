<!-- draft-id: chapter:synthesis:v0.1 -->
# 総合 — 妥当性に特権的な方向はない

*English working title: Synthesis — Adequacy Has No Privileged Direction*

> **Draft status:** bounded synthesis v0.1. The exact theorem owned here is TU-1 on revision after compression. Chapters 1–8 remain source-owned proved conditions under different carriers, estimands, contracts, and comparison orders. This chapter does not claim one global scalar theorem of scientific adequacy.

## 1. The dissertation began with reuse, not with “more is bad”

The opening problem was simple to state. A representation, measurement, law, state variable, or evidence design works for one scientific responsibility. Can it be reused when the responsibility changes?

A tempting response is to order scientific objects by richness. Keep the more detailed state. Measure more variables. Prefer the earlier signal. Retain more memory. Add more interventions. Collect more replicates. If one object contains “more,” perhaps it should be at least as adequate as a poorer one.

The final forbidden inference is therefore deliberately broad:

> **より詳細にする／より多く測る／より長く記憶する／より多く介入する ⇒ より妥当になる**

But the dissertation has not proved the simple converse either. It does not show that more detail, measurement, memory, intervention, or repetition is generally harmful. Several chapters contain regimes in which enrichment is exactly what is required. Chapter 1 needs an additional independent observation direction. Chapter 3 benefits from adaptive measurement when branchwise optima conflict. Chapter 5 requires more response memory when newly legal futures become addressable. Chapter 8 can favor additional independent modes above an explicit sensitivity threshold.

The synthesis is therefore not anti-information. Its claim is narrower:

> **Richness has no privileged validity status before the scientific responsibility and its adequacy condition are specified.**

That statement is supported not by one global monotonicity theorem, but by TU-1 plus eight typed source-owned conditions. [S1,S2]

## 2. TU-1 gives the exact reuse theorem for revision after compression

TU-1 isolates the dissertation's opening reuse problem on one finite carrier.

Let an old scientific contract store partition \(P\) with quotient map

\[
q_P:\Omega\to S_P,
\]

and let a revised responsibility require partition \(Q\) with quotient map

\[
q_Q:\Omega\to S_Q.
\]

The question is whether the revised state can be computed using only the state label that was retained under the old contract.

TU-1 proves that the following are equivalent:

1. there exists a deterministic recoding \(f:S_P\to S_Q\) such that
   \[
   q_Q=f\circ q_P;
   \]
2. worlds merged by the old state are also merged by the revised state;
3. every block of \(P\) lies inside one block of \(Q\);
4. the old partition is at least as informative as the revised partition in the relevant refinement order. [T1]

Thus reuse after revision is not licensed because the old representation was once successful, nor because it was large, detailed, or expensive. It is licensed exactly when the revised response **factors through what was retained**.

This is the precise sense in which adequacy is responsibility-relative without becoming arbitrary. The revised contract supplies a mathematical test.

## 3. When factorization fails, TU-1 quantifies the information that was forgotten

If state-only revision fails, TU-1 does not stop at “information was lost.” It asks for the minimum auxiliary code needed to repair the old representation.

For each old block \(B\in P\), let

\[
r_B(P,Q)
\]

be the number of revised-state blocks intersecting \(B\). Define

\[
K_{\rm rev}(P\to Q)=\max_{B\in P}r_B(P,Q).
\]

TU-1 proves that the minimum auxiliary alphabet permitting exact revision has cardinality exactly

\[
\boxed{|M|_{\min}=K_{\rm rev}(P\to Q)}.
\]

The corresponding minimum fixed-length side memory is

\[
\boxed{b_{\rm rev}=\left\lceil\log_2 K_{\rm rev}\right\rceil}.
\]

Necessity comes from the worst old block: if one old label hides \(r_B\) distinct revised states, those possibilities must be separated somehow. Sufficiency follows because auxiliary labels can be reused across different old blocks; the old label already tells us which block we occupy. [T1]

TU-1 further distinguishes average global refinement from worst-case local revisability. A representation can have arbitrarily small average refinement debt while one rare old state hides an arbitrarily large revision burden. [T1]

This result supplies the exact substrate for the final chapter: what matters is not how rich a representation appears globally, but whether it preserves distinctions required by the next contract.

## 4. Why TU-1 does not subsume Chapters 1–8

It would be tempting to announce that every previous chapter is “really” TU-1. That would overstate the theory and erase the source programmes' distinct estimands.

Chapter 1 studies rank of an observation operator. Chapter 2 studies discrimination of a binary horizon marker. Chapter 3 studies adaptive expected mechanism-information value. Chapter 4 studies order-theoretic scalar representability of multiple targets. Chapter 5 studies exact response memory under future grammar expansion. Chapter 6 studies state and monitoring burden under capability expansion. Chapter 7 studies source-relative law transport across a changing carrier/relation. Chapter 8 studies failure-aware detection guarantees.

These are not one mathematical object in disguise. Their carriers, probability structures, resource measures and adequacy criteria differ. [S1]

TU-1 instead supplies a meta-level reuse question:

> after one responsibility has licensed a compression, can the distinctions needed by a later responsibility still be recovered from what was retained?

Some later chapters can motivate a revised \(Q\), but their theorems are not corollaries of TU-1.

## 5. Chapter 1: additional observation matters exactly when it adds an identifying direction

The first research chapter replaced observational richness with a rank condition.

For compatible exact log-linear observations

\[
Mx=y,
\]

the mechanism-compatible set has dimension

\[
k-\operatorname{rank}(M).
\]

A new scalar observation reduces structural ambiguity **if and only if** its row lies outside the current row span. If it does, the residual dimension drops by exactly one. [S2]

This makes several apparently different enrichments equivalent from the identification perspective: exact repetition, rescaling, or any linear combination of existing observation rows adds no structural rank. Greater precision can reduce statistical uncertainty while leaving structural identification unchanged.

The relevant direction is not “more observation.” It is “more independent mechanism-separating observation.”

## 6. Chapter 2: perfect temporal richness fixes sensitivity but leaves discrimination open

The second chapter replaced the intuitive value of “earlier and more reproducible” with a denominator theorem.

Under perfect event-conditioned precedence of a binary horizon marker, sensitivity is forced to one. But non-event specificity is unconstrained by that event-only statement. For the binary score,

\[
\mathrm{AUC}=\frac{1+\mathrm{specificity}}{2}.
\]

The same perfect event precedence is therefore compatible with AUC from 0.5 to 1. The locked EGWE ensembles attain the sharp lower endpoint: 35/35 and 33/33 event leads coexist with 48/48 and 49/49 non-event firings. [S2]

Here “more temporal consistency” is not wrong or useless. It answers the event-conditioned timing question extremely well. It simply does not determine the different responsibility of warning discrimination.

## 7. Chapter 3: adaptivity has value exactly when the future choice actually depends on the observed branch

The third chapter replaces “more candidate measurements” and “adaptive is better” with another iff condition.

After a fixed first observation \(X\), let \(U_q(x)\) be the mechanism-learning value of remaining candidate \(q\) on branch \(x\). Then

\[
V_{\rm adapt}=E[\max_q U_q(X)]
\]

is always at least

\[
V_{\rm static}=\max_q E[U_q(X)].
\]

The inequality is strict **if and only if** no candidate is optimal on every positive-probability branch. Equivalently, the intersection of branchwise argmax sets is empty. [S2]

Thus adaptivity is not privileged either. If one measurement remains best on every possible first outcome, recomputation cannot improve expected second-step value. When branchwise optima conflict, no fixed second choice can match the adaptive policy.

The four-world witness reaches 1.0 bit adaptively versus 0.5 bits for the best static candidate and is minimal in its declared deterministic branch-switch class.

## 8. Chapter 4: one state scalar exists exactly when the targets admit one order

The fourth chapter makes state plurality testable rather than philosophical.

For a finite set of target vectors oriented so that larger coordinate values mean no worse, one exact directionally coherent sufficient scalar exists **if and only if** the distinct target vectors form a chain under coordinatewise product order. [S2]

A crossing pair is therefore an impossibility certificate.

The locked eco-genetic H3 result contains such a crossing between the two-patch and sixteen-patch states: retained interaction and local effective size decline while realised high-trait mass rises. The chain condition fails on that finite target set.

This does not mean scalar indices are always invalid. It states exactly when one common monotone scalar can represent all declared targets, and why it cannot do so in the recovered crossing.

## 9. Chapters 5 and 6: local size and capability size do not bound the knowledge responsibility they expose

CCOC and CREST contain two superficially similar but distinct no-bound results.

In Chapter 5, static/local resource measures remain fixed while the legal future grammar is opened. A bounded-degree tree with one-edge focal/exterior cut and bounded local alphabets can move from a two-class closed quotient to \(2^{m+1}\) open response classes, creating exactly \(m\) additional response bits. The family attains the finite-domain bound. Separate coherence conditions show when a shared portable macro-law does exist. [S2]

In Chapter 6, the future change is not grammar opening but capability expansion. For every \(m\ge1\), one new controllable action can add exactly one robust-carrier world while forcing a retained present slice from one required state to \(2^m\) and creating exactly \(m\) monitoring bits under unchanged evidence. No finite upper bound based only on carrier-size gain can control the required resolution. Yet a coarse target can remain reportable. [S2]

Neither result says that richer futures or interventions are bad. They show that the visible size of the physical/capability change is not a privileged proxy for the representational burden created by the responsibility.

## 10. Chapter 7: source success does not license transport without an exact coherence test

MLTR addresses another kind of apparent richness: confidence in an already exact source law.

The carried source law remains exact on a target **if and only if** output, legal-action rows, and successor carried labels are constant within every carried target fiber. Failure has a finite witness, and fixed-point refinement returns the unique coarsest exact source-relative repair. [S2]

Across several replacement routes, one route-independent inherited semantics exists exactly when complete carried terminal maps agree. If they differ, one immutable history mode per distinct carried map is necessary and sufficient.

Thus even perfect source exactness has no privileged transport status. What matters is whether the target relation preserves the operational distinctions that give the inherited labels their meaning.

## 11. Chapter 8: even the correction to replication has a condition

The final research chapter is especially useful for the synthesis because it contains a reversal inside one declared design problem.

At equal effort of two reads per truly present coordinate, compare one mode with two repeats against two independent modes with one read each. For joint detection of \(k\) coordinates,

\[
G_D>G_R
\iff
p>2-2^{1/k}.
\]

Below the threshold, deeper repetition is better; above it, failure-mode diversity is better. [S2]

So the dissertation cannot end by replacing “more repeats is better” with “more diverse modes is better.” The correct design depends on read sensitivity and target dimension.

At large within-mode effort, a separate theorem imposes the worst-case availability ceiling

\[
1-(1-a)^m
\]

for fixed mode count \(m\). No amount of repetition inside those same modes can raise the uniform contract guarantee above it.

Chapter 8 therefore contains the local lesson of the entire thesis in miniature: enrichment has to be evaluated relative to the failure mechanism and target responsibility.

## 12. The eight conditions do not define one scalar adequacy order

The typed synthesis matrix records eight different richness proxies and eight different adequacy responsibilities. [S1]

| Chapter | Richness proxy | Adequacy responsibility | Replacement condition |
|---:|---|---|---|
| 1 | observation amount/proximity | mechanism identification | new observation must increase rank |
| 2 | precedence consistency | warning discrimination | full denominator determines specificity/AUC |
| 3 | candidate measurements/adaptivity | mechanism-learning value | strict adaptive gain iff no common branchwise optimum |
| 4 | common state detail | multi-target scalar adequacy | target vectors must form a product-order chain |
| 5 | physical/local boundary | open-future response memory | addressability can force arbitrary memory; coherence gives positive portability |
| 6 | capability increment | required state/monitoring | carrier gain alone supplies no finite burden bound |
| 7 | source-law exactness | structural portability | within-fiber coherence; route maps determine history modes |
| 8 | replicate/mode allocation | failure-aware guarantee | finite threshold plus asymptotic mode ceiling |

These rows cannot be pooled into a single effect size. A rank, an AUC, a mutual-information value, a product-order condition, a number of bits, a carrier increment, a history-mode count and a detection guarantee are not exchangeable units.

Therefore “no privileged direction” means:

> none of these untyped richness proxies can certify adequacy outside the condition associated with its scientific responsibility.

It does **not** mean that all forms of scientific enrichment are incomparable in every context.

## 13. Adequacy is a relation, not an intrinsic amount possessed by a representation

The dissertation's common conceptual move can now be stated without inventing a global metric.

A representation \(R\) is not simply “adequate” because it contains many variables, has high resolution, or once predicted well. Adequacy is always shorthand for a relation:

\[
R\quad\text{is adequate for responsibility}\quad\mathcal C
\]

under a declared observation/model/error/transport contract.

Changing \(\mathcal C\) can change which distinctions must be preserved. TU-1 tests whether the revised responsibility factors through the retained state. Chapters 1–8 show that the relevant preservation criterion can involve rank, discrimination, adaptive branches, target order, future response addressability, intervention-dependent state refinement, structural semantics, or failure modes.

This relational view is not permission to define a new state every time a result is inconvenient. Each chapter requires the responsibility and its criterion to be declared and then tested. Failures remain failures; `not evaluable`, ambiguity sets, repair costs and STOP outcomes remain legitimate outputs.

## 14. What “more information” can safely mean after this dissertation

The phrase “more information” is useful only after its object is typed.

One can legitimately say:

- the observation operator has higher rank;
- the marker has higher specificity;
- an experiment has greater conditional mechanism information;
- a stored representation refines another partition;
- an interface requires more exact response bits;
- a capability contract requires a finer state;
- a replacement history needs more immutable modes;
- a monitoring design has a higher worst-case detection guarantee.

Those are meaningful ordered statements.

What the dissertation rejects is the silent transition from any one of them to a generic statement of greater scientific validity.

The missing bridge is always the scientific responsibility.

## 15. The practical rule is not “keep everything”

One reaction to revision risk is to preserve maximal raw detail forever. TU-1 explains why that is safe in one narrow sense: retaining a finer old state cannot increase the worst-case auxiliary revision debt for a later same-carrier partition.

But maximal retention is not the dissertation's recommendation.

First, Chapter 4 shows that raw detail and target-relevant state are different objects. Second, Chapter 6 shows that full-state monitoring can become unlicensed while a coarse target remains reportable. Third, Chapter 8 shows that more observation effort can be allocated inefficiently. Scientific design still has costs, nuisance dimensions, failure modes and target-specific stopping rules.

The alternative is **revision-aware compression**:

1. declare the present responsibility;
2. retain the minimal distinctions needed for it;
3. identify plausible future responsibility changes;
4. test whether those revised responses factor through what will be stored;
5. when they do not, quantify or deliberately retain the side information needed for revision.

This is the constructive reading of the reuse problem.

## 16. What this dissertation establishes—and what it does not

The dissertation establishes an exact same-carrier reuse theorem in TU-1 and assembles eight source-owned proved conditions showing that different forms of apparent scientific richness require different adequacy tests.

It establishes that:

1. state-only revision after compression is possible iff the revised state factors through the retained old state;
2. exact auxiliary revision debt has a minimum alphabet determined by the worst hidden split of an old block;
3. Chapters 1–8 each replace one automatic reuse/richness shortcut with a theorem-level condition, sharp boundary, or no-bound result;
4. all eight conditions are verified against their source proof/test contracts;
5. the synthesis must remain typed because the rows use different mathematical and scientific objects.

It does **not** establish one intrinsic ecological state, one universal information metric, or one global theorem that adequacy rises or falls monotonically with detail. It does not say simpler representations are generally better. It does not say richer representations are generally safer. It does not transfer theorem ownership from the source repositories to theouni. [S1,S3]

The strongest safe synthesis is:

> **Scientific adequacy has no privileged untyped direction. A representation, observation, law, intervention model, or evidence design earns reuse only through the condition attached to the responsibility it must support.**

## 17. Closing the loop

Chapter 0 asked what happens after a representation that once worked is asked to carry a new responsibility.

The answer is now precise enough to be useful.

Sometimes reuse is exact: the new response factors through the old representation, a new observation adds no necessary distinction, a carried law remains coherent, or repeated measurements already meet the required failure-aware guarantee.

Sometimes reuse fails but admits a minimal repair: add one independent observation direction, retain one missing state distinction, add the minimum auxiliary code, refine the inherited law, introduce the required history modes, or add enough independent failure opportunities.

And sometimes the available design cannot license the desired conclusion at all. Then ambiguity, partial identification, set-valued reporting, `not evaluable`, or STOP is not an analytical embarrassment. It is the correct boundary of the current scientific contract.

The dissertation's final principle is therefore not “more is not better.” It is more demanding:

> **Before reusing what worked, prove that it still preserves what the new question requires.**

## Internal source keys

- **[T1]** `theory/TU1_CONTRACT_REVISION.md` and `theory/verify_tu1.py` — factorization iff, minimum auxiliary alphabet, average-versus-worst revision debt and divergence family.
- **[S1]** `thesis/typed_synthesis_matrix.json` v2 and `thesis/TYPED_SYNTHESIS_RECOVERY.md` — typed synthesis boundaries and prohibition on a global scalar adequacy theorem.
- **[S2]** `thesis/proved_condition_registry.json` — exact imported proved condition, proof source, verification source and claim ceiling for Chapters 1–8.
- **[S3]** `thesis/verification_recovery_registry.json` and `universe/WORLDLINE_ATLAS.md` — source ownership, synthesis status and separation between editorial traversal and non-ordered theory map.
