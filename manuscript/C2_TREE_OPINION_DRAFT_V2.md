# When more measurement is not more evidence: diagnosing four failures in ecology and evolution

**Article type:** Opinion  
**Target:** *Trends in Ecology & Evolution*  
**Status:** preferred full manuscript draft v2; not submission-formatted; source ownership firewalls remain active

## Highlights

- More measurement can fail for four different reasons: geometry, objective, dependence and pipeline.
- Each failure requires a different remedy; more of the same measurement is not a universal solution.
- Sample size, precision, information gain and classifier accuracy are useful but responsibility-specific proxies.
- Measurement design should ask which distinction the next observation must create or preserve.

## Abstract

Ecology and evolution are becoming measurement-rich. Automated sensors, remote sensing, bioacoustics, camera traps, genomic assays, environmental DNA and machine-learning pipelines can increase observation volume, precision and downstream performance at rapidly falling marginal cost. Yet additional measurement does not automatically strengthen evidence for the scientific question being asked. We distinguish four recurrent failures of this monotonic intuition. **Same-dimension failure** occurs when greater precision or repetition measures distinctions already represented and therefore does not separate additional explanations. **Wrong-target failure** occurs when a measurement reveals more about the system overall but less about the prediction or decision of interest. **False-independence failure** occurs when nominal replicates share a common failure domain. **Too-late failure** occurs when information is lost before record creation or when operating semantics are inherited after a representation changes. These failures demand different remedies: measure a new distinction, target the relevant outcome, diversify failure opportunities, or move measurement earlier in the pipeline. We argue that measurement escalation should therefore be **diagnostic-first, not quantity-first**.

## The problem is no longer simply how to collect more data

Ecologists and evolutionary biologists can now measure systems at scales that were recently impractical. Autonomous sensors generate continuous environmental records. Camera traps and microphones collect millions of images and sounds. Genomic and environmental-DNA assays resolve biological variation at extraordinary throughput. Automated phenotyping and machine learning turn raw observations into classifications faster than human observers can inspect them. In many settings, adding another record is becoming easier than deciding whether that record adds the distinction needed for the scientific claim.

A familiar response to uncertainty is still to collect more data. Often that is exactly right. More observations can reduce sampling error, reveal rare states, improve parameter precision and support better predictions. The difficulty is that “more” is not one thing. A study can add more measurements of the same variable, more variables, more information about latent state, more replicates, more accurate classifier outputs, or more processing downstream of observation. These additions are not interchangeable.

Consider four situations. A trait cline is sampled twice as densely, but competing mechanisms still predict the same cline. A genomic assay resolves many additional nuisance states, but none changes the evolutionary hypothesis being tested. Hundreds of samples come from one population, sensor, batch or field window and therefore share the same dominant failure. A biodiversity classifier becomes nearly perfect on retained sequences, but primer or sensor bias removed some biological events before classification. In each case the data set becomes larger or more precise while the decisive scientific distinction remains unchanged.

The practical question is therefore not simply **“how can we measure more?”** It is:

> **What distinction must the next measurement create or preserve for the ecological or evolutionary conclusion to change?**

Several mature literatures already answer parts of this question. Structural-identifiability theory distinguishes model ambiguity from estimation precision [1]. Targeted and goal-oriented experimental design asks whether an observation reduces uncertainty in a declared prediction or quantity of interest rather than in a full parameter vector [2,3]. Value-of-information analysis asks whether resolving uncertainty can improve a decision [4]. Ecologists have long distinguished nominal sample size from independent replication [5]. Occupancy and imperfect-detection models separate latent ecological state from observation [6], while calibration and dataset-shift studies show that numerical model outputs can lose their nominal interpretation when deployment conditions change [7–9].

These traditions are usually taught and applied separately. We connect them through one negative result: **evidence is not monotone in the amount of measurement**. Crucially, there is not one reason for this failure. We distinguish four. Each describes a different way in which an additional observation can fail to become additional evidence, and each points to a different remedy (Figure 1).

This is not an argument against large data sets, replication or accurate models. It is an argument against using their quantity as a universal certificate of evidential progress.

---

## Failure 1: more precision can stay in the same evidential dimension

Suppose two explanations predict the same value for the variable that a study measures. Improving the precision of that variable can narrow confidence intervals indefinitely without separating those explanations. Repeating the same assay, rescaling it, or adding another exact transformation of it may improve estimation while leaving the set of compatible mechanisms unchanged.

This is the distinction between **precision** and **structural identification**. Structural-identifiability theory formalizes whether distinct parameterizations or mechanisms can in principle generate the same observations [1]. The broader lesson is simple: an observation can be measured extremely well and still fail to cut the ambiguity that matters.

In ecology, fruit set can be consistent with many visits of low effectiveness or few visits of high effectiveness. Measuring fruit set more precisely does not itself distinguish those mechanisms. In evolutionary biology, dense measurement of a phenotype can sharpen the trajectory of change without distinguishing evolutionary processes that make the same prediction for that phenotype. More detail along the existing observational axis helps only if that axis was where the unresolved alternatives differed.

The diagnostic is:

> **Does the proposed measurement separate a previously unresolved explanation, or only measure an already represented distinction more accurately?**

If the answer is the latter, the remedy is not necessarily more replication. It is a new distinction. In a pollination system that may be per-visit pollen deposition rather than another count of visits. In a trophic system it may be an interaction or intervention response rather than a denser abundance series. In an evolutionary study it may be a second trait, experimental perturbation or historical contrast that makes alternative processes diverge.

The exact structural geometry and diagnostic conditions for one declared positive log-linear observation class belong to the companion Boundary/C1 paper and are deliberately not reproduced here [Boundary manuscript placeholder]. The Opinion-level lesson is qualitative: **more precision is evidence only when precision was the limiting problem**.

---

## Failure 2: more information can answer the wrong question

Even when a measurement genuinely separates latent states, those distinctions may be irrelevant to the scientific target.

Targeted experiment design makes this familiar. If the scientific responsibility is a forecast, intervention effect, evolutionary contrast or management decision, reducing uncertainty in every parameter or latent state can be less valuable than resolving one distinction that changes the target [2–4]. The same observation can therefore be highly informative about the system and nearly useless for the question at hand.

A finite example makes the mismatch concrete. Imagine eight equally plausible worlds. They differ in a binary target-relevant state and a four-level nuisance attribute. One candidate measurement perfectly reveals the four-level nuisance state. It therefore provides 2 bits of information about full world identity but leaves the binary target unresolved. A second candidate provides only 1 bit about world identity but directly separates the target states. If the objective is full latent-state learning, the first measurement is better. If the responsibility is to license the target distinction, the second is better. No contradiction exists because the objectives are different.

The same issue appears whenever a study quietly switches goals. A biodiversity survey can seek discovery, occupancy estimation and conservation prioritization. A phylogenomic programme can seek topology, timing and a test of a focal evolutionary transition. A restoration project can seek mechanism learning and a yes/no treatment decision. A measurement that strongly improves one responsibility need not improve the others.

The diagnostic is:

> **Can the new distinction change the prediction, classification, evolutionary contrast or decision that the study is responsible for?**

If not, more information may still be scientifically valuable, but it is not stronger evidence for that target. The remedy is **target-relevant measurement**, not information maximization in the abstract.

This does not make broad mechanism learning unimportant. Basic science often has excellent reasons to resolve as much latent structure as possible. The narrower claim is that total entropy reduction, parameter precision or generic model fit should not be treated as if they certify every downstream claim.

---

## Failure 3: more replicates can share the same blind spot

Replication is one of the strongest safeguards in ecology and evolution, but replicate count and evidential independence are not synonyms.

Hurlbert's critique of pseudoreplication made this classical in ecology: observations that share an experimental unit or treatment history cannot be counted as independent treatment replicates [5]. The same logic appears in modern observation systems when measurements share a **failure domain**.

Ten camera images from one obscured camera share a camera-level failure. Ten PCR reads from one failed extraction share an extraction failure. Hundreds of individuals sampled from one population do not replace independent population contrasts when the inferential unit is population-level. Multiple genomic measurements can share library, batch or amplification failures. Repeated classifier evaluations on records produced by one upstream sensor inherit sensor-specific blind spots.

Within a functioning mode, more repeats can improve conditional sensitivity. But they cannot provide the same worst-case protection as observations distributed across independent modes if the dominant risk is common-mode loss. An unlimited number of records behind one shared point of failure can still disappear together.

The design resource is therefore not only replication but **failure diversity**. A programme with fewer nominal observations but more independent opportunities for the focal distinction to survive may provide stronger evidence than a much larger set of repeated reads concentrated inside one fragile mode.

The diagnostic is:

> **Did we add another observation, or another genuinely independent opportunity for the distinction to survive failure?**

If shared dependence is limiting, the remedy is to diversify sensors, sites, populations, observers, batches, time windows or other relevant failure domains. Which domain matters depends on the responsibility being protected.

This also explains why post hoc corrections cannot always substitute for design. Statistical dependence can sometimes be estimated and adjusted. But if every measurement can be jointly erased or distorted by the same upstream event, no reweighting scheme creates an independent observation that was never collected.

---

## Failure 4: better downstream processing can arrive too late

The previous failures concern what a measurement distinguishes, what objective it serves and whether it creates an independent opportunity. The fourth concerns **where in the observation pipeline information is lost**.

Modern ecological and evolutionary observations often pass through many stages: biological opportunity, sensor exposure, record entry, filtering, amplification or detection, classification, thresholding, aggregation and reporting. Improving a late stage does not necessarily repair losses at an earlier one.

The simplest version is imperfect detection. Occupancy modelling formalized the point that nondetection is not absence when detection probability is below one [6]. In digital systems the asymmetry can be sharper. If a biological event never entered the retained record, no downstream classifier—however accurate—can classify that missing event correctly. Better semantics on retained rows cannot recreate absent rows.

The same issue is easy to see in biodiversity sequencing. A taxonomic classifier can be nearly perfect on the sequences it receives while remaining blind to taxa removed earlier by sampling, extraction or amplification. The downstream model may be excellent and the observation system still incomplete for the biological claim.

A complementary problem occurs when records are retained but their numerical representation changes. A threshold that had a particular operating meaning under one representation may lose that meaning after recalibration, domain shift or feature transformation. Calibration work has long emphasized that nominal scores require validation [7], while recent ecological AI work warns against assuming that one confidence threshold has stable meaning across classifiers, species and applications [8,9].

These are related but distinct. One is **irreversible support loss**: the needed event or distinction is no longer present in the record. The other is **operating-semantics drift**: the distinction remains, but the relationship between score and claimed error behaviour has changed.

The remedies differ. Changed semantics can sometimes be repaired by recalibration against a declared error criterion. An omitted event cannot. Recovery then requires independent new information—another sensor, a reference process, an audit sample, an alternative primer or a redesign that moves measurement earlier in the pipeline.

The diagnostic is:

> **Is the distinction we need still present in the retained record?**

If yes, a better downstream model or recalibration may help. If no, downstream accuracy is the wrong investment target. The remedy is to **capture the distinction earlier**.

This matters because headline model performance is usually measured conditional on records that reached the model. A classifier can perform excellently on its evaluation set while the observation system remains biased because relevant opportunities were selectively omitted before classification. Classifier performance and observation-system adequacy are therefore different objects.

---

## The synthesis is a decision rule, not a four-box warning

A taxonomy of failure modes would not justify another conceptual framework. The useful step is to connect each diagnosis to a different next action.

| If the limiting failure is… | Ask… | Then prioritize… |
|---|---|---|
| **same dimension** | Does the next measurement separate a previously unresolved explanation? | a new distinction, not merely more precision |
| **wrong target** | Can the new distinction change the declared prediction or decision? | target-relevant information |
| **shared dependence** | Does the added observation create an independent opportunity for evidence to survive failure? | failure-domain diversity |
| **upstream loss / semantic drift** | Is the needed distinction still present in the retained record? | earlier capture if lost; recalibration if retained |

This is the core proposal: **measurement escalation should be diagnostic-first, not quantity-first**.

The framework also shows why common scalar summaries are useful but incomplete. Sample size is meaningful when sampling variance is limiting. Precision is meaningful when the right dimension is already observed. Entropy reduction is meaningful when the object of entropy matches the scientific responsibility. Replicate number is meaningful when replicates provide relevant independent opportunities. Classifier accuracy is meaningful when the retained records contain the needed support and the operating semantics travel.

None of these quantities is defective. The error is to treat one as a universal proxy for evidential strength.

Figure 1 should therefore be read as a decision map rather than a ranking. We do not claim that every study experiences all four failures, that the four are exhaustive, or that they can be collapsed into one evidence score. The claim is operational: asking **why current evidence is inadequate** gives a better next-measurement decision than asking only **how to collect more**.

---

## Box 1. Island *Campanula*: measure the mechanism-separating trait, not only the cline

Spatial trait clines can be visually compelling yet mechanistically ambiguous. In an island *Campanula* observation-design example, several causal structures can remain compatible with the same coarse spatial pattern. Increasing the number of observations along that pattern improves description of the cline but need not separate the competing explanations.

A more diagnostic design asks which additional trait or interaction produces different predictions under the still-compatible structures. One prospective candidate is a nectar-guide gradient. Its value does not come from being intrinsically more mechanistic or more precise than the original trait. Its value comes from whether the competing structures predict different guide patterns.

This example connects two failure classes. If more sampling only sharpens an already represented cline, the problem is **same dimension**. If a candidate measurement resolves biological detail that does not change the mechanism comparison or focal prediction, the problem is **wrong target**. The preferred observation is the one that separates the live alternatives for the question being asked.

This is a **worked design example, not a new empirical validation claim**. The source programme separates validated structural statements from phenomenological simulation, and coefficient magnitudes chosen for illustration should not be read as field estimates [MROD manuscript placeholder].

---

## Box 2. Island pollination: different questions require different measurements

Island pollination makes the target problem concrete because “pollination” can refer to several different links.

Suppose an island plant shows a change in floral phenotype. At least three questions can follow.

1. **Are different visitors present?** This requires visitor occurrence or visitation composition.
2. **Do those visitors provide effective pollination service?** This requires legitimate contact, pollen transfer or another defensible effectiveness measurement.
3. **Does pollination service change reproductive outcome?** This requires a link from service to seed set, recruitment or another reproductive consequence.

Collecting more data on question 1 cannot substitute for question 2, and question 2 cannot substitute for question 3. A huge camera sample can therefore be excellent evidence for visitation while remaining weak evidence for reproductive consequence. The problem is not low data volume. It is a mismatch between the measured distinction and the scientific responsibility.

The same system can exhibit dependence and pipeline failures. Hundreds of observations from one camera position can share a field-of-view blind spot. A classifier cannot recover visits that never entered the recording window. Thus one biological system can move among the four diagnoses as its question changes.

This is a **translation contract for observation design, not an empirical causal conclusion** [MROD island-pollination translation placeholder].

---

## A measurement contract for ecological and evolutionary studies

A diagnostic-first approach changes reporting as well as design. Methods sections usually describe what was measured and how often, but less often explain **which competing explanations, target states or failure modes each measurement was intended to distinguish**.

Four additions would make evidential claims easier to audit.

**State the scientific responsibility.** Is the measurement intended for mechanism discrimination, prediction, evolutionary comparison, intervention choice, discovery or another target? This prevents generic information gain from being mistaken for target relevance.

**State the live alternatives.** What explanations or target states remain compatible before the new measurement? A new variable becomes evidentially useful relative to alternatives it can separate.

**State the relevant failure domains.** Which observations share sensors, observers, sites, populations, batches, access conditions or other common points of failure? Raw replicate count is not enough.

**Separate retained support from downstream performance.** Which biological opportunities could enter the record, which could be lost before classification, and which performance metric is conditional on survival through those stages?

These additions do not require every paper to become a formal identifiability analysis. They require only that claims about “more evidence” be tied to the distinction the added measurement is expected to create or preserve.

---

## Outstanding questions

### How can failure domains be learned rather than assumed?

Real failure structures are rarely known perfectly. Sensors fail jointly for unexpected reasons, observer biases cluster, populations share history, and nominally independent sites can experience the same disturbance. Methods that infer failure domains prospectively—or diversify them adaptively when dependence is detected—would make the framework more operational.

### How robust is target-relevant measurement to target misspecification?

Targeted measurement is only as useful as the target declaration. Scientific goals can change, management objectives can be contested, and a variable treated as nuisance can become important later. This creates a real tension between efficient target-specific design and preserving optionality. One direction is to pair target-relevant design with an explicit record of which distinctions were intentionally left unresolved.

### When is upstream loss recoverable?

Some pipeline losses are irreversible without new data, but others can be repaired using reference samples, audit subsamples, alternative sensors or calibration data. We need clearer conditions for when a retained record plus an external reference process is sufficient to reconstruct omitted opportunities and when no downstream correction can identify the missing support.

### Can a study move between failure classes over time?

Yes. Early in a programme, structural ambiguity may dominate. After adding a mechanism-separating measurement, target mismatch may become limiting. Once the target is measured, common-mode failure may dominate precision. After automation, pipeline loss can become decisive. The framework is therefore a sequence of diagnoses during the life of an observation system, not a permanent label for a study.

### Are the four failures exhaustive?

No. They are intended as a useful cross-cutting set, not a theorem about every form of evidential failure. Model misspecification, nonstationarity, causal transport, selective reporting, strategic behaviour and ethical constraints can limit evidence in other ways. The practical test is whether a proposed additional measurement fails because it stays in the same distinction, answers the wrong target, shares the same failure, or arrives after the needed information has been lost. If not, another diagnosis is needed.

---

## Conclusion: ask what the next measurement changes

Ecology and evolution do not face one generic data shortage. In many systems the bottleneck is no longer the ability to collect more records. It is deciding **which new distinction would count as evidence for the question at hand**.

Four common intuitions can fail. Greater precision can stay in the same evidential dimension. More latent-state information can answer the wrong target. More replicates can share one blind spot. Better downstream processing can arrive after decisive information has disappeared.

The remedies are correspondingly different: measure a new distinction, measure the target-relevant distinction, diversify failure opportunities, or move observation earlier in the pipeline. None can be replaced by a generic instruction to increase sample size or model performance.

The rule is simple enough to use before designing a study, adding a sensor, sequencing another batch, sampling another population or retraining a classifier:

> **Before collecting more data, ask what distinction the next measurement must create or preserve for the conclusion to change.**

Additional measurement becomes additional evidence only when that answer is explicit.

---

## Figure 1. Diagnostic-first measurement escalation

**Concept:** current evidence does not resolve the ecological or evolutionary question → diagnose the limiting failure → choose a remedy matched to that failure.

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
