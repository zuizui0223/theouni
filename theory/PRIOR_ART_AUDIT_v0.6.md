# Prior-art audit for the v0.6 Contract-Indexed Representation Adequacy spine

Status: **bounded primary-source audit; suitable for draft positioning, not an exhaustive novelty review**

Audit date: 2026-08-26

Object audited: [`DRAFT_v0.6_CONTRACT_INDEXED_QUOTIENT_TRANSPORT.md`](DRAFT_v0.6_CONTRACT_INDEXED_QUOTIENT_TRANSPORT.md) and [`contract_indexed_adequacy_registry.json`](contract_indexed_adequacy_registry.json)

## Decision

The bare mathematical spine of CIRA-1 through CIRA-5 should **not** be presented as a new information order or a new sufficiency theorem.

Its closest classical relatives divide into four distinct families:

1. Blackwell compares stochastic experiments by decision performance and parameter-independent randomization;
2. Le Cam turns exact experiment comparison into directed approximate comparison by deficiency;
3. classical statistical sufficiency preserves the information in a statistical model independently of a chosen loss;
4. Markov-chain lumpability gives a dynamic closure condition for a particular state-space quotient.

CIRA is an exact deterministic factorization calculus on a declared common carrier. Its defensible contribution, if the manuscript demonstrates one, is the **ecological contract architecture built on that substrate**: typed responsibilities, source ownership, evidence and reality firewalls, revision reserve, bridge obligations, and claim ceilings.

The concise Blackwell-positioning sentence is:

> **Relative to Blackwell, v0.6 does not claim a new information order; it recasts deterministic factorization as a contract-indexed ecological accountability discipline, and any novelty must come from the added provenance, bridge, revision, and claim-ceiling structure producing nontrivial ecological consequences.**

## Method and scope

This audit used primary publications and author-owned book chapters for substantive claims. Bibliographic/index pages were used only to locate those works. The comparison is conceptual rather than a proof of categorical equivalence: the four traditions do not use the same objects, quantifiers, or empirical semantics.

The audit is deliberately narrow. It does not cover computational mechanics, bisimulation, state abstraction, predictive representations, abstract statistical experiments after Le Cam, or recent machine-learning work on sufficient representations. Those remain separate prior-art obligations if the draft advances a novelty claim against them.

## Comparison map

| prior theory | object and comparison | overlap with CIRA | boundary that must remain explicit |
|---|---|---|---|
| Blackwell comparison | experiments/channels with a common parameter space; comparison through attainable risks and randomization | deterministic signature factorization is a zero-noise special case of post-processing | Blackwell compares observation experiments, normally uniformly over decision problems; CIRA changes the required response/task on a common world carrier |
| Le Cam deficiency | directed approximate simulation of one experiment by another, with bounded-loss risk transfer | natural candidate for an approximate or stochastic extension of exact CIRA adequacy | current CIRA has no Markov kernels, risk metric, approximation tolerance, or asymptotics |
| classical sufficiency | statistic sufficient for a distribution family/parameter when conditioning on it removes parameter dependence | the no-erasure/factorization intuition is shared | classical sufficiency is not, by default, relative to one selected loss function |
| Markov lumpability | partition of a Markov state space that preserves a closed Markov transition law | a special case of response-signature factorization when the response is the next-block transition distribution | TU-3 permits arbitrary contract-complete loss responses and is not restricted to Markov closure |

## 1. Blackwell comparison of experiments

### Primary result relevant here

Blackwell's 1951 comparison defines one experiment as more informative than another when every risk attainable with the latter is attainable with the former, and relates this comparison to a transition/sufficiency relation. The 1953 paper removes a finite-outcome restriction in the comparison result and also introduces weaker comparisons restricted by the number of available decisions. See [Blackwell (1951), *Comparison of Experiments*](https://projecteuclid.org/euclid.bsmsp/1200500222) and [Blackwell (1953), *Equivalent Comparisons of Experiments*](https://doi.org/10.1214/aoms/1177729032).

Under the usual channel reading, an experiment `F` is obtainable from `E` when a parameter-independent stochastic transition post-processes observations from `E` into observations distributed as under `F`. This gives a preorder; quotienting by mutual simulability gives the corresponding information order. It need not be total.

That non-totality can be seen without importing a new theorem. On the four-point parameter carrier

```text
Omega = {00, 01, 10, 11},
```

let one deterministic experiment reveal only the first bit and another reveal only the second. No parameter-independent post-processing of the first-bit observation can reproduce the second bit for both `00` and `01`, and conversely. The experiments are incomparable. This is an inference from Blackwell's transition definition, not a separate historical claim attributed to the papers.

### Exact relation to CIRA

For deterministic maps on one carrier, the CIRA task relation

```text
Sigma_alpha = g o Sigma_beta
```

has the same formal shape as deterministic post-processing. CIRA-2's reflexive/transitive preorder, CIRA-3's one-way reuse condition, and CIRA-4's incomparable pair therefore sit very close to the deterministic edge of Blackwell comparison.

The identification must stop there:

- Blackwell holds the parameterized experiment comparison fixed and quantifies over decision problems/risk functions for the strong order.
- CIRA holds a model-world carrier fixed and lets each task be a demanded response signature.
- A CIRA task is not automatically a Blackwell decision problem, and a retained deterministic representation is not automatically a statistical experiment.
- Blackwell's weaker `k`-decision comparisons show that restricting the decision class changes the comparison, but that does not by itself establish CIRA's ecological notion of a contract-complete response signature.

Consequently, “failure of order transport across incomparable tasks” is more precise than “quotient noncommutativity,” but incompleteness of an information preorder is not itself novel relative to Blackwell. Also, incomparability is only one failure mode: reverse reuse across a strict refinement fails even when the two tasks are comparable.

## 2. Le Cam deficiency

### Primary result relevant here

Le Cam's 1964 paper develops sufficiency and approximate sufficiency for statistical experiments; the later monograph explicitly organizes experiments, transitions, deficiencies, and sufficiency in one decision-theoretic framework. See [Le Cam (1964), *Sufficiency and Approximate Sufficiency*](https://doi.org/10.1214/aoms/1177700372), [Le Cam (1986), *Asymptotic Methods in Statistical Decision Theory*](https://doi.org/10.1007/978-1-4612-4946-7), especially [Chapter 2, *Some Results from Decision Theory: Deficiencies*](https://doi.org/10.1007/978-1-4612-4946-7_2).

The relevant conceptual move is from exact randomization to approximate randomization. A directed deficiency asks how closely one experiment can simulate another through a transition; its decision-theoretic interpretation controls the additional risk needed to transfer bounded-loss procedures. Symmetrizing the two directed comparisons yields a distance between experiments. Exact constants depend on the normalization and regularity convention and are not imported into v0.6 here.

### Consequence for v0.6

Le Cam is not a contradiction to CIRA. It identifies the missing structure required to make CIRA approximate:

- a stochastic experiment rather than only a deterministic signature;
- a permitted class of transitions or Markov kernels;
- a discrepancy, usually total-variation-based in the classical construction;
- a bounded loss or decision class for risk transfer;
- an approximation tolerance and, for asymptotic claims, a sequence of experiments.

The present registry explicitly excludes stochastic, continuous, and approximate extensions. Therefore it may call CIRA an **exact deterministic substrate**, but it should not advertise an approximate adequacy theory until a deficiency-like quantity and its risk-transfer theorem are supplied.

## 3. Statistical sufficiency and the “loss-dependent sufficiency” phrase

### What the classical sources establish

Halmos and Savage formulate sufficiency for a family of probability measures and give a measure-theoretic factorization treatment. Bahadur then develops its role in statistical decision problems: under suitable conditions, decisions based on the full observation can be matched by decisions based on a sufficient statistic, so the justification is not confined to one hand-picked loss. See [Halmos and Savage (1949), *Application of the Radon-Nikodym Theorem to the Theory of Sufficient Statistics*](https://doi.org/10.1214/aoms/1177730032), [Bahadur (1954), *Sufficiency and Statistical Decision Functions*](https://doi.org/10.1214/aoms/1177728715), and [Bahadur (1955), *A Characterization of Sufficiency*](https://doi.org/10.1214/aoms/1177728545).

The classical dependence is on the statistical model or parameter family. A statistic can be sufficient for one family and insufficient for another. That is a genuine relativity, but it is not the same as selecting one loss function and calling the resulting reduction classically sufficient.

### Audit verdict on the phrase

This bounded audit did **not** verify “sufficient statistics are loss-function-relative” as a standard classical theorem under that wording. The safer distinctions are:

- **classical sufficiency:** model/family-relative and decision-universal within its stated conditions;
- **Blackwell comparison:** experiment-relative and quantified over a declared decision/risk class;
- **CIRA exact adequacy:** relative to one explicitly encoded response responsibility;
- **possible future extension:** loss-class-relative risk preservation, which would require its own definition and theorem.

There is also a terminology trap. `L-sufficiency` in the partial-sufficiency literature uses `L` for **likelihood**, not loss; the primary paper makes that convention explicit. See [Rémon (1984), *On a Concept of Partial Sufficiency: L-Sufficiency*](https://researchportal.unamur.be/en/publications/on-a-concept-of-partial-sufficiency-l-sufficiency/) and [Barndorff-Nielsen (1999), *L-nonformation, L-ancillarity, and L-sufficiency*](https://doi.org/10.1137/S0040585X97977495).

Accordingly, the v0.6 manuscript should use **task-indexed exact adequacy** or **decision-specific preservation** rather than claim that CIRA merely restates a standard theorem called “loss-dependent sufficiency.” A broader literature search could still locate specialized decision-relative notions; this audit's negative result is not a proof that no such terminology exists.

## 4. Markov-chain lumpability and TU-3

### Primary result relevant here

Kemeny and Snell define a finite Markov chain as lumpable with respect to a partition when, for every starting distribution, the block-valued process is Markov and its transition probabilities do not depend on that starting distribution. Their necessary-and-sufficient condition requires that, for every source block and destination block, the total one-step probability into the destination block is identical for every original state in the source block. See [Kemeny and Snell, *Finite Markov Chains*, §§6.3–6.4, especially pp. 124–126](https://math.pku.edu.cn/teachers/yaoy/Fall2011/Kemeny-Snell_Chapter6.3-4.pdf).

If `pi` maps a microstate to its block and

```text
Sigma_transition(x)
  = (P(x, destination block B))_B,
```

then the Kemeny-Snell condition is precisely that `Sigma_transition` is constant on every `pi`-fiber. In CIRA notation,

```text
Sigma_transition = Sigma_bar o pi.
```

Thus strong finite-state lumpability is an exact specialization of response-signature factorization for a transition-law responsibility.

### Relation to TU-3

This is proximity, not conflict.

- TU-3 asks whether a representation preserves the entire response signature required by a loss contract.
- Lumpability asks whether a state partition preserves a closed Markov transition law.
- If the loss contract requires the complete next-block transition distribution, the lumpability criterion directly supplies the relevant factorization test.
- If the loss signature is a terminal risk, mechanism label, history functional, or other non-Markov response, ordinary lumpability does not settle TU-3.
- Kemeny and Snell's weak lumpability depends on restricted starting distributions and is outside the current registry's deterministic exact carrier theorem unless that dependence is encoded explicitly in the contract.

The correct prior-art sentence is therefore: **TU-3 generalizes the same fiber-constancy pattern beyond Markov transition closure; it does not overturn lumpability.** Any manuscript claim that TU-3 is mathematically new must be narrowed to its extra loss-contract structure or withdrawn.

## What is already classical, and what remains open

### Do not claim as new

- factorization of a required response through a retained representation;
- equivalence between factorization, kernel inclusion, and refinement of induced partitions in the finite deterministic setting;
- reflexive/transitive comparison induced by post-processing;
- failure of reverse reuse after strict information loss;
- existence of incomparable information structures;
- joint retention by pairing two response maps;
- the fiber-constancy criterion when TU-3 is instantiated as finite Markov lumpability;
- the idea of an approximate experiment comparison once Le Cam deficiency is admitted.

### Potentially distinctive, but not established by this audit

- treating a scientific contract as jointly carrying future, history, mechanism, evidence, reportability, and warning responsibilities;
- keeping exact quotient adequacy separate from TU-2's graded epistemic utility;
- source-owned bridge obligations and common-carrier/map conditions across CREST, CCOC, MLTR, MRM, CED, RACH, EGC, and EGW;
- separating freeze integrity from revision reserve;
- using machine-readable claim ceilings and contradiction/bridge certificates as research-governance objects;
- the additional quantitative content of TU-1, TU-3, and TU-4, provided each survives its own domain-specific prior-art audit;
- a demonstrated ecological result that becomes sharper, testable, or safer because the modules are organized by this spine.

These are programme-level candidates. They become manuscript-level contributions only when an ecological example or theorem uses them to do work that the classical comparison theories alone do not already perform.

## Claim ceiling and promotion gate

The strongest statement licensed by this audit is:

> **CIRA-1 through CIRA-5 are a source-explicit deterministic synthesis of classical factorization, experiment comparison, and quotient preservation. The draft may claim architectural unification and ecological accountability only; it may not claim a new general information order, a new general sufficiency theorem, a Le Cam-style approximation theory, or a new lumpability result.**

The named-source prior-art gate is **boundedly complete** for draft positioning. Promotion to a manuscript claim still requires:

1. a wider search covering computational mechanics, bisimulation/state abstraction, predictive representations, and modern task-specific representation sufficiency;
2. a domain-level demonstration that the ecological contract architecture changes a theorem, admissible claim, analysis decision, or audit outcome;
3. separate novelty checks for TU-1's repair cost, TU-3's nuisance/hidden-coordinate witnesses, and TU-4's warning portability results;
4. exact citations and assumptions in the manuscript, rather than analogy-only references.

## Source-access limitations

- Project Euclid's current anti-bot layer prevented direct automated retrieval of the Blackwell and Le Cam article PDFs during this audit. Their DOI records, article metadata/abstracts, and the author-owned 1986 Le Cam chapter landing page were accessible. No unverified verbatim theorem text from the blocked PDFs is used here.
- The Kemeny-Snell chapter was available as an institutional scan; §§6.3–6.4 and the page-numbered definition/theorem were readable.
- Bahadur's 1954 publisher-version scan was available from the Indian Academy of Sciences repository, while searchable text quality was limited. The audit relies on its author summary and theorem-level scope, not OCR-sensitive quotation.
- The absence of a standard result named “loss-dependent sufficiency” is a bounded search result, not an exhaustive nonexistence claim.
