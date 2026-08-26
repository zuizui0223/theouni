# Relation Semantics — typed arrows for the Theory Universe

Status: **notation firewall outside the frozen v0.5 semantic core**.

The Theory Universe uses graphs for several different purposes. A single unlabeled arrow must not silently mean all of them.

The repository therefore distinguishes three primary relation types.

---

## 1. Normative / definitional dependency

Notation:

\[
A\prec_{\rm norm}B
\]

or a dashed/dotted graph edge.

Meaning:

> `B` is defined, constrained, or logically downstream of `A` in the theory architecture.

Examples:

```text
Theory Constitution  ≺norm  Empirical admission rules
ScientificContract   ≺norm  RequiredState definition
Loss contract        ≺norm  LossGeneratingState definition
```

This is **not** a claim that data physically flow from `A` to `B`.

---

## 2. Operational / data / inference flow

Notation:

\[
A\to_{\rm op}B
\]

or a solid directed graph edge.

Meaning:

> an observation, record, representation, or decision output produced/accepted at `A` becomes an input to `B`.

Examples:

```text
Named project ->op programme typing ->op Empirical Projection Gate
ObservationRecord ->op RealizedEvidenceClass
RealizedEvidenceClass ->op reportability / causal-admissibility calculation
```

This does **not** establish normative ownership or theorem implication by itself.

---

## 3. Provenance / ownership relation

Notation:

\[
A\to_{\rm prov}B
\]

or an explicitly labeled provenance edge.

Meaning:

> object/claim `B` is sourced from, owned by, or provenance-linked to `A`.

Examples:

```text
CREST ->prov source theorem used in theouni
microdonta/RACH ->prov NOV semantics
source commit ->prov bridge registry record
```

Provenance does not imply logical dependence, empirical support, or physical causation.

---

# 4. Two opposite-looking orders are therefore compatible

The repository has used both:

```text
Theory first
    -> admission rules
    -> programme types
    -> named projects
```

and

```text
Named project
    -> programme typing
    -> admission gate
    -> model-world representation
```

These are not inverse scientific claims.

They are different typed relations.

### Normative design order

\[
\boxed{
\text{Theory}
\prec_{\rm norm}
\text{Admission rules}
\prec_{\rm norm}
\text{Programme schema}
\prec_{\rm norm}
\text{Named-project manifest}
}
\]

The abstract rules constrain what a concrete project is allowed to claim.

### Operational admission flow

\[
\boxed{
\text{Named project}
\to_{\rm op}
\text{Programme typing}
\to_{\rm op}
\text{Admission gate}
\to_{\rm op}
\text{Model-world / evidence object}
}
\]

A real project supplies records upward through those constraints.

The directions differ because the relations differ.

---

## 5. Graph firewall

Every machine-readable cross-layer edge should declare a `relation_type` or sufficiently specific `relation` value that can be mapped to one of:

- `normative_dependency`;
- `operational_flow`;
- `provenance_ownership`;
- explicitly declared additional typed relations such as `mathematical_factorization`, `empirical_support`, or `counterexample`.

An unlabeled edge must never be used as evidence that:

- a source theorem logically proves a downstream empirical claim;
- a project is normatively prior to the theory that classifies it;
- provenance implies causation;
- operational data flow transfers theorem ownership.

---

## 6. Mermaid convention

When one figure must contain several relation types:

- **solid arrow** `-->` = operational/data/inference flow;
- **dashed arrow** `-.->` = normative/definitional dependency;
- **labeled provenance edge** = provenance/ownership only.

If a figure becomes visually ambiguous, split it into separate normative and operational diagrams rather than reuse one arrow style.

---

## 7. Why this matters scientifically

The Theory Universe already forbids type collapse among `World`, `State`, `EvidenceClass`, and `Report`. Graph relations require the same discipline.

A graph edge is not a generic relation. The **kind of arrow is part of the scientific claim**.

---

## 8. Pairwise contradiction-audit relations

The v0.6 draft contradiction matrix uses a second vocabulary for **symmetric pairwise comparison**. These values are audit classifications, not directed graph edges:

- `compatible` — the two typed claims are directly co-satisfiable in their already-declared matched scope; equality or implication is not asserted;
- `conditional-on-common-carrier-or-map` — no conflict follows after an explicit common carrier, lift, typed map, response map, or commutation contract is supplied; composition is forbidden until then;
- `orthogonal-estimand` — the modules constrain different typed objects, so neither is the logical negation of the other and no automatic bridge follows;
- `open-bridge` — no current contradiction is identified, but the scientifically useful cross-layer identification or composition is not proved at the stated generality;
- `actual-conflict` — after carrier, type, scope, and estimand are matched, the two claims are jointly unsatisfiable.

These relations must not be collapsed into the arrow types above. In particular:

```text
compatible != mathematical equivalence
conditional-on-common-carrier-or-map != completed bridge
orthogonal-estimand != evidence of independence
open-bridge != favourable or null evidence
actual-conflict = 0 != global or higher-order consistency proof
```

The five labels are human semantic judgments. The validator is deliberately fail-closed for missing pairs, unknown vocabulary, generated-certificate drift, and a declared `actual-conflict`, but it cannot prove that a reviewer chose the correct label. Relation misclassification therefore remains an external-review risk rather than a machine-certified property.

The canonical registry is [`contradiction_matrix.json`](contradiction_matrix.json), and the generated audit surface is [`CONTRADICTION_CERTIFICATE_v0.6.md`](CONTRADICTION_CERTIFICATE_v0.6.md).
