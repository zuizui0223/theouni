# Theory Universe v0.1 — repository consistency audit

This audit projects only the current **theoretical core repositories** into the v0.1 type system. It deliberately excludes empirical species systems, island syndromes, SDM workflows, and sensor platforms.

The purpose is to prevent a common failure mode: two repositories use similar words (`state`, `law`, `observation`, `warning`) for mathematically different objects, and a synthesis silently equates them.

## 1. Canonical projection table

| Repository | Input types | Owned transformation / theorem family | Output types | Forbidden upgrade |
|---|---|---|---|---|
| `crest` | `ModelWorldUniverse`, `ScientificContract` | contract-relative adequacy / least-information quotient on declared finite carrier | `RequiredState`, monitoring debt, reportability conditions | `RequiredState = natural intrinsic state` |
| `ccoc` | worlds/interfaces + changed `Gamma` | open-future/composition obstruction and memory lower bound | refined future-sufficient interface / witness of old merge failure | `future obstruction = history repair` |
| `mltr` | source/target world systems + declared replacement relation + `H` | transport, coarsest repair, transport defect, history augmentation | transported/repaired state partition | `declared relation = empirically inferred lineage history` |
| `mrm` | visible state + retained candidate mechanisms `Theta` + actions | response-type agreement, candidate-safe quotient, typed/set-valued law | mechanism-robust `RequiredState` refinement / `Report` | `candidate family = inferred mechanism truth` |
| `ced` | latent worlds + experiment/observation/failure contract `D` + target `T` | evidence quotient, target-safe refinement, reliability/risk-limited licensing | `EvidenceClass`, licensed `Report` | `evidence resolution = structural state adequacy` |
| `microdonta` / RACH | declared causal programmes + constraints + observation map + observed record | causal admissibility, replaceability/degeneracy, NOV/RACH-SEQ | `AdmissibleCausalSet`, `NextObservation` | `admissible set = best model` |
| `eco-genetic-criticality` | explicit simulator closure + forcing/stochastic law | mechanistic dynamics, complete-state sufficiency, coarse-summary counterexample | `CompleteSimulatorState`, dynamic endpoint evidence | `CompleteSimulatorState = minimal/natural RequiredState` |
| `eco-genetic-warning-extensions` | frozen loss-generating closure + endpoint + candidate empirical coordinates | condition recovery, within-state warning replication, portability boundaries | `LossGeneratingState` candidate, `WarningValidity`, empirical state tests | `warning statistic = universal warning state` |
| `theouni` | typed outputs of all above | type registry, bridge contracts, claim ceilings, cross-program consistency | cross-repository ontology only | `registry edge = theorem/evidence` |

## 2. The state-name collision

The following objects must remain distinct even when repositories locally call them a `state`:

```text
CREST RequiredState
!= eco-genetic CompleteSimulatorState
!= eco-genetic empirical candidate / partial state
!= EvidenceClass
!= AdmissibleCausalSet
!= LossGeneratingState unless explicitly constructed as a RequiredState for a loss contract
```

### Resolution rule

Cross-repository prose must use qualified names. Unqualified `state` is allowed only inside a repository-local derivation where its type is already fixed.

## 3. CREST versus eco-genetic state sufficiency

### Compatible claims

`eco-genetic-criticality` can prove that a complete explicit simulator state is future-sufficient under a declared Markov closure.

CREST can then ask a different question:

> On a declared carrier and target, what is the coarsest quotient that remains adequate?

These claims are compatible because **sufficient** does not imply **minimal**.

### Required bridge shape

```text
CompleteSimulatorState records
       |
       | opaque source records + future-response signatures
       v
CREST finite carrier
       |
       v
RequiredState quotient for declared target
```

### Prohibited inference

```text
complete simulator state
=> natural ecological state
```

is invalid without an independent empirical/model adequacy argument.

## 4. CCOC versus MLTR

Both use partition/refinement mathematics, but the quantifiers differ.

### CCOC

The same present/closed interface is tested after **future grammar expansion**.

```text
fixed carrier or interface setting
+ larger Gamma
-> old merge may fail
```

### MLTR

A source system is mapped into a **replacement target system**, potentially with a different state space.

```text
source carrier
+ replacement relation / history H
-> transported label may fail
-> minimal repair/history augmentation
```

### Firewall

A future action becoming legal is not by itself a replacement history. A replacement relation is not by itself an open-composition lower-bound construction.

## 5. MRM versus RACH versus CED

These three repositories all discuss observations or experiments, but they optimize different objects.

### MRM: response disagreement

Given a candidate mechanism family, MRM asks:

> Which mechanism distinctions must remain because they alter declared responses?

Output: response types, candidate-safe quotient, deterministic/typed/set-valued law, discrimination plan conditional on the candidate family.

### RACH: causal admissibility

Given data, constraints, and a model family, RACH asks:

> Which causal programmes remain compatible, and what feasible observation is expected to reduce that ambiguity?

Output: `AdmissibleCausalSet` and `NextObservation`.

### CED: licensed resolution

Given an observation/failure/calibration architecture and target, CED asks:

> Does the experiment actually justify a deterministic report, and at what risk/cost?

Output: `EvidenceClass` and licensed `Report`.

### Correct compositional order

A candidate future bridge should have the shape

```text
RACH AdmissibleCausalSet
        |
        v
MRM response-type partition / mechanism-safe report
        |
        v
candidate discriminating observations
        |
        v
CED reliability/failure/risk contract
        |
        v
licensed observation/report plan
```

But this is **not yet a composition theorem**. In particular:

- high RACH information gain need not imply high CED licensed-resolution probability;
- an MRM discrimination action need not be reliable under the actual failure architecture;
- CED can license a target report without identifying the full MRM response type;
- RACH can retain multiple causal programmes even when the requested target is already CED-reportable.

These divergences are research targets rather than contradictions.

## 6. Required state versus evidence class

Let `J` denote a required-state partition and `E` an evidence partition.

The conceptual direction is:

```text
world differences
   |
   | contract adequacy
   v
RequiredState J

observation records
   |
   | compatibility / reliability
   v
EvidenceClass E
```

Evidence does not refine nature by decree. It may or may not resolve the distinctions already required by `J`.

Three cases must remain distinct:

1. `E` identifies `J`: full state report licensed.
2. `E` does not identify `J`, but target is constant on `E`: target-only report licensed.
3. target varies within `E`: ambiguity must be retained.

This is the central reason `required state != identified state != reportable target` is a theorem architecture rather than a slogan.

## 7. Loss-generating state and warning

A `LossGeneratingState` is valid only after a loss target `L` and its future contract are fixed.

The desired theoretical construction is

```text
loss endpoint L
     |
     v
loss contract C_L
     |
     v
RequiredState S_L = Omega / ~_{C_L}
     |
     v
within-state warning test
```

The current eco-genetic programme supplies a simulator-specific frozen loss-generating closure and conditional warning evidence. It does not yet prove a representation-invariant minimal `S_L` across arbitrary models.

### Prohibited inference

A statistic such as diversity, F_ST, connectivity, or any other coordinate cannot become a universal warning state merely because it precedes one loss endpoint in one calibrated domain.

## 8. Reality-to-model firewall

All finite theorem repositories operate inside a declared mathematical/model universe.

Therefore every empirical application must introduce an explicit bridge:

```text
Reality
  |
  | measurement + model assumptions + calibration
  v
compatible ModelWorld set
```

This bridge must state at least:

- empirical unit;
- time/cohort;
- observed coordinates;
- unobserved coordinates;
- model-world carrier/universe;
- target;
- observation/reliability model;
- claim ceiling;
- known non-identifiabilities.

Without this bridge, a mathematical theorem may motivate an empirical question but does not establish an empirical state.

## 9. Current non-contradiction result

At Theory Universe v0.1, the eight theory repositories can be placed in one universe **without a logical contradiction**, provided the type firewall is respected.

The apparent conflicts are type collisions rather than contradictory theorems:

- detailed simulator state versus least adequate state;
- required state versus identified evidence class;
- mechanism-safe law versus admissible causal set;
- predicted information gain versus licensed resolution;
- warning statistic versus loss-generating state.

No theorem currently requires these pairs to be identical.

## 10. The first genuinely new cross-repository mathematics to pursue

The strongest next step is not another repository relabeling. It is to prove one or more **composition results**.

### TU-1 Contract-composition theorem

Given refinement operators for `Gamma`, `H`, `Theta`, and `D/T`, characterize conditions under which

\[
C_\Gamma\vee C_H\vee C_\Theta\vee C_{D,T}
\]

is independent of application order, and characterize failure when operators depend on carrier changes or one another.

### TU-2 Learning-versus-licensing divergence

Construct a finite family in which a next observation has arbitrarily large reduction in RACH causal ambiguity but zero gain in CED licensed target resolution, and a converse family where a low-information observation licenses the target without identifying causal programme.

### TU-3 Loss-state representation theorem

Define when two different simulator representations induce the same loss-generating quotient for a declared endpoint, separating representation invariance from complete-state identity.

### TU-4 Empirical-state factorization criterion

For an empirical coordinate map `Z`, define state adequacy for target horizon `H` by held-out factorization:

\[
P(T_{t+H}\mid \omega_t)
=
P(T_{t+H}\mid Z_t)
\]

within a declared model/observation class, with explicit failure when origin/history/mechanism retains residual predictive information.

### TU-5 Warning portability theorem

Characterize the weakest map between two loss-generating state spaces under which a warning ordering can transport without assuming one universal numerical threshold.

These are the candidate mathematical spine of a future `theouni` primary theory paper. Until such results exist, `theouni` remains the type/bridge owner rather than the owner of the source theorems.
