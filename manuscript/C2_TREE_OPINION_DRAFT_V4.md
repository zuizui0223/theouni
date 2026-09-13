# When more measurement is not more evidence

**Article type:** Opinion  
**Target:** *Trends in Ecology & Evolution*  
**Status:** preferred manuscript draft v4; self-contained; not yet journal-formatted

## Highlights

- Data quantity is not a universal proxy for evidential progress in ecology or evolution.
- Useful added measurement can require four different properties: separation, relevance, failure diversity and timely preservation.
- Their absence produces four distinct failures: same dimension, wrong target, false independence and too late.
- Diagnosing the limiting property identifies what should be measured next.

## Abstract

Ecology and evolution are becoming measurement-rich. Automated sensors, remote sensing, bioacoustics, camera traps, genomic assays, environmental DNA and machine-learning pipelines can increase observation volume, precision and downstream performance at rapidly falling marginal cost. Yet these quantities are not universal proxies for evidential progress. We connect four recurrent failures of the intuition that “more measurement” should resolve a scientific question. Greater precision can remain in the **same evidential dimension**, more latent-state information can answer the **wrong target**, nominal replicates can share the same failure and create **false independence**, and improved downstream processing can arrive **too late** after the needed distinction has been lost. These are not four versions of the same problem. They diagnose missing properties of an added measurement: separation of live alternatives, relevance to the declared target, diversity of failure opportunities, or preservation of information early enough in the observation pipeline. We propose a four-question screen that maps each diagnosis to a different remedy. Measurement escalation should be **diagnostic-first, not quantity-first**.

## The bottleneck is not always data quantity

Ecologists and evolutionary biologists can now measure systems at scales that were recently impractical. Autonomous sensors generate continuous environmental records. Camera traps and microphones collect millions of images and sounds. Genomic and environmental-DNA assays resolve biological variation at extraordinary throughput. Automated phenotyping and machine learning turn raw observations into classifications faster than human observers can inspect them. In many settings, adding another record is becoming easier than deciding whether that record creates the distinction needed for the scientific claim.

A familiar response to uncertainty is to collect more data. Often that is exactly right. More observations can reduce sampling error, reveal rare states, improve parameter precision and support better predictions. The difficulty is that “more” is not one thing. A study can add more measurements of the same variable, more variables, more information about latent state, more replicates, more accurate classifier outputs, or more processing downstream of observation. These additions are not interchangeable.

Consider four situations. A trait cline is sampled twice as densely, but competing mechanisms still predict the same cline. A genomic assay resolves many additional nuisance states, but none changes the evolutionary contrast being tested. Hundreds of samples come from one population, sensor, batch or field window and therefore share the same dominant failure. A biodiversity classifier becomes nearly perfect on retained sequences, but sampling or amplification bias removed some taxa before classification. In each case the data set becomes larger or more precise while the decisive scientific distinction remains unchanged.

The practical question is therefore not simply **“how can we measure more?”** It is:

> **What distinction must the next measurement create or preserve for the ecological or evolutionary conclusion to change?**

We use **evidential progress** in this operational sense: increased ability to distinguish among live alternatives that matter to a declared scientific claim, using distinctions that the observation process actually preserves. This is deliberately narrower than a general philosophical definition of evidence.

The components of this problem have deep roots. Structural-identifiability theory distinguishes model ambiguity from estimation precision [1]. Targeted and goal-oriented experimental design asks whether an observation reduces uncertainty in a declared prediction or quantity of interest rather than in a full parameter vector [2,3]. Value-of-information analysis asks whether resolving uncertainty can improve a decision [4]. Ecological monitoring has repeatedly argued that data collection should be organized around explicit questions and decisions [5,6]. Ecologists have long distinguished nominal sample size from independent replication [7,8]. Occupancy and species-distribution modelling show why the observation process must be separated from the latent ecological state [9,10]. Calibration, ecological AI and metabarcoding studies show that downstream scores and taxonomic outputs inherit assumptions and losses from earlier stages [11–14].

The opportunity is to connect these traditions through a measurement-design diagnostic. Four common quantities—precision, total information, replicate count and downstream accuracy—can each fail as a proxy for progress, but for different reasons. The missing property may be **separation**, **relevance**, **failure diversity** or **timely preservation**. Identifying which property is missing tells us what kind of measurement could help next (Figure 1).

### A necessary non-harm caveat

Our argument is not that extra information is intrinsically harmful. In an ideal decision problem, a cost-free observation that can simply be ignored need not make an optimal decision worse. Nor do we argue against large data sets, replication or accurate models. The non-monotonicity at issue is a **proxy-to-responsibility mapping**: more sample size, precision, total latent-state information, nominal replication or conditional classifier accuracy does not guarantee more resolution of the claim for which evidence is being collected. Under finite budgets and real pipelines, choosing the wrong form of “more” can therefore spend effort without resolving the limiting uncertainty.

---

## Property 1 — Separation: does the measurement distinguish a live alternative?

### Failure when missing: same dimension

Suppose two explanations predict the same value for the variable that a study measures. Improving the precision of that variable can narrow confidence intervals indefinitely without separating those explanations. Repeating the same assay, rescaling it, or adding another transformation of it may improve estimation while leaving the set of compatible mechanisms unchanged.

This is the distinction between **precision** and **structural identification**. Structural-identifiability theory formalizes whether distinct parameterizations or mechanisms can in principle generate the same observations [1]. The broader lesson is simple: an observation can be measured extremely well and still fail to cut the ambiguity that matters.

In ecology, fruit set can be consistent with many visits of low effectiveness or few visits of high effectiveness. Measuring fruit set more precisely does not itself distinguish those mechanisms. In evolutionary biology, dense measurement of a phenotype can sharpen the trajectory of change without distinguishing processes that make the same prediction for that phenotype. More detail along the existing observational axis helps only if that axis is where the unresolved alternatives differ.

The diagnostic question is:

> **Does the proposed measurement separate a previously unresolved explanation, or only measure an already represented distinction more accurately?**

If the answer is the latter, the remedy is not necessarily more replication. It is a new distinction. In a pollination system that may be per-visit pollen deposition rather than another visit count. In a trophic system it may be an interaction or intervention response rather than a denser abundance series. In an evolutionary study it may be a second trait, experimental perturbation or historical contrast that makes alternative processes diverge.

The point is qualitative: **more precision is evidential progress only when precision was the limiting problem**. When unresolved explanations remain observationally equivalent, another kind of measurement is required.

---

## Property 2 — Relevance: can the distinction change the declared target?

### Failure when missing: wrong target

A measurement can genuinely separate latent states and still be irrelevant to the scientific responsibility.

Targeted experimental design makes this familiar. If the responsibility is a forecast, intervention effect, evolutionary contrast or management decision, reducing uncertainty in every parameter or latent state can be less valuable than resolving one distinction that changes the target [2–4]. The same observation can therefore be highly informative about the system and almost useless for the question at hand.

A finite example makes the mismatch concrete. Imagine eight equally plausible worlds. They differ in a binary target-relevant state and a four-level nuisance attribute. Under a fixed budget that allows one next measurement, one candidate perfectly reveals the four-level nuisance state. It therefore provides 2 bits of information about full world identity but leaves the binary target unresolved. A second candidate provides only 1 bit about world identity but directly separates the target states. If the objective is full latent-state learning, the first measurement is better. If the responsibility is target resolution, the second is better. No contradiction exists because the objectives are different.

The same issue appears whenever a study quietly switches goals. A biodiversity survey can seek discovery, occupancy estimation and conservation prioritization. A phylogenomic programme can seek topology, timing and a test of a focal evolutionary transition. A restoration project can seek mechanism learning and a yes/no treatment decision. An observation that strongly improves one responsibility need not improve the others.

The diagnostic question is:

> **Can the new distinction change the prediction, classification, evolutionary contrast or decision that the study is responsible for?**

If not, more information may still be scientifically valuable, but it is not stronger evidence for that target. The remedy is **target-relevant measurement**, not information maximization in the abstract.

This does not make broad mechanism learning unimportant. Basic science often has excellent reasons to resolve latent structure. The narrower claim is that total entropy reduction, parameter precision or generic model fit should not be treated as if they certify every downstream conclusion. Monitoring theory reaches the same practical conclusion from another direction: information gathering becomes most useful when its role in learning or decision making is explicit [5,6].

---

## Property 3 — Failure diversity: is this a genuinely new opportunity for evidence to survive?

### Failure when missing: false independence

Replication is one of the strongest safeguards in ecology and evolution, but replicate count and evidential independence are not synonyms.

Hurlbert's critique of pseudoreplication made this classical in ecology: observations that share an experimental unit or treatment history cannot be counted as independent treatment replicates [7]. The same principle remains central in contemporary experimental design, where the correct scale of replication depends on the scale at which inference is sought [8]. Modern observation systems add another version of the problem: measurements can share a **failure domain** even when they are numerically or temporally distinct.

Ten camera images from one obscured camera share a camera-level failure. Ten PCR reads from one failed extraction share an extraction failure. Hundreds of individuals sampled from one population do not replace independent population contrasts when the inferential unit is population-level. Multiple genomic measurements can share library, batch or amplification failures. Repeated classifier evaluations on records produced by one upstream sensor inherit sensor-specific blind spots.

Within a functioning mode, more repeats can improve conditional sensitivity. But they cannot provide the same protection as observations distributed across independent modes if the dominant risk is common-mode loss. An unlimited number of records behind one shared point of failure can still disappear together.

The design resource is therefore not only replication but **failure diversity**. A programme with fewer nominal observations but more independent opportunities for the focal distinction to survive may provide stronger support for a claim than a much larger set of repeated reads concentrated inside one fragile mode.

The diagnostic question is:

> **Did we add another observation, or another genuinely independent opportunity for the distinction to survive failure?**

If shared dependence is limiting, the remedy is to diversify sensors, sites, populations, observers, batches, time windows or other relevant failure domains. Which domain matters depends on the responsibility being protected.

This is not a license to label every dependent data set invalid. Dependence can often be modelled, and ecological work has rightly warned against dogmatic uses of pseudoreplication arguments. The narrower design claim is that statistical adjustment cannot retroactively create an independent biological or technical opportunity that was never sampled. Design and analysis answer different parts of the problem.

---

## Property 4 — Timely preservation: is the needed distinction still available downstream?

### Failure when missing: too late

Modern ecological and evolutionary observations often pass through many stages: biological opportunity, sensor exposure or sampling, record entry, extraction, amplification or detection, classification, thresholding, aggregation and reporting. Improving a late stage does not necessarily repair losses at an earlier one.

The simplest version is imperfect detection. Occupancy modelling formalized the point that nondetection is not absence when detection probability is below one [9]. Species-distribution studies have shown that ignoring detectability can damage both calibration and inference about the underlying distribution [10]. In digital systems the asymmetry can be sharper. If a biological event never entered the retained record, no downstream classifier—however accurate—can classify that missing event correctly. Better semantics on retained rows cannot recreate absent rows.

The same logic is visible in biodiversity sequencing. A taxonomic classifier can be excellent on the sequences it receives while remaining blind to taxa removed earlier by field sampling, DNA degradation, extraction, primer mismatch or amplification bias. Metabarcoding workflows therefore require attention to errors and biases at multiple stages, not only final taxonomic assignment [13]. The downstream model may be excellent while the observation system remains incomplete for the biological claim.

A complementary problem occurs when records are retained but their numerical representation changes. A threshold that had a particular operating meaning under one representation may lose that meaning after recalibration, domain shift or feature transformation. Calibration work shows that nominal probabilities cannot simply be assumed to have their stated probabilistic meaning [11]. Ecological AI work similarly emphasizes that classifier confidence, misclassification and ecological inference must be connected explicitly across the data-to-inference pipeline [12], while deployment studies show how nominal classifier performance can fall under dataset shift [14].

These are related but distinct. One is **irreversible support loss**: the needed event or distinction is no longer present in the record. The other is **operating-semantics drift**: the distinction remains, but the relationship between a score and the error behaviour assigned to that score has changed.

The remedies differ. Changed semantics can sometimes be repaired by recalibration against a declared criterion. An omitted event cannot. Recovery then requires independent new information—another sensor, a reference process, an audit sample, an alternative primer or a redesign that moves measurement earlier in the pipeline.

The diagnostic question is:

> **Is the distinction we need still present in the retained record?**

If yes, a better downstream model or recalibration may help. If no, downstream accuracy is the wrong investment target. The remedy is to **capture the distinction earlier**.

This matters because headline model performance is usually measured conditional on records that reached the model. A classifier can perform excellently on its evaluation set while the observation system remains biased because relevant opportunities were selectively omitted before classification. Classifier performance and observation-system adequacy are therefore different objects.

---

## A four-question screen for the next measurement

The four failures can now be stated positively as four properties that may be missing from a proposed measurement.

| Property needed | Diagnostic question | Failure if absent | Remedy |
|---|---|---|---|
| **separation** | Does it separate a live alternative? | same dimension | measure a new distinction |
| **relevance** | Can that distinction change the declared target? | wrong target | measure target-relevant information |
| **failure diversity** | Does it add an independent opportunity for the distinction to survive? | false independence | diversify failure domains |
| **timely preservation** | Is the needed distinction still present at the stage being improved? | too late | capture earlier, or recalibrate if still retained |

This table is not a necessary-and-sufficient theorem for all evidence. Not every study needs all four checks to the same degree, and other evidential problems exist. It is a practical screen for a common decision: **what should we measure next?**

The screen also clarifies why common scalar summaries are useful but incomplete. Sample size is meaningful when sampling variance is limiting. Precision is meaningful when the right distinction is already observed. Information gain is meaningful when the object of information matches the scientific responsibility. Replicate number is meaningful when replicates provide relevant independent opportunities. Classifier accuracy is meaningful when the retained records contain the needed support and the operating semantics travel.

None of these quantities is defective. The mistake is to treat one as a universal proxy for evidential strength.

The resulting principle is therefore straightforward:

> **Measurement escalation should be diagnostic-first, not quantity-first.**

---

## Box 1. Island *Campanula*: measure the mechanism-separating trait, not only the cline

Consider a prospective island *Campanula* study in which a floral trait varies geographically and several explanations can generate the same coarse cline: abiotic filtering, pollinator-mediated selection, demographic history, or combinations of them. Increasing the number of trait measurements along that cline can improve its description without separating the explanations.

A diagnostic design instead asks which additional observation would make the live alternatives predict different outcomes. A nectar-guide phenotype could be one such measurement if pollinator-mediated explanations predict a guide pattern that purely abiotic or demographic explanations do not. The value of the new measurement would not come from being intrinsically “more mechanistic.” It would come from the alternative explanations it separates.

This prospective example links separation and relevance. If more sampling only sharpens the original cline, the missing property is **separation**. If a new variable reveals biological detail that does not change the focal mechanism comparison, the missing property is **relevance**. The preferred observation is the one that separates the live alternatives for the declared question.

The example is intentionally a **worked design example, not a new empirical validation claim**.

---

## Box 2. Island pollination: different questions require different measurements

Island pollination makes relevance concrete because “pollination” can refer to several links in a causal chain.

Suppose an island plant shows a change in floral phenotype. At least three questions can follow.

1. **Are different visitors present?** This requires visitor occurrence or visitation composition.
2. **Do those visitors provide effective pollination service?** This requires legitimate contact, pollen transfer or another defensible effectiveness measurement.
3. **Does pollination service change reproductive outcome?** This requires a link from service to seed set, recruitment or another reproductive consequence.

Collecting more data on question 1 cannot substitute for question 2, and question 2 cannot substitute for question 3. A huge camera sample can therefore be excellent evidence for visitation while remaining weak evidence for reproductive consequence. The problem is not low data volume. It is a mismatch between the measured distinction and the scientific responsibility.

The same system can exhibit the other missing properties. Hundreds of observations from one camera position can share a field-of-view blind spot, reducing failure diversity. A classifier cannot recover visits that never entered the recording window, revealing a timely-preservation problem. Thus one biological system can move among the four diagnoses as its question and observation architecture change.

This is a **translation contract for observation design, not an empirical causal conclusion**.

---

## A measurement contract for ecological and evolutionary studies

A diagnostic-first approach changes reporting as well as design. Methods sections usually describe what was measured and how often, but less often explain **which competing explanations, target states or failure modes each measurement was intended to distinguish**. This gap echoes long-standing calls to design monitoring around explicit questions and decisions [5,6].

Four additions would make claims about measurement adequacy easier to audit.

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

### When do the four properties conflict?

A design that maximizes separation may be expensive, fragile or poorly targeted. A highly target-specific measurement may sacrifice information useful for future questions. Diversifying failure domains may reduce within-mode replication. Moving observation earlier in a pipeline may increase annotation or storage burden. The next step is therefore not to maximize four scores independently, but to understand trade-offs among the properties under explicit scientific and resource constraints.

### Can a study move between failure classes over time?

Yes. Early in a programme, lack of separation may dominate. After adding a mechanism-separating measurement, target mismatch may become limiting. Once the target is measured, shared failure can dominate. After automation, pipeline loss can become decisive. The framework is therefore a sequence of diagnoses during the life of an observation system, not a permanent label for a study.

### Are the four failures exhaustive?

No. They are intended as a useful cross-cutting set, not a theorem about every form of evidential failure. Model misspecification, nonstationarity, causal transport, selective reporting, strategic behaviour and ethical constraints can limit evidence in other ways. The four-question screen is useful when the bottleneck concerns what an added measurement distinguishes, whether the distinction matters, whether it survives independent failure opportunities, or whether it is still available downstream. If none fits, another diagnosis is needed.

---

## Conclusion: ask what the next measurement changes

Ecology and evolution do not face one generic data shortage. In many systems the bottleneck is no longer the ability to collect more records. It is deciding **which new distinction would count as evidence for the question at hand**.

Four common quantities can fail as proxies for that progress. Greater precision can stay in the same evidential dimension. More latent-state information can answer the wrong target. More replicates can share one blind spot. Better downstream processing can arrive after decisive information has disappeared.

The positive formulation is more useful. Ask whether the next measurement adds **separation**, **relevance**, **failure diversity** or **timely preservation**. The answer identifies whether to measure a new distinction, target the question more directly, diversify observation modes, or move measurement earlier in the pipeline.

The rule is simple enough to use before designing a study, adding a sensor, sequencing another batch, sampling another population or retraining a classifier:

> **Before collecting more data, ask what distinction the next measurement must create or preserve for the conclusion to change.**

Additional measurement becomes additional evidence for a declared claim only when the limiting evidential property is addressed.

---

## Figure 1. From more measurement to more evidence: a four-question screen

Start with a study whose current evidence does not resolve its ecological or evolutionary question. For a proposed additional measurement, ask:

1. **Separation:** does it separate a live alternative? If not → measure a new distinction.
2. **Relevance:** can the separated alternative change the declared target? If not → redirect measurement to target-relevant information.
3. **Failure diversity:** does it create an independent opportunity for the distinction to survive? If not → diversify failure domains rather than only replicate.
4. **Timely preservation:** is the needed distinction still present at the stage being improved? If not → capture earlier; if retained but semantics changed → recalibrate.

The screen is diagnostic, not a universal evidence score and not an exhaustive theory of evidence.

---

## References

1. Villaverde AF, Barreiro A, Papachristodoulou A. Structural Identifiability of Dynamic Systems Biology Models. *PLoS Computational Biology*. 2016;12(10):e1005153. doi:10.1371/journal.pcbi.1005153.
2. Vanlier J, Tiemann CA, Hilbers PAJ, van Riel NAW. A Bayesian approach to targeted experiment design. *Bioinformatics*. 2012;28(8):1136–1142. doi:10.1093/bioinformatics/bts092.
3. Attia A, Alexanderian A, Saibaba AK. Goal-Oriented Optimal Design of Experiments for Large-Scale Bayesian Linear Inverse Problems. *Inverse Problems*. 2018;34(9):095009. doi:10.1088/1361-6420/aad210.
4. Canessa S, Guillera-Arroita G, Lahoz-Monfort JJ, Southwell DM, Armstrong DP, Chades I, Lacy RC, Converse SJ. When do we need more data? A primer on calculating the value of information for applied ecologists. *Methods in Ecology and Evolution*. 2015;6(10):1219–1228. doi:10.1111/2041-210X.12423.
5. Nichols JD, Williams BK. Monitoring for conservation. *Trends in Ecology & Evolution*. 2006;21(12):668–673. doi:10.1016/j.tree.2006.08.007.
6. Lindenmayer DB, Likens GE. Adaptive monitoring: a new paradigm for long-term research and monitoring. *Trends in Ecology & Evolution*. 2009;24(9):482–486. doi:10.1016/j.tree.2009.03.005.
7. Hurlbert SH. Pseudoreplication and the Design of Ecological Field Experiments. *Ecological Monographs*. 1984;54(2):187–211. doi:10.2307/1942661.
8. Marshall DJ. Principles of experimental design for ecology and evolution. *Ecology Letters*. 2024;27:e14400. doi:10.1111/ele.14400. (See published correction: doi:10.1111/ele.70124.)
9. MacKenzie DI, Nichols JD, Lachman GB, Droege S, Royle JA, Langtimm CA. Estimating site occupancy rates when detection probabilities are less than one. *Ecology*. 2002;83(8):2248–2255. doi:10.1890/0012-9658(2002)083[2248:ESORWD]2.0.CO;2.
10. Lahoz-Monfort JJ, Guillera-Arroita G, Wintle BA. Imperfect detection impacts the performance of species distribution models. *Global Ecology and Biogeography*. 2014;23(4):504–515. doi:10.1111/geb.12138.
11. Dormann CF. Calibration of probability predictions from machine-learning and statistical models. *Global Ecology and Biogeography*. 2020;29(4):760–765. doi:10.1111/geb.13070.
12. Cowans A, Lambin X, Hare D, Sutherland C. Improving the integration of artificial intelligence into existing ecological inference workflows. *Methods in Ecology and Evolution*. 2026;17(2):228–237. doi:10.1111/2041-210X.14485. First published online 26 December 2024.
13. Alberdi A, Aizpurua O, Gilbert MTP, Bohmann K. Scrutinizing key steps for reliable metabarcoding of environmental samples. *Methods in Ecology and Evolution*. 2018;9(1):134–147. doi:10.1111/2041-210X.12849.
14. Chen C, Kyathanahally SP, Reyes M, Merkli S, Merz E, Francazi E, Hoege M, Pomati F, Baity-Jesi M. Producing plankton classifiers that are robust to dataset shift. *Limnology and Oceanography: Methods*. 2025;23(1):39–66. doi:10.1002/lom3.10659.
