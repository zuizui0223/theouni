# Positive bridge v0.1 — RACH -> MRM -> CED

Status: **implemented finite cross-layer bridge outside the frozen v0.5 core**.

Purpose: demonstrate that Theory Universe consistency is not obtained only by forbidding type collapses. This bridge composes three source-owned layers into a positive scientific statement.

Source semantics are pinned to:

- RACH / `microdonta` snapshot `f7303c4a618d432949177c424adaafeb9c78f1d3`;
- MRM snapshot `12b4fc375d96a18b9b18cb625861aa028e77a73e`;
- CED snapshot `85aad0092e743a35d5c41ff0665b954a5cfd77c0`.

The bridge does not transfer theorem ownership.

---

## 1. Question

Suppose current observations leave several causal programmes admissible.

Must science identify one true causal programme before it can make a deterministic ecological report?

The answer is **no** when all remaining programmes are equivalent for the declared response/target and the observation architecture reliably resolves whatever response distinction remains.

This gives the positive chain

```text
RACH admissible causal set
        ->
MRM response-equivalence quotient
        ->
CED evidence/reportability audit
        ->
licensed deterministic or set-valued target report
```

---

## 2. Shared finite carrier

Fix ecological context `x` and let RACH return a finite admissible causal set

\[
A\subseteq\mathcal M.
\]

Construct one latent world for each admissible programme:

\[
W_A=\{w_m:m\in A\}.
\]

This bridge is conditional on this explicit map. It does not assert that causal programmes are literally natural worlds in every application.

---

## 3. MRM response map

Let

\[
\rho:W_A\to\mathcal R
\]

be the declared response signature under the intervention/action family relevant to the scientific contract.

Two admissible causal programmes are MRM-equivalent when

\[
\rho(w_m)=\rho(w_{m'}).
\]

This induces the response partition

\[
Q_\rho=W_A/\ker\rho.
\]

Let the requested report target be

\[
T:W_A\to\mathcal Y.
\]

The strongest simple bridge assumes `T` is constant within each response class; equivalently

\[
T=t\circ\rho
\]

for some map `t`.

---

# 4. Positive result A — causal multiplicity can be report-irrelevant

If all currently admissible programmes lie in one MRM response class,

\[
|Q_\rho|=1,
\]

then the response signature is already deterministic over the RACH admissible set even when

\[
|A|>1.
\]

If `T=t o rho`, the requested target is also deterministic over `A`.

Therefore:

\[
\boxed{
\text{causal singleton is not necessary for a mechanism-robust deterministic target.}
}
\]

This is a positive composition statement: RACH may honestly retain multiple causal explanations while MRM shows that their remaining disagreement is irrelevant to the declared report.

---

## 5. CED evidence layer

Let a declared CED experiment/reliability contract induce a reliability-qualified evidence partition

\[
E_D
\]

on `W_A`.

For a realized evidence class `e`, define

\[
W_e=\{w\in W_A:[w]_{E_D}=e\}.
\]

CED's honest-report criterion gives:

### Target report

A deterministic target report is licensed on evidence class `e` iff

\[
\boxed{
T\text{ is constant on }W_e.
}
\]

### Full response-class report

A deterministic MRM response-class report is licensed iff

\[
\boxed{
\rho\text{ is constant on }W_e.
}
\]

If the condition fails, the sharp report is the set of compatible target values or response classes.

---

# 6. Positive result B — response-class resolution is enough

Suppose one CED evidence class contains multiple admissible causal programmes but only one MRM response class:

\[
|W_e|>1,
\qquad
|\rho(W_e)|=1.
\]

Then:

- causal identity remains unresolved;
- the response class is deterministic;
- every target that factors through `rho` is deterministic;
- full causal-programme identification is unnecessary for that report.

Thus

\[
\boxed{
\text{RACH ambiguity can survive while MRM/CED target reporting is fully licensed.}
}
\]

This is the bridge's main non-vacuous scientific statement.

---

## 7. Positive result C — evidence must resolve only report-relevant disagreement

If an evidence partition refines the target partition but not the causal-programme partition, CED can license the target without identifying the mechanism.

If it further refines the MRM response partition, it can license the full response class without identifying the exact causal programme.

Hence the natural resolution hierarchy is

```text
exact causal programme
        finer than or equal to
MRM response class
        finer than or equal to
requested target class
```

with equality depending on the scientific contract.

Monitoring effort should therefore be evaluated against the **coarsest report-relevant unresolved distinction**, not against causal identity by default.

---

## 8. Where RACH next-observation design enters

RACH may rank a candidate observation `Q` by validated causal-learning value such as

\[
I(S;Q\mid A_\epsilon)/K.
\]

The bridge does not convert that score into a CED license.

To pass from a RACH candidate observation to a CED-approved experiment, the candidate must additionally acquire:

- an explicit record/outcome map;
- a reliability/failure/calibration contract;
- a target/report objective;
- the corresponding evidence partition or risk-limited reporting rule.

This preserves TU-2:

```text
RACH observation value
    !=
CED target licensing value
```

while still giving a positive composition route.

---

## 9. Finite witness

Take four admissible causal programmes

```text
m1, m2, m3, m4
```

with MRM response classes

```text
R0 = {m1, m2}
R1 = {m3, m4}
```

and target

```text
T=0 on R0
T=1 on R1.
```

An experiment that observes only the response class has evidence classes

```text
{m1,m2}, {m3,m4}.
```

For either realized class:

- two causal programmes remain admissible;
- one response class remains;
- one target remains;
- deterministic target reporting is licensed.

An uninformative experiment with evidence class

```text
{m1,m2,m3,m4}
```

leaves two target values and therefore requires an ambiguity-explicit report.

The executable witness is `theory/bridges/verify_rach_mrm_ced_bridge.py`.

---

## 10. Claim ceiling

This bridge establishes a finite exact composition on an explicit shared carrier.

It does **not** establish:

- that a RACH admissible causal programme is the true natural mechanism;
- that every RACH model family can be embedded into an MRM world carrier canonically;
- that MRM and CED operators commute in arbitrary models;
- that a high-NOV RACH observation is reliable or target-optimal;
- empirical calibration of any real sensor or experiment;
- a new standalone quotient theorem independent of the source programmes.

The scientific value is compositional:

> **unresolved causal multiplicity need not block a deterministic report when all compatible causal programmes agree at the response/target resolution actually required, and evidence need only resolve remaining report-relevant disagreement.**
