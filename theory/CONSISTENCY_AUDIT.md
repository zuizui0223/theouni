# Theory Universe v0.5 — consistency and ownership audit

This audit covers only the theoretical core. Empirical species systems, island syndromes, SDM workflows, sensors, and field platforms remain outside the core until explicit typed projection contracts are defined.

The v0.5 core distinguishes eight questions:

1. **What model world is being represented?**
2. **What state is required by the scientific contract?**
3. **Can available evidence identify that state or at least license the requested target?**
4. **Which causal programmes remain admissible and what observation is valuable for causal learning?**
5. **If the contract changes later, can the revised state be recovered from what science previously retained?**
6. **Does a change in raw simulator representation preserve the target-relevant loss state?**
7. **Is the loss state sufficient for warning evaluation?**
8. **Does within-state warning behaviour transport across different states/domains?**

---

## 1. Canonical projection table

| Repository/module | Main input | Owned question | Main output | Forbidden upgrade |
|---|---|---|---|---|
| `crest` | model worlds + scientific contract | what is the least adequate state on a declared common carrier? | `RequiredState`, carrier/evidence gates | intrinsic natural state |
| `ccoc` | changed future grammar `Gamma` | can new futures expose a distinction hidden by an old merge? | future obstruction / interface lower bound | history theorem |
| `mltr` | source/target systems + replacement/history | can inherited macro meaning transport; if not, what repair/history is needed? | transported/repaired partition | empirically inferred history from declaration alone |
| `mrm` | candidate mechanisms `Theta` + actions | which mechanism differences alter required responses? | candidate-safe state / typed or set-valued law | mechanism truth |
| `ced` | experiment/failure contract `D` + target `T` | what distinctions/reports are evidentially licensed? | `EvidenceClass`, licensed `Report` | structural state adequacy |
| `microdonta` / RACH | causal programmes + observations | which causal programmes remain and what should be measured next for causal learning? | `AdmissibleCausalSet`, `NextObservation`, NOV | best-model winner or target license |
| `eco-genetic-criticality` | explicit simulator closure | what dynamics and complete-state sufficiency hold in the declared simulator? | `CompleteSimulatorState`, dynamic evidence | minimal/natural state |
| `eco-genetic-warning-extensions` | warning-blind frozen loss domain + endpoints | when does warning reproduce within a domain and where does portability fail empirically? | `WarningValidity`, partial-state tests, portability bounds | universal threshold or complete natural state |
| `theouni` / TU-1 | stored old state + revised required state | can a revised state be recovered after compression? | revisability criterion, idealized revision debt | physical irreversibility / empirical cost |
| `theouni` / TU-2 | causal state + target + candidate experiment | does causal-learning value imply target licensing? | exact orthogonality and policy-reversal witnesses | universal experiment ranking |
| `theouni` / TU-3 | representation projection + loss-response signature | does a representation preserve the loss-relevant quotient? | loss-faithful factorization / representation failure | natural-state minimality |
| `theouni` / TU-4 | loss response + warning response + cross-state correspondence | is loss state enough for warning, and does warning transport? | `WarningEvaluationState`, portability criterion | universal warning threshold / empirical portability |

---

## 2. State-type firewall

The following objects are not interchangeable:

```text
CREST RequiredState
!= CompleteSimulatorState
!= EvidenceClass
!= AdmissibleCausalSet
!= WarningStatistic
```

Target-specific state hierarchy:

```text
RequiredState(C)
   |
   +--> LossGeneratingState       [C specialized to loss response]
            |
            `--> WarningEvaluationState [joint loss + warning response]
```

with

```text
LossGeneratingState <= WarningEvaluationState
```

in the partition-refinement order. Equality requires warning response to factor through the loss-state quotient.

Likewise:

```text
StoredStateRepresentation != RevisedRequiredState
```

unless TU-1 factorization passes.

---

## 3. CREST-J1 versus TU-1

CREST-J1 begins while world-level distinctions remain available on a common lift and constructs the least partition satisfying the joint contract. Noncommuting audits can still converge under fair iteration.

TU-1 begins **after a previous compression has already been stored**.

For old partition `P` and revised required partition `Q`, state-only revision exists iff

\[
q_Q=f\circ q_P.
\]

When this fails, TU-1 gives the exact minimum finite auxiliary label needed in its same-carrier setting. TU-1 is therefore a revision-after-forgetting result, not another closure-commutation result.

---

## 4. RACH versus CED versus TU-2

RACH values reduction of uncertainty about a declared causal-programme object. CED values defensible target reporting under a reliability/failure/risk contract.

TU-2 shows that these utilities are not interchangeable even before observation failure is introduced.

On one finite product universe, equal-cost observations can have

```text
maximal normalized causal-learning value + zero target license
```

or

```text
zero causal-learning value + complete target license.
```

The correct chain is therefore

```text
causal-learning value
    != nominal target separation
    != reliability-qualified target licensing
```

A future coincidence theorem must state conditions under which these align; alignment is not the default.

---

## 5. Complete simulator state versus TU-3 loss state

A complete simulator state may be future-sufficient under its declared Markov closure. That says nothing by itself about minimality for a particular loss endpoint.

TU-3 defines a representation projection `pi` as loss-faithful exactly when the declared loss response factors through it:

\[
r_L=\bar r_L\circ\pi.
\]

Consequences:

- arbitrary nuisance coordinates can inflate raw simulator state without increasing the loss quotient;
- one hidden loss-relevant coordinate is sufficient to make a coarse projection invalid;
- representation equivalence is always target-qualified.

Thus

```text
more model detail != more loss-relevant ecological state
```

and

```text
CompleteSimulatorState != LossGeneratingState
```

unless an independent minimality/equality result is proved.

---

## 6. Loss state versus TU-4 warning state

The previous phrase

> warning is conditional on a loss-generating state

is retained only as an **ordering/conditioning rule**: the loss domain must be fixed warning-blind before warning performance is evaluated.

It is not an assertion that loss state automatically determines warning behaviour.

TU-4 defines warning-evaluation state from the joint response

\[
(r_L,r_G).
\]

Hence

\[
Q_{loss}\preceq Q_{warn}.
\]

Two worlds can share the same loss future while having different warning lead/tie/lag response. They then belong to the same loss state but different warning-evaluation states.

This protects the empirical warning programme from over-generalization: strict warning replication inside one frozen domain is compatible with bounded or failed portability across other domains.

---

## 7. Within-state reproducibility versus portability

`eco-genetic-warning-extensions` empirically separates:

```text
C2: loss process fixed warning-blind
 -> C3: warning tested within frozen domain
 -> C4: portability tested across separately calibrated domains
```

Theory Universe v0.5 mirrors this as:

```text
LossGeneratingState
 -> WarningEvaluationState
 -> within-state WarningValidity
 -> cross-state WarningPortability audit
```

Therefore:

```text
within-state replication != universal threshold != cross-state portability
```

No graph or theorem bridge may collapse these claims.

---

## 8. Evidence versus required state versus report

Let `J` be a required-state partition and `E` an evidence partition.

1. `E` resolves `J`: full state report licensed.
2. `E` does not resolve `J`, but target is constant on every relevant evidence class: target-only report licensed.
3. target varies inside an evidence class: ambiguity must be retained.

Evidence cannot manufacture a structural distinction absent from the contract.

TU-1 adds a time-indexed issue: old evidence may have licensed old state `P`, yet a later required state `Q` may not factor through the stored state representation.

TU-2 adds an objective-indexed issue: an observation can improve causal identification without improving the requested report, or vice versa.

---

## 9. Reality-to-model firewall

All current theorem modules operate on declared mathematical/model worlds.

Every empirical application must specify at least:

- empirical unit and time/cohort;
- observed and unobserved coordinates;
- candidate model-world universe/carrier;
- scientific contract and target;
- observation/reliability model;
- external/held-out adequacy criterion if state status is claimed;
- claim ceiling and known non-identifiabilities.

Without this bridge, theory may motivate an empirical question but does not establish an empirical ecological state.

---

## 10. Current non-contradiction result

The theory core is logically coherent if qualified types are respected.

The principal apparent conflicts are type collisions, not theorem contradictions:

- complete simulator state versus least adequate state;
- required state versus evidence class;
- mechanism-safe law versus admissible causal set;
- causal-learning value versus target-licensing status;
- stored state versus revised required state;
- raw representation complexity versus loss-state complexity;
- loss-generating state versus warning-evaluation state;
- within-state warning validity versus cross-state portability.

TU-1 through TU-4 turn the last four collisions into explicit finite firewalls rather than prose cautions.

---

## 11. Closed finite modules

Current closed finite modules/inputs include:

- CREST common-carrier least-state substrate;
- CCOC future obstruction;
- MLTR history transport/repair;
- MRM mechanism-safe state/law;
- CED evidence/reportability;
- RACH causal admissibility/NOV;
- TU-1A–E revision after compression;
- TU-2A–C plus policy reversal;
- TU-3A–D representation-faithful loss state;
- TU-4A–D warning-state refinement and finite portability criterion.

`theouni` does not transfer ownership of the source theorem programmes.

---

## 12. Remaining frontier

The next theoretical work should close cross-layer gaps rather than add another named module by default.

Priority open problems:

1. **Reality -> model adequacy** — formal conditions for empirical rather than merely mathematical adequacy.
2. **Beyond finite exact** — stochastic, continuous, approximate and delayed-observation extensions.
3. **Carrier-changing revision** — revision through replacement relations/common lifts and invariant revision cost.
4. **Learning/licensing coincidence** — necessary and sufficient conditions for causal-learning and risk-limited target rankings to agree.
5. **Empirical-state factorization** — when measured coordinates close a held-out future target and make origin/history/mechanism residual information redundant.
6. **Empirical warning-state identification** — when measurable natural coordinates identify enough of the warning-evaluation state to support portability claims.

The most direct bridge to the concrete biological portfolio is now **empirical-state factorization**.

---

## 13. Novelty firewall

TU-1 through TU-4 use finite factorization, quotient, coding, information, and response-equivalence constructions with substantial classical mathematical relatives.

Their present role is **Theory Universe infrastructure and cross-layer logical discipline**. Standalone mathematical novelty is not assumed.

A future primary `theouni` paper should require a stronger result that couples layers in a way not reducible to the existing source theories or elementary quotient/factorization machinery—most plausibly empirical-state factorization with a nontrivial generalization theorem, a carrier-changing revision result, or a reliability-aware learning/licensing coincidence theorem.
