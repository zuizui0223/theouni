# `theouni` universe views

`universe/` keeps distinct views of the same research programme because they answer different questions.

## 1. Portfolio architecture

[`ARCHITECTURE.md`](ARCHITECTURE.md) and [`registry.json`](registry.json) answer:

> **Where does each claim, object, evidence type, and bridge come from?**

This is the provenance/ownership view. Source theorem ownership remains distributed across CREST, CCOC, MLTR, MRM, CED, RACH, the eco-genetic repositories, and the concrete empirical programmes.

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

## 4. Publication programme

[`PUBLICATION_PROGRAMME_2026-09-11.json`](PUBLICATION_PROGRAMME_2026-09-11.json) is the **only current publication-routing source of truth**.

It answers:

> **Which scientific questions should be submitted as papers, and which repository retains each method/result?**

Current programme:

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

Thus the current plan is **five confirmed submission units plus one conditional concept paper**, not a ten-paper chapter mapping and not the previous two-paper Observation/Evidence consolidation.

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
- `python scripts/validate_publication_programme.py` — validates publication/thesis separation and the current 5+1 routing.

Do not merge the views merely to reduce file count. Their estimands are different:

```text
Portfolio architecture
    = provenance / ownership / evidence topology

Worldline atlas
    = scientifically allowed task / perspective topology

Dissertation architecture
    = editorial traversal around forbidden inferences

Publication programme
    = submission units / journals / cross-paper firewalls
```

The hard rule is:

```text
thesis order != theory-map order != publication units
```
