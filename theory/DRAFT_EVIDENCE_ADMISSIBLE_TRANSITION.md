# Draft — Evidence-Admissible Transition

> **Status:** executable bridge draft only. This does not modify the frozen Theory Universe core, does not expand TU-2's theorem claim, and is not a model of human informed consent.
>
> **2026-09-08 routing clarification:** EAT is a local bridge from **Boundary-style structural target identification** to **CED-style reliability-qualified terminal reporting**. It is not a replacement for REC/V3/TNOA observation processing or MROD prospective observation design. See [`WORLD_STATE_EVIDENCE_HIERARCHY_2026-09-08.md`](WORLD_STATE_EVIDENCE_HIERARCHY_2026-09-08.md).

The motivating structural analogy is simple: a system should not move from an evidence state to a stronger scientific report merely because that report is globally attractive or convenient. The transition must be supported by the distinctions actually preserved by the current evidence and by the declared reliability contract.

The safe scientific name used here is **Evidence-Admissible Transition (EAT)**.

## 1. Finite deterministic form

Let

```text
E_y
```

be the current non-empty compatible-world class and let

```text
T: world -> declared target value.
```

A proposed report value `t_hat` is EAT-admissible only when all three conditions hold:

```text
1. target constancy:
   |T(E_y)| = 1

2. reliability:
   the declared evidence/reliability requirement is satisfied

3. proposal agreement:
   t_hat equals the unique value in T(E_y).
```

The executable audit is in

```text
theory/evidence_admissible_transition.py
```

with verifier

```text
theory/verify_evidence_admissible_transition.py.
```

## 2. Mechanism multiplicity is allowed

EAT does not require a unique compatible mechanism/world.

It permits

```text
|E_y| > 1
and
|T(E_y)| = 1.
```

This structural identification statement is owned by the current identification layer represented by `boundary`: unresolved mechanism identity does not imply that every narrower target remains unidentified.

EAT adds no new identification theorem here. It asks whether a structurally identified target may be promoted to a terminal report after the separate reliability contract is checked.

## 3. Reliability remains separate from structural identification

Even when

```text
|T(E_y)|=1,
```

a transition is withheld if the declared reliability/evidence requirement is not satisfied.

This keeps the v0.5.1 distinction intact:

```text
D_req != E_y^{D_req}.
```

A compatible-world set and the contract governing whether evidence is acceptable are different objects.

This is also the clean Boundary/CED firewall:

```text
Boundary
-> what the current observation map structurally identifies

CED
-> whether the attained evidence is reliable enough for terminal stopping/reporting

EAT
-> the local transition contract between those two objects
```

## 4. Relation to the observation-information family

The draft is a composition layer, not a transfer of claim ownership.

```text
REC
-> audits opportunities/records lost before row entry

V3
-> refines compatible states using already-retained side/reference information

TNOA
-> preserves process-aware observation semantics and licenses record-level attribution claims without forcing unsupported collapse

Boundary
-> returns the compatible-world geometry and target image under the current observation map

MROD
-> values/selects prospective observations expected to reduce residual mechanism/target ambiguity

CED
-> owns reliability/failure architecture and risk-limited terminal scientific reporting/stopping

theouni EAT draft
-> states a minimal finite Boundary-to-CED transition contract
```

A realized MROD-selected observation may later become ordinary V3-style retained refinement. TNOA may preserve the semantic distinctions carried by the resulting record. Neither operation is collapsed into EAT.

## 5. Relation to CREST

CREST supplies the upstream required-state distinction:

```text
J = distinctions required by the declared scientific contract
```

whereas Boundary supplies the current identification state and CED supplies terminal reliability-qualified reportability.

The larger hierarchy is therefore:

```text
CREST J: what must be distinguished
        ↓
observation family: what has actually survived and been identified
        ↓
Boundary: is the target structurally identified?
        ↓
EAT / CED reliability gate
        ↓
licensed or withheld terminal scientific report
```

EAT does not decide whether `J` itself is the correct required state; that remains a CREST/companion-theory question.

## 6. Relation to the EG programme

EGC/EGWE/EGWEE provide domain-specific tests of whether proposed eco-genetic states, representations, warning rules and empirical proxies actually carry endpoint-relevant future information.

Those results can determine whether a measurable variable is a defensible input to an empirical evidence contract, but EAT does not promote a plausible proxy to state status by itself.

```text
plausible measurement
!=
validated EmpiricalPartialState
!=
reliable evidence for a terminal target
```

The generic empirical admission route remains the theouni Empirical Projection Gate.

## 7. Why this is not called informed consent

Human informed consent concerns autonomous persons, disclosure, comprehension, voluntariness and authorization. Those ethical requirements are not properties of ecological model states.

The useful transferable structure is only the narrower logical pattern:

```text
possible transition
!=
admissible transition under the declared information/authorization contract.
```

Calling the ecological object Evidence-Admissible Transition avoids importing human-subject semantics that the model does not contain.

## 8. Verification witness

Run from `theory/`:

```bash
python verify_evidence_admissible_transition.py
```

The verifier checks four finite cases:

1. two mechanisms, same target, reliable evidence, matching proposal → admissible;
2. same structurally identified target but failed reliability → withheld;
3. compatible worlds disagree on target → withheld;
4. target identified but proposed report disagrees → withheld.

This is an executable consistency witness, not a claim of new general mathematical novelty.
