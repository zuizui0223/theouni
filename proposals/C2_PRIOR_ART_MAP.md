# C2 prior-art map — *More measurement is not more evidence*

Status: **external-literature novelty firewall for the TREE Opinion proposal**.  
Checked: **2026-09-11**.  
Purpose: prevent C2 from claiming novelty for component ideas that already have mature literatures. C2 owns only the cross-literature synthesis into four distinct failures of monotonic measurement reasoning in ecology.

## The claim C2 may make

> Ecologists often speak as if more measurement, greater precision, more latent-state information, more repeats, or better downstream classification all move evidence in the same favourable direction. They do not. Four different failure mechanisms — **geometry, objective, dependence, and pipeline** — break that monotonic intuition for different reasons and therefore require different design remedies.

C2 should **not** claim that it is the first work to show that more data can be unhelpful, that identifiability matters, that experiments should be goal-directed, that pseudoreplication is dangerous, that nondetection is not absence, or that classifier calibration/domain shift matter.

The proposal-level novelty is instead:

1. to distinguish four mathematically and operationally different ways in which “more” fails;
2. to connect each failure to a different ecological measurement-design question;
3. to show why no single scalar such as sample size, precision, entropy reduction, replicate count, or classifier accuracy can certify evidential adequacy across these responsibilities;
4. to connect those abstract failures to concrete ecological measurement contracts without transferring theorem or empirical-result ownership from the source papers.

---

## Failure 1 — Geometry

### C2 formulation

**More precise measurement, more repeats, or more reported variables need not improve structural identification when they do not add a new observation direction.**

### Mature prior literature

- **Villaverde, Barreiro & Papachristodoulou (2016), “Structural Identifiability of Dynamic Systems Biology Models,” PLOS Computational Biology 12:e1005153. DOI: 10.1371/journal.pcbi.1005153.**  
  Structural identifiability is explicitly separated from the success of a parameter-estimation algorithm; unidentifiable model structure cannot be repaired merely by applying a better estimator.

This literature establishes that structural identifiability is a prerequisite and that richer/noisier estimation should not be confused with identifiability.

### Source-owned sharpening used by C2

`zuizui0223/boundary` supplies the exact positive log-linear result:

- residual dimension `k - rank(M)`;
- one scalar candidate reduces the structural unidentified dimension iff its row lies outside the current row span;
- duplicate, rescaled, or exact linear-combination rows add no structural identification.

### Novelty boundary

C2 does **not** invent structural identifiability, rank-nullity, or the idea that some measurements are redundant. Its contribution is to place **identification geometry** beside three other non-monotonicities and translate the result into a general ecological design diagnostic:

> Did the new measurement cut a previously unresolved direction, or merely measure an old direction more accurately?

---

## Failure 2 — Objective

### C2 formulation

**More information about the latent world need not be more useful evidence for the declared scientific target.**

### Mature prior literature

- **Vanlier et al. (2012), “A Bayesian approach to targeted experiment design,” Bioinformatics 28:1136–1142. DOI: 10.1093/bioinformatics/bts092.**  
  Experimental effort is targeted at reducing uncertainty in predictions of interest rather than indiscriminately reducing all parameter uncertainty.

- **Attia, Alexanderian & Saibaba (2018), “Goal-Oriented Optimal Design of Experiments for Large-Scale Bayesian Linear Inverse Problems,” Inverse Problems 34. DOI: 10.1088/1361-6420/aad210.**  
  Goal-oriented OED minimizes posterior uncertainty in a declared quantity of interest rather than the full estimated parameter.

- **Canessa et al. (2015), “When do we need more data? A primer on calculating the value of information for applied ecologists,” Methods in Ecology and Evolution 6:1219–1228. DOI: 10.1111/2041-210X.12423.**  
  Ecological value-of-information analysis asks whether additional information is expected to improve management outcomes given explicit objectives and available actions.

These literatures already establish that information value is objective-dependent.

### Source-owned sharpening used by C2

`zuizui0223/ced` provides an exact same-world/same-cost finite witness:

- `nuisance_detail`: 2 bits about full mechanism identity, exact target-resolution probability 0;
- `target_split`: 1 bit about full mechanism identity, exact target-resolution probability 1.

`zuizui0223/mrod` separately owns mechanism-learning observation design and must not be absorbed into C2.

### Novelty boundary

C2 does **not** claim to invent targeted OED, goal-oriented design, or value of information. It uses those traditions to make the broader synthesis credible and asks a sharper cross-programme question:

> More information **about what**, for **which scientific responsibility**?

---

## Failure 3 — Dependence

### C2 formulation

**More repeated observations need not provide more independent evidence when they share a failure domain.**

### Mature prior literature

- **Hurlbert (1984), “Pseudoreplication and the Design of Ecological Field Experiments,” Ecological Monographs 54:187–211. DOI: 10.2307/1942661.**  
  The classical pseudoreplication argument distinguishes nominal sample count from statistically independent replication and shows why non-independent replicates cannot be treated as independent evidence for a treatment effect.

This literature already makes dependence and experimental-unit structure central to ecological evidence.

### Source-owned sharpening used by C2

`zuizui0223/ced` supplies a failure-architecture result in which:

- within-mode repeats can improve conditional sensitivity;
- independent modes alter the worst-case guarantee against losing all assigned observations through common-mode failure;
- unlimited repeats within a fixed shared-failure architecture need not reach the guarantee supplied by additional independent failure opportunities.

### Novelty boundary

C2 does **not** rebrand pseudoreplication as new. The new synthesis is to treat **failure-domain diversity** as a distinct measurement resource, separate from replicate number, precision, and target relevance:

> Did we add another read, or another genuinely independent opportunity for the distinction to survive failure?

---

## Failure 4 — Pipeline

### C2 formulation

**Better downstream classification, more confident thresholding, or an inherited numerical operating point need not restore distinctions or operating meaning lost earlier in the observation pipeline.**

This failure has two subtypes in C2: **upstream support loss** and **representation/operating-semantics shift**.

### Mature prior literature: upstream observation error

- **MacKenzie et al. (2002), “Estimating site occupancy rates when detection probabilities are less than one,” Ecology 83:2248–2255. DOI: 10.1890/0012-9658(2002)083[2248:ESORWD]2.0.CO;2.**  
  A nondetection does not imply absence when detection probability is below one; ecological state and observation process must be separated.

This is a foundational ecological demonstration that the observed record is not automatically the latent biological state.

### Mature prior literature: calibration and threshold semantics

- **Dormann (2020), “Calibration of probability predictions from machine-learning and statistical models,” Global Ecology and Biogeography 29:760–765. DOI: 10.1111/geb.13070.**  
  Raw probability predictions need not have their nominal probabilistic meaning and should be calibrated before probabilistic interpretation.

- **Cowans et al. (2026), “Improving the integration of artificial intelligence into existing ecological inference workflows,” Methods in Ecology and Evolution. DOI: 10.1111/2041-210X.14485.**  
  Thresholding AI confidence scores into ecological detections discards classification uncertainty; a single catch-all threshold is unlikely to yield consistent performance across classifiers/species/applications.

- **Chen et al. (2024/2025), “Producing plankton classifiers that are robust to dataset shift,” Limnology and Oceanography: Methods. DOI: 10.1002/lom3.10659.**  
  High-throughput ecological classifiers can fail under deployment dataset shift despite satisfactory nominal in-dataset performance.

These literatures already establish imperfect observation, calibration problems, threshold sensitivity, and domain shift.

### Source-owned sharpening used by C2

`zuizui0223/rec` supplies a protected BirdVox irreversibility result in which the true late-minus-early contrast is about `+0.130820`, whereas an oracle downstream analysis restricted to truth-positive rows that actually entered the record yields about `-0.000025`. The claim is not that all detectors behave this way, but that downstream semantic perfection cannot recreate truth-positive rows omitted upstream in that audited system.

`zuizui0223/tnoa` supplies a closed-world representation-change result in which an inherited raw threshold `0.55` yields nuisance recall `0.23125` after the representation changes, while recalibration against a declared family-conditional error meaning restores the predeclared operating criterion. TNOA owns the process-preserving observation interface and semantic-restraint method; C2 owns only the cross-programme lesson.

### Novelty boundary

C2 does **not** invent imperfect-detection modelling, classifier calibration, uncertainty-aware thresholding, or dataset-shift analysis. It adds a pipeline-level distinction:

> Is the problem a downstream decision rule that can be recalibrated, or an upstream distinction that has already been deleted from the record and therefore requires independent new information to recover?

---

# Cross-literature synthesis table

| “More” proxy | Why it can fail | Mature literature already covering the component | C2 design question |
|---|---|---|---|
| precision / number of measured variables | same observation geometry | structural identifiability | Did the new measurement add a new identification direction? |
| latent-world information / entropy reduction | wrong scientific objective | targeted/goal-oriented OED; ecological VoI | Did it resolve a distinction that can change the declared target? |
| replicate count | shared dependence / common-mode failure | pseudoreplication / experimental-unit design | Did we add independent failure opportunities or only repeated reads? |
| classifier quality / threshold confidence | upstream omission or changed operating semantics | imperfect detection; calibration; domain shift | Is the lost distinction still present to be recalibrated, or already gone? |

The unifying claim is therefore **not** that these literatures missed their own problem. The proposed TREE Opinion argues that ecology lacks a sufficiently explicit cross-cutting doctrine for deciding **which kind of “more” is evidentially relevant in a given scientific responsibility**.

---

# What would falsify or weaken the C2 pitch

The TREE pitch should be weakened or redirected if a prior synthesis is found that already does all of the following together:

1. separates structural identification gain from precision gain;
2. separates latent-state information gain from target/decision value;
3. separates replicate count from independent failure diversity;
4. separates downstream calibration problems from irreversible upstream record loss;
5. presents these as distinct non-monotonicities of ecological measurement/evidence rather than as one domain-specific problem.

Finding strong prior art for any **one** of the four components does not falsify C2; it is expected and should be cited prominently. The novelty claim only survives if the **four-way synthesis and diagnostic separation** remains genuinely absent or underdeveloped.

# Proposal writing rule

Lead with external literatures, not with repository names. Source-repository results should appear as compact demonstrations that make the synthesis testable and concrete. The editor should be able to accept the conceptual premise even without knowing the source programme.
