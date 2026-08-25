# Theory Universe v0.2 — consistency and ownership audit

This audit covers only the theoretical core. Empirical species systems, island syndromes, SDM workflows, and sensor platforms remain outside the core until explicit typed projection bridges are defined.

The purpose is to distinguish three different questions that are easy to collapse:

1. **What state is required by a scientific contract?**
2. **Can available evidence identify/report it?**
3. **If the contract later changes, can the new state be recovered from what science previously chose to retain?**

The third question is now owned by TU-1.

## 1. Canonical projection

| Repository | Main input | Owned question | Main output | Forbidden upgrade |
|---|---|---|---|---|
| `crest` | model worlds + full scientific contract | what is the least adequate state on a declared common carrier? | `RequiredState`, carrier/evidence gates | intrinsic natural state |
| `ccoc` | changed future grammar `Gamma` | can new futures expose a distinction hidden by an old merge? | future obstruction / interface lower bound | history theorem |
| `mltr` | source/target systems + replacement/history | can inherited macro meaning transport; if not, what repair/history is needed? | transported/repaired partition | empirically inferred history from declaration alone |
| `mrm` | candidate mechanisms `Theta` + actions | which mechanism differences alter required responses? | candidate-safe state / typed or set-valued law | mechanism truth |
| `ced` | experiment/failure contract `D` + target `T` | what distinctions/reports are evidentially licensed? | `EvidenceClass`, licensed `Report` | structural state adequacy |
| `microdonta` / RACH | causal programmes + observations | which causal programmes remain and what should be measured next? | `AdmissibleCausalSet`, `NextObservation` | best-model winner |
| `eco-genetic-criticality` | explicit simulator closure | what dynamics and complete-state sufficiency hold in the declared simulator? | `CompleteSimulatorState`, dynamic evidence | minimal/natural state |
| `eco-genetic-warning-extensions` | frozen loss process + endpoint | when does warning reproduce within a loss-generating state and where does portability fail? | `WarningValidity`, candidate empirical state tests | universal threshold |
| `theouni` / TU-1 | old stored state + revised required state | is revision possible after compression, and what exact auxiliary information is minimally required? | revisability criterion, revision debt | physical irreversibility or Shannon/sampling cost |

## 2. The old state-name collision remains forbidden

```text
CREST RequiredState
!= eco-genetic CompleteSimulatorState
!= EvidenceClass
!= AdmissibleCausalSet
!= WarningStatistic
```

`LossGeneratingState` may be treated as a specialized `RequiredState` only after a loss contract and adequate quotient have actually been declared.

New in v0.2:

```text
StoredStateRepresentation
!= RevisedRequiredState
```

unless the TU-1 factorization criterion passes.

## 3. CREST-J1 versus TU-1

This is the most important new firewall.

### CREST-J1

Input: the relevant world-level distinctions remain available on one common finite lift.

Question:

> What is the unique coarsest partition satisfying the joint Future / History / Mechanism / Evidence-Target obligations?

Result: a least common fixed point exists under the declared closure assumptions. Pairwise audit commutation is unnecessary; fair repeated iteration is order-independent at convergence.

### TU-1

Input: science has **already stored** an old state partition `P`, while a revised/joint world-level analysis now requires partition `Q`.

Question:

> Can `Q` be recovered from the old state label alone?

Result:

\[
q_Q=f\circ q_P
\]

iff every `P` block lies inside one `Q` block.

If not, the exact minimum reusable auxiliary alphabet is

\[
K_{rev}(P\to Q)=\max_{B\in P}|\{C\in Q:B\cap C\neq\varnothing\}|.
\]

Therefore TU-1 is **not another closure-commutation theorem**. It is a theorem about revision after an earlier compression has already erased world distinctions.

## 4. What TU-1 adds to the worldview

The old slogan was:

> state = what science may safely forget for the current contract.

The v0.2 correction is:

> state = what science may safely forget for the current contract, **with an explicit future cost if later contracts require distinctions that were discarded**.

This does not make one richer state universally preferable. It exposes a tradeoff between present compression and future revisability.

### Exact finite debt

For old block `B`, let `r_B` be the number of revised-state blocks hidden inside it. Then:

- state-only revision succeeds iff `max r_B = 1`;
- minimum auxiliary alphabet = `max r_B`;
- idealized worst-case revision debt = `log2(max r_B)`.

The global average refinement debt is

\[
D_{avg}=\log_2\left(\frac{1}{|P|}\sum_Br_B\right),
\]

and TU-1 proves

\[
D_{avg}\le D_{rev}.
\]

For any `m` and any positive `epsilon`, a finite example can have `m` bits of worst-case revision debt but `D_avg < epsilon`.

So rare states can carry large hidden revisability burdens even when a global partition-count summary barely changes.

## 5. CCOC / MLTR / MRM / CED versus TU-1

These programmes can be **sources of a revised required partition** but are not replaced by TU-1.

```text
CCOC / MLTR / MRM / CED
        |
        | changed scientific responsibility
        v
full-world revised required partition Q
        |
        v
TU-1
        |
        +-- old P already factors Q -> recode old state
        |
        `-- old P erased needed distinctions -> auxiliary information / reopen world description
```

TU-1 therefore sits after structural/evidential state construction, not before it.

## 6. MRM / RACH / CED remain different

### MRM
Given retained mechanisms, determine response-relevant equivalence and a mechanism-safe law/report.

### RACH
Given observations and a causal model family, retain compatible causal programmes and choose observations expected to reduce ambiguity.

### CED
Given failure/calibration/risk architecture, determine which state/target reports are actually licensed.

A future bridge may use

```text
RACH -> MRM -> CED
```

but no theorem currently equates:

- RACH information gain with CED licensed-resolution probability;
- MRM discriminability with sensor reliability;
- full mechanism identification with target reportability.

This remains the next major cross-layer mathematical target.

## 7. Required state versus evidence versus report

Let `J` be a required-state partition and `E` an evidence partition.

The three canonical cases remain:

1. `E` resolves `J`: full state report licensed;
2. `E` does not resolve `J`, but target is constant within each evidence class: target-only report licensed;
3. target varies within an evidence class: ambiguity must be retained.

Evidence cannot create a structural distinction that the contract did not require.

TU-1 adds a separate time-indexed issue: even if old evidence once licensed old state `P`, a later required `Q` may not factor through what was retained from that old scientific episode.

## 8. Simulator sufficiency and loss state

`eco-genetic-criticality` may prove one explicit simulator state future-sufficient under its Markov closure. CREST may then seek a coarser required quotient for a declared target. These are compatible because sufficient does not imply minimal.

For warning, the desired order remains:

```text
loss endpoint L
   -> loss contract C_L
   -> RequiredState / LossGeneratingState S_L
   -> within-state warning test
   -> portability test across separately calibrated states
```

A warning statistic cannot be upgraded to a universal state.

## 9. Reality-to-model firewall

All finite theory modules operate on declared model worlds. Every empirical application must specify at least:

- empirical unit and time/cohort;
- observed and unobserved coordinates;
- model-world universe/carrier;
- scientific contract and target;
- observation/reliability model;
- claim ceiling and known non-identifiabilities.

Without this bridge, a theorem can motivate an empirical question but does not establish an empirical ecological state.

## 10. Current non-contradiction result

The theory core remains logically coherent if qualified types are respected.

The principal apparent conflicts are type collisions rather than theorem contradictions:

- complete simulator state versus least adequate state;
- required state versus evidence class;
- mechanism-safe law versus admissible causal set;
- information gain versus licensed resolution;
- warning statistic versus loss-generating state;
- old stored state versus revised required state.

The last collision is now formalized rather than left as prose.

## 11. Current theorem frontier

### Closed enough to retain

- finite common-lift least state: CREST-J1;
- future obstruction: CCOC;
- history transport/repair: MLTR;
- mechanism-safe state/law: MRM;
- evidence/reportability: CED;
- causal admissibility/next observation: RACH;
- finite same-carrier revision after compression: TU-1A–E.

### Next theory targets

1. **Carrier-changing TU-1F:** revision through replacement relations/common lifts; test lift-invariance of revision debt.
2. **TU-2 learning-versus-licensing:** exact divergence/coincidence between RACH ambiguity reduction and CED licensed resolution.
3. **Loss-state representation theorem:** conditions under which different simulator representations induce the same loss-generating quotient.
4. **Warning portability theorem:** weakest state-space map that transports an ordering without assuming one universal threshold.
5. **Empirical-state factorization:** out-of-sample criterion for when measured coordinates actually close a future target.

## 12. Novelty firewall

TU-1A is elementary quotient factorization. TU-1B is closely related to finite zero-error coding/side-information partition problems. The programme must therefore not claim that these elementary substrates are new.

The potentially distinctive contribution is the ecological theory built from their conjunction with contract-relative state:

- scientific forgetting is formalized as quotienting;
- later responsibility changes are separated from initial joint-state construction;
- exact revisability is tested after compression;
- worst-case local revision burden is distinguished from global average refinement burden;
- rare-state divergence is made explicit.

A dedicated prior-art audit is still required before treating this conjunction as a publication-level novelty claim.
