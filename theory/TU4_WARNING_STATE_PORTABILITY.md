# TU-4 — Warning evaluation state and portability

> **Status:** finite exact warning-state firewall. The factorization/refinement substrate is elementary. TU-4's role is to prevent the phrase “warning belongs to a loss-generating state” from being read as the stronger and generally false statement that the loss-state quotient automatically determines warning behaviour.

## 1. Why a second warning state is needed

The condition-first warning programme correctly fixes the downstream loss process before inspecting genetic lead/lag behaviour. This prevents circular selection of the ecological domain using the warning outcome.

But two mathematical questions remain distinct:

1. what distinctions among worlds are required to generate the declared **loss process**?
2. what distinctions are required to generate the declared **joint warning/loss relation**?

A state sufficient for the first need not be sufficient for the second.

## 2. Loss and warning signatures

Let \(\Omega\) be a finite world carrier.

Fix a loss-response signature

\[
\lambda:\Omega\to\Lambda,
\]

where `lambda` contains the future loss responsibility declared by the loss contract, for example loss/no-loss, loss time, or an intervention-indexed loss law.

Define the loss-generating partition

\[
Q_L=\Omega/\sim_L,
\qquad
\omega\sim_L\omega'
\iff
\lambda(\omega)=\lambda(\omega').
\]

Now fix a warning-response signature

\[
\gamma:\Omega\to\Gamma_W.
\]

Depending on the scientific contract, `gamma` may encode:

- warning time \(\tau_G\);
- lead/tie/lag category relative to \(\tau_L\);
- lead-time magnitude;
- the joint distribution of \((\tau_G,\tau_L)\);
- a vector of warning responses across declared thresholds or observation modes.

Define the **warning-evaluation signature**

\[
\eta(\omega)=(\lambda(\omega),\gamma(\omega))
\]

and the corresponding partition

\[
Q_W=\Omega/\sim_W.
\]

`Q_W` is the finite exact `WarningEvaluationState` for the declared warning contract.

## 3. TU-4A — warning state refines loss state

### Theorem

\[
\boxed{Q_W\text{ refines }Q_L.}
\]

Moreover,

\[
\boxed{Q_W=Q_L}
\]

iff the warning-response signature factors through the loss-state quotient:

\[
\boxed{\gamma=\bar\gamma\circ q_L}
\]

for some map \(\bar\gamma:Q_L\to\Gamma_W\).

### Proof

If two worlds agree in the joint signature `(lambda,gamma)`, they necessarily agree in `lambda`; hence every warning-state block lies inside one loss-state block.

Equality holds exactly when no loss-state block is further split by `gamma`, i.e. when `gamma` is constant on every loss-state block. That is precisely the factorization condition through `q_L`. ∎

### Interpretation

A loss-generating state is automatically sufficient for warning evaluation **only when warning behaviour is homogeneous within each loss-state class**.

Otherwise

\[
\boxed{\text{WarningEvaluationState is strictly finer than LossGeneratingState}.}
\]

## 4. Consequence for the phrase “warning is state-conditional”

The safe statement is:

> Warning must be evaluated only after a loss-generating state/domain has been fixed independently of warning outcomes.

The stronger statement

> the loss-generating state itself determines warning validity

requires TU-4A's factorization condition and is not automatic.

Thus `LossGeneratingState` is a **conditioning scaffold** for non-circular warning inference, while `WarningEvaluationState` is the required quotient for the joint warning/loss target.

## 5. TU-4B — identical loss state can support opposite warning validity

### Construction

Take two worlds \(u,v\) with the same loss time

\[
\tau_L(u)=\tau_L(v)=10.
\]

Let

\[
\tau_G(u)=5,
\qquad
\tau_G(v)=15.
\]

Then both worlds occupy the same loss-state block, but their warning orderings are opposite:

\[
\tau_G(u)<\tau_L(u),
\qquad
\tau_G(v)>\tau_L(v).
\]

Hence `Q_L` has one block while `Q_W` has two.

### Conclusion

Loss-state identity alone does not determine warning validity.

This is an exact counterexample to any unqualified implication

```text
same loss-generating state
=> same warning ordering
```

unless the warning factorization condition has been established.

## 6. Replication inside a frozen domain

Suppose repeated trajectories are generated under one frozen calibrated domain/state `s`, and the warning-order distribution

\[
P(\tau_G<\tau_L\mid s)
\]

is reproducible under independent seeds or replicates.

This establishes a conditional warning result for that domain. It does not imply that another calibrated state `s'` has the same warning law.

This distinction matches the theory-universe separation:

```text
within-state replication
!= cross-state portability
```

## 7. TU-4C — warning portability criterion on loss states

Consider two model domains `A` and `B` whose loss-state quotients are related by a declared bijection

\[
h:Q_L^B\to Q_L^A.
\]

Assume warning behaviour factors through the loss state in each domain:

\[
\gamma_A=\bar\gamma_A\circ q_L^A,
\qquad
\gamma_B=\bar\gamma_B\circ q_L^B.
\]

### Theorem

Warning behaviour transports across `h` iff

\[
\boxed{
\bar\gamma_B
=
\bar\gamma_A\circ h.
}
\]

### Proof

Under the factorization assumptions, each loss-state class has one well-defined warning signature. Portability across corresponding loss states is exactly equality of those class-level signatures after applying `h`. ∎

### Meaning

Even a perfect loss-state isomorphism does not automatically transport warning. The warning law itself must commute with the cross-state correspondence.

## 8. TU-4D — when warning does not factor through loss state

If either domain violates TU-4A's factorization condition, portability cannot be defined faithfully on the loss quotient alone.

One must instead compare the finer warning-evaluation quotients

\[
Q_W^A,
\qquad
Q_W^B.
\]

A valid portability map must preserve the declared joint warning/loss signatures on those finer classes.

Therefore the general sequence is

```text
LossGeneratingState
    |
    | test warning homogeneity within loss-state blocks
    v
if homogeneous: warning law on loss quotient
if not: refine to WarningEvaluationState
    |
    v
cross-domain portability map
```

## 9. Relation to the eco-genetic warning programme

The current condition-first sequence

```text
C2 loss process fixed warning-blind
-> C3 warning tested within the frozen domain
-> C4 portability evaluated separately
```

is logically compatible with TU-4.

TU-4 sharpens its interpretation:

- C2 identifies/fixes the loss-generating scaffold used for non-circular evaluation;
- C3 provides evidence about a warning-response signature within that scaffold;
- C4 asks whether the warning signature transports across a different calibrated state/domain.

A successful C3 result is not automatically a theorem that the loss quotient is itself warning-sufficient.

## 10. Threshold portability

A numerical warning threshold \(c\) is universal only under a much stronger condition than warning-order portability.

If warning signatures include threshold-crossing times \(\tau_{G,c}\), then one fixed `c` can transport only when its induced warning-response signature satisfies the portability criterion across all relevant state classes/domains.

Thus

```text
within-state reproducible relative warning
!= universal numerical threshold
```

without additional proof.

## 11. Type firewall

TU-4 forbids:

- `LossGeneratingState = WarningEvaluationState` without warning factorization;
- `within-state warning replication = cross-state warning portability`;
- `loss-state isomorphism = warning-law isomorphism`;
- `warning portability = universal threshold`;
- `warning statistic = warning state`;
- `warning-blind state calibration = proof that state is warning-sufficient`.

## 12. Prior-art boundary

The underlying mathematics is target-relative partition refinement and factorization. Similar ideas appear throughout sufficient-statistic, predictive-state, task-specific abstraction, and model-reduction theory.

TU-4 is therefore not claimed as a new generic factorization theorem. Its purpose is to make the ecology-specific logical architecture exact:

\[
\boxed{
\text{loss state}
\to
\text{warning evaluation state}
\to
\text{within-state replication}
\to
\text{portability}
}
\]

with a separate gate at each arrow.

## 13. Next extension

The finite deterministic signatures above can be replaced by probability laws.

A stochastic warning-portability theorem should compare conditional joint laws

\[
\mathcal L(\tau_G,\tau_L\mid s)
\]

under a declared state correspondence and observation/censoring contract. Exact equality, tolerance-qualified distance, and evidence-licensed indistinguishability should remain separate notions.

That stochastic/evidential extension is open.
