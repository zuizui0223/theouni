# `theouni` universe views

`universe/` has three complementary views of the same research programme.

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

## 3. Preferred dissertation traversal

[`DISSERTATION_ARCHITECTURE.md`](DISSERTATION_ARCHITECTURE.md) and [`dissertation_architecture.json`](dissertation_architecture.json) answer:

> **Which valid traversal best exposes the source programmes as distinct, non-obvious failures of scientific transport and reuse?**

This is an editorial view, not a new theorem layer. It chooses the following novelty-first sequence:

```text
General Introduction — the reuse problem

Part I   — capability and open futures
Part II  — macro-law and mechanism transport
Part III — evidence, causal learning, and decision licensing
Part IV  — loss-generating state and warning failure

General Synthesis — revision after compression and the Theory Universe
```

The source-owned research chapters are:

1. CREST — conservation capacity can outgrow conservation knowledge;
2. CCOC — closed simplicity need not survive open futures;
3. MLTR — inherited macro-laws need not survive replacement;
4. MRM — visible equivalence need not support one mechanism-safe law;
5. CED — more information need not license the target;
6. RACH + TU-2 — causal learning and decision licensing can diverge;
7. eco-genetic criticality + TU-3 — simulator detail and coarse marginals need not define the loss state;
8. eco-genetic warning extensions + TU-4 — a signal can lead loss without predicting it.

TU-1 is retained for the General Synthesis, where it asks whether an old scientific compression remains revisable after the task changes. TU-2, TU-3, and TU-4 remain embedded bridge/firewall modules rather than standalone novelty chapters.

The preferred traversal maximizes editorial novelty while preserving the Worldline Atlas claim that theory identity is not chapter order.

## Graphify surfaces

- [`../graphify-out/GRAPH_REPORT.md`](../graphify-out/GRAPH_REPORT.md) — full portfolio/provenance graph.
- [`../graphify-out/WORLDLINE_REPORT.md`](../graphify-out/WORLDLINE_REPORT.md) — focused task/perspective overlay.
- [`../graphify-out/DISSERTATION_REPORT.md`](../graphify-out/DISSERTATION_REPORT.md) — novelty-first dissertation overlay.
- `python scripts/build_worldline_overlay.py` — writes a Graphify-compatible worldline extraction.
- `python scripts/build_dissertation_overlay.py` — writes a Graphify-compatible dissertation extraction.

Do not merge the three views into one overloaded graph merely to reduce file count. Their estimands are different:

```text
Portfolio architecture
    = provenance / ownership / evidence topology

Worldline atlas
    = scientifically allowed task / perspective topology

Dissertation architecture
    = preferred editorial traversal for exposing novelty
```
