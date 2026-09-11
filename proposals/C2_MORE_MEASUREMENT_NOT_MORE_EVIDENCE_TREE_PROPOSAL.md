# Proposal — Trends in Ecology & Evolution Opinion

## Proposed title

**More measurement is not more evidence: four failures of monotonic reasoning in ecology**

## One-sentence thesis

Ecologists often treat more precise, more informative, more repeated, or better classified observations as automatically stronger evidence, but these four monotonic intuitions fail for different structural reasons; evidence is stronger only when new observations change the distinctions relevant to the declared scientific responsibility under a credible observation contract.

## Why this Opinion now

Ecology is increasingly measurement-rich. Automated sensors, remote sensing, bioacoustics, camera traps, genomic assays and model-based monitoring can generate more observations at lower marginal cost than before. Yet the scientific value of additional measurement is rarely monotone in the amount of data collected. A repeated observation can share the same failure mode as its predecessor; a precise measurement can lie in an already-observed direction; a highly informative variable can resolve nuisance state while leaving the ecological target ambiguous; and a perfect downstream classifier cannot reconstruct opportunities removed before a record existed.

These are often discussed separately as identifiability, experimental design, dependence, missingness, calibration or classification problems. We propose that they are better understood together as **four failures of monotonic reasoning about evidence**. The synthesis is not that all evidence problems reduce to one scalar. It is the opposite: different scientific responsibilities impose different conditions under which an added measurement can legitimately count as added evidence.

## Four failures

### 1. Geometry failure — more precision is not more identification

In a declared positive log-linear observation family, residual structural unidentified dimension is `k - rank(M)`. Repeating, rescaling or measuring more precisely along an existing row direction can reduce sampling uncertainty while leaving the row span—and therefore structural identification—unchanged. A new measurement changes structural identification only when it adds a genuinely new observation direction. The ecological lesson is that closeness to a mechanism, measurement detail and measurement precision are not an identification axis by themselves.

**Source owner:** `zuizui0223/boundary`.

### 2. Objective failure — more latent information is not more target evidence

The same candidate measurements can be ranked differently depending on the scientific responsibility. In an exact eight-world witness, a candidate revealing nuisance detail carries `2 bits` of mechanism information but has target-resolution probability `0`, whereas a `1 bit` target split resolves the declared target with probability `1`. Full latent-state information and target-licensing value therefore need not have the same maximizer.

**Source owners:** `zuizui0223/ced`; the learning/licensing distinction is coordinated with TU-2 and the MROD causal-learning programme without transferring MROD ownership.

### 3. Dependence failure — more repeats are not more independent evidence

Repeated reads within one shared weather, access, sensor, observer, batch or laboratory failure domain are not evidentially equivalent to observations distributed across independent failure opportunities. Repetition can improve sensitivity conditional on an operating mode while leaving the worst-case common-mode failure guarantee unchanged. Ecological sampling design must therefore distinguish replicate count from failure diversity.

**Source owner:** `zuizui0223/ced`.

### 4. Pipeline failure — better downstream processing is not recovery of upstream meaning

Two complementary cases expose this failure. First, in a protected BirdVox analysis, a true late-minus-early contrast of approximately `+0.1308` was essentially absent (`-0.000025`) after upstream entry selection even when downstream semantics were made oracle-perfect among retained truth-positive rows. Second, after a nuisance representation changed in TNOA, an inherited raw threshold of `0.55` retained strong ranking but nuisance recall at that threshold fell to `0.23125`; the transferable object was a declared error criterion that required recalibration, not the raw threshold itself. Thus neither downstream semantic perfection nor threshold inheritance can guarantee recovery of distinctions or operating meaning lost earlier in the observation pipeline.

**Source owners:** `zuizui0223/rec` and `zuizui0223/tnoa`.

## Ecological worked examples

The Opinion will include two compact worked examples whose role is illustration, not new empirical validation.

### Campanula / Izu observation design

The `mrod` Campanula/Izu programme separates a publication-grade structural example from phenomenological simulation. It asks which additional observations would discriminate among causal structures compatible with island patterns rather than merely collecting more of the same observable. This makes the geometry/objective distinction concrete: a measurement is valuable because of the worlds it separates for the question at hand, not because it is measurable or precise.

**Claim ceiling:** use `causal_model/campanula_structural.py` for validated structural statements; treat `examples/campanula_izu/` phenomenological coefficients only as illustrative model settings.

### Island pollination translation

The `examples/island_pollination_translation/` programme provides adapter contracts translating island-pollination questions into observation-design tracks. The repository explicitly classifies these as external adapter contracts rather than empirical evidence. They will be used to show how the same ecological system can demand different measurements for signed position, effective service and a complete response chain.

**Claim ceiling:** translation example only; no empirical validation claim.

## Proposed conceptual figure

A single four-panel figure will show four distinct reasons why the horizontal axis “more measurement” does not imply a vertical increase in “scientific evidence”:

1. **same row span** — precision increases, rank does not;
2. **wrong objective** — information increases, target remains unresolved;
3. **shared failure** — replicate number increases, independent failure opportunities do not;
4. **upstream collapse** — downstream accuracy increases, lost support/semantics do not return.

The figure will explicitly avoid a universal evidence score. Each panel has its own criterion for when extra measurement becomes scientifically useful.

## What is new in the synthesis

The mathematical ingredients—identification, information gain, dependence, missingness and calibration—have substantial literatures. The proposed contribution is therefore not a priority claim over those literatures. The new synthesis is an ecological **anti-monotonicity framework**: it identifies four recurrent ways in which common “more is better” reasoning fails, ties each failure to an explicit scientific responsibility, and turns the failures into practical design questions:

- Did the measurement add a new identification direction?
- Did it resolve distinctions relevant to the declared target?
- Did it add an independent failure opportunity?
- Was the relevant distinction retained before irreversible selection or semantic collapse?

This shifts monitoring design away from raw measurement abundance and toward responsibility-specific evidence contracts.

## Relationship to source papers

This Opinion owns the **cross-programme conceptual synthesis only**. It does not replace the source methods papers:

- `boundary` owns the identification geometry;
- `tnoa` owns semantic restraint, unresolved evidence states and calibration semantics;
- `mrod` owns sequential mechanism-learning observation design;
- `ced` owns target-safe reportability and failure-aware evidence;
- `v3/rec` own retained-information and record-entry empirical/audit machinery.

Detailed algorithms, proofs, thresholds and validation benchmarks remain in those source papers. The Opinion cites them as examples of the four failures rather than absorbing their novelty.

## Relationship to the Boundary Perspective proposal

The existing Ecology Letters Boundary proposal is retained as a conditional independent route. Its exclusive question is whether mechanistic proximity and identification strength form distinct axes. This proposal is broader: it asks why scientific evidence is non-monotone in measurement amount across geometry, objective, dependence and pipeline stages. If both routes proceed, Boundary mathematics appears here only as the geometry-failure exemplar rather than as the full identification-axis argument.
