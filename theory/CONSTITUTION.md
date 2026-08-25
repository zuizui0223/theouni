# Theory Universe Constitution v0.5

This document is the normative theory spine of `theouni`.

It does not claim that the axioms below are laws of nature. They are **scientific-ontology and inference commitments** that define the mathematical universe in which the current programme is allowed to reason. A theorem or empirical projection that violates one of these commitments must either supply an explicit bridge theorem or be treated as outside the current universe.

The governing question is:

> **What may science safely forget, what must remain revisable, and which distinctions are required by the scientific question actually being asked?**

---

## I. Primitive layers

The theory separates five layers before any biological example is introduced.

1. **Reality layer** — ecological reality, denoted `Reality` or \(\mathfrak R\).
2. **Model-world layer** — a declared admissible universe \(\Omega\) of temporally extended model worlds.
3. **Representational layer** — contract-relative quotients of worlds, including `RequiredState`, `LossGeneratingState`, and `WarningEvaluationState`.
4. **Epistemic layer** — observation records, evidence classes, reportability, causal admissibility, and learning.
5. **Cross-time / cross-representation layer** — revision after compression, representation changes, and warning portability.

No object may silently change layer.

---

## II. Constitutional axioms

### A0 — Reality/model separation

\[
\boxed{\mathfrak R\neq\Omega.}
\]

A theorem on model worlds is not automatically an empirical theorem about ecological reality. Empirical use requires an explicit projection/measurement/model contract.

### A1 — World before state

A model world is temporally extended. A schematic representation is

\[
\omega_t=(h_{\le t},x_t,\theta_t,K_t),
\]

where history, present configuration, retained mechanism, and future-response structure may all be relevant.

Consequently,

\[
\boxed{\text{Snapshot}\neq\text{World}.}
\]

Snapshot sufficiency is a proposition to be established, not a default ontology.

### A2 — Contract-relative state

A scientific contract is

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,\mathcal D;T).
\]

Two worlds may be merged only when they are scientifically interchangeable for every responsibility declared by \(\mathcal C\).

The required state is therefore a quotient

\[
S_{\mathcal C}=\Omega/\sim_{\mathcal C}.
\]

State identity is purpose-relative but not arbitrary: dynamics, history, mechanism disagreement, and evidence/report requirements can refute a proposed merge.

### A3 — Safe-forgetting principle

A state is a scientifically admissible compression. A distinction may be forgotten exactly when erasing it leaves all contract-required responses invariant.

Thus the programme treats state construction as **maximal lawful forgetting**, not maximal description.

### A4 — Evidence non-creation

Evidence does not create ontic distinctions. It determines which already-required distinctions are identified and which reports are licensed.

Hence, in general,

\[
\boxed{
\text{RequiredState}\neq\text{EvidenceClass}\neq\text{Report}.
}
\]

### A5 — Target-relative reportability

A full state need not be identified for a target to be reportable. A deterministic target is licensed exactly when it is constant on the reliability-qualified compatible evidence class.

The canonical separation is

\[
\boxed{
\text{required state}\neq\text{identified state}\neq\text{reportable target}.
}
\]

### A6 — Set-valued causal uncertainty

Unresolved causal uncertainty remains set-valued. A single causal winner is licensed only when the declared model/observation/evidence contract actually reduces the admissible set to a singleton or otherwise establishes a decision-safe equivalence.

Therefore

\[
\boxed{\text{AdmissibleCausalSet}\neq\text{CausalWinner}.}
\]

### A7 — Revision non-regeneration

Once a distinction has been discarded by a stored state representation, a later contract cannot reconstruct it from that state label alone unless the revised required state factors through the stored state.

Scientific compression can therefore be adequate now but unrevisable later.

### A8 — Typed scientific utility

The value of learning about a causal programme is not identical to the value of licensing a target report.

\[
\boxed{\text{CausalLearningValue}\neq\text{TargetLicensingStatus}.}
\]

Neither determines the other in general.

### A9 — Representation/target separation

Raw simulator-state complexity is not ecological state complexity. Two model representations are equivalent for a declared target only when the target-response signature factors through the representation bridge.

Therefore a `CompleteSimulatorState` may be sufficient while being nonminimal, unnatural, or empirically inaccessible.

### A10 — Loss state before warning state

A loss-generating state is the required quotient for a declared loss response. A warning evaluation state is the required quotient for the **joint loss + warning response**.

Thus

\[
\boxed{Q_{\rm loss}\preceq Q_{\rm warn}.}
\]

Equality holds only when warning response is constant within every loss-state block.

### A11 — Within-state reproducibility before portability

Reproducibility of a warning relation inside one frozen warning-evaluation domain and portability of that relation across different domains are separate claims.

A universal warning threshold is never inferred merely from within-domain lead ordering.

### A12 — Empirical admission gate

No species, island syndrome, trait, SDM surface, sensor output, network index, or genetic statistic is a state coordinate merely because it is biologically plausible.

An empirical object enters the theory only through an explicit typed projection specifying at minimum:

- empirical unit and time/cohort;
- measured coordinates and missing coordinates;
- model-world universe or candidate class;
- scientific contract and target;
- observation/reliability model;
- held-out or otherwise external adequacy criterion when state status is claimed;
- claim ceiling and known non-identifiabilities.

---

## III. Canonical definitions

### D1 — ModelWorld

A declared temporally extended mathematical object on which dynamics, response, evidence, and intervention statements are evaluated.

### D2 — ScientificContract

A tuple of future, historical, mechanism, evidence, and target responsibilities.

### D3 — RequiredState

The coarsest adequate quotient when such a quotient exists for the declared carrier/contract.

### D4 — EcologicalLaw

A well-defined effective response law on an adequate quotient. A law may fail after contract change because the old quotient ceased to be adequate, without being false in its original domain.

### D5 — EvidenceClass

The set/block of worlds compatible with a reliability-qualified observation record.

### D6 — AdmissibleCausalSet

The causal programmes whose supported worlds remain compatible with the current evidence and constraints.

### D7 — StoredStateRepresentation

A state label/partition retained from an earlier scientific contract and subsequently used without reopening the full world description.

### D8 — RevisionDebt

The minimum idealized auxiliary distinction required to reconstruct a revised required state from a stored old state, as defined by TU-1 on a finite same-carrier setting.

### D9 — LossGeneratingState

The quotient induced by equality of the declared loss-response signature.

### D10 — WarningEvaluationState

The quotient induced by equality of the joint loss-response and warning-response signatures.

### D11 — WarningPortability

Commutation of warning response with an explicitly declared correspondence between source and target warning-evaluation state spaces/domains.

---

## IV. Source-owned theorem substrate

`theouni` does not re-own the following results.

| Source | Constitutional role |
|---|---|
| `crest` | finite common-carrier required-state construction; carrier/state/evidence/target separation |
| `ccoc` | future/open-composition obstruction to old merges |
| `mltr` | transport, repair, and history augmentation after replacement |
| `mrm` | response-relevant mechanism distinction and mechanism-safe reporting |
| `ced` | evidence classes, target-safe resolution, failure-aware licensing, risk-limited reportability |
| `microdonta` / RACH | admissible causal sets and next-observation causal-learning value |
| `eco-genetic-criticality` | simulator-state sufficiency boundary and eco-genetic dynamics |
| `eco-genetic-warning-extensions` | warning-blind loss conditioning, within-state warning replication, portability bounds, empirical partial-state tests |

The theory universe uses these as typed inputs. It may derive cross-layer firewalls without transferring the original theorem/evidence ownership.

---

## V. `theouni` theorem modules

### TU-1 — Contract revision after compression

Question: after an old state has already been stored, can a revised state be recovered without reopening the original world description?

Finite results:

- exact state-only recoding criterion;
- exact minimum auxiliary revision alphabet;
- worst-case revision debt;
- average/worst-case divergence construction.

Boundary: elementary finite coding/factorization substrate; no standalone information-theory novelty claim.

### TU-2 — Learning versus licensing

Question: does an observation that is valuable for causal identification also resolve the requested report target?

Finite results:

- equal causal-learning value with opposite target licensing;
- maximal normalized causal learning with zero target license;
- zero causal learning with complete target license;
- equal-cost policy-order reversal.

Boundary: finite noiseless bridge firewall; reliability/failure/risk remains CED-owned.

### TU-3 — Loss-state representation invariance

Question: when do different raw simulator representations encode the same target-relevant loss state?

Finite results:

- loss-response factorization criterion;
- representation-faithful quotient isomorphism;
- arbitrary nuisance-state inflation without loss-state inflation;
- hidden-coordinate counterexample when loss response changes inside a projection fiber.

Boundary: closely related to classical quotient/lumpability/bisimulation/predictive-state ideas; used here as a type firewall.

### TU-4 — Warning evaluation state and portability

Question: when is a loss state sufficient for warning evaluation, and when can warning transport across domains?

Finite results:

- warning-state quotient refines loss-state quotient;
- equality iff warning response factors through loss state;
- warning-insufficiency counterexample with identical loss response but different warning ordering;
- explicit portability commutation criterion.

Boundary: does not establish a universal threshold, empirical state minimality, or cross-domain portability in nature.

---

## VI. Dependency structure

The canonical dependency order is:

```text
A0-A3  Reality / World / Contract / Safe forgetting
   |
   v
CREST required-state substrate
   |\
   | +--> CCOC future obstruction
   | +--> MLTR history obstruction
   | `--> MRM mechanism obstruction
   |
   +--> CED evidence/reportability
   |      |
   |      `--------------------------.
   |                                 |
   +--> RACH causal admissibility ---+--> TU-2 Learning != Licensing
   |
   +--> Stored state --------------------> TU-1 Revision after compression
   |
   `--> Dynamics / target response
           |
           `--> TU-3 Loss-state representation invariance
                    |
                    v
              LossGeneratingState
                    |
                    +--> warning response
                    v
              TU-4 WarningEvaluationState / portability
```

TU-1 and TU-2 do not depend on TU-3 or TU-4. TU-4 conceptually depends on the target-response quotient discipline formalized in TU-3, but its finite factorization statements can be checked independently.

---

## VII. Claim ceilings

The current Theory Universe does **not** establish:

- one intrinsic ecological state independent of scientific purpose;
- a canonical model-world universe supplied directly by nature;
- a general continuous/stochastic/approximate CREST theorem;
- that a complete simulator state is a natural state;
- that causal information gain is equivalent to scientific reporting value;
- that a loss-generating state automatically determines warning behaviour;
- universal genetic-warning thresholds;
- warning portability across arbitrary ecological domains;
- that any current empirical partial state is complete;
- that Graphify connectivity or repository proximity is scientific evidence;
- that TU-1 through TU-4 are standalone mathematical novelties independent of classical prior art.

---

## VIII. Frozen v0.5 scientific sentence

The current theory universe may be summarized as:

> **Ecological reality is represented by temporally extended model worlds. Scientific states are contract-relative quotients that erase only distinctions irrelevant to a declared future, history, mechanism, evidence, and target responsibility. Evidence determines which required distinctions are identified and what may be reported; causal uncertainty remains set-valued when evidence does not discriminate it. Compression may become unrevisable when later contracts require forgotten distinctions. Learning about causes and licensing a target are distinct utilities. Raw simulator detail is not state complexity: target-relevant states are invariant only under response-faithful representation changes. Warning must be evaluated on a joint warning/loss state, and within-state reproducibility does not imply cross-state portability.**

Any future theoretical extension should preserve this sentence or explicitly version the constitution.
