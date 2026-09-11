# C2 TREE red-team — likely editorial rejection reasons and pre-emptive fixes

Status: **internal editorial-risk audit**.

This audit asks how the proposal could be rejected even if every source result is correct.

## R1 — “This is just a sophisticated way to say more data are not always better.”

**Risk:** very high if the pitch leads with the slogan rather than the diagnostic separation.

**Current defence:** the proposal separates four failures that have different causes and different remedies: same dimension, wrong target, shared dependence, upstream loss.

**Required wording:** always follow the title-level slogan with the sentence that the contribution is the **four-way diagnostic separation**, not the slogan itself.

**Do not add:** more examples of generic bad data. That would strengthen the rejection rather than answer it.

## R2 — “The four boxes are a collage of known ideas from unrelated literatures.”

**Risk:** high because structural identifiability, goal-oriented design, pseudoreplication and imperfect detection/calibration are all mature literatures.

**Current defence:** C2 explicitly gives those literatures priority and claims only a cross-cutting doctrine for deciding which kind of ‘more’ is relevant to a particular ecological question.

**Editorial test:** the four failures must share one decision point:

> Before adding measurement effort, ask what distinction the new measurement creates or preserves, whether that distinction matters to the target, whether the opportunity is independent, and whether it survives the observation pipeline.

If the paper cannot be organized around that common decision, R2 wins and C2 should be redirected to a narrower journal.

## R3 — “This sounds like statistics/methods, not ecology or evolution.”

**Risk:** high if terms such as compatible worlds, rank, entropy, licensing and failure architecture dominate the proposal.

**Current defence:** editor-facing text now uses ecological-language aliases: same dimension / wrong target / shared dependence / upstream loss. Formal labels remain secondary.

**Required figure logic:** Figure 1 should show four ordinary ecological choices, not four equations:

1. measuring the same gradient more precisely;
2. measuring a nuisance trait instead of the biological target;
3. repeating one sensor or method with the same blind spot;
4. improving classification after missed encounters were never recorded.

Equations belong in the eventual boxes or source papers, not in the proposal’s visual centre.

## R4 — “The proposal is too inward-looking and based on the authors’ own programme.”

**Risk:** medium-high.

**Current defence:** external prior-art map leads the intellectual positioning; source-repository results are demonstrations, not literature substitutes.

**Release rule:** the final proposal bibliography and prose should contain more external intellectual anchors than self-programme references. Repository names should never appear in the editor-facing email.

## R5 — “The Campanula and island-pollination examples are unpublished or speculative.”

**Risk:** medium.

**Current defence:** both are explicitly worked measurement-design examples with claim ceilings; the proposal does not present their coefficients or translation tracks as new empirical findings.

**Required label:** use “worked example” or “measurement-design example,” never “case study demonstrating” unless empirical validation exists.

## R6 — “The framework is not genuinely useful because each field already knows its own warning.”

**Risk:** high and substantive.

**Best answer:** the framework is useful only if ecologists routinely face decisions where the wrong remedy is applied to the wrong failure — e.g. adding replicates to a structural-identification problem, optimizing classifier accuracy after upstream omission, or maximizing information about nuisance mechanisms when the reporting target is already different.

**Needed in final Opinion if invited:** at least one cross-domain example where diagnosing the failure class changes the next measurement decision.

## R7 — “The title overclaims: evidence is not monotone in measurement amount.”

**Risk:** medium.

**Current defence:** the paper does not say that more measurement never helps. It says additional measurement is not guaranteed to increase evidential adequacy across distinct scientific responsibilities.

**Fallback title if editor pushes back:**

**When more measurement is not more evidence: diagnosing four failures in ecological inference**

This is less provocative but more conditional.

## R8 — “Why TREE rather than MEE or a statistics/methods journal?”

**Risk:** high unless breadth is explicit.

**TREE answer:** this is not a new estimator or workflow. It is an Opinion about how ecology should reason about escalating measurement effort across field sampling, monitoring, sensors, experiments and mechanistic inference. Detailed algorithms remain in source methods papers.

If the editor asks for algorithmic validation or implementation detail as the central contribution, the concept is probably being read as MEE rather than TREE and the framing has failed.

## R9 — “The four failures are not exhaustive.”

**Risk:** medium if the text says or implies a complete taxonomy.

**Current rule:** call them **four recurrent failures** or **four diagnostically distinct failures**, not an exhaustive universal partition of all evidence problems.

## R10 — “The authorship looks strategically inflated or under-supported.”

**Risk:** currently low because only one named author is evidence-backed.

**Rule:** do not add supervisors/senior collaborators automatically. Additional authors require substantive C2-level synthesis, drafting and accountability contributions. Source-result ownership is handled by citation, not automatic authorship.

# Go / no-go after red-team

C2 should be sent only if all are true:

- the proposal can state its novelty without claiming any component warning as new;
- a non-specialist ecologist can explain the four failures after one read;
- at least one example changes a plausible ecological measurement decision;
- the paper is visibly an ecological Opinion, not a bundle of methods results;
- authorship is defensible by C2-level contributions;
- the live TREE contact route is confirmed immediately before sending.

Current internal assessment: **GO subject to outside-reader check and final authorship/contact confirmation.**
