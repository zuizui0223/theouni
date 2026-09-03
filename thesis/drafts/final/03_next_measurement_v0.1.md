<!-- draft-id: chapter:3:v0.1 -->
# 境界の内側で、次に何を測るか

*English working title: What to Measure Next Inside the Boundary*

> **Draft status:** source-bounded v0.1 from merged MROD snapshot `689ba17d14fec2218e9e96f4c9e432eb8b71fb58`. The chapter concerns mechanism-learning observation design inside a declared admissible mechanism family. Its headline theorem is an exact two-step condition for when adaptive recomputation strictly improves expected information over the best precommitted second measurement; the frozen G2 challenge remains a separate controlled validation layer.

## 1. The question is not whether information can rank measurements

Once multiple mechanisms remain compatible with current observations, “collect more data” is not yet a design. There may be many technically valid, biologically interesting and affordable candidate measurements. The scientific question is which candidate should be collected **now**, conditional on what remains unresolved.

The motivating forbidden inference is

> **測れるものは測る価値がある ⇒ 測る順序に良し悪しはない**

but merely defining an information score does not remove the obviousness problem. If a method says “measure the variable with the highest information,” a reviewer can reasonably ask whether the adaptive part of the procedure has any theorem-level content or merely repeats an algorithmic convention.

The nontrivial question is therefore narrower and stronger:

> **After a fixed first observation is taken, under exactly what condition can choosing the second measurement after seeing the first outcome achieve more expected mechanism information than every second measurement chosen in advance?**

MROD now answers that question with a necessary-and-sufficient condition. [M0]

The chapter still begins from the MROD principle of retaining compatible mechanisms rather than forcing a winner. But the scientific peak is no longer “we recompute the score.” It is the condition under which recomputation is strictly valuable.

## 2. The admissible mechanism region defines what is still unresolved

Let

\[
S\in\{0,1\}^K
\]

be a declared mechanism vector and let `theta` contain the remaining parameters. A pre-data biological grammar, fixed ecological context, observed targets, simulator/predictive map, discrepancy function and tolerance define an admissible mechanism region

\[
A_\epsilon
=\{(\theta,s):G(\theta)=1,
\ d(P_{sim}(f(x_{obs};\theta,s)),P_{obs}(y_{obs}))\le\epsilon\}.
\]

The implementation represents this region with accepted draws. The conceptual commitment is that multiplicity in `A_epsilon` is not removed merely because one row or mechanism combination has the largest mass. If multiple mechanism programmes remain compatible, that multiplicity is the object the next observation is supposed to resolve. [M1]

For the retained mechanism state, MROD reports joint entropy

\[
D=H(S\mid A_\epsilon)
\]

and normalized resolvability

\[
R=1-D/K.
\]

These quantities are not universal ecological uncertainty measures. They are typed to the declared mechanism vector. Their role is to make the remaining ambiguity explicit enough that a candidate observation can be evaluated against it.

The evidence roles are also fixed before selection: current observed targets may constrain `A_epsilon`; context variables condition the simulator; diagnostics remain diagnostics; future observations remain withheld until selection. The same variable is not allowed to define the current state, rank itself as a prospective measurement and then reappear as independent validation.

## 3. Candidate value requires a verified predictive partition

Let `Q` be a prospective measurement. When its possible outcomes form a mutually exclusive and exhaustive partition of the current admissible region, the stored region identifies the predictive outcome distribution needed for a mechanism-information calculation.

MROD uses

\[
V(Q)=\frac{I(S;Q\mid A_\epsilon)}{K}.
\]

Equivalently, this is the expected increase in normalized resolvability after observing `Q`. Thus a candidate can be perfectly measurable yet carry zero information about the particular mechanism distinctions that remain.

The partition condition matters. Missing prediction rows, overlapping outcome maps or incomplete outcome maps invalidate the stored-region information calculation. Such a candidate is reported as non-estimable unless an explicitly different predictive model is supplied. An external prior is not silently inserted and relabelled as the validated MROD value. [M1]

This fail-closed condition became important during the theorem upgrade. A stale Figure 1 regression test still pointed to a retired generator name. The fix did not resurrect that retired implementation; it connected the test to the current canonical information-value implementation and preserved the verified-partition semantics. The theorem PR then passed the full Python 3.10/3.11/3.12 suite. [M5]

## 4. The adaptive problem can be stated independently of random order

Consider a two-step finite design. The first observation has already been selected. Let its realised outcome be `X`, with positive-probability branches `x`. There is a finite set of remaining candidate measurements.

For each remaining candidate `q`, define its branch-specific second-step mechanism-learning value

\[
U_q(x)=I(S;Q_q\mid X=x).
\]

Dividing all values by `K` would give the normalized MROD scale and would not change any rankings or conclusions.

An adaptive policy is allowed to observe `X=x` and then choose whichever candidate has the highest value in that branch. Its expected second-step value is

\[
V_{adapt}
=\mathbb E_X\left[\max_q U_q(X)\right].
\]

A static policy must choose one candidate before `X` is known. The strongest possible static comparator is therefore

\[
V_{static}
=\max_q\mathbb E_X[U_q(X)].
\]

This comparator is deliberately stronger than the random-order policy used in G2. The theorem does not win by comparing an information policy with a weak random baseline. It asks whether adaptation itself can beat the **best candidate one could have precommitted to in expectation**. [M0]

## 5. Theorem A1: adaptation can never be worse than the best fixed second measurement

For every fixed candidate `q` and every branch `x`,

\[
\max_j U_j(x)\ge U_q(x).
\]

Taking expectations gives

\[
\mathbb E[\max_jU_j(X)]\ge\mathbb E[U_q(X)].
\]

Because this holds for every fixed candidate, it holds for the fixed candidate with the largest expected value:

\[
\boxed{V_{adapt}\ge V_{static}.}
\]

This inequality is simple, but it is not yet the main result. The critical question is when it is **strict**.

## 6. Theorem A2: exact condition for strict adaptive advantage

For each positive-probability branch, let

\[
A(x)=\operatorname{argmax}_qU_q(x)
\]

be the set of branchwise best candidates.

The theorem states

\[
\boxed{V_{adapt}=V_{static}}
\]

if and only if

\[
\boxed{\bigcap_{x:P(X=x)>0}A(x)\ne\varnothing.}
\]

Equivalently,

\[
\boxed{V_{adapt}>V_{static}}
\]

if and only if **no single remaining candidate is optimal in every positive-probability first-outcome branch**. [M0]

The sufficiency direction is direct. If some candidate `q*` belongs to every branchwise argmax set, then it attains the adaptive maximum branch by branch. Precommitting `q*` therefore matches the adaptive expected value.

For necessity, suppose equality holds and let `q*` be a static candidate attaining `V_static`. Define the nonnegative branchwise gap

\[
D(x)=\max_qU_q(x)-U_{q*}(x)\ge0.
\]

Equality of adaptive and static expected values implies

\[
\mathbb E[D(X)]=0.
\]

A nonnegative random variable has expectation zero only if it is zero on every positive-probability branch. Hence `q*` must be branchwise optimal everywhere.

This proof gives the exact replacement for the vague phrase “rankings can change after the first measurement.” Ranking movement alone is not enough. If one candidate remains tied for best in every branch, adaptation has no expected second-step advantage. Strict advantage requires the **common argmax intersection to be empty**.

## 7. A four-world witness attains a strict adaptive gain

The abstract condition has a minimal deterministic realization. Take four equally likely mechanism states

\[
S\in\{a,b,c,d\}.
\]

The first observation partitions them into two branches:

\[
X=0:\{a,b\},
\qquad
X=1:\{c,d\}.
\]

Two remaining deterministic candidates are designed as follows:

- `Q1` distinguishes `a` from `b` but is constant on `c,d`;
- `Q2` is constant on `a,b` but distinguishes `c` from `d`.

The branchwise mutual-information table is then

| first-outcome branch | `Q1` | `Q2` |
|---|---:|---:|
| `X=0` | 1 bit | 0 bits |
| `X=1` | 0 bits | 1 bit |

There is no common best candidate. Theorem A2 gives

\[
V_{adapt}=1\text{ bit},
\qquad
V_{static}=0.5\text{ bit}.
\]

The first observation itself carries one bit, so the two-step totals are two bits adaptively versus 1.5 bits with the best precommitted second candidate. [M0]

The source also establishes minimality within this deterministic branch-switch class. Strict branch switching needs at least two positive-probability branches. A branch containing only one mechanism state has zero conditional entropy, so every remaining candidate is tied at zero there and cannot eliminate a common maximizer. Therefore each of two branches needs at least two compatible mechanism states: four worlds are necessary, and the witness attains that lower bound.

This minimality matters. The example is not a large construction hiding an arbitrary advantage. It is the smallest deterministic branch structure capable of the strict effect under the declared class.

## 8. Sequential MROD uses the theorem's branch logic repeatedly, without claiming global greedy optimality

The publication-facing procedure computes current `V(Q)`, selects the largest positive value, obtains the realised outcome, conditions the admissible region and recomputes all remaining candidate values. [M1]

Theorem A2 justifies the possibility of strict value in recomputation. It does **not** prove that the entire multi-step greedy policy is globally optimal over every experiment tree. Such a result would require additional structural assumptions such as adaptive submodularity or a full dynamic-programming argument.

This distinction is important for claim discipline. The chapter can say exactly when adaptive choice at the second step beats every fixed second measurement. It cannot silently extend that theorem to arbitrary long-horizon design.

## 9. G2 is a separate controlled policy validation, not the proof of adaptation

The frozen G2 challenge tests information-guided sequential selection on 1,000 generated systems per policy across five predeclared seeds. Each generated system contains four to six mechanism switches, one or two designed confounds, explicit resolving candidates and two mechanism-independent nuisance candidates. Hidden truth is unavailable to the ranking calculation and is materialised only after selection. [M2]

At budget two, information-guided selection achieves mean initial-confounding resolution `1.000` and convergence `0.990`, compared with `0.6045` and `0.435` under random order. Nuisance selection is `0.001` versus `0.974` per system. Hidden-truth false exclusion remains zero. [M2]

At budget four, both policies reach mean edge resolution `1.000`, but guided design uses `1.518` observations compared with `2.673` for random order and selects `0.014` nuisance measurements compared with `1.169`. The nuisance ratio is about 83.5-fold; the absolute values must accompany that ratio. [M2]

G2 demonstrates that the current implementation can exploit designed information structure under a truth-peek-free protocol. But random order is not the comparator in Theorem A2. The theorem deliberately answers the stronger conceptual question: **when can adaptation beat the best fixed second candidate, not merely random order?**

## 10. Zero false exclusion prevents one trivial route to apparent success

A mechanism-resolution policy could appear powerful by conditioning away the hidden generating explanation. G2 therefore records whether hidden truth remains inside the admissible set.

False exclusion is zero in every policy-by-budget cell. [M2]

This does not prove robustness to model-family misspecification. It does establish that the benchmark's favourable resolution numbers are not produced by silently deleting the known generating mechanism within the declared family.

## 11. TU-2: the adaptive theorem is typed to mechanism learning

The observation value in this chapter has a declared object: residual mechanism identity. It is not a universal measure of scientific worth.

TU-2 constructs experiments with identical information about a causal programme state but opposite target-licensing status. It also constructs maximal causal learning with zero licensing of an independent target, and zero causal learning with perfect target licensing. [T2]

Thus Theorem A2 means:

> if branchwise optimal measurements disagree, adaptive recomputation strictly improves expected information about the declared mechanism state.

It does not mean:

> the adaptive choice is universally the best observation for every ecological decision, report target or reliability obligation.

This distinction is especially important because “information” can otherwise become an untyped word that swallows the rest of the dissertation.

## 12. What the chapter establishes

The chapter now has two independent result layers.

**Exact design condition.** For a fixed first observation and finite remaining candidate set, adaptive expected second-step mechanism information is at least that of the best precommitted second candidate, with strict advantage **iff** there is no candidate optimal on every positive-probability branch. A four-world deterministic witness attains a `1` versus `0.5` bit second-step contrast and is minimal within the declared branch-switch class. [M0]

**Controlled implementation validation.** In the frozen truth-peek-free G2 challenge, current information-guided sequential selection resolves designed confounds more efficiently than random ordering and avoids mechanism-independent nuisance measurements while retaining hidden truth. [M2]

The chapter does **not** prove global optimality of arbitrary multi-step greedy design, completeness of the mechanism vocabulary, natural-system causal truth, or universal scientific utility of the MROD score. It does not rescue Chapter 2's failed warning thresholds. [M4]

The safe conclusion is:

> **Measurement order has a provable adaptive advantage exactly when first-observation outcomes create incompatible optimal next measurements; the controlled MROD benchmark then shows that the implemented policy can exploit such mechanism-relevant information without truth peeking.**

## 13. Transition: a good measurement policy still needs a correctly typed state

Theorem A2 tells us when adaptation improves a declared mechanism-learning objective. It does not tell us whether the state or target being learned should itself be represented by one scalar summary.

Chapter 4 asks that next question. Potential viability, realised occupancy, demographic condition, genetic diversity and allele persistence may impose different response responsibilities. The source chapter proves an exact condition for when several oriented targets can be represented by one common monotone scalar, and then tests that condition against the locked fragmentation gradient. [TR]

Thus the transition is not “MROD proves multiple ecological states.” It is:

> **Once observation value is explicitly relative to a learning object, under what condition can several ecological responsibilities share one state axis at all?**

## Internal source keys

- **[M0]** MROD `docs/adaptive_recomputation_theorem_2026-09-03.md` and `tests/test_adaptive_recomputation_theorem.py` — A1/A2, common-argmax iff, four-world witness and minimality.
- **[M1]** MROD `docs/mainline.md`, `paper/manuscript.md`, and current canonical information-value implementation — admissible region, verified predictive partition, `V(Q)=I(S;Q|A_epsilon)/K`, sequential conditioning.
- **[M2]** MROD `paper/results/g2_frozen_v2_summary.json` and `paper/check_submission_bundle.py` — frozen G2 counts, nuisance selections, convergence and zero false exclusion.
- **[M4]** `thesis/verification_recovery_registry.json`, Chapter 3 claim ceiling.
- **[M5]** MROD PR #101 CI recovery — stale retired Figure 1 import removed; current canonical test suite passes Python 3.10/3.11/3.12.
- **[T2]** `theory/TU2_LEARNING_LICENSING.md` and `theory/verify_tu2.py` — mechanism learning versus target licensing firewall.
- **[TR]** `thesis/transition_recovery_matrix.json` — Chapter 3→4 is a question handoff, not theorem implication.
