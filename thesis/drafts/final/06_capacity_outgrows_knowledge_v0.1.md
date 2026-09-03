<!-- draft-id: chapter:6:v0.1 -->
# 能力は知識を追い越す

*English working title: Capacity Can Outgrow Knowledge*

> **Draft status:** source-bounded v0.1 from CREST snapshot `2ff41e18cdbf100932813fbef9851078ec60413a`. The chapter concerns the separation between management capability, required present-state resolution, evidence adequacy, and target-only reportability in finite deterministic controlled systems. Its headline is a connected all-`m` no-bound theorem, not the generic observation that more interventions may require more information.

## 1. “More intervention requires more knowledge” is not yet a theorem

A management programme that gains new control options often needs new information. Stated at that level, the claim is intuitive and weak. If the intervention set grows arbitrarily, the state space grows arbitrarily, and monitoring is allowed to deteriorate arbitrarily, a large information burden is unsurprising.

The motivating forbidden inference is

> **介入の規模が小さい ⇒ 表現と監視の負担も小さい**

but the chapter asks a sharper question:

> **Can a capability expansion that adds exactly one controllable action and makes exactly one additional world viable nevertheless force an arbitrarily large refinement of the present state and arbitrarily large monitoring-resolution debt?**

CREST answers yes. For every integer `m>=1`, it constructs one connected finite system in which the same single new action produces simultaneously

\[
\Delta |K^*|=1
\]

at the viability gate and

\[
\Delta K_{U_0}=m\text{ bits}
\]

at the present-state gate, while unchanged evidence moves from fully adequate to `m` bits short of identifying the new required state. A coarse target can nevertheless remain exactly reportable. [R0]

The result therefore separates four questions that are often collapsed:

1. **What worlds are controllably viable?**
2. **What distinctions among present worlds are required by the expanded future responsibility?**
3. **Does current monitoring resolve those distinctions?**
4. **Does the particular requested target require all of them?**

A small change at the first gate does not impose a small change at the second or third.

## 2. Capability is represented by a controlled carrier, not by action count alone

Let a finite compatible world set carry a declared controllable action repertoire. A robust controlled carrier consists of worlds from which there exists a legal safe control choice keeping the system inside the carrier under the declared uncertainty/transition contract. CREST's controlled-carrier theorem identifies the greatest such carrier under its finite assumptions. [R1]

The size of the action alphabet by itself is not the measure of capability used in the headline comparison. The relevant capability consequence is which worlds become viable under safe control.

This distinction prevents an easy but misleading construction. One could add a new action that never changes viability and separately add an unrelated high-information readout gadget. That would prove that “one action” and “many bits” can coexist, but would not connect the intervention change to the same response structure.

The CREST family instead makes the construction connected: the repeated trajectories of the newly admitted `probe` action that expose the latent address also pass through the unique world that `probe` newly makes viable. [R0]

Even so, the theorem is careful about causation. It does not say the one-world carrier gain *causes* the `m`-bit state refinement. It proves that a fixed-size capability expansion can have a constant effect at one gate and an unbounded effect at another within one connected finite system.

## 3. Construction: one new `probe` action and an `m`-bit latent address

Fix `m>=1` and let

\[
X_m=\{0,1\}^m.
\]

For each address

\[
x=(x_1,\ldots,x_m)\in X_m,
\]

construct a chain of neutral present/readout states. The retained present slice is

\[
U_0=\{p_{x,0}:x\in X_m\},
\]

so `U_0` contains `2^m` worlds. [R0]

Use a fixed output alphabet with four symbols: `neutral`, `bit0`, `bit1`, and `done`. The old controllable repertoire contains only

\[
A_c^- = \{\mathsf{hold}\}.
\]

Every address-chain world and a safe sink `s` can self-loop safely under `hold`. A special world `r` has no safe old control and is therefore excluded from the greatest old robust carrier.

The expanded repertoire is

\[
A_c^+ = \{\mathsf{hold},\mathsf{probe}\}.
\]

Old `hold` transitions remain unchanged. Repeated `probe` operations move along the address chain, emit `bit0` or `bit1` according to the next coordinate of `x`, and eventually enter `r`; from `r`, the same `probe` action reaches safe sink `s`. [R0]

No action name or output symbol grows with `m`. The same newly admitted action both exposes the address and supplies the missing safe transition from `r`.

This is the core design that makes the cross-gate comparison nontrivial.

## 4. Carrier theorem: the capability gain is exactly one world

Under the old repertoire, every chain world and `s` has safe action `hold`, while `r` has no legal safe control. Therefore

\[
K_m^{*-}=W_m\setminus\{r\}.
\]

After `probe` is admitted,

\[
r\xrightarrow{\mathsf{probe}}s,
\]

so `r` becomes viable. Every previously viable world remains viable because the old safe `hold` action is unchanged. Hence

\[
K_m^{*+}=W_m=K_m^{*-}\cup\{r\}.
\]

Therefore

\[
\boxed{|K_m^{*+}|-|K_m^{*-}|=1.}
\]

for every `m`. [R0]

This fixes the capability side of the comparison. The family is not allowed to buy a large information burden by adding an increasing number of rescued worlds. The carrier gain remains one while `m` is free to grow.

## 5. Before expansion, the entire retained present slice is one exact future state

Under the old repertoire, every world in `U_0` has output `neutral` and self-loops under the only legal action `hold`. No old legal future can expose the address bits.

Therefore all `2^m` present worlds in `U_0` have the same complete legal future trace under the old contract. The coarsest exact future-sensitive state on that slice has one class:

\[
\boxed{|J_m^-\restriction_{U_0}|=1.}
\]

Using present-slice state complexity

\[
K_{U_0}(J)=\log_2|J\restriction_{U_0}|,
\]

we obtain

\[
K_{U_0}(J_m^-)=0.
\]

The old monitoring record can therefore be a single block on `U_0` and still identify the old required state exactly. [R0]

This mirrors Chapter 5 in one respect: distinctions can be physically present while irrelevant to the currently legal future responsibility. But Chapter 6 changes the controlled repertoire and viability structure, not merely a legal response grammar. The ownership and theorem are different.

## 6. After expansion, every address must become a distinct required present state

Take two different address vectors `x` and `y`. Let coordinate `j+1` be their first disagreement. Starting from `p_{x,0}` and `p_{y,0}`, the same repeated `probe` word reaches readout states reporting different binary outputs at the first differing coordinate. [R0]

Thus the two present worlds have different legal future response traces under the expanded repertoire. No exact future-sensitive state may merge them.

Because every pair of distinct address vectors differs somewhere,

\[
\boxed{|J_m^+\restriction_{U_0}|=2^m.}
\]

Hence

\[
K_{U_0}(J_m^+)=m
\]

and the exact present-slice state increase is

\[
\boxed{\Delta K_{U_0}=m.}
\]

The capability gain at the controlled-carrier gate remains exactly one world, while the least exact present representation on the retained slice gains arbitrary `m` bits.

The important quantity is not the number of action names or the number of newly viable worlds. It is the number of previously merged present worlds that the expanded future responsibility now requires us to distinguish.

## 7. Fixed monitoring moves from adequate to exactly `m` bits short

Now hold the evidence map fixed. Suppose all worlds in `U_0` produce the same current monitoring record. Under the old required state this one-block evidence is sufficient because the old state also has one block on `U_0`.

After action expansion, the required state has `2^m` blocks while evidence still has one. CREST defines a finite monitoring-resolution debt on the slice by the additional partition resolution needed for the evidence to identify the required state. For this construction,

\[
D_{U_0}(E,J_m^-)=0,
\]

whereas

\[
D_{U_0}(E,J_m^+)=m.
\]

Thus unchanged monitoring changes from fully adequate to exactly `m` bits deficient. [R0,R2]

This is stronger than saying that the new action “requires new monitoring.” It quantifies an arbitrarily large exact deficit while the capability change remains fixed at one rescued world.

The source monitoring theorem also separates **required state complexity** from **evidence refinement**. A richer state representation does not automatically imply that an existing field record identifies it. Evidence adequacy is an additional gate.

## 8. No bound from carrier gain alone can exist

The family gives an immediate no-bound corollary. Suppose a finite function `f` existed such that every CREST capability expansion satisfied

\[
\Delta K_{U_0}\le f(\Delta|K^*|).
\]

For the connected family,

\[
\Delta|K^*|=1
\]

for every `m`, while

\[
\Delta K_{U_0}=m.
\]

Choosing `m>f(1)` yields a contradiction. Therefore

\[
\boxed{\text{no universal finite upper bound on required present-state resolution can depend only on carrier-size gain}.}
\]

The same logic applies to the fixed-evidence monitoring debt in this family. [R0]

This is the chapter's anti-obviousness theorem. It is not merely that capability and knowledge are “different concepts.” The theorem rules out a whole class of proposed universal bounds based solely on the number of newly viable worlds.

Any positive bound must therefore use additional structural information: for example, restrictions on how the new action changes future response distinctions, constraints on the retained present slice, or direct bounds on the refined state/evidence partition.

## 9. Full-state identification can fail while a coarse requested target remains licensed

A second feature prevents the chapter from collapsing “insufficient full-state knowledge” into “scientific ignorance.”

Let the requested target `T` be constant over `U_0`, such as a coarse current viability label. The unchanged one-block evidence cannot identify which of the `2^m` new exact present states is occupied, but it still identifies the target because all those states share the same target value. [R0]

Thus after expansion the same evidence can satisfy

\[
\text{full required state: licensed}\to\text{unlicensed}
\]

while

\[
\text{coarse target: licensed}\to\text{licensed}.
\]

This result is conceptually important for the dissertation. Monitoring should not be judged against maximal latent-state identity unless that is actually the scientific responsibility. A capability expansion can create a large state-resolution deficit while leaving some decisions or reports unaffected.

The opposite mistake is also forbidden: target reportability does not imply that the full state is known. CREST keeps these objects typed separately.

## 10. The connected construction blocks a cheap disjoint-gadget objection

A weaker proof could combine two unrelated subsystems: one where a new action rescues one world and another where the same action name reads an arbitrary memory vector. The conjunction would establish the numerical contrast but not a meaningful structural link.

The CREST family avoids that construction. The same repeated `probe` trajectories that expose the latent address eventually enter the uniquely rescued world `r`, and `r` is viable only because the same `probe` action reaches `s`. [R0]

This does not establish causal proportionality between carrier gain and information burden; indeed the no-bound theorem denies such a general proportional relation. It establishes something more appropriate:

> one fixed-size intervention expansion can simultaneously generate a constant viability change and an unbounded representational/evidence change in one connected response system.

That is enough to refute carrier-size gain as a universal proxy for knowledge burden.

## 11. The general CREST architecture explains where the divergence sits

The divergence theorem crosses several CREST gates but does not replace them.

- A future/response contract determines which present distinctions must be retained.
- A controlled-carrier construction determines where safe management is possible.
- A required-state quotient represents distinctions needed under the declared responsibility.
- An evidence partition determines what the monitoring record actually resolves.
- A target map determines whether the requested report requires the full state or only a coarser distinction. [R1]

The theorem supplies one family in which these gates move by very different amounts under the same action expansion.

This layered architecture is why the chapter title uses “knowledge” carefully. `m` monitoring bits are not a psychological measure, a sample-size estimate or a monetary cost. They are an exact finite partition-resolution deficit under a declared evidence map.

Empirical monitoring cost would require an observation model, sensor error, sampling design and resource accounting. None is inferred from the finite theorem.

## 12. What would make a small capability change benign?

The no-bound theorem does not say every small capability expansion creates large debt. The construction reveals the missing condition: the new action must create many future-response distinctions on the retained present slice for the state complexity to grow.

If the newly admitted action leaves all worlds previously merged on `U_0` future-response equivalent under the expanded contract, then the least exact state on that slice need not refine. If a declared target also factors through the old evidence, target reporting may remain unchanged. [R1]

This observation is not advertised as a separate novelty theorem; it is the direct positive side of the exact-state definition. Its role in the chapter is to block the false converse:

> small capability expansion **can** generate unbounded state/evidence burden, but does not **necessarily** do so.

The actual design question is whether the added capability exposes previously hidden distinctions relevant to the declared future responsibility.

## 13. Relation to Chapter 5: legal-future opening and capability expansion are not the same operation

Chapter 5 kept the physical network fixed and changed the legal future grammar used to evaluate exact response equivalence. Chapter 6 changes the controllable repertoire and, consequently, the robust carrier and required future-sensitive state.

The theorems are related in spirit because both expose dormant distinctions, but they answer different questions. CCOC does not supply the +1-world carrier theorem; CREST does not replace CCOC's fixed-regular response-interface sharpness result. [TR]

The chapter order is therefore conceptual, not deductive:

1. Chapter 5 shows that physical narrowness does not bound memory when the legal future expands.
2. Chapter 6 asks whether a small **capability consequence**—only one newly viable world—can bound state/evidence burden.
3. The CREST no-bound family says it cannot.

## 14. What the chapter establishes

For the declared finite deterministic CREST class, the chapter establishes:

1. for every `m>=1`, one newly admitted action makes exactly one additional world viable;
2. on a retained present slice, exact future-sensitive state complexity simultaneously increases from zero to `m` bits;
3. unchanged one-block evidence simultaneously moves from zero monitoring debt to exactly `m` bits of debt;
4. the construction is connected through the same new action rather than a disjoint union of independent gadgets;
5. therefore no universal finite upper bound on the state-resolution increase can depend only on carrier-size gain;
6. full-state identification can become unlicensed while a declared coarse target remains exactly reportable;
7. the theorem does not imply that every small capability expansion has a large burden—large burden arises when the expanded responsibility splits many previously merged present worlds.

It does **not** estimate real monitoring expense, identify a natural conservation state, show that one additional management action usually creates high information burden, or claim a causal law from carrier gain to state complexity. [R3]

The precise conclusion is:

> **Management capability and scientific resolution are different gates. A fixed one-world viability gain can coexist with arbitrarily large required present-state refinement and monitoring debt, so the scale of capability gain cannot by itself certify that existing representation and evidence remain adequate.**

## 15. Transition: even a well-resolved law may fail after the system is structurally replaced

Chapter 6 concerns an action expansion within one declared controlled system. The next question changes the carrier/structure itself.

Suppose a macro-law was exact in a source system and the source state was adequately represented. After a component, interaction structure or ecological module is replaced, can that source law be carried unchanged to the target merely because the same labels can be assigned?

CREST does not answer that source-relative transport problem. MLTR owns the next theorem:

> **A carried source law is exact after replacement if and only if outputs, legal-action rows and successor carried labels are constant within every carried fiber; if not, the target has a unique coarsest source-relative repair, and route disagreement requires explicit history modes.** [TR]

## Internal source keys

- **[R0]** CREST `docs/crest_capability_resolution_divergence_theorem_2026-08-22.md` — connected all-`m` construction, +1 carrier theorem, `1→2^m` state refinement, `0→m` monitoring debt, target-only reportability and no-bound corollary.
- **[R1]** CREST `docs/crest_mathematical_spine.md`, controlled-carrier and joint-state/evidence theorem stack — gate definitions and positive interpretation boundaries.
- **[R2]** CREST `docs/crest_monitoring_resolution_debt_2026-08-21.md` and supplementary proof — minimum evidence refinement / monitoring debt semantics.
- **[R3]** CREST blinded manuscript and novelty/claim firewalls — finite deterministic theorem, no empirical monitoring-cost or prevalence claim.
- **[R4]** CREST `tests/test_crest_capability_resolution_divergence.py` — executable connected arbitrary-scaling/no-bound witness.
- **[TR]** `thesis/transition_recovery_matrix.json` — Chapter 5→6 and Chapter 6→7 are editorial question handoffs, not theorem implications.
