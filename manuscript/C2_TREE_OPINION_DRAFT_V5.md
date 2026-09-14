# When more measurement is not more evidence

**Article type:** Opinion  
**Target:** *Trends in Ecology & Evolution*  
**Status:** preferred manuscript draft v5; self-contained; cross-domain; not yet journal-formatted

## Highlights

- Data quantity is not a universal proxy for evidential progress in ecology or evolution.
- Measurement becomes evidence through distinct interfaces: preservation, separation, relevance and failure diversity.
- Different bottlenecks require different remedies; more of the same measurement can leave the limiting distinction unresolved.
- Ecological measurement design should shift from quantity-first data acquisition toward diagnostic distinction design.

## Abstract

Ecology and evolution are becoming measurement-rich. Automated sensors, remote sensing, bioacoustics, camera traps, genomic assays, environmental DNA and machine-learning pipelines can increase observation volume, precision and downstream performance at rapidly falling marginal cost. Yet these quantities are not universal proxies for evidential progress. We argue that an added measurement becomes useful evidence for a declared claim only through several distinct interfaces. The needed biological distinction must be **preserved** by the observation pipeline, the measurement must **separate** live alternatives, the separated alternatives must be **relevant** to the scientific target, and repeated support must contain sufficient **failure diversity** for the distinction not to depend on one shared point of failure. Missing these properties produces four recurrent failures: too late, same dimension, wrong target and false independence. These failures are not interchangeable and therefore do not share a generic remedy. We propose a four-question measurement-to-evidence screen that diagnoses which interface is limiting and what kind of observation should be added next. The practical shift is from quantity-first data acquisition to **diagnostic distinction design**.

## The bottleneck is not always data quantity

Ecologists and evolutionary biologists can now measure systems at scales that were recently impractical. Autonomous sensors generate continuous environmental records. Camera traps and microphones collect millions of images and sounds. Genomic and environmental-DNA assays resolve biological variation at extraordinary throughput. Automated phenotyping and machine learning turn raw observations into classifications faster than human observers can inspect them. In many settings, adding another record is becoming easier than deciding whether that record creates the distinction needed for the scientific claim.

A familiar response to uncertainty is to collect more data. Often that is exactly right. More observations can reduce sampling error, reveal rare states, improve parameter precision and support better predictions. The difficulty is that “more” is not one thing. A study can add more measurements of the same variable, more variables, more information about latent state, more nominal replicates, more accurate classifier outputs, or more processing downstream of observation. These additions act at different parts of the measurement-to-evidence process and are not interchangeable.

Consider four situations. A trait cline is sampled twice as densely, but competing mechanisms still predict the same cline. A genomic assay resolves many additional nuisance states, but none changes the evolutionary contrast being tested. Hundreds of samples come from one population, sensor, batch or field window and therefore share the same dominant failure. A biodiversity classifier becomes nearly perfect on retained sequences, but sampling or amplification bias removed some taxa before classification. In each case the data set becomes larger or more precise while the decisive scientific distinction remains unchanged.

The practical question is therefore not simply **“how can we measure more?”** It is:

> **What distinction must the next measurement create or preserve for the ecological or evolutionary conclusion to change?**

We use **evidential progress** in this operational sense: increased ability to distinguish among live alternatives that matter to a declared scientific claim, using distinctions that the observation process actually preserves. This is deliberately narrower than a general philosophical definition of evidence.

The components of this problem have deep roots. Structural-identifiability theory distinguishes model ambiguity from estimation precision [1]. Targeted and goal-oriented experimental design asks whether an observation reduces uncertainty in a declared prediction or quantity of interest rather than in a full parameter vector [2,3]. Value-of-information analysis asks whether resolving uncertainty can improve a decision [4]. Ecological monitoring has repeatedly argued that data collection should be organized around explicit questions and decisions [5,6]. Ecologists have long distinguished nominal sample size from independent replication [7,8]. Occupancy and species-distribution modelling show why the observation process must be separated from the latent ecological state [9,10]. Calibration, ecological AI and metabarcoding studies show that downstream scores and taxonomic outputs inherit assumptions and losses from earlier stages [11–14].

The opportunity is to connect these traditions through a common measurement-design problem. Data must travel from biological opportunity to retained record, from record to distinguishable alternatives, and from those distinctions to the scientific claim. Repeated support must also be protected against shared failure. We therefore distinguish four properties of useful added measurement: **timely preservation**, **separation**, **relevance** and **failure diversity**. Their absence yields four different bottlenecks and four different remedies (Figure 1).

### A necessary non-harm caveat

Our argument is not that extra information is intrinsically harmful. In an ideal decision problem, a cost-free observation that can simply be ignored need not make an optimal decision worse. Nor do we argue against large data sets, replication or accurate models. The failure is in the **proxy-to-responsibility mapping**: more sample size, precision, total latent-state information, nominal replication or conditional classifier accuracy does not guarantee more resolution of the claim for which evidence is being collected. Under finite budgets and real observation pipelines, choosing the wrong form of “more” can therefore consume effort while leaving the limiting uncertainty untouched.

## From measurement to evidence: four interfaces, not one quantity

A useful way to see the problem is as a set of interfaces rather than a list of warnings.

First, a biologically relevant difference must survive long enough to become a retained observation. We call this **timely preservation**. Second, the retained measurement must differ across the live alternatives that remain scientifically plausible. This is **separation**. Third, that difference must matter for the declared prediction, contrast, classification or decision. This is **relevance**. Finally, when support is replicated, it must not depend entirely on one shared point of failure. This is **failure diversity**.

These properties are not a linear checklist in which one number can summarize the whole chain. Failure diversity can apply at several stages, and relevance is defined by the scientific responsibility rather than by pipeline order. The point is that each property answers a different question. A study can be excellent on three interfaces and still fail at the fourth.

This view also explains why familiar performance summaries can be locally useful yet globally misleading. Precision concerns uncertainty conditional on what was measured. Information gain concerns what was learned, but not necessarily whether it matters to the target. Replicate number counts observations, but not necessarily independent opportunities for a distinction to survive. Classifier accuracy describes performance on records that reached the classifier, not necessarily the adequacy of the upstream observation system. None is a universal proxy for evidence.

Our position is therefore stronger than “collect better data” but narrower than a general theory of evidence:

> **Ecological and evolutionary measurement design should be organized around the flow of distinctions required by the claim, not around data volume alone.**

The four interfaces provide a way to audit that flow.

---

## Interface 1 — Separation: does the measurement distinguish a live alternative?

### Failure when missing: same dimension

Suppose two explanations predict the same value for the variable that a study measures. Improving the precision of that variable can narrow confidence intervals indefinitely without separating those explanations. Repeating the same assay, rescaling it, or adding another transformation of it may improve estimation while leaving the set of compatible mechanisms unchanged.

This is the distinction between **precision** and **structural identification**. Structural-identifiability theory formalizes whether distinct parameterizations or mechanisms can in principle generate the same observations [1]. The broader lesson is simple: an observation can be measured extremely well and still fail to cut the ambiguity that matters.

In ecology, fruit set can be consistent with many visits of low effectiveness or few visits of high effectiveness. Measuring fruit set more precisely does not itself distinguish those mechanisms. In evolutionary biology, dense measurement of a phenotype can sharpen the trajectory of change without distinguishing processes that make the same prediction for that phenotype. More detail along the existing observational axis helps only if that axis is where the unresolved alternatives differ.

The diagnostic question is:

> **Does the proposed measurement separate a previously unresolved explanation, or only measure an already represented distinction more accurately?**

If the answer is the latter, the remedy is not necessarily more replication. It is a new distinction. In a pollination system that may be per-visit pollen deposition rather than another visit count. In a trophic system it may be an interaction or intervention response rather than a denser abundance series. In an evolutionary study it may be a second trait, experimental perturbation or historical contrast that makes alternative processes diverge.

The point is qualitative: **more precision is evidential progress only when precision was the limiting problem**. When unresolved explanations remain observationally equivalent, another kind of measurement is required.

---

## Interface 2 — Relevance: can the distinction change the declared target?

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

## Interface 3 — Failure diversity: is this a genuinely new opportunity for evidence to survive?

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

## Interface 4 — Timely preservation: is the needed distinction still available downstream?

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

## A four-question distinction-flow audit

The four failures can now be stated positively as four interfaces that may limit a proposed measurement.

| Interface | Diagnostic question | Failure if absent | Remedy |
|---|---|---|---|
| **separation** | Does it separate a live alternative? | same dimension | measure a new distinction |
| **relevance** | Can that distinction change the declared target? | wrong target | measure target-relevant information |
| **failure diversity** | Does it add an independent opportunity for the distinction to survive? | false independence | diversify failure domains |
| **timely preservation** | Is the needed distinction still present at the stage being improved? | too late | capture earlier, or recalibrate if still retained |

This audit is not a necessary-and-sufficient theorem for all evidence. Not every study needs all four checks to the same degree, and other evidential problems exist. It is a practical screen for a common design decision: **what should we measure next?**

A useful workflow follows.

1. **Declare the responsibility.** What prediction, contrast, mechanism claim or decision must the study support?
2. **List the live alternatives.** Which explanations or target states remain compatible with current evidence?
3. **Trace the distinction.** Where in the observation pipeline could those alternatives first produce a measurable difference, and can that difference survive to the retained record?
4. **Audit failure domains.** Are repeated observations genuinely independent opportunities for the relevant distinction to survive?
5. **Add measurement where the bottleneck is.** Improve precision only when precision is limiting; otherwise change the measured distinction, the target alignment, the failure architecture or the observation stage.

The workflow changes the unit of design from records to **distinctions**. A million additional observations can be valuable, but their value comes from what they resolve or preserve, not from their count alone.

The screen also clarifies why common scalar summaries are useful but incomplete. Sample size is meaningful when sampling variance is limiting. Precision is meaningful when the right distinction is already observed. Information gain is meaningful when the object of information matches the scientific responsibility. Replicate number is meaningful when replicates provide relevant independent opportunities. Classifier accuracy is meaningful when the retained records contain the needed support and the operating semantics travel.

None of these quantities is defective. The mistake is to treat one as a universal proxy for evidential strength.

> **Measurement escalation should be diagnostic-first, not quantity-first.**

---

## Box 1. Island *Campanula*: measure the mechanism-separating trait, not only the cline

Consider a prospective island *Campanula* study in which a floral trait varies geographically and several explanations can generate the same coarse cline: abiotic filtering, pollinator-mediated selection, demographic history, or combinations of them. Increasing the number of trait measurements along that cline can improve its description without separating the explanations.

A diagnostic design instead asks which additional observation would make the live alternatives predict different outcomes. A nectar-guide phenotype could be one such measurement if pollinator-mediated explanations predict a guide pattern that purely abiotic or demographic explanations do not. The value of the new measurement would not come from being intrinsically “more mechanistic.” It would come from the alternative explanations it separates.

This prospective example links separation and relevance. If more sampling only sharpens the original cline, the missing interface is **separation**. If a new variable reveals biological detail that does not change the focal mechanism comparison, the missing interface is **relevance**. The preferred observation is the one that separates the live alternatives for the declared question.

The example is intentionally a **worked design example, not a new empirical validation claim**.

---

## Box 2. Metabarcoding: improve the interface that lost the taxon

Consider an environmental-DNA or metabarcoding survey in which a focal taxon is absent from the final taxonomic table. A natural response is to improve the classifier or sequence more deeply. That may help—but only if the relevant sequence entered the retained pool.

The focal taxon could have been lost at several earlier interfaces: the field sample may not have contained its DNA; extraction may have failed; a primer may have amplified it poorly; library preparation may have removed it; or the sequence may have entered the retained pool but been misclassified. These possibilities imply different remedies [13].

The distinction-flow audit separates them. If the taxon's sequence is present but classifier probabilities no longer have a stable operating meaning, recalibration or a better classifier can improve the downstream interface [11,12,14]. If the sequence was never amplified, no classifier can recover it. The relevant intervention is then upstream: an alternative primer, a reference assay, independent extraction or another sampling route.

Failure diversity matters as well. Thousands of reads from one extraction are not thousands of independent opportunities to survive an extraction-level failure. Replication across extraction, primer or sampling modes may add more protection than deeper sequencing inside one mode when common-mode loss is the bottleneck.

The lesson is not that sequencing depth or classifier quality is unimportant. It is that each acts on a particular interface. **The correct investment target is the interface at which the biologically relevant distinction is being lost.**

This is a worked design illustration based on established metabarcoding and ecological-inference problems, not a new empirical benchmark.

---

## What this stance changes

A conceptual framework matters only if it changes practice. The distinction-flow view makes three concrete demands.

### 1. Design reports should name the limiting interface

Statements such as “we need more data” or “classifier performance must improve” are incomplete. Authors should specify whether the current limitation is failure to preserve an event, failure to separate alternatives, failure to align with the declared target, or vulnerability to shared failure. This makes the proposed remedy inspectable.

### 2. Benchmarks should follow the scientific responsibility through the pipeline

A downstream benchmark can be excellent while an upstream observation process fails. Where feasible, studies should report where relevant biological opportunities can be lost and which performance metric is conditional on having reached the evaluated stage. This is especially important in sensor, imaging, acoustic, genomic and environmental-DNA workflows.

### 3. Additional measurement should compete against alternative measurement

The relevant design comparison is rarely “more versus less” of one quantity. It is often “more of the current measurement versus a different measurement that attacks another interface.” Budget allocation should therefore compare observation candidates by the distinctions they create or preserve for the declared claim.

These demands turn the framework from a taxonomy into a prospective research programme. They can be tested by asking whether diagnosis-guided additions outperform quantity-matched additions in resolving predeclared ecological or evolutionary targets.

## Predictions for a distinction-design research programme

The framework suggests several empirical expectations rather than claiming universal laws.

First, when separation is the limiting interface, increasing same-variable precision should show diminishing or zero gains in discriminating predeclared alternatives, whereas a cross-modal or mechanism-separating measurement can create a discontinuous gain in target resolution. Second, when shared failure dominates, adding records within one failure domain should improve conditional precision more than robustness to common-mode loss, while adding independent modes should have the opposite pattern. Third, where upstream support loss is substantial, downstream model accuracy should overstate observation-system adequacy when evaluated only on retained records. Fourth, the best added measurement should depend on the declared responsibility: designs optimized for mechanism discovery, target prediction and management choice need not rank candidate observations identically.

These expectations are directly testable with prospective design comparisons, simulation studies with known truth, and monitoring systems that retain reference channels or audit samples. A useful next step is therefore not to prove that “more data can fail” in the abstract, but to test whether **diagnosing the missing interface predicts which design intervention produces the largest gain for a predeclared claim**.

## A measurement contract for ecological and evolutionary studies

The four interfaces can be expressed as a compact measurement contract before data collection or expansion:

1. **Responsibility:** what exact scientific statement, prediction, contrast or decision is the evidence meant to support?
2. **Live alternatives:** which states or explanations are still compatible with what is already known?
3. **Separation:** what candidate observation differs across those alternatives?
4. **Preservation:** can the observation process retain that difference through sampling, sensing, extraction, classification and aggregation?
5. **Failure structure:** which observations share failure domains, and where are independent opportunities created?
6. **Decision rule:** what result from the new observation would change the conclusion or next action?

This contract need not become a bureaucratic checklist. Its purpose is to make hidden substitutions visible. If “more samples” quietly substitutes for a new mechanism-separating observation, the contract exposes it. If “higher classifier accuracy” substitutes for an audit of missed recording opportunities, the contract exposes it. If “more information” substitutes for information relevant to the declared target, the contract exposes it.

The same logic applies across natural-history sampling, experiments, biodiversity monitoring, comparative studies, population genomics, automated sensing and model-based decision support. The details differ; the measurement-to-evidence interfaces do not.

## Outstanding questions

### How should the four interfaces be quantified without collapsing them into one score?

A central research problem is to develop diagnostics for each property while preserving their differences. Separation may be represented through structural distinguishability or expected discrimination among alternatives. Relevance may be expressed through target resolution, predictive utility or value of information. Failure diversity requires explicit dependence or common-mode structure. Timely preservation requires models of the observation pipeline and its loss states. A useful framework should allow these to be compared without pretending they are commensurable.

### How should trade-offs among interfaces be optimized?

A design that maximizes separation may be expensive, fragile or poorly targeted. A highly target-specific measurement may sacrifice information useful for future questions. Diversifying failure domains may reduce within-mode replication. Moving observation earlier in a pipeline may increase annotation or storage burden. The next step is therefore not to maximize four scores independently, but to understand trade-offs among the interfaces under explicit scientific and resource constraints.

### Can diagnosis improve prospective design decisions?

This is the most important empirical test of the proposal. In studies with a predeclared target and several candidate expansions, can researchers diagnose the limiting interface before collecting new data, and does the remedy matched to that diagnosis outperform an equal-cost quantity-first expansion? Such tests would turn the framework from a conceptual synthesis into a falsifiable design doctrine.

### Can a study move between failure classes over time?

Yes. Early in a programme, lack of separation may dominate. After adding a mechanism-separating measurement, target mismatch may become limiting. Once the target is measured, shared failure can dominate. After automation, pipeline loss can become decisive. The framework is therefore a sequence of diagnoses during the life of an observation system, not a permanent label for a study.

### Are the four failures exhaustive?

No. They are intended as a useful cross-cutting set, not a theorem about every form of evidential failure. Model misspecification, nonstationarity, causal transport, selective reporting, strategic behaviour and ethical constraints can limit evidence in other ways. The four-question audit is useful when the bottleneck concerns what an added measurement distinguishes, whether the distinction matters, whether it survives independent failure opportunities, or whether it is still available downstream. If none fits, another diagnosis is needed.

---

## Conclusion: design distinctions, not just data volume

Ecology and evolution do not face one generic data shortage. In many systems the bottleneck is no longer the ability to collect more records. It is deciding **which new distinction would count as evidence for the question at hand**.

The measurement-to-evidence view identifies four interfaces at which an added observation can fail to help: the relevant difference can be lost before it reaches the record, the retained measurement may not separate live alternatives, the separated alternatives may not matter to the declared target, or repeated support may share one dominant point of failure.

The positive formulation is more useful. Preserve the distinction, separate the alternatives, align the measurement with the target and diversify the failure opportunities. These are different design tasks. None is guaranteed by data volume alone.

The practical rule is simple enough to use before designing a study, adding a sensor, sequencing another batch, sampling another population or retraining a classifier:

> **Before collecting more data, ask what distinction the next measurement must create or preserve for the conclusion to change.**

That shift—from quantity-first acquisition to diagnostic distinction design—is the stance we think measurement-rich ecology and evolution now need.

---

## Figure 1. Measurement-to-evidence interfaces and the four-question audit

Central flow:

**Biological opportunity / live alternatives → retained record → distinguishable alternatives → declared target**

- **Timely preservation:** was the relevant difference retained through the observation pipeline?
- **Separation:** does the retained measurement separate a live alternative?
- **Relevance:** can the separated alternative change the declared target?
- **Failure diversity:** across repeated observation paths, are there independent opportunities for the relevant distinction to survive?

For a proposed additional measurement, the practical audit is:

1. Does it separate a live alternative? If not → measure a new distinction.
2. Can that difference change the target? If not → redirect to target-relevant information.
3. Does it add an independent opportunity to survive failure? If not → diversify failure domains.
4. Is the needed distinction still present at the stage being improved? If not → capture earlier; if retained but semantics changed → recalibrate.

The figure should depict failure diversity as wrapping or paralleling the observation paths rather than as one sequential arrow. The screen is diagnostic, not a universal evidence score and not an exhaustive theory of evidence.

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