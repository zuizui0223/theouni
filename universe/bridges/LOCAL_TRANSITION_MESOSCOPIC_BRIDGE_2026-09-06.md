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

Core files now include:

```text
zuizui0223/payoff/src/mesoscopic_architecture.py
zuizui0223/payoff/src/architecture_phase_atlas.py
zuizui0223/payoff/src/bounded_interaction_theory.py
zuizui0223/payoff/src/interaction_kernel_robustness.py
zuizui0223/payoff/src/kernel_accessibility_envelope.py
zuizui0223/payoff/theory/MESOSCOPIC_ARCHITECTURE_DYNAMICS.md
zuizui0223/payoff/theory/BOUNDED_INTERACTION_PHASE_ATLAS.md
zuizui0223/payoff/theory/HARD_CUTOFF_ESCAPE_THEOREM.md
zuizui0223/payoff/theory/SMOOTH_KERNEL_ACCESSIBILITY_ROBUSTNESS.md
zuizui0223/payoff/theory/KERNEL_ACCESSIBILITY_ENVELOPE_RESULT.md
```

Objects:

```text
f(r,t)                         architecture distribution
H_epsilon(r,q)                 bounded architecture interaction
small_jump_mutation            local mutation kernel
population phase               single / interior clusters / endpoint coexistence
critical uphill jump           local accessibility diagnostic
kernel accessibility envelope  all-accessible / all-trapped / kernel-sensitive
```

The bounded kernel is structurally analogous to bounded-confidence interaction, but architectures are not opinions and the repository does not relabel the biological model as Hegselmann--Krause.

The extension now makes a sharper distinction:

```text
local branching onset
!=
nonlocal branch fate
!=
local all-uphill accessibility.
```

For every positive finite interaction radius, the infinitesimal quadratic branching boundary remains

```text
gamma_branch=-kappa/2
```

because sufficiently nearby mutants are still inside the interaction neighbourhood. Finite range instead changes branch maturation after architectures separate far enough for interaction locality to matter.

The hard-cutoff model also yields an exact interface escape-jump theorem. Smooth-kernel controls show that the specific barrier can disappear under smoothing, while other smooth compact and Gaussian kernels can generate barriers at different feedback strengths. Therefore local accessibility is now reported over a declared kernel family rather than treated as kernel-invariant by default.

A registered 40-cell four-kernel sweep gave

```text
all_accessible     18
kernel_sensitive   21
all_trapped         1
```

for the declared one-bin mutation radius. These are grid results, not biological prevalence.

### Eco-genetic warning extensions — trait-bin small-jump bridge

Files now include:

```text
zuizui0223/eco-genetic-warning-extensions/src/eco_genetic_warning_extensions/small_jump_trait_bins.py
zuizui0223/eco-genetic-warning-extensions/src/eco_genetic_warning_extensions/small_jump_diffusion_bridge.py
zuizui0223/eco-genetic-warning-extensions/tests/test_small_jump_trait_bins.py
zuizui0223/eco-genetic-warning-extensions/tests/test_small_jump_diffusion_bridge.py
zuizui0223/eco-genetic-warning-extensions/docs/SMALL_JUMP_TRAIT_BIN_BRIDGE_2026-09-06.md
zuizui0223/eco-genetic-warning-extensions/docs/SMALL_JUMP_DIFFUSION_BRIDGE_2026-09-06.md
```

The locked `eco-genetic-criticality` parent is not modified. The extension adds a prospective local mutation kernel that can be composed with the existing finite trait-bin state in a separately declared experiment.

For radius-one mutation on an equally spaced trait grid, the strict-interior finite-bin generator is now shown exactly to satisfy

```text
(f_i'-f_i)/Delta t
= D (f_{i-1}-2f_i+f_{i+1})/h^2,
D=mu h^2/(2 Delta t).
```

Thus the finite-bin-to-diffusion bridge is exact before the later continuum limit. Boundary-adjacent bins are deliberately excluded because the current finite-bin endpoint renormalisation does not by itself identify a Neumann, reflecting, absorbing, or other continuum boundary condition.

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

Files now include:

```text
zuizui0223/mrod/causal_model/target_observation_value.py
zuizui0223/mrod/causal_model/target_sequential_design.py
zuizui0223/mrod/tests/test_target_observation_value.py
zuizui0223/mrod/tests/test_target_sequential_design.py
zuizui0223/mrod/docs/TARGET_AWARE_OBSERVATION_VALUE_2026-09-06.md
```

The validated publication score remains

```text
V_S(Q)=I(S;Q|A_epsilon)/K.
```

The extension adds the separate declared-target score

```text
V_T(Q)=I(T;Q|A_epsilon)/H(T|A_epsilon).
```

and a target-oriented sequential policy that recomputes `V_T` after each selected observation. A frozen witness gives exact objective reversal:

```text
Q_mech:   I(S;Q)=1 bit, I(T;Q)=0
Q_target: I(S;Q)=0,     I(T;Q)=1 bit.
```

Thus changing the scientific task changes the optimal first measurement. Realised outcomes of unselected candidates remain hidden during ranking.

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

The implementations now expose a richer recurring distinction:

```text
globally preferable
!= locally reachable

locally unstable
!= guaranteed nonlocal branch fate

finite-bin local mutation
!= an assumed continuum boundary condition

mechanism unresolved
!= every target unresolved

mechanism-optimal next observation
!= target-optimal next observation

observation informative
!= informative for the requested target

correction successful somewhere
!= correction transportable everywhere

scientific statement conceivable
!= statement admissible under the current evidence contract.
```

The shared pattern is useful for repository navigation, but the mathematical objects differ across evolutionary dynamics, observation theory and scientific reportability. No universal equivalence among them is asserted by this bridge.
