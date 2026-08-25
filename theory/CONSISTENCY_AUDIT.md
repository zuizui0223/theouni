# Theory Universe v0.3 — consistency and ownership audit

This audit covers only the theoretical core. Empirical species systems, island syndromes, SDM workflows, and sensor platforms remain outside the core until explicit typed projection bridges are defined.

The theory universe now distinguishes four questions:

1. **What state is required by a scientific contract?**
2. **Can available evidence identify/report it?**
3. **If the contract changes later, can the revised state be recovered from what science previously retained?**
4. **What object is a proposed next observation valuable for learning or licensing?**

## 1. Canonical projection

| Repository/module | Main input | Owned question | Main output | Forbidden upgrade |
|---|---|---|---|---|
| `crest` | model worlds + full scientific contract | what is the least adequate state on a declared common carrier? | `RequiredState`, carrier/evidence gates | intrinsic natural state |
| `ccoc` | changed future grammar `Gamma` | can new futures expose a distinction hidden by an old merge? | future obstruction / interface lower bound | history theorem |
| `mltr` | source/target systems + replacement/history | can inherited macro meaning transport; if not, what repair/history is needed? | transported/repaired partition | empirically inferred history from declaration alone |
| `mrm` | candidate mechanisms `Theta` + actions | which mechanism differences alter required responses? | candidate-safe state / typed or set-valued law | mechanism truth |
| `ced` | experiment/failure contract `D` + target `T` | what distinctions/reports are evidentially licensed? | `EvidenceClass`, licensed `Report` | structural state adequacy |
| `microdonta` / RACH | causal programmes + observations | which causal programmes remain and what should be measured next for causal learning? | `AdmissibleCausalSet`, `NextObservation`, NOV | best-model winner or target license |
| `eco-genetic-criticality` | explicit simulator closure | what dynamics and complete-state sufficiency hold in the declared simulator? | `CompleteSimulatorState`, dynamic evidence | minimal/natural state |
| `eco-genetic-warning-extensions` | frozen loss process + endpoint | when does warning reproduce within a loss-generating state and where does portability fail? | `WarningValidity`, candidate empirical state tests | universal threshold |
| `theouni` / TU-1 | old stored state + revised required state | is revision possible after compression, and what exact auxiliary information is minimally required? | revisability criterion, revision debt | physical irreversibility or Shannon/sampling cost |
| `theouni` / TU-2 | RACH causal state + CED target + candidate experiment | does causal-learning value imply target-licensing value, or conversely? | exact orthogonality / policy-reversal witnesses | universal experiment ranking |

## 2. State-type firewall

```text
CREST RequiredState
!= eco-genetic CompleteSimulatorState
!= EvidenceClass
!= AdmissibleCausalSet
!= WarningStatistic
```

`LossGeneratingState` is a specialization of `RequiredState` only after a loss contract and adequate quotient have been declared.

Likewise:

```text
StoredStateRepresentation != RevisedRequiredState
```

unless TU-1 factorization passes.

## 3. CREST-J1 versus TU-1

CREST-J1 begins while world-level distinctions remain available on a common lift. It constructs the least partition satisfying the joint Future / History / Mechanism / Evidence-Target obligations. Noncommuting audits still converge under fair iteration.

TU-1 begins **after an earlier compression has already been stored**.

For old partition `P` and revised required partition `Q`, exact state-only revision exists iff

\[
q_Q=f\circ q_P,
\]

or equivalently every `P` block lies inside one `Q` block.

If that fails, the exact minimum auxiliary alphabet is

\[
K_{rev}(P\to Q)=\max_{B\in P}|\{C\in Q:B\cap C\neq\varnothing\}|.
\]

Thus TU-1 is not another closure-commutation theorem. It is a theorem about **revision after forgetting**.

## 4. Present compression versus future revisability

The old statement

> state = what science may safely forget for the current contract

is now qualified by

> an old scientifically safe forgetting can create a later revision obligation when the contract changes.

This does not imply that maximal detail should always be retained. It exposes a tradeoff between present compression and future revisability.

TU-1 further separates:

\[
D_{avg}
=
\log_2\left(\frac{1}{|P|}\sum_Br_B\right)
\]

from

\[
D_{rev}=\log_2\max_Br_B.
\]

The first is a global average split burden; the second is a worst-case local revision burden. TU-1 proves `D_avg <= D_rev` and an arbitrary divergence family.

## 5. RACH versus CED versus TU-2

RACH's validated observation score is causal-programme information reduction. CED's terminal criterion is whether evidence licenses the requested target under the declared experiment/reliability contract.

These are different estimands.

TU-2 makes the difference exact on one world universe

\[
\Omega=\{0,1\}^m\times\{0,1\},
\]

with causal state `S` and independent target `T`.

For

\[
Q_{k,b}=\text{first k causal bits, optionally plus T},
\]

both `b=0` and `b=1` give

\[
I(S;Q)=k,
\]

but target licensing is respectively 0 and 1.

Therefore:

```text
same causal-learning value
    can imply
no target license OR complete target license
```

and the sharp endpoints are

```text
maximal causal NOV + zero target license
zero causal NOV + complete target license
```

for equal-cost witness experiments.

## 6. TU-2 does not replace CED failure theory

TU-2 uses noiseless exact records to isolate semantic orthogonality.

CED adds another independent requirement: a nominal target split must be trustworthy under detection, calibration, dependence, reset, risk, and cost assumptions.

The correct chain is therefore

```text
causal-learning value
    != nominal target separation
    != reliability-qualified target licensing
```

A future coincidence theorem must state conditions for all three to align; they are not aligned by default.

## 7. MRM / RACH / CED remain different

- **MRM:** given candidate mechanisms, determine response-relevant mechanism equivalence and a mechanism-safe law/report.
- **RACH:** given data/model family, retain admissible causal programmes and value observations for reducing causal ambiguity.
- **CED:** given evidence/failure/target contract, determine what reports are licensed and which experiment meets a risk/cost objective.

A candidate bridge can use

```text
RACH -> MRM -> CED
```

but the bridge must not identify the three estimands.

## 8. Required state versus evidence versus report

Let `J` be a required-state partition and `E` an evidence partition.

1. `E` resolves `J`: full state report licensed.
2. `E` does not resolve `J`, but target is constant within each evidence class: target-only report licensed.
3. target varies within an evidence class: ambiguity must be retained.

Evidence cannot create a structural distinction that the contract did not require.

TU-1 adds a time-indexed issue: even if old evidence once licensed old state `P`, a later required `Q` may not factor through the stored representation.

TU-2 adds an objective-indexed issue: an observation can improve causal identification without improving the requested report, or vice versa.

## 9. Simulator sufficiency and loss state

`eco-genetic-criticality` may prove one explicit simulator state future-sufficient under its Markov closure. CREST may seek a coarser required quotient for a declared target. These are compatible because sufficient does not imply minimal.

For warning, the order remains:

```text
loss endpoint L
   -> loss contract C_L
   -> RequiredState / LossGeneratingState S_L
   -> within-state warning test
   -> portability test across separately calibrated states
```

A warning statistic cannot be upgraded to a universal state.

## 10. Reality-to-model firewall

All finite theory modules operate on declared model worlds. Every empirical application must specify at least:

- empirical unit and time/cohort;
- observed and unobserved coordinates;
- model-world universe/carrier;
- scientific contract and target;
- observation/reliability model;
- claim ceiling and known non-identifiabilities.

Without this bridge, a theorem can motivate an empirical question but does not establish an empirical ecological state.

## 11. Current non-contradiction result

The theory core remains logically coherent if qualified types are respected.

The main apparent conflicts are type collisions rather than theorem contradictions:

- complete simulator state versus least adequate state;
- required state versus evidence class;
- mechanism-safe law versus admissible causal set;
- causal-learning value versus target-licensing status;
- warning statistic versus loss-generating state;
- old stored state versus revised required state.

The last two cross-program collisions are now formal theorem modules rather than prose warnings.

## 12. Theorem frontier

### Closed finite modules

- CREST-J1: common-lift least state;
- CCOC: future obstruction;
- MLTR: history transport/repair;
- MRM: mechanism-safe state/law;
- CED: evidence/reportability;
- RACH: causal admissibility/NOV;
- TU-1A–E: same-carrier revision after compression;
- TU-2A–C: causal-learning/target-licensing orthogonality and policy reversal.

### Next targets

1. **TU-1F:** carrier-changing revision through replacement relations/common lifts; test lift-invariance of revision debt.
2. **TU-2D:** necessary/sufficient coincidence conditions for RACH ranking and CED reliability-qualified target ranking.
3. **Loss-state representation theorem:** when different simulator representations induce the same loss-generating quotient.
4. **Warning portability theorem:** weakest map that transports warning ordering without a universal threshold.
5. **Empirical-state factorization:** out-of-sample criterion for when measured coordinates actually close a future target.

## 13. Novelty firewall

TU-1 factorization/side-information and TU-2 product-information constructions use elementary mathematical substrates and overlap broad prior art in quotient theory, zero-error side-information coding, information theory, decision-relevant experiment design, and active learning.

Their current status is therefore **theory-universe infrastructure**, not automatically publication-level mathematical novelty.

A future `theouni` primary theory paper should require a stronger cross-layer result such as TU-1F, TU-2D, representation-invariant loss state, or warning portability rather than relying on elementary bridge firewalls alone.
