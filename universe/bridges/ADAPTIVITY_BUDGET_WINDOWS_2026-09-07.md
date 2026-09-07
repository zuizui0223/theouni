# Adaptivity is budget-local — 2026-09-07

> **Status:** provenance/interpretation bridge only. Source claims remain owned by PAYOFF, MROD and BALANCE. This file does not modify the frozen Theory Universe core.

The routing work adds a resource axis to the earlier task/resolution-indexed view.

A strict adaptive advantage need not persist as budget increases. There are three qualitatively different regimes:

```text
1. too little budget to route and then act;
2. an intermediate budget where outcome-contingent continuation is useful;
3. enough budget for a fixed design to acquire every measurement it needs and catch up.
```

## MROD information-gap profile

For scenario `s` and pathwise budget `B`, define the class-oracle gap

```text
G_s(B)
= max_adaptive I_s(T; transcript)
  - max_fixed I_s(T; bundle).
```

The fixed class is contained in the adaptive class, so the declared implementation audits `G_s(B)>=0` up to numerical tolerance.

In the registered context-routing witness:

```text
balanced context:
  G(0)=0
  G(1)=0
  G(2)=0.5 bit
  G(3)=0

3/4-versus-1/4 context scenarios:
  G(0)=0
  G(1)=0
  G(2)=0.25 bit
  G(3)=0.
```

Budget 1 cannot both learn the route and use the route-specific assay. Budget 2 can. Budget 3 lets a fixed bundle acquire context and both assays, so the gap closes.

The XOR complementarity adverse control has `G(B)=0` for every tested budget despite zero singleton information and positive two-test information.

Source:

```text
zuizui0223/mrod/causal_model/adaptivity_budget_profile.py
zuizui0223/mrod/docs/ADAPTIVITY_BUDGET_PROFILE.md
```

## PAYOFF resolution-cost window

PAYOFF has no declared probabilities on its bounded-error finite panel, so the corresponding comparison is in acquisition cost rather than bits.

Let

```text
C_adapt = minimum worst-path cost of a resolving adaptive tree
C_fixed = minimum cost of a resolving fixed bundle.
```

An adaptive-only resolution window exists at budgets satisfying

```text
C_adapt <= B < C_fixed.
```

For the registered four-world quadratic/triangular routing witness,

```text
C_adapt=2,
C_fixed=3,
```

so the adaptive-only budget window is exactly

```text
B=2.
```

At lower budgets neither class resolves; at `B>=3` the fixed class catches up.

Source:

```text
zuizui0223/payoff/src/adaptivity_budget_profile.py
zuizui0223/payoff/docs/ADAPTIVITY_BUDGET_WINDOW.md
```

## BALANCE negative control

Under BALANCE's current Cartesian threshold-span objective, a midpoint reset query maps both stay/switch outcomes to the same future span. The existing Bellman control verifies that allowing the next direction to depend on observed branch labels does not improve the optimum fixed allocation of forward/reverse query counts.

Thus its adaptivity-gap profile is identically zero under the declared assumptions, even though query *locations* are updated after each realized outcome.

This matters because

```text
adaptive measurement location
!=
adaptive action-selection advantage.
```

Source:

```text
zuizui0223/balance/docs/ADAPTIVITY_NO_GAIN_CONTROL.md
```

## Cross-repository rule

A useful routing observation needs more than branch dependence. Strict adaptive gain is jointly indexed by

```text
available action vocabulary,
measurement resolution,
resource budget,
and the declared future-value state.
```

Operationally:

```text
branch-dependent continuation + insufficient budget to buy all branches
can create an adaptivity window;

more budget can close that window;

insufficient response resolution can remove it by making both classes unable to identify;

branch-invariant future state can make the gap zero at every budget.
```

No common numerical adaptivity metric is asserted across repositories. MROD uses target-information bits, PAYOFF uses acquisition units for guaranteed finite-panel resolution, and BALANCE uses worst-case threshold-width span.

## Claim boundary

This bridge does not claim that intermediate-budget adaptive advantage is universal. It records three exact synthetic/conditional patterns under already-declared repository contracts:

```text
MROD   -> positive intermediate information gap
PAYOFF -> positive intermediate resolution-cost window
BALANCE-> zero gap under branch-invariant sufficient state.
```

Empirical frequency, field cost distributions, stochastic acquisition error and broader adaptive-design theory remain separate questions.
