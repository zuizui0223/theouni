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
6. Files under [`audits/`](audits/) record editorial overlap, duplication, and claim-allocation decisions.
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

The ten source-bounded briefs are present. The General Introduction has progressed to citation-audited v0.2 under [`drafts/00_general_introduction_v0.2.md`](drafts/00_general_introduction_v0.2.md), with support boundaries recorded in [`source_maps/00_general_introduction_v0.2_sources.md`](source_maps/00_general_introduction_v0.2_sources.md).

Version 0.2 replaces provisional source tags with an explicit reference list and separates the dissertation-level reuse problem from the CREST chapter's conservation paradox, contract construction, shallow-lake case, and capability–resolution theorem. The allocation decision is recorded in [`audits/00_general_introduction_crest_overlap.md`](audits/00_general_introduction_crest_overlap.md).

The remaining eight research chapters and General Synthesis remain at brief stage. Chapter 1 is now the next active drafting target and must be adapted from the CREST paper using the overlap audit rather than reintroducing the full dissertation framework.

Run:

```bash
python scripts/validate_thesis_workspace.py
python scripts/build_thesis_workspace_report.py
```

The first command checks chapter order, source ownership, TU allocation, hard dependencies, required headings, claim ceilings, draft/source-map/audit presence, citation-stage requirements, and minimum draft length. The second rebuilds `graphify-out/THESIS_WORKSPACE_REPORT.md`.
