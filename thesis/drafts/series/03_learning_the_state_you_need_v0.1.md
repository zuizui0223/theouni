# Chapter 3 — Learning the State You Need

## Problem

Once a scientific responsibility requires a distinction among ecological mechanisms or states, two different measurement questions arise.

First:

> **Can the current or proposed observation map identify that distinction in principle?**

Second:

> **If several unresolved mechanisms remain and several measurements are available, which observation should be acquired next?**

These questions are often collapsed into “collect more data.” That shortcut fails when repeated or proximal measurements remain invariant along the same mechanism-equivalence class, and it wastes effort when available measurements differ sharply in the ambiguity they can resolve.

This chapter integrates `boundary` and `mrod` into one observation-design sequence while keeping their theorem scopes distinct.

## Standalone contribution

The paper-scale contribution is:

> **Mechanism-resolving measurement design has two gates: an observation must first change structural identification, and among measurements that can separate the remaining admissible mechanisms, acquisition should be ranked by current information value and recomputed after each realised outcome.**

The structural gate prevents “more of the same” data from being mistaken for mechanism resolution. The sequential-design gate prevents every technically measurable variable from being treated as equally useful.

## 1. Gate 1 — can the observation map reduce structural ambiguity?

Consider positive latent channels in log coordinates `x` and exact log-linear observations collected as rows of a matrix `M`.

For any nonempty compatible observation set, the mechanism-compatible affine set is

\[
x_0+\ker M.
\]

Therefore its structural dimension is

\[
\dim \mathcal C_y = k-\operatorname{rank}(M).
\]

Point identification occurs exactly when `rank(M)=k`.

### One new scalar observation

Appending an exact scalar observation with row `a^T` reduces the unidentified dimension iff

\[
a\notin \operatorname{rowspan}(M).
\]

For one scalar row, the dimension then falls by exactly one.

This gives a necessary-and-sufficient design rule:

> **A new exact observation improves structural identification iff it adds row rank to the current exact observation operator.**

Repeated measurements, nonzero rescalings, or exact linear combinations of existing observation rows can improve precision without changing the structural identification class.

The theorem does not claim that precision is statistically useless. It separates statistical precision from structural identification.

## 2. A field-like pollination witness

The structural point can be made without an abstract matrix alone.

Let effective service have three positive channels,

\[
W=V E D,
\]

where the symbols denote a declared visitation/quantity channel, per-interaction effectiveness, and a downstream dependency/reproductive channel.

Two latent mechanisms can produce the same currently observed records:

```text
(V,E,D) = (10, 0.4, 0.5)
(V,E,D) = (10, 0.2, 1.0)
```

Both yield

```text
V = 10
W = 2
W/V = 0.2
```

so the available exact rows have rank two for three latent channels. One structural degree of freedom remains. The same net service and the same currently derived ratio therefore do not identify whether the difference lies in effectiveness or dependency.

Add one exact effectiveness anchor `E`. The observation operator reaches rank three, and the final channel is recovered from

\[
D=W/(VE).
\]

This witness matters because it shows what the rank theorem means as field design:

> **the solution is not automatically more endpoint replication; it can require a qualitatively new channel-resolving measurement.**

## 3. Structural identifiability is not the whole design problem

After an observation map has been declared, a realistic mechanism-inference workflow may still retain many parameter–mechanism combinations compatible with the evidence already collected.

MROD represents the retained combinations as an admissible mechanism region

\[
A_\epsilon(y_{obs},x_{obs})
=
\{(\theta,s):G(\theta)=1,
 d(P_{sim}(f(x_{obs};\theta,s)),P_{obs}(y_{obs}))\le\epsilon\}.
\]

The method does not force one modal mechanism to stand in for the whole region. Remaining mechanism ambiguity is itself a scientific output and becomes the object of measurement design.

For a binary mechanism vector `S` with `K` components, residual entropy and normalized resolvability are

\[
D=H(S\mid A_\epsilon),
\qquad
R=1-D/K.
\]

## 4. Gate 2 — which verified candidate should be measured next?

Let a candidate observation `Q` have outcomes that form a verified mutually exclusive and exhaustive predictive partition of the current admissible region.

Its observation information value is

\[
V(Q)
=\frac{I(S;Q\mid A_\epsilon)}{K}.
\]

A candidate with zero current mutual information cannot reduce residual mechanism entropy under the declared region. A candidate whose predictive outcome partition is unavailable is not silently assigned an external prior and relabelled as validated information value; it is non-estimable for this quantity.

The sequential policy is:

```text
retain current admissible region
-> score every verified candidate by current V(Q)
-> choose the largest positive value
-> reveal only that selected outcome
-> condition the region
-> recompute all remaining values
-> stop when resolved, budget-limited, or information-limited
```

## 5. When does recomputation itself have strict value?

Sequential recomputation should not be defended merely by comparison with random measurement order.

Fix the first observation `X`. For each remaining candidate `q`, let

\[
U_q(x)=I(S;Q_q\mid X=x).
\]

The adaptive value of choosing the best second observation separately on each branch is

\[
V_{adapt}=E_X[\max_q U_q(X)],
\]

while the strongest precommitted static second measurement is

\[
V_{static}=\max_q E_X[U_q(X)].
\]

Then

\[
V_{adapt}\ge V_{static}.
\]

Equality holds exactly when one candidate is branchwise optimal on **every positive-probability branch**:

\[
V_{adapt}=V_{static}
\iff
\bigcap_{x:P(X=x)>0}\arg\max_q U_q(x)\neq\varnothing.
\]

Therefore recomputation has strict expected value iff there is no common branchwise maximizer.

A four-world witness gives branch-specific second-step information of `1` bit adaptively versus `0.5` bit for the best static second measurement. In the declared deterministic two-branch class, fewer than four worlds cannot produce the required strict branch switch.

This theorem is independent of the Boundary product/rank model. It operates inside any declared finite information-design setting satisfying its assumptions.

## 6. Frozen controlled validation

The principal validation is the frozen truth-peek-free MROD benchmark, not the pollination illustration.

The benchmark contains confounded generated systems, informative measurements, and mechanism-independent nuisance measurements. Hidden truth is used only after a policy has chosen a candidate, solely to materialise the realised outcome.

At budget two:

| outcome | information-guided | random order |
|---|---:|---:|
| initial confounding edges resolved | `1.000` | `0.6045` |
| systems converged | `0.990` | `0.435` |
| observations used | `1.505` | `1.821` |
| nuisance selections | `0.001` | `0.974` |

At budget four, both policies resolved all initial confounding edges on average, but nuisance selection remained sharply different:

- information-guided: `0.014` nuisance measurements per system;
- random order: `1.169`;
- approximately `83.5`-fold difference;
- observations used: `1.518` versus `2.673`.

Hidden-truth false exclusion was zero in every policy-by-budget cell.

These frozen results validate the declared observation-selection procedure against the declared random-order comparator. They do not prove global optimality against every experimental-design method.

## 7. Why Boundary and MROD belong in one methods chapter

Boundary and MROD solve consecutive design questions:

```text
1. Does a proposed measurement change what is structurally identifiable?
        Boundary

2. Conditional on the remaining admissible ambiguity,
   which verified candidate is most informative now?
        MROD
```

This sequence prevents two different errors.

### Error A — precision mistaken for identification

A measurement may be extremely precise yet remain in the row span of the current exact observation map. More replication of that measurement does not remove the structural ambiguity.

### Error B — all new measurements treated as equivalent

Several candidates can all add some new information but differ substantially in how they partition the currently admissible mechanisms. MROD ranks that current discriminating value and updates after outcomes are observed.

The integration therefore turns a Perspective plus a methods paper into one explicit **measurement-design pipeline**.

## 8. Internal dependency map

The paper must preserve the following boundaries.

- MROD does **not** mathematically require the multiplicative Boundary model.
- Boundary does **not** depend on the MROD synthetic benchmark.
- The Boundary theorem is a structural-identification layer and ecological worked example, not validation of the MROD algorithm.
- The MROD benchmark is the primary algorithmic validation and does not demonstrate a natural-system mechanism.
- The adaptive common-argmax theorem is stronger than comparison with random order, but it does not prove a globally optimal greedy multi-step policy.

Thus the relation is a scientific workflow, not theorem inheritance.

## 9. Relation to CREST without overclaiming

The preceding dissertation chapter asks what distinctions a scientific responsibility requires. This chapter asks whether those distinctions can be learned from observations.

The connection is conceptually strong but currently incomplete at the algorithmic level. Present MROD resolves a declared mechanism vector. CREST may require only target-relevant distinctions rather than full mechanism identity.

Therefore current MROD should **not** be described as the universal CREST monitoring optimizer.

A future extension could compare two objectives:

1. reduce full mechanism/state ambiguity;
2. reduce only ambiguity relevant to the declared CREST target.

That extension would make the vertical connection algorithmically explicit without being required for the present standalone methods paper.

## Manuscript strategy

Preferred integrated paper:

> **From Identifiability Limits to Mechanism-Resolving Observation Design**

Main text should prioritize:

1. ecological mechanism ambiguity and the two-gate measurement problem;
2. structural rank criterion plus one compact ecological witness;
3. admissible mechanism region and observation information value;
4. sequential recomputation theorem;
5. frozen controlled validation;
6. practical field-design interpretation and claim ceilings.

Detailed calibration transport, additional Boundary examples, MROD software contracts, and extended proofs can remain in Supplementary Information.

The existing standalone Boundary Perspective and frozen MROD submission package remain fallback artifacts until an integrated journal-format manuscript is fully audited.

## Claim ceiling

This chapter does **not** establish:

- that every ecological mechanism problem is multiplicative or log-linear;
- that every ambiguous mechanism set can be resolved by available measurements;
- that more data are generally useless when structural identification is unchanged;
- that MROD is globally optimal among all sequential experimental-design procedures;
- that the synthetic benchmark identifies a real ecological mechanism;
- that current MROD automatically targets the minimal CREST state rather than full declared mechanism identity.

## Source ownership

- observation-rank theorem, calibration/identification theory, and pollination-style structural witness: `zuizui0223/boundary`;
- admissible mechanism region, observation information value, adaptive recomputation theorem, frozen G2 benchmark, software and submission artifacts: `zuizui0223/mrod`;
- cross-source design sequence and dissertation handoff: `zuizui0223/theouni`.

## Dissertation handoff

The three research series now close a loop:

```text
Eco-genetic: different scientific jobs require different adequacy tests.
CREST: changing futures can change which distinctions the state must retain.
Observation design: identification and measurement determine which required distinctions can actually be learned.
```

The synthesis asks whether those revised responsibilities can be recovered from what earlier representations retained, returning to TU-1 and the reuse problem.
