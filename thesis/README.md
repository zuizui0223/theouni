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
6. Files under [`audits/`](audits/) record editorial overlap, duplication, practical-connection, and claim-allocation decisions.
7. [`../universe/DISSERTATION_ARCHITECTURE.md`](../universe/DISSERTATION_ARCHITECTURE.md) owns the novelty-first editorial rationale.
8. [`../universe/WORLDLINE_ATLAS.md`](../universe/WORLDLINE_ATLAS.md) owns the non-linear theory map.

## Writing rule for every chapter

Each brief must retain these sections:

- **Problem** — the ecological or scientific failure that motivates the chapter;
- **Headline result** — the one result that earns chapter status;
- **Why the result is nontrivial** — why the chapter is not merely a familiar principle restated;
- **Ecological payoff** — what inference, design, or interpretation changes;
- **Claim ceiling** — what the source does not establish;
- **Canonical source handoff** — where the proof, data, code, and manuscript live;
- **Transition** — why the next chapter is scientifically necessary.

Every prose draft must additionally have a source map. The source map states what each source supports, what it does not support, and which claims still require primary-literature verification. Citation-audited drafts must contain a reference list and must not retain provisional internal source tags.

## Ownership firewall

- CREST, CCOC, MLTR, MRM, CED, RACH, eco-genetic-criticality, and eco-genetic-warning-extensions remain the primary owners of their source results.
- `theouni` owns the cross-repository type system, bridge registry, chapter coordination, and synthesis only.
- TU-2 belongs inside Chapter 6, TU-3 inside Chapter 7, TU-4 inside Chapter 8, and TU-1 inside the General Synthesis.
- A chapter may cite another worldline but may not silently absorb its theorem or empirical evidence.
- Prose completion, word count, or editorial polish does not alter a claim ceiling.

## Current writing state

Four units now have citation-audited v0.2 prose.

### General Introduction

[`drafts/00_general_introduction_v0.2.md`](drafts/00_general_introduction_v0.2.md) frames the dissertation around the reuse problem, provides only the minimum factorization language, and leaves the source-owned scientific results to Chapters 1–8. Its support boundary is recorded in [`source_maps/00_general_introduction_v0.2_sources.md`](source_maps/00_general_introduction_v0.2_sources.md).

### Chapter 1 — CREST

[`drafts/01_conservation_capacity_v0.2.md`](drafts/01_conservation_capacity_v0.2.md) retains the conservation paradox, contract-relative state, shallow-lake case, finite architecture, capability–resolution theorem, and transition to CCOC while avoiding a second dissertation-level philosophy introduction.

Its source/proof handoff is [`source_maps/01_conservation_capacity_sources.md`](source_maps/01_conservation_capacity_sources.md). The General Introduction allocation is fixed in [`audits/00_general_introduction_crest_overlap.md`](audits/00_general_introduction_crest_overlap.md), and the restoration-budget interpretation is bounded in [`audits/01_crest_monitoring_budget_connection.md`](audits/01_crest_monitoring_budget_connection.md).

### Chapter 2 — CCOC

[`drafts/02_open_futures_v0.2.md`](drafts/02_open_futures_v0.2.md) develops the grammar-aware exact interface, cross-grammar addressability lower bound, maximal one-action family, bounded-local relay, positive portability boundary, and ecological reading of open future addressability.

Its theorem/prior-art/reproducibility handoff is [`source_maps/02_open_futures_sources.md`](source_maps/02_open_futures_sources.md). The quantified boundary against CREST and MLTR is fixed in [`audits/02_ccoc_crest_mltr_boundary.md`](audits/02_ccoc_crest_mltr_boundary.md), preventing the three chapters from collapsing into the slogan that state merely depends on context.

### Chapter 3 — MLTR

[`drafts/03_macro_law_replacement_v0.2.md`](drafts/03_macro_law_replacement_v0.2.md) develops exact inherited-law portability, local obstruction, unique coarsest source-relative repair, transport defect, route coherence, minimum history augmentation, and the plant–pollinator restoration-priority witness.

Its proof/example/reproducibility handoff is [`source_maps/03_macro_law_replacement_sources.md`](source_maps/03_macro_law_replacement_sources.md). The distinction between source-relative repair, target-only abstraction, CCOC grammar inflation, conditional history, and MRM mechanism uncertainty is fixed in [`audits/03_mltr_transport_repair_boundary.md`](audits/03_mltr_transport_repair_boundary.md).

Chapter 4 is now the next active drafting target. It must move from declared source/target replacement to retained mechanism candidates that share a visible state but disagree under future interventions.

Run:

```bash
python scripts/validate_thesis_workspace.py
python scripts/build_thesis_workspace_report.py
```

The first command checks chapter order, source ownership, TU allocation, hard dependencies, required headings, claim ceilings, draft/source-map/audit presence, citation-stage requirements, and minimum draft length. The second rebuilds `graphify-out/THESIS_WORKSPACE_REPORT.md`.
