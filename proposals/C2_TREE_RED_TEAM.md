# C2 TREE red-team — likely editorial rejection reasons and pre-emptive fixes

Status: **internal editorial-risk audit aligned with manuscript v8 direct-neighbour positioning**.

This audit asks how the proposal could be rejected even if every source result is correct.

## R1 — “This is just a sophisticated way to say more data are not always better.”

**Residual risk:** medium; reduced from very high in v6.

**V7 defence:** the paper now leads with a stronger common structure: familiar performance metrics are **local quantities conditioned on earlier measurement choices and losses**. Precision is conditional on the observational axis; information gain on the objective; replicate count on inferential unit/failure architecture; classifier accuracy on the retained-record set. The headline is therefore not “more can fail” but **when a local metric can and cannot proxy downstream claim resolution**.

**Required wording:** preserve the sentence that a conditional local metric is not automatically a universal proxy for a downstream scientific responsibility.

## R2 — “TREE already published LIES of omission; this is another observation-process taxonomy.”

**Residual risk:** high before v8; now the main editorial risk and explicitly confronted.

**V8 concession:** Chadwick et al. (2024) is the closest direct neighbour and must be cited early. LIES already provides a cross-field ecological typology (Latency, Identifiability, Effort, Scale), seeks methodological commonalities, links problem classes to inferential solutions, and treats interactions among observation problems. C2 cannot claim novelty for cross-field synthesis, four-part organization or interaction language.

**V8 defence:** C2 changes the publication-level question from **“what observation-process problem do we have and how can inference account for it?”** to **“for this declared claim, what class of measurement must change next?”** The four interfaces are an intervention screen, not a replacement taxonomy. The empirical commitment is prospective: claim-specific bottleneck diagnosis should predict whether equal effort is better spent on earlier capture, a new separating axis, target-relevant measurement or a new failure domain.

**Editorial test:** an outside reader should be able to explain the difference from LIES in one sentence and recover the prospective intervention-class prediction. If they instead describe C2 as a new taxonomy of observation bias, R2 is unresolved.

## R3 — “Separation is just Chamberlin/Platt strong inference.”

**Residual risk:** low-medium after v7.

**V7 fix:** Chamberlin (1890) and Platt (1964) are now explicit prior art, and ecological parameter-redundancy literature is added (Catchpole et al. 1996; Cole & McCrea 2016). C2 does not claim the idea of discriminating hypotheses. Its question is what observation design creates/preserves the required discrimination and how the other interfaces can still block it.

## R4 — “This sounds like statistics/methods, not ecology or evolution.”

**Risk:** medium.

**Current defence:** submission-facing text uses ecological-language interfaces and ordinary design questions. Formal mathematics remains in source papers. Box 1 now uses island/site contrasts and pollinator exclusion logic rather than an abstract trait-only example.

**Required Figure 1 logic:** biological opportunity → retained record → distinguishable alternatives → declared target; failure diversity is cross-cutting.

## R5 — “The proposal ignores the closest ecology/TREE design literature.”

**Residual risk:** low only if v8 citations stay explicit.

**V8 fix:** the manuscript now acknowledges not only big-data ecology (Michener & Jones 2012; McCleery et al. 2023) but also Williams & Brown (2019) on sampling-design/inference conditionality and Chadwick et al. (2024) LIES as the direct TREE neighbour. C2 cannot claim either observation-process synthesis or design conditionality as new.

## R6 — “The relevance example is a strawman.”

**Residual risk:** low after v7.

**V7 fix:** Candidate A now has more total world information **and a nonzero noisy target signal (75% correct)**. Candidate B has less total information but exact target resolution. The ranking reversal is between two scientifically useful measurements under different objectives, not nuisance-only information versus a perfect target oracle.

## R7 — “The worked examples are unpublished or speculative.”

**Risk:** medium.

**Current defence:** both remain explicitly worked design illustrations. Box 1 no longer assumes nectar-guide specificity; it asks for decoupled pollinator–climate contrasts or exclusions and measures visitor identity, effective pollen transfer and reproductive consequence. Box 2 is grounded in published metabarcoding/calibration literature.

**Required label:** use “worked design example/illustration,” never “case study demonstrating.”

## R8 — “The Predictions section is tautological.”

**Residual risk:** low-medium after v7.

**V8 fix:** interface-specific consequences are explicitly demoted as near-definitional. The paper also concedes that VoI/OED already rank candidate measurements once a target and model are specified. The remaining empirical claim is intervention-class prediction from the C2 diagnosis:

> Given a predeclared claim and equal-cost measurement expansions, diagnosis of the limiting interface before collecting new data should predict which intervention yields the largest gain in claim resolution.

Concrete tests are specified: known-truth simulations, monitoring systems with reference channels/audit samples, and randomized equal-effort prospective comparisons. The doctrine is weakened if diagnosis fails to predict intervention ranking. It is not claimed to outperform a correctly specified full VoI/OED model; the test is whether it identifies missing candidate classes or useful measurement changes before such a full model is available.

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

# Go / no-go after v8 direct-neighbour red-team

C2 is **GO for outside-reader testing** only if all are true:

- an outside reader can distinguish C2 from LIES as a prospective claim-specific measurement-choice doctrine rather than another observation-process taxonomy;
- they can state the intervention-class prediction without repository context;
- they understand that VoI/OED already rank candidate measurements and that C2 does not claim superiority to a correctly specified full design model;
- they can explain at least one cross-interface trade-off;
- Chamberlin/Platt, parameter-redundancy, sampling-design/inference and LIES prior art are acknowledged rather than claimed as new;
- Box 1 reads as decoupled design logic rather than trait-specific mechanism assertion;
- v8 interface order matches Figure 1;
- operating-semantics drift remains distinct from preservation failure;
- Boundary/C1 theorem ownership remains outside C2;
- the live TREE contact route is confirmed immediately before sending.

Current internal assessment: **GO for outside-reader testing, but not yet editorially de-risked. R2 is now a concrete direct-neighbour test: can a broad ecologist state what C2 adds after LIES and VoI/OED?**
