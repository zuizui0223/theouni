# Local-transition and mesoscopic bridge — 2026-09-06

> **Status:** cross-repository provenance/implementation map. This file transfers no theorem, empirical-result, or manuscript ownership to `theouni`.

This bridge records the implementation prompted by four neighboring ideas:

```text
small local jumps
bounded interaction (HK-like locality)
mesoscopic population representation
evidence-admissible transitions
```

The terms are not treated as one theory and are not forced into every repository. Each implementation is placed only where it matches the repository's existing scientific responsibility.

## A. Evolutionary / architecture side

### PAYOFF — local architecture interaction + small mutation jumps + mesoscopic density

Files:

```text
zuizui0223/payoff/src/mesoscopic_architecture.py
zuizui0223/payoff/tests/test_mesoscopic_architecture.py
zuizui0223/payoff/theory/MESOSCOPIC_ARCHITECTURE_DYNAMICS.md
```

Objects:

```text
f(r,t)                         architecture distribution
H_epsilon(r,q)                 bounded architecture interaction
small_jump_mutation            local mutation kernel
minimum_jump_to_better_state   accessibility diagnostic
```

The bounded kernel is structurally analogous to bounded-confidence interaction, but architectures are not opinions and the repository does not relabel the biological model as Hegselmann--Krause.

### Eco-genetic warning extensions — trait-bin small-jump bridge

Files:

```text
zuizui0223/eco-genetic-warning-extensions/src/eco_genetic_warning_extensions/small_jump_trait_bins.py
zuizui0223/eco-genetic-warning-extensions/tests/test_small_jump_trait_bins.py
zuizui0223/eco-genetic-warning-extensions/docs/SMALL_JUMP_TRAIT_BIN_BRIDGE_2026-09-06.md
```

The locked `eco-genetic-criticality` parent is not modified. The extension adds a prospective local mutation kernel that can be composed with the existing finite trait-bin state in a separately declared experiment.

### BALANCE — explicit small-step environmental forcing

Files:

```text
zuizui0223/balance/balance_domain/stepwise_hysteresis.py
zuizui0223/balance/tests/test_stepwise_hysteresis.py
zuizui0223/balance/theory/STEPWISE_FORCING_HYSTERESIS.md
```

This `small step` is an external `Phi`-forcing resolution assumption, not mutation size in architecture space. The implementation composes the existing switching-cost theorem and rejects forcing paths that violate a prospectively declared maximum jump.

### SCH / BITA — intentionally unchanged

`SCH` owns causal reconstruction of the shared-coordinate compromise. `BITA` owns the architecture crossing and differentiated-coordinate mechanism layer. Neither needs a mesoscopic/HK-like population update to define its current estimand.

The intended transport remains

```text
SCH -> BALANCE -> BITA -> PAYOFF dynamics.
```

## B. Observation / identification side

The human-ethics term `informed consent` is not imported as ecological terminology. The transferable logical structure is implemented as **evidence-admissible transition / fail-closed licensing**.

### TNOA — observation record -> report claim

Files:

```text
zuizui0223/tnoa/tnoa/licensing.py
zuizui0223/tnoa/tests/test_licensing.py
zuizui0223/tnoa/docs/EVIDENCE_ADMISSIBLE_REPORT_TRANSITIONS.md
```

The layer prevents B/T/N/U records from being silently promoted into stronger semantic claims. In particular, baseline does not license biological absence; absence requires a separately validated channel.

### boundary — compatible worlds -> target image

Files:

```text
zuizui0223/boundary/boundary_model/target_identification.py
zuizui0223/boundary/tests/test_target_identification.py
zuizui0223/boundary/docs/TARGET_SPECIFIC_IDENTIFICATION_2026-09-06.md
```

Key distinction:

```text
multiple compatible mechanisms
and
one unique target value
```

can coexist. `boundary` reports structural point-identification only; it does not take ownership of downstream report licensing.

### MROD — mechanism-learning value != target-resolving value

Files:

```text
zuizui0223/mrod/causal_model/target_observation_value.py
zuizui0223/mrod/tests/test_target_observation_value.py
zuizui0223/mrod/docs/TARGET_AWARE_OBSERVATION_VALUE_2026-09-06.md
```

The original publication score remains

```text
V_S(Q)=I(S;Q|A_epsilon)/K.
```

The extension adds a separate declared-target score

```text
V_T(Q)=I(T;Q|A_epsilon)/H(T|A_epsilon).
```

A stored witness has zero mechanism information and one bit of target information, preventing the two utilities from being collapsed.

### REC — correction transport permission

Files:

```text
zuizui0223/rec/scripts/correction_transport_gate.py
zuizui0223/rec/scripts/verify_correction_transport_gate.py
zuizui0223/rec/CORRECTION_TRANSPORT_GATE.md
```

A correction is applied only inside an explicitly validated hardware x observation-context transport cell after validation passes. Success in one setting does not authorize export to an unvalidated setting.

### theouni — finite cross-layer transition witness

Files:

```text
zuizui0223/theouni/theory/evidence_admissible_transition.py
zuizui0223/theouni/theory/verify_evidence_admissible_transition.py
zuizui0223/theouni/theory/DRAFT_EVIDENCE_ADMISSIBLE_TRANSITION.md
```

The draft Evidence-Admissible Transition audit requires:

```text
|T(E_y)|=1
reliability requirement satisfied
proposed report equals the identified target.
```

It is an executable consistency bridge, not a human informed-consent model and not a modification of the frozen Theory Universe core.

## C. Common pattern, without claiming one universal theorem

The implementations expose a recurring distinction:

```text
globally preferable
!= locally reachable

interaction possible
!= interaction locally active

mechanism unresolved
!= every target unresolved

observation informative
!= informative for the requested target

correction successful somewhere
!= correction transportable everywhere

scientific statement conceivable
!= statement admissible under the current evidence contract.
```

The shared pattern is useful for repository navigation, but the mathematical objects differ across evolutionary dynamics, observation theory and scientific reportability. No universal equivalence among them is asserted by this bridge.
