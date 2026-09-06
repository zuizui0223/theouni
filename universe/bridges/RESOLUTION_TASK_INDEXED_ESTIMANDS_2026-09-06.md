# Resolution- and task-indexed estimands — 2026-09-06

> **Status:** provenance/interpretation bridge only. Source theorems remain owned by their repositories. This file does not modify the frozen Theory Universe core.

The local-transition work exposes a common failure mode that is more precise than a generic warning about model assumptions:

```text
an answer can change because
1. the biological transition scale changed,
2. the numerical/measurement resolution changed, or
3. the scientific task changed.
```

Those are different operations and should not be collapsed.

## 1. PAYOFF — biological jump scale versus numerical grid scale

PAYOFF distinguishes the declared evolutionary jump radius from the numerical architecture grid.

A finite-grid critical jump of one bin is not evidence for a positive biological barrier. The new grid-refinement certificate asks whether the **physical** critical distance stabilizes as the grid is refined.

Registered smooth-kernel witnesses show both outcomes:

```text
positive refinement-stable barrier:
  triangular  gamma=-2,  epsilon=0.3
  cosine      gamma=-3,  epsilon=0.3
  gaussian    gamma=-20, epsilon=0.05

resolution-limited adverse control:
  gamma=-1, epsilon=0.1 under triangular/cosine/gaussian
  critical radius = one bin at every refinement
  physical critical distance -> 0.
```

Therefore

```text
finite-grid obstruction
!=
positive continuum-scale accessibility barrier.
```

Source:

```text
zuizui0223/payoff/src/kernel_barrier_resolution.py
zuizui0223/payoff/theory/KERNEL_BARRIER_GRID_REFINEMENT.md
```

## 2. BALANCE — forcing resolution becomes an identification interval

BALANCE treats the external forcing increment as an observation/design resolution, not an evolutionary mutation scale.

For observed forward/reverse switch points `(F_hat,R_hat)` with monotone step bounds `(delta_up,delta_down)`, the exact switching thresholds satisfy conservative envelopes

```text
F_hat-delta_up <= Phi_F <= F_hat
R_hat <= Phi_R <= R_hat+delta_down.
```

Hence the true hysteresis width is interval-identified:

```text
max(0, W_hat-delta_up-delta_down)
<= W <= W_hat.
```

If the horizon `T` is independently known, the same interval transports to the total switching-cost burden because

```text
C_SD + C_DS = T W.
```

Thus small-step forcing is not merely a smoothness convenience. It determines the precision with which the switching-cost hysteresis can be recovered.

Source:

```text
zuizui0223/balance/balance_domain/hysteresis_interval.py
zuizui0223/balance/theory/INVERSE_HYSTERESIS_IDENTIFICATION.md
```

## 3. Eco-genetic extension — grid spacing, jump radius and time scaling define the continuum coefficient

For symmetric local trait mutation radius `J`, grid spacing `h`, mutation rate `mu`, and step duration `Delta t`, the strict-interior finite operator is exactly

```text
(f_i'-f_i)/Delta t
=
mu/(2J Delta t)
sum_{k=1}^J [f_{i-k}+f_{i+k}-2f_i].
```

Its leading continuum coefficient is

```text
D = mu h^2 (J+1)(2J+1)/(12 Delta t).
```

So a continuum statement is not defined by `h -> 0` alone. The scaling relation among `h`, `J`, `mu`, and `Delta t` is part of the mathematical contract.

Boundary conditions remain separately undeclared: an exact interior generator does not identify a continuum endpoint law.

Source:

```text
zuizui0223/eco-genetic-warning-extensions/src/eco_genetic_warning_extensions/general_radius_diffusion.py
zuizui0223/eco-genetic-warning-extensions/docs/GENERAL_RADIUS_DIFFUSION_BRIDGE_2026-09-06.md
```

## 4. MROD — scientific task changes the observation ordering

MROD keeps

```text
V_S(Q)=I(S;Q|A_epsilon)/K
```

for mechanism resolution separate from

```text
V_T(Q)=I(T;Q|A_epsilon)/H(T|A_epsilon)
```

for a declared target.

A registered finite witness has

```text
Q_mechanism -> (V_S,V_T)=(1,0)
Q_target    -> (V_S,V_T)=(0,1)
Q_noise     -> (V_S,V_T)=(0,0).
```

The first two observations form a two-point Pareto front. There is no unique best next observation until a scientific task or additional decision criterion is declared.

The implementation deliberately does **not** invent a default weighted sum of the two utilities.

Source:

```text
zuizui0223/mrod/causal_model/task_pareto.py
zuizui0223/mrod/docs/TASK_PARETO_OBSERVATION_VALUE_2026-09-06.md
```

## 5. Cross-repository rule

These examples motivate one navigation rule without claiming a universal theorem:

```text
resolution parameter
or
task index
that can change the answer
must be carried with the estimand rather than hidden as implementation detail.
```

Operationally:

```text
numerical refinement changes answer
-> audit numerical convergence before biological interpretation

biological/experimental step bound changes answer
-> report an identification interval or accessibility class indexed by that bound

continuum scaling changes answer
-> declare the scaling regime and boundary contract

task objective changes optimal action
-> report task-indexed policies or a Pareto set, not a universal optimum.
```

## 6. Relation to Theory Universe

This bridge is compatible with the existing contract-indexed worldview:

```text
same stored representation
!= adequate for every later task

same evidence
!= same utility under every target

same discrete implementation
!= same continuum object under every scaling

same finite-grid answer
!= same answer after numerical refinement.
```

No equality among evolutionary accessibility, hysteresis identification, diffusion scaling and observation utility is asserted. Their common role is diagnostic: each exposes an index that must remain visible if the scientific claim depends on it.
