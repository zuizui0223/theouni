# Theory Universe v0.2 — worlds, states, evidence, learning, revision, and warning

This directory is the **theory-first core** of `theouni`. Species systems, island syndromes, floral traits, SDMs, camera systems, and field protocols are deliberately excluded until the abstract universe is internally coherent.

The programme question is now:

> **What may science safely forget, and what must be retained so that later scientific responsibilities remain revisable?**

The second clause is new in v0.2. CREST defines contract-relative adequate state; TU-1 asks what happens **after that state has already been used as a compression** and the scientific contract later changes.

## 1. Constitutional commitments

1. **Nature is not a state.** Ecological reality is temporally extended.
2. **A model world is not reality.** Mathematics operates on an admissible world universe, not directly on nature.
3. **A state is a contract-relative quotient of worlds.** State identity is defined by what may safely be forgotten for a declared scientific responsibility.
4. **Evidence does not create ontic distinctions.** It determines which required distinctions are identified and which reports are licensed.
5. **Causal uncertainty remains set-valued until discriminating evidence exists.**
6. **Warning is conditional on a loss-generating state.**
7. **Scientific forgetting can be revision-irreversible.** A distinction removed by an old stored state cannot be recreated from that state label alone when a later contract requires it.

## 2. Reality, worlds, and snapshots

Let ecological reality be

\[
\mathfrak R.
\]

Scientific mathematics acts on a model-world universe

\[
\Omega,
\]

with an explicit modelling/measurement bridge

\[
\Pi_V:\mathfrak R\dashrightarrow\mathcal P(\Omega).
\]

Thus

\[
\boxed{\mathfrak R\neq\Omega.}
\]

A model world can be written schematically as

\[
\omega_t=(h_{\le t},x_t,\theta_t,K_t),
\]

where history, present configuration, retained mechanism, and future-response structure may all matter.

The foundational firewall is

\[
\boxed{\text{Snapshot}\neq\text{World}\neq\text{RequiredState}.}
\]

Snapshot sufficiency is a theorem/question, never an assumption.

## 3. Scientific contract and required state

A scientific contract is

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,\mathcal D;T),
\]

where:

- \(\Gamma\): future/intervention obligations;
- \(\mathcal H\): inherited meaning and history that must remain coherent;
- \(\Theta\): retained mechanism alternatives;
- \(\mathcal D\): observation, experiment, reliability, and calibration obligations;
- \(T\): requested report, forecast, decision, or endpoint.

Two worlds are equivalent when they are scientifically interchangeable for the declared contract:

\[
\omega\sim_{\mathcal C}\omega'.
\]

The required state space is

\[
\boxed{S_{\mathcal C}=\Omega/\sim_{\mathcal C}.}
\]

On one declared finite common carrier, CREST supplies the unique least-information adequate partition via the common fixed point of the declared refinement closures.

The state is therefore the maximal **lawful forgetting** compatible with the contract.

## 4. Three structural reasons a present merge can fail

These are separate theorem families inside one state universe.

### Future — CCOC

Opening or changing \(\Gamma\) can expose future-response differences hidden by an old present-state merge.

### History — MLTR

Replacement, turnover, extinction, recolonisation, or rewiring can invalidate inherited state meaning. Exact transport may fail and require repair or history augmentation.

### Mechanism — MRM

Worlds with the same visible present configuration may retain response mechanisms that disagree under a required intervention. Only response-relevant mechanism differences must survive the quotient.

These are not rival definitions of state. They are three ways an attempted forgetting can become scientifically unsafe.

## 5. Ecological laws as quotient laws

An ecological law is an effective law on an adequate quotient. For actions \(A\),

\[
L:S_{\mathcal C}\times A\to S_{\mathcal C}
\]

is well-defined only when all worlds merged by the state agree on the contract-relevant response.

A law can therefore cease to transport after the contract or ecological structure changes without having been false in its original domain: the old quotient may simply cease to be adequate.

## 6. Evidence, identification, and reporting — CED

An observation record \(y\) defines an evidence-compatible set

\[
E(y)=\{\omega\in\Omega:\omega\text{ is compatible with }y\text{ under }\mathcal D\}.
\]

This is epistemic, not ontic:

\[
\boxed{\text{EvidenceClass}\neq\text{RequiredState}.}
\]

Hence

\[
\boxed{\text{required state}\neq\text{identified state}\neq\text{reportable target}.}
\]

For target \(T\),

\[
R_T(y)=\{T(\omega):\omega\in E(y)\}.
\]

A deterministic target can be licensed even when the full required state remains unresolved.

## 7. Causal admissibility and learning — RACH

Let a declared causal programme \(m\) support model worlds \(\Omega_m\). The admissible causal set is

\[
A(y)=\{m:\Omega_m\cap E(y)\neq\varnothing\}.
\]

It is not a best-model winner. RACH keeps all compatible programmes and designs observations expected to reduce unresolved causal equivalence.

Learning is therefore

\[
(E_t,A_t)\xrightarrow{\text{new observation}}(E_{t+1},A_{t+1}),
\]

not compulsory collapse to one explanation.

CED and RACH remain distinct: predicted ambiguity reduction is not the same object as reliability-qualified licensed resolution.

## 8. Dynamics, simulator state, and loss state

Model worlds evolve under a declared transition law

\[
\omega_{t+1}\sim K(\cdot\mid\omega_t,a_t).
\]

A complete simulator state can be sufficient under one explicit Markov closure without being proved minimal, natural, or empirically measurable.

For a declared future loss endpoint \(L\), construct a loss contract \(\mathcal C_L\). Its required quotient

\[
S_L=S_{\mathcal C_L}
\]

is a **LossGeneratingState** when it is sufficient for the declared loss process in the domain under study.

Warning is then a conditional property such as

\[
\tau_G<\tau_L
\]

within a frozen loss-generating state. A warning statistic is not itself the state.

## 9. TU-1 — contract revision after scientific forgetting

CREST-J1 answers:

> If all relevant world distinctions are still available on one common lift, what is the least state satisfying the joint contract?

TU-1 asks a later question:

> If an old contract has already been compressed to a stored state, can a revised required state be recovered from that stored label alone?

Let \(P\) be the old stored partition and \(Q\) the revised required partition.

### TU-1A — state-only revision

There exists a recoding

\[
q_Q=f\circ q_P
\]

iff every old-state block lies inside one revised-state block.

Thus a distinction already forgotten by \(P\) cannot be regenerated from the old state label alone when \(Q\) later requires it.

### TU-1B — exact revision side information

For each old block \(B\), define

\[
r_B(P,Q)=|\{C\in Q:B\cap C\neq\varnothing\}|.
\]

Then the exact minimum auxiliary alphabet required for revision is

\[
\boxed{K_{\rm rev}(P\to Q)=\max_B r_B(P,Q).}
\]

The idealized worst-case revision debt is

\[
D_{\rm rev}=\log_2 K_{\rm rev}.
\]

### TU-1D/E — average versus worst-case debt

The global average refinement debt is

\[
D_{\rm avg}
=
\log_2|P\vee Q|-\log_2|P|
=
\log_2\left(\frac{1}{|P|}\sum_Br_B\right).
\]

TU-1 proves

\[
0\le D_{\rm avg}\le D_{\rm rev}.
\]

More strongly, for every \(m\ge1\) and \(\varepsilon>0\), finite partitions exist with

\[
\boxed{D_{\rm rev}=m\quad\text{and}\quad D_{\rm avg}<\varepsilon.}
\]

So a globally tiny update burden can hide an arbitrarily large local revisability problem in one rare old state.

Full statements, proofs, claim ceilings, and the executable construction are in:

- `TU1_CONTRACT_REVISION.md`
- `tu1_registry.json`
- `contract_revision.py`
- `verify_tu1.py`

The factorization/coding substrate is elementary and related to zero-error side-information problems. No standalone information-theory novelty claim is made at this stage.

## 10. Canonical worldline

The ontic/dynamical side is

```text
Reality R
  |
  | model/measurement bridge
  v
ModelWorldUniverse Omega
  |
  v
World omega_t ---- dynamics ----> World omega_t+1
  |
  | ScientificContract C
  v
RequiredState q_C(omega_t)
```

The epistemic/learning side is

```text
World
  |
  v
ObservationRecord
  |
  v
EvidenceClass
  |\
  | +--> licensed Report
  v
AdmissibleCausalSet
  |
  v
NextObservation -> refined evidence/causal set
```

A temporal scientific-programme side is now explicit as well:

```text
full worlds
  -> old contract C0
  -> stored state P
  -> contract changes
  -> full-world revised state Q
  -> TU-1 revisability test
       |-- state-only recoding
       `-- auxiliary revision information / reopen world description
```

## 11. Type firewall

The following collapses are forbidden without an explicit bridge/theorem:

| Forbidden collapse | Why |
|---|---|
| `Reality = ModelWorld` | mathematical validity is not empirical truth |
| `Snapshot = RequiredState` | sufficiency must be demonstrated |
| `CompleteSimulatorState = RequiredState` | sufficiency does not imply minimality/naturality |
| `EvidenceClass = RequiredState` | evidence resolution and structural adequacy differ |
| `Mechanism = RequiredState` | only response-relevant mechanism differences matter |
| `Proxy = StateCoordinate` | calibration or predictive adequacy is required |
| `Target = RequiredState` | target-only reporting may be possible |
| `AdmissibleCausalSet = CausalWinner` | unresolved multiplicity must remain |
| `WarningStatistic = LossGeneratingState` | warning is a conditional relation |
| `StoredState = RevisedRequiredState` | every contract change requires a TU-1 factorization check |
| `RevisionSideInformation = EvidenceClass` | empirical observability/reliability requires a CED-style bridge |

## 12. Current ownership

| Layer | Owner |
|---|---|
| World / contract / required state | `crest` |
| Future obstruction | `ccoc` |
| History transport / repair | `mltr` |
| Mechanism-robust state / law | `mrm` |
| Evidence / reportability | `ced` |
| Causal admissibility / next observation | `microdonta` / RACH |
| Eco-genetic dynamics / simulator-state boundary | `eco-genetic-criticality` |
| Loss-state recovery / conditional warning | `eco-genetic-warning-extensions` |
| Cross-repository type system | `theouni` |
| Contract revision after compression | `theouni` / TU-1 |

## 13. Remaining mathematical frontier

Theory Universe v0.2 leaves these as genuine open obligations:

1. **Reality -> model adequacy:** when does a model-world projection earn empirical adequacy rather than compatibility only?
2. **Beyond finite exact state:** stochastic, continuous, approximate, and delayed-observation versions.
3. **Carrier-changing revision:** extend TU-1 through replacement relations/common lifts and test lift-invariance of revision debt.
4. **Learning vs licensing:** characterize when RACH information gain and CED licensed-resolution gain coincide or diverge.
5. **Representation-invariant loss state:** when do different simulators induce the same loss-generating quotient?
6. **Warning portability:** when can warning ordering transport across different loss-state spaces without a universal threshold?
7. **Empirical state discovery:** formulate held-out state adequacy as a factorization problem rather than proxy accumulation.

## 14. Boundary to the empirical universe

No species, island syndrome, floral polymorphism, SDM method, visit camera, or field protocol defines the core types.

Empirical projects enter later only through an explicit projection

\[
\text{empirical system}\to(\Omega,\mathcal C,O_{\mathcal D},T)
\]

with a claim ceiling. Their role is to instantiate, test, falsify, or expose missing coordinates in the theory universe.
