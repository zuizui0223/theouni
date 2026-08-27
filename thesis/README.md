# Thesis writing workspace

This directory converts the preferred dissertation traversal into a source-bounded writing workflow. It does not copy source manuscripts into `theouni`, transfer theorem ownership, or turn bridge modules into independent novelty claims.

## Central thesis

> **When does a scientific representation that is adequate for one ecological task cease to be reusable after capability, future grammar, structural replacement, mechanism responsibility, evidence, target, representation, or domain changes?**

The dissertation is not organized as repeated answers to “what is ecological state?” Each research chapter owns one non-obvious forbidden inference and one source-owned result that makes the prohibition scientifically consequential.

## Canonical order

1. General Introduction — *The Reuse Problem in Ecology*
2. CREST — *When Conservation Capacity Outgrows Conservation Knowledge*
3. CCOC — *When Closed Simplicity Fails under Open Futures*
4. MLTR — *When Macro-Laws Do Not Survive Ecological Replacement*
5. MRM — *When Visible Equivalence Fails under Mechanism Uncertainty*
6. CED — *When Evidence Does Not License the State We Need*
7. RACH + TU-2 — *When Learning the Cause and Licensing the Decision Diverge*
8. Eco-genetic criticality + TU-3 — *Which State Actually Generates Functional Loss?*
9. Eco-genetic warning extensions + TU-4 — *When an Early Signal Is Not a Warning*
10. General Synthesis — *The Theory Universe: Adequacy Has No Privileged Direction of Travel*

This is the preferred editorial traversal, not the only valid topological order in the Worldline Atlas.

## Source-of-truth hierarchy

1. Source repository manuscript and theorem documents own scientific claims.
2. [`chapter_registry.json`](chapter_registry.json) owns chapter allocation, claim ceilings, source handoffs, and writing status.
3. Files under [`chapters/`](chapters/) are writing briefs. They may reorganize source-owned material but may not strengthen it.
4. [`../universe/DISSERTATION_ARCHITECTURE.md`](../universe/DISSERTATION_ARCHITECTURE.md) owns the novelty-first editorial rationale.
5. [`../universe/WORLDLINE_ATLAS.md`](../universe/WORLDLINE_ATLAS.md) owns the non-linear theory map.

## Writing rule for every chapter

Each brief must retain these sections:

- **Problem** — the ecological or scientific failure that motivates the chapter;
- **Headline result** — the one result that earns chapter status;
- **Why the result is nontrivial** — why the chapter is not merely a familiar principle restated;
- **Ecological payoff** — what inference, design, or interpretation changes;
- **Claim ceiling** — what the source does not establish;
- **Canonical source handoff** — where the proof, data, code, and manuscript live;
- **Transition** — why the next chapter is scientifically necessary.

## Ownership firewall

- CREST, CCOC, MLTR, MRM, CED, RACH, eco-genetic-criticality, and eco-genetic-warning-extensions remain the primary owners of their source results.
- `theouni` owns the cross-repository type system, bridge registry, chapter coordination, and synthesis only.
- TU-2 belongs inside Chapter 6, TU-3 inside Chapter 7, TU-4 inside Chapter 8, and TU-1 inside the General Synthesis.
- A chapter may cite another worldline but may not silently absorb its theorem or empirical evidence.

## Current writing state

The chapter registry and all ten writing briefs are the next-stage deliverables. Scientific results are already available at different maturity levels, from submission-frozen RACH and active CREST/EGW manuscripts to theorem-core chapter sources. The workspace records these differences rather than pretending that all chapters are equally drafted.

Run:

```bash
python scripts/validate_thesis_workspace.py
python scripts/build_thesis_workspace_report.py
```

The first command checks chapter order, source ownership, TU allocation, hard dependencies, required headings, and claim-ceiling markers. The second rebuilds `graphify-out/THESIS_WORKSPACE_REPORT.md`.
