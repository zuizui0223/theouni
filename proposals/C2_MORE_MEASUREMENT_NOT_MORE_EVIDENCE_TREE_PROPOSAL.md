# Proposal — Trends in Ecology & Evolution Opinion

## Proposed title

**When more measurement is not more evidence**

## One-sentence thesis

Ecologists and evolutionary biologists often treat more precise, more informative, more repeated or better classified observations as automatically stronger evidence, but these quantities are not universal proxies for evidential progress; added measurement becomes useful evidence only when it creates or preserves a distinction that matters to the declared scientific responsibility.

## Opinion position

This Opinion argues for a change in default practice:

> **Measurement escalation should be diagnostic-first, not quantity-first.**

Before adding observations, precision, variables, replicates or downstream classifier performance, ecologists should diagnose which interface currently limits inference. We organize that diagnosis around four properties: **timely preservation, separation, relevance and failure diversity**. Their absence produces four recurrent failures — too late, same dimension, wrong target and false independence — and each points to a different measurement remedy.

## Why this Opinion now

Ecology and evolution are increasingly measurement-rich. Automated sensors, remote sensing, bioacoustics, camera traps, genomic assays, environmental DNA and machine-learning pipelines can expand observation volume and downstream performance at rapidly falling marginal cost. Yet the scientific bottleneck can remain unchanged. A repeated observation can share the same failure mode as its predecessor; a precise measurement can lie along an already represented distinction; a highly informative variable can resolve nuisance state while leaving the target ambiguous; and a perfect downstream classifier cannot reconstruct opportunities removed before a record existed.

These problems are often discussed separately as identifiability, experimental design, dependence, imperfect detection, calibration, missingness or classification. We propose that they can be connected through one question:

> **What distinction must the next measurement create or preserve for the conclusion to change?**

The synthesis is explicitly not a universal evidence score. It is a practical account of how a biological distinction must survive an observation pipeline, separate live alternatives, matter to the declared target and avoid dependence on one shared failure domain.

## Four interfaces and their failure modes

### 1. Separation — failure when missing: same dimension

Repeated, rescaled or more precise measurement of a distinction already represented in the observation system can reduce sampling uncertainty without separating additional mechanism states. What matters for structural identification is whether the new measurement creates a genuinely new distinction among otherwise compatible explanations.

This is the editor-facing version of the source-internal **same-direction failure**.

**Source owner:** `zuizui0223/boundary`. The **exact rank theorem**, row-span criterion, proxy-transport geometry and anchor diagnostics **remain exclusively in the Boundary/C1 paper** and are not reproduced here.

### 2. Relevance — failure when missing: wrong target

The same candidate measurements can be ranked differently depending on the scientific responsibility. In an exact eight-world witness, a candidate revealing nuisance detail carries `2 bits` of mechanism information but has target-resolution probability `0`, whereas a `1 bit` target split resolves the declared target with probability `1`. Full latent-state learning and target-licensing value therefore need not have the same maximizer.

**Source owner:** `zuizui0223/ced`.

### 3. Failure diversity — failure when missing: false independence

Repeated reads within one shared weather, access, sensor, observer, population, batch or laboratory failure domain are not evidentially equivalent to observations distributed across independent failure opportunities. Repetition can improve sensitivity conditional on a functioning mode while leaving vulnerability to a common-mode loss unchanged. Ecological sampling design must therefore distinguish replicate count from failure diversity.

**Source owner:** `zuizui0223/ced`.

### 4. Timely preservation — failure when missing: too late

A biological difference can disappear before a downstream model ever sees it. In a protected BirdVox analysis, a true late-minus-early contrast of approximately `+0.1308` was essentially absent (`-0.000025`) after upstream entry selection even when downstream semantics were oracle-perfect among retained truth-positive rows. A complementary TNOA result shows that when representation changes, an inherited numerical threshold can lose its operating meaning even if ranking remains useful; the transferable object is the declared error semantics, which may require recalibration.

These are two forms of the same interface question: **is the needed distinction still present in the retained record?** If yes, downstream modelling or recalibration may help. If no, the intervention must move earlier.

**Source owners:** `zuizui0223/rec` and `zuizui0223/tnoa`.

## Remedy-matched decision rule

The central synthesis is the **remedy-matched decision rule**, not merely the names of the four failures.

| interface / diagnosed failure | question before collecting more data | appropriate next move |
|---|---|---|
| separation / same dimension | does the proposed measurement separate a previously unresolved alternative? | measure a new distinction rather than only the old quantity more precisely |
| relevance / wrong target | can the new distinction change the declared prediction, contrast or decision? | measure target-relevant information rather than maximizing generic information |
| failure diversity / false independence | does the added observation create an independent opportunity for the distinction to survive failure? | diversify failure domains rather than only increasing repeat count |
| timely preservation / too late | is the needed distinction still present at the stage being improved? | capture earlier, or recalibrate only if the distinction remains retained |

A diagnosis is useful only if it changes what the ecologist would measure next.

## Ecological worked examples

The Opinion uses two compact worked examples whose role is illustration, not new empirical validation.

### Box 1 — Island *Campanula*: separation and relevance

A prospective island *Campanula* study can observe the same coarse floral cline under several compatible explanations, including abiotic filtering, pollinator-mediated selection and demographic history. More observations of the same cline improve description but need not separate those alternatives. A targeted nectar-guide phenotype can be more valuable if it makes the competing explanations predict different outcomes. Its value comes from the alternatives it separates for the declared question, not from being intrinsically more mechanistic.

**Claim ceiling:** worked design example only; no new field-validation claim.

### Box 2 — Metabarcoding: timely preservation and failure diversity

If a focal taxon is absent from a final metabarcoding table, deeper sequencing or a better classifier helps only if the relevant sequence survived field sampling, extraction and amplification. If the sequence remains but output probabilities have unstable operating meaning, recalibration or improved classification may help. If the sequence was never amplified, no downstream classifier can recover it. Thousands of reads from one extraction also do not constitute thousands of independent opportunities to survive extraction failure.

**Claim ceiling:** worked design illustration based on established metabarcoding and ecological-inference problems; no new empirical benchmark.

## Proposed conceptual figure

Figure 1 is a **measurement-to-evidence interface map**, not a four-box catalogue. It follows the flow from biological opportunity / live alternatives to retained record, distinguishable alternatives and declared target. **Timely preservation, separation and relevance** label the three interfaces. **Failure diversity** is not a fourth sequential arrow; it spans the observation paths as a cross-cutting robustness layer.

Each failure is paired with its question and remedy, and the figure explicitly avoids both a universal evidence score and a claim that the four interfaces are exhaustive. Canonical specification: `proposals/C2_FIGURE1_DECISION_MAP_SPEC.md`.

## What is new in the synthesis

The mathematical and methodological ingredients — structural identification, goal-oriented design, value of information, replication, imperfect detection, calibration and observation-pipeline bias — have substantial literatures. The contribution is therefore not a priority claim over those literatures. The proposed synthesis is a cross-domain ecological framework for **diagnostic distinction design**: it asks which distinction is missing, where it is lost, whether it matters to the target and whether repeated support survives independent failure opportunities.

This reframes monitoring and experiment design away from raw measurement abundance and toward responsibility-specific observation contracts.

## Why this perspective is timely and appropriately positioned

The problem becomes more important as ecological workflows combine automated collection, model-based filtering, machine classification and downstream decisions. In such pipelines, increasing throughput can make a study look increasingly information-rich while leaving the actual inferential bottleneck unchanged.

The Opinion does not ask TREE readers to adopt source-specific mathematics or software. It extracts a simpler design doctrine that can travel across field sampling, biodiversity monitoring, sensor networks, experimental ecology, evolutionary inference and adaptive management.

## Relationship to source papers

This Opinion owns the **cross-programme conceptual synthesis only**. Detailed algorithms, proofs, thresholds and validation benchmarks remain source-owned:

- `boundary` owns the identification geometry;
- `ced` owns target-safe reportability and failure-aware evidence;
- `mrod` owns mechanism-learning observation design and the prospective *Campanula* source example;
- `rec` owns record-entry loss and irreversibility evidence;
- `tnoa` owns calibration semantics and transfer of declared error meaning across representation change.

## Relationship to the Boundary Perspective proposal

The Ecology Letters Boundary proposal is retained as a conditional independent route. Its exclusive question is whether mechanistic proximity and identification strength are distinct axes. C2 asks the broader question of how measurement becomes evidence across preservation, separation, relevance and failure diversity. If both routes proceed, Boundary appears here only as the qualitative same-dimension exemplar; the exact identification-axis mathematics and diagnostics remain in C1.
