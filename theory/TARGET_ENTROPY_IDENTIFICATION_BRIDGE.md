# Target image cardinality, entropy, and effective multiplicity

> **Status:** finite exact bridge theorem. `boundary` retains ownership of set-valued target identification; `mrod` retains ownership of target-oriented observation information. This file records their exact overlap on a finite positive-weight admissible support.

Let `A` be the current finite admissible set of worlds/rows and let `T` be a declared target. Assume every stored row has strictly positive weight.

`boundary`-style target ambiguity retains the image

```text
T(A)={T(w): w in A}
```

with cardinality

```text
m=|T(A)|.
```

`MROD` target-aware observation value starts from the weighted entropy

```text
H(T|A).
```

## Exact point-identification equivalence

For finite positive-weight support,

```text
|T(A)|=1
iff
H(T|A)=0.
```

Finite Shannon entropy is zero exactly when all positive probability mass lies on one target value. Strictly positive row weights make the positive-probability target support equal to the target image of the stored admissible rows.

## Graded bridge: effective target multiplicity

More generally,

```text
0 <= H(T|A) <= log2 m.
```

Define

```text
N_eff(T|A)=2^{H(T|A)}.
```

Then

```text
1 <= N_eff(T|A) <= |T(A)|.
```

Interpretation:

```text
|T(A)|
= number of distinct target values still structurally compatible,

N_eff
= entropy-equivalent number of equally weighted target values.
```

Thus two admissible regions can have the same set-valued target image but very different target uncertainty when their compatible-world weights differ.

The lower equality

```text
N_eff=1
```

is exactly point identification. The upper equality

```text
N_eff=|T(A)|
```

holds when total probability mass is uniform across the distinct target values.

The executable verifier includes a three-target example with unequal row counts but equal **total target mass**, recovering

```text
H=log2 3,
N_eff=3.
```

and a strongly skewed two-target example with

```text
1 < N_eff < 2.
```

## Consequence for observation value

When

```text
H(T|A)=0,
```

the target is already point-identified and normalized additional target value is

```text
V_T(Q)=0.
```

This does **not** imply that mechanism learning is exhausted. MROD contains an explicit witness where

```text
H(T|A)=0,
V_T(Q)=0,
I(S;Q|A)=1 bit.
```

so a target-oriented policy stops immediately while the same admissible region still contains a fully mechanism-informative observation.

## Consequence for evidence-admissible reporting

Target point identification is still not report licensing. The Evidence-Admissible Transition bridge additionally requires the declared reliability condition and agreement between the proposed report and the identified target.

The cross-layer chain is therefore

```text
compatible worlds
-> target image T(A), cardinality m
-> weighted target entropy H(T|A)
-> effective multiplicity N_eff=2^H <= m
-> m=1 iff H=0 iff N_eff=1
-> target acquisition stops when H=0
-> mechanism learning may still remain
-> reliability/report-match checks still required for licensing.
```

Implementation:

```text
theory/target_entropy_identification_bridge.py
theory/verify_target_entropy_identification_bridge.py
```

The verifier exhausts all non-empty binary and ternary target sequences of length 1 through 6 and adds unequal positive-weight witnesses.

## Claim boundary

These statements are elementary finite-information identities used here as a representation bridge, not claimed as new Shannon theory. They assume finite support, strictly positive weights, and a deterministic declared target value on each stored world/row. Zero-weight worlds, interval-valued targets, continuous distributions, target-measurement uncertainty, or approximate identification require different statements.
