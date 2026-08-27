<!-- draft-id: chapter:3:v0.2 -->
# Chapter 3 — When Macro-Laws Do Not Survive Ecological Replacement

> **Draft status:** dissertation-adapted v0.2. The transport, repair, history, proof, replay, figure, and manuscript assets remain owned by `zuizui0223/mltr`.

## 1. The system itself has changed

Chapter 2 held one controlled ecological plant fixed and changed the legal future grammar. It showed that exact interfaces optimized under restricted futures need not combine into one comparably small interface when those futures are opened. Structural ecological change poses a different problem. Species disappear or arrive, interaction networks rewire, habitats are reconfigured, and restoration creates a target system whose raw configurations may not be nested inside the source system at all.

Ecologists nevertheless reuse inherited variables across such changes. A functional guild, successional stage, resilience category, occupancy state, or management class may have been accepted because it supported predictions in the source system. After turnover or replacement, the same label is often carried forward. The label may remain scientifically useful, but that is not guaranteed by its familiarity or by the existence of a target model with the same number of classes.

This chapter asks:

> **Given an exact ecological macro-law accepted for a source system, when can its inherited meaning be transported through structural replacement, and when transport fails, what is the least exact repair that preserves every inherited merge still valid?**

The central prohibition is

\[
\boxed{
\text{exact source macro-law}
\not\Rightarrow
\text{the same exact macro-law after ecological replacement}.
}
\]

The chapter does not solve target abstraction from scratch. The source law is part of the scientific responsibility. Any admissible target repair must remain inside the labels inherited from the source rather than abandoning them for an unrelated target-only optimum. This source-relative constraint gives the results their ecological meaning and distinguishes Macro-Law Transport and Repair (MLTR) from fixed-system lumpability, generic bisimulation minimization, and the closed/open grammar comparison of CCOC.

MLTR returns more than a rejection. It gives an exact portability criterion; a finite local obstruction when portability fails; the unique coarsest exact target refinement that preserves inherited semantics; a transport-defect measure; a path-coherence condition for route-independent meaning; and the minimum history context needed when different replacement routes carry incompatible terminal labels.

## 2. Why target re-aggregation is not enough

Suppose a source community was compressed into two macrostates, `low` and `high`, and that this classification exactly preserved the outputs and interventions relevant to the source programme. After species turnover, a target modeller could ignore the inherited labels and compute a new minimal target partition. That target-only quotient may be mathematically exact. It does not answer whether the original ecological variable survived.

The distinction matters whenever labels carry accumulated scientific or management meaning. A monitoring programme may have thresholds, archived time series, policy rules, or restoration targets expressed in the old categories. Replacing them with a new abstraction can be reasonable, but it is a different decision from repairing the inherited law. MLTR asks how much of the old semantics can remain exact in the changed system.

Formally, the admissible target solution is constrained:

\[
\boxed{
\min_{q_T\ \mathrm{exact},\;q_T\succeq \operatorname{carry}(q_S)}|q_T|.
}
\]

Here \(q_S\) is the accepted source projection, \(\operatorname{carry}(q_S)\) is the partition induced on the target through a declared source–target relation, and \(q_T\succeq \operatorname{carry}(q_S)\) means that the repaired target partition may split inherited fibers but may not merge across their labels.

This constraint makes the outcome a repair rather than a redesign. It also makes repair cost relative to the source law. A smaller target abstraction may exist after discarding inherited meaning; MLTR does not call that smaller abstraction a cheaper repair.

## 3. Operational setting

Let a finite controlled ecological system be

\[
\mathcal S=(X,A,G,\delta,y),
\]

where \(X\) is the finite state set, \(A\) the declared action set, \(G\) the legal finite action grammar, \(\delta\) the controlled transition rule, and \(y\) the current ecological output.

An exact operational macro-law is a surjective projection

\[
q:X\to Q
\]

such that states sharing one macro label have:

1. the same current output;
2. the same legal-action row; and
3. successors carrying the same macro label under every common legal action.

These conditions make the coarse dynamics well defined. A macrostate is not exact merely because it groups states with similar current output. It must support the declared interventions and their successors.

Let \(\mathcal S_S\) be the source system and \(\mathcal S_T\) the target system. Structural replacement is represented by a declared total relation

\[
R\subseteq X_S\times X_T.
\]

The relation can be many-to-one or one-to-many. The source and target spaces need not be nested, and MLTR does not infer \(R\) from data. It is part of the finite model contract.

Let

\[
q_S:X_S\to Q_S
\]

be an exact source projection. When every target state related to source states receives one consistent source label, the relation induces the carried target map

\[
c_R(t)=q_S(s)
\qquad ((s,t)\in R).
\]

The first question is whether \(c_R\) is already an exact target macro-law. If it is, unchanged reuse is justified. If it is not, the old label has merged target states that the changed system requires to be distinguished.

## 4. Exact portability and its local obstruction

### 4.1 Operational portability criterion

The carried target partition is exact if and only if, inside every carried fiber:

1. current target outputs are constant;
2. legal target-action rows are constant; and
3. successors under each common legal action occupy the same carried fiber.

Equivalently, the inherited target labels themselves form an exact operational quotient.

The criterion separates three ways an inherited category can fail:

- **output failure:** states with one inherited label already differ in the current target response;
- **availability failure:** one state admits a target action that another state in the same inherited fiber does not;
- **successor failure:** a shared action sends states in one inherited fiber to different inherited successor labels.

Target-only actions are especially revealing. An action absent from the source can expose a distinction that the source law legitimately ignored. In MLTR this is not optimized as a new open-grammar minimum. It is a test of whether one fixed inherited law remains closed under the target operation.

### 4.2 Finite witness of failure

If portability fails, it has a local operational witness. Two target states lie in one inherited fiber but differ in current output, legal-action row, or successor inherited label. More generally, a newly legal finite future word can return different target traces from two states the inherited law merged.

The obstruction pair identifies exactly where the old semantic interface breaks. It is more informative than a global statement that model transfer is poor: it names the inherited fiber and target operation responsible for failure.

Passing this test does not establish empirical transferability. Parameters, observation error, and model misspecification can still cause predictive failure. MLTR isolates a prior structural condition: whether the inherited macrostate could support a well-defined target law even with perfect knowledge of the declared finite systems.

## 5. Unique coarsest source-relative repair

When the carried partition is not exact, start from

\[
P_0=c_R.
\]

Given a current partition \(P_n\), split states inside one \(P_n\)-block whenever they differ in:

1. current output;
2. legal-action row; or
3. the \(P_n\)-block of a successor under a shared legal action.

This gives a monotone sequence

\[
P_0\preceq P_1\preceq P_2\preceq\cdots
\]

that never merges inherited source labels. Finiteness guarantees termination at a fixed point \(P_\infty\).

### Theorem 1 — relative exact refinement

\[
\boxed{
P_\infty
\text{ is the unique coarsest exact target interface that refines }c_R.
}
\]

Exactness follows because no fixed-point block contains output, legal-row, or successor-block disagreement. Minimality follows by induction: every exact target interface refining the inherited labels must already separate every pair split by each refinement round and therefore must refine the fixed point.

The generic refinement algorithm is standard substrate. The substantive result is the admissible set and its interpretation. The fixed point is minimal **relative to inherited source semantics**. It adds only distinctions forced by target outputs, actions, or successors while preserving every old merge that remains operationally valid.

This gives a canonical answer to the management question “what must be added to the old monitoring variable?” If one ecological coordinate is sufficient to separate the obstruction fibers, the repair requires that coordinate and no arbitrary target detail beyond it. If multiple response distinctions are independently exposed, the repaired interface grows accordingly.

## 6. Transport defect

Let

\[
Q_T^{\min}=P_\infty
\]

be the repaired target macrostate set. Define the additional number of macrostates

\[
\Delta_{\#}
=|Q_T^{\min}|-|Q_S|
\]

and the change in exact description length

\[
\Delta_K
=\log_2|Q_T^{\min}|-
\log_2|Q_S|.
\]

A zero defect means that the carried partition is already exact. A positive defect measures the minimum loss of compression required to keep the inherited law operational in the target.

The defect is relative. It is not a universal distance between ecosystems, a financial restoration cost, a sampling-effort estimate, or proof that no smaller target-only quotient exists.

### 6.1 Accumulating binary family

For every \(m\), consider a source law with two labels, `low` and `high`. The source permits only `reset`. The target contains one low state for every vector

\[
(b_1,\ldots,b_m)
\in\{0,1\}^m
\]

and one high state. A target-only action `probe_i` sends a low vector to the high state exactly when \(b_i=1\).

All binary vectors inherit the one source label `low`, but the target probes distinguish every pair. Therefore

\[
|Q_S|=2,
\qquad
|Q_T^{\min}|=2^m+1,
\]

so

\[
\boxed{
\Delta_{\#}=2^m-1,
\qquad
\Delta_K=\log_2(2^m+1)-1.
}
\]

The witness shows that one inherited fiber can require a rapidly growing repair when the target exposes independently varying response capacities. It uses a growing target probe alphabet and is not offered as an empirical scaling law or a constant-alphabet result. That boundary distinguishes it from CCOC's fixed-alphabet bounded-local construction.

## 7. Multiple replacement histories

A single source–target relation is often not enough. Similar terminal communities may be reachable through different sequences of extinction, colonization, restoration, or rewiring. The terminal configuration may be the same while the inherited meaning carried from the source differs by route.

Represent replacement possibilities as a rooted finite directed acyclic graph. Each edge carries a declared total relation. A root-to-terminal path \(p\) induces a carried terminal map

\[
c_p:X_T\to Q_S
\]

when its composed relation is root-fiber-label-consistent.

### 7.1 Path-label coherence

The replacement graph is path-label coherent at the terminal stage when every declared root-to-terminal path carries the same source label to every terminal state:

\[
\boxed{
c_p(t)=c_{p'}(t)
\quad
\text{for all terminal states }t
\text{ and all paths }p,p'.}
\]

### Theorem 2 — route-independent repair

If path-label coherence holds, then the carried terminal partition is independent of route. Because relative exact refinement is a deterministic function of that partition and the terminal controlled system, the unique repair and both transport-defect measures are also route independent.

The condition is doing real work. Total replacement relations alone do not guarantee route-independent meaning. A boundary diamond can carry labels \((0,1)\) along one path and \((1,0)\) along another. In that case there is no single route-free carried map that preserves both histories.

### 7.2 Minimum history augmentation

When path coherence fails, do not automatically store the complete ecological history. Group paths by equality of their entire carried terminal maps. The canonical history modes are

\[
H_{\min}
=
\{c_p:p\text{ is a declared root-to-terminal path}\}.
\]

### Theorem 3 — minimum history context

\[
\boxed{
|H_{\min}|=
\bigl|\{c_p\}\bigr|
}
\]

is the smallest number of immutable history modes capable of representing every declared path-specific carried map.

Different carried maps must occupy different modes because at least one terminal state receives incompatible source labels. One mode per distinct map attains the bound.

Create one immutable terminal copy for each history mode and retain the carried labels appropriate to that mode. Relative exact refinement on this history-sliced system yields the coarsest exact history-aware repair. It may merge history slices again when their inherited labels and all future responses are indistinguishable.

The theory therefore does not say that history always belongs in ecological state. History is retained only when different declared histories carry different operational meanings that cannot otherwise be represented.

In the two-route boundary witness,

\[
c_{p_1}=(0,1),
\qquad
c_{p_2}=(1,0),
\]

so two history modes are necessary and sufficient. The augmented four-state witness then refines to four exact blocks. The raw history-mode cost and final exact-interface repair are distinct quantities.

## 8. Plant–pollinator turnover and restoration priority

A finite plant–pollinator witness illustrates why source-relative repair can change a decision.

Suppose the source system classifies configurations into two functional macrostates: `low service` and `high service`. The classification is exact under the source pollinator community and source management actions. After pollinator turnover, the target system contains three configurations. Two inherit `low service`; one inherits `high service`. The carried target labels are therefore

\[
(0,0,1).
\]

The two low configurations are currently similar under the inherited output, but they differ in substitute-pollinator response capacity. A target-only restoration action can raise one low configuration to the high state while leaving the other low. The inherited `low` fiber is therefore not exact for the target management grammar.

Relative exact refinement splits only that fiber:

\[
(0,0,1)
\longrightarrow
(0,1,2).
\]

The repaired distinction records substitute-pollinator response capacity. It is not a new functional classification invented independently of the source law; it is the minimum target distinction required to preserve the source meaning while supporting the newly relevant action.

The management consequence can be a restoration-priority reversal. Under the inherited binary label, two low-service sites appear equivalent and a programme may prioritize them using cost, location, or another secondary criterion. Under the repaired law, one site is intervention-responsive and the other is not under the declared action. The site expected to cross into the high-service class becomes the priority if functional recovery is the target.

This example is finite and diagnostic. It does not estimate a natural pollinator-turnover relation, identify substitute taxa, or assert deterministic restoration. Its role is to show how unchanged current labels can hide a target response that alters a management ranking, and how the theorem returns the least additional ecological variable needed to repair that decision interface.

## 9. Relation to neighboring theory

### 9.1 Lumpability and bisimulation

Classical lumpability asks whether an aggregation is exact within a fixed process (Kemeny and Snell 1960; Feret et al. 2012). Bisimulation and partition-refinement theory characterize behaviorally equivalent states and coarsest quotients (Milner 1989; Larsen and Skou 1991; Paige and Tarjan 1987). MLTR uses the same exactness and refinement substrate.

Its chapter-level contribution is not another generic quotient algorithm. It is the source-relative problem: an accepted partition is carried through a declared non-nested replacement, and every repair must preserve its inherited labels. This constraint defines the admissible target set, makes the minimal repair canonical, and gives the transport defect meaning.

### 9.2 Causal and statistical transportability

Causal transportability asks when conclusions can be transferred across populations or environments (Pearl and Bareinboim 2014). MLTR does not infer a transport relation or estimate causal effects. It asks a prior structural question conditional on a declared relation: can the inherited macrostate interface define target outputs, legal actions, and successors at all?

Passing the MLTR audit does not guarantee empirical external validity. Failing it means that no parameter refit inside the unchanged inherited partition can make the target macro dynamics exact.

### 9.3 Resilience and adaptive management

Resilience and regime-shift theory motivate many ecological macrostates, while adaptive management revises policies as states and evidence change (Holling 1973, 1978; Walters 1986; Scheffer et al. 2001). MLTR does not redefine resilience or optimize policies. It audits whether the state variable supplied to those analyses retains operational meaning after structural replacement and identifies the minimum monitoring repair when it does not.

### 9.4 Boundary from CCOC

CCOC holds one controlled plant fixed and compares exact interfaces optimized under restricted and open future grammars. MLTR may include newly legal target actions, but one source partition is fixed first and target repair is constrained to refine its carried labels. CCOC's minimum-interface gap and MLTR's transport defect are therefore different quantities.

The distinction is essential. If the inherited source labels are abandoned, MLTR loses its semantic-repair problem. If closed interfaces are not independently optimized, CCOC loses its cross-grammar comparison.

## 10. Ecological implications

MLTR yields four practical distinctions.

First, **unchanged labels and unchanged label counts are not enough**. A three-state source and a three-state target do not share one macro-law unless outputs, action meanings, and successor labels align.

Second, **failure can be localized**. An obstruction pair and action identify which inherited fiber no longer supports the target prediction.

Third, **repair can be minimal rather than wholesale**. Monitoring need add only variables that separate response-distinct states inside the failed inherited fibers.

Fourth, **history is conditional**. Different replacement routes require explicit context only when they carry different terminal label maps. The minimum history state records equivalence classes of operational meanings, not every event in the ecological past.

These conclusions make structural replacement auditable. They do not tell field scientists which relation or history is true. That is an evidence and causal-learning problem developed later in the dissertation.

## 11. Limits and transition

The current theory is finite, deterministic, exact, and conditional on declared source and target systems, replacement relations, action grammars, and histories. It does not infer those objects from observations, quantify approximate repair under stochastic uncertainty, or prove that a repaired model predicts a natural system.

The transport defect is relative to an inherited source law. It is not a universal ecological distance or a claim that old semantics should always be preserved. In some applications abandoning the source classification may be preferable; MLTR makes that choice explicit by distinguishing repair from redesign.

This chapter has addressed system replacement while treating the relevant target dynamics as declared. A further problem remains. Even after source and target state spaces are aligned, several candidate mechanisms may generate the same visible state and disagree under future interventions. Then the question is no longer whether one inherited law transports through replacement, but whether any candidate-independent deterministic law can be reported honestly. Chapter 4 develops that mechanism-robustness problem.

## References

Feret J, Henzinger TA, Koeppl H, Petrov T (2012) Lumpability abstractions of rule-based systems. *Theoretical Computer Science* 431:137–164. https://doi.org/10.1016/j.tcs.2011.12.059

Holling CS (1973) Resilience and stability of ecological systems. *Annual Review of Ecology and Systematics* 4:1–23. https://doi.org/10.1146/annurev.es.04.110173.000245

Holling CS (ed) (1978) *Adaptive Environmental Assessment and Management*. Wiley, Chichester.

Kemeny JG, Snell JL (1960) *Finite Markov Chains*. Van Nostrand, Princeton.

Larsen KG, Skou A (1991) Bisimulation through probabilistic testing. *Information and Computation* 94:1–28. https://doi.org/10.1016/0890-5401(91)90030-6

Milner R (1989) *Communication and Concurrency*. Prentice Hall, New York.

Paige R, Tarjan RE (1987) Three partition refinement algorithms. *SIAM Journal on Computing* 16:973–989. https://doi.org/10.1137/0216062

Pearl J, Bareinboim E (2014) External validity: from do-calculus to transportability across populations. *Statistical Science* 29:579–595. https://doi.org/10.1214/14-STS486

Scheffer M, Carpenter S, Foley JA, Folke C, Walker B (2001) Catastrophic shifts in ecosystems. *Nature* 413:591–596. https://doi.org/10.1038/35098000

Walters CJ (1986) *Adaptive Management of Renewable Resources*. Macmillan, New York.
