# More measurement is not more evidence: four failures of monotonic reasoning in ecology

**Article type:** Opinion  
**Target:** *Trends in Ecology & Evolution*  
**Status:** full manuscript draft v1; not submission-formatted; source ownership firewalls remain active

## Abstract

Ecology is becoming measurement-rich. Automated sensors, remote sensing, bioacoustics, camera traps, genomic assays and machine-learning pipelines can increase observation volume, precision and downstream predictive performance at rapidly falling marginal cost. Yet more measurement does not automatically yield stronger evidence for the ecological question being asked. We distinguish four recurrent failures of this monotonic intuition. **Same-dimension failure** occurs when greater precision or repetition measures distinctions already represented and therefore does not separate additional ecological explanations. **Wrong-target failure** occurs when a measurement reveals more about the system overall but less about the prediction or decision of interest. **False-independence failure** occurs when nominal replicates share a common failure domain. **Too-late failure** occurs when information is lost before record creation or when operating semantics are inherited after a representation changes. These failures have different remedies. The appropriate response may be to measure a new distinction, target the relevant outcome, diversify failure opportunities, or move measurement earlier in the pipeline. We argue that ecological measurement escalation should therefore be **diagnostic-first, not quantity-first**.

## More data are easier to collect than the right distinction

A familiar response to ecological uncertainty is to collect more data. Often that is the right response. More observations can reduce sampling error, reveal rare states, improve parameter precision and support better predictions. But “more” is not one thing. A study can add more measurements of the same variable, more variables, more information about latent system state, more replicates, more accurate classifier outputs, or more processing downstream of data collection. These additions are not interchangeable, and none is guaranteed to increase the evidence available for the scientific responsibility that motivated the study.

This distinction matters because contemporary ecology increasingly uses observation systems in which the cost of adding records is much lower than the cost of changing what is observed. A camera can collect millions of frames without observing the event that distinguishes two mechanisms. A classifier can improve from 90% to 98% accuracy while remaining downstream of an earlier filtering step that removed the events needed for a population-level contrast. A field programme can double the number of samples while leaving all samples exposed to the same site, observer, batch, weather or access failure. A genomic or sensor assay can sharply reduce uncertainty about nuisance state while leaving the management decision unchanged.

The usual phrase “we need more data” therefore hides a design question: **what distinction must the next measurement create or preserve for the ecological conclusion to change?**

Several mature literatures already answer parts of this question. Structural-identifiability theory distinguishes model ambiguity from estimation precision [1]. Targeted and goal-oriented experimental design asks whether an observation reduces uncertainty in a declared prediction or quantity of interest rather than in a full parameter vector [2,3]. Value-of-information analysis asks whether resolving uncertainty can improve a decision [4]. Ecologists have long distinguished nominal sample size from independent replication [5]. Occupancy and imperfect-detection models distinguish the latent ecological state from the observation process [6], while calibration and dataset-shift studies show that numerical model outputs can lose their nominal interpretation when deployment conditions change [7–9].

These traditions are usually taught and applied separately. We suggest that they can be connected by a common negative result: **evidence is not monotone in the amount of measurement**. Importantly, there is not one reason for this failure. We distinguish four. Each diagnoses a different way that an additional observation can fail to become additional evidence, and each points to a different remedy (Figure 1).

---

## Failure 1: more precision can stay in the same evidential dimension

Suppose two ecological explanations predict the same value for the variable that a study measures. Improving the precision of that variable can narrow confidence intervals indefinitely without separating those explanations. Repeating the same assay, rescaling it, or adding another exact transformation of it may increase numerical precision while leaving the set of compatible mechanisms unchanged.

This is the distinction between **precision** and **structural identification**. In systems biology and inverse problems, structural-identifiability theory formalizes whether distinct parameterizations or mechanisms can in principle generate the same observations [1]. The ecological lesson is broader than any particular model class: an observation can be measured extremely well and still fail to cut the ambiguity that matters.

Consider a pollination study in which fruit set is jointly determined by visit frequency and per-visit effectiveness. Measuring total fruit set more precisely does not by itself separate a “many visits, low effectiveness” explanation from a “few visits, high effectiveness” explanation. Likewise, measuring a spatial cline with ever greater precision does not distinguish alternative causal structures if those structures project to the same cline. The missing evidence is not more precision along the existing axis. It is an observation that separates explanations that were previously compatible.

The practical diagnostic is therefore:

> **Does the proposed measurement distinguish a previously unresolved ecological explanation, or does it only measure an already represented distinction more accurately?**

If the answer is the latter, the remedy is not necessarily more replication. It is a new measurement dimension. In a pollination system that may be per-visit pollen deposition rather than another count of visits. In a trophic system it may be an interaction or intervention response rather than a denser measurement of abundance. In a trait-environment study it may be a mechanistically discriminating trait rather than another covariate correlated with the same environmental gradient.

The exact structural geometry and diagnostic conditions for one declared positive log-linear observation class belong to the companion Boundary/C1 paper and are not reproduced here [Boundary manuscript placeholder]. Here the point is qualitative: **more precision is evidence only when precision was the limiting problem**.

---

## Failure 2: more information can answer the wrong question

Even when a measurement genuinely separates latent states, those distinctions may be irrelevant to the scientific target.

This point is familiar in targeted experiment design. If the scientific responsibility is a forecast, intervention effect or management decision, reducing uncertainty in every parameter or latent state can be less valuable than resolving one distinction that changes the target [2–4]. The same observation can therefore be highly informative about the system and nearly useless for the decision at hand.

A simple finite example makes the mismatch concrete. Imagine eight equally plausible ecological worlds. The worlds differ in a binary target-relevant state and a four-level nuisance attribute. One candidate measurement perfectly reveals the four-level nuisance state. It therefore provides 2 bits of information about full world identity, but it leaves the binary target unresolved. A second candidate provides only 1 bit about world identity but directly separates the target states. If the goal is to learn the full latent world, the first measurement is better. If the responsibility is to license the target distinction, the second is better. No contradiction exists: the two objectives are different.

This is why phrases such as “maximally informative sampling” are incomplete unless the object of information is declared. The relevant question is not simply how much uncertainty a measurement removes, but **which uncertainty** and **for what responsibility**.

Ecological monitoring often bundles several responsibilities that should instead be separated. A biodiversity survey may seek species discovery, occupancy estimation and management prioritization. A disease-surveillance programme may seek detection, prevalence estimation and intervention timing. A restoration project may seek mechanism learning and a yes/no decision about whether a treatment will improve a focal response. The observation that best serves one responsibility need not be the observation that best serves another.

The diagnostic is:

> **Can the new distinction change the prediction, classification or decision that the study is responsible for?**

If not, more information may be scientifically interesting without being evidence for the declared target. The remedy is **target-relevant measurement**, not information maximization in the abstract.

This does not make full-system learning unimportant. Mechanistic science often has good reasons to pursue broad latent-state resolution. The claim is narrower: a study should not use total entropy reduction, total parameter precision or generic model fit as if these automatically certify evidential adequacy for every downstream ecological claim.

---

## Failure 3: more replicates can share the same blind spot

Replication is one of ecology's strongest safeguards, but replicate count and evidential independence are not synonyms.

Hurlbert's critique of pseudoreplication made this point classical: observations that share an experimental unit or treatment history cannot be counted as if they were independent experimental replicates [5]. Modern monitoring systems add another version of the same problem. Multiple observations can share a **failure domain** even when they are temporally or numerically distinct.

Examples are common. Ten camera images from the same obscured camera share a camera-level failure. Ten PCR reads from one failed extraction share an extraction failure. Ten observations collected during one access restriction share an access failure. Repeated classifier evaluations on records produced by the same upstream sensor can share sensor-specific blind spots. Repeated surveys by the same observer, in the same weather window, or using the same protocol can inherit a common mode of failure.

Within a functioning mode, more repeats can improve conditional sensitivity. But they cannot provide the same worst-case protection as observations distributed across independent modes if the dominant risk is common-mode loss. An unlimited number of observations behind one shared point of failure can still disappear together.

This suggests a design resource that is often omitted from sample-size discussions: **failure diversity**. A programme with fewer nominal observations but more independent opportunities for the target-relevant distinction to survive may provide stronger evidence than a larger set of repeated reads concentrated inside one fragile mode.

The diagnostic is:

> **Did we add another observation, or another genuinely independent opportunity for evidence to survive failure?**

If the limiting problem is shared dependence, the remedy is not merely to increase the replicate count. It is to diversify sensors, sites, observers, batches, modes, time windows or other relevant failure domains. The exact choice depends on what failures are plausible for the scientific responsibility being protected.

The distinction also clarifies why “effective sample size” is not always enough as a generic correction. Statistical dependence can sometimes be summarized after data collection. But common-mode failure is partly a design property: if every measurement can be jointly erased or distorted by the same upstream event, no post hoc weighting scheme creates the missing independent opportunity.

---

## Failure 4: better downstream processing can arrive too late

The previous failures concern what a measurement distinguishes, what objective it serves and whether it provides an independent evidential opportunity. A fourth failure concerns **where in the observation pipeline information is lost**.

Ecological observations increasingly pass through multiple stages: opportunity for an event to occur, sensor exposure, record entry, filtering, detection, classification, thresholding, aggregation and final reporting. Improving a late stage does not necessarily repair losses at an earlier one.

The simplest version is imperfect detection. Occupancy modelling formalized the idea that a nondetection is not the same as absence when detection probability is below one [6]. In multi-stage digital systems, the problem can be even more explicit. If a biological event never entered the retained record, no downstream classifier—however accurate—can classify that missing event correctly. Better semantics on retained rows cannot recreate absent rows.

A complementary problem occurs when the record is retained but its numerical representation changes. A threshold that had a particular operating meaning under one representation may no longer carry the same meaning after recalibration, domain shift or feature transformation. Calibration work has long emphasized that nominal probability scores require validation [7], while recent ecological AI work warns against treating one confidence threshold as universally portable across species, classifiers and applications [8,9].

These are related but not identical failures. One is **irreversible support loss**: the distinction is no longer present in the record. The other is **operating-semantics drift**: the distinction may still be present, but the mapping from score to claimed error behaviour has changed.

This difference matters because the remedies differ. A changed threshold semantics can sometimes be repaired by recalibration against a declared error criterion. An omitted event cannot. Recovery then requires independent new information—another sensor, a reference process, an audit sample, or a redesign that moves observation earlier in the pipeline.

The diagnostic is:

> **Is the distinction we need still present in the retained record?**

If yes, recalibration or a better downstream model may help. If no, downstream accuracy is the wrong target for investment. The remedy is to **capture the distinction earlier**.

This failure is especially important for automated ecological monitoring because headline model performance is usually measured conditional on the records that reached the model. A classifier can be excellent on its evaluation set while the observation system as a whole remains biased because biologically relevant opportunities were selectively omitted before classification. Evaluating only the downstream model therefore risks confusing classifier performance with observation-system adequacy.

---

## From a four-box warning to a decision rule

A taxonomy of failure modes would not by itself justify another conceptual framework. The useful step is to turn diagnosis into a different next action.

| If the limiting failure is… | Ask… | Then prioritize… |
|---|---|---|
| **same dimension** | Does the next measurement separate a previously unresolved explanation? | a new distinction, not merely more precision |
| **wrong target** | Can the new distinction change the declared prediction or decision? | target-relevant information |
| **shared dependence** | Does the added observation create an independent opportunity for evidence to survive failure? | failure-domain diversity |
| **upstream loss / semantic drift** | Is the needed distinction still present in the retained record? | earlier capture if lost; recalibration if retained |

This is the core proposal: **measurement escalation should be diagnostic-first, not quantity-first**.

The framework also explains why common scalar summaries are useful but incomplete. Sample size is meaningful when sampling variance is limiting. Precision is meaningful when the right dimension is already observed. Entropy reduction is meaningful when the object of entropy matches the scientific responsibility. Replicate number is meaningful when replicates create relevant independent opportunities. Classifier accuracy is meaningful when the retained records are the correct support and the operating semantics travel. None of these quantities is defective. The error is to treat one of them as a universal proxy for evidential strength.

Figure 1 should therefore be read as a decision map rather than a ranking. There is no claim that every study experiences all four failures, that the four are exhaustive, or that they can be collapsed into one evidence score. The point is that asking **why current evidence is inadequate** is more informative than asking only **how to collect more**.

---

## Box 1. Island *Campanula*: measure the mechanism-separating trait, not only the cline

Spatial trait clines can be visually compelling yet mechanistically ambiguous. In an island *Campanula* observation-design example, several causal structures can remain compatible with the same coarse spatial pattern. Increasing the number of observations along that pattern improves description of the cline but need not separate the competing explanations.

A more diagnostic design asks which additional trait or interaction would produce different predictions under the still-compatible structures. One prospective candidate is a nectar-guide gradient. Its value does not come from being intrinsically more mechanistic or more precise than the original trait. Its value comes from whether the competing structures predict different guide patterns.

This example connects two failure classes. If more sampling only sharpens an already represented cline, the problem is **same dimension**. If a candidate measurement resolves biological detail that does not change the mechanism comparison or focal prediction, the problem is **wrong target**. The preferred observation is the one that separates the live alternatives for the question being asked.

This is a worked design example, not a new empirical validation claim. The source programme separates validated structural statements from phenomenological simulation, and coefficient magnitudes chosen for illustration should not be read as field estimates [MROD manuscript placeholder].

---

## Box 2. Island pollination: different questions require different measurements

Island pollination provides a simple way to see why “more pollination data” is not a single prescription.

Suppose an island plant shows a change in floral phenotype. At least three different scientific questions can follow.

1. **Are different visitors present?**  
   This requires measurement of visitor occurrence or visitation composition.

2. **Do those visitors provide effective pollination service?**  
   This requires measurements such as legitimate contact, pollen transfer or another defensible effectiveness proxy.

3. **Does pollination service change reproductive outcome?**  
   This requires a link from service to seed set, recruitment or another reproductive consequence.

Collecting more data on question 1 cannot substitute for question 2, and question 2 cannot substitute for question 3. A large camera-trap sample can therefore be excellent evidence for visitation while remaining weak evidence for reproductive consequence. The problem is not low data volume. It is a mismatch between the measured distinction and the scientific responsibility.

The same system can also exhibit dependence and pipeline failures. Hundreds of observations from one camera position can share a field-of-view blind spot. A classifier cannot recover visits that never entered the recording window. Thus a single ecological study can move among the four diagnoses as its question changes.

The example is a translation contract for observation design, not an empirical causal conclusion. Its purpose is to show how a biological question determines what measurement must exist before quantity becomes relevant [MROD island-pollination translation placeholder].

---

## What should ecologists report about measurement adequacy?

A diagnostic-first approach changes not only data collection but reporting. Methods sections usually describe what was measured and how often, but less often explain **which competing explanations, target states or failure modes each measurement was intended to distinguish**.

Four additions would make evidential claims easier to audit.

First, studies could name the **scientific responsibility** of the measurement: mechanism discrimination, prediction, classification, intervention choice, discovery, or another target. This prevents generic information gain from being mistaken for target relevance.

Second, studies could state the **live alternatives** that remain compatible before the new measurement. A new variable is evidentially useful only relative to alternatives it can separate.

Third, studies could describe relevant **failure domains** rather than only replicate counts. The question is whether repeated observations share sensors, observers, sites, batches, access conditions or other common points of failure.

Fourth, digital pipelines could distinguish **record support** from **downstream performance**. How many ecological opportunities could enter the record? Which were excluded before classification? Which performance metric is conditional on surviving those stages?

These additions do not require every ecological paper to become a formal identifiability analysis. They require only that measurement claims be tied to the distinction they are expected to create or preserve.

---

## Outstanding questions

### How can failure domains be learned rather than assumed?

Our diagnostic treats failure diversity as a design resource, but real failure structures are rarely known perfectly. Sensors can fail jointly for unexpected reasons, observer biases can cluster, and nominally independent sites can share environmental disturbances. Methods that infer failure domains prospectively—or adaptively diversify them when residual dependence is detected—would make the framework more operational.

### How robust is target-relevant evidence to target misspecification?

Targeted measurement is only as useful as the target declaration. Scientific goals can change, management objectives can be contested, and an initially nuisance variable can become important later. This creates a genuine tension between efficient target-specific design and preserving optionality for future questions. One promising direction is to design measurements that are target-relevant while retaining a transparent record of which other distinctions were intentionally left unresolved.

### When is upstream loss recoverable?

Some pipeline losses are irreversible without new data, but others can be repaired using reference samples, audit subsamples or alternative sensors. A useful next step is to characterize when a retained record plus an external reference process is sufficient to reconstruct omitted opportunities, and when no downstream correction can identify the missing support.

### Can one study move between failure classes over time?

Yes. Early in a programme, structural ambiguity may dominate. After adding a mechanism-separating measurement, target mismatch may become the limiting issue. Once the correct target is measured, common-mode failure can dominate precision. After automation, pipeline losses can become decisive. The framework is therefore not a once-only classification of studies. It is a sequence of diagnoses during the life of an observation system.

### Are the four failures exhaustive?

No. They are intended as a useful cross-cutting set, not a theorem about all possible evidential failure. Other problems—model misspecification, nonstationarity, strategic behaviour, causal transport, selective reporting and ethical constraints on measurement—can limit evidence in ways not captured here. The practical test is whether a proposed additional measurement fails because it stays in the same distinction, answers the wrong target, shares the same failure, or arrives after the needed information has been lost. If not, another diagnosis is needed.

---

## Conclusion: ask what the next measurement changes

Ecology does not have a data shortage in the same sense across all problems. In many systems the bottleneck is no longer the ability to collect more records. It is the ability to decide **which new distinction would count as evidence for the question at hand**.

Four common intuitions can therefore fail. Greater precision can stay in the same evidential dimension. More latent-state information can answer the wrong target. More replicates can share one blind spot. Better downstream processing can arrive after the decisive information has disappeared.

The remedies are correspondingly different: measure a new distinction, measure the target-relevant distinction, diversify failure opportunities, or move observation earlier in the pipeline. None can be replaced by a generic instruction to increase sample size or model performance.

The resulting rule is simple enough to use before designing a study, adding a sensor, commissioning another assay or retraining a classifier:

> **Before collecting more data, ask what distinction the next measurement must create or preserve for the ecological conclusion to change.**

Additional measurement becomes additional evidence only when that answer is explicit.

---

## Figure 1. Diagnostic-first measurement escalation

**Concept:** current evidence does not resolve the ecological question → diagnose the limiting failure → choose a remedy matched to that failure.

- Same dimension → does the next measurement separate an unresolved explanation? → **measure a new distinction**.
- Wrong target → can the new distinction change the prediction or decision? → **measure target-relevant information**.
- Shared dependence → is this an independent opportunity for evidence to survive failure? → **diversify failure domains**.
- Upstream loss → is the needed distinction still present in the retained record? → **capture earlier in the pipeline** (or recalibrate if the distinction remains present but its operating semantics changed).

Full visual specification: `proposals/C2_FIGURE1_DECISION_MAP_SPEC.md`.

---

## References

1. Villaverde AF, Barreiro A, Papachristodoulou A. Structural Identifiability of Dynamic Systems Biology Models. *PLoS Computational Biology*. 2016;12:e1005153. doi:10.1371/journal.pcbi.1005153.
2. Vanlier J et al. A Bayesian approach to targeted experiment design. *Bioinformatics*. 2012;28:1136–1142. doi:10.1093/bioinformatics/bts092.
3. Attia A, Alexanderian A, Saibaba AK. Goal-Oriented Optimal Design of Experiments for Large-Scale Bayesian Linear Inverse Problems. *Inverse Problems*. 2018;34. doi:10.1088/1361-6420/aad210.
4. Canessa S et al. When do we need more data? A primer on calculating the value of information for applied ecologists. *Methods in Ecology and Evolution*. 2015;6:1219–1228. doi:10.1111/2041-210X.12423.
5. Hurlbert SH. Pseudoreplication and the Design of Ecological Field Experiments. *Ecological Monographs*. 1984;54:187–211. doi:10.2307/1942661.
6. MacKenzie DI et al. Estimating site occupancy rates when detection probabilities are less than one. *Ecology*. 2002;83:2248–2255. doi:10.1890/0012-9658(2002)083[2248:ESORWD]2.0.CO;2.
7. Dormann CF. Calibration of probability predictions from machine-learning and statistical models. *Global Ecology and Biogeography*. 2020;29:760–765. doi:10.1111/geb.13070.
8. Cowans et al. Improving the integration of artificial intelligence into existing ecological inference workflows. *Methods in Ecology and Evolution*. 2026. doi:10.1111/2041-210X.14485.
9. Chen et al. Producing plankton classifiers that are robust to dataset shift. *Limnology and Oceanography: Methods*. 2024/2025. doi:10.1002/lom3.10659.

### Companion/source-manuscript citation placeholders to resolve before submission

- Boundary/C1 — structural identification geometry and diagnostics.
- CED/M3 — target-safe reportability, finite learning-versus-licensing witness and failure-domain result.
- MROD/M2 — prospective observation-design examples, including *Campanula* and island-pollination translation.
- REC — record-entry loss / irreversibility demonstration.
- TNOA/M1 — semantic restraint and representation-change calibration semantics.

These placeholders preserve source ownership. If a companion manuscript is not publicly citable at submission time, replace the placeholder with a self-contained conceptual example or an external published anchor rather than presenting unpublished source results as established literature.
