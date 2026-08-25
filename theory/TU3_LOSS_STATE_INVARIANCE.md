# TU-3 — Loss-state representation invariance and nuisance inflation

> **Status:** finite exact representation theorem module. The factorization, quotient-isomorphism, predictive-equivalence, bisimulation, sufficient-statistic, and lumpability substrates have extensive prior art. TU-3 is therefore an internal theory-universe theorem and type firewall, not yet a standalone novelty claim.

## 1. Question

`eco-genetic-criticality` distinguishes a complete simulator state from coarser ecological summaries. CREST defines a required state relative to a declared scientific contract. The warning programme then speaks about a loss-generating state.

This raises a representation question:

> **If two simulators or mathematical descriptions encode the same loss-relevant ecological futures using different raw state spaces, should they define the same loss-generating state?**

TU-3 answers yes under an explicit loss-response factorization, and it states exactly how the claim fails when a supposedly nuisance coordinate changes the declared loss future.

## 2. Loss-response signature

Fix a loss contract

\[
\mathcal C_L=(\Gamma_L,\mathcal H_L,\Theta_L,\mathcal D_L;L).
\]

For a finite model representation `A` with raw carrier \(\Omega_A\), define a **loss-response signature**

\[
\sigma_A:\Omega_A\to\Sigma_L.
\]

`Sigma_L` is a declared common signature space. A signature may encode, depending on the contract:

- exact future loss endpoint;
- loss time;
- loss/no-loss trajectory class;
- the distribution of a stochastic loss endpoint;
- the vector of loss responses under every contemplated intervention in \(\Gamma_L\).

TU-3 does not require a particular choice. The signature must simply contain exactly the future loss responsibility that the state is required to preserve.

Define the loss partition

\[
Q_A=\Omega_A/\sim_L,
\]

where

\[
a\sim_L a'\iff\sigma_A(a)=\sigma_A(a').
\]

This is the finite exact target-response quotient for the declared loss signature. If additional CREST History/Mechanism/Evidence obligations are required, `sigma_A` must be enriched accordingly before TU-3 is applied.

## 3. Representation map

Let a second representation `B` have carrier \(\Omega_B\) and signature

\[
\sigma_B:\Omega_B\to\Sigma_L.
\]

Let

\[
\pi:\Omega_B\twoheadrightarrow\Omega_A
\]

be a declared surjective representation map: `B` may refine each `A` world into several raw states.

We call `pi` **loss-faithful** when

\[
\boxed{\sigma_B=\sigma_A\circ\pi.}
\]

Thus extra coordinates in `B` may change raw representation identity but not the declared loss response.

## 4. TU-3A — quotient invariance theorem

### Theorem

If \(\pi:\Omega_B\twoheadrightarrow\Omega_A\) is loss-faithful, then it induces a canonical bijection

\[
\bar\pi:Q_B\to Q_A,
\qquad
[b]_{Q_B}\mapsto[\pi(b)]_{Q_A}.
\]

The bijection preserves the common loss-response signature.

### Proof

**Well-defined.** If \(b\sim_L b'\) in `B`, then

\[
\sigma_B(b)=\sigma_B(b').
\]

Loss faithfulness gives

\[
\sigma_A(\pi(b))=\sigma_A(\pi(b')),
\]

so \(\pi(b)\sim_L\pi(b')\) in `A`.

**Injective.** If the induced `A` classes coincide, then

\[
\sigma_A(\pi(b))=\sigma_A(\pi(b')).
\]

By loss faithfulness, \(\sigma_B(b)=\sigma_B(b')\), so the original `B` loss classes coincide.

**Surjective.** For every \(a\in\Omega_A\), surjectivity of \(\pi\) supplies some \(b\in\Omega_B\) with \(\pi(b)=a\). Therefore every `A` loss class is hit. ∎

### Interpretation

Raw simulator states may differ in dimension, naming, or internal nuisance coordinates while the required loss-state quotient remains the same.

Therefore

\[
\boxed{\text{Simulator representation identity}\neq\text{LossGeneratingState identity}.}
\]

## 5. TU-3B — fiber-homogeneity criterion

Often `A` does not yet have an independently supplied loss signature. We instead ask whether the richer representation `B` can be loss-compressed through \(\pi\).

### Theorem

For a surjective map \(\pi:\Omega_B\twoheadrightarrow\Omega_A\), there exists a unique map

\[
\sigma_A:\Omega_A\to\Sigma_L
\]

such that

\[
\sigma_B=\sigma_A\circ\pi
\]

iff every fiber of \(\pi\) is loss-response homogeneous:

\[
\boxed{
\pi(b)=\pi(b')\Rightarrow\sigma_B(b)=\sigma_B(b').
}
\]

### Proof

If the factorization exists, equal `pi` values immediately imply equal `sigma_B` values.

Conversely, if every fiber is homogeneous, define \(\sigma_A(a)\) as \(\sigma_B(b)\) for any `b` with \(\pi(b)=a\). Surjectivity ensures existence and fiber homogeneity ensures uniqueness/well-definedness. ∎

### Meaning

A coordinate is genuinely nuisance for the declared loss contract exactly when forgetting it does not merge raw states with different loss-response signatures.

This is a representation-level factorization condition, not an empirical test by itself.

## 6. TU-3C — arbitrary nuisance inflation with fixed loss-state complexity

### Theorem

For every finite loss model `A` and every integer \(m\ge1\), construct

\[
\Omega_B=\Omega_A\times\{0,1\}^m,
\]

with projection \(\pi(a,z)=a\) and

\[
\sigma_B(a,z)=\sigma_A(a).
\]

Then:

1. \(|\Omega_B|=2^m|\Omega_A|\);
2. \(Q_B\cong Q_A\);
3. the number of loss-state classes is unchanged.

### Proof

The projection is surjective and loss-faithful, so TU-3A gives quotient isomorphism. The raw carrier-size identity follows directly from the product construction. ∎

### Consequence

Raw simulator-state complexity can increase by arbitrary numbers of bits while loss-state complexity remains fixed.

Thus no inference of the form

```text
more detailed simulator state
=> more scientifically required loss state
```

is valid without a target-response argument.

## 7. TU-3D — one hidden loss-relevant coordinate breaks the projection

Take the same product representation

\[
\Omega_B=\Omega_A\times\{0,1\}.
\]

Suppose there is at least one base state \(a_*\) for which

\[
\sigma_B(a_*,0)\neq\sigma_B(a_*,1).
\]

Then the projection \(\pi(a,z)=a\) is not loss-sufficient: no \(\sigma_A\) can satisfy

\[
\sigma_B=\sigma_A\circ\pi.
\]

This is an immediate violation of TU-3B fiber homogeneity.

### Meaning

A coordinate can be omitted from a scientific state only while it is nuisance relative to the declared future loss responsibility. Once it changes that response, the old coarse representation is structurally insufficient.

This gives a generic mathematical reading of cross-layer alignment examples: the point is not that a particular coordinate is universally part of ecological state, but that a projection is invalid whenever its fibers contain different required future responses.

## 8. Relation to CREST and the eco-genetic bridge

TU-3 is downstream of a declared loss contract.

```text
full simulator/model representation
    |
    | declare loss-response responsibility
    v
loss-response signature sigma_L
    |
    v
CREST-style required loss quotient
    |
    | compare alternative raw representations
    v
TU-3 representation-invariance test
```

The existing bounded EcoGenetic -> CREST aligned/anti-aligned witness shows one failure of coarse-summary sufficiency for an exact next-interaction target. TU-3 generalizes the *type of question*: any candidate projection is safe for a declared target only when its fibers are response-homogeneous.

TU-3 does not upgrade that bounded witness to a theorem about the full simulator or natural systems.

## 9. Dynamics and lumpability boundary

Equality of a one-shot loss signature is not automatically enough to define recursive quotient dynamics.

If the required state must itself evolve Markovianly under declared actions, an additional closure/lumpability/bisimulation condition is required: states merged by the quotient must induce the same distribution over future quotient states under each declared action.

That dynamical closure belongs to CREST/state-transition theory and classical lumpability/bisimulation substrate. TU-3A–D make only the loss-response quotient claim explicitly stated above.

## 10. Warning boundary

Quotient invariance of the loss state does **not** by itself prove warning portability.

A warning statistic can depend on coordinates that differ across representations, observation processes, or calibrated domains. Transporting warning therefore requires a separate map for warning time/order and its evidence contract.

That is a later theorem target.

## 11. Type firewall

TU-3 forbids:

- `CompleteSimulatorState = LossGeneratingState`;
- `larger raw state space = more required loss states`;
- `representation map = faithful projection` without fiber homogeneity;
- `same endpoint label = same full dynamics` unless the signature actually contains the required future law;
- `loss-state quotient invariance = warning portability`;
- `model representation invariance = empirical natural-state identification`.

## 12. Prior-art firewall

The mathematical substrate overlaps established ideas:

- sufficient statistics and factorization;
- state abstraction and predictive-state representations;
- bisimulation and behavioral equivalence;
- Markov lumpability and quotient dynamics;
- model reduction and target-preserving abstraction.

Accordingly, TU-3A/B are not presented as new general mathematics. TU-3C/D are exact finite witnesses used to enforce the theory-universe distinction between **raw representation complexity** and **contract-required ecological state complexity**.

## 13. Next extension

The next genuinely useful step is to add a warning layer.

Let two loss representations have isomorphic loss quotients. A warning-portability theorem should ask whether there exists a map preserving the joint law/order of

\[
(\tau_G,\tau_L)
\]

across corresponding loss-state classes.

The expected result is that loss-state isomorphism alone is insufficient; warning observables must also factor through the cross-representation correspondence. That extension is not yet claimed here.
