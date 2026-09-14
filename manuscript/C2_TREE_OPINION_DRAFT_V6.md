# When more measurement is not more evidence

**Article type:** Opinion  
**Target:** *Trends in Ecology & Evolution*  
**Status:** preferred editorial draft v6; self-contained; cross-domain; not yet journal-formatted

## Highlights

- Data quantity is not a universal proxy for evidential progress in ecology or evolution.
- Measurement becomes evidence through preservation, separation, relevance and failure diversity.
- Different bottlenecks require different remedies; more of the same can leave the limiting distinction unresolved.
- Measurement design should shift from quantity-first acquisition to diagnostic distinction design.

## Abstract

Ecology and evolution are increasingly measurement-rich. Sensors, remote sensing, bioacoustics, camera traps, genomic assays, environmental DNA and machine-learning pipelines can expand observation volume, precision and downstream performance at rapidly falling marginal cost. Yet these quantities are not universal proxies for evidential progress. We argue that an added measurement becomes useful evidence for a declared claim through distinct interfaces. The needed biological difference must be **preserved** by the observation pipeline, the measurement must **separate** live alternatives, the separated alternatives must be **relevant** to the scientific target, and repeated support must contain enough **failure diversity** not to depend on one shared point of failure. Missing these properties produces four recurrent failures: too late, same dimension, wrong target and false independence. Because the failures differ, so do their remedies. We propose a four-question measurement-to-evidence screen for diagnosing what kind of observation should be added next. The practical shift is from quantity-first acquisition to **diagnostic distinction design**.

## The bottleneck is not always data quantity

Ecologists and evolutionary biologists can now measure systems at scales that were recently impractical. Autonomous sensors generate continuous records; cameras and microphones collect millions of observations; genomic and environmental-DNA assays resolve variation at high throughput; automated phenotyping and machine learning convert raw observations into classifications faster than humans can inspect them. Adding another record is often easier than deciding whether that record creates the distinction needed for the scientific claim.

Collecting more data is often exactly right. More observations can reduce sampling error, reveal rare states and improve predictions. The problem is that “more” can mean more measurements of the same variable, more variables, more latent-state information, more nominal replicates, better classifier outputs, or more downstream processing. These additions act at different parts of the measurement-to-evidence process.

A trait cline can be sampled twice as densely while competing mechanisms still predict the same cline. A genomic assay can resolve many nuisance states while leaving the focal evolutionary contrast unchanged. Hundreds of samples can share one population, sensor, batch or field window. A biodiversity classifier can become nearly perfect on retained sequences while upstream sampling or amplification has already removed some taxa. In each case a familiar performance metric improves while the decisive scientific distinction does not.

The practical question is therefore not simply **“how can we measure more?”** It is:

> **What distinction must the next measurement create or preserve for the ecological or evolutionary conclusion to change?**

We use **evidential progress** in this operational sense: increased ability to distinguish among live alternatives that matter to a declared scientific claim, using distinctions that the observation process actually preserves. This is deliberately narrower than a general philosophical definition of evidence.

The components have deep roots. Structural-identifiability theory distinguishes model ambiguity from estimation precision [1]. Targeted and goal-oriented experimental design asks whether observations reduce uncertainty in a declared prediction or quantity of interest [2,3], while value-of-information analysis asks whether resolving uncertainty can improve a decision [4]. Ecological monitoring has long argued that data collection should be organized around explicit questions and decisions [5,6]. Ecologists distinguish nominal sample size from independent replication [7,8]. Occupancy and species-distribution modelling separate the observation process from latent ecological state [9,10]. Calibration, ecological AI and metabarcoding studies show that downstream outputs inherit assumptions and losses from earlier stages [11–14].

These traditions can be connected through one design problem. A biological difference must survive long enough to become a record, the record must distinguish live alternatives, the distinction must matter to the declared target, and repeated support must not depend entirely on one shared failure. We call these properties **timely preservation**, **separation**, **relevance** and **failure diversity** (Figure 1).

### A necessary non-harm caveat

Our argument is not that extra information is intrinsically harmful. In an ideal decision problem, a cost-free observation that can simply be ignored need not make an optimal decision worse. Nor do we argue against large data sets, replication or accurate models. The failure is in the **proxy-to-responsibility mapping**: more sample size, precision, total latent-state information, nominal replication or conditional classifier accuracy does not guarantee more resolution of the claim for which evidence is being collected. Under finite budgets, choosing the wrong form of “more” can consume effort while leaving the limiting uncertainty untouched.

## From measurement to evidence: four interfaces, not one quantity

A biologically relevant difference first has to survive the observation process: **timely preservation**. The retained measurement must then differ across live alternatives: **separation**. That difference must matter for the prediction, contrast or decision the study owns: **relevance**. When support is replicated, it must also not depend entirely on one shared point of failure: **failure diversity**.

These properties are not a linear checklist summarized by one score. Failure diversity can apply at several stages, and relevance is defined by the scientific responsibility rather than pipeline order. A study can perform well on three interfaces and still fail at the fourth.

This explains why useful local metrics can be poor global proxies. Precision concerns uncertainty conditional on what was measured. Information gain concerns what was learned, not necessarily whether it matters to the target. Replicate number does not count independent opportunities for a distinction to survive. Classifier accuracy describes records that reached the classifier, not necessarily upstream observation adequacy.

Our position is therefore stronger than “collect better data” but narrower than a general theory of evidence:

> **Ecological and evolutionary measurement design should be organized around the flow of distinctions required by the claim, not around data volume alone.**

## Interface 1 — Separation: does the measurement distinguish a live alternative?

### Failure when missing: same dimension

Suppose two explanations predict the same value for the variable being measured. Improving its precision can narrow confidence intervals indefinitely without separating those explanations. Repeating the same assay, rescaling it or adding a transformation may improve estimation while leaving the compatible mechanisms unchanged.

This is the distinction between **precision** and **structural identification**. Structural-identifiability theory formalizes whether distinct parameterizations or mechanisms can in principle generate the same observations [1]. An observation can therefore be measured extremely well and still fail to cut the ambiguity that matters.

In ecology, fruit set can be consistent with many visits of low effectiveness or few visits of high effectiveness. In evolutionary biology, dense phenotypic measurement can sharpen a trajectory without distinguishing processes that predict the same phenotype. More detail along the existing observational axis helps only when that axis is where the live alternatives differ.

The diagnostic question is:

> **Does the proposed measurement separate a previously unresolved explanation, or only measure an already represented distinction more accurately?**

If the latter, the remedy is a **new distinction**, not necessarily more replication: per-visit pollen deposition rather than another visit count, an interaction response rather than a denser abundance series, or a second trait or historical contrast that makes evolutionary alternatives diverge.

The point is qualitative: **more precision is evidential progress only when precision was the limiting problem**.

## Interface 2 — Relevance: can the distinction change the declared target?

### Failure when missing: wrong target

A measurement can genuinely separate latent states and still be irrelevant to the scientific responsibility.

Targeted experimental design makes this familiar. If the responsibility is a forecast, intervention effect, evolutionary contrast or management decision, reducing uncertainty in every parameter can be less valuable than resolving one distinction that changes the target [2–4].

Imagine eight equally plausible worlds differing in a binary target state and a four-level nuisance attribute. Under a budget allowing one measurement, one candidate perfectly reveals the nuisance state: 2 bits about world identity but no target resolution. A second provides only 1 bit about world identity but directly separates the target states. The first is better for full latent-state learning; the second is better for target resolution. The rankings differ because the responsibilities differ.

The same problem appears when a study quietly switches goals. A biodiversity survey may seek discovery, occupancy estimation and conservation prioritization. A phylogenomic programme may seek topology, timing and a focal evolutionary transition. An observation that strongly improves one responsibility need not improve the others.

The diagnostic question is:

> **Can the new distinction change the prediction, classification, evolutionary contrast or decision that the study is responsible for?**

If not, the information may still be scientifically useful, but it is not stronger evidence for that target. The remedy is **target-relevant information**, not information maximization in the abstract. Monitoring theory reaches the same conclusion from another direction: information gathering is most useful when its role in learning or decision making is explicit [5,6].

## Interface 3 — Failure diversity: is this a genuinely new opportunity for evidence to survive?

### Failure when missing: false independence

Replication is a central safeguard in ecology and evolution, but replicate count and evidential independence are not synonyms.

Hurlbert's critique of pseudoreplication showed that observations sharing an experimental unit or treatment history cannot be counted as independent treatment replicates [7]. Contemporary design retains the same principle: the scale of replication must match the scale of inference [8]. Modern observation systems add technical failure domains even when records are numerically distinct.

Ten camera images from one obscured camera share a camera-level failure. Ten PCR reads from one failed extraction share an extraction failure. Hundreds of individuals from one population do not replace independent population contrasts when population is the inferential unit. Multiple genomic measurements can share library, batch or amplification failures.

Within a functioning mode, more repeats can improve conditional sensitivity. They do not provide the same protection as observations distributed across independent modes when common-mode loss dominates. The relevant design resource is therefore **failure diversity**.

The diagnostic question is:

> **Did we add another observation, or another genuinely independent opportunity for the distinction to survive failure?**

If shared dependence is limiting, the remedy is to **diversify failure domains**—sensors, sites, populations, observers, batches, primers, time windows or other relevant modes. Dependence can often be modelled, but statistical adjustment cannot retroactively create an independent biological or technical opportunity that was never sampled.

## Interface 4 — Timely preservation: is the needed distinction still available downstream?

### Failure when missing: too late

Ecological and evolutionary observations often pass through many stages: biological opportunity, sampling or sensing, record entry, extraction or amplification, classification, thresholding, aggregation and reporting. Improving a late stage does not necessarily repair losses at an earlier one.

Occupancy modelling formalized the basic point that nondetection is not absence when detection probability is below one [9]. Species-distribution studies show that ignoring detectability can damage calibration and inference about underlying distributions [10]. In digital systems the asymmetry can be sharper: if an event never entered the retained record, no downstream classifier can recover it.

The same logic appears in biodiversity sequencing. A taxonomic classifier may be excellent on received sequences while remaining blind to taxa lost through field sampling, DNA degradation, extraction, primer mismatch or amplification. Metabarcoding therefore requires attention to errors and biases throughout the workflow, not only final assignment [13].

A complementary problem occurs when records survive but their numerical representation changes. A threshold that had one operating meaning can lose it after recalibration, domain shift or feature transformation. Calibration work shows that nominal probabilities cannot simply be assumed to have their stated meaning [11]. Ecological AI similarly requires classifier uncertainty and ecological inference to be connected explicitly [12], and deployment studies show how nominal performance can fall under dataset shift [14].

These failures require different remedies. **Irreversible support loss** requires independent new information—another sensor, reference process, audit sample, alternative primer or earlier-stage redesign. **Operating-semantics drift** can sometimes be repaired by recalibration if the relevant distinction remains in the record.

The diagnostic question is:

> **Is the distinction we need still present in the retained record?**

If yes, a better downstream model or recalibration may help. If no, downstream accuracy is the wrong investment target: **capture the distinction earlier**.

## A four-question distinction-flow audit

The four interfaces can be condensed into a prospective screen.

| Interface | Diagnostic question | Failure if absent | Remedy |
|---|---|---|---|
| **separation** | Does it separate a live alternative? | same dimension | measure a new distinction |
| **relevance** | Can that distinction change the declared target? | wrong target | measure target-relevant information |
| **failure diversity** | Does it add an independent opportunity for the distinction to survive? | false independence | diversify failure domains |
| **timely preservation** | Is the needed distinction still present at the stage being improved? | too late | capture earlier, or recalibrate if still retained |

This audit is **not a necessary-and-sufficient theorem for all evidence**. It is a practical screen for a common design decision: what should we measure next?

A compact workflow follows: declare the scientific responsibility; list the live alternatives; locate where they could first produce a measurable difference; ask whether that difference survives to the record; audit shared failure; then add measurement at the limiting interface. Improve precision when precision is limiting; otherwise change the distinction, target alignment, failure architecture or observation stage.

The workflow changes the design unit from records to **distinctions**. Sample size, precision, information gain, replication and classifier accuracy remain useful when they correspond to the limiting interface. None is a universal proxy for evidence.

> **Measurement escalation should be diagnostic-first, not quantity-first.**

## Box 1. Island *Campanula*: measure the mechanism-separating trait, not only the cline

Consider a prospective island *Campanula* study in which a floral trait varies geographically and several explanations can generate the same coarse cline: abiotic filtering, pollinator-mediated selection, demographic history, or combinations of them. Increasing trait measurements along that cline can improve its description without separating the explanations.

A diagnostic design instead asks which additional observation would make the alternatives predict different outcomes. A nectar-guide phenotype could be one such measurement if pollinator-mediated explanations predict a guide pattern that purely abiotic or demographic explanations do not. Its value would come from the alternatives it separates, not from being intrinsically “more mechanistic.”

This links separation and relevance. If more sampling only sharpens the original cline, **separation** is limiting. If a new variable reveals detail that does not change the focal mechanism comparison, **relevance** is limiting. The preferred observation is the one that separates the live alternatives for the declared question.

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

### 2. Benchmarks should follow the scientific responsibility through the pipeline

A downstream benchmark can be excellent while an upstream observation process fails. Where feasible, studies should report where relevant opportunities can be lost and which performance metric is conditional on having reached the evaluated stage.

### 3. Additional measurement should compete against alternative measurement

The relevant comparison is often not “more versus less” of one quantity but “more of the current measurement versus a different measurement attacking another interface.” Candidate observations should therefore be compared by the distinctions they create or preserve for the declared claim.

## Predictions for a distinction-design research programme

The framework suggests testable expectations rather than universal laws. When separation is limiting, increasing same-variable precision should yield smaller gains in discriminating predeclared alternatives than a mechanism-separating measurement. When shared failure dominates, adding records within one failure domain should improve conditional precision more than robustness to common-mode loss, whereas adding independent modes should do the reverse. Where upstream support loss is substantial, downstream accuracy evaluated only on retained records should overstate observation-system adequacy. Finally, candidate observations optimized for mechanism discovery, target prediction and management choice need not receive the same ranking.

These expectations can be tested with prospective design comparisons, simulations with known truth, and monitoring systems that retain reference channels or audit samples. The key empirical test is whether **diagnosing the missing interface predicts which design intervention produces the largest gain** for a predeclared claim.

## A measurement contract for ecological and evolutionary studies

Before expanding measurement, a study can state:

1. **Responsibility:** what statement, prediction, contrast or decision must the evidence support?
2. **Live alternatives:** which states or explanations remain compatible with current evidence?
3. **Separation:** what candidate observation differs across those alternatives?
4. **Preservation:** can that difference survive sampling, sensing, extraction, classification and aggregation?
5. **Failure structure:** which observations share failure domains, and where are independent opportunities created?
6. **Decision rule:** what result from the new observation would change the conclusion or next action?

The contract is not meant as bureaucracy. It exposes hidden substitutions: more samples for a missing mechanism-separating measurement; higher classifier accuracy for unmeasured missed opportunities; more total information for information relevant to the declared target.

## Outstanding questions

### How should the four interfaces be quantified without collapsing them into one score?

Separation may be represented through structural distinguishability or expected discrimination among alternatives. Relevance may use target resolution, predictive utility or value of information. Failure diversity requires explicit dependence or common-mode structure. Timely preservation requires models of observation loss. Useful diagnostics must preserve these differences rather than force them onto one scale.

### How should trade-offs among interfaces be optimized?

A design maximizing separation may be expensive or fragile; a target-specific measurement may sacrifice information useful for future questions; failure-domain diversity may reduce within-mode replication; earlier observation may increase storage or annotation burden. The next step is therefore to study trade-offs under explicit scientific and resource constraints.

### Can diagnosis improve prospective design decisions?

This is the decisive empirical test. With a predeclared target and several candidate expansions, can researchers diagnose the limiting interface before collecting new data, and does the matched remedy outperform an equal-cost quantity-first expansion? Such tests would turn the synthesis into a falsifiable design doctrine.

### Can a study move between failure classes over time?

Yes. Lack of separation can dominate early; after adding a separating measurement, relevance or shared failure may become limiting; after automation, pipeline loss may become decisive. The framework describes recurring diagnoses, not permanent labels.

### Are the four failures exhaustive?

No. They are intended as a useful cross-cutting set, not a theorem about every evidential failure. Model misspecification, nonstationarity, causal transport, selective reporting, strategic behaviour and ethical constraints create other limitations. If none of the four interfaces fits the bottleneck, another diagnosis is needed.

## Conclusion: design distinctions, not just data volume

Ecology and evolution do not face one generic data shortage. In many systems, the bottleneck is deciding **which new distinction would count as evidence for the question at hand**.

The positive formulation is simple: preserve the distinction, separate the alternatives, align the measurement with the target and diversify the failure opportunities. These are different design tasks, and none is guaranteed by data volume alone.

> **Before collecting more data, ask what distinction the next measurement must create or preserve for the conclusion to change.**

That shift—from quantity-first acquisition to diagnostic distinction design—is the stance we think measurement-rich ecology and evolution now need.

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
