# `theouni` universe views

`universe/` keeps distinct views of the same research programme because they answer different questions.

## 1. Portfolio architecture

[`ARCHITECTURE.md`](ARCHITECTURE.md) and [`registry.json`](registry.json) answer:

> **Where does each claim, object, evidence type, and bridge come from?**

This is the provenance/ownership view. Source theorem ownership remains distributed across CREST, CCOC, MLTR, MRM, CED, RACH, the eco-genetic repositories, and the concrete empirical programmes.

The ontology registry is a provenance/theory snapshot, not the current whole-owner publication router. Its repository count must not be used as the current GitHub publication inventory.

## 2. Worldline atlas

[`WORLDLINE_ATLAS.md`](WORLDLINE_ATLAS.md) and [`worldline_atlas.json`](worldline_atlas.json) answer:

> **How can several task-indexed scientific perspectives coexist in one theory universe without one privileged chapter order or one privileged state?**

The atlas distinguishes nine worldlines:

```text
Capability / Required-State
Future / Open Grammar
History / Replacement
Mechanism / Response Type
Evidence / Licensing
Causal Learning / Next Observation
Revision / After Compression
Loss / Dynamic State
Warning / Portability
```

and keeps separate:

- universe-wide invariants;
- perspective-specific observables;
- intersections and bridge types;
- legitimate termination modes;
- genuine failure modes;
- hard scientific dependencies;
- narrative/presentation order.

The central organizational rule is:

> **The theory has a dependency structure, but no privileged narrative order.**

A dissertation chapter sequence is one traversal of the theory atlas, not the definition of the universe.

## 3. Dissertation traversal

The canonical dissertation source is [`../thesis/final_chapter_architecture.json`](../thesis/final_chapter_architecture.json).

It answers:

> **Which valid traversal best exposes the source programmes as distinct forbidden inferences?**

Its status is `final_editorial_order_forbidden_inference_spine`. The ten chapters are an editorial traversal and do not define publication units or transfer theorem ownership.

Older dissertation-view files under `universe/` remain useful overlays, but they do not override the thesis canonical source.

## 4. Whole-portfolio publication governance

[`PORTFOLIO_GOVERNANCE_2026-09-11.json`](PORTFOLIO_GOVERNANCE_2026-09-11.json) is the **only whole-owner publication-governance source of truth**. The readable companion is [`PORTFOLIO_GOVERNANCE_2026-09-11.md`](PORTFOLIO_GOVERNANCE_2026-09-11.md).

It answers:

> **Across all current `zuizui0223` repositories, which independent paper units exist, which repositories own or feed them, which items are modules/infrastructure/future programmes, and what is each paper's operational state?**

The governance snapshot covers **38 repositories** and distinguishes paper homes, co-homes, source-only repositories, modules, future programmes and infrastructure.

Its central invariant is:

```text
repository count
!= paper count
!= thesis chapter count
!= theory-map nodes
!= submission queue
```

In particular:

- one repository may own multiple papers (`fcp` currently owns two);
- one paper may span multiple repositories (`V3_REC_M4` is co-owned by `v3` and `rec`);
- a source repository may feed a flagship without becoming a simultaneous submission (`egc` -> `EGWE_NEE`);
- a module is not a failed paper (`balance`, PAYOFF-A/spatial/topology modules);
- future experimental programmes are not active papers until their gates close (`aza3`, `TTF`, `insepi`).

## 5. Observation / Evidence track publication programme

[`PUBLICATION_PROGRAMME_2026-09-11.json`](PUBLICATION_PROGRAMME_2026-09-11.json) is the **track-local router for Observation/Evidence only**.

It answers:

> **Within the Observation/Evidence track, which concept/method papers should be submitted and which repository retains each result?**

Current track programme:

```text
CONCEPT TRACK
C2  More measurement is not more evidence       -> TREE proposal-first
C1  Boundary identification-axis Perspective     -> conditional / parked

METHOD TRACK
M1  TNOA                                         -> MEE
M2  MROD                                         -> MEE
M3  CED                                          -> Ecological Modelling
M4  V3 + REC, excluding TNOA                     -> Ecological Informatics
```

Thus **5 confirmed + 1 conditional** is a property of this track only. It is explicitly forbidden to report 5+1 as the size of the whole publication portfolio.

The old files

- `SUBMISSION_ARCHITECTURE_2026-09-08.md`;
- `TWO_PAPER_EXECUTION_STATUS_2026-09-08.md`;

are historical snapshots. `TWO_PAPER_FIREWALL.json` remains a frozen historical artifact because downstream manifests may pin its blob SHA; it is not current publication governance.

## Graphify surfaces

- [`../graphify-out/GRAPH_REPORT.md`](../graphify-out/GRAPH_REPORT.md) — full portfolio/provenance graph.
- [`../graphify-out/WORLDLINE_REPORT.md`](../graphify-out/WORLDLINE_REPORT.md) — focused task/perspective overlay.
- [`../graphify-out/DISSERTATION_REPORT.md`](../graphify-out/DISSERTATION_REPORT.md) — dissertation overlay.
- `python scripts/build_worldline_overlay.py` — writes a Graphify-compatible worldline extraction.
- `python scripts/build_dissertation_overlay.py` — writes a Graphify-compatible dissertation extraction.
- `python scripts/validate_portfolio_governance.py` — validates all-repository paper/module/future routing.
- `python scripts/validate_publication_programme.py` — validates the Observation/Evidence 5+1 track and its firewall against the whole-portfolio router.

Do not merge the views merely to reduce file count. Their estimands are different:

```text
Portfolio architecture
    = provenance / ownership / evidence topology

Worldline atlas
    = scientifically allowed task / perspective topology

Dissertation architecture
    = editorial traversal around forbidden inferences

Portfolio governance
    = all-repository paper/module/future ownership and operational status

Observation/Evidence publication programme
    = track-local submission units / journals / cross-paper firewalls
```

The hard rule is:

```text
thesis order != theory-map order != portfolio paper units != track-local submission order
```
