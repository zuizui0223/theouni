# Target image singleton iff target entropy is zero

> **Status:** finite exact bridge theorem. `boundary` retains ownership of set-valued target identification; `mrod` retains ownership of target-oriented observation information. This file records their exact overlap on a finite positive-weight admissible support.

Let `A` be the current finite admissible set of worlds/rows and let `T` be a declared target. Assume every stored row has strictly positive weight.

`boundary`-style point identification asks whether

```text
|T(A)| = 1.
```

`MROD` target-aware observation value starts from

```text
H(T | A).
```

For a finite positive-weight support,

```text
|T(A)| = 1
iff
H(T | A) = 0.
```

The proof is elementary: finite Shannon entropy is zero exactly when all positive probability mass lies on one target value. Strictly positive row weights make the positive-probability target support equal to the target image of the stored admissible rows.

Implementation:

```text
theory/target_entropy_identification_bridge.py
theory/verify_target_entropy_identification_bridge.py
```

The verifier exhausts all non-empty binary and ternary target sequences of length 1 through 6 and adds unequal positive-weight witnesses.

## Consequence for observation value

When

```text
H(T | A)=0,
```

the target is already point-identified on the stored admissible support. The normalized additional target value is therefore zero by construction:

```text
V_T(Q)=0.
```

When

```text
H(T | A)>0,
```

at least two target values remain alive and target-resolving observations can have positive value.

This does **not** imply that mechanism identity is resolved. Multiple mechanisms can remain compatible while every compatible mechanism induces the same target.

## Consequence for evidence-admissible reporting

Target point identification is still not the same as report licensing. The Evidence-Admissible Transition bridge additionally requires the declared reliability condition and agreement between the proposed report and the identified target.

So the cross-layer chain is

```text
compatible worlds
-> target image T(A)
-> |T(A)|=1 iff H(T|A)=0
-> target already resolved for MROD utility
-> reliability/report-match checks still required for licensing.
```

## Claim boundary

The equivalence is for a finite support with strictly positive weights and a deterministic declared target value on each stored world/row. Zero-weight worlds, interval-valued targets, continuous distributions, measurement uncertainty in the target itself, or approximate identification require a different statement.
