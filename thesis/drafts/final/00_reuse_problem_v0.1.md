<!-- draft-id: chapter:introduction:v0.1 -->
# 再利用問題

*English working title: The Reuse Problem*

> **Draft status:** source-bounded v0.1. Chapter 0 is framing, not an independent global theorem. The exact theorem used here is TU-1 on revision after compression; Chapters 1–8 supply the heterogeneous source-owned counterexamples.

## 1. The problem begins after a representation succeeds

Ecology cannot retain everything. A field survey records a subset of what is present; a mechanistic model retains selected processes; a monitoring programme compresses a changing system into indicators; a management rule maps a small state description to an action; an early-warning analysis compresses trajectories into signals. These reductions are not defects. They are what make scientific comparison, forecasting and intervention possible.

The problem of this dissertation begins after such a representation has already worked.

A representation can be adequate for one scientific responsibility and then be asked to do something else. A measurement that tracks an endpoint may later be used to identify mechanism. A signal that appears before loss may be used as a warning. A variable that can be measured may be promoted to the next measurement worth collecting. A single eco-genetic summary may be asked to stand for several distinct target states. A compact interface calibrated under a restricted future may be reused after the future grammar is opened. A small change in management capability may be assumed to require only a small increase in monitoring. A source macro-law may be carried through structural replacement. Repeated observations may be treated as interchangeable with independent evidence.

These moves share one tempting inference:

> **A representation that worked once can be reused for every later scientific responsibility.**

This dissertation rejects that inference as a default. It does not replace it with the opposite claim that reuse always fails. Instead it asks, chapter by chapter, what must be true for reuse to be licensed and what kind of failure occurs when that condition is absent.

The distinction matters because failure of reuse is not the same as falsity of the original representation. A state may still be adequate for the task for which it was built. A source macro-law may still be exact on the source system. A genetic trajectory may genuinely precede loss. Repeated measurements may genuinely improve precision. What fails is the additional inference that success under one responsibility automatically travels to another.

## 2. A minimal formal language for reuse

Let \(\Omega\) be a declared finite universe of model worlds and let a scientific responsibility \(\alpha\) require a response signature

\[
\Sigma_\alpha:\Omega\to Y_\alpha.
\]

A retained representation is a map

\[
R:\Omega\to Z.
\]

The minimal exact adequacy condition is factorization:

\[
R\models\alpha
\quad\Longleftrightarrow\quad
\exists f:Z\to Y_\alpha\text{ such that }\Sigma_\alpha=f\circ R.
\]

The representation is adequate exactly when it does not merge two worlds that the declared responsibility requires to have different answers. This is classical quotient/factorization substrate, not a novelty claim of the dissertation. Its value here is disciplinary: it makes clear that adequacy is indexed by a responsibility rather than by a context-free amount of detail. [T0]

Reuse introduces a second responsibility, \(\beta\). Even if \(R\models\alpha\), reuse for \(\beta\) requires a second factorization,

\[
\Sigma_\beta=g\circ R.
\]

Nothing in the first factorization implies the second. A representation can therefore be correct, useful and even minimal for \(\alpha\) while being insufficient for \(\beta\). No contradiction follows. The two tasks ask for different response distinctions.

The dissertation uses this language as a common grammar, but it does not claim that every chapter is one instance of the same theorem. Some chapters establish exact finite impossibility or existence results; one uses a controlled benchmark; one uses a full-denominator warning audit; one establishes finite-model state separation. Their carriers, estimands and evidence types differ. The commonality is the structure of the forbidden inference, not identity of mathematical object.

## 3. Revision after compression gives an exact reuse boundary

TU-1 gives the cleanest exact version of the reuse problem after a state has already been stored. Suppose an old scientific contract induces partition \(P\) of \(\Omega\), and only the old state label \(q_P(\omega)\) is retained. A later contract requires partition \(Q\). The new state is recoverable from the old label alone exactly when

\[
q_Q=f\circ q_P
\]

for some deterministic map \(f\). Equivalently, every old-state block lies inside one new-state block. [T1]

If the revised responsibility splits an old block, post-processing the old state label cannot recreate the erased distinction. This is not a claim that nature has lost information. It is a statement about scientific storage: once a distinction has been collapsed by the retained representation, it is unavailable to a later task unless raw-world access or revision-sufficient auxiliary information remains.

TU-1 also quantifies the minimum exact side information required for revision. If an old block \(B\) intersects \(r_B(P,Q)\) new blocks, then the minimum auxiliary alphabet is governed by the worst hidden split,

\[
K_{\rm rev}(P\to Q)=\max_{B\in P}r_B(P,Q),
\]

with idealized revision debt \(D_{\rm rev}=\log_2K_{\rm rev}\). The executable verification checks the factorization boundary, the constructive minimum code, the relation between average refinement debt and worst-case revision debt, and a family in which worst-case debt is \(m\) bits while average refinement debt is arbitrarily small. [T2]

This result gives Chapter 0 a formal anchor without turning the chapter into a theorem that all reuse fails. It proves only a same-carrier revision criterion after compression. The substantive diversity of reuse failures is supplied by the source programmes in Chapters 1–8.

## 4. Eight ways a successful shortcut can fail to travel

The final chapter order is organized by one forbidden inference per research chapter. The sequence is editorial rather than a theorem-dependency chain. Each chapter closes one shortcut and hands a different question to the next. [A0]

### 4.1 More observation does not automatically mean more mechanism identification

Chapter 1 starts with the observation map itself. In a declared positive multiplicative chain, endpoint-only observation can remain invariant along a mechanism-equivalence class. Adding precision, repeated endpoint observations or biologically proximal measurements does not remove that equivalence unless the observation map acquires an identifying anchor. The relevant object is identification strength, not biological proximity alone. [C1]

### 4.2 Earlier does not automatically mean predictive

Chapter 2 moves from identification to warning discrimination. In the frozen EGWE audit, each genetic threshold precedes every observed loss in both tested ensembles, yet the same thresholds also fire in every audited non-event. Temporal precedence is therefore compatible with zero specificity and binary-marker AUC 0.5. A signal can be genuinely early and still fail the scientific responsibility of warning. [C2]

### 4.3 Measurable does not mean equally worth measuring next

Chapter 3 asks what to observe after ambiguity has been admitted rather than hidden. MROD ranks verified candidate observations by current information about the retained mechanism ambiguity and recomputes value after every realized outcome. In the frozen controlled benchmark, information-guided ordering resolves ambiguity with fewer nuisance selections and fewer observations than random ordering under the declared synthetic family. The result concerns ordering under a specified candidate vocabulary, not universal optimality. [C3]

### 4.4 One system does not have one context-free state

Chapter 4 moves from measurement choice to the object being summarized. The eco-genetic programme separates potential viability, realised occupancy, demographic state, genetic diversity and allele persistence. A fragmentation gradient and an alignment counterexample show that these target-dependent states need not move together and that coarse marginals can hide transition-relevant structure. The conclusion is not that five named variables form a universal ontology; it is that one convenient eco-genetic summary cannot be presumed to represent every declared responsibility. [C4]

### 4.5 A narrow physical boundary does not cap future-response memory

Chapter 5 opens the future grammar. CCOC supplies a finite synthetic relay whose local implementation and focal/exterior cut remain bounded while an open grammar forces exponentially many exact response distinctions. Physical narrowness and causal-interface memory are therefore different resources. The witness is exact within the declared finite construction; it is not an empirical claim about islands, corridors or ecological networks in general. [C5]

### 4.6 A small capability change does not cap epistemic burden

Chapter 6 changes a different object: the action repertoire itself. CREST proves that for every \(m\), one newly admitted controllable action can add one viable world while forcing a retained present slice to refine from one state to \(2^m\) required states, creating exactly \(m\) bits of monitoring debt under unchanged evidence. Small capability gain and small monitoring burden are not generally coupled. [C6]

### 4.7 A source law does not automatically survive structural replacement

Chapter 7 asks whether an inherited macro-law retains one meaning after the system is replaced. MLTR makes the source semantics explicit. A route-independent carried law exists only under source-target coherence; when complete carried maps disagree across declared histories, one history mode per distinct carried map is necessary and sufficient to preserve the inherited meanings. Structural replacement is not merely a larger future grammar or a larger action set; it changes the carrier and the semantics being transported. [C7]

### 4.8 Repetition does not substitute for independent failure opportunities

Chapter 8 turns from structural transport to evidence reliability. CED shows that repeated observations within one shared failure domain face a guarantee ceiling that independent failure modes can exceed under equal raw effort. The result does not say repetition is useless. It says replicate count alone is not a certificate that the observation architecture has diversified the ways in which evidence can succeed. [C8]

## 5. The common result is typed, not scalar

It is tempting to summarize these chapters by saying that “more information is not always better.” That slogan is too coarse. The chapters do not share one scalar measure of information, and they do not define one total order called scientific adequacy. [S0]

Their richness proxies are different: biological proximity, temporal earliness, measurability, summary breadth, physical-boundary simplicity, intervention increment, source-law validity and replicate count. Their failures are also different: non-identification, zero discrimination, poor observation ordering, target-state mismatch, open-future memory inflation, monitoring debt, route-dependent semantic transport and shared failure architecture.

The safe synthesis is therefore typed:

> **Across these distinct scientific responsibilities, none of the recorded richness proxies is an automatic certificate of adequacy.**

This claim is weaker than a global theorem of non-monotonicity and stronger than a loose collection of cautions. It is supported by eight source-owned results that block eight different monotone shortcuts. Chapter 9 will return to this matrix and combine it with TU-1's exact revisability criterion. [S1]

## 6. What the dissertation does not claim

The reuse problem does not license a context-free skepticism about ecological representation. The dissertation does not claim that coarse states are bad, that more measurement is harmful, that interventions should remain limited, that repeated sampling is pointless, or that scientific laws never travel.

Nor does the Theory Universe acquire ownership of the source results. Boundary owns the identification theorem and field-design consequence; EGWE owns the warning audit; MROD owns the observation-design benchmark; eco-genetic-criticality owns the finite-model state separation; CCOC owns the open-future memory witness; CREST owns the capability-resolution theorem; MLTR owns the source-relative replacement results; CED owns the failure-architecture result. theouni supplies a typed architecture, relation firewalls and the TU modules used at specified junctions. [A1]

Finally, the formal model-world results do not automatically establish natural empirical states. Moving from ecological reality into a declared model world requires an explicit admission bridge: empirical unit, measurement map, target, observation/reliability contract, validation unit and claim ceiling. The distinction between model-world adequacy and empirical truth is maintained throughout. [A2]

## 7. Roadmap as a sequence of questions

The chapter order should be read as a sequence of questions, not as a proof chain.

Chapter 1 asks what an observation map can identify in principle. Once identification strength is separated from biological proximity, Chapter 2 asks a different question: can an observed signal discriminate future loss? When temporal precedence fails to guarantee warning, Chapter 3 asks which additional observation is worth collecting next. Chapter 4 then asks whether the state being learned is itself unique across scientific targets. Chapters 5 and 6 ask how future grammar and intervention capability create distinct burdens of memory and monitoring. Chapter 7 asks whether a law built on one structure can be transported after replacement. Chapter 8 asks whether repeated evidence is trustworthy when its failures are shared. Chapter 9 asks whether these heterogeneous successes and failures can be ordered along one privileged direction of adequacy.

The answer anticipated here is deliberately bounded: no single richness proxy used in these chapters licenses that privilege. The rest of the dissertation earns that conclusion one forbidden inference at a time.

## Internal source keys

- **[T0]** `theory/DRAFT_v0.6_CONTRACT_INDEXED_QUOTIENT_TRANSPORT.md` — task-indexed factorization substrate; draft, classical mathematics, no empirical/global theorem claim.
- **[T1]** `theory/TU1_CONTRACT_REVISION.md` — exact same-carrier state-only revision criterion.
- **[T2]** `theory/verify_tu1.py` — executable TU-1 verification including divergence family.
- **[A0]** `thesis/final_chapter_architecture.json`, `thesis/transition_recovery_matrix.json` — editorial question-handoff order, not theorem implication.
- **[A1]** `thesis/verification_recovery_registry.json` — source ownership, snapshot SHA and claim ceilings.
- **[A2]** `theory/RELATION_SEMANTICS.md`, empirical admission validators — relation and reality/model firewalls.
- **[C1]** Boundary snapshot `d950cf9fe4d21d4677f1e16f29e8fbe3c7af8f84`.
- **[C2]** EGWE snapshot `7b2ca69b398d32071fd92d1da1d3b169c18a5d84`.
- **[C3]** MROD snapshot `5a89c3f77b3987751652541086816231507edf9d`.
- **[C4]** eco-genetic-criticality snapshot `290663cd25dd2ab06ef8913f97696fd29370f7f2`.
- **[C5]** CCOC snapshot `96d823309ce04affb33446f1996aedf0a163a039`.
- **[C6]** CREST snapshot `2ff41e18cdbf100932813fbef9851078ec60413a`.
- **[C7]** MLTR snapshot `d9e23d27c385759b9e1fea93a556f30618122fe1`.
- **[C8]** CED snapshot `e76c82cb9ab2ff674488f1434d0c13a7cb0c24ce`.
- **[S0]** `thesis/typed_synthesis_matrix.json` — distinct richness proxies and adequacy failures.
- **[S1]** `thesis/TYPED_SYNTHESIS_RECOVERY.md` — synthesis claim firewall.
