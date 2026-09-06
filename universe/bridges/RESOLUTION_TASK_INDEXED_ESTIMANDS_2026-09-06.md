# Resolution- and task-indexed estimands — 2026-09-06

> **Status:** provenance/interpretation bridge only. Source theorems remain owned by their repositories. This file does not modify the frozen Theory Universe core.

The local-transition work exposes a common failure mode that is more precise than a generic warning about model assumptions:

```text
an answer can change because
1. the biological transition/interation scale changed,
2. the numerical/measurement resolution changed,
3. the continuum scaling regime changed, or
4. the scientific task changed.
```

Those are different operations and should not be collapsed.

## 1. PAYOFF — biological locality versus numerical grid scale

PAYOFF distinguishes the declared evolutionary jump radius and interaction range from the numerical architecture grid.

A finite-grid critical jump of one bin is not evidence for a positive biological barrier. The grid-refinement certificate asks whether the **physical** critical distance stabilizes as the grid is refined.

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

For the triangular kernel the biological interaction range itself can be non-dimensionalized as

```text
E=epsilon/r*,  r*=alpha/kappa.
```

The exact global-better barrier phase is bounded by universal curves

```text
g_on(E)=1/E-1,
g_hi(E)=(1-x)(3-x)/(2x^2),
x=[3-sqrt(9-8E)]/2,
g=-gamma/kappa.
```

Thus locality range is not an implementation detail: changing `E` changes the feedback interval in which a finite-jump accessibility barrier exists.

Sources:

```text
zuizui0223/payoff/src/kernel_barrier_resolution.py
zuizui0223/payoff/src/triangular_kernel_phase_curve.py
zuizui0223/payoff/theory/KERNEL_BARRIER_GRID_REFINEMENT.md
zuizui0223/payoff/theory/TRIANGULAR_KERNEL_PHASE_CURVE.md
```

## 2. BALANCE — forcing resolution becomes an identification and design interval

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

The bound can also be inverted into an experimental-resolution requirement. If a maximum width discretization error `eta` is declared, then

```text
delta_up + delta_down <= eta.
```

For forward/reverse sweep spans `(S_up,S_down)`, the continuous minimum-interval allocation obeys

```text
delta_up : delta_down = sqrt(S_up) : sqrt(S_down)
```

with lower bound

```text
N_intervals >= (sqrt(S_up)+sqrt(S_down))^2 / eta.
```

The repository additionally computes the exact minimum integer interval design.

Sources:

```text
zuizui0223/balance/balance_domain/hysteresis_interval.py
zuizui0223/balance/balance_domain/hysteresis_resolution_design.py
zuizui0223/balance/theory/INVERSE_HYSTERESIS_IDENTIFICATION.md
```

## 3. Eco-genetic extension — finite-bin locality has two distinct continuum regimes

For symmetric local trait mutation radius `J`, grid spacing `h`, mutation rate `mu`, and step duration `Delta t`, the translation-invariant finite stencil is exact only at destinations at least `2J` bins from each represented trait boundary. The extra `J` comes from source-side boundary renormalization: sources feeding a destination must themselves have a full mutation neighbourhood.

In that `2J`-deep interior,

```text
(f_i'-f_i)/Delta t
=
mu/(2J Delta t)
sum_{k=1}^J [f_{i-k}+f_{i+k}-2f_i].
```

Its leading local continuum coefficient is

```text
D = mu h^2 (J+1)(2J+1)/(12 Delta t).
```

But `h -> 0` does not define one unique continuum model.

### Fixed bin radius

If `J` is fixed and `Delta t proportional to h^2`, then the physical jump range `Jh -> 0` and higher-order corrections vanish: this is the local diffusion regime.

### Fixed physical radius

If instead

```text
rho=J h > 0
```

is held fixed while `J -> infinity` and `h -> 0`, then

```text
D  -> mu rho^2/(6 Delta t)
C4 -> mu rho^4/(120 Delta t) > 0.
```

The limiting object is the finite-range nonlocal jump operator

```text
L_rho f(z)
=mu/Delta t * [
  (1/(2rho)) integral_{-rho}^{rho} f(z+s) ds - f(z)
].
```

So grid refinement alone does not license a diffusion PDE; the physical locality range must shrink as part of the scaling contract.

Sources:

```text
zuizui0223/eco-genetic-warning-extensions/src/eco_genetic_warning_extensions/general_radius_diffusion.py
zuizui0223/eco-genetic-warning-extensions/src/eco_genetic_warning_extensions/mutation_scaling_regimes.py
zuizui0223/eco-genetic-warning-extensions/docs/GENERAL_RADIUS_DIFFUSION_BRIDGE_2026-09-06.md
```

## 4. MROD — scientific task changes both ordering and stopping

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

Task choice can also change when acquisition stops. A target can already satisfy

```text
H(T|A_epsilon)=0
```

so the target-oriented policy stops without collecting another observation, while a candidate with

```text
I(S;Q|A_epsilon)=1 bit
```

can still remain available for mechanism learning. Thus

```text
target resolved
!=
causal learning exhausted.
```

The implementation deliberately does **not** invent a default weighted sum of the two utilities.

Sources:

```text
zuizui0223/mrod/causal_model/task_pareto.py
zuizui0223/mrod/causal_model/target_sequential_design.py
zuizui0223/mrod/docs/TASK_PARETO_OBSERVATION_VALUE_2026-09-06.md
```

## 5. Cross-repository rule

These examples motivate one navigation rule without claiming a universal theorem:

```text
resolution parameter,
physical locality range,
scaling regime,
or task index
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
-> declare which physical range is shrinking and declare the boundary contract

task objective changes optimal action or stopping
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
!= same answer after numerical refinement

same target identification status
!= same remaining mechanism-learning value.
```

No equality among evolutionary accessibility, hysteresis identification, diffusion scaling and observation utility is asserted. Their common role is diagnostic: each exposes an index that must remain visible if the scientific claim depends on it.
