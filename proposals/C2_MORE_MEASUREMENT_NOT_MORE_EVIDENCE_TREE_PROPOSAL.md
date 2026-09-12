# Proposal — Trends in Ecology & Evolution Opinion

## Proposed title

**More measurement is not more evidence: four failures of monotonic reasoning in ecology**

## One-sentence thesis

Ecologists often treat more precise, more informative, more repeated, or better classified observations as automatically stronger evidence, but these four monotonic intuitions fail for different structural reasons; evidence is stronger only when new observations change the distinctions relevant to the declared scientific responsibility under a credible observation contract.

## Opinion position

This Opinion argues for a change in default practice:

> **Measurement escalation should be diagnostic-first, not quantity-first.**

Before adding observations, precision, variables, replicates or downstream classifier performance, ecologists should first diagnose why the present evidence is inadequate. Different failures require different new information. Adding more of the wrong kind can leave the scientific conclusion unchanged even when data volume or nominal information increases substantially.

## Why this Opinion now

Ecology is increasingly measurement-rich. Automated sensors, remote sensing, bioacoustics, camera traps, genomic assays and model-based monitoring can generate more observations at lower marginal cost than before. Yet the scientific value of additional measurement is rarely monotone in the amount of data collected. A repeated observation can share the same failure mode as its predecessor; a precise measurement can lie in an already-observed direction; a highly informative variable can resolve nuisance state while leaving the ecological target ambiguous; and a perfect downstream classifier cannot reconstruct opportunities removed before a record existed.

These are often discussed separately as identifiability, experimental design, dependence, missingness, calibration or classification problems. We propose that they are better understood together as **four failures of monotonic reasoning about evidence**. The synthesis is not that all evidence problems reduce to one scalar. It is the opposite: different scientific responsibilities impose different conditions under which an added measurement can legitimately count as added evidence.

## Four failures

### 1. Same-dimension failure — more precision is not necessarily more identification

Repeated, rescaled or more precise measurement of a distinction already represented in the observation system can reduce sampling uncertainty without separating any additional mechanism states. What matters for structural identification is whether the new measurement creates a genuinely new distinction among otherwise compatible explanations. The ecological lesson is that closeness to a mechanism, measurement detail and measurement precision are not an identification axis by themselves.

This is the editor-facing label for the source-internal **same-direction failure**.

**Source owner:** `zuizui0223/boundary`. The exact rank theorem, sharp conditions, proxy-transport geometry and anchor diagnostics remain exclusively in the Boundary/C1 paper and are not reproduced here.

### 2. Wrong-target failure — more latent information is not more target evidence

The same candidate measurements can be ranked differently depending on the scientific responsibility. In an exact eight-world witness, a candidate revealing nuisance detail carries `2 bits` of mechanism information but has target-resolution probability `0`, whereas a `1 bit` target split resolves the declared target with probability `1`. Full latent-state information and target-licensing value therefore need not have the same maximizer.

**Source owners:** `zuizui0223/ced`; the learning/licensing distinction is coordinated with TU-2 and the MROD causal-learning programme without transferring MROD ownership.

### 3. False-independence failure — more repeats are not more independent evidence

Repeated reads within one shared weather, access, sensor, observer, batch or laboratory failure domain are not evidentially equivalent to observations distributed across independent failure opportunities. Repetition can improve sensitivity conditional on an operating mode while leaving the worst-case common-mode failure guarantee unchanged. Ecological sampling design must therefore distinguish replicate count from failure diversity.

**Source owner:** `zuizui0223/ced`.

### 4. Too-late failure — better downstream processing is not recovery of upstream meaning

Two complementary cases expose this failure. First, in a protected BirdVox analysis, a true late-minus-early contrast of approximately `+0.1308` was essentially absent (`-0.000025`) after upstream entry selection even when downstream semantics were made oracle-perfect among retained truth-positive rows. Second, after a nuisance representation changed in TNOA, an inherited raw threshold of `0.55` retained strong ranking but nuisance recall at that threshold fell to `0.23125`; the transferable object was a declared error criterion that required recalibration, not the raw threshold itself. Thus neither downstream semantic perfection nor threshold inheritance can guarantee recovery of distinctions or operating meaning lost earlier in the observation pipeline.

**Source owners:** `zuizui0223/rec` and `zuizui0223/tnoa`.

## Remedy-matched decision rule

The central synthesis is not the names of the four failures. It is the mapping from diagnosis to next action.

| diagnosed failure | question before collecting more data | appropriate next move |
|---|---|---|
| same dimension | does the new measurement separate a previously unresolved alternative? | measure a distinction that separates an unresolved explanation, not merely the old quantity more precisely |
| wrong target | can the new distinction change the declared prediction or decision? | measure target-relevant information rather than maximizing generic information |
| shared dependence | does the added observation create a genuinely independent opportunity for evidence to survive failure? | diversify failure domains rather than only increasing repeat count |
| upstream loss | is the needed distinction still present in the retained record? | capture it earlier in the pipeline; downstream accuracy cannot recreate deleted information |

A diagnosis is useful only if it changes what the ecologist would measure next.

## Ecological worked examples

The Opinion will include two compact worked examples whose role is illustration, not new empirical validation.

### Campanula / Izu observation design

The `mrod` Campanula/Izu programme separates a publication-grade structural example from phenomenological simulation. It asks which additional observations would discriminate among causal structures compatible with island patterns rather than merely collecting more of the same observable. This makes the geometry/objective distinction concrete: a measurement is valuable because of the worlds it separates for the question at hand, not because it is measurable or precise.

**Claim ceiling:** use `causal_model/campanula_structural.py` for validated structural statements; treat `examples/campanula_izu/` phenomenological coefficients only as illustrative model settings.

### Island pollination translation

The `examples/island_pollination_translation/` programme provides adapter contracts translating island-pollination questions into observation-design tracks. The repository explicitly classifies these as external adapter contracts rather than empirical evidence. They will be used to show how the same ecological system can demand different measurements for signed position, effective service and a complete response chain.

**Claim ceiling:** translation example only; no empirical validation claim.

## Proposed conceptual figure

Figure 1 is a **decision map**, not a four-box catalogue.

It begins from one common problem — current evidence does not resolve the ecological question — and asks which failure limits inference. Each diagnosis then leads to its own question and its own next measurement action:

1. **same dimension** → add an identification direction;
2. **wrong target** → add target-relevant information;
3. **shared dependence** → add an independent failure opportunity;
4. **upstream loss** → capture the distinction earlier in the pipeline.

The figure will explicitly avoid a universal evidence score and will not imply that the four failures are exhaustive. Canonical specification: `proposals/C2_FIGURE1_DECISION_MAP_SPEC.md`.

## What is new in the synthesis

The mathematical ingredients—identification, information gain, dependence, missingness and calibration—have substantial literatures. The proposed contribution is therefore not a priority claim over those literatures. The new synthesis is an ecological **anti-monotonicity framework with remedy matching**: it identifies four recurrent ways in which common “more is better” reasoning fails, ties each failure to an explicit scientific responsibility, and makes the diagnosis operational by asking what distinct kind of measurement would actually change the conclusion.

This shifts monitoring and experimental design away from raw measurement abundance and toward responsibility-specific evidence contracts.

## Why this perspective is timely and appropriately positioned

The problem becomes more important as ecological workflows combine automated collection, model-based filtering, machine classification and downstream decision systems. In such pipelines, increasing throughput can make a study look increasingly information-rich while leaving the actual inferential bottleneck unchanged.

The perspective arises from a linked programme spanning structural identification, target-relative reporting, failure-aware observation design, record-entry loss and calibration semantics. The Opinion does not ask TREE readers to adopt those source formalisms. It uses the cross-programme view to extract a simpler ecological decision doctrine that can travel across field sampling, biodiversity monitoring, sensor networks, experimental ecology, mechanistic inference and adaptive management.

## Relationship to source papers

This Opinion owns the **cross-programme conceptual synthesis only**. It does not replace the source methods papers:

- `boundary` owns the identification geometry;
- `tnoa` owns semantic restraint, unresolved evidence states and calibration semantics;
- `mrod` owns sequential mechanism-learning observation design;
- `ced` owns target-safe reportability and failure-aware evidence;
- `v3/rec` own retained-information and record-entry empirical/audit machinery.

Detailed algorithms, proofs, thresholds and validation benchmarks remain in those source papers. The Opinion cites them as examples of the four failures rather than absorbing their novelty.

## Relationship to the Boundary Perspective proposal

The existing Ecology Letters Boundary proposal is retained as a conditional independent route. Its exclusive question is whether mechanistic proximity and identification strength form distinct axes. This proposal is broader: it asks why scientific evidence is non-monotone in measurement amount across geometry, objective, dependence and pipeline stages. If both routes proceed, Boundary appears here only as the qualitative same-dimension exemplar; the exact identification-axis mathematics and diagnostics remain in C1.
