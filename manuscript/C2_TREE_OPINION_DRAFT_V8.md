# When more measurement is not more evidence

**Article type:** Opinion  
**Target:** *Trends in Ecology & Evolution*  
**Status:** preferred editorial draft v8; self-contained; cross-domain; direct-neighbour prior art integrated; not yet journal-formatted

## Highlights

- Familiar performance metrics are local quantities conditioned on upstream measurement choices and losses.
- Existing ecological frameworks already synthesize observation-process failures; C2 instead asks what measurement to choose next for a declared claim.
- The prospective doctrine maps a diagnosed bottleneck to a measurement intervention class: preserve earlier, create separation, align with the target or diversify failure domains.
- The decisive test is whether pre-data diagnosis predicts which equal-cost measurement expansion improves claim resolution most.

## Abstract

Ecology and evolution are increasingly measurement-rich. Sensors, remote sensing, bioacoustics, camera traps, genomic assays, environmental DNA and machine-learning pipelines can expand observation volume, precision and downstream performance at rapidly falling marginal cost. Yet these quantities are not universal proxies for evidential progress. We focus on **conditioning-set dependence**: precision is local to what was measured, classifier accuracy to what entered the retained record, information gain to the state or target represented in the objective, and replicate count to an inferential unit and failure architecture. Existing ecological frameworks already show that observation processes and sampling design shape inference; our narrower claim is prospective. For a declared scientific responsibility, ask where the distinction needed by that claim is lost or never created, diagnose the limiting interface—**timely preservation**, **separation**, **relevance** or **failure diversity**—and change the measurement accordingly. We therefore propose a falsifiable measurement-choice doctrine: before collecting new data, test whether a diagnosis-matched equal-cost intervention improves claim resolution more than quantity-first or local-performance expansion.

## The bottleneck is not always data quantity

Ecologists and evolutionary biologists can now measure systems at scales that were recently impractical. Autonomous sensors generate continuous records; cameras and microphones collect millions of observations; genomic and environmental-DNA assays resolve variation at high throughput; automated phenotyping and machine learning convert raw observations into classifications faster than humans can inspect them. Adding another record is often easier than deciding whether that record creates the distinction needed for the scientific claim.

Collecting more data is often exactly right. More observations can reduce sampling error, reveal rare states and improve predictions. The problem is that “more” can mean more measurements of the same variable, more variables, more latent-state information, more nominal replicates, better classifier outputs, or more downstream processing. These additions act at different parts of the measurement-to-evidence process.

A trait cline can be sampled twice as densely while competing mechanisms still predict the same cline. A genomic assay can resolve many nuisance states while leaving the focal evolutionary contrast uncertain. Hundreds of samples can share one population, sensor, batch or field window. A biodiversity classifier can become nearly perfect on retained sequences while upstream sampling or amplification has already removed some taxa. In each case a familiar performance metric improves while the decisive scientific distinction may not.

The practical question is therefore not simply **“how can we measure more?”** It is:

> **What distinction must the next measurement create or preserve for the ecological or evolutionary conclusion to change?**

We use **evidential progress** in this operational sense: increased ability to distinguish among live alternatives that matter to a declared scientific claim, using distinctions that the observation process actually preserves. This is deliberately narrower than a general philosophical definition of evidence.

The components have deep roots. Chamberlin's multiple working hypotheses and Platt's strong inference made discrimination among competing explanations a central scientific ideal [15,16]. Structural-identifiability and parameter-redundancy work formalize when observations can or cannot distinguish model parameters or combinations, including in ecological capture–recapture and state-space models [1,17,18]. Targeted and goal-oriented experimental design asks whether observations reduce uncertainty in a declared prediction or quantity of interest [2,3], while value-of-information analysis asks whether resolving uncertainty can improve a decision [4]. Ecological monitoring has long argued that data collection should be organized around explicit questions and decisions [5,6]. Ecologists distinguish nominal sample size from independent replication [7,8]. Occupancy and species-distribution modelling separate observation from latent ecological state [9,10], while calibration, ecological AI and metabarcoding show that downstream outputs inherit assumptions and losses from earlier stages [11–14]. Williams and Brown explicitly link sampling design to statistical inference and discuss a conditionality principle and effective sampling strategies [22]. Most directly, Chadwick and colleagues' TREE **LIES** framework already provides a cross-field typology of observation processes—Latency, Identifiability, Effort and Scale—and links problem classes to inferential solutions [21]. The rise of data-intensive ecology has made the scale of the opportunity explicit, while TREE work has emphasized complementarity between big observational data and experiments rather than treating volume as a substitute for discriminating design [19,20].

Our contribution is therefore **not another typology of observation problems**, and it is not the observation that sampling and analysis are conditional on design. The shared conditional structure is a starting point, not the novelty claim. We shift the unit of diagnosis to the **distinction required by a declared claim** and use the diagnosis prospectively to choose what kind of measurement must change next. Precision is local to an observational axis; information gain to a represented state or target; replication to a dependence and failure architecture; classifier accuracy to records that survived earlier stages. The proposed advance is a claim-specific mapping from bottleneck to intervention class, coupled to a prospective test of that mapping.

We operationalize that measurement-choice problem through four interfaces. A biological difference must survive long enough to become a record, the record must distinguish live alternatives, the distinction must matter to the declared target, and repeated support must not depend entirely on one shared failure. We call these properties **timely preservation**, **separation**, **relevance** and **failure diversity** (Figure 1). They are a prospective intervention screen, not a claim to replace LIES or other observation-process taxonomies.

### A necessary non-harm caveat

Our argument is not that extra information is intrinsically harmful. In an ideal decision problem, a cost-free observation that can simply be ignored need not make an optimal decision worse. Nor do we argue against large data sets, replication or accurate models. The failure is in treating a **conditional local metric as a universal proxy for a downstream scientific responsibility**. More sample size, precision, total latent-state information, nominal replication or conditional classifier accuracy does not guarantee more resolution of the claim for which evidence is being collected. Under finite budgets, choosing the wrong form of “more” can consume effort while leaving the limiting uncertainty untouched.

## From measurement to evidence: four interacting interfaces

The ordering used here follows the observation path in Figure 1. A biologically relevant difference first has to survive the observation process: **timely preservation**. The retained measurement must then differ across live alternatives: **separation**. That difference must matter for the prediction, contrast or decision the study owns: **relevance**. **Failure diversity** is cross-cutting rather than a fourth downstream stage: at any point, repeated support can depend on a shared failure domain.

This ordering is descriptive, not a claim that studies must diagnose interfaces in sequence. A study can perform well on three interfaces and fail at the fourth, and improving one interface can change another. Adding a second sensor may increase failure diversity while introducing a different detection function or calibration problem. Primer diversity can protect against one amplification blind spot while reducing depth per primer. A highly target-specific measurement can improve relevance while sacrificing information useful for future mechanism discovery. Moving capture earlier in a pipeline can improve preservation while increasing storage, annotation or false-positive burden. The framework is therefore not four independent checkboxes; it is a way to locate **trade-offs in the flow of distinctions**.

This is the key difference from a catalogue or typology of familiar observation problems. The question is not merely which observation-process problem is present, nor whether precision, information gain, replication or classifier accuracy are good metrics. It is **what distinction the declared claim still requires, where that distinction is blocked, and which measurement change should remove that bottleneck**.

> **Ecological and evolutionary measurement design should be organized around the flow of distinctions required by the claim, not around data volume alone.**

## Interface 1 — Timely preservation: is the needed distinction still available downstream?

### Failure when missing: too late

Ecological and evolutionary observations often pass through many stages: biological opportunity, sampling or sensing, record entry, extraction or amplification, classification, thresholding, aggregation and reporting. Improving a late stage does not necessarily repair losses at an earlier one.

Occupancy modelling formalized the basic point that nondetection is not absence when detection probability is below one [9]. Species-distribution studies show that ignoring detectability can damage calibration and inference about underlying distributions [10]. In digital systems the asymmetry can be sharper: if an event never entered the retained record, no downstream classifier can recover it.

The same logic appears in biodiversity sequencing. A taxonomic classifier may be excellent on received sequences while remaining blind to taxa lost through field sampling, DNA degradation, extraction, primer mismatch or amplification. Metabarcoding therefore requires attention to errors and biases throughout the workflow, not only final assignment [13].

The diagnostic question is:

> **Is the distinction we need still present in the retained record?**

If no, downstream accuracy is the wrong investment target: **capture the distinction earlier** or add an independent observation path.

A nearby but distinct problem occurs when the record survives but its **operating semantics drift**. A threshold or probability that once had one operating meaning can lose it after recalibration, domain shift or feature transformation. That is not preservation failure because the record still exists. It is a calibration or transport problem that can sometimes be repaired downstream if the relevant distinction remains encoded [11,12,14]. Keeping these cases separate matters: irreversible loss requires new support, whereas semantic drift may permit recalibration.

## Interface 2 — Separation: does the measurement distinguish a live alternative?

### Failure when missing: same dimension

Suppose two explanations predict the same value for the variable being measured. Improving its precision can narrow confidence intervals indefinitely without separating those explanations. Repeating the same assay, rescaling it or adding a transformation may improve estimation while leaving the compatible mechanisms unchanged.

This is the distinction between **precision** and **identification**. Chamberlin and Platt framed the scientific task as discriminating among live hypotheses [15,16]; parameter-redundancy work shows formally that some ecological models cannot estimate all parameters from a given observation structure, while additional data types or constraints can change what is estimable [17,18]. Structural-identifiability theory gives a related formal language in dynamical systems [1]. The broader lesson is simple: an observation can be measured extremely well and still fail to cut the ambiguity that matters.

In ecology, fruit set can be consistent with many visits of low effectiveness or few visits of high effectiveness. In evolutionary biology, dense phenotypic measurement can sharpen a trajectory without distinguishing processes that predict the same phenotype. More detail along the existing observational axis helps only when that axis is where the live alternatives differ.

The diagnostic question is:

> **Does the proposed measurement separate a previously unresolved explanation, or only measure an already represented distinction more accurately?**

If the latter, the remedy is a **new distinction**, not necessarily more replication: per-visit pollen deposition rather than another visit count, an interaction response rather than a denser abundance series, or a second trait, intervention or historical contrast that makes evolutionary alternatives diverge.

The exact conditions for structural identification depend on the model class; C2 does not import those theorem surfaces from the specialist literature. The Opinion-level point is only that separation is, in principle, a testable property of an observation design rather than a synonym for precision.

## Interface 3 — Relevance: can the distinction change the declared target?

### Failure when missing: wrong target

A measurement can genuinely separate latent states and still be poorly aligned with the scientific responsibility.

Targeted experimental design makes this familiar. If the responsibility is a forecast, intervention effect, evolutionary contrast or management decision, reducing uncertainty in every parameter can be less valuable than resolving one distinction that changes the target [2–4].

Consider eight equally plausible worlds defined by a binary target state and a four-level nuisance state. Candidate A identifies the nuisance state perfectly and also carries a noisy target signal that is correct 75% of the time. It therefore reveals more about total world identity and is not useless for the target. Candidate B reveals the binary target exactly but no nuisance state. A full-world information criterion can rank A above B because A resolves two nuisance bits plus some target information; a target-resolution criterion ranks B above A because only B closes the declared binary contrast. The disagreement is therefore not produced by comparing useful information with pure noise. It arises because two reasonable objectives rank the same candidate measurements differently.

The same problem appears when a study quietly switches goals. A biodiversity survey may seek discovery, occupancy estimation and conservation prioritization. A phylogenomic programme may seek topology, timing and a focal evolutionary transition. An observation that strongly improves one responsibility need not improve the others.

The diagnostic question is:

> **Can the new distinction change the prediction, classification, evolutionary contrast or decision that the study is responsible for?**

If not, the information may still be scientifically useful, but it is not stronger evidence for that target. The remedy is **target-relevant information**, not information maximization in the abstract. Monitoring theory reaches the same conclusion from another direction: information gathering is most useful when its role in learning or decision making is explicit [5,6].

## Interface 4 — Failure diversity: is this a genuinely new opportunity for evidence to survive?

### Failure when missing: false independence

Replication is a central safeguard in ecology and evolution, but replicate count and evidential independence are not synonyms.

Hurlbert's critique of pseudoreplication showed that observations sharing an experimental unit or treatment history cannot be counted as independent treatment replicates [7]. Contemporary design retains the same principle: the scale of replication must match the scale of inference [8]. Modern observation systems add technical failure domains even when records are numerically distinct.

Ten camera images from one obscured camera share a camera-level failure. Ten PCR reads from one failed extraction share an extraction failure. Hundreds of individuals from one population do not replace independent population contrasts when population is the inferential unit. Multiple genomic measurements can share library, batch or amplification failures.

Within a functioning mode, more repeats can improve conditional sensitivity. They do not provide the same protection as observations distributed across independent modes when common-mode loss dominates. The relevant design resource is therefore **failure diversity**.

The diagnostic question is:

> **Did we add another observation, or another genuinely independent opportunity for the distinction to survive failure?**

If shared dependence is limiting, the remedy is to **diversify failure domains**—sensors, sites, populations, observers, batches, primers, time windows or other relevant modes. Dependence can often be modelled, but statistical adjustment cannot retroactively create an independent biological or technical opportunity that was never sampled.

## A four-question distinction-flow audit

The four interfaces can be condensed into a prospective screen in the same order as Figure 1.

| Interface | Diagnostic question | Failure if absent | Remedy |
|---|---|---|---|
| **timely preservation** | Is the needed distinction still present at the stage being improved? | too late | capture earlier; if retained but semantics drifted, recalibrate |
| **separation** | Does it separate a live alternative? | same dimension | measure a new distinction |
| **relevance** | Can that distinction change the declared target? | wrong target | measure target-relevant information |
| **failure diversity** | Does support depend on one shared failure domain? | false independence | diversify failure domains |

This audit is **not a necessary-and-sufficient theorem for all evidence**. It is a practical screen for a common design decision: what should we measure next?

A compact workflow follows: declare the scientific responsibility; list the live alternatives; locate where they could first produce a measurable difference; ask whether that difference survives to the record; ask whether the retained difference separates the alternatives and matters to the target; then audit shared failure. Improve precision when precision is limiting; otherwise change the observation stage, distinction, target alignment or failure architecture.

> **Measurement escalation should be diagnostic-first, not quantity-first.**

## Box 1. Island *Campanula*: design a contrast that decouples pollinators from climate

Consider a prospective island *Campanula* study in which floral phenotype covaries geographically with climate and pollinator community. Dense sampling of the same cline can improve description while leaving abiotic filtering, pollinator-mediated selection and demographic history jointly compatible.

A stronger separation design does not require assuming that one floral trait belongs uniquely to one mechanism. Instead, deliberately seek **decoupled contrasts**: island or site pairs that overlap in climate and elevation but differ in pollinator community, or pollinator exclusions that alter visitation while leaving the abiotic setting unchanged. In the Izu context, contrasts involving sites with and without large bumblebee service are a natural prospective target, provided climate overlap and demographic differences are handled explicitly rather than assumed away.

The measurement package then changes. Floral phenotype remains useful, but the mechanism-separating observations are visitor identity, visitation, effective pollen transfer and reproductive consequence measured across the decoupled contrast. If phenotype shifts with pollinator service under comparable abiotic conditions, the pollinator explanation gains separation; if the same phenotype pattern persists where pollinator service differs, that explanation loses support. The design creates a contrast among live alternatives rather than declaring any single floral character intrinsically mechanistic.

This also illustrates interface interaction. Adding a new island or exclusion can improve separation while introducing a new observer, season or sensor failure domain; the same design must therefore be audited for preservation and failure diversity.

The example is intentionally a **worked design example, not a new empirical validation claim**.

## Box 2. Metabarcoding: improve the interface that lost the taxon

Consider an environmental-DNA or metabarcoding survey in which a focal taxon is absent from the final table. Improving the classifier or sequencing more deeply may help—but only if the relevant sequence entered the retained pool.

The taxon could have been lost during field sampling, extraction, amplification, library preparation or classification, and these possibilities imply different remedies [13]. If the sequence is present but classifier probabilities have unstable operating meaning, recalibration or a better classifier can help [11,12,14]. If the sequence was never amplified, no classifier can recover it; the intervention must move upstream.

Failure diversity matters too. Thousands of reads from one extraction are not thousands of independent opportunities to survive extraction failure. Replication across extraction, primer or sampling modes can be more valuable than deeper sequencing within one mode when common-mode loss is limiting.

The lesson is not that sequencing depth or classifier quality is unimportant. Each acts on a particular interface. **The correct investment target is the interface at which the biologically relevant distinction is being lost.**

This is a **worked design illustration based on established metabarcoding and ecological-inference problems**, not a new empirical benchmark.

## What this stance changes

A conceptual framework matters only if it changes practice.

### 1. Design reports should name the limiting interface

Statements such as “we need more data” or “classifier performance must improve” are incomplete. Authors should state whether the limitation is failure to preserve an event, failure to separate alternatives, failure to align with the target, or vulnerability to shared failure.

### 2. Benchmarks should expose their conditioning set

A downstream benchmark can be excellent while an upstream observation process fails. Precision, information gain, replicate count and classifier accuracy should therefore be reported with the condition that makes each quantity local: the measured axis, target definition, inferential unit, retained-record set or other eligibility set on which the metric is calculated.

### 3. Additional measurement should compete against alternative measurement

The relevant comparison is often not “more versus less” of one quantity but “more of the current measurement versus a different measurement attacking another interface.” Candidate observations should therefore be compared by the distinctions they create or preserve for the declared claim.

## One core prediction: diagnosis should predict the best intervention

Ranking candidate measurements is not itself new: goal-oriented design and value-of-information methods already compare observations once a target, candidate set and probabilistic or decision model are specified [2–4]. Nor is diagnosing observation-process structure new [21,22]. C2 instead makes a coarser, cross-system empirical claim about **intervention class**: a claim-specific diagnosis of where the needed distinction is blocked should predict whether the next investment must move earlier in the pipeline, create a new separating axis, become more target-aligned, or diversify failure domains.

Several interface-specific consequences follow almost by definition; those are not the strongest empirical claim. The decisive prediction is prospective:

> **Given a predeclared claim and several equal-cost measurement expansions, diagnosing the limiting interface before collecting new data should predict which intervention produces the largest gain in claim resolution.**

This can be tested in three ways. First, simulations with known truth can generate designs in which preservation, separation, relevance or common-mode failure is deliberately made limiting; an analyst blinded to the best intervention diagnoses the interface from the baseline data and chooses among equal-cost expansions. Second, monitoring programmes with a higher-quality reference channel or audit sample can be replayed retrospectively: hide the reference channel, diagnose the bottleneck using the ordinary observation system, then test whether the matched intervention would have recovered more reference-supported claim resolution than quantity-first expansion. Third, prospective field or sensor studies can randomize equal effort among “more of the same” and diagnosis-matched alternatives.

The evaluation criterion should be declared before the expansion—for example, discrimination among predeclared mechanisms, calibration of a focal prediction, recovery of known opportunities, or correct management classification. The framework is supported if prospective diagnosis predicts intervention-class ranking better than simple data-volume or local-performance heuristics. Where a correctly specified full value-of-information or optimal-design model is available, C2 is not expected to outperform it; the relevant test is whether interface diagnosis identifies the missing candidate class or supplies useful ranking information before such a full model is available. The framework is weakened if the diagnoses do not predict which equal-cost intervention helps.

This prediction turns the synthesis from a vocabulary into a research programme.

## A measurement contract for ecological and evolutionary studies

Before expanding measurement, a study can state:

1. **Responsibility:** what statement, prediction, contrast or decision must the evidence support?
2. **Live alternatives:** which states or explanations remain compatible with current evidence?
3. **Preservation:** where could a relevant difference be lost before it becomes a retained record?
4. **Separation:** what candidate observation differs across those alternatives?
5. **Relevance:** would that difference change the declared responsibility?
6. **Failure structure:** which observations share failure domains, and where are independent opportunities created?
7. **Decision rule:** what result from the new observation would change the conclusion or next action?

The contract is not bureaucracy. It exposes hidden substitutions: more samples for a missing mechanism-separating measurement; higher classifier accuracy for unmeasured missed opportunities; more total information for information relevant to the declared target.

## Outstanding questions

### What does interface diagnosis add beyond observation-process frameworks and formal optimal design?

LIES already supplies a cross-field language for complex observation processes, sampling-design frameworks already connect collection to inference, and value-of-information or optimal-design methods can rank candidate observations [2–4,21,22]. C2 should earn its keep only if a claim-specific distinction-flow diagnosis adds something operational: identifying a missing intervention class, locating an upstream or shared-failure bottleneck that a downstream benchmark hides, or predicting a useful measurement change before a fully specified design model is available. Direct comparison against those baselines is therefore part of the research programme, not optional positioning.

### How should the four interfaces be quantified without collapsing them into one score?

Separation may be represented through structural distinguishability or expected discrimination among alternatives. Relevance may use target resolution, predictive utility or value of information. Failure diversity requires explicit dependence or common-mode structure. Timely preservation requires models of observation loss. Useful diagnostics must preserve these differences rather than force them onto one scale.

### How should trade-offs among interfaces be optimized?

This is now a central rather than peripheral problem. A design maximizing separation may be expensive or fragile; a target-specific measurement may sacrifice information useful for future questions; failure-domain diversity may reduce within-mode replication; earlier observation may increase storage or annotation burden. The next step is to compare bundles of interface properties under explicit scientific and resource constraints.

### When does a local metric become an adequate proxy for the claim?

The framework emphasizes conditionality, but local metrics can be exactly the right target when the relevant upstream conditions are satisfied. Characterizing when precision, information gain, replication or classifier accuracy becomes sufficient for a declared responsibility would sharpen the boundary between quantity-first and distinction-first design.

### Can a study move between failure classes over time?

Yes. Preservation can dominate when the observation system is first deployed; after adding a reference channel, separation may become limiting; after adding a separating measurement, relevance or shared failure may dominate. The framework describes recurring diagnoses, not permanent labels.

### Are the four failures exhaustive?

No. They are intended as a useful cross-cutting set, not a theorem about every evidential failure. Model misspecification, nonstationarity, causal transport, selective reporting, strategic behaviour and ethical constraints create other limitations. If none of the four interfaces fits the bottleneck, another diagnosis is needed.

## Conclusion: design distinctions, not just data volume

Ecology and evolution do not face one generic data shortage. In many systems, the bottleneck is deciding **which new distinction would count as evidence for the question at hand**.

The shared structure is **conditioning-set dependence**: every familiar performance metric is calculated after some observational choices, exclusions or losses have already occurred. This phrase is descriptive and should not be confused with the formal statistical conditionality principle used in sampling theory [22]. The C2 design task is prospective: make those conditions explicit, ask which distinction the declared claim still needs, and choose the measurement change that removes the limiting bottleneck.

Preserve the distinction, separate the alternatives, align the measurement with the target and diversify the failure opportunities. These are different and interacting design tasks, and none is guaranteed by data volume alone.

> **Before collecting more data, ask what distinction the next measurement must create or preserve for the conclusion to change.**

The strongest test of that stance is prospective: can the diagnosis predict which equal-cost measurement expansion actually helps most?

## Figure 1. Measurement-to-evidence interfaces and the four-question audit

Central flow:

**Biological opportunity / live alternatives → retained record → distinguishable alternatives → declared target**

- **Timely preservation:** was the relevant difference retained through the observation pipeline?
- **Separation:** does the retained measurement separate a live alternative?
- **Relevance:** can the separated alternative change the declared target?
- **Failure diversity:** across repeated observation paths, are there independent opportunities for the relevant distinction to survive?

Failure diversity should wrap or parallel the observation paths rather than appear as one sequential stage. The figure is a diagnostic screen, not a universal evidence score or exhaustive theory.

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
15. Chamberlin TC. The Method of Multiple Working Hypotheses. *Science*. 1890;15(366):92–96. doi:10.1126/science.ns-15.366.92.
16. Platt JR. Strong Inference: Certain systematic methods of scientific thinking may produce much more rapid progress than others. *Science*. 1964;146(3642):347–353. doi:10.1126/science.146.3642.347.
17. Catchpole EA, Freeman SN, Morgan BJT. Steps to Parameter Redundancy in Age-Dependent Recovery Models. *Journal of the Royal Statistical Society: Series B (Methodological)*. 1996;58(4):763–774. doi:10.1111/j.2517-6161.1996.tb02114.x.
18. Cole DJ, McCrea RS. Parameter redundancy in discrete state-space and integrated models. *Biometrical Journal*. 2016;58(5):1071–1090. doi:10.1002/bimj.201400239.
19. McCleery R, Guralnick R, Beatty M, Belitz M, Campbell CJ, Idec J, Jones M, Kang Y, Potash A, Fletcher RJ Jr. Uniting Experiments and Big Data to advance ecology and conservation. *Trends in Ecology & Evolution*. 2023;38(10):970–979. doi:10.1016/j.tree.2023.05.010.
20. Michener WK, Jones MB. Ecoinformatics: supporting ecology as a data-intensive science. *Trends in Ecology & Evolution*. 2012;27(2):85–93. doi:10.1016/j.tree.2011.11.016.
21. Chadwick FJ, Haydon DT, Husmeier D, Ovaskainen O, Matthiopoulos J. LIES of omission: complex observation processes in ecology. *Trends in Ecology & Evolution*. 2024;39(4):368–380. doi:10.1016/j.tree.2023.10.009.
22. Williams BK, Brown ED. Sampling and analysis frameworks for inference in ecology. *Methods in Ecology and Evolution*. 2019;10(11):1832–1842. doi:10.1111/2041-210X.13279.
