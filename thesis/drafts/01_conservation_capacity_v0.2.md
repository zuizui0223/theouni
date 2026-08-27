<!-- draft-id: chapter:1:v0.2 -->
# Chapter 1 — When Conservation Capacity Outgrows Conservation Knowledge

> **Draft status:** dissertation-adapted v0.2. The source theorem, proof, executable witness, and submission manuscript remain owned by `zuizui0223/crest`.

## 1. The conservation paradox

New management options are normally treated as gains. A barrier can be removed, a degraded population can be translocated, an invasive species can be targeted, a wetland can be rewetted, or a lake can be treated through an intervention that was previously unavailable. In each case the management repertoire expands, and ecological futures that were once unreachable may become feasible.

That gain can have an overlooked epistemic consequence. A new action can expose differences among ecosystems that did not matter under the old repertoire. Once those differences change the expected result of an admissible action, a state description that previously grouped the systems together may no longer be adequate. The ecosystem need not have changed yet. The action need not have been applied. The scientific responsibility has changed because the programme now needs to predict a larger family of counterfactual responses.

The resulting asymmetry is the chapter's central claim:

\[
\boxed{
\textbf{conservation capacity can outgrow conservation knowledge.}
}
\]

The claim is not simply that better management sometimes requires more data. It is a statement about scale. A small increase in what can be done need not imply a small increase in the ecological distinctions that monitoring must resolve. The chapter develops an exact finite construction in which management capability grows by one world while the information required to represent a retained present slice grows by an arbitrary number of bits.

### 1.1 Why the scale question matters in practice

Restoration monitoring is often budgeted through quantities that are readily available before the full response problem is known: total project cost, construction cost, restored area, number of sites, or a fixed monitoring duration. Such heuristics can be administratively necessary. A U.S. Environmental Protection Agency wetland-restoration valuation case study, for example, calculated monitoring as five percent of the combined land-acquisition, transaction, restoration-action, and maintenance costs (U.S. EPA 2002). Historical restoration projects reviewed by the National Academies had monitoring costs averaging thirteen percent of total project cost, but ranging from three to sixty-seven percent (National Academies 2017). The range itself shows how weakly one scalar project-size measure determines actual monitoring burden.

CREST does not claim that a percentage-based budgeting rule is irrational or that project cost should never influence monitoring resources. Nor does it interpret those agencies as asserting a theorem that project size determines epistemic sufficiency. It draws a narrower boundary:

> **A scale-based budget rule cannot, by itself, certify that the resulting monitoring resolves every distinction required by the management problem.**

Project cost, restored area, or number of newly feasible actions can be budget variables. They are not universal epistemic bounds. The theorem below shows why additional ecological structure is required before any such bound can be justified.

## 2. From the reuse problem to a state problem

The General Introduction framed the dissertation around reuse: when may a representation earned for one scientific task be used for another? This chapter studies one specific transition. The original task supports a restricted management repertoire. The revised task admits a new action. The question is whether the old ecological state remains adequate.

Let \(\Omega\) be a declared set of possible ecological worlds. A world contains whatever history, present configuration, latent mechanism, and future-response structure the task requires. CREST does not identify a world with a measured snapshot. Measurements provide access to worlds; the state specifies which world differences the scientific responsibility must preserve.

Write the responsibility schematically as

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,D;T),
\]

where \(\Gamma\) specifies contemplated future operations, \(\mathcal H\) inherited or historical meanings that must remain coherent, \(\Theta\) retained mechanism or response alternatives, \(D\) the evidence and reliability architecture, and \(T\) the report or decision target. Two worlds may occupy the same ecological state only while they are interchangeable for the work assigned by \(\mathcal C\).

The corresponding quotient map is

\[
q_{\mathcal C}:\Omega\to Q_{\mathcal C}.
\]

A merge is sound when every required response is constant inside each fiber of \(q_{\mathcal C}\). The state is therefore not a measurement vector or a complete microdescription. It is a response-preserving equivalence class for a declared task.

This contract relativity is constrained rather than arbitrary. The intervention family and target must be specified independently of the preferred partition; the candidate worlds must share a non-vacuous domain; and a proposed merge must have a failure condition. If two merged worlds respond differently to an intervention that the state is required to support, the merge fails regardless of convenience.

The broader philosophical background—abstraction, idealization, multiple realization, and adequacy-for-purpose—was established in the General Introduction. This chapter uses that background rather than repeating it. Its distinctive question is quantitative: when one management capability is added, how much additional state resolution can become necessary?

## 3. A shallow-lake worked case

Shallow-lake restoration makes the state question concrete. Reduced external nutrient loading can improve water quality, but recovery may be delayed by internal phosphorus loading, and turbid conditions can be stabilized by food-web and macrophyte feedbacks (Scheffer et al. 2001; Jeppesen et al. 2005; Søndergaard et al. 2007). These mechanisms need not define two natural kinds of lake. They provide two possible worlds that can agree under one monitoring target and disagree under another.

Consider three finite worlds:

- \(S_w\): a currently turbid lake in which a mobile sediment-phosphorus legacy sustains internal loading;
- \(F_w\): a currently turbid lake in which fish-community structure and failed macrophyte recovery sustain the turbid state;
- \(C\): a recovered clear-water world.

Let the available actions be

\[
L=\text{continue external-load reduction},
\qquad
S=\text{sediment-focused treatment},
\qquad
F=\text{food-web/macrophyte intervention}.
\]

An illustrative response table is:

| present world | current output | \(L\) | \(S\) | \(F\) |
|---|---|---|---|---|
| sediment legacy \(S_w\) | turbid | \(S_w\) | \(C\) | \(S_w\) |
| food-web feedback \(F_w\) | turbid | \(F_w\) | \(F_w\) | \(C\) |
| recovered \(C\) | clear | \(C\) | \(C\) | \(C\) |

The table is deliberately schematic. It represents distinct restoration channels supported by the lake literature; it does not assign empirical transition probabilities or claim deterministic recovery in real lakes.

### 3.1 Current-status reporting

For the target

> is the lake currently turbid or clear?

\(S_w\) and \(F_w\) are interchangeable. The partition

\[
\{S_w,F_w\}\mid\{C\}
\]

is sufficient. A routine water-column observation can license the target even though it does not identify the latent restoration mechanism.

### 3.2 Intervention choice

Now change the scientific responsibility:

> which supplementary restoration channel is expected to reach the clear-water world?

The old turbid fiber is no longer sound. The two worlds disagree under both supplementary actions, and the least exact partition becomes

\[
\{S_w\}\mid\{F_w\}\mid\{C\}.
\]

No physical change is needed at the moment the management programme admits the two intervention channels. What changes is the counterfactual information that the state must preserve.

### 3.3 Evidence does not automatically follow the required refinement

Suppose routine monitoring still records only water-column status. Its evidence partition remains

\[
E_{\mathrm{routine}}=
\{S_w,F_w\}\mid\{C\}.
\]

That evidence is adequate for current-status reporting and inadequate for selecting the mechanism-specific intervention. The earlier record has not become false. It supports a coarser claim than the new responsibility requires.

Measurements of sediment phosphorus, fish-community structure, or macrophyte recovery may refine the evidence toward the needed distinction. Replicating the same aggregate water-column channel may not. The limiting resource can therefore be measurement type rather than sample size.

The example yields the separation

\[
\boxed{
\text{required state}
\neq
\text{identified state}
\neq
\text{reportable target}.
}
\]

A coarse target can remain reportable even when the full intervention-response state is unresolved.

## 4. Finite CREST architecture

The worked case has only three worlds. CREST gives the same logic a finite general form.

### 4.1 Admissible carrier

Different scientific responsibilities do not automatically share a coherent world set. CREST therefore separates world feasibility from state construction. Under a controlled responsibility, uncontrollable moves must remain safe and at least one admissible control must be available. Descending iteration produces the greatest robust controlled-invariant carrier \(K^*\).

An empty or coverage-incomplete carrier cannot be repaired by splitting state classes more finely. That is a failure of the declared world set or contract, not a resolution problem.

### 4.2 Least-information adequate state

On a finite admissible carrier \(U\), let \(B\) be a baseline partition. Implemented responsibilities are represented by monotone, inflationary, idempotent refinement closures

\[
C_\Gamma,
\qquad
C_{\mathcal H},
\qquad
C_\Theta,
\qquad
C_{D,T}.
\]

The common closure

\[
\boxed{
J=(C_\Gamma\vee C_{\mathcal H}\vee C_\Theta\vee C_{D,T})(B)
}
\]

is, under the declared assumptions, the unique coarsest partition satisfying those responsibilities. The generic closure and partition machinery is classical. Its role is to identify the resolution requirement without retaining distinctions irrelevant to the task.

### 4.3 Evidence licensing

Let \(E_D\) be the reliability-qualified evidence partition. Full deterministic state reporting is licensed exactly when

\[
J\preceq E_D.
\]

When this fails, the required distinction still exists in the model contract, but the evidence does not locate the true world in one required-state block. A target can nevertheless remain deterministic if it factors through the evidence partition.

The architecture therefore distinguishes three sources of failure: the relevant worlds may not form one admissible carrier; the proposed state may merge response-distinct worlds; or the evidence may fail to identify the state that the task requires.

## 5. Capability–resolution divergence

Expanding the management repertoire can enlarge the viable carrier and refine the required state. The nontrivial question is whether the two increases must be comparable.

### Theorem 1 — one action, one viable world, arbitrary state debt

For every integer \(m\ge1\), there exists a finite deterministic controlled system in which admitting one controllable action `probe` gives

\[
\boxed{
\Delta|K^*|=1,
\qquad
\Delta K_{U_0}=m.
}
\]

Here \(U_0\) is a retained present slice and

\[
K_{U_0}(J)=\log_2|J\restriction_{U_0}|
\]

is the exact state complexity on that slice.

Before the action expansion, \(U_0\) contains \(2^m\) worlds indexed by binary addresses. Under the old action `hold`, all return the same response and can occupy one state. After `probe` is admitted, repeated use of that one action reads one binary coordinate at a time. Every pair of addresses differs at some coordinate, so some finite probe word separates every pair. The least exact state on \(U_0\) therefore refines from one block to \(2^m\) blocks.

The same connected response graph contains one additional world, `fragile`. It is not in the old robust controlled carrier because no old action keeps it safe. Under the expanded repertoire, `probe` sends it to a safe sink. The carrier therefore grows by exactly one world. The readout and rescue effects are produced by the same action in one connected construction rather than by unrelated disjoint gadgets.

Hold the evidence on \(U_0\) fixed as one record class. Before expansion, that evidence identifies the single required state. After expansion, it merges \(2^m\) required states and creates exactly \(m\) bits of monitoring-resolution debt. Full-state licensing changes from yes to no. A target constant on \(U_0\) remains reportable.

The same family therefore realizes

\[
\boxed{
\Delta|K^*|=1,
\quad
\Delta K_{U_0}=m,
\quad
D_{U_0}:0\to m,
\quad
\text{full state: yes}\to\text{no},
\quad
\text{target: yes}\to\text{yes}.
}
\]

### Corollary 1 — no carrier-gain-only upper bound

There is no universal finite function \(f\) of carrier-size gain alone such that

\[
\Delta K_{U_0}\le f(\Delta|K^*|)
\]

for every system in the declared class. The family fixes \(\Delta|K^*|=1\) while \(m\) is arbitrary.

This is an extremal existence theorem. It does not predict exponential state growth in typical ecosystems. It forbids a universal inference in the absence of additional ecological structure.

## 6. What the theorem forbids

### 6.1 Intervention scale is not an epistemic bound

The strongest conservation implication is negative:

\[
\boxed{
\text{small capability gain}
\not\Rightarrow
\text{small monitoring-resolution burden}.
}
\]

A budget proportional to project cost or area may be administratively defensible. It cannot, without a response model, certify that all distinctions required by the new action repertoire have been resolved. The appropriate monitoring level depends on how the new actions split worlds previously grouped by the old state, not merely on the cost, area, or count of interventions.

This conclusion is compatible with the wide variation observed in restoration monitoring costs. It does not explain that variation by itself, and it does not imply that arbitrary spending is scientifically necessary. It says that no carrier-gain-only rule can guarantee adequacy across all systems.

### 6.2 New capability can invalidate old state knowledge before implementation

An intervention can change the required state as soon as it becomes part of the responsibility. Assisted migration, corridor construction, targeted removal, rewetting, or food-web manipulation can make dormant differences operational even before an action is executed. The representational change comes from a new counterfactual question, not from a prior physical alteration of the system.

### 6.3 Decision sufficiency is not full-state knowledge

The construction preserves a coarse target while full-state identification fails. Consequently,

\[
\boxed{
\text{decision-safe target knowledge}
\not\Rightarrow
\text{full ecological-state knowledge}.
}
\]

This is not necessarily a defect. Conservation decisions often require less information than complete state identification. The distinction matters because successful decision support should not be reported as comprehensive ecosystem understanding.

### 6.4 Measurement repair can require a new channel

If the newly exposed difference concerns mechanism or response type, more samples of the old aggregate variable may leave the worlds merged. Monitoring repair may require sediment chemistry rather than additional water-column replicates, demographic source information rather than more occupancy observations, or interaction measurements rather than species counts.

The theorem does not specify the correct new measurement. It identifies the fiber that must be split. CED and RACH, developed later in the dissertation, ask whether an observation architecture can reliably support that split and which observation is valuable for the relevant epistemic objective.

### 6.5 Conservation state is partly indexed by the feasible action set

Labels such as `recoverable`, `restoration-ready`, or `managed stable` are not properties of a snapshot alone when their scientific meaning includes intervention response. Two systems can occupy one state under one management repertoire and require different states under another. This does not make ecological reality observer-created. The response differences constrain the partition; management determines which response family the state is asked to preserve.

The resulting operational principle is:

\[
\boxed{
\text{when the management repertoire changes, state adequacy must be re-audited.}
}
\]

## 7. Boundary from existing abstraction theory and from CCOC

State/action coupling, predictive-state representation, causal abstraction, POMDP state choice, and purpose-relative model adequacy all provide established foundations (Littman et al. 2002; Singh et al. 2004; Nicol and Chadès 2012; Beckers and Halpern 2019; Konidaris 2019; Parker 2020). CREST does not claim to invent action-sensitive state or generic quotient construction.

Its chapter-level contribution is the connected scale separation among four quantities:

1. gain in robustly controllable worlds;
2. required state complexity on a retained present slice;
3. evidence or monitoring debt;
4. reportability of a coarser target.

One action produces a fixed gain in the first quantity and arbitrary growth in the second and third while leaving the fourth unchanged. The result therefore says more than that a different task can induce a different state partition.

Chapter 2 develops the closest companion result, but the quantified objects remain different. CCOC compares interfaces optimized separately under fixed closed future grammars with the exact interface required when those futures are opened jointly. CREST compares capability/carrier gain with state and evidence burden in one management contract. CCOC explains how open future addressability can expose hidden distinctions; it is not a corollary of the conservation theorem, and the CREST theorem is not merely CCOC with management labels.

## 8. Limits and transition

The current result is finite, deterministic, exact, and existential. It does not establish a universal continuous or stochastic theory, predict typical effect sizes, infer the correct management grammar from data, or validate the shallow-lake partition empirically. The official budgeting examples demonstrate that scale-based cost heuristics exist; they do not prove that any particular programme believed monitoring adequacy was mathematically bounded by project scale.

The theorem also diagnoses **that** a previous state must split, not automatically **how** field scientists should measure the split. That downstream problem requires an evidence model, failure architecture, and explicit observational candidates.

This chapter began with a practical paradox: doing more can require knowing more. It ends with a structural question. How can one newly legal action reveal an arbitrarily large family of distinctions that every previous closed context safely merged? Chapter 2 answers that question at the level of exact response interfaces under open future grammars.

## References

Beckers S, Halpern JY (2019) Abstracting causal models. *Proceedings of the AAAI Conference on Artificial Intelligence* 33:2678–2685. https://doi.org/10.1609/aaai.v33i01.33012678

Chadès I, Pascal LV, Nicol S, Fletcher CS, Ferrer-Mestres J (2021) A primer on partially observable Markov decision processes (POMDPs). *Methods in Ecology and Evolution* 12:2058–2072. https://doi.org/10.1111/2041-210X.13692

Jeppesen E, Søndergaard M, Jensen JP, Havens KE, Anneville O, Carvalho L, Coveney MF, Deneke R, Dokulil MT, Foy B et al (2005) Lake responses to reduced nutrient loading—an analysis of contemporary long-term data from 35 case studies. *Freshwater Biology* 50:1747–1771. https://doi.org/10.1111/j.1365-2427.2005.01415.x

Konidaris G (2019) On the necessity of abstraction. *Current Opinion in Behavioral Sciences* 29:1–7. https://doi.org/10.1016/j.cobeha.2018.11.005

Littman ML, Sutton RS, Singh S (2002) Predictive representations of state. *Advances in Neural Information Processing Systems* 14:1555–1561.

National Academies of Sciences, Engineering, and Medicine (2017) *Effective Monitoring to Evaluate Ecological Restoration in the Gulf of Mexico*. National Academies Press, Washington, DC. https://doi.org/10.17226/23476

Nicol S, Chadès I (2012) Which states matter? An application of an intelligent discretization method to solve a continuous POMDP in conservation biology. *PLoS ONE* 7:e28993. https://doi.org/10.1371/journal.pone.0028993

Parker WS (2020) Model evaluation: an adequacy-for-purpose view. *Philosophy of Science* 87:457–477. https://doi.org/10.1086/708691

Scheffer M, Carpenter S, Foley JA, Folke C, Walker B (2001) Catastrophic shifts in ecosystems. *Nature* 413:591–596. https://doi.org/10.1038/35098000

Singh S, James MR, Rudary MR (2004) Predictive state representations: a new theory for modeling dynamical systems. In: *Proceedings of the 20th Conference on Uncertainty in Artificial Intelligence*, pp 512–519.

Søndergaard M, Jeppesen E, Lauridsen TL, Skov C, Van Nes EH, Roijackers R, Lammens E, Portielje R (2007) Lake restoration: successes, failures and long-term effects. *Journal of Applied Ecology* 44:1095–1105. https://doi.org/10.1111/j.1365-2664.2007.01363.x

U.S. Environmental Protection Agency (2002) *Case Study Analysis for the Proposed Section 316(b) Phase II Existing Facilities Rule, Parts H–I*. U.S. Environmental Protection Agency, Washington, DC.
