# Draft — Evidence-Admissible Transition

> **Status:** executable bridge draft only. This does not modify the frozen Theory Universe core, does not expand TU-2's theorem claim, and is not a model of human informed consent.

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

This is the same finite structural distinction now made executable in `boundary`: unresolved mechanism identity does not imply that every narrower target remains unidentified.

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

## 4. Relation to the repository ecosystem

The draft is a composition layer, not a transfer of claim ownership.

```text
TNOA
-> preserves process-aware observation state and now exposes fail-closed report transitions

boundary
-> returns the target image of the current compatible-world set

MROD
-> can separately value mechanism information I(S;Q) and declared-target information I(T;Q)

CED / TU-2
-> own the deeper target-reportability / learning-versus-licensing theory

theouni EAT draft
-> states a finite transition contract connecting those objects.
```

No source repository loses ownership of its theorem or empirical evidence.

## 5. Why this is not called informed consent

Human informed consent concerns autonomous persons, disclosure, comprehension, voluntariness and authorization. Those ethical requirements are not properties of ecological model states.

The useful transferable structure is only the narrower logical pattern:

```text
possible transition
!=
admissible transition under the declared information/authorization contract.
```

Calling the ecological object Evidence-Admissible Transition avoids importing human-subject semantics that the model does not contain.

## 6. Verification witness

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
