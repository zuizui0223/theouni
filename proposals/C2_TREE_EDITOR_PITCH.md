# Editor-facing pitch — Trends in Ecology & Evolution

## Proposed Opinion

**When more measurement is not more evidence**

Ecologists and evolutionary biologists can now measure more often, more precisely and with increasingly automated tools. Yet extra measurements do not automatically strengthen the evidence for the question at hand. We propose an Opinion arguing that measurement becomes evidence through four distinct properties: **timely preservation, separation, relevance and failure diversity**. Missing these properties produces four recurrent failures. **Same-dimension failure (geometry):** measuring an already represented distinction more precisely need not separate competing mechanisms. **Wrong-target failure (objective):** a measurement can reveal more about the system overall while revealing less about the ecological quantity or decision that matters. **False-independence failure (dependence):** many repeated observations can still share one blind spot or failure domain. **Too-late failure (pipeline):** better downstream processing cannot recover a biological distinction that never entered the retained record.

The contribution is not another warning that “more data can be bad,” nor a universal evidence score. It is a **remedy-matched diagnostic** for deciding what kind of additional measurement could actually change an ecological or evolutionary conclusion. The four failures point to different next moves:

| diagnosed failure | question before collecting more data | appropriate next move |
|---|---|---|
| same dimension | does the proposed measurement separate a previously unresolved alternative? | measure a distinction that **separates an unresolved explanation**, not merely the old quantity more precisely |
| wrong target | can the new distinction change the declared prediction, contrast or decision? | measure **target-relevant information** rather than maximizing generic information |
| false independence | does the added observation create a genuinely **independent opportunity** for the relevant distinction to survive failure? | diversify failure domains rather than only increasing repeat count |
| too late | is the needed distinction still present in the retained record? | **capture it earlier**, or recalibrate if the distinction remains available |

The unifying ecological claim is therefore about the **flow of distinctions from biological opportunity to scientific responsibility**. A study can improve sample size, precision, information gain, replicate count or classifier accuracy while leaving the limiting distinction unresolved.

## Why now, and why this perspective

The issue is becoming more consequential as ecological inference increasingly combines automated sensors, remote sensing, environmental DNA, genomic assays, classifier outputs and multi-stage digital pipelines. These systems make it easy to increase data volume or downstream performance while leaving the relevant ecological distinction unresolved, target-irrelevant, non-independent or already lost upstream.

The proposal grows from a coordinated programme in ecological measurement design in which the author has worked across mechanism discrimination, target-relative observation design, repeated-observation failure structure and record-entry/representation boundaries. The Opinion does not ask readers to adopt those source methods; it uses the experience of confronting these failure modes together to connect mature literatures that are usually treated separately.

## Prior-art position

Each component has a mature literature. Structural-identifiability work distinguishes structural resolution from estimation precision (Villaverde et al. 2016). Targeted and goal-oriented experimental design, together with ecological value-of-information analysis, shows that information value depends on the prediction or decision of interest (Vanlier et al. 2012; Canessa et al. 2015; Attia et al. 2018). Ecological experimental design has long distinguished sample count from independent replication (Hurlbert 1984; Marshall 2024). Question-driven monitoring, imperfect-detection, calibration, ecological AI and metabarcoding literatures show that recorded data and downstream outputs inherit the structure and losses of earlier stages (Nichols & Williams 2006; Lindenmayer & Likens 2009; MacKenzie et al. 2002; Lahoz-Monfort et al. 2014; Dormann 2020; Alberdi et al. 2018; Chen et al. 2025; Cowans et al. 2026).

What is missing is a cross-cutting ecological diagnosis of **why** an additional measurement failed to become additional evidence. The failures are not interchangeable, and neither are their remedies: more precision cannot solve a separation problem; more total information cannot solve target mismatch; more repeats cannot solve shared dependence; and better downstream processing cannot recreate information deleted upstream.

Two worked examples make the synthesis concrete. In an island *Campanula* design, several mechanisms can remain compatible with the same coarse clinal pattern, so a targeted nectar-guide measurement can be more informative than simply increasing observations of the original pattern. In metabarcoding, deeper sequencing or a better classifier helps only if the focal taxon survived field sampling, extraction and amplification; when loss occurs earlier, the intervention must also move earlier. These are explicitly worked design examples, not new empirical-validation claims.

The framework is intended to travel across field sampling, biodiversity monitoring, sensor networks, experimental ecology, evolutionary inference and adaptive management. The practical message is deliberately sharper than “collect better data”:

> **Before collecting more data, ask what distinction the next measurement must create or preserve for the conclusion to change.**

## Proposed elements

- **Figure 1:** a measurement-to-evidence chain from biological opportunity to retained record, distinguishable alternatives and declared target; timely preservation, separation and relevance label the interfaces, while failure diversity spans the observation paths as a cross-cutting robustness layer.
- **Box 1:** island *Campanula* mechanism discrimination as a worked separation/relevance example.
- **Box 2:** metabarcoding as a worked preservation/failure-diversity example.
- **Outstanding questions:** how to infer shared failure structure, how robust target-relative evidence is to model misspecification, and how lost observation opportunities can be audited prospectively.

## Selected external anchors

1. Hurlbert SH. 1984. *Pseudoreplication and the Design of Ecological Field Experiments*. Ecological Monographs 54:187–211. DOI: 10.2307/1942661.
2. MacKenzie DI et al. 2002. *Estimating site occupancy rates when detection probabilities are less than one*. Ecology 83:2248–2255. DOI: 10.1890/0012-9658(2002)083[2248:ESORWD]2.0.CO;2.
3. Vanlier J et al. 2012. *A Bayesian approach to targeted experiment design*. Bioinformatics 28:1136–1142. DOI: 10.1093/bioinformatics/bts092.
4. Canessa S et al. 2015. *When do we need more data? A primer on calculating the value of information for applied ecologists*. Methods in Ecology and Evolution 6:1219–1228. DOI: 10.1111/2041-210X.12423.
5. Villaverde AF, Barreiro A, Papachristodoulou A. 2016. *Structural Identifiability of Dynamic Systems Biology Models*. PLOS Computational Biology 12:e1005153. DOI: 10.1371/journal.pcbi.1005153.
6. Attia A, Alexanderian A, Saibaba AK. 2018. *Goal-Oriented Optimal Design of Experiments for Large-Scale Bayesian Linear Inverse Problems*. Inverse Problems 34:095009. DOI: 10.1088/1361-6420/aad210.
7. Dormann CF. 2020. *Calibration of probability predictions from machine-learning and statistical models*. Global Ecology and Biogeography 29:760–765. DOI: 10.1111/geb.13070.
8. Cowans et al. 2026. *Improving the integration of artificial intelligence into existing ecological inference workflows*. Methods in Ecology and Evolution 17:228–237. DOI: 10.1111/2041-210X.14485.

A fuller novelty firewall is maintained in `proposals/C2_PRIOR_ART_MAP.md`.

## Source/novelty firewall

This Opinion owns only the cross-programme synthesis. The component results remain source-owned by Boundary (identification geometry), CED (target reportability and failure architecture), MROD (mechanism-learning observation design), REC (record-entry loss and irreversibility), and TNOA (semantic restraint and calibration semantics). Detailed algorithms, proofs and benchmarks remain in their source papers.

## Relationship to the Boundary Perspective proposal

The Boundary proposal asks the narrower question of whether mechanistic proximity and identification strength are distinct axes. If both routes proceed, the **Boundary paper retains the full identification theorem** and Γ–κ development; the TREE Opinion uses Boundary only as the qualitative **geometry-failure exemplar** within the broader measurement-to-evidence synthesis.
