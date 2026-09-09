# Current theory hierarchy

Canonical synchronization date: **2026-09-09**.

The current cross-repository structure is documented in:

- [`theory/WORLD_STATE_EVIDENCE_HIERARCHY_2026-09-08.md`](theory/WORLD_STATE_EVIDENCE_HIERARCHY_2026-09-08.md) — human-readable hierarchy, worldviews, junctions and overlap firewalls;
- [`theory/OBSERVATION_SUPPORT_BRIDGE_2026-09-09.md`](theory/OBSERVATION_SUPPORT_BRIDGE_2026-09-09.md) — admission bridge separating method validity, deployment detectability, realized observation support, and downstream reportability;
- [`universe/theory_hierarchy_2026-09-08.json`](universe/theory_hierarchy_2026-09-08.json) — machine-readable nodes, typed edges, layers, canonical loop and overlap routing;
- [`universe/validate_theory_hierarchy_2026_09_08.py`](universe/validate_theory_hierarchy_2026_09_08.py) — fail-closed structural validator;
- [`theory/DRAFT_EVIDENCE_ADMISSIBLE_TRANSITION.md`](theory/DRAFT_EVIDENCE_ADMISSIBLE_TRANSITION.md) — local Boundary-to-CED report-transition bridge aligned to the hierarchy.

## One-line map

```text
CREST family
what must be distinguished
        ↓
Method / deployment qualification
whether the frozen inferential design can recover the target on the declared world/geometry
        ↓
Observation-support admission
whether realized measurement preserves enough support to instantiate that qualified design
        ↓
Observation family
what survives semantically, is identified, and can still be refined or acquired
        ↓
CED
when attained evidence is reliable enough to stop/report
        ↓
EG family
whether proposed states, proxies and warnings actually carry future information in the domain
        ↘
theouni meta-layer
whether any task-indexed representation/result can be reused after the contract changes
```

The principal junction is no longer represented by one comparison alone. It is the typed chain

```text
RequiredState J
    -> qualified inferential responsibility
    -> realized ObservationSupport O
    -> current evidence/identification E
    -> ReportableTarget
```

with non-equivalences

```text
RequiredState
!= MethodValidity
!= DeploymentDetectability
!= ObservationSupport
!= IdentifiedEvidence
!= ReportableTarget
```

The current routing firewall is:

```text
CREST    = required distinctions
method/deployment qualification = error/power/detectability on declared worlds and geometry
ObservationSupport = whether realized measurement preserves the support needed to instantiate the qualified procedure
REC      = pre-row support/selection loss
V3       = refinement by already-retained information
TNOA     = observation-semantic preservation/coarsening
Boundary = structural identification now
MROD     = prospective observation choice
CED      = reliability-qualified terminal stopping/reportability
EG       = domain predictive/measurement validation
theouni  = task-indexed bridge/reuse/revision synthesis
```

## Empirical bridge witness

TTF v0.11 -> v0.12 is registered only as a bounded source-owned witness of the new admission distinction:

```text
method/design qualification PASS
        +
realized observation-support FAIL
        ->
not_evaluable / empirical statistic remains unopened
```

It is **not** treated as empirical validation of CREST, CED, or the hierarchy, and it supplies no positive or negative flower-colour sharedness result.

This index is a synthesis artifact only. Source repositories retain theorem, code and empirical ownership.