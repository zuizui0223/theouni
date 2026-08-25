# Theory Universe v0.5 — a contract-relative ecology of worlds, states, evidence, learning, revision, loss, and warning

This directory is the **theory-first core** of `theouni`.

Concrete species, island syndromes, floral polymorphisms, SDMs, cameras, sensors, and field protocols are deliberately excluded from the core. They enter later only through typed empirical projection contracts.

The canonical governing document is [`CONSTITUTION.md`](CONSTITUTION.md).

The programme question is:

> **What may science safely forget, what must remain revisable, and which distinctions are required by the scientific question actually being asked?**

---

## 1. One universe, five layers

Theory Universe v0.5 separates:

1. **Reality** — temporally extended ecological reality \(\mathfrak R\).
2. **Model worlds** — a declared mathematical universe \(\Omega\).
3. **Representation** — contract-relative quotients such as `RequiredState`, `LossGeneratingState`, and `WarningEvaluationState`.
4. **Epistemology** — `EvidenceClass`, reportability, `AdmissibleCausalSet`, and learning.
5. **Cross-time / cross-representation operations** — revision after compression, representation change, and warning portability.

The first firewall is

\[
\boxed{
\text{Reality}\neq\text{ModelWorld}\neq\text{Snapshot}\neq\text{RequiredState}.
}
\]

A theorem on a model-world universe is not automatically a theorem about nature.

---

## 2. World before state

A temporally extended model world can be written schematically as

\[
\omega_t=(h_{\le t},x_t,\theta_t,K_t),
\]

where history, present configuration, retained mechanism, and future-response structure may matter.

A scientific contract is

\[
\mathcal C=(\Gamma,\mathcal H,\Theta,\mathcal D;T),
\]

with future, historical, mechanism, evidence, and target responsibilities.

Two worlds may be merged only when they are scientifically interchangeable for the declared contract. The required state is therefore

\[
\boxed{
S_{\mathcal C}=\Omega/\sim_{\mathcal C}.
}
\]

The state is the **maximal lawful forgetting** compatible with that contract.

On a declared finite common carrier, CREST owns the least-information adequate-state construction. `theouni` does not re-own that theorem.

---

## 3. Why a present merge can fail

Three source theorem programmes provide distinct structural obstructions.

| Contract responsibility | Source | Failure mode |
|---|---|---|
| future / intervention \(\Gamma\) | `ccoc` | a newly legal future exposes a distinction erased by an old merge |
| history / inherited meaning \(\mathcal H\) | `mltr` | replacement or turnover makes an inherited state label non-transportable without repair/history |
| retained mechanisms \(\Theta\) | `mrm` | hidden mechanism differences produce different required responses |

These are not rival definitions of ecological state. They are three ways that forgetting can become scientifically unsafe.

---

## 4. Ecological laws are quotient laws

A coarse ecological law is an effective response law on an adequate quotient.

For actions \(A\),

\[
L:S_{\mathcal C}\times A\to S_{\mathcal C}
\]

is well-defined only if all worlds merged into one state agree on the contract-relevant response.

A law may therefore stop transporting after a contract or ecological structure changes because the old quotient ceases to be adequate, even though the law was valid in its original domain.

---

## 5. Evidence is not state — CED layer

An observation record \(y\) determines a reliability-qualified compatible-world class

\[
E(y)=\{\omega\in\Omega:\omega\text{ remains compatible with }y\}.
\]

This is an epistemic object:

\[
\boxed{
\text{EvidenceClass}\neq\text{RequiredState}.
}
\]

The canonical separation is

\[
\boxed{
\text{required state}\neq\text{identified state}\neq\text{reportable target}.
}
\]

A target can be deterministic on an evidence class even when the full required state remains unresolved. CED owns the finite evidence, failure, calibration, risk, and reportability layer.

---

## 6. Causal uncertainty is set-valued — RACH layer

For declared causal programmes \(m\) supporting world subsets \(\Omega_m\), define

\[
A(y)=\{m:\Omega_m\cap E(y)\neq\varnothing\}.
\]

This is the `AdmissibleCausalSet`, not a best-model winner.

RACH keeps compatible causal programmes and designs next observations that reduce unresolved causal ambiguity. For verified candidate outcome partitions, its publication-facing information quantity is schematically

\[
\operatorname{NOV}(Q)=\frac{I(S;Q\mid A_\epsilon)}{K}.
\]

The fact that an observation is valuable for causal learning does not by itself say whether a requested ecological target becomes reportable; TU-2 formalizes that firewall.

---

## 7. Dynamics, simulator state, and target-specific state

Model worlds evolve under a declared dynamics law

\[
\omega_{t+1}\sim K(\cdot\mid\omega_t,a_t).
\]

A `CompleteSimulatorState` can be future-sufficient under one explicit simulator closure without being minimal, natural, or empirically observable.

For a declared target-response signature \(r\), worlds are target-equivalent when they have the same required response. Raw representation complexity is therefore separate from target-relevant state complexity.

This separation is the basis of TU-3.

---

# 8. `theouni` theorem modules

## TU-1 — Contract revision after compression

CREST asks what state is adequate while the full common carrier is still available. TU-1 asks what happens **after a previous state has already been stored**.

Let \(P\) be the old stored-state partition and \(Q\) the revised required partition.

State-only revision exists iff

\[
q_Q=f\circ q_P.
\]

Equivalently, every old `P` block must lie inside one revised `Q` block.

If not, define

\[
r_B(P,Q)=|\{C\in Q:B\cap C\neq\varnothing\}|.
\]

The exact minimum idealized auxiliary alphabet is

\[
\boxed{
K_{\rm rev}(P\to Q)=\max_B r_B(P,Q),
}
\]

with worst-case revision debt

\[
D_{\rm rev}=\log_2 K_{\rm rev}.
\]

A finite construction shows that worst-case local debt can be arbitrarily large while average refinement debt is arbitrarily small.

**Interpretation:** scientific compression can be adequate today but unrevisable for a later scientific responsibility.

Source: [`TU1_CONTRACT_REVISION.md`](TU1_CONTRACT_REVISION.md).

---

## TU-2 — Causal learning is not target licensing

RACH and CED assign value to different scientific objects.

In a finite product universe

\[
\Omega=\{0,1\}^m\times\{0,1\},
\]

let \(S\) be causal state and \(T\) an independent report target.

Experiments can be constructed with

\[
\operatorname{NOV}=1,\quad L_T=0,
\]

and conversely

\[
\operatorname{NOV}=0,\quad L_T=1.
\]

Thus

\[
\boxed{
\text{CausalLearningValue}\neq\text{TargetLicensingStatus}.
}
\]

Equal-cost experiments can be ranked in opposite order by causal-learning and target-report objectives.

Source: [`TU2_LEARNING_LICENSING.md`](TU2_LEARNING_LICENSING.md).

---

## TU-3 — Loss-state representation invariance

Let \(r_L\) be the declared loss-response signature. The loss-generating quotient is

\[
Q_L=\Omega/\!\sim_L,
\qquad
\omega\sim_L\omega'\iff r_L(\omega)=r_L(\omega').
\]

For a representation projection \(\pi:X\to Z\), the coarse representation is loss-faithful iff

\[
r_L=\bar r_L\circ\pi.
\]

If this factorization holds, nuisance coordinates can make a simulator arbitrarily more detailed without increasing the loss-state quotient. If it fails, even one hidden coordinate can make the projection transition/loss-insufficient.

Therefore

\[
\boxed{
\text{raw simulator-state complexity}\neq\text{loss-state complexity}.
}
\]

Source: [`TU3_LOSS_STATE_INVARIANCE.md`](TU3_LOSS_STATE_INVARIANCE.md).

---

## TU-4 — Warning evaluation state and portability

A loss-generating state need not determine warning behaviour.

Let \(r_L\) be the loss response and \(r_G\) the warning response. Define the warning-evaluation quotient by equality of the joint signature

\[
(r_L,r_G).
\]

Then

\[
\boxed{
Q_{\rm loss}\preceq Q_{\rm warn}.
}
\]

Equality holds iff warning response factors through the loss state:

\[
r_G=\bar r_G\circ q_L.
\]

Thus two worlds can have the same loss future but different lead/tie/lag warning ordering and must then occupy different warning-evaluation states.

Warning portability across domains is an additional commutation condition on a declared cross-state correspondence; within-state reproducibility does not imply portability.

Source: [`TU4_WARNING_STATE_PORTABILITY.md`](TU4_WARNING_STATE_PORTABILITY.md).

---

## 9. Canonical state hierarchy

The word `state` is qualified throughout cross-repository work.

```text
ModelWorld
   |
   +--> RequiredState(C)
   |
   +--> CompleteSimulatorState       [model-specific sufficient representation]
   |
   +--> LossGeneratingState          [quotient for loss response]
   |       |
   |       `--> WarningEvaluationState [joint loss + warning response]
   |
   `--> EvidenceClass                [NOT an ontic state; epistemic compatible set]
```

In particular,

\[
\boxed{
\text{CompleteSimulatorState}
\neq
\text{LossGeneratingState}
\preceq
\text{WarningEvaluationState}
}
\]

unless explicit factorization/minimality conditions establish equality.

---

## 10. Canonical worldline

### Ontic / representational

```text
Reality
  |
  | model / measurement bridge
  v
ModelWorldUniverse
  |
  +--> dynamics through time
  |
  `--> ScientificContract
          |
          v
       RequiredState
```

### Epistemic / learning

```text
World
  -> ObservationRecord
  -> EvidenceClass
       |\
       | `--> TargetLicensingStatus / Report
       `----> AdmissibleCausalSet
                  |
                  `--> CausalLearningValue / next observation
```

### Revision

```text
RequiredState under C0
  -> StoredStateRepresentation
  -> contract changes to C1
  -> TU-1 factorization / revision-debt audit
```

### Loss and warning

```text
World dynamics
  -> declared LossResponseSignature
  -> TU-3 LossGeneratingState
       |
       + declared WarningResponseSignature
       v
     TU-4 WarningEvaluationState
       |
       +--> within-state WarningValidity
       `--> cross-state WarningPortability audit
```

---

## 11. Type firewall

Without an explicit bridge/theorem, the following collapses are forbidden:

| Forbidden collapse | Why |
|---|---|
| `Reality = ModelWorld` | model theorem is not empirical truth |
| `Snapshot = RequiredState` | sufficiency must be demonstrated |
| `CompleteSimulatorState = RequiredState` | sufficiency does not prove minimality/naturality |
| `CompleteSimulatorState = LossGeneratingState` | target-relative quotient may be much coarser |
| `EvidenceClass = RequiredState` | epistemic resolution differs from structural adequacy |
| `AdmissibleCausalSet = CausalWinner` | unresolved causal multiplicity must remain |
| `CausalLearningValue = TargetLicensingStatus` | TU-2 separates them exactly |
| `StoredState = RevisedRequiredState` | TU-1 factorization is required after contract change |
| `WarningStatistic = LossGeneratingState` | statistic is an observable coordinate, not a quotient |
| `LossGeneratingState = WarningEvaluationState` | equality requires warning-response factorization |
| `within-state warning replication = portability` | cross-state transport is an additional claim |
| `biologically plausible proxy = StateCoordinate` | empirical adequacy must be earned |

---

## 12. Ownership

| Layer | Primary owner |
|---|---|
| world / contract / required state | `crest` |
| future obstruction | `ccoc` |
| history transport / repair | `mltr` |
| mechanism-robust state / law | `mrm` |
| evidence / reportability | `ced` |
| causal admissibility / NOV | `microdonta` / RACH |
| eco-genetic dynamics / simulator-state boundary | `eco-genetic-criticality` |
| warning-blind loss conditioning and empirical warning results | `eco-genetic-warning-extensions` |
| cross-repository type system | `theouni` |
| revision after compression | `theouni` / TU-1 |
| learning/licensing firewall | `theouni` / TU-2 |
| loss-state representation firewall | `theouni` / TU-3 |
| warning-state/portability firewall | `theouni` / TU-4 |

Source theorem/evidence ownership is never transferred merely because the objects appear in the same theory graph.

---

## 13. Frozen dependency graph

The machine-readable dependency DAG is [`theorem_graph.json`](theorem_graph.json).

The normative constitution is [`CONSTITUTION.md`](CONSTITUTION.md).

The dependency graph is intentionally directed from prerequisite to dependent and preserves open problems as explicit open nodes. Graph reachability is not itself scientific proof.

---

## 14. Current theorem modules and claim ceilings

| Module | Closed finite result | Major non-claim / open extension |
|---|---|---|
| TU-1 | same-carrier revision criterion + exact idealized revision debt + local/global divergence | carrier-changing revision; physical irreversibility; empirical measurement cost |
| TU-2 | causal-learning/target-licensing orthogonality and policy reversal | reliability-aware coincidence theorem; generic active-learning novelty |
| TU-3 | target-response factorization + representation-faithful loss quotient + nuisance inflation | recursive stochastic quotient dynamics; empirical natural-state minimality |
| TU-4 | warning-state refinement/equality criterion + finite portability commutation | universal thresholds; natural cross-domain portability |

These modules currently serve primarily as **cross-layer type firewalls**. Their elementary finite mathematical substrates overlap established areas, so standalone mathematical novelty is not assumed.

---

## 15. Remaining frontier

The next theory development should target gaps that genuinely connect layers rather than add more labels.

1. **Reality -> model adequacy** — when does a model-world projection earn empirical adequacy rather than compatibility only?
2. **Beyond finite exact** — stochastic, continuous, approximate, delayed-observation, and tolerance-qualified state construction.
3. **Carrier-changing revision** — extend TU-1 through replacement relations/lifts and identify invariant revision cost.
4. **Learning/licensing coincidence** — necessary and sufficient conditions under which causal-learning and risk-limited target objectives agree.
5. **Empirical-state factorization** — define when measured coordinates genuinely make origin/history/mechanism residual information redundant out of sample.
6. **Warning-state empirical identification** — distinguish a mathematically sufficient warning state from coordinates that can actually be measured and validated in nature.

These remain open. They are not current theorem claims.

---

## 16. Boundary to empirical ecology

No empirical object enters the core merely by biological plausibility.

A concrete system must be projected as

\[
\text{empirical system}
\to
(\Omega,\mathcal C,O_{\mathcal D},T)
\]

with explicit empirical unit, time/cohort, measured and missing coordinates, reliability/calibration, validation design, and claim ceiling.

This is where thistles, island syndromes, flower-colour polymorphism, SDM-derived field design, visit cameras, and other concrete programmes will enter later.

---

## 17. Validation

```text
python theory/validate_core.py
python theory/validate_theory_graph.py
python theory/verify_tu1.py
python theory/verify_tu2.py
python theory/verify_tu3.py
python theory/verify_tu4.py
```

The theory validators enforce the type firewall and dependency graph. They do not convert finite witnesses into empirical ecological evidence.
