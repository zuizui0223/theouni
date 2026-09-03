<!-- draft-id: chapter:5:v0.1 -->
# 未来を開くと、記憶が要る

*English working title: Opening the Future Requires Memory*

> **Draft status:** source-bounded v0.1 from CCOC snapshot `96d823309ce04affb33446f1996aedf0a163a039`. The chapter concerns exact response-interface memory under declared finite future grammars. Its central result is a bounded-local extremal theorem showing that one fixed-size grammar opening can expose arbitrarily large exact response memory while local/static resources and the focal–exterior physical cut remain fixed. It does not claim that real ecological corridors or islands realize the extremal construction.

## 1. “More possible futures require more memory” is too weak

It is easy to say that a model needs more memory when more future situations are considered. That statement is almost definitional if both the number of states and the number of future queries are allowed to grow without restriction. It cannot carry this chapter.

The motivating forbidden inference is

> **物理的境界が狭い ⇒ 必要な因果記憶も小さい**

but the scientific question is stronger than merely denying that shortcut:

> **Can exact causal-interface memory become arbitrarily large even when the physical cut is one edge, local degree and alphabets remain bounded, the primitive action alphabet is fixed, and the legal future grammar changes by only one transition?**

CCOC answers yes with an explicit all-`m` construction. [C0]

This matters because ecological models are often modularized according to present spatial or interaction boundaries. A narrow corridor, one focal–exterior connection, a sparse network, or a small current interface can encourage the intuition that only a correspondingly small summary should be required at that boundary. That intuition is safe only if the future responsibility represented by the interface is also controlled. Once newly legal future actions can interrogate distinctions that were previously dormant, physical narrowness alone does not bound exact response memory.

The chapter therefore separates two quantities:

1. **static/local physical resources**: cut width, degree, local alphabets, primitive actions and local update radius;
2. **future-response responsibility**: which action words are legal and which resulting traces the interface must preserve exactly.

The theorem keeps the first class uniformly bounded while making the second expose an arbitrary number of previously irrelevant distinctions.

## 2. Exact interface means equality of all legal future responses

Consider a finite deterministic controlled system with a declared legal future grammar. Two present states are equivalent when every legal finite future word produces the same output trace from the two states. The resulting response quotient is the coarsest exact deterministic interface for that declared grammar. [C1]

This definition is not the contribution by itself. Finite-state minimization, quotient dynamics and response equivalence have extensive classical relatives. CCOC uses that substrate to ask a cross-grammar question:

> if a small quotient is exact under a restricted legal future grammar, what can be inferred about the size of an exact quotient after the legal grammar is expanded?

Nothing useful follows from the old quotient size alone. The same physical system may hide distinctions that no old legal word could expose. When the grammar changes, those distinctions can become observable without any change in the physical network or its local transition rule.

This is why “state complexity” in this chapter is contract-relative. It is not a claim that the physical ecosystem acquires metaphysical memory when a scientist changes a model. The required interface changes because the set of future responses the scientific representation promises to preserve has changed.

## 3. The fixed-regular construction keeps the resource budget constant

For every integer

\[
m\ge1,
\]

CCOC constructs a finite deterministic synchronous controlled network `N_m`. The comparison domain contains one focal bit `y` and `m` exterior memory bits:

\[
D_m=\{0,1\}^{m+1}
=\{(y,b_1,\ldots,b_m)\}.
\]

The primitive action alphabet is fixed once and for all:

\[
A=\{0,1,\mathsf{fire},\mathsf{tick}\}.
\]

It does not grow with `m`. [C0]

The closed legal grammar allows only

\[
L_C=\{0,1,\mathsf{tick}\}^{*},
\]

while the open grammar is

\[
L_O=A^{*}.
\]

Operationally, opening the future adds the single previously illegal action `fire`. Both legal grammars are represented by one-state partial automata independent of `m`; the underlying network transition rule remains unchanged. [C0]

The interaction network is a tree. The focal node attaches to the entire exterior relay body through exactly one edge. Maximum degree is at most three. Node-state and message alphabets are bounded by constants independent of `m`, and updates are radius-one local. [C0]

Thus the theorem does **not** produce growing memory by quietly giving the system a wider boundary, an `m`-symbol action alphabet, unbounded local state, a growing port identifier or direct global access to every exterior coordinate. Those obvious routes are explicitly removed.

The question becomes whether one newly legal primitive action can nevertheless make every one of the `m` exterior distinctions relevant to exact future response.

## 4. Closed grammar: all exterior memory is response-invisible

Under the closed grammar, `fire` is illegal. Address actions may move a selector through the relay tree, but they do not create a pulse. `tick` only propagates an already existing pulse, and the construction starts pulse-free.

Therefore, under every closed legal word:

- all permanent exterior bits `b_j` remain unchanged;
- no exterior bit is transmitted to the focal output;
- the focal bit `y` remains the only response-relevant distinction on the comparison domain. [C0]

The proof is an induction on legal word length. Pulse absence is preserved by each closed action, so the output trace cannot depend on the exterior memory vector.

Consequently states with the same focal bit are response-equivalent under the closed grammar. The empty word distinguishes `y=0` from `y=1`, giving exactly

\[
\boxed{|P_C|=2,\qquad K_C=\log_2|P_C|=1.}
\]

This is already stronger than “the physical boundary is narrow.” It shows that the exact interface is genuinely one bit under **all** closed legal futures, even though the physical domain contains `m` additional stored bits.

Those exterior distinctions are not approximately ignored; they are exactly irrelevant to the declared closed response contract.

## 5. Opening one primitive action makes every exterior coordinate legally decodable

After `fire` becomes legal, each exterior leaf can be addressed by a finite left/right word. If leaf `j` has address `a_j` and depth `d_j`, CCOC defines a legal open word

\[
w_j=a_j\,\mathsf{fire}\,\mathsf{tick}^{d_j+1}.
\]

The address moves the selector to leaf `j`. `fire` copies permanent bit `b_j` into the pulse layer. The following ticks propagate the pulse through local parent edges until it reaches the focal root. The final focal output is therefore

\[
\operatorname{finaloutput}(s,w_j)=b_j.
\]

Every exterior coordinate is thus separately decodable by a legal open future word. [C0]

Take two distinct comparison states. If their focal bits differ, the current output distinguishes them. If their focal bits agree, then some exterior bit differs, and the corresponding word `w_j` distinguishes them. Hence no two distinct comparison states can remain in the same exact open response class.

The open quotient is therefore discrete:

\[
\boxed{|P_O|=2^{m+1},\qquad K_O=m+1.}
\]

The opening has created an exact interface gap

\[
\boxed{K_O-K_C=m.}
\]

The system's local resource constants did not grow. The legal grammar changed by one primitive transition. Yet the response memory forced by the future contract grows without bound as `m` increases.

That is the chapter's central result.

## 6. The `m`-bit gap is sharp, not merely large

The comparison domain contains `2^(m+1)` states. Starting from a two-class closed quotient, no exact refinement on that finite domain can require more than

\[
\log_2(2^{m+1})-\log_2 2=m
\]

additional bits.

The open construction attains exactly `m` additional bits. Therefore it reaches the absolute finite-domain capacity bound with equality. [C0]

This sharpness is important for the anti-obviousness argument. CCOC is not merely presenting one example where a future opening “increases complexity a lot.” It constructs a family whose opening exposes **all response information that was available to expose beyond the closed focal bit**.

Equivalently, if the focal bit is already supplied, an exact exterior label must distinguish all `2^m` exterior bit vectors. Fewer than `m` bits cannot do so. The lower bound is forced by legal decoder words and is attained by the full exterior response label.

The finite executable certificate checks this equality for supplied finite values of `m`; the quantified proof remains the analytic all-`m` argument. [C2]

## 7. There is no upper bound based only on the fixed local/static resources

Because the same resource constants work for every `m`, the extremal family gives a no-bound corollary.

Consider the class of systems with uniformly bounded:

- primitive action alphabet size;
- grammar-state count and one-transition closed/open edit;
- maximum graph degree;
- focal–exterior cut width;
- local node-state and message alphabets;
- local update radius.

Every `N_m` belongs to the same such resource class, but

\[
K_O(N_m)-K_C(N_m)=m.
\]

If there were a finite universal upper bound depending only on those static/local resource constants, choosing `m` larger than that bound would contradict the construction. Therefore

\[
\boxed{\text{no static-resource-only finite bound on exact interface inflation exists for this class}.}
\]

This is stronger than the chapter title. The conclusion is not merely “opening futures may require more memory.” It is:

> **physical cut width, bounded degree, bounded local alphabets, fixed primitive action vocabulary and a one-transition grammar edit do not jointly impose any finite universal bound on the newly required exact response memory.**

The missing quantity is the amount of dormant future-addressable distinction in the comparison domain.

## 8. Access remains local: the construction does not buy memory with instantaneous global queries

One possible objection is that the construction might hide a global oracle inside `fire`. It does not. Reading an exterior bit requires routing a selector to a leaf and propagating a pulse back through local edges.

For a midpoint-balanced relay tree, maximum leaf depth is

\[
\lceil\log_2m\rceil.
\]

The canonical read word has exact worst-case length

\[
\boxed{2\lceil\log_2m\rceil+2.}
\]

A separate causal-cone argument shows that exposing exponentially many exact response classes in bounded-degree, bounded-local-state radius-one systems requires at least logarithmic horizon order. Thus the relay's `Theta(log m)` access is order-optimal in that broader bounded-local class. [C0]

The theorem therefore keeps two ideas separate:

- memory burden can grow linearly in `m`;
- local time required to address one selected coordinate grows only logarithmically in `m`.

Neither comes from an unbounded direct port to the exterior.

## 9. The positive boundary: future expansion does not always destroy a compact law

An extremal counterexample alone would leave the chapter as a pathology catalogue. CCOC also states a positive sufficient condition for portability. [C3]

Suppose a nested sequence of finite controlled systems has finite stage maps into one common macro alphabet `Q`. Assume there is one common macro dynamics—same macro output, legal-action relation and macro successor rule—through which every stage factors. Require also that embeddings preserve macro labels: an old physical state retains the same macro meaning after extension.

Under those conditions, every stage realizes the same exact macro dynamics, and the nested composition carries one extension-portable macro-law. [C3]

The proof is by representative-independent factorization at each stage plus induction through the label-coherent embeddings. Old legal trajectories retain their macro traces at later stages.

This gives a constructive contrast:

- **negative side:** if newly legal futures can address distinctions hidden inside an old macrostate, exact interface memory can inflate without a local-resource bound;
- **positive side:** if all stages continue to factor through one common macro dynamics and embeddings preserve those labels, one finite macro-law remains portable.

The chapter therefore does not say “future opening always requires more memory.” It identifies why opening can be harmless in one family and maximally destructive to compression in another.

## 10. A local future-word witness diagnoses failure before the full lower bound is known

The positive theorem also makes a useful converse-style obstruction explicit. Suppose two states are merged by a proposed macrostate at an early stage, and their embedded images remain assigned the same macro label later. If a newly legal future word produces different traces from those two images, then that merge cannot belong to any exact coherent portable law. [C3]

This is a finite certificate:

- name the two previously merged states;
- name the later legal word;
- show the resulting traces differ.

One does not need to derive the full `m`-bit product lower bound to know that the old macrostate has failed. The witness locates the exact forgotten distinction that became future-relevant.

This diagnostic is ecologically interpretable. A new exposure, reconnection, species interaction, management action or habitat route can make two formerly equivalent conditions respond differently. At that point the old summary is no longer portable for the expanded responsibility, even if its label count looked adequate at every previous stage.

## 11. Why physical boundary and causal interface must remain separate concepts

A graph cut measures a static topological property. An exact response interface measures distinctions required to preserve all legal future responses. These quantities can correlate in particular models, but CCOC proves that one does not upper-bound the other under the declared finite class.

The one-edge focal/exterior cut remains one for every `m`, while the exact future-response information grows as `m`. [C0]

This distinction is relevant to ecological modularity. Spatial isolation, narrow corridors, trophic boundaries or weak present coupling can motivate useful decompositions. But a decomposition intended to support future interventions or compositions needs a **future-response** justification, not merely a current graph-separation justification.

The theorem does not imply that every real narrow corridor hides arbitrary information. That would require empirical identification of the states, actions and response grammar. The mathematical result only closes the inference from geometric narrowness alone to a universal causal-memory bound.

## 12. Relation to Chapter 4: changing the target and changing the legal future are different revisions

Chapter 4 asked whether several declared target responsibilities can share one scalar state. Chapter 5 asks a different question: even if one compact response state is sufficient under the current future grammar, will that same compression remain sufficient when new futures become legal?

The CCOC relay is not an eco-genetic fragmentation model. The Chapter 4 H3 crossing does not generate the Chapter 5 memory lower bound. The transition is a question handoff: target dependence motivates asking what happens when the responsibility itself expands along the future-action dimension. [TR]

TU-1 provides a useful downstream reading. If the old closed quotient has already been stored and the open contract later requires the discrete refinement, the earlier compression has forgotten distinctions needed for revision. But CCOC owns the theorem that creates the open/closed response gap; TU-1 only diagnoses revisability after that required refinement is declared.

## 13. What the chapter establishes

The chapter establishes, for the declared finite deterministic controlled class:

1. a fixed four-symbol primitive action alphabet and one-transition grammar opening can coexist with an exact response-interface gap of `m` bits for arbitrary `m`;
2. the physical network can remain a bounded-degree tree with one focal–exterior edge cut and bounded local alphabets;
3. the closed quotient is exactly two classes while the open quotient is exactly `2^(m+1)` classes;
4. the `m`-bit innovation attains the finite-domain upper bound and is therefore sharp;
5. no universal finite bound depending only on the listed static/local resource constants can upper-bound exact interface inflation;
6. local canonical access uses `Theta(log m)` horizon rather than an instantaneous global oracle;
7. a separate coherence theorem gives sufficient conditions under which a finite macro-law **does** remain portable across nested extension;
8. a newly legal future word separating two previously merged states is a concrete obstruction to exact portability.

The chapter does **not** establish that real ecological systems with narrow physical boundaries generally require large memory. It does not claim historical invention of finite-state minimization, sequential-machine compilation or generic quotient theory. It does not say every future expansion destroys portability. [C4]

The precise conclusion is:

> **A small present physical interface is not an exact upper bound on future-response memory. What controls portability is whether the expanded legal future continues to factor through the old macro meaning; when future actions make hidden distinctions addressable, interface burden can grow to the full finite-domain limit while local/static resources remain fixed.**

## 14. Transition: capability change is not the same as grammar change

Opening a legal future grammar changes which responses the representation must preserve. Chapter 6 moves to a different operation: expanding the set of controllable actions can change which worlds are viable under management and what present state must be distinguished to use that capability safely.

CCOC does not prove that a small **capability gain** creates a large monitoring burden. CREST owns that separate result. The handoff is therefore:

> **If one fixed-size opening of future legality can expose unbounded interface memory, can an apparently tiny gain in actual intervention capability likewise create an arbitrarily large state and evidence obligation?**

Chapter 6 answers that question with a connected finite family in which one new action adds exactly one viable world while creating `m` bits of present-state monitoring debt. [TR]

## Internal source keys

- **[C0]** CCOC `docs/fixed_regular_extremal_theorem_2026-08-13.md` — all-`m` fixed-grammar construction, closed/open quotient proof, sharpness, one-edge cut, local-resource bounds, no-bound corollary and query length.
- **[C1]** CCOC `docs/theorem_spine.md` and dynamic-interface substrate — exact legal-future response quotient and cross-grammar theorem ownership.
- **[C2]** CCOC `causal_model/extremal_open_composition.py` and `tests/test_extremal_open_composition.py` — finite executable certificates for supplied `m`; implementation guard, not replacement for the quantified proof.
- **[C3]** CCOC `docs/coherent_portable_macrolaw.md` — positive coherent portability theorem and newly legal future-word obstruction.
- **[C4]** CCOC theorem spine / manuscript claim boundaries — no empirical narrow-boundary claim and no historical firstness claim for classical substrate.
- **[TR]** `thesis/transition_recovery_matrix.json` — Chapter 4→5 and Chapter 5→6 are editorial question handoffs, not theorem implications.
