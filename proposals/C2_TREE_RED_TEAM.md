# C2 TREE red-team — likely editorial rejection reasons and pre-emptive fixes

Status: **internal editorial-risk audit aligned with manuscript v6**.

This audit asks how the proposal could be rejected even if every source result is correct.

## R1 — “This is just a sophisticated way to say more data are not always better.”

**Risk:** very high if the pitch leads with the slogan rather than the diagnostic separation.

**Current defence:** the paper does not argue that more information is intrinsically harmful. It distinguishes four recurrent bottlenecks — timely preservation, separation, relevance and failure diversity — whose missing properties generate different failures and therefore different remedies.

**Required wording:** always follow the title-level slogan with the operational question: **what distinction must the next measurement create or preserve for the conclusion to change?**

**Do not add:** generic examples of “bad data.” That would strengthen the rejection rather than answer it.

## R2 — “This is a collage of known ideas from unrelated literatures.”

**Risk:** high because structural identifiability, goal-oriented design, value of information, pseudoreplication, imperfect detection, calibration and metabarcoding all have mature literatures.

**Current defence:** C2 explicitly gives those literatures priority and claims only the cross-cutting **measurement-to-evidence** synthesis: a biological distinction must be preserved, must separate live alternatives, must matter to the declared target, and repeated support must contain sufficient failure diversity.

**Editorial test:** the paper must remain organized around one prospective design decision:

> Before adding measurement effort, locate the limiting interface and ask what distinction the next measurement must create or preserve.

If the paper collapses back into four unrelated warnings, R2 wins and the synthesis should be narrowed.

## R3 — “This sounds like statistics/methods, not ecology or evolution.”

**Risk:** high if terms such as compatible worlds, rank, entropy, licensing and failure architecture dominate the proposal.

**Current defence:** submission-facing text uses ecological-language interfaces and ordinary design questions. Formal mathematics remains in source papers.

**Required Figure 1 logic:** Figure 1 must show the flow from **biological opportunity → retained record → distinguishable alternatives → declared target**. Timely preservation, separation and relevance label the interfaces; failure diversity spans the observation paths as a cross-cutting robustness layer. The visual centre must be an ecological measurement problem, not equations.

## R4 — “The proposal is too inward-looking and based on the author’s own programme.”

**Risk:** medium-high.

**Current defence:** external prior art leads the intellectual positioning; source-repository results are demonstrations, not literature substitutes. The v6 manuscript uses fourteen external references and removes repository labels and unpublished-source placeholders from submission-facing prose.

**Release rule:** editor-facing prose should contain more external intellectual anchors than self-programme detail. Repository names must never appear in the actual email sent to TREE.

## R5 — “The worked examples are unpublished or speculative.”

**Risk:** medium.

**Current defence:** Box 1 (*Campanula*) is explicitly a prospective worked design example, not empirical validation. Box 2 (metabarcoding) is based on established workflow-bias, calibration and ecological-inference literature rather than an unpublished field result.

**Required label:** use “worked design example” or “worked design illustration,” never “case study demonstrating” unless empirical validation exists.

## R6 — “The framework is not genuinely useful because each field already knows its own warning.”

**Risk:** high and substantive.

**Best answer:** the framework is useful only if diagnosing the limiting interface changes the next measurement decision — for example, choosing a mechanism-separating observation instead of more precision, diversifying failure domains instead of adding nominal replicates, or moving a metabarcoding intervention upstream instead of optimizing a classifier after amplification loss.

**Required payoff:** the final Opinion must make remedy matching more memorable than the four failure names themselves.

## R7 — “The title overclaims.”

**Risk:** medium.

**Current defence:** the manuscript includes an explicit non-harm caveat. It does not claim that extra information necessarily worsens inference; it claims that sample size, precision, total information, replicate count and conditional classifier accuracy are not universal monotone proxies for evidential progress toward a declared responsibility.

**Current preferred title:** **When more measurement is not more evidence**.

**Fallback if the editor requests more qualification:** **When more measurement is not more evidence: diagnosing bottlenecks in ecological inference**.

## R8 — “Why TREE rather than MEE or a statistics/methods journal?”

**Risk:** high unless breadth is explicit.

**TREE answer:** this is not a new estimator or workflow. It is an Opinion about how ecology and evolution should reason about escalating measurement effort across field sampling, monitoring, sensors, eDNA, genomics, experiments and mechanistic inference. Detailed algorithms remain in source methods papers.

If the editor asks for algorithmic validation or implementation detail as the central contribution, the concept is being read as MEE rather than TREE and the framing has failed.

## R9 — “The four interfaces are not exhaustive.”

**Risk:** medium if the text implies a complete taxonomy.

**Current rule:** call them **four recurrent interfaces/bottlenecks** or a practical screen, not a necessary-and-sufficient partition of all evidence problems. Failure diversity is explicitly cross-cutting rather than a fourth sequential pipeline stage.

## R10 — “The authorship looks strategically inflated or under-supported.”

**Risk:** currently low because only one named author is evidence-backed.

**Rule:** do not add supervisors or senior collaborators automatically. Additional authors require substantive C2-level synthesis, drafting and accountability contributions. Source-result ownership is handled by citation, not automatic authorship.

# Go / no-go after red-team

C2 should be sent only if all are true:

- the proposal can state its novelty without claiming any component warning as new;
- a non-specialist ecologist can explain the measurement-to-evidence logic after one read;
- at least one worked example changes a plausible ecological measurement decision;
- the paper is visibly an ecological/evolutionary Opinion, not a bundle of methods results;
- the four interfaces are presented as a practical screen rather than an exhaustive theorem;
- Boundary/C1 theorem ownership remains outside C2;
- authorship is defensible by C2-level contributions;
- the live TREE contact route is confirmed immediately before sending.

Current internal assessment: **GO subject to outside-reader check and final authorship/contact confirmation.**
