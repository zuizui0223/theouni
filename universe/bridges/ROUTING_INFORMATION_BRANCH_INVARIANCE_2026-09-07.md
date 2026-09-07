# Routing information and branch-invariance — 2026-09-07

> **Status:** provenance/interpretation bridge only. Source algorithms and claims remain owned by PAYOFF, BALANCE and MROD. This file does not modify the frozen Theory Universe core.

The recent adaptive-design extensions expose a distinction not captured by ordinary "how much does this observation tell us about the target?" language:

```text
an observation can be useful because
its result changes what should be measured next,
even when it does not directly resolve or inform the final target.
```

That is a routing role, not a new universal information measure.

## 1. MROD — direct target information versus continuation routing

For a selected adaptive policy with root observation `Q1` and full transcript `H`, MROD now audits

```text
I(T;H)
= I(T;Q1)
  + [I(T;H)-I(T;Q1)].
```

The first term is direct root target information. The second is conditional continuation target information.

Separately, if `A2` denotes the immediate next query selected by the already-declared policy after observing the root outcome, MROD reports

```text
H(A2)
```

as routing-action entropy. This is entropy of the next action identity, **not** information about `T`.

In the registered context/assay witness,

```text
I(T;context)=0,
context=0 -> assay0,
context=1 -> assay1.
```

For balanced context frequencies:

```text
root direct target information       = 0 bit
full adaptive target information     = 1 bit
conditional continuation information = 1 bit
routing-action entropy                = 1 bit
adaptive gain over best fixed pair   = 0.5 bit.
```

An XOR adverse control also has a zero-MI first observation and positive later information, but its second query is the same on every root branch. Routing-action entropy is zero and adaptive gain over the best fixed pair is zero.

Therefore

```text
zero direct target information
!=
routing value,
```

and

```text
positive continuation information
!=
adaptive advantage.
```

Source:

```text
zuizui0223/mrod/causal_model/adaptive_routing_audit.py
zuizui0223/mrod/docs/ROUTING_INFORMATION_AUDIT.md
```

## 2. PAYOFF — branch-dependent measurement identity without invented probabilities

PAYOFF's finite-panel bounded-error design has no declared world probabilities, so it does not translate the same structure into bits.

The routing audit instead asks whether different first-response cells require different immediate next contrasts.

For the registered four-world quadratic/triangular witness,

```text
first: intrinsic_r_0.5

low-alpha branch  -> interaction_d_0.2
high-alpha branch -> interaction_d_0.1.
```

The root does not resolve the phase on every branch. The minimum resolving fixed bundle costs 3 acquisition units; the adaptive tree costs 2. Hence

```text
branch-dependent continuation = true
root direct phase resolution   = false
adaptive worst-path saving     = 1 acquisition unit.
```

A direct-resolution two-world control has one root contrast that finishes the phase decision immediately and gives no routing-only saving.

Source:

```text
zuizui0223/payoff/src/adaptive_routing_audit.py
zuizui0223/payoff/docs/ADAPTIVE_ROUTING_AUDIT.md
```

## 3. BALANCE — branch invariance gives a negative control

BALANCE supplies the useful opposite case.

For a threshold bracket with span `w` and bounded command error `e`, a minimax midpoint reset query leaves worst-case span

```text
a(w,e)=min(w,w/2+e)
```

under either stay or switch outcome. The two posterior intervals have different locations but the same span.

Under the declared BALANCE objective, future value depends on the sufficient state

```text
sigma = (w_F, w_R, remaining_budget,
         e_F, e_R, acquisition_costs),
```

not on interval location. Therefore both outcomes of a midpoint query map to the same future `sigma` for the queried direction. Allowing the next **direction** to depend on the observed stay/switch label cannot beat the existing optimum count allocation. The repository verifies this against a separate Bellman recursion.

Source:

```text
zuizui0223/balance/docs/ADAPTIVITY_NO_GAIN_CONTROL.md
zuizui0223/balance/tests/test_adaptive_allocation_control.py
```

## 4. Branch-invariance criterion

The three repositories motivate a restricted sequential-design rule.

Let a declared sequential problem have current state `s`, remaining resources `B`, observation/action `q`, outcome `y`, and a sufficient continuation state

```text
sigma(s,B).
```

Assume all future feasible actions, costs and objective values depend on history only through `sigma`.

If, for a particular observation `q`,

```text
sigma(s_{q,y}, B-cost(q)) = sigma'
```

for every possible outcome `y`, then the outcome of `q` cannot have **routing value at that step** under this declared sufficient-state representation. Every branch presents the same continuation problem. Branch-specific action labels can only be tie-breaking among continuation-equivalent choices.

If this branch invariance holds at every reachable node, adaptive outcome-contingent planning collapses to a non-outcome-contingent action sequence for the declared objective.

The converse is deliberately weaker:

```text
branch-dependent continuation state
is necessary for a strict routing advantage,
but is not sufficient.
```

Different child states can still share the same optimal continuation or equal value. A positive adaptive advantage must be demonstrated by the actual fixed-versus-adaptive comparison, as PAYOFF and MROD do in their registered witnesses.

## 5. Relation to the earlier task-indexed estimand bridge

The earlier bridge said that task, resolution, physical locality and scaling regime must remain visible when changing them can change the answer.

Routing adds another index:

```text
history-dependent continuation policy.
```

The same observation can have

```text
low or zero direct target information
but positive policy-routing value,
```

or

```text
positive direct/continuation information
but zero adaptive advantage over a fixed plan.
```

Therefore an acquisition report should keep at least these questions separate:

```text
1. Did this observation directly reduce target uncertainty?
2. Did its outcome change the appropriate next action?
3. Did allowing that branch dependence improve the declared objective?
4. Did the resulting evidence actually identify/license the scientific target?
```

## 6. Claim boundary

This bridge does not claim a new general theory of value of information or adaptive experimental design. Sequential value of information, contingent test selection and adaptive policies are established topics. The contribution here is a repository-level separation of direct target information, continuation information, routing structure, adaptive gain and evidence licensing under the already-declared ecological contracts.

No common numerical scale is asserted across the three repositories:

```text
MROD   -> target information / regret in bits
PAYOFF -> acquisition units for finite-panel phase discrimination
BALANCE-> worst-case threshold-width span.
```

Their commonality is structural, not metric.
