# Theory Universe Worldline Atlas

> **Status:** meta-architecture only. This document reorganizes existing source-owned results; it does not transfer theorem ownership to `theouni`, create a new ecological state theorem, or upgrade open bridges to established ones.

## 1. Why a second Graphify view is needed

The portfolio-level Graphify graph is useful for provenance and repository navigation, but its broad `Definability and Shared Ontology` community is intentionally heterogeneous and many degree-one claim/evidence leaves are provenance terminals. That makes the full graph a poor surface for answering a different question:

> **How can the same ecological reality support several scientifically valid worldlines without requiring one privileged chapter order or one privileged state?**

The Worldline Atlas is therefore a focused overlay on top of the existing portfolio graph.

It keeps two structures separate:

1. **portfolio graph** — repositories, claims, evidence, ownership, bridges, and provenance;
2. **worldline graph** — task-indexed scientific perspectives, their invariants, intersections, termination modes, and failure modes.

The first answers *where a result comes from*. The second answers *how results coexist in one theory universe*.

Machine-readable source: [`worldline_atlas.json`](worldline_atlas.json).

---

## 2. Origin of a scientific worldline

The common origin is ecological reality, not a state label.

```text
Ecological Reality
    -> declared measurement/model bridge
ModelWorld universe
    -> scientific task / contract
contract-complete response signature
    -> equivalence relation
Task-indexed scientific state
```

Schematically, for task `alpha`,

\[
\Sigma_\alpha:\Omega_\alpha\to Y_\alpha,
\qquad
\omega\sim_\alpha\omega'
\iff
\Sigma_\alpha(\omega)=\Sigma_\alpha(\omega'),
\]

and the resulting state is

\[
Q_\alpha=\Omega_\alpha/\!\sim_\alpha.
\]

A worldline therefore begins when a scientific responsibility specifies which differences among possible model worlds must affect the answer.

This is not a claim that the task creates ecological reality. Reality constrains the allowed model worlds and responses; the task determines which of those real/modelled distinctions the scientific representation is responsible for preserving.

---

## 3. Universe-wide invariants

These are the rules intended to survive every worldline.

1. **Reality is not ModelWorld.** A theorem on declared model worlds is not automatically a theorem about nature.
2. **State is task-indexed.** No unqualified repository-local `state` becomes the intrinsic state of nature.
3. **Safe merging requires response preservation.** A merge is licensed only while the task-required response factors through what is retained.
4. **Evidence does not create structural distinctions.** Evidence identifies or licenses; it does not create the distinction the task requires.
5. **Required state, identified state, and reportable target remain distinct.**
6. **No bridge is not a contradiction.** Cross-worldline transport is not licensed merely because no conflict is known.
7. **Validity here does not imply portability elsewhere.** Reuse requires a factorization, lift, replacement map, evidence projection, causal-response map, or portability correspondence as appropriate.

These invariants are the closest thing in `theouni` to universe-wide laws. The objects visible inside a particular worldline may change; these type/transport rules do not.

---

## 4. Nine task-indexed worldlines

| Worldline | Source owner(s) | Main question | Perspective-specific output | Forbidden inference |
|---|---|---|---|---|
| **Capability / Required-State** | CREST | what happens to required state/monitoring when management capability changes? | capability-resolution gap; monitoring debt | small capability gain `=>` small epistemic burden |
| **Future / Open Grammar** | CCOC | does a small exact closed interface remain small after opening the future grammar? | interface inflation | simple closed interfaces `=>` simple open interface |
| **History / Replacement** | MLTR | can an inherited macro-law survive replacement; if not, what repair/history is required? | transport defect; history-mode debt | valid source law `=>` valid target law |
| **Mechanism / Response Type** | MRM | which hidden mechanism differences change required intervention responses? | mechanism-safe state / typed law | same visible state `=>` same deterministic law |
| **Evidence / Licensing** | CED | what distinction or target is honestly licensed by the experiment/failure/risk contract? | EvidenceClass; licensed report | more information `=>` licensed target |
| **Causal Learning / Next Observation** | RACH + TU-2 firewall | which causal programmes remain and what should be measured next? | admissible causal set; NOV | pattern fit or high NOV `=>` cause/target identified |
| **Revision / After Compression** | TU-1 | can a later required state be recovered after an earlier scientific compression was stored? | revision status; revision debt | adequate now `=>` revisable later |
| **Loss / Dynamic State** | eco-genetic-criticality + TU-3 | what representation is sufficient for the declared loss response? | LossGeneratingState; representation faithfulness | raw detail/coarse marginals `=>` correct loss state |
| **Warning / Portability** | eco-genetic-warning-extensions + TU-4 | after loss is fixed warning-blind, what warning state is required and does it transport? | WarningEvaluationState; portability status | signal leads loss `=>` valid/portable warning |

The rows are not nine rival definitions of ecological state. They are nine task-indexed cuts through a common typed universe.

---

## 5. Intersections: where worldlines actually meet

### 5.1 Required-State Junction

```text
Capability
Future ---------> joint RequiredState
History --------> on a common carrier/lift
Mechanism ------>
```

CCOC, MLTR, and MRM supply different structural reasons that an old merge may fail. CREST can combine compatible obligations on a declared common carrier or faithful lift. This composition does not transfer the source theorem ownership.

### 5.2 Knowledge Junction

```text
RequiredState
     |
     +--> CED: what is licensed?
     |
     `--> RACH: what causal possibilities remain and what should be learned next?
```

The central firewall is

\[
\text{required distinctions}
\neq
\text{evidential identification}
\neq
\text{causal-learning value}
\neq
\text{reportability}.
\]

TU-2 exists to prevent causal-learning utility from silently replacing CED target licensing.

### 5.3 Revision Junction

A revision worldline exists only after a scientific representation has actually been retained.

```text
old task -> stored state P
new/revised task -> required state Q
                   |
                   `-> TU-1: does Q factor through P?
```

The trigger for `Q` may originate from Future, History, Mechanism, Evidence/Target, or another changed responsibility.

### 5.4 Loss-Warning Junction

Loss and warning are not parallel interchangeable states.

\[
Q_L\preceq Q_W.
\]

Warning evaluation includes the loss responsibility and may require additional distinctions. Equality requires warning response to factor through the loss quotient. Portability requires a further cross-domain correspondence/commutation condition.

### 5.5 Reality-to-Theory Junction

Every worldline returns to the same unresolved outer boundary:

```text
real system
 -> empirical unit/time/cohort
 -> observation/reliability contract
 -> model-world support
 -> task/target
 -> held-out/external adequacy criterion
 -> bounded claim
```

Without this admission bridge, source theorems remain statements about declared model worlds.

---

## 6. No bridge is not a contradiction

The pairwise v0.6 contradiction certificate audits 12 modules and all 66 unordered pairs. At the current claim ceilings it registers `actual-conflict = 0`, but most pairs are not unconditional identities or automatic compositions.

The registered relation types are deliberately different:

- `compatible` — already co-satisfiable in matched scope;
- `conditional-on-common-carrier-or-map` — composition needs an explicit carrier/lift/map;
- `orthogonal-estimand` — different typed objects are being estimated;
- `open-bridge` — no contradiction is identified, but useful composition remains unproved;
- `actual-conflict` — jointly unsatisfiable after types/scope/estimand are matched.

Therefore:

\[
\boxed{
\text{not transportable}
\neq
\text{contradictory}.
}
\]

The atlas does not promote the pairwise audit into a global consistency theorem. The current triadic screen covers all 220 triples only as a pair-profile triage; two triples have bounded executable shared-carrier witnesses and 218 do not.

---

## 7. Termination is not the same as failure

A scientific worldline can close in several legitimate ways.

### Resolved

The task-relevant distinctions are represented and, where needed, identified.

### Licensed ignorance

The full state is unresolved, but the requested target is constant across the relevant evidence class and can be reported honestly.

### Honest ambiguity

The target varies across compatible worlds, so the sharp result remains set-valued or explicitly unresolved.

### Bounded non-portability

The result is valid inside the declared task/domain, while a transport test fails or remains unsupported elsewhere.

### Open worldline

A bridge, model-adequacy condition, observation contract, or contract-complete response definition remains incomplete. Keeping the worldline open is not a contradiction.

---

## 8. Genuine universe failure modes

The atlas reserves `failure` for breakdowns stronger than ordinary non-portability or uncertainty.

1. **Carrier collapse.** The joint obligations have no adequate common carrier/coverage; state refinement cannot repair the world-set problem.
2. **Ill-posed task.** The task/signature is post-hoc, vacuous, non-testable, or otherwise fails the declared responsibility criteria.
3. **Representation failure.** The required response does not factor through what was retained.
4. **Reality-to-model failure.** Internal theorem validity is correct, but the declared ModelWorld universe has not earned adequacy for the empirical system/target.
5. **Higher-order consistency failure.** Pairwise compatibility does not guarantee a jointly satisfiable multi-module carrier or map. This remains an open global risk outside the bounded witnesses.

This distinction prevents `theouni` from explaining every failure by saying only that a different worldline was chosen.

---

## 9. What is invariant and what is perspective-specific?

### Visible across all worldlines

- Reality/ModelWorld separation;
- task indexing;
- response-preserving factorization requirement;
- evidence/structure separation;
- required/identified/reportable separation;
- explicit bridge requirement;
- nonautomatic portability.

### Visible only from particular perspectives

- **Capability:** capability-resolution divergence, monitoring debt;
- **Future:** closed-to-open interface inflation;
- **History:** transport defect and minimal history augmentation;
- **Mechanism:** response-type ambiguity frontier;
- **Evidence:** identification gap and failure-domain guarantee ceiling;
- **Learning:** admissible causal set and next-observation value;
- **Revision:** revision debt and worst local hidden split;
- **Loss:** loss-state complexity and representation faithfulness;
- **Warning:** warning refinement, discrimination, and portability.

A distinction can therefore be scientifically indispensable in one worldline and safely forgotten in another without any physical contradiction. What changes is its representational relevance to the task.

---

## 10. Chapter order is not theory identity

The source theorem DAG contains scientific dependencies, but it does not impose one privileged narrative sequence.

Only hard scientific dependencies must be respected. The clearest current example is:

```text
Loss responsibility
    -> Warning responsibility
```

because warning claims require loss to have been fixed warning-blind. Other major worldlines are often incomparable perspectives or orthogonal estimands.

Consequently many chapter orders are compatible with the same universe. Four examples retained in the machine-readable atlas are:

1. **state-first** — Capability -> Future -> History -> Mechanism -> Evidence -> Learning -> Revision -> Loss -> Warning;
2. **intervention-first** — Capability -> Mechanism -> Future -> History -> Revision -> Evidence -> Learning -> Loss -> Warning;
3. **knowledge-first** — Evidence -> Learning -> Capability -> Future -> History -> Mechanism -> Revision -> Loss -> Warning;
4. **dynamics-first** — Loss -> Warning -> Capability -> Future -> History -> Mechanism -> Evidence -> Learning -> Revision.

A chapter may also appear earlier than a source dependency for narrative reasons if it locally imports/restates the prerequisite; the theorem dependency itself is not reversed by presentation.

Hence:

> **The theory has a dependency structure, but no privileged narrative order.**

A dissertation chapter sequence is one traversal of the atlas, not the definition of the universe.

---

## 11. Graphify organization rule

The full portfolio graph should continue to own repository provenance, evidence leaves, source claims, and concrete-project bridges.

The Worldline Atlas should own only:

- scientific worldlines;
- universe-wide invariants;
- worldline-specific observables;
- intersections;
- bridge types;
- termination modes;
- failure modes;
- hard scientific dependencies;
- presentation-order examples.

Do **not** move source theorem nodes, source evidence, or repository ownership into this overlay.

This gives `theouni` two complementary Graphify views:

```text
Portfolio graph
    = provenance / ownership / evidence / repository topology

Worldline atlas
    = task / perspective / intersection / invariant / termination topology
```

The two graphs answer different questions and should remain separate.
