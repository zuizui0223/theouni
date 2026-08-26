# Empirical Projection Gate v0.1 — admitting natural systems into the frozen Theory Universe v0.5

Status: **bridge protocol outside the frozen v0.5 semantic core**.

This document does not modify the Theory Universe v0.5 axioms or TU-1–TU-4. It defines how a real empirical system may be *projected into* that frozen theory without silently upgrading a plausible proxy, geographic label, or observed statistic into an ecological state.

The central question is:

> **What empirical evidence is required before a measured coordinate set may be treated as a target-relative partial state rather than merely as a predictor or correlate?**

---

## 1. The ideal factorization and the empirical limitation

In the ideal theory, a candidate state coordinate map

\[
Z:\Omega\to\mathcal Z
\]

is sufficient for a declared future target \(Y_{t+h}\) and action/context family \(A\) when the target response factors through \(Z\):

\[
\boxed{
\mathcal L(Y_{t+h}\mid \omega_t,a)
=
\mathcal L(Y_{t+h}\mid Z_t,a)
}
\]

for every admissible world \(\omega_t\) and declared action \(a\).

Natural data cannot verify this equality over unobserved ecological reality. Empirical state discovery therefore cannot prove a complete natural state merely by fitting a successful model.

The operational object is instead an **EmpiricalPartialState claim relative to a declared target, horizon, observation class, and validation scope**.

---

## 2. Three objects that must remain distinct

```text
biologically plausible coordinate set
        !=
predictive coordinate set
        !=
empirically supported partial state
```

A variable can be biologically plausible but nonpredictive.

A variable can be predictive yet still leave substantial target-relevant information in upstream geography, history, mechanism, cohort, or observation architecture.

A coordinate set earns partial-state status only after both its own endpoint information and its residual-context boundary are evaluated under leakage-free validation.

### 2A. What this gate adds beyond ordinary cross-validation

The gate does **not** claim a new causal estimator or a new generalization theorem.

Its added value over ordinary cross-validation is a **preregistered type-and-claim discipline** that couples, before outcome-driven expansion,

\[
(U,\tau,Z,H,A,Y,\mathcal O,\mathcal V,\Delta,\epsilon)
\]

with an ordered decision procedure and explicit claim ceiling.

In particular, it requires all of the following to be declared as part of one scientific object rather than chosen independently after model fitting:

- the ecological transfer unit `U`;
- temporal/cohort alignment `tau`;
- candidate state coordinates `Z`;
- upstream context/history set `H`;
- target/action family `A,Y`;
- observation/reliability contract `O`;
- whole-unit validation partition `V`;
- minimum candidate-state gain `Delta`;
- maximum tolerated residual-context gain `epsilon`;
- ordered failure classes from `not_identifiable` through bounded partial-state support.

The gate therefore adds **claim discipline and falsification order**, not causal identification by itself.

### 2B. Causal limitation

A candidate `Z` can pass held-out prediction even when its association with the target is noncausal, including cases where unmeasured structure influences both `Z` and `Y`.

Likewise, failure of the declared `H` set to add residual held-out information does not prove absence of all unmeasured confounding or hidden history. It establishes only bounded predictive redundancy for the **predeclared** context set and validation scope.

Therefore an E3 decision means:

> `Z` behaves as a target-relative predictive partial state under the declared transfer test.

It does **not** mean:

> `Z` is a causally sufficient state of nature.

Causal interpretation requires an additional mechanism/intervention/evidence bridge, potentially involving MRM, RACH, CED, or a domain-specific causal design.

---

## 3. Empirical projection contract

Every projection into Theory Universe v0.5 must declare:

\[
\mathcal P_{emp}
=
(U,\tau,Z,H,A,Y,\mathcal O,\mathcal V,\Delta,\epsilon).
\]

Where:

- \(U\): empirical unit, e.g. site × season, individual × cohort, population × observation window;
- \(\tau\): temporal/cohort alignment between candidate state and future target;
- \(Z\): candidate measured state coordinates;
- \(H\): upstream context/origin/history coordinates tested *after* \(Z\);
- \(A\): declared action/intervention/comparison family, when applicable;
- \(Y\): target endpoint at declared horizon;
- \(\mathcal O\): observation/reliability/calibration contract;
- \(\mathcal V\): leakage-free validation partition over whole ecological units;
- \(\Delta\): minimum predeclared gain required for candidate-state predictive support;
- \(\epsilon\): maximum residual-context gain tolerated for context redundancy.

The contract is frozen before outcome-dependent model expansion.

---

## 4. Gate G0 — provenance and synchronization

Before any state claim, the data must pass a synchronization gate.

Required checks include:

1. candidate coordinates and target belong to the same declared empirical unit or have an explicit cross-unit map;
2. candidate state is measured at or before the target horizon relevant to the contract;
3. cohort identity is preserved when genetics, recruitment, reproduction, or delayed response makes cohort relevant;
4. joins and labels are source-traceable;
5. no target outcome was used to repair schema, choose coordinates, relabel ecological units, or redefine the validation split after the preregistered gate;
6. access/schema failure is retained as `not_identifiable`, not converted to an ecological null.

Failure at G0 stops the projection.

---

## 5. Gate G1 — candidate-state predictive adequacy

Let \(R_0\) denote held-out risk for the preregistered baseline model and \(R_Z\) held-out risk after adding candidate state \(Z\). Lower risk is assumed better; an equivalent score orientation may be used if declared in advance.

A candidate state must first demonstrate endpoint-relevant information:

\[
\boxed{
R_0-R_Z\ge\Delta
}
\]

or pass an equivalent preregistered uncertainty rule.

The baseline is contract-specific. It may retain design variables, season, focal taxon identity, treatment strata, or other variables required to make the target comparison scientifically coherent.

### Interpretation

- If G1 fails: `candidate_state_not_predictively_supported`.
- Do **not** ask whether geography/history adds residual information after a candidate state that failed to predict the endpoint itself.

This ordering prevents a plausible proxy from receiving state status merely because an upstream label also fails.

---

## 6. Gate G2 — residual-context redundancy

Only after G1 passes, add the preregistered upstream context/history set \(H\).

Let \(R_{Z,H}\) be held-out risk for the augmented model.

Define residual-context gain

\[
G_H=R_Z-R_{Z,H}.
\]

Context redundancy is supported only when

\[
\boxed{
G_H\le\epsilon
}
\]

under the preregistered uncertainty/decision rule.

### Interpretation

- `G_H > epsilon`: `residual_context_detected` — the candidate state is incomplete for the declared target/validation class, or the current state coordinates are missing a process, memory, alignment, compensation, scale, or observation coordinate.
- `G_H <= epsilon`: `no_detected_residual_context_information` — upstream context did not add transferable predictive information beyond the candidate state within the declared scope.

This is a **bounded redundancy statement**, not proof that origin/history is biologically irrelevant and not proof of causal sufficiency.

---

## 7. Gate G3 — validation must hold out ecological units

The empirical projection must use a validation split that matches the claimed transfer unit.

Examples include:

- leave-one-site-out;
- leave-one-population-out;
- leave-one-garden-out;
- leave-one-array-out;
- leave-one-maternal-plant-out;
- leave-one-island/system-out for a cross-system claim.

Row-wise random splitting is insufficient when rows from the same ecological unit share environment, history, genotype, treatment, observer, or measurement process.

The validation unit is part of the claim.

---

## 8. Gate G4 — observation reliability remains separate

Predictive success does not erase observation error.

The projection must state which candidate coordinates are:

- direct measurements;
- calibrated proxies;
- uncalibrated proxies;
- latent model estimates;
- sensor-derived events;
- aggregate availability measures rather than realized interactions.

A coordinate may improve held-out prediction while remaining too poorly calibrated for a stronger mechanistic or causal claim.

Thus empirical-state adequacy and CED-style evidence licensing remain separate layers.

---

## 9. Gate G5 — target/action stress

A state claim is always target-relative.

If the scientific contract includes multiple targets, horizons, or interventions, the candidate state must be tested against that declared family rather than one convenient endpoint.

A coordinate set may therefore be:

```text
adequate for pollen receipt
but not for seed recruitment;

adequate for one-generation loss risk
but not for warning lead time;

adequate for present matching
but not for a future intervention.
```

Passing one endpoint never upgrades the coordinate set to a universal natural state.

---

## 10. Decision classes

The bridge uses the following ordered decisions.

### E0 — `not_identifiable`

G0 or a required reliability/schema/access gate fails. No ecological null is inferred.

### E1 — `candidate_state_not_predictively_supported`

G0 passes but G1 fails. The proposed coordinates do not earn state status for the declared target/horizon.

### E2 — `predictive_candidate_context_open`

G1 passes, but G2 detects residual upstream context. The coordinates carry target information but are incomplete as a context-closing partial state.

### E3 — `empirical_partial_state_supported`

G0–G4 pass, G1 passes, and no material residual context is detected under G2 for the declared validation class.

Meaning:

> the measured coordinates behave as a target-relative **predictive** empirical partial state within the tested scope.

Non-meanings:

> the complete natural state has been identified;

> the coordinates are causally sufficient;

> no unmeasured confounding/history remains.

### E4 — `portable_empirical_partial_state_supported`

E3 is independently reproduced across a predeclared external domain/system class while preserving target and observation semantics.

This is stronger than E3 but remains target/domain relative and still does not by itself establish causal sufficiency.

---

## 11. The missing-coordinate loop

A failed residual-context test is not merely a negative result. It generates a theory-guided next question.

```text
candidate Z predicts target
        |
        v
upstream H still adds held-out information
        |
        v
Z is incomplete
        |
        +--> search process coordinate
        +--> search history/memory coordinate
        +--> search cross-layer alignment
        +--> search compensation / alternative pathway
        +--> search scale/cohort mismatch
        `--> search observation/reliability coordinate
```

RACH can then be used to preserve multiple candidate explanations and design a next observation, but only after an explicit empirical observation map is supplied.

---

## 12. Relationship to TU-1 through TU-4

### TU-1

An E3 empirical partial state may be adequate for the current target yet still incur revision debt under a future contract. Empirical success today does not guarantee revisability tomorrow.

### TU-2

An observation that reduces causal ambiguity need not improve target prediction/licensing. Empirical state measurement and mechanism discrimination may therefore prefer different next observations.

### TU-3

Raw measurement dimensionality does not determine target-relevant state complexity. Additional measured coordinates matter only when they change the declared target response or close residual predictive information.

### TU-4

A coordinate set adequate for loss prediction need not be adequate for warning evaluation. Warning-state identification must test the joint loss + warning contract.

---

## 13. Reality-to-model claim ceiling

Passing E3 or E4 does **not** prove

\[
\mathfrak R\cong\Omega
\]

or that the candidate coordinates are ontologically complete.

The strongest admissible claim is conditional:

> Within the declared empirical unit, target, horizon, observation contract, candidate model class, and held-out transfer scope, the measured coordinates carried reproducible endpoint-relevant information and the preregistered upstream context set contributed no material residual predictive gain.

Anything stronger requires an additional bridge or broader validation.

---

## 14. Why this gate matters for the wider research universe

This protocol creates a single entry point for later concrete systems without letting those systems redefine the theory.

The same abstract gate can later receive:

- island functional-state candidates;
- floral trait / phenotype states;
- thistle evolutionary-process coordinates;
- SDM-derived environmental state candidates;
- sensor-derived interaction states;
- eco-genetic partial states.

They remain biologically different systems. What becomes comparable is the **scientific contract used to decide whether a measured representation closes the declared future target**.

Its main methodological contribution is therefore not "cross-validation plus a new name" but the requirement that prediction, residual-context testing, reliability, transfer unit, thresholds, and claim ceiling be declared as one typed contract before the state language is licensed.

---

## 15. Status

This document is a bridge/admission protocol, not TU-5 and not part of the frozen Theory Universe v0.5 semantic core.

The unresolved mathematical question remains whether useful generalization bounds or necessary/sufficient empirical-state identification results can be proved under explicit stochastic/model classes. Until then, E0–E4 are claim-discipline categories built around preregistered held-out factorization tests, not a proof of complete ecological ontology or causal state identification.
