# Concrete Research Universe v0.1

This layer sits **outside** the frozen Theory Universe v0.5 semantic core.

Its job is to classify concrete ecological research programmes before any named species, island system, SDM product, or sensor dataset is admitted through `theory/EMPIRICAL_PROJECTION_GATE.md`.

The central rule is:

> **A concrete research programme is not itself a state. It is a typed way of constructing worlds, candidate coordinates, contexts, targets, or observations that may later support a state claim.**

## Five programme archetypes

### CR-1 — Comparative phenomenon programme

Examples include island syndrome, urban fragmentation, repeated ecological convergence, or other named macroecological phenomena.

Primary role: define phenomenon/origin context `H`, comparable units `U`, candidate process coordinates `Z`, and test whether upstream context remains predictive after `Z`.

```text
phenomenon / origin H
    + measured process coordinates Z
    + future endpoint Y
    -> Empirical Projection Gate
```

Forbidden upgrade:

```text
island / urban / habitat label = ecological state
```

### CR-2 — Lineage and trait-evolution programme

Primary role: supply historical objects `H`, present traits `Z`, retained mechanism candidates `Theta`, and evolutionary/functional target `Y`.

```text
lineage/history H
    + present traits Z
    + candidate mechanisms Theta
    + target Y
    -> history/mechanism-aware projection
```

Forbidden upgrades:

```text
phylogeny = causal history
visible phenotype = biochemical state
ancestral reconstruction = direct observation of past world
```

### CR-3 — Phenotype / polymorphism / trait-construction programme

Primary role: construct measured/latent phenotype coordinates `Z`, then test their target relevance and whether environment, geography, ancestry, or interaction context retains residual information.

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

### CR-4 — Spatial world-construction and forecast programme

Primary role: construct/constrain `Omega`, support, suitability, reachability, candidate worlds, or candidate observation locations.

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

### CR-5 — Sensing and observability programme

Primary role: generate `ObservationRecord`, effort and calibration metadata, and observation failure architecture.

```text
real ecological process
    -> sensor / observer
    -> record y
    -> reliability qualification
    -> evidence
```

Forbidden upgrades:

```text
classifier detection = confirmed biological event
camera effort = visitation rate without denominator/calibration
sensor state = biological interaction state
```

This is an **observation-process type**. It measures the empirical world; it does not define the biological world by itself.

## Shared projection contract

Every programme ultimately supplies fields to

\[
\mathcal P_{emp}=(U,\tau,Z,H,A,Y,\mathcal O,\mathcal V,\Delta,\epsilon).
\]

| Programme | Primary fields | Secondary fields |
|---|---|---|
| CR-1 phenomenon | `U, H, Z, Y, V` | `A, O` |
| CR-2 lineage/evolution | `tau, H, Z, A, Y` | `O, V` |
| CR-3 phenotype/polymorphism | `Z, U, Y, H, V` | `tau, O` |
| CR-4 spatial world construction | `Omega proxy, U, A, Y, V` | `H, O` |
| CR-5 sensing/observability | `O, U, tau, V` | `Z, Y` |

No archetype may bypass G0–G5 in `theory/EMPIRICAL_PROJECTION_GATE.md`.

## Composition rules

```text
CR-4 spatial world construction
    -> candidate sites/worlds
    -> CR-5 sensing
    -> reliability-qualified records

CR-3 phenotype construction
    -> candidate Z
    -> CR-1 phenomenon comparison
    -> residual origin/context test

CR-2 lineage/history
    -> H / Theta candidates
    -> CR-3 or CR-1
    -> MLTR/MRM/RACH-compatible projection
```

A method programme can support a biological programme without becoming its biological state.

## Reality-to-Theory path firewall

The machine-readable bridge graph is [`reality_theory_graph.json`](reality_theory_graph.json).

Its validated invariants are:

1. every path from any `CR-*` programme to `RequiredState` passes `EmpiricalProjectionGate`;
2. every path from `NamedProject` to `RequiredState` passes `EmpiricalProjectionGate`;
3. every route from raw CR-5 sensor output to a biological-event record passes `ReliabilityQualification`;
4. candidate world support from CR-4 cannot directly become a state.

The validator is [`validate_reality_theory_graph.py`](validate_reality_theory_graph.py).

## Current provisional repository typing

Typing means **scientific role only**. Every repository below remains `projection_status = not_instantiated_here`; none is granted empirical-state status by this table.

| Primary type | Provisionally typed repositories |
|---|---|
| CR-1 comparative phenomenon | `island`, `izu-core`, `fcp` |
| CR-2 lineage/evolution | `EAzami`, `chun` |
| CR-3 phenotype/trait construction | `hotarubukuro`, `azami`, `shimahotarubukuro` |
| CR-4 spatial world construction | `eog`, `sdmr`, `acsp` |
| CR-5 sensing/observability | `pollipi`, `insepi` |

Secondary typing preserves mixed roles; for example `island` also uses CR-4 spatial support, `azami` hands temporal questions to CR-2, and `hotarubukuro` can feed a CR-1 comparative context.

The authoritative typing-only map is [`project_typing_map.json`](project_typing_map.json).

Theory/inference owners (`crest`, `ccoc`, `mltr`, `mrm`, `ced`, `microdonta`, the eco-genetic theory pair), `theouni`, the `bita` connector, and the `odsp` tombstone are deliberately excluded from CR v0.1 typing.

## Decision outputs

Concrete programmes do not directly return `RequiredState`. They may return:

- `CandidateCoordinateSet`;
- `ContextDescriptor`;
- `ModelWorldUniverse` / support field;
- `ObservationRecord`;
- `ObservabilityContract`;
- `CandidateCausalProgrammeSet`;
- projection-gate decisions E0–E4.

Only a projection-gate decision may support cross-repository `EmpiricalPartialState` language, and only with its declared target/domain/validation scope.

## Machine-readable artifacts

- [`system_types.json`](system_types.json) — five CR types and allowed composition edges.
- [`project_manifest.template.json`](project_manifest.template.json) — reusable typed manifest for one named project.
- [`project_typing_map.json`](project_typing_map.json) — provisional typing of current concrete repositories.
- [`reality_theory_graph.json`](reality_theory_graph.json) — Reality-to-Theory path architecture.
- [`validate_empirical_universe.py`](validate_empirical_universe.py) — type/typing validator.
- [`validate_reality_theory_graph.py`](validate_reality_theory_graph.py) — path-firewall validator.

## Next boundary

The next scientifically meaningful step is **not to promote these typed repositories to state examples**. It is to instantiate `project_manifest.template.json` from each source repository, pin its empirical unit, target, candidate coordinates, context, observation/reliability contract, and validation unit, and only then run the Empirical Projection Gate.
