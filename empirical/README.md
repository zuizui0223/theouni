# Concrete Research Universe v0.1

This layer sits **outside** the frozen Theory Universe v0.5 semantic core.

Its job is to classify concrete ecological research programmes before any named species, island system, SDM product, or sensor dataset is admitted through `theory/EMPIRICAL_PROJECTION_GATE.md`.

The central rule is:

> **A concrete research programme is not itself a state. It is a typed way of constructing worlds, candidate coordinates, contexts, targets, or observations that may later support a state claim.**

## Five programme archetypes

### CR-1 — Comparative phenomenon programme

Examples of the eventual class include island syndrome, urban fragmentation, repeated ecological convergence, or other named macroecological phenomena.

Primary role:

- define a phenomenon label or upstream context `H`;
- define comparable ecological units `U` across systems;
- ask whether the phenomenon label retains predictive information after a measured process state `Z` is supplied.

Canonical projection:

```text
phenomenon label / origin H
        +
measured process coordinates Z
        +
future endpoint Y
        -> Empirical Projection Gate
```

Forbidden upgrade:

```text
island / urban / habitat label = ecological state
```

A phenomenon becomes mechanistically interesting when different origins become predictively redundant after conditioning on the same target-relevant state, or when residual origin information reveals a missing coordinate.

---

### CR-2 — Lineage and trait-evolution programme

This is the natural home for a concrete lineage, clade, or focal species complex studied through evolutionary time.

Primary role:

- define historical objects `H` such as lineage, transition history, replacement path, ancestry, or retained biochemical state;
- define present candidate coordinates `Z`;
- define competing mechanism programmes `Theta`;
- define evolutionary or functional target `Y`.

Canonical projection:

```text
lineage/history H
      + present traits Z
      + candidate mechanisms Theta
      + target Y
      -> history/mechanism-aware empirical projection
```

Forbidden upgrades:

```text
phylogeny = causal history
visible phenotype = biochemical state
ancestral reconstruction = direct observation of past world
```

This type can later bridge to MLTR, MRM, RACH, and CREST, but only through explicit uncertainty-preserving maps.

---

### CR-3 — Phenotype / polymorphism / trait-construction programme

This type covers within-lineage continuous or discrete phenotype variation, polymorphism, trait integration, latent trait construction, and spatial phenotype structure.

Primary role:

- define how raw measurements become candidate phenotype coordinates `Z`;
- distinguish direct measurements from latent constructions, scores, or image-derived traits;
- test whether those coordinates predict the declared future/functional target;
- test whether environment, geography, ancestry, or interaction context retains residual information after `Z`.

Canonical projection:

```text
raw measurements
   -> trait construction Z
   -> held-out target Y
   -> residual context H
```

Forbidden upgrades:

```text
PCA/CFA/latent score = natural state
trait correlation = mechanism
spatial clustering = causal process
```

A trait representation earns empirical partial-state status only through the projection gate, not by dimensional reduction alone.

---

### CR-4 — Spatial world-construction and forecast programme

This type covers SDMs, candidate-universe learning, latent-world reconstruction, reachability/support maps, and survey candidate generation.

Primary role:

- construct or constrain a model-world universe `Omega`;
- define support, suitability, reachability, candidate patches, or future-world sets;
- expose scale, mask, source closure, horizon, and uncertainty;
- hand off candidate worlds or sites to observation design.

Canonical projection:

```text
environmental / occurrence evidence
   -> candidate world universe Omega
   -> support / reachability / candidate locations
   -> external observation
```

Forbidden upgrades:

```text
suitability = occupancy
candidate patch = presence
latent world identity = true history
support map = biological state
```

This is a **world-construction method type**, not automatically a biological-state type.

---

### CR-5 — Sensing and observability programme

This type covers visit cameras, timelapse systems, automated event detection, classifier pipelines, effort records, and sensor failure architecture.

Primary role:

- generate `ObservationRecord` objects;
- define observation map `O` and effort denominator;
- quantify false-positive, missed-detection, attribution, calibration, failure-domain, and reset structure;
- provide evidence to CED/RACH/empirical projection only at the resolution earned by calibration.

Canonical projection:

```text
real ecological process
   -> sensor / observer
   -> record y
   -> reliability-qualified EvidenceClass
```

Forbidden upgrades:

```text
classifier detection = confirmed biological event
camera effort = visitation rate without denominator/calibration
sensor state = biological interaction state
```

This is an **observation-process type**. It measures the empirical world; it does not define the biological world by itself.

---

## Shared projection contract

Every programme type ultimately supplies fields to the frozen empirical projection contract

\[
\mathcal P_{emp}=(U,\tau,Z,H,A,Y,\mathcal O,\mathcal V,\Delta,\epsilon).
\]

The five archetypes emphasize different fields:

| Programme | Primary fields | Secondary fields |
|---|---|---|
| CR-1 phenomenon | `U, H, Z, Y, V` | `A, O` |
| CR-2 lineage/evolution | `tau, H, Z, A, Y` | `O, V` |
| CR-3 phenotype/polymorphism | `Z, U, Y, H, V` | `tau, O` |
| CR-4 spatial world construction | `Omega proxy, U, A, Y, V` | `H, O` |
| CR-5 sensing/observability | `O, U, tau, V` | `Z, Y` |

No archetype is allowed to bypass G0–G5 in `theory/EMPIRICAL_PROJECTION_GATE.md`.

## Composition rules among archetypes

The types are composable but not interchangeable.

```text
CR-4 spatial world construction
        -> candidate sites/worlds
        -> CR-5 sensing
        -> ObservationRecord / EvidenceClass

CR-3 phenotype construction
        -> candidate Z
        -> CR-1 phenomenon comparison
        -> residual origin/context test

CR-2 lineage/history
        -> H / Theta candidates
        -> CR-3 phenotype or CR-1 phenomenon programme
        -> MLTR/MRM/RACH-compatible projection
```

A method programme can support a biological programme without becoming its biological state.

## Decision outputs

Concrete programmes do not directly return `RequiredState`. They may return one or more of:

- `CandidateCoordinateSet`;
- `ContextDescriptor`;
- `ModelWorldUniverse` / support field;
- `ObservationRecord`;
- `ObservabilityContract`;
- `CandidateCausalProgrammeSet`;
- `EmpiricalPartialState` decision E0–E4 from the projection gate.

Only the last category is allowed to use state language across repositories, and even then only with its declared target/domain/validation scope.

## Boundary to named projects

No named project is assigned here yet. The next step is to instantiate these five archetypes with typed manifests for the concrete research portfolio while keeping source repository ownership unchanged.
