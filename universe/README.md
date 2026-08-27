# `theouni` universe views

`universe/` has two complementary views of the same research programme.

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

## Graphify surfaces

- [`../graphify-out/GRAPH_REPORT.md`](../graphify-out/GRAPH_REPORT.md) — full portfolio/provenance graph.
- [`../graphify-out/WORLDLINE_REPORT.md`](../graphify-out/WORLDLINE_REPORT.md) — focused task/perspective overlay.
- `python scripts/build_worldline_overlay.py` — writes a Graphify-compatible extraction to `graphify-out/.worldline_extraction.json` by default.

Do not merge the two views into one overloaded graph merely to reduce file count. Their estimands are different: provenance topology versus theory-worldline topology.
