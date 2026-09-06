# Chapter 2 — CREST: State under Changing Futures

## Problem

Ecological state descriptions are useful because they merge physically different systems into the same scientifically meaningful class. A lake may be called turbid, a population persistent, a community functionally intact, or a landscape connected even though many lower-level details differ. Such compression is legitimate only while the discarded distinctions remain irrelevant to the responsibility assigned to the state.

The difficulty is that the relevant future can change. New restoration actions become possible, previously isolated modules become reachable, structural replacement carries an inherited classification into a different system, or retained mechanisms imply different intervention responses. At the same time, even when a finer distinction becomes scientifically required, the available evidence may not identify it.

This chapter asks:

> **When does a previously adequate ecological state cease to be adequate after the future scientific contract changes?**

The integrated CREST series combines source-owned results from `crest`, `ccoc`, `mltr`, `mrm`, and `ced`. These modules are not a five-step theorem chain. The chapter is organized around one state-adequacy problem.

## Standalone contribution

The chapter's central claim is:

> **Ecological state is a scientifically licensed compression of temporally extended ecological worlds, and an increase in conservation capability can increase the state and monitoring resolution required for responsible action by an arbitrarily larger amount.**

The flagship quantitative theorem fixes the capability increase while allowing the knowledge burden to grow without bound. Three companion obstruction classes explain *why* an old state merge can become inadequate, and a final evidence-licensing layer separates required state from reportable state.

## 1. Contract-relative ecological state

Let `Omega` be a declared carrier of temporally extended ecological worlds. A scientific contract specifies the future operations, inherited meanings, retained mechanism alternatives, evidence architecture, and target that the state representation must support.

Two worlds may share one state exactly when their differences are irrelevant to those responsibilities. The state is therefore a quotient

\[
q_{\mathcal C,V}:\Omega\to Q_{\mathcal C,V},
\]

where the contract `C` and scientific-access context `V` determine which merges are licensed.

This task-relativity is constrained rather than arbitrary. If two worlds merged by a proposed state respond differently to an operation or target that the contract requires, the merge fails regardless of convenience. Conversely, physical differences need not be retained when they make no difference to the declared responsibility.

The distinction is between:

- **required state** — what the scientific task needs distinguished;
- **evidence-resolved state** — what the available observation system actually identifies;
- **reportable target** — what may still be reported even if full state identification fails.

## 2. Headline theorem — conservation capacity can outgrow conservation knowledge

The flagship CREST construction asks whether a small increase in action capability necessarily causes only a small increase in representational burden.

It does not.

For every integer `m >= 1`, the source theorem constructs one finite connected deterministic ecological system and one newly admitted controllable action such that:

- the robust/viable carrier grows by exactly **one world**;
- a retained present slice that previously required **one state** now requires **`2^m` states**;
- the minimum state-resolution increase is therefore exactly **`m` bits**;
- under unchanged monitoring, full-state licensing changes from available to unavailable with an exact **`m`-bit monitoring debt**;
- a coarser target can nevertheless remain reportable.

Schematically,

\[
\Delta |K^*|=1,
\qquad
|J^-|_{U_0}=1,
\qquad
|J^+|_{U_0}=2^m,
\]

so

\[
\Delta K_{U_0}=m.
\]

Because `m` is arbitrary, no universal finite function of the carrier-size gain alone can upper-bound the required state-resolution increase in this construction class.

The ecological point is not that every new intervention creates exponential complexity. It is that **capability size is not a valid general proxy for knowledge burden**.

## 3. Three parallel reasons an old state merge can split

The headline theorem establishes an asymmetry between capability and required knowledge. The companion theories identify structurally different ways an old state merge can become invalid.

They are **parallel obstruction classes**.

### 3.1 Future/composition obstruction — CCOC

Under a restricted future grammar, several micro-configurations may be exactly response-equivalent because no legal future can address their hidden differences. Enlarging the grammar can make those differences operationally visible.

CCOC defines exact response equivalence relative to legal future words. In its sharp family, the closed response quotient has only

\[
|P_C|=2
\]

classes, while opening one previously illegal future primitive produces

\[
|P_O|=2^{m+1},
\]

so exact response memory increases by `m` bits.

The construction remains sharp while keeping the action alphabet and local state/message alphabets bounded, local interaction radius fixed, graph degree bounded, and the focal cut small. Therefore the increase is not merely the result of trivially enlarging local static resources.

**CREST reading:** a difference that was legitimately ignored under the old future becomes state-defining once the future contract can address it.

### 3.2 Structural replacement and inherited meaning — MLTR

A second failure mode occurs when an ecological macro-law is carried from a source system to a structurally changed target.

MLTR asks whether states that share an inherited source label still have the same current output, legal-action row, and successor carried labels in the target. This gives an exact portability criterion.

When portability fails, source-relative refinement yields the unique coarsest exact target partition that preserves every inherited merge that remains valid.

The strongest route result concerns several replacement histories. A single route-free inherited terminal law exists exactly when the complete carried terminal maps agree across histories. If they disagree, one immutable history mode per **distinct carried terminal map** is necessary and sufficient to preserve all declared inherited meanings.

**CREST reading:** an old state can fail because its inherited meaning is not coherent after structural replacement, even if one could build a different target-only quotient.

### 3.3 Retained-mechanism obstruction — MRM

A third failure mode is mechanism ambiguity. Two worlds can share the same visible present state yet retain different response mechanisms. If those mechanisms predict different outcomes for a future intervention required by the contract, the mechanisms cannot remain merged in the required state.

MRM constructs the unique coarsest candidate-safe quotient that preserves only response-relevant mechanism distinctions. In its canonical `m`-bit response family, the mechanism-safe law has `2^(m+1)` states and an exact `m`-bit memory surcharge relative to a fixed two-state candidate law.

The paired intervention theorem shows that exactly `m` binary probes are necessary and sufficient in the worst case to identify one of `2^m` response signatures; after `k` distinct probes, exactly `2^(m-k)` signatures remain compatible.

**CREST reading:** full mechanism identity is not automatically state. Only mechanism differences that alter a responsibility-relevant response must be retained.

## 4. These obstruction modules do not prove one another

The integrated chapter must not turn thematic similarity into theorem dependence.

- CCOC does not prove MLTR: future-grammar enlargement and structural replacement are different contracts.
- MLTR does not prove MRM: inherited label incoherence and retained mechanism disagreement are different obstructions.
- MRM does not prove CCOC: mechanism ambiguity does not require future grammar expansion.
- None of the three proves the flagship CREST capacity-versus-knowledge theorem.

Their unifying role is taxonomic and explanatory:

> **they identify different reasons that a previously licensed state fiber may need to split.**

This is why they belong as sections of one state theory rather than as a forced dissertation sequence.

## 5. Evidence licensing is downstream — CED

Once a distinction is scientifically required, a different question remains:

> **Does the observation contract identify it well enough to support the desired claim?**

CED is therefore downstream of the state-obstruction layer. Evidence does not create the ecological distinction; it licenses or fails to license a report about a distinction required by the task.

CED's exact reporting machinery distinguishes full-state identification, target-safe reporting, and set-valued reporting. Its failure-domain theory also shows why adding observations is not a one-dimensional path to adequacy.

One equal-effort result compares two reads per coordinate within one failure mode against one read per coordinate in each of two independent modes. For `k` coordinates and per-read sensitivity `p`, the diversity-versus-depth difference changes sign at

\[
p_k^*=2-2^{1/k}.
\]

For `k=3`, the threshold is approximately `0.7401`: at lower sensitivity, within-mode repetition can outperform mode diversity for joint detection; at higher sensitivity, diversity wins. Separately, any fixed number of modes has an availability ceiling under unlimited repetition.

The lesson is not “diversity always beats replication.” It is that **evidence architecture must be matched to the reporting responsibility and failure contract**.

## 6. One integrated CREST architecture

The chapter can now be represented as one coherent theory:

```text
What ecological differences must the task retain?
        |
        |-- future/composition can expose a difference          [CCOC]
        |-- replacement/history can invalidate inherited meaning [MLTR]
        |-- retained mechanisms can imply different responses    [MRM]
        |
        v
construct / audit the required ecological state                 [CREST]
        |
        v
can current evidence license that distinction and target?        [CED]
```

This organization has a clear scientific asymmetry:

- the first four layers concern **what the task requires**;
- CED concerns **what the evidence licenses**.

## 7. Manuscript strategy — one headline, supporting theorem families

The flagship paper should not present five independent theorem families as five equal novelties.

### Main-text priority

1. conservation paradox and contract-relative state;
2. finite state construction / well-posed contract;
3. flagship capacity-versus-knowledge no-bound theorem;
4. three short obstruction classes with one sharp result each;
5. evidence licensing as the final scientific gate;
6. ecological worked interpretation.

### Supplement priority

- full CCOC cross-grammar lower-bound and bounded-local construction;
- full MLTR portability, repair, transport-defect, and route proofs;
- full MRM memory/intervention frontier and dynamic-programming discrimination results;
- CED equal-effort threshold, availability ceiling, calibration, and risk-limited reporting machinery.

This preserves theorem ownership and proof completeness while allowing one readable flagship argument.

## 8. Why this is a better standalone paper

The paper does not depend on the eco-genetic chapter or the observation-design chapter for its theorem claims. It can be read as a finite theory of ecological state and conservation representation.

Its single paper-scale question is:

> **What makes an ecological state scientifically adequate when the set of relevant futures changes?**

The answer has a core theorem, three structurally different failure classes, and a downstream evidence gate. That is more coherent than separate papers whose abstracts repeatedly begin from the claim that state depends on context.

## Claim ceiling

The integrated CREST chapter does **not** establish:

- one universal ecological state partition independent of scientific task;
- that every new intervention increases monitoring burden;
- that all open ecological systems require exponentially large states;
- that CCOC, MLTR, and MRM are theorem-equivalent formulations;
- that CED evidence failure proves the required ecological distinction is absent;
- that the finite exact results automatically extend to continuous, infinite, stochastic, or empirical systems without additional assumptions;
- that field evidence currently identifies the correct CREST contract for a particular ecosystem.

## Source ownership

- world/contract-relative state and flagship capacity-versus-knowledge theorem: `zuizui0223/crest`;
- future/composition obstruction: `zuizui0223/ccoc`;
- structural replacement, route coherence, and history completion: `zuizui0223/mltr`;
- mechanism-safe state and active discrimination: `zuizui0223/mrm`;
- evidence licensing and failure-domain reporting: `zuizui0223/ced`;
- cross-source integration and dependency firewall: `zuizui0223/theouni`.

## Dissertation handoff

CREST establishes that a task may require distinctions absent from an earlier state representation. The next chapter asks the epistemic and design question:

> **Once a distinction matters, can the current observations identify it—and if not, what should be measured next?**
