# Theoretical Universe / 理論宇宙

`theouni` has two deliberately separate layers.

1. **Theory Universe** — the theory-first ontology and mathematics of worlds, states, evidence, learning, revision, dynamics, and warning.
2. **Portfolio Registry** — the provenance-preserving map of the wider repository ecosystem and its typed bridges.

The theory layer comes first. Concrete species, island syndromes, SDMs, sensors, and empirical workflows do not define the core theory; they are projected into it later through explicit contracts.

## Central programme

> **What may science safely forget, what must remain revisable, and what exactly is science trying to learn or license?**

The current worldview is:

- ecological reality is temporally extended and is not itself a `State`;
- mathematics acts on declared `ModelWorld`s rather than directly on reality;
- a `RequiredState` is a contract-relative quotient of model worlds;
- ecological laws are effective laws on adequate quotients;
- `EvidenceClass` is epistemic and is not the same object as `RequiredState`;
- causal uncertainty remains set-valued until discriminating evidence exists;
- warning validity is conditional on a declared loss-generating state;
- a state adequate for one contract can become unrevisable after later responsibilities require distinctions previously forgotten;
- causal-learning value and target-licensing value are distinct scientific utilities.

```mermaid
flowchart TD
    R[Ecological reality] -->|model / measurement bridge| W[Model-world universe]
    W --> C[Scientific contract]
    C --> G[Future / Gamma]
    C --> H[History / H]
    C --> M[Mechanism / Theta]
    C --> D[Evidence / D]
    C --> T[Target / T]

    G --> CCOC[CCOC]
    H --> MLTR[MLTR]
    M --> MRM[MRM]
    CCOC --> J[Required state]
    MLTR --> J
    MRM --> J

    J --> CED[CED evidence licensing]
    D --> CED
    T --> CED

    CED --> RACH[RACH causal admissibility / next observation]
    RACH --> LV[Causal learning value]
    CED --> TL[Target licensing status]

    W --> DYN[Eco-genetic dynamics]
    DYN --> LS[Loss-generating state]
    LS --> WARN[Conditional warning]

    J --> OLD[Stored state under old contract]
    OLD --> REV[TU-1 contract revision]
    REV --> NEW[Revised required state]

    LV --> SEP[TU-2 learning/licensing firewall]
    TL --> SEP
```

## Start here

### 1. Theory Universe

- [`theory/README.md`](theory/README.md) — canonical theory-world statement.
- [`theory/core_universe.json`](theory/core_universe.json) — machine-readable type system.
- [`theory/CONSISTENCY_AUDIT.md`](theory/CONSISTENCY_AUDIT.md) — ownership and anti-collapse audit.
- [`theory/TU1_CONTRACT_REVISION.md`](theory/TU1_CONTRACT_REVISION.md) — TU-1: revision after compression.
- [`theory/tu1_registry.json`](theory/tu1_registry.json) — TU-1 claim ceiling.
- [`theory/contract_revision.py`](theory/contract_revision.py) and [`theory/verify_tu1.py`](theory/verify_tu1.py) — executable TU-1 construction.
- [`theory/TU2_LEARNING_LICENSING.md`](theory/TU2_LEARNING_LICENSING.md) — TU-2: causal learning versus target licensing.
- [`theory/tu2_registry.json`](theory/tu2_registry.json) — TU-2 claim ceiling.
- [`theory/learning_licensing.py`](theory/learning_licensing.py) and [`theory/verify_tu2.py`](theory/verify_tu2.py) — executable TU-2 construction.

### 2. Portfolio Registry

- [`universe/ARCHITECTURE.md`](universe/ARCHITECTURE.md) — wider repository architecture.
- [`universe/registry.json`](universe/registry.json) — machine-readable repository/claim registry.
- [`graphify-out/graph.html`](graphify-out/graph.html) — interactive Graphify map.
- [`universe/bridges/eco_genetic_crest_bridge_registry.json`](universe/bridges/eco_genetic_crest_bridge_registry.json) — bounded EcoGenetic -> CREST bridge.
- [`universe/PROVENANCE.json`](universe/PROVENANCE.json) — provenance manifest.

## Core theoretical ownership

| Layer | Primary owner |
|---|---|
| World / contract / least adequate state | `crest` |
| Future obstruction | `ccoc` |
| Historical-semantic transport / repair | `mltr` |
| Mechanism-robust state / law | `mrm` |
| Evidence / reportability | `ced` |
| Causal admissibility / next observation | `microdonta` / RACH |
| Eco-genetic dynamics / simulator-state boundary | `eco-genetic-criticality` |
| Loss-state recovery / conditional warning | `eco-genetic-warning-extensions` |
| Cross-repository type system | `theouni` |
| Contract revision after compression | `theouni` / TU-1 |
| Learning/licensing bridge firewall | `theouni` / TU-2 |

## Canonical distinctions

```text
Reality
!= ModelWorld
!= Snapshot
!= RequiredState
!= EvidenceClass
!= AdmissibleCausalSet
!= Report
```

and

```text
CompleteSimulatorState != Minimal/Natural RequiredState
WarningStatistic != LossGeneratingState
StoredStateRepresentation != RevisedRequiredState
CausalLearningValue != TargetLicensingStatus
```

unless an explicit theorem or typed bridge establishes the needed factorization.

The long-standing central distinction remains:

```text
required state != identified state != reportable target
```

TU-1 adds a temporal distinction:

```text
state adequate for contract C0
    does not imply
state revisable for later contract C1
```

TU-2 adds an objective distinction:

```text
more causal learning
    does not imply
more target licensing
```

and the converse also fails.

## TU-1 — contract revision after compression

TU-1 deliberately does **not** re-claim CREST-J1's common-lift closure result. CREST already proves that noncommuting refinement audits converge under fair iteration to one least joint state on a declared finite common carrier.

TU-1 starts after an old state has already been stored.

For old partition `P` and revised required partition `Q`:

- state-only revision succeeds iff every `P` block lies inside one `Q` block;
- otherwise the exact minimum auxiliary alphabet is the maximum number of `Q` blocks hidden inside any single `P` block;
- worst-case local revision debt can be arbitrarily large while global average partition-refinement debt is arbitrarily small.

The finite coding/factorization substrate is elementary and overlaps classical zero-error side-information ideas. No standalone information-theory novelty claim is made without further prior-art audit.

## TU-2 — causal learning versus target licensing

TU-2 embeds a RACH causal state `S` and a CED report target `T` in one finite product-world universe.

For experiments `Q_{k,b}` that reveal `k` causal bits and optionally reveal `T`:

```text
I(S; Q_{k,0}) = I(S; Q_{k,1}) = k
```

while target licensing is opposite:

```text
L_T(Q_{k,0}) = 0
L_T(Q_{k,1}) = 1
```

Hence the same causal-learning value can correspond to either no target license or complete target license. In the sharp endpoints, normalized RACH-style causal NOV can be maximal with zero target licensing, or zero with complete target licensing.

TU-2 is a bridge firewall, not a replacement for RACH or CED. Its noiseless construction does not inherit CED's failure/calibration/risk guarantees.

## Boundary to empirical ecology

Species, islands, floral polymorphisms, SDM methods, visit cameras, and other concrete research programmes enter only through typed projections such as

```text
empirical system
    -> model-world universe
    -> scientific contract
    -> observation/reliability map
    -> target
```

with explicit claim ceilings. Their role is to instantiate, test, falsify, or expose missing coordinates in the theory universe.

## Current mathematical frontier

The next theory results should strengthen cross-layer composition rather than add more relabelings.

1. **TU-1F — carrier-changing revision:** revision through replacement relations/common lifts and lift-invariance of revision debt.
2. **TU-2D — learning/licensing coincidence:** necessary and sufficient conditions under which RACH ranking and CED reliability-qualified target ranking agree.
3. **Representation-invariant loss state:** when different simulator representations induce the same loss-generating quotient.
4. **Warning portability:** when warning ordering transports across different loss-state spaces without assuming one universal numerical threshold.
5. **Empirical-state factorization:** when measured coordinates close a held-out future target rather than merely correlate with it.

## Validation

```text
python theory/validate_core.py
python theory/verify_tu1.py
python theory/verify_tu2.py

python scripts/build_curated_graph.py
python scripts/build_graph.py
python scripts/write_provenance_manifest.py
python scripts/validate_universe.py
```

The theory validators check the theory-first type firewall and finite theorem modules. The universe validators check the broader provenance-preserving repository registry and generated graph.
