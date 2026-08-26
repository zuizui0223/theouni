# Draft Theory Universe v0.6 — Contract-Indexed Quotient Transport

Status: **draft generalization outside the frozen v0.5 core and v0.5.1 clarification layer**.

This document asks whether TU-1 through TU-4 are genuinely separate principles or specializations of one more general structure.

The answer is:

> **TU-1, TU-3, and TU-4 are exact specializations of one task-indexed factorization theorem. TU-2 is the graded epistemic analogue obtained when exact task adequacy is replaced by task-specific observation utility.**

The useful general principle is not literally "quotient noncommutativity". Quotient formation itself need not be noncommutative. The failure occurs when a scientific ordering is transported from one task/contract to another **without a factorization morphism connecting the tasks**.

The programme-level slogan is therefore:

> **Fineness, sufficiency, or value under one scientific responsibility does not transport to another responsibility unless the second responsibility factors through the retained representation.**

---

## 1. Primitive setup

Let `Omega` be a declared model-world universe.

A scientific responsibility or task `alpha` is represented by a **contract-complete response signature**

\[
\Sigma_\alpha:\Omega\to Y_\alpha.
\]

`Sigma_alpha` contains exactly the response distinctions that must be preserved for task `alpha`; it need not be a scalar and may encode a tuple/family of future, history, mechanism, target, or report-relevant responses.

Define task equivalence

\[
\omega\sim_\alpha\omega'
\iff
\Sigma_\alpha(\omega)=\Sigma_\alpha(\omega').
\]

and the canonical quotient

\[
Q_\alpha=\Omega/\!\sim_\alpha,
\qquad
q_\alpha:\Omega\to Q_\alpha.
\]

A candidate retained representation is any map

\[
R:\Omega\to Z.
\]

Its fibers define a partition `Q_R` of `Omega`.

The partition order follows CREST convention:

\[
P\preceq Q
\iff
Q\text{ refines }P.
\]

Thus moving upward retains more distinctions.

---

## 2. Definition — exact task adequacy

A representation `R` is **adequate for task alpha** when the complete response signature can be reconstructed from `R`:

\[
\boxed{
R\models\alpha
\iff
\exists f:Z\to Y_\alpha
\text{ such that }
\Sigma_\alpha=f\circ R.
}
\]

Equivalently, `R` never merges two worlds that task `alpha` requires to remain distinct.

---

# 3. General theorem CIRA-1 — Contract-Indexed Representation Adequacy

For any task `alpha` and representation `R`, the following are equivalent:

1. `R models alpha`;
2. `Sigma_alpha = f o R` for some map `f`;
3. every fiber of `R` is contained in one `alpha`-equivalence class;
4. `ker(R) subseteq ker(Sigma_alpha)`;
5. in the CREST information order,
   \[
   \boxed{Q_\alpha\preceq Q_R.}
   \]

### Proof

`1 <-> 2` is the definition.

`2 -> 3`: if `R(omega)=R(omega')`, then

\[
\Sigma_\alpha(\omega)
=f(R(\omega))
=f(R(\omega'))
=\Sigma_\alpha(\omega').
\]

Hence one representation fiber cannot cross an `alpha`-class.

`3 <-> 4` is the kernel formulation of the same statement.

`3 <-> 5` follows because `Q_R` is finer than `Q_alpha` exactly when every `R`-block lies within an `alpha`-block. ∎

### Interpretation

The canonical task quotient `Q_alpha` is the coarsest exact representation for `alpha` once `Sigma_alpha` is fixed.

This is classical factorization/quotient substrate. The role here is not to claim new mathematics but to expose the single structure shared by the Theory Universe modules.

---

## 4. CIRA-2 — A preorder on scientific responsibilities

Define

\[
\boxed{
\alpha\sqsubseteq\beta
}
\]

when task `beta` is at least as discriminating as task `alpha`, meaning

\[
\exists g:Y_\beta\to Y_\alpha
\quad
\Sigma_\alpha=g\circ\Sigma_\beta.
\]

Then

\[
\alpha\sqsubseteq\beta
\iff
Q_\alpha\preceq Q_\beta.
\]

So the assignment

\[
\alpha\mapsto Q_\alpha
\]

is monotone from the task preorder into the partition lattice.

This is the precise sense in which order **does** transport: it transports only along declared task-refinement morphisms.

---

# 5. CIRA-3 — Reuse theorem

Let `q_alpha` be the canonical state retained for task `alpha`.

Then `q_alpha` is adequate for a later/different task `beta` iff

\[
\boxed{
\beta\sqsubseteq\alpha.
}
\]

Equivalently,

\[
\Sigma_\beta=h\circ q_\alpha
\]

for some `h`, or

\[
Q_\beta\preceq Q_\alpha.
\]

### Consequence

A state built for a weaker task is generally **not** reusable for a stronger task.

If

\[
\alpha\sqsubseteq\beta
\]

with strict refinement

\[
Q_\alpha\prec Q_\beta,
\]

then the canonical `alpha`-state has already forgotten distinctions needed by `beta`.

This is TU-1's core logical condition before revision debt is quantified.

---

# 6. CIRA-4 — Incomparability theorem

Suppose tasks `alpha` and `beta` are incomparable:

\[
\alpha\not\sqsubseteq\beta,
\qquad
\beta\not\sqsubseteq\alpha.
\]

Then:

- `q_alpha` is adequate for `alpha` but not for `beta`;
- `q_beta` is adequate for `beta` but not for `alpha`.

Hence there is no task-independent notion of "more scientifically sufficient" that can be inferred merely from adequacy under one of the two tasks.

### Important terminology

This is better described as **failure of order transport across incomparable task indices** than as noncommutativity of quotient formation.

The quotient map is well behaved once the task relation is typed. The problem is precisely that arbitrary task changes need not supply a morphism.

---

## 7. CIRA-5 — Joint responsibilities

For two tasks `alpha` and `beta`, define the joint response signature

\[
\Sigma_{\alpha\vee\beta}(\omega)
=
(\Sigma_\alpha(\omega),\Sigma_\beta(\omega)).
\]

Then

\[
Q_{\alpha\vee\beta}
=
Q_\alpha\vee Q_\beta
\]

in the partition lattice: the joint task retains exactly the distinctions required by either component.

This is the response-signature version of CREST's joint-state idea. CREST retains the more general source-owned closure/common-carrier theorem machinery; this draft does not replace it.

---

# 8. TU-1 through TU-4 as specializations

## TU-1 — revision after compression

Take

- `alpha = C0`, the old contract;
- `beta = C1`, the revised contract;
- retained representation `R = q_C0`.

Then the general reuse theorem gives

\[
q_{C_0}\models C_1
\iff
C_1\sqsubseteq C_0.
\]

When this fails, TU-1 adds genuinely additional structure: the exact minimum auxiliary side-information alphabet and revision-debt bounds.

Thus TU-1 is **factorization failure + quantified repair cost**.

---

## TU-3 — representation invariance

Take

- `alpha = C_L`, the loss contract;
- `R = pi`, a coarse representation/projection.

Then

\[
\pi\models C_L
\iff
\Sigma_{C_L}=\bar\Sigma_{C_L}\circ\pi.
\]

This is exactly TU-3's loss-faithfulness criterion under the v0.5.1 contract-complete loss signature.

Thus TU-3 is **the general adequacy theorem applied to a representation change**.

---

## TU-4 — loss state versus warning state

Let

- `alpha = C_L`, the loss-only task;
- `beta = C_W`, the joint loss + warning task.

By construction,

\[
C_L\sqsubseteq C_W,
\]

so

\[
Q_L\preceq Q_W.
\]

The canonical loss state is reusable for warning exactly when

\[
C_W\sqsubseteq C_L,
\]

which is equivalent to the warning response factoring through the loss state.

Thus TU-4 is **strict task refinement unless warning contributes no new distinction**.

---

## TU-2 — graded epistemic analogue

TU-2 is slightly different and should not be forced into a false exact identity.

Let

- `alpha = causal-identification task S`;
- `beta = report-target task T`.

When `S` and `T` induce incomparable task quotients, the exact theorem already permits representations that are sufficient for one but not the other.

TU-2 then replaces exact adequacy for the causal task with a **graded information utility** such as RACH NOV, while CED target licensing remains a target-specific reporting property.

The sharp TU-2 endpoints are exact manifestations of task incomparability:

```text
representation fully resolves S but not T
representation fully resolves T but carries no information about S
```

Intermediate NOV values require the additional information-theoretic utility structure and are therefore not claimed as direct corollaries of the exact quotient theorem.

Thus TU-2 is best described as the **graded epistemic analogue of task-order nontransport**.

---

# 9. Why this makes TU-5 unnecessary in principle

The current four modules expose four locations where task-indexed order fails to transport:

| Module | retained object | changed evaluation responsibility | extra content beyond general factorization |
|---|---|---|---|
| TU-1 | old state | revised contract | exact revision side-information/debt |
| TU-2 | candidate observation | causal task vs target-report task | graded utility and policy reversal |
| TU-3 | model representation | loss target contract | nuisance-inflation / hidden-coordinate witnesses |
| TU-4 | loss state | warning contract | warning refinement and portability criterion |

A future TU-number should therefore not be added merely because another application exhibits the same failure of order transport.

A genuinely new core theorem must add something not reducible to:

1. task-indexed factorization;
2. a source-owned theorem already in CREST/CCOC/MLTR/MRM/CED/RACH;
3. one of the existing quantified repair/utility/representation/portability structures.

This is the formal reason the core can close without an automatic TU-5.

---

# 10. Relation to prior theory

The substrate has strong classical relatives and should be positioned as synthesis, not invented mathematics:

- sufficient-statistic factorization and statistical reduction;
- computational mechanics / predictive equivalence classes;
- state abstraction and bisimulation / reward-predictive representations;
- quotient and effective-theory coarse graining;
- Blackwell-style comparison of information structures for decision tasks.

The possible novelty of the wider programme, if any, lies in the **ecological contract architecture and the coupling of future, history, mechanism, evidence, revision, empirical admission, and warning claim ceilings**, not in the bare factorization lemma.

---

# 11. Current decision

This is a **v0.6 draft**, not a change to the frozen core.

The generalization now has an executable draft spine:

- [`contract_indexed_adequacy_registry.json`](contract_indexed_adequacy_registry.json) records CIRA-1 through CIRA-5, their scope, and the specialization branches;
- [`verify_contract_indexed_quotient_transport.py`](verify_contract_indexed_quotient_transport.py) exhausts all 15 partitions of a four-world carrier and checks adequacy/kernel equivalence, preorder reflexivity/transitivity, reuse, incomparability witnesses, and joint responsibility;
- the registry requires `TU-1`, `TU-3`, and `TU-4` to remain on the `exact` branch and `TU-2` to remain on the `graded_epistemic_analogue` branch.

The cross-module audit is also executable:

- [`contradiction_matrix.json`](contradiction_matrix.json) types every one of the 66 unordered pairs among CREST, CCOC, MLTR, MRM, CED, RACH, EGC, EGW, and TU-1 through TU-4;
- [`CONTRADICTION_CERTIFICATE_v0.6.md`](CONTRADICTION_CERTIFICATE_v0.6.md) is the generated human-readable certificate;
- [`validate_contradiction_matrix.py`](validate_contradiction_matrix.py) fails closed on a missing/duplicate pair, an unknown relation, certificate drift, or any nonzero `actual-conflict` count.

The current certificate has `actual-conflict = 0`. This is a **pairwise typed non-contradiction result only**. `conditional-on-common-carrier-or-map` and `open-bridge` are not upgraded to completed compositions, and no empirical truth or higher-order consistency result is claimed.

Before promotion, two non-executable gates remain:

1. prior-art audit for task-indexed quotient/factorization formulations;
2. manuscript-level test that replacing four apparently independent principles by this one meta-theorem actually sharpens, rather than trivializes, the ecological argument.
