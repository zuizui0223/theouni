<!-- draft-id: chapter:introduction:v0.1 -->
# General Introduction — The Reuse Problem in Ecology

> **Draft status:** source-bounded v0.1. Internal source tags `[A]`–`[E]` refer to the companion source map and are not final bibliography citations.

## 1. Ecological science depends on reuse

Ecology advances by compressing complexity. A lake is described as clear or turbid, a population as viable or declining, a landscape as connected or fragmented, and a community as functionally intact or impaired. These descriptions are useful because they allow many physically different systems to be treated as equivalent for a particular scientific purpose. The same economy underlies reduced models, monitoring indicators, causal interpretations, management rules, and early-warning signals. None attempts to reproduce every detail of an ecological system. Each retains a subset of distinctions so that prediction, intervention, explanation, or reporting remains possible.

The practical difficulty is not merely how to construct such representations. It is whether a representation built for one scientific responsibility can be reused after that responsibility changes. A state variable calibrated for present-status reporting may later be asked to choose among interventions. A macro-law accepted before species turnover may be carried into a structurally altered community. An observation selected to distinguish causal explanations may be treated as if it also licensed a management target. A genetic indicator that repeatedly precedes ecological loss in one calibrated domain may be exported as a warning in another. In each case the representation once did legitimate work. The risk appears when that success is treated as a general passport to a different task. [A, B]

This dissertation calls that risk the **reuse problem in ecology**:

> **When may a state, law, measurement, causal result, or warning built for one ecological responsibility be transported to another?**

The problem is broader than model transfer in the ordinary statistical sense. The changed object may be the set of legal future actions, the ecological system itself, the mechanism family retained as possible, the observation and failure architecture, the decision target, the raw simulator representation, or the warning domain. A representation can therefore fail even when its original calculation was correct. The failure is not necessarily bad estimation. It may be a mismatch between the distinctions preserved by the representation and the distinctions demanded by the new scientific task. [A, C]

## 2. Adequacy is local to a scientific responsibility

Let \(\Omega\) be a declared universe of model worlds. A scientific responsibility or task \(\alpha\) is represented by a contract-complete response signature

\[
\Sigma_\alpha:\Omega\to Y_\alpha,
\]

where \(\Sigma_\alpha\) records exactly the responses that must be preserved for that task. It may contain future responses under interventions, inherited meanings, mechanism-indexed outcomes, a loss trajectory, a warning relation, or a report target. A retained representation is a map

\[
R:\Omega\to Z.
\]

The minimal shared criterion used throughout this dissertation is

\[
\boxed{
R\models\alpha
\iff
\exists f:Z\to Y_\alpha
\text{ such that }
\Sigma_\alpha=f\circ R.
}
\]

A representation is adequate for \(\alpha\) when the complete task response can be reconstructed from what the representation retains. Equivalently, the representation must not merge two worlds that task \(\alpha\) requires to have different answers. [C]

This criterion is classical factorization and quotient substrate, not the dissertation's principal mathematical novelty. Purpose-relative representation, abstraction, idealization, and task-specific sufficiency all have extensive prior literatures. The shared formal language matters here because it makes eight different ecological failures comparable without pretending that they are one theorem. Each research chapter supplies a source-owned result showing that a plausible inference from one context to another is invalid, sometimes by an exact necessary-and-sufficient criterion and sometimes by a quantitative counterexample or empirical failure. [B, C, D]

The criterion also prevents task relativity from becoming arbitrary relabelling. Scientists may choose which prediction or decision matters, but they cannot declare two worlds equivalent if those worlds yield different responses that the chosen task requires. The task determines which difference is relevant; ecological dynamics and the declared model determine whether that difference exists. [D]

## 3. Reuse can fail in several non-equivalent ways

The dissertation is not organized around eight rival definitions of ecological state. It is organized around eight ways in which scientific adequacy fails to travel.

First, an increase in management capability can outpace the knowledge needed to use it. A new controllable action can expose distinctions that were irrelevant under the old repertoire. CREST shows that the gain in viable or controllable worlds can remain fixed while the required state resolution and monitoring debt grow without a corresponding bound. The forbidden inference is that a small intervention or capability gain implies a small epistemic burden. [B, D]

Second, an exact interface that is small under each fixed closed future grammar need not remain small when those futures are opened jointly. CCOC studies this cross-grammar failure. Its object is not the same as CREST's capability–monitoring comparison: it compares independently optimized closed interfaces with the interface required by the open grammar. The forbidden inference is that simplicity under every closed context guarantees simplicity under open composition. [B]

Third, a macro-law can lose its meaning when the ecological system is replaced rather than merely extended. MLTR begins with an inherited source partition and asks whether it transports through turnover, extinction, recolonization, habitat reconfiguration, or interaction rewiring. If transport fails, the task is not to discard the old semantics and optimize a new aggregation from scratch, but to construct the unique coarsest exact repair that preserves every inherited merge still valid. The forbidden inference is that an exact source law remains exact after structural replacement. [B]

Fourth, visible equivalence need not support one deterministic law when multiple mechanisms remain scientifically admissible. MRM does not insist that every mechanistic difference enter ecological state. It retains only differences that change a required future response. A candidate-independent deterministic law exists exactly when the retained response types agree; otherwise honest reporting must remain typed or set-valued. The forbidden inference is that the same visible present state guarantees the same intervention law. [B]

Fifth, a distinction required in principle may not have been earned by the evidence. CED separates the compatible-world class produced by an experiment from the additional resolution a target would require. It further asks whether the observation architecture can reliably support a nominal split under missed detection, shared failure modes, calibration limits, and false-resolution risk. The forbidden inference is that more information, finer records, or more repetitions automatically license the requested target. [A, B]

Sixth, learning a causal explanation and licensing a decision are different scientific achievements. RACH retains all causal programmes compatible with the model family, biological constraints, and observed pattern, then selects a next observation by its value for causal learning. TU-2 supplies the firewall: causal-learning value and target-licensing status can vary independently and can rank equal-cost observations in opposite orders. The forbidden inference is that a strong pattern match or high information gain identifies the cause or resolves the decision. [B, E]

Seventh, raw simulator detail and common ecological summaries need not define the state that generates functional loss. The eco-genetic programme shows both sides. A complete explicit state is sufficient under its declared Markov closure, yet common demographic, interaction, trait, and genetic marginals can conceal transition-relevant spatial alignment. TU-3 formalizes the representation boundary for a declared loss response. The forbidden inference is that a detailed simulator state is automatically the minimal loss state, or that matching familiar marginals proves loss-state equivalence. [B]

Eighth, a signal can precede loss repeatedly without functioning as a warning. In the warning programme, relative genetic erosion preceded realized loss in every audited event trajectory in both inherited and fresh ensembles, but the same thresholds also fired in every audited non-event trajectory. Temporal ordering reproduced; discrimination failed. TU-4 separates the loss-generating state from the finer warning-evaluation state and within-state validity from cross-state portability. The forbidden inference is that temporal precedence establishes predictive or portable warning. [B]

These failures are connected, but they are not interchangeable. Future opening does not supply a history map. Historical transport does not identify a mechanism. Mechanism-safe prediction does not license an observation. Causal learning does not imply reportability. A loss state does not automatically determine warning behaviour. Their coexistence in one theory universe depends on type discipline and explicit bridges, not on relabelling every result as a special case of one master theorem. [A, B]

## 4. What remains invariant across worldlines

Although the scientific objects change from chapter to chapter, seven rules remain fixed.

1. **Ecological reality is not a declared ModelWorld universe.** Internal theorem validity does not by itself establish empirical adequacy.
2. **State is task-indexed.** No repository-local state label becomes an intrinsic, context-free state of nature.
3. **A merge is safe only while required responses are preserved.** Reuse requires factorization through what was retained.
4. **Evidence does not create structural distinctions.** It identifies, fails to identify, or licenses reports about distinctions required elsewhere.
5. **Required state, identified state, and reportable target are not interchangeable.**
6. **The absence of a bridge is not a contradiction.** Results that cannot yet be transported may remain mutually consistent.
7. **Validity in one worldline does not imply portability to another.** A common carrier, faithful lift, replacement relation, evidence projection, causal-response map, or portability correspondence must be supplied as appropriate. [A]

These invariants provide the dissertation's unity. They also set its failure conditions. The theory fails if task-relative separation becomes a way to avoid all possible conflict while making cross-task claims untestable. For that reason, each chapter states not only a limitation but also a positive criterion, exact repair, quantitative witness, executable selection result, or empirical falsification. The theory universe is intended to regulate movement between scientific responsibilities, not merely to assign different labels to every disagreement. [A, B]

## 5. Transport is not the same as truth

A representation may be internally adequate yet empirically misplaced. Every chapter therefore operates under a Reality-to-Theory boundary. At minimum, an application must declare the empirical unit and temporal or cohort scale, the observed and unobserved coordinates, the candidate model-world support, the task and target, the observation and reliability model, the validation unit, and the claim ceiling. Without this bridge, the theorems remain statements about declared model worlds. [A]

Conversely, failure to transport does not imply that the original representation was false. A state can be adequate for present-status reporting and inadequate for choosing among new interventions. A law can be exact in a source system and inapplicable after replacement. A measurement can be excellent for causal learning and irrelevant to a decision target. A genetic trajectory can be reproducibly early and still fail as a classifier. The central question is not whether the old result was simply right or wrong, but what scientific responsibility it had earned and whether the new responsibility factors through it. [B, C]

This distinction allows several legitimate endings. A task may be resolved. Full state may remain unknown while a coarse target is licensed. Honest ambiguity may be the sharp result. A result may be valid but non-portable beyond a bounded domain. A worldline may remain open because a bridge or empirical admission condition is missing. These are not interchangeable with contradiction or theoretical collapse. [A]

## 6. Dissertation claim and scope

The dissertation's common claim is not that there exists one privileged ecological state. Nor is it that factorization, purpose relativity, partition refinement, information gain, or state abstraction is new in itself. Its claim is that ecologists repeatedly move representations across changes in capability, future grammar, system identity, mechanism responsibility, evidence, target, model representation, and domain, and that these movements require different explicit conditions. The source-owned chapters identify non-obvious cases where a familiar inference fails and characterize what replaces it: a finer interface, a repaired law, a typed report, an evidence-qualified target, a next observation, a loss-faithful representation, or a warning-specific portability test. [B]

The General Synthesis returns to the time-indexed version of reuse. Once an earlier scientific compression has actually been stored, a revised state \(Q\) can be recovered from an old state \(P\) only when

\[
q_Q=f\circ q_P.
\]

If the factorization fails, distinctions erased by the old representation cannot be recreated by post-processing the old label alone. TU-1 quantifies the auxiliary revision information required in the current same-carrier setting. This result does not absorb the previous chapters. It shows why a representation adequate today need not remain revisable tomorrow. [B, C]

## 7. Roadmap

Part I asks how doing more can require knowing more. Chapter 1 presents the conservation-capacity paradox and the capability–resolution no-bound result. Chapter 2 isolates the related but distinct cross-grammar interface inflation under open futures.

Part II asks when scientific laws fail to travel. Chapter 3 studies source-relative transport and repair after ecological replacement. Chapter 4 studies deterministic law under retained mechanism uncertainty.

Part III asks why more information need not give the needed answer. Chapter 5 separates evidence classes, target-safe resolution, failure architecture, and licensed reporting. Chapter 6 develops admissible causal sets and next-observation selection while separating causal learning from decision licensing.

Part IV moves into an explicit eco-genetic dynamic system. Chapter 7 asks which representation actually generates functional loss. Chapter 8 shows how a perfectly reproduced temporal ordering can nevertheless fail as a warning and why portability requires a separate state and test.

The General Synthesis reconstructs these chapters as a typed universe of scientific transport, non-transport, and revision. The theory has a dependency structure, but no privileged narrative order. The chosen sequence is an editorial traversal designed to expose the strongest surprises first; it is not the definition of the underlying theory universe. [A, B]

## Internal source keys

- `[A]` — `universe/WORLDLINE_ATLAS.md`
- `[B]` — `universe/DISSERTATION_ARCHITECTURE.md`
- `[C]` — `theory/DRAFT_v0.6_CONTRACT_INDEXED_QUOTIENT_TRANSPORT.md`
- `[D]` — `zuizui0223/crest:manuscript/crest_biology_philosophy_blinded_submission.md`
- `[E]` — `zuizui0223/microdonta:paper/README.md` and `theory/TU2_LEARNING_LICENSING.md`
