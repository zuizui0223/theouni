# C2 prior-art map — *When more measurement is not more evidence*

Status: **external-literature novelty firewall aligned with manuscript v7**.  
Checked: **2026-09-24**.  
Purpose: prevent C2 from claiming novelty for component ideas with mature literatures and make the R1/R2 defence explicit.

## The claim C2 may make

C2 does **not** claim to discover that more data can be unhelpful. Its proposed contribution is a cross-literature design doctrine built around a shared conditional structure:

> **Precision, information gain, replicate count and classifier accuracy are local quantities conditioned on earlier choices about what was measured, what survived the observation process, what target matters, and which observations share failure domains.**

The manuscript organizes these conditions into four interacting interfaces:

1. **timely preservation** — did the biological distinction survive into the retained record?
2. **separation** — does the retained measurement distinguish a live alternative?
3. **relevance** — can the distinction change the declared scientific responsibility?
4. **failure diversity** — does support depend on one shared failure domain?

The strongest empirical claim is prospective, not definitional:

> Given a predeclared claim and equal-cost measurement expansions, diagnosing the limiting interface before collecting new data should predict which intervention yields the largest gain in claim resolution.

C2 should not claim that it invented competing-hypothesis reasoning, identifiability, goal-oriented design, value of information, pseudoreplication, imperfect detection, calibration, dataset-shift analysis, the link between sampling design and inference, cross-field observation-process typologies, or the value of experiments relative to big observational data.

---

## Historical separation tradition: multiple hypotheses and strong inference

The separation interface sits in a long scientific tradition and must acknowledge it explicitly.

- **Chamberlin TC (1890), “The Method of Multiple Working Hypotheses,” Science 15(366):92–96. DOI: 10.1126/science.ns-15.366.92.**  
  Argues for carrying multiple explanations simultaneously rather than allowing one ruling theory to dominate observation and interpretation.

- **Platt JR (1964), “Strong Inference,” Science 146(3642):347–353. DOI: 10.1126/science.146.3642.347.**  
  Makes discriminating alternatives through decisive tests central to rapid scientific progress.

### Novelty boundary

C2 does not rebrand strong inference. It asks a measurement-design question downstream of that tradition: **what kind of observation creates the distinction needed to discriminate the alternatives, and what other interfaces can still block that distinction from becoming evidence?**

---

## Interface 1 — Timely preservation

### C2 formulation

A distinction cannot support a claim downstream if it never entered, or was irreversibly deleted from, the retained record.

### Mature prior literature

- **MacKenzie et al. (2002), Ecology 83:2248–2255. DOI: 10.1890/0012-9658(2002)083[2248:ESORWD]2.0.CO;2.**  
  Nondetection is not absence when detection probability is below one; ecological state and observation process must be separated.

- **Lahoz-Monfort, Guillera-Arroita & Wintle (2014), Global Ecology and Biogeography 23:504–515. DOI: 10.1111/geb.12138.**  
  Demonstrates consequences of imperfect detection for species-distribution modelling.

- **Alberdi et al. (2018), Methods in Ecology and Evolution 9:134–147. DOI: 10.1111/2041-210X.12849.**  
  Shows how metabarcoding reliability depends on multiple upstream workflow steps, not only final taxonomic assignment.

### Nearby but distinct literature: operating-semantics drift

- **Dormann (2020), Global Ecology and Biogeography 29:760–765. DOI: 10.1111/geb.13070.**
- **Cowans et al. (2026), Methods in Ecology and Evolution 17:228–237. DOI: 10.1111/2041-210X.14485.**
- **Chen et al. (2025), Limnology and Oceanography: Methods 23:39–66. DOI: 10.1002/lom3.10659.**

These establish calibration/uncertainty/dataset-shift problems. V7 deliberately distinguishes these from preservation failure: if the record survives but its operating meaning changes, recalibration may be possible; if the distinction never entered the record, downstream repair cannot recreate it.

### Source-owned sharpening

`zuizui0223/rec` owns the protected record-entry irreversibility result. `zuizui0223/tnoa` owns representation-change/calibration semantics. C2 owns only the cross-interface lesson.

---

## Interface 2 — Separation

### C2 formulation

Greater precision need not distinguish live alternatives when those alternatives make the same prediction for the measured axis.

### Mature prior literature: structural identification

- **Villaverde, Barreiro & Papachristodoulou (2016), PLOS Computational Biology 12:e1005153. DOI: 10.1371/journal.pcbi.1005153.**

### Ecology/statistics parameter-redundancy tradition

- **Catchpole, Freeman & Morgan (1996), “Steps to Parameter Redundancy in Age-Dependent Recovery Models,” JRSS B 58:763–774. DOI: 10.1111/j.2517-6161.1996.tb02114.x.**  
  Establishes inspection-based diagnosis of parameter redundancy in ecological recovery models.

- **Cole & McCrea (2016), “Parameter redundancy in discrete state-space and integrated models,” Biometrical Journal 58:1071–1090. DOI: 10.1002/bimj.201400239.**  
  Develops parameter-redundancy methods for ecological state-space/integrated models and shows how combining data types can change estimability.

### Source-owned sharpening

`zuizui0223/boundary` supplies the exact declared log-linear rank result and diagnostics.

### Publication-surface ceiling

C2 may state only that **separation can have formal, testable conditions** and that more precision is not synonymous with identification. The exact `k-rank(M)` theorem, row-span iff condition, Γ/κ development, breakdown factor and anchor ladder remain Boundary/C1 publication surface.

---

## Interface 3 — Relevance

### C2 formulation

More information about the latent world can be less useful for a declared target than a smaller amount of target-aligned information.

### Mature prior literature

- **Vanlier et al. (2012), Bioinformatics 28:1136–1142. DOI: 10.1093/bioinformatics/bts092.**
- **Attia, Alexanderian & Saibaba (2018), Inverse Problems 34:095009. DOI: 10.1088/1361-6420/aad210.**
- **Canessa et al. (2015), Methods in Ecology and Evolution 6:1219–1228. DOI: 10.1111/2041-210X.12423.**
- **Nichols & Williams (2006), Trends in Ecology & Evolution 21:668–673. DOI: 10.1016/j.tree.2006.08.007.**
- **Lindenmayer & Likens (2009), Trends in Ecology & Evolution 24:482–486. DOI: 10.1016/j.tree.2009.03.005.**

These already establish target- and decision-dependent information value.

### V7 strengthening

The manuscript no longer compares “pure nuisance information” against “perfect target information.” Candidate A now contains **more total world information and a nonzero noisy target signal**, whereas Candidate B has less total information but exact target resolution. The ranking reversal is therefore not a strawman comparison of useful information with irrelevant noise.

### Source-owned sharpening

`zuizui0223/ced` retains its exact finite equal-cost witness. C2 uses only the cross-literature objective-mismatch lesson.

---

## Interface 4 — Failure diversity

### C2 formulation

Nominal replicate count need not equal independent opportunities for a distinction to survive when observations share a failure domain.

### Mature prior literature

- **Hurlbert (1984), Ecological Monographs 54:187–211. DOI: 10.2307/1942661.**
- **Marshall (2024), Ecology Letters 27:e14400. DOI: 10.1111/ele.14400.**

### Source-owned sharpening

`zuizui0223/ced` owns the failure-mode guarantee results. C2 does not rebrand pseudoreplication; it uses failure-domain diversity as one interacting interface in measurement-to-evidence design.

---

## Big-data / data-intensive ecology prior art

C2 must not imply that ecology has ignored the opportunities or limitations of data volume.

- **Michener & Jones (2012), “Ecoinformatics: supporting ecology as a data-intensive science,” Trends in Ecology & Evolution 27:85–93. DOI: 10.1016/j.tree.2011.11.016.**  
  Frames ecology as increasingly data-intensive and emphasizes infrastructure for turning heterogeneous data into knowledge.

- **Hampton et al. (2013), “Big data and the future of ecology,” Frontiers in Ecology and the Environment 11:156–162. DOI: 10.1890/120103.**  
  Emphasizes the scientific opportunity of distributed ecological big data.

- **McCleery et al. (2023), “Uniting Experiments and Big Data to advance ecology and conservation,” Trends in Ecology & Evolution 38:970–979. DOI: 10.1016/j.tree.2023.05.010.**  
  Explicitly argues that big observational data and experiments are complementary rather than substitutes, including for mechanism and intervention questions.

### Novelty boundary relative to big-data Opinions

C2 is not an anti-big-data argument and does not claim that experiments are always superior. Its proposed novelty is the **conditioning-set diagnosis**: ask what a local metric is conditional on, locate the limiting interface, and prospectively choose among equal-cost measurement expansions.

---

## Direct-neighbour ecological syntheses that narrow the C2 novelty claim

### Chadwick et al. 2024 — LIES of omission

- **Chadwick FJ, Haydon DT, Husmeier D, Ovaskainen O, Matthiopoulos J. (2024), “LIES of omission: complex observation processes in ecology,” Trends in Ecology & Evolution 39:368–380. DOI: 10.1016/j.tree.2023.10.009.**
- This is the closest publication-surface neighbour because it is already a TREE synthesis of complex observation processes across ecological applications.
- Its LIES framework classifies observation-process problems through **Latency, Identifiability, Effort and Scale**, explicitly seeks methodological commonalities across fields, and links problem classes to inferential solutions.
- The thesis version underlying the published review explicitly lists linking observation-process models to experimental-design techniques and improving data collection as an outstanding question. The published abstract and highlights frame LIES primarily as a typology of observation problems and inferential solutions, not as the prospective claim-specific intervention-ranking doctrine proposed in C2.

**Consequence for C2:** cross-field synthesis, a four-part observation framework, and interaction among observation problems are **not** novelty claims. C2 must cite LIES early and position itself as the prospective measurement-choice step: for a declared claim, locate where the required distinction is blocked and predict the class of measurement change that should remove that bottleneck.

### Williams & Brown 2019 — sampling design and inference

- **Williams BK, Brown ED. (2019), “Sampling and analysis frameworks for inference in ecology,” Methods in Ecology and Evolution 10:1832–1842. DOI: 10.1111/2041-210X.13279.**
- This review explicitly links sampling design to statistical inference, discusses a statistical conditionality principle for model-based inference, integrates design- and model-based reasoning, and notes that the combined framework can identify effective sampling strategies.

**Consequence for C2:** “inference is conditional on design” is not a novelty claim. C2 uses **conditioning-set dependence** descriptively and must distinguish that phrase from the formal statistical conditionality principle.

### Revised novelty boundary after the direct-neighbour audit

C2 is **not**:
1. a new taxonomy of observation processes;
2. the discovery that sampling design conditions inference;
3. the invention of ranking candidate measurements—goal-oriented design and value-of-information already do that.

The defensible prospective claim is narrower:

> **For a predeclared scientific claim, diagnosing where the required distinction is blocked should predict the class of measurement intervention that improves claim resolution: capture earlier, create a new separating axis, measure target-relevant information, or diversify failure domains.**

This is best treated as a falsifiable cross-system design hypothesis. Where a correctly specified full value-of-information or optimal-design model is available, C2 should not claim superiority. Its empirical value is instead whether interface diagnosis (i) identifies a missing candidate intervention class, (ii) exposes an upstream/shared-failure bottleneck hidden by a downstream metric, or (iii) provides useful intervention-class ranking before a full design model is available.

---

# Why the synthesis is not merely four citations side by side

The v8 synthesis must satisfy three tests after conceding the direct-neighbour overlap above.

### 1. A common structure

Each familiar metric is local because it is calculated after some eligibility condition has already been imposed:

| metric | hidden/explicit conditioning set |
|---|---|
| precision | the observational axis already chosen |
| information gain | the state variables included in the objective |
| replicate count | the inferential unit and failure architecture |
| classifier accuracy | records that survived upstream entry/processing |

C2's cross-literature claim is that **local metric improvement is not equivalent to downstream claim resolution unless the relevant conditioning set preserves the distinction required by the claim**.

### 2. Interface interactions

The interfaces are not four independent boxes. Adding another sensor can increase failure diversity while changing detectability/calibration; primer diversity can protect against one amplification blind spot while reducing sequencing depth; a target-specific measurement can improve relevance while losing broader mechanism information; earlier capture can improve preservation while increasing annotation burden.

### 3. A falsifiable prospective prediction

The framework is not validated because its interface-specific remedies sound sensible. The decisive test is whether **pre-data diagnosis predicts intervention ranking** among equal-cost alternatives better than quantity-first or local-performance heuristics.

---

# What would falsify or weaken the C2 pitch

The TREE pitch should be weakened or redirected if prior work already provides all three of the following together:

1. the **claim-specific distinction-flow** formulation across preservation, separation, relevance and failure diversity;
2. an explicit mapping from the diagnosed bottleneck to a **measurement intervention class**, rather than another problem taxonomy;
3. a prospective test in which pre-data diagnosis predicts which equal-cost intervention class should produce the largest gain for a declared claim, with formal VoI/OED treated as a stronger baseline where a correctly specified full model is available.

Strong prior art for any one interface is expected and should be cited prominently.

# Proposal writing rule

Lead with external intellectual traditions and the conditional-locality synthesis, not repository names. The editor should be able to state the novelty without knowing the source programme:

> **The Opinion argues that familiar ecological performance metrics are conditional local quantities; evidential progress depends on whether their conditioning sets preserve and create the distinction required by the declared claim.**

Then give the practical test: diagnose the limiting interface before collecting more data and ask whether that diagnosis predicts the best equal-cost measurement expansion.
