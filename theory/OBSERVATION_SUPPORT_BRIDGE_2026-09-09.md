# Observation-Support Bridge — Model Qualification Is Not Empirical Admission

Status: synthesis / architecture note. This document introduces no new source-owned empirical result and does not claim a novel mathematical theorem. Its purpose is to keep three logically distinct admission questions separate across the `theouni` stack.

## 1. Three gates

For a target empirical claim \(\tau\), distinguish:

1. **Method validity** \(V(M,W)\): the procedure \(M\) has the declared error/power properties on a specified model or semi-synthetic world family \(W\).
2. **Deployment-geometry adequacy** \(D(M,G)\): the intended sampling geometry \(G\) contains enough structural support for the declared target to be detectable with the frozen method.
3. **Observation-support admissibility** \(O(R,G)\): after the realized measurement process \(R\), enough of the predeclared observational support remains to instantiate the geometry and statistic whose properties were qualified.

These are not interchangeable:

```text
V(M,W) != D(M,G) != O(R,G)
```

An empirical target may be opened only under the declared conjunction

\[
V(M,W) \land D(M,G) \land O(R,G).
\]

This is an admission convention, not a claim that every scientific workflow must use these exact three labels.

## 2. Legitimate termination

If method validity passes but observation support fails,

\[
V(M,W)=1, \qquad O(R,G)=0,
\]

the licensed endpoint is

```text
not_evaluable / abstain
```

rather than

```text
negative biological result.
```

The reason is simple: the downstream empirical estimand was never instantiated under the predeclared support contract. A failure to open the statistic cannot determine the sign, magnitude, or absence of the biological target.

This gives a bridge discipline:

```text
qualified model-world procedure
        |
        v
predeclared deployment geometry
        |
        v
realized measurement support
        |
        +-- sufficient --> empirical statistic may be opened
        |
        +-- insufficient --> not_evaluable; stop
```

## 3. Relation to the existing hierarchy

This note refines, without replacing, the distinction already used in `WORLD_STATE_EVIDENCE_HIERARCHY_2026-09-08.md`:

```text
RequiredState
    !=
ObservationRecord / CompatibleWorldSet
    !=
ReportableTarget.
```

The observation-support gate lives at the bridge between a qualified inferential design and the evidence actually retained by measurement. It therefore answers a different question from CREST-style required-state lower bounds and from CED-style evidence sufficiency:

- **CREST / required-state layer:** what distinctions would a responsibility require?
- **method/deployment layer:** can the declared procedure recover the target on the declared geometry?
- **observation-support layer:** did the realized measurement process preserve enough support to instantiate that qualified procedure?
- **evidence/reportability layer:** given what was actually observed, what target statements are licensed?

A failure at any one layer cannot automatically be promoted into a conclusion owned by another layer.

## 4. Bounded source-owned witness: TTF v0.11 → v0.12

Owning source: `zuizui0223/TTF`, branch `analysis/gate-i-geometry-calibration`.

### v0.11 — qualified model/deployment surface

A fresh species-disjoint plant geometry was prospectively frozen at 250 species × 100 records, using density-scaled `k=15` and fixed 125/125 train/evaluation species.

The frozen confirmatory result passed:

- maximum private-world Wilson 95% upper bound: **0.09580 ≤ 0.10**;
- shared amplitude-2 power: **0.998**;
- Wilson 95% lower bound: **0.98876 ≥ 0.80**.

Thus the declared method/design surface was qualified for that synthetic/semi-synthetic responsibility.

### v0.12 — realized observation support

Before any empirical TTF statistic was permitted to open, the same 25,000 frozen photo IDs passed through an independently frozen location-blind measurement pipeline. The predeclared gate required all 250 species to retain at least 40 evaluable photographs.

Terminal result:

- **189/250** species met the minimum;
- median evaluable records/species = **51**;
- minimum = **15**;
- retained actual geometry = **0 species / 0 records**;
- colour-vector values were not read by TTF;
- pairwise colour distances were not computed;
- the empirical TTF transfer statistic was not computed.

Therefore the source-owned terminal state was `not_evaluable_actual_geometry_classifiability_gate_failed`.

This is a concrete witness of

```text
method/design qualification PASS
        +
actual observation-support FAIL
        ->
empirical claim remains unopened
```

## 5. What this witness does not establish

TTF v0.11/v0.12 does **not** establish:

- that real ecological observation generally destroys model validity;
- that flower-colour shared transitions are absent or present;
- that CREST, CED, or any other `theouni` theory is empirically true;
- that the three-gate decomposition is uniquely correct or mathematically novel;
- a universal numerical threshold for observational adequacy.

It supplies one unusually clean source-owned case where the workflow was designed so that a support failure terminated the empirical bridge before the biological statistic was opened.

## 6. Dissertation use

The safe dissertation-level synthesis is:

> A representation or inference rule may be adequate in its declared model-world responsibility while the realized observation process fails to preserve the support needed to instantiate that responsibility empirically. In that case, disciplined inference terminates as non-evaluable rather than converting missing admissibility into a biological negative.

This sentence should be cited to the TTF source-owned frozen ledgers when used as an empirical illustration. It should not be presented as a theorem derived from the TTF data.
