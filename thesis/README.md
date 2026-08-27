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

1. Source repository manuscripts, proofs, evidence ledgers, and code own scientific claims.
2. [`chapter_registry.json`](chapter_registry.json) owns stable chapter allocation, source handoffs, headline claims, forbidden inferences, and claim ceilings.
3. [`draft_status.json`](draft_status.json) owns mutable prose progress and next drafting actions. Draft stage never upgrades scientific status.
4. Files under [`chapters/`](chapters/) are source-bounded writing briefs.
5. Files under [`drafts/`](drafts/) are working prose, and files under [`source_maps/`](source_maps/) record the support and non-support boundary for those drafts.
6. [`../universe/DISSERTATION_ARCHITECTURE.md`](../universe/DISSERTATION_ARCHITECTURE.md) owns the novelty-first editorial rationale.
7. [`../universe/WORLDLINE_ATLAS.md`](../universe/WORLDLINE_ATLAS.md) owns the non-linear theory map.

## Writing rule for every chapter

Each brief must retain these sections:

- **Problem** — the ecological or scientific failure that motivates the chapter;
- **Headline result** — the one result that earns chapter status;
- **Why the result is nontrivial** — why the chapter is not merely a familiar principle restated;
- **Ecological payoff** — what inference, design, or interpretation changes;
- **Claim ceiling** — what the source does not establish;
- **Canonical source handoff** — where the proof, data, code, and manuscript live;
- **Transition** — why the next chapter is scientifically necessary.

Every prose draft must additionally have a source map. The source map states what each source supports, what it does not support, and which claims still require primary-literature verification.

## Ownership firewall

- CREST, CCOC, MLTR, MRM, CED, RACH, eco-genetic-criticality, and eco-genetic-warning-extensions remain the primary owners of their source results.
- `theouni` owns the cross-repository type system, bridge registry, chapter coordination, and synthesis only.
- TU-2 belongs inside Chapter 6, TU-3 inside Chapter 7, TU-4 inside Chapter 8, and TU-1 inside the General Synthesis.
- A chapter may cite another worldline but may not silently absorb its theorem or empirical evidence.
- Prose completion, word count, or editorial polish does not alter a claim ceiling.

## Current writing state

The ten source-bounded briefs are present. The General Introduction has progressed to a v0.1 prose draft under [`drafts/00_general_introduction_v0.1.md`](drafts/00_general_introduction_v0.1.md), with support boundaries recorded in [`source_maps/00_general_introduction_sources.md`](source_maps/00_general_introduction_sources.md). It frames the dissertation around the reuse problem, uses only the minimum factorization language, and leaves source-owned results to the research chapters.

The remaining eight research chapters and General Synthesis remain at brief stage, but their source maturity and next actions are recorded explicitly in `chapter_registry.json` and `draft_status.json`.

Run:

```bash
python scripts/validate_thesis_workspace.py
python scripts/build_thesis_workspace_report.py
```

The first command checks chapter order, source ownership, TU allocation, hard dependencies, required headings, claim ceilings, draft/source-map presence, and minimum draft length. The second rebuilds `graphify-out/THESIS_WORKSPACE_REPORT.md`.
