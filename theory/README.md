# Theory Universe v0.5.1 — contract-relative ecology with clarified evidence and loss semantics

This directory is the **theory-first core** of `theouni`.

The immutable semantic base is **Theory Universe v0.5**. The current interpretation is **v0.5.1**, which adds only two semantic clarifications without changing TU-1–TU-4 results, dependency direction, or claim ceilings:

1. `D_req` (pre-observation evidence/reliability requirement) is distinct from realized evidence `E_y^{D_req}`;
2. `LossResponseSignature` means the **full contract-complete loss-response signature** `Sigma_{C_L}`, not one convenient scalar loss summary.

Version pointers:

- [`CURRENT.json`](CURRENT.json) — current theory version and base freeze;
- [`FREEZE_v0.5.json`](FREEZE_v0.5.json) — immutable v0.5 semantic-core manifest;
- [`CONSTITUTION.md`](CONSTITUTION.md) — frozen v0.5 constitution;
- [`CLARIFICATION_v0.5.1.md`](CLARIFICATION_v0.5.1.md) — current semantic clarification layer;
- [`clarification_v0.5.1.json`](clarification_v0.5.1.json) — machine-readable clarification contract.

The programme question remains:

> **What may science safely forget, what must remain revisable, and which distinctions are required by the scientific question actually being asked?**

The v0.6 generalization remains a draft outside this current v0.5.1 interpretation. Its entrypoints are:

- [`DRAFT_v0.6_CONTRACT_INDEXED_QUOTIENT_TRANSPORT.md`](DRAFT_v0.6_CONTRACT_INDEXED_QUOTIENT_TRANSPORT.md) — theory-spine statement;
- [`contract_indexed_adequacy_registry.json`](contract_indexed_adequacy_registry.json) — machine-readable CIRA-1 through CIRA-5 and exact/graded specialization branches;
- [`CONTRADICTION_CERTIFICATE_v0.6.md`](CONTRADICTION_CERTIFICATE_v0.6.md) — generated 12-module, 66-pair typed contradiction certificate;
- [`contradiction_matrix.json`](contradiction_matrix.json) and [`validate_contradiction_matrix.py`](validate_contradiction_matrix.py) — canonical audit data and fail-closed validator.

The pairwise result is `actual-conflict = 0` at current claim ceilings. It is not a global-consistency, empirical-truth, or bridge-completion claim.

---

## 1. One universe, five layers

Theory Universe separates:

1. **Reality** — temporally extended ecological reality \(\mathfrak R\).
2. **Model worlds** — a declared mathematical universe \(\Omega\).
3. **Representation** — contract-relative quotients such as `RequiredState`, `LossGeneratingState`, and `WarningEvaluationState`.
4. **Epistemology** — realized evidence classes, reportability, admissible causal sets, and learning.
5. **Cross-time / cross-representation operations** — revision after compression, representation change, and warning portability.

The first firewall is

\[
\boxed{
\text{Reality}\neq\text{ModelWorld}\neq\text{Snapshot}\neq\text{RequiredState}.
}
\]

A theorem on model worlds is not automatically a theorem about nature.

---

## 2. World before state

A temporally extended model world can be written schematically as

\[
\omega_t=(h_{\le t},x_t,\theta_t,K_t),
\]

where history, present configuration, retained mechanism, and future-response structure may matter.

The canonical scientific contract is now written

\[
\boxed{
\mathcal C=(\Gamma,\mathcal H,\Theta,\mathcal D_{\rm req};T).
}
\]

Here:

- \(\Gamma\): future/intervention responsibilities;
- \(\mathcal H\): historical/semantic responsibilities;
- \(\Theta\): retained mechanism responsibilities;
- \(\mathcal D_{\rm req}\): **pre-observation** experiment, calibration, failure, reliability, resolution, and reporting requirements;
- \(T\): requested target/report/decision.

Two worlds may be merged only when they are scientifically interchangeable for the declared contract. The required state is

\[
\boxed{
S_{\mathcal C}=\Omega/\sim_{\mathcal C}.
}
\]

The state is the **maximal lawful forgetting** compatible with the contract.

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

is well-defined only if all worlds merged into one state agree on every contract-relevant response.

A law may stop transporting after a contract or ecological structure changes because the old quotient ceases to be adequate, even though the law was valid in its original domain.

---

## 5. Evidence requirement is not realized evidence — CED layer

The v0.5.1 distinction is

\[
\boxed{
\mathcal D_{\rm req}\neq E_y^{\mathcal D_{\rm req}}.
}
\]

`D_req` is declared **before** observation and specifies what observation/reliability architecture counts as acceptable.

After a realized record \(y\), define

\[
\boxed{
E_y^{\mathcal D_{\rm req}}
=
\{\omega\in\Omega:
\omega\text{ remains compatible with }y
\text{ under }\mathcal D_{\rm req}\}.
}
\]

This is an epistemic object.

Therefore

\[
\boxed{
\text{RequiredState}\neq\text{RealizedEvidenceClass}\neq\text{Report}.
}
\]

The canonical separation remains

\[
\boxed{
\text{required state}\neq\text{identified state}\neq\text{reportable target}.
}
\]

The correct direction is

```text
ScientificContract / D_req -> required distinctions
realized observation y     -> E_y^{D_req}
required + identified      -> licensed report
```

and not

```text
realized data -> structural distinction by decree
```

Where older v0.5 prose writes `C_{D,T}`, v0.5.1 reads it as `C_{D_req,T}`: the **required resolution/reportability responsibility**, not the accidental contents of the realized sample.

CED owns the finite evidence, failure, calibration, risk, and reportability layer.

---

## 6. Causal uncertainty is set-valued — RACH layer

For declared causal programmes \(m\) supporting world subsets \(\Omega_m\), define

\[
A(y)=\{m:\Omega_m\cap E_y^{\mathcal D_{\rm req}}\neq\varnothing\}.
\]

This is the `AdmissibleCausalSet`, not a best-model winner.

RACH keeps compatible causal programmes and designs next observations that reduce unresolved causal ambiguity. For verified candidate outcome partitions, its publication-facing information quantity is schematically

\[
\operatorname{NOV}(Q)=\frac{I(S;Q\mid A_\epsilon)}{K}.
\]

An observation can be valuable for causal learning without licensing the requested ecological target; TU-2 formalizes that firewall.

---

## 7. Dynamics, simulator state, and contract-complete target state

Model worlds evolve under a declared dynamics law

\[
\omega_{t+1}\sim K(\cdot\mid\omega_t,a_t).
\]

A `CompleteSimulatorState` can be future-sufficient under one explicit simulator closure without being minimal, natural, or empirically observable.

For any target-specific state, the response object used to define equivalence must be complete for the declared scientific responsibility. A convenient scalar response is sufficient only if it has independently been shown to exhaust the contract.

This requirement is especially important for TU-3 and loss state.

---

# 8. `theouni` theorem modules

## TU-1 — Contract revision after compression

CREST asks what state is adequate while the full common carrier is still available. TU-1 asks what happens **after a previous state has already been stored**.

Let \(P\) be the old stored-state partition and \(Q\) the revised required partition. State-only revision exists iff

\[
q_Q=f\circ q_P.
\]

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

Scientific compression can be adequate today but unrevisable for a later scientific responsibility.

Source: [`TU1_CONTRACT_REVISION.md`](TU1_CONTRACT_REVISION.md).

---

## TU-2 — Causal learning is not target licensing

RACH and CED assign value to different scientific objects.

Finite constructions give both

\[
\operatorname{NOV}=1,\quad L_T=0,
\]

and

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

Let the loss contract be

\[
\mathcal C_L
=(\Gamma_L,\mathcal H_L,\Theta_L,\mathcal D_{L,\rm req};T_L).
\]

Let \(\mathcal Q_L\) index **all loss-relevant query contexts required by that contract**, including declared actions/interventions, horizons/stopping rules, retained history/mechanism semantics, and target/report distinctions when applicable.

The full loss-contract response signature is

\[
\boxed{
\Sigma_{\mathcal C_L}(\omega)
=
\bigl(R_q(\omega)\bigr)_{q\in\mathcal Q_L}.
}
\]

The loss-generating quotient is

\[
\boxed{
Q_L
=
\Omega/\ker\Sigma_{\mathcal C_L}.
}
\]

A representation projection \(\pi:X\to Z\) is loss-faithful iff the **full signature** factors through it:

\[
\boxed{
\Sigma_{\mathcal C_L}
=
\bar\Sigma_{\mathcal C_L}\circ\pi.
}
\]

A quotient based only on one loss probability, one threshold time, or one horizon is merely a candidate loss quotient unless that summary has been shown to exhaust `C_L`.

If `Sigma_{C_L}` exhaustively encodes the loss-specialized CREST responsibilities on the declared common carrier, then

\[
Q_L\cong S_{\mathcal C_L}.
\]

Therefore

\[
\boxed{
\text{raw simulator-state complexity}\neq\text{contract-complete loss-state complexity}.
}
\]

Source: [`TU3_LOSS_STATE_INVARIANCE.md`](TU3_LOSS_STATE_INVARIANCE.md), interpreted through [`CLARIFICATION_v0.5.1.md`](CLARIFICATION_v0.5.1.md).

---

## TU-4 — Warning evaluation state and portability

Let \(\Sigma_G(\omega)\) be the warning response required by the warning contract. The warning-evaluation signature is

\[
\boxed{
\Sigma_W(\omega)
=
\bigl(\Sigma_{\mathcal C_L}(\omega),\Sigma_G(\omega)\bigr).
}
\]

The warning-evaluation quotient therefore satisfies

\[
\boxed{
Q_L\preceq Q_W.
}
\]

Equality holds iff the required warning response factors through the **full loss-contract state**.

Thus two distinct warnings are protected against collapse:

```text
same scalar loss summary
    does not imply
same LossGeneratingState

same LossGeneratingState
    does not imply
same WarningEvaluationState
```

Warning portability across domains is an additional commutation condition on a declared cross-state correspondence; within-state reproducibility does not imply portability.

Source: [`TU4_WARNING_STATE_PORTABILITY.md`](TU4_WARNING_STATE_PORTABILITY.md), interpreted through [`CLARIFICATION_v0.5.1.md`](CLARIFICATION_v0.5.1.md).

---

## 9. Canonical state hierarchy

```text
ModelWorld
   |
   +--> RequiredState(C)
   |
   +--> CompleteSimulatorState
   |
   +--> LossGeneratingState          [full contract-complete loss signature]
   |       |
   |       `--> WarningEvaluationState [joint full loss + warning response]
   |
   `--> E_y^{D_req}                  [NOT ontic state; realized epistemic class]
```

In particular,

\[
\boxed{
\text{CompleteSimulatorState}
\neq
\text{LossGeneratingState}
\preceq
\text{WarningEvaluationState}.
}
\]

---

## 10. Canonical worldline

### Ontic / representational

```text
Reality
  -> model / measurement bridge
  -> ModelWorldUniverse
  -> ScientificContract C=(Gamma,H,Theta,D_req;T)
  -> RequiredState
```

### Epistemic / learning

```text
World + D_req
  -> ObservationRecord y
  -> E_y^{D_req}
       |\
       | `--> TargetLicensingStatus / Report
       `----> AdmissibleCausalSet
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
LossContract C_L
  -> full Sigma_{C_L}
  -> TU-3 LossGeneratingState
       + Sigma_G
       -> TU-4 WarningEvaluationState
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
| `D_req = E_y^{D_req}` | contract requirement and realized evidence are different layers |
| `EvidenceClass = RequiredState` | epistemic resolution differs from structural adequacy |
| `CompleteSimulatorState = RequiredState` | sufficiency does not prove minimality/naturality |
| `CompleteSimulatorState = LossGeneratingState` | target-relative quotient may be much coarser |
| `single loss summary = LossGeneratingState` | only valid after full-contract sufficiency is established |
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

Source theorem/evidence ownership is never transferred merely because objects appear in the same theory graph.

---

## 13. Frozen base and current clarification

The frozen dependency DAG is [`theorem_graph.json`](theorem_graph.json).

The immutable v0.5 semantic core remains protected by [`FREEZE_v0.5.json`](FREEZE_v0.5.json).

The current v0.5.1 overlay does **not** alter dependency direction. It only prevents two dangerous readings:

```text
D_req == realized evidence
```

and

```text
one loss statistic == full loss-contract state
```

Both are now forbidden.

---

## 14. Current theorem modules and claim ceilings

| Module | Closed finite result | Major non-claim / open extension |
|---|---|---|
| TU-1 | same-carrier revision criterion + exact idealized revision debt + local/global divergence | carrier-changing revision; physical irreversibility; empirical measurement cost |
| TU-2 | causal-learning/target-licensing orthogonality and policy reversal | reliability-aware coincidence theorem; generic active-learning novelty |
| TU-3 | full-response factorization + representation-faithful loss quotient + nuisance inflation | recursive stochastic quotient dynamics; empirical natural-state minimality |
| TU-4 | warning-state refinement/equality criterion + finite portability commutation | universal thresholds; natural cross-domain portability |

The v0.5.1 patch narrows signature interpretation; it does not expand any theorem claim.

---

## 15. Remaining frontier

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
(\Omega,\mathcal C,O_{\mathcal D_{\rm req}},T)
\]

with explicit empirical unit, time/cohort, measured and missing coordinates, reliability/calibration, validation design, and claim ceiling.

---

## 17. Validation

```text
python theory/validate_core.py
python theory/validate_theory_graph.py
python theory/verify_tu1.py
python theory/verify_tu2.py
python theory/verify_tu3.py
python theory/verify_tu4.py
python theory/validate_freeze.py
python theory/validate_clarification_v0_5_1.py
python theory/verify_contract_indexed_quotient_transport.py
python theory/validate_contradiction_matrix.py
python theory/validate_revision_and_positive_bridge.py
python theory/bridges/verify_rach_mrm_ced_bridge.py
```

The frozen v0.5 validator guarantees that the historical core did not drift. The v0.5.1 validator guarantees that `D_req`/`E_y` and full loss-contract signature semantics remain separated. The draft v0.6 validators guarantee registry completeness, exact/graded branch separation, and a complete 66-pair certificate with zero registered `actual-conflict` relations.
