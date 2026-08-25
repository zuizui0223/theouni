# TU-2 — Causal learning and target licensing are orthogonal

> **Status:** finite exact bridge theorem module. The construction is elementary; the programme contribution is to make the RACH learning objective and CED reportability objective explicitly non-interchangeable inside one typed ecological world universe.

## 1. Question

RACH and CED both influence what should be measured next, but they answer different questions.

RACH's validated NOV uses causal-programme information gain,

\[
\operatorname{NOV}(Q)=\frac{I(S;Q\mid A_\epsilon)}{K},
\]

for a verified candidate outcome partition, where `S` is the retained causal/switch state and `K` is the declared normalization/cost factor.

CED asks whether the resulting evidence class licenses the requested target. In the deterministic exact setting, target `T` is licensed after record `q` exactly when `T` is constant on the compatible world class.

TU-2 asks:

> Does more causal learning imply more target licensing, or vice versa?

The answer is no, even in the smallest noiseless finite setting.

## 2. Product-world construction

Fix integer \(m\ge1\).

Let the causal programme state be

\[
S=(S_1,\ldots,S_m)\in\{0,1\}^m
\]

and let the report target be

\[
T\in\{0,1\}.
\]

Take the finite world universe

\[
\Omega=\{0,1\}^m\times\{0,1\},
\]

with the uniform distribution, so `S` and `T` are independent.

For \(k\in\{0,\ldots,m\}\) and \(b\in\{0,1\}\), define experiment

\[
Q_{k,b}=
\begin{cases}
(S_1,\ldots,S_k), & b=0,\\
(S_1,\ldots,S_k,T), & b=1.
\end{cases}
\]

Thus `k` controls how much causal state is revealed, while `b` controls whether the target itself is resolved.

## 3. TU-2A — exact orthogonality theorem

### Theorem

For every \(k\in\{0,\ldots,m\}\):

\[
\boxed{I(S;Q_{k,0})=I(S;Q_{k,1})=k\text{ bits}.}
\]

But target licensing differs maximally:

\[
\boxed{L_T(Q_{k,0})=0,\qquad L_T(Q_{k,1})=1,}
\]

where `L_T=1` means every possible resulting evidence class has one deterministic target value, and `L_T=0` means none does.

### Proof

`Q_{k,b}` reveals exactly the first `k` independent fair causal bits. Because `T` is independent of `S`, appending `T` changes no mutual information about `S`. Hence both experiments have causal information gain `k` bits.

When `b=0`, every record fixes at most `S_1,...,S_k` and leaves both target values compatible because `T` is independent and unobserved. Therefore the CED-style target report remains `{0,1}` for every record.

When `b=1`, every record contains `T`; each compatible class is target-constant. Hence deterministic target reporting is licensed for every record. ∎

## 4. Corollary — no causal-information score can determine target licensing

For each possible causal information gain `k`, there are two experiments with exactly the same `I(S;Q)` but opposite target-licensing status.

Therefore no function of causal information gain alone can recover whether the target is licensed.

With the RACH normalization `NOV=I(S;Q)/m` and equal experiment cost, the same statement holds for every normalized score in

\[
\{0,1/m,\ldots,1\}.
\]

## 5. TU-2B — maximal RACH learning with zero target licensing

Take

\[
Q_{m,0}=S.
\]

Then

\[
I(S;Q_{m,0})=m,
\qquad
\operatorname{NOV}=1
\]

under normalization by `m` causal coordinates.

Yet `T` remains independent and unresolved, so

\[
L_T(Q_{m,0})=0.
\]

Thus even maximal causal-state learning need not license the requested ecological target.

## 6. TU-2C — zero RACH learning with complete target licensing

Take

\[
Q_{0,1}=T.
\]

Then

\[
I(S;Q_{0,1})=0,
\qquad
\operatorname{NOV}=0,
\]

but

\[
L_T(Q_{0,1})=1.
\]

Thus an observation can be completely useless for resolving the retained causal programme while being perfectly sufficient for the declared report target.

## 7. Policy reversal

Consider equal-cost choices between

- `Q_causal = Q_{m,0}`;
- `Q_target = Q_{0,1}`.

A policy maximizing RACH-style causal information chooses `Q_causal`.

A policy whose sole terminal objective is deterministic target licensing chooses `Q_target`.

Hence the two design objectives can rank the same two experiments in exactly opposite order.

This is not a contradiction. It is a difference of estimand.

## 8. Why this does not duplicate CED

CED already contains target-relative counterexamples in which full-world information gain can prefer target-irrelevant measurements. TU-2 is narrower and cross-typed:

- the learning variable is specifically the **RACH causal programme state** `S`;
- the reporting object is specifically the **CED target** `T`;
- both are embedded in one common `World` type;
- the construction proves that causal-learning value and target-licensing value are independently variable.

TU-2 therefore acts as a bridge firewall between repositories rather than as a replacement for either repository's own design theory.

## 9. Failure-aware extension belongs to CED

TU-2 uses noiseless deterministic records to isolate semantic orthogonality.

In a real observation architecture, even an experiment that nominally separates target values may fail CED's reliability/risk contract because of shared failure modes, calibration uncertainty, false positives, missed detection, or non-reset dependence.

Thus failure-aware licensing can only add another gate:

```text
causal learning value
    != nominal target separation
    != reliability-qualified target licensing
```

TU-2 does not re-prove CED's failure theorems.

## 10. Type firewall

TU-2 forbids these upgrades:

- `high NOV => licensed target`;
- `low NOV => scientifically useless observation`;
- `causal programme identified => target identified`;
- `target identified => causal programme identified`;
- `nominal target separation => reliability-qualified report`.

## 11. Interpretation

The theory-universe reading is:

> **Learning is always learning of a declared object.** Reducing uncertainty about causal explanation, reducing uncertainty about required state, and licensing a requested target are different scientific achievements.

The correct next observation therefore cannot be defined before the scientific responsibility is typed.

This strengthens the programme question:

> What may science safely forget — and **what exactly is science trying to learn next?**

## 12. Claim ceiling and prior-art boundary

The product construction and mutual-information calculation are elementary. Decision-relevant versus task-irrelevant information is a broad prior-art theme in information theory, statistics, active learning, and experimental design.

No standalone novelty claim is made for the abstract fact that information about one variable need not resolve another.

The role of TU-2 is to make the RACH/CED distinction exact inside the ecological state universe and to prevent future bridge code from silently replacing licensed resolution with an information-gain proxy.

## 13. Next extension

A stronger TU-2D should incorporate a reliability-qualified CED experiment family and characterize when RACH ranking and CED risk-limited ranking coincide.

A natural condition to test is whether every causal-programme distinction cut by an experiment is target-relevant **and** every nominal target split is trustworthy under the same failure domain.

That coincidence theorem is open.
