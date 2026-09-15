# C2 TREE red-team — likely editorial rejection reasons and pre-emptive fixes

Status: **internal editorial-risk audit aligned with manuscript v7**.

This audit asks how the proposal could be rejected even if every source result is correct.

## R1 — “This is just a sophisticated way to say more data are not always better.”

**Residual risk:** medium; reduced from very high in v6.

**V7 defence:** the paper now leads with a stronger common structure: familiar performance metrics are **local quantities conditioned on earlier measurement choices and losses**. Precision is conditional on the observational axis; information gain on the objective; replicate count on inferential unit/failure architecture; classifier accuracy on the retained-record set. The headline is therefore not “more can fail” but **when a local metric can and cannot proxy downstream claim resolution**.

**Required wording:** preserve the sentence that a conditional local metric is not automatically a universal proxy for a downstream scientific responsibility.

## R2 — “This is a collage of known ideas from unrelated literatures.”

**Residual risk:** medium-high; still the main editorial risk, but v7 now has two explicit defences.

### Defence A — shared conditional structure

The paper no longer relies only on a four-item list. It argues that the four literatures share one architecture: a local metric is evaluated after some conditioning set has already been imposed, and evidential adequacy depends on whether that conditioning set preserves/creates the distinction required by the claim.

### Defence B — interface interactions

V7 gives interactions in the main text: a second sensor can increase failure diversity while changing detectability/calibration; primer diversity can reduce amplification blind spots while reducing depth; target-specific measurement can improve relevance while sacrificing broad mechanism information; earlier capture can improve preservation while raising annotation/storage burden.

**Editorial test:** if an outside reader still summarizes the paper as “identifiability + VOI + pseudoreplication + detection bias,” R2 remains unresolved. They should instead be able to state the conditional-locality thesis and the prospective intervention-ranking test.

## R3 — “Separation is just Chamberlin/Platt strong inference.”

**Residual risk:** low-medium after v7.

**V7 fix:** Chamberlin (1890) and Platt (1964) are now explicit prior art, and ecological parameter-redundancy literature is added (Catchpole et al. 1996; Cole & McCrea 2016). C2 does not claim the idea of discriminating hypotheses. Its question is what observation design creates/preserves the required discrimination and how the other interfaces can still block it.

## R4 — “This sounds like statistics/methods, not ecology or evolution.”

**Risk:** medium.

**Current defence:** submission-facing text uses ecological-language interfaces and ordinary design questions. Formal mathematics remains in source papers. Box 1 now uses island/site contrasts and pollinator exclusion logic rather than an abstract trait-only example.

**Required Figure 1 logic:** biological opportunity → retained record → distinguishable alternatives → declared target; failure diversity is cross-cutting.

## R5 — “The proposal ignores big-data ecology / prior TREE Opinions.”

**Residual risk:** low after v7, but keep explicit.

**V7 fix:** prior-art map and manuscript now acknowledge Michener & Jones (2012) on data-intensive ecology and McCleery et al. (2023) on integrating experiments and big data. C2 is not anti-big-data; its novelty claim is the conditioning-set diagnosis and prospective intervention ranking.

## R6 — “The relevance example is a strawman.”

**Residual risk:** low after v7.

**V7 fix:** Candidate A now has more total world information **and a nonzero noisy target signal (75% correct)**. Candidate B has less total information but exact target resolution. The ranking reversal is between two scientifically useful measurements under different objectives, not nuisance-only information versus a perfect target oracle.

## R7 — “The worked examples are unpublished or speculative.”

**Risk:** medium.

**Current defence:** both remain explicitly worked design illustrations. Box 1 no longer assumes nectar-guide specificity; it asks for decoupled pollinator–climate contrasts or exclusions and measures visitor identity, effective pollen transfer and reproductive consequence. Box 2 is grounded in published metabarcoding/calibration literature.

**Required label:** use “worked design example/illustration,” never “case study demonstrating.”

## R8 — “The Predictions section is tautological.”

**Residual risk:** low-medium after v7.

**V7 fix:** interface-specific consequences are explicitly demoted as near-definitional. The paper now has one core falsifiable prediction:

> Given a predeclared claim and equal-cost measurement expansions, diagnosis of the limiting interface before collecting new data should predict which intervention yields the largest gain in claim resolution.

Concrete tests are specified: known-truth simulations, monitoring systems with reference channels/audit samples, and randomized equal-effort prospective comparisons. The doctrine is weakened if diagnosis fails to predict intervention ranking.

## R9 — “The interface ordering is inconsistent.”

**Residual risk:** closed in v7.

Sections, table and Figure logic all use **timely preservation → separation → relevance**, with **failure diversity cross-cutting**. The text explicitly says this is an observation-path ordering, not a mandatory diagnostic sequence.

## R10 — “Operating-semantics drift is not preservation failure.”

**Residual risk:** closed in v7.

V7 labels semantic drift as a **nearby but distinct** calibration/transport problem. Preservation failure means the needed distinction is absent from the retained record; semantic drift means the record survives but its operating meaning changes.

## R11 — “Why TREE rather than MEE or a statistics/methods journal?”

**Risk:** medium-high unless breadth remains visible.

**TREE answer:** this is not a new estimator or workflow. It is an Opinion about how ecology and evolution should choose the next measurement across field sampling, monitoring, sensors, eDNA, genomics, experiments and mechanistic inference. Detailed proofs/algorithms remain in source papers.

## R12 — “The title overclaims.”

**Risk:** medium.

**Current defence:** explicit non-harm caveat. The paper does not claim that extra information worsens optimal inference; it claims that local metrics are not universal proxies for evidential progress toward a declared responsibility.

**Preferred title:** **When more measurement is not more evidence**.

**Fallback:** **When more measurement is not more evidence: diagnosing bottlenecks in ecological inference**.

## R13 — “The four interfaces are not exhaustive.”

**Risk:** low-medium.

**Current rule:** four recurrent interfaces/practical screen, not an exhaustive theorem. Model misspecification, nonstationarity, causal transport, selective reporting, strategic behaviour and ethics remain outside the taxonomy.

## R14 — “C2 steals Boundary's mathematical novelty.”

**Risk:** low if firewall remains intact.

**V7 rule:** C2 may say separation can have formal, testable conditions and may cite external parameter-redundancy literature. It may **not** reproduce `k-rank(M)`, the row-span iff theorem, Γ/κ, breakdown factor or anchor-ladder diagnostics. Those remain C1/Boundary.

## R15 — “The authorship looks strategically inflated or under-supported.”

**Risk:** currently low because only one named author is evidence-backed.

**Rule:** source ownership is handled by citation, not automatic coauthorship. Additional authors require substantive C2-level synthesis/drafting/accountability contributions.

# Go / no-go after v7 red-team

C2 is **GO for outside-reader testing** only if all are true:

- an outside reader can state the conditional-locality thesis without seeing repository context;
- they can explain at least one cross-interface trade-off;
- Chamberlin/Platt and ecological parameter-redundancy prior art are acknowledged rather than claimed as new;
- the main prediction is prospective intervention ranking, not a definitional restatement;
- Box 1 reads as decoupled design logic rather than trait-specific mechanism assertion;
- v7 interface order matches Figure 1;
- operating-semantics drift remains distinct from preservation failure;
- Boundary/C1 theorem ownership remains outside C2;
- the live TREE contact route is confirmed immediately before sending.

Current internal assessment: **GO, with R2 (cross-literature synthesis originality) as the remaining substantive editorial risk to test with the outside reader.**
