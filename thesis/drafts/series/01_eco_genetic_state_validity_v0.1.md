# Chapter 1 — Eco-genetic State Is Responsibility-Specific

## Problem

A single ecological system can be summarized in many ways: interaction intensity, potential trait viability, realised trait occupancy, demographic state, local and metapopulation genetic diversity, allele persistence, or an early genetic signal. The tempting shortcut is to treat these quantities as different readouts of one latent eco-genetic deterioration axis. If that shortcut were valid, one scalar state could order the system, matching coarse marginals would be enough to determine what happens next, and a genetic signal that consistently precedes loss could be treated as a warning.

This chapter asks a narrower and more testable question:

> **Can one eco-genetic representation support several distinct scientific responsibilities at once: cross-target state representation, next-transition prediction, downstream risk prediction, and predictive warning?**

The chapter integrates source-owned results from `eco-genetic-criticality` and `eco-genetic-warning-extensions`. Integration does **not** mean that one source result proves the next. The common object is the scientific responsibility assigned to a representation.

## Standalone contribution

The chapter makes one domain-level claim:

> **Eco-genetic state validity is responsibility-specific. A representation adequate for one target or task need not be adequate for another, even inside one declared finite model programme.**

Three independent tests recover this claim at different levels:

1. **cross-target scalar adequacy** — when can several target variables share one monotone sufficient scalar state?
2. **transition adequacy** — do equal coarse marginals determine the same exact next transition and downstream loss risk?
3. **warning adequacy** — does event-conditioned temporal precedence imply predictive discrimination over the full eligible denominator?

The results are linked horizontally by the question of adequacy, not vertically by theorem implication.

## 1. Cross-target state representation

Let a finite ecological world carry a target vector

\[
T(\omega)=(T_1(\omega),\ldots,T_m(\omega)),
\]

with each coordinate oriented so that larger means no worse for the declared responsibility. A scalar state `h` is directionally coherent and sufficient when each target factors through `h` by a nondecreasing map.

The source theorem gives an exact criterion:

> **A common directionally coherent sufficient scalar exists iff the distinct target vectors form a chain under the product order.**

This is stronger than defining several variables and observing that they differ. If two states cross—one target improves while another worsens—then any scalar ordering of the states forces at least one target map to violate monotonicity. Conversely, a finite product-order chain can be ranked to construct a sufficient scalar.

### Locked crossing

The locked fragmentation gradient supplies a direct violation of the chain condition. From the 2-patch to the 16-patch state, interaction and local effective size decrease while realised high-trait mass increases:

- interaction: approximately `0.00174443 -> 0.00124401`;
- local effective size: approximately `0.221311 -> 0.033058`;
- realised high-trait mass: approximately `0.282918 -> 0.393880`.

The target vector therefore crosses in product order. No exact common monotone scalar can preserve even these target coordinates on the locked comparison.

A second separation is between **potential viability** and **realised occupancy**. In the preregistered fragmentation gradient, potential high-trait viability changed from present in `1037/1037` one-patch prepared outcomes to absent at every tested subdivision, whereas realised high-trait occupancy remained present at the 30-generation endpoint in approximately `99.6–100%` of supported trajectories. Potential and realised state therefore cannot be collapsed merely because they refer to the same trait.

## 2. Transition sufficiency of a coarse eco-genetic state

A scalar-representation failure does not by itself prove that the usual coarse marginals are dynamically insufficient. That is a separate question.

The state-validity construction fixes the declared census, interaction-state multiset, allele-frequency multiset, trait-mass multiset, complete trait-bin totals, `H_alpha`, `H_gamma`, and `F_ST`, while reversing patchwise cross-layer alignment.

The aligned and anti-aligned states therefore share the declared coarse marginal signature, but cross-layer covariance changes from `+0.025` to `-0.025`. Their exact next interaction transitions differ patchwise, with maximum generation-1 difference approximately

\[
0.2543.
\]

Thus the coarse marginals are not transition-sufficient for the declared local dynamics.

### Downstream propagation is a separate quantitative question

The original frozen 500-pair, 60-generation comparison gave loss risks `0.678` versus `0.722`, an anti-aligned minus aligned difference of `+4.4` percentage points with paired 95% interval approximately `-1.2` to `+10.0` points. The correct reading is imprecision, not equivalence.

A separately locked post-Phase-V experiment then used one common trajectory family, the original forcing rate, four predeclared readout horizons, and nested paired sample sizes. At the primary `1500`-pair scale, anti-aligned minus aligned loss-risk differences were approximately:

| generation | risk difference |
|---:|---:|
| 5 | `0.00` pp |
| 10 | `+0.33` pp |
| 20 | `+5.33` pp |
| 40 | `+5.20` pp |

The paired 95% intervals at generations 20 and 40 were approximately `+2.04 to +8.62` and `+1.96 to +8.44` percentage points. Under the declared forcing path, the hidden alignment difference therefore had little realised loss-risk consequence at the 5–10 generation readouts, had propagated to about five percentage points by generation 20, and remained similar at generation 40.

This does not identify generation 20 as a universal biological threshold. It shows why **transition sufficiency and long-horizon consequence are different responsibilities**.

## 3. Temporal precedence versus predictive warning

The warning question is independent of the common-scalar theorem and of the propagation theorem. It starts from frozen event/non-event definitions and asks whether the six predeclared relative genetic thresholds discriminate future loss over the full eligible denominator.

Let `Y` indicate an event by the fixed horizon and `M` indicate whether a binary marker fired by that horizon. If every event has prior marker firing, then sensitivity is one. But the number of marker-positive non-events remains unconstrained.

For a binary marker,

\[
\mathrm{AUC}=\frac{\mathrm{sensitivity}+\mathrm{specificity}}{2}.
\]

Therefore perfect event-conditioned precedence is compatible with binary-marker AUC anywhere from `0.5` to `1`. The worst endpoint is sharp: if every non-event also fires, specificity is zero and AUC is `0.5`.

### Frozen full-denominator recovery

That sharp endpoint is exactly what the frozen audit reaches.

- inherited ensemble: all `35/35` events had prior firing, but all `48/48` non-events also fired;
- fresh ensemble: all `33/33` events had prior firing, but all `49/49` non-events also fired.

Thus sensitivity is `1`, specificity is `0`, and binary-marker AUC is `0.5` in both frozen ensembles.

The result does not show that genetic diversity contains no predictive information generally. It shows that **these six frozen binary warning rules, evaluated over their full denominator, do not discriminate events from non-events despite perfect event-conditioned precedence**.

## 4. Why the three results belong in one chapter

The three source results answer different adequacy questions about representations inside one eco-genetic programme:

| Responsibility | Exact / locked question | Result |
|---|---|---|
| cross-target state | can several target variables share one monotone sufficient scalar? | iff product-order chain; locked crossing violates it |
| transition prediction | do equal coarse marginals imply the same next transition? | no; exact difference `0.2543` |
| downstream risk | does the hidden transition distinction matter immediately and equally across horizons? | no; little contrast at 5–10, about 5 pp at 20–40 under declared forcing |
| warning | does perfect precedence imply predictive discrimination? | no; specificity `0`, AUC `0.5` in both frozen ensembles |

The scientific synthesis is therefore not “everything is different.” It is:

> **Adequacy must be indexed by the responsibility assigned to the eco-genetic state.**

## Internal dependency map

There is no theorem chain of the form

```text
common-scalar failure -> transition failure -> warning failure.
```

Instead:

- the common-scalar theorem owns a cross-target representability condition;
- the aligned/anti-aligned construction owns a transition-sufficiency counterexample and propagation experiment;
- the warning theorem owns the denominator/discrimination condition;
- all three reuse source-frozen semantic or model contracts where declared, but none upgrades the others' proof status.

## Claim ceiling

This chapter does **not** establish:

- one universal eco-genetic state variable;
- that every ecological target must use a different state;
- a natural-system 20-generation propagation threshold;
- that genetic diversity is generally non-predictive;
- that the common-scalar theorem causes or explains the frozen warning failure;
- empirical validation of the finite closure by the natural-data four-gate programme.

The natural-data programme remains a companion measurement-validation line because it tests whether candidate ecological states/proxies earn endpoint relevance in heterogeneous observed systems. It is not used here as replication of the finite model.

## Source ownership

- state-separation theorem, fragmentation crossing, potential-versus-realised state: `zuizui0223/eco-genetic-criticality`;
- aligned/anti-aligned transition certificate, Phase-V interval, post-Phase-V propagation experiment: `zuizui0223/eco-genetic-warning-extensions` state-validity lane;
- full-denominator warning theorem and frozen audit: `zuizui0223/eco-genetic-warning-extensions` warning-validity lane;
- chapter-level integration and dependency firewall: `zuizui0223/theouni`.

No proof, data set, or frozen numerical artifact is transferred to `theouni` by this chapter.

## Dissertation handoff

The eco-genetic series shows that the representation adequate for one scientific job can fail another job even before leaving one model programme. The next chapter asks the more general question:

> **What changes in the future scientific contract make an old state merge cease to be legitimate in the first place?**
