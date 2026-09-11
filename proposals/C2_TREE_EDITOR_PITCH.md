# Editor-facing pitch — Trends in Ecology & Evolution

## Proposed Opinion

**More measurement is not more evidence: four failures of monotonic reasoning in ecology**

Ecology is becoming measurement-rich, but scientific evidence does not necessarily increase monotonically with measurement amount, precision, information or replication. We propose an Opinion organized around four structurally different failures of the common “more is better” intuition. **Geometry failure:** greater precision or repetition along an existing observation direction need not improve structural identification. **Objective failure:** an observation carrying more information about the latent world can be less useful for the declared ecological target. **Dependence failure:** repeated observations within one shared failure domain need not provide the guarantee supplied by independent failure opportunities. **Pipeline failure:** better downstream classification or inherited thresholds cannot necessarily restore distinctions or operating meaning lost earlier through record-entry selection or representation change.

The conceptual contribution is not a universal evidence score. It is a practical anti-monotonicity framework: each failure asks a different design question—did the measurement add a new identification direction, resolve a target-relevant distinction, diversify failure opportunities, or preserve the relevant distinction before irreversible loss? This framework connects identifiability, goal-directed measurement, failure dependence and observation-pipeline design without claiming that those component literatures are individually new.

## Prior-art position

The component warnings are well established, which is exactly why the synthesis can be useful. Structural-identifiability work already distinguishes estimability from identifiable model structure (e.g. Villaverde et al. 2016, DOI: 10.1371/journal.pcbi.1005153). Targeted and goal-oriented experimental design already optimize predictions or quantities of interest rather than all latent uncertainty (Vanlier et al. 2012, DOI: 10.1093/bioinformatics/bts092; Attia et al. 2018, DOI: 10.1088/1361-6420/aad210), while ecological value-of-information analysis asks whether collecting more data would actually improve a decision (Canessa et al. 2015, DOI: 10.1111/2041-210X.12423). Ecological experimental design has long distinguished nominal sample count from independent replication (Hurlbert 1984, DOI: 10.2307/1942661). Imperfect-detection, calibration and dataset-shift literatures likewise show that observed records and classifier outputs cannot be read naively as biological truth (e.g. MacKenzie et al. 2002; Dormann 2020).

What is missing is not another warning that “more data can fail.” We propose a common diagnostic that separates **why** it failed. The four failures are not interchangeable: additional precision cannot repair an identification-geometry problem; more entropy reduction cannot repair an objective mismatch; more repeats cannot repair shared failure dependence; and better downstream semantics cannot recreate upstream-deleted support. Each therefore implies a different remedy.

Two ecological worked examples make the synthesis concrete. A Campanula island-cline example shows how several mechanism structures remain compatible with the same published ordinal pattern and how a targeted nectar-guide measurement can separate them. An island-pollination translation example shows how signed functional position, effective service and complete service-to-response chains demand different observations; these are explicitly presented as measurement contracts rather than as new empirical findings.

We expect the Opinion to be useful beyond automated monitoring because the four failures apply to field sampling, sensor networks, experimental ecology, mechanistic inference and adaptive monitoring. The practical message is deliberately sharper than “collect better data”: **additional measurement becomes additional evidence only when it changes distinctions relevant to the scientific responsibility under a credible observation contract.**

## Proposed elements

- **Figure 1:** four non-monotonicity panels—same row span, wrong objective, shared failure, upstream collapse.
- **Box 1:** Campanula/Izu mechanism discrimination as a worked observation-design example.
- **Box 2:** island-pollination translation from ecological question to required measurement contract.
- **Outstanding questions:** how to estimate failure-domain structure, when target-relative evidence measures are robust to model misspecification, and how to audit lost opportunities prospectively.

## Selected external anchors

1. Hurlbert SH. 1984. *Pseudoreplication and the Design of Ecological Field Experiments*. Ecological Monographs 54:187–211. DOI: 10.2307/1942661.
2. MacKenzie DI et al. 2002. *Estimating site occupancy rates when detection probabilities are less than one*. Ecology 83:2248–2255. DOI: 10.1890/0012-9658(2002)083[2248:ESORWD]2.0.CO;2.
3. Vanlier J et al. 2012. *A Bayesian approach to targeted experiment design*. Bioinformatics 28:1136–1142. DOI: 10.1093/bioinformatics/bts092.
4. Canessa S et al. 2015. *When do we need more data? A primer on calculating the value of information for applied ecologists*. Methods in Ecology and Evolution 6:1219–1228. DOI: 10.1111/2041-210X.12423.
5. Villaverde AF, Barreiro A, Papachristodoulou A. 2016. *Structural Identifiability of Dynamic Systems Biology Models*. PLOS Computational Biology 12:e1005153. DOI: 10.1371/journal.pcbi.1005153.
6. Attia A, Alexanderian A, Saibaba AK. 2018. *Goal-Oriented Optimal Design of Experiments for Large-Scale Bayesian Linear Inverse Problems*. Inverse Problems 34. DOI: 10.1088/1361-6420/aad210.
7. Dormann CF. 2020. *Calibration of probability predictions from machine-learning and statistical models*. Global Ecology and Biogeography 29:760–765. DOI: 10.1111/geb.13070.

A fuller novelty firewall is maintained in `proposals/C2_PRIOR_ART_MAP.md`.

## Source/novelty firewall

This Opinion owns only the cross-programme synthesis. The component results remain source-owned by Boundary (identification geometry), CED (target reportability and failure architecture), MROD (mechanism-learning observation design), REC (record-entry loss and irreversibility), and TNOA (semantic restraint and calibration semantics). Detailed algorithms, proofs and benchmarks remain in their source papers.

## Relationship to the Boundary Perspective proposal

The Boundary proposal asks one narrower question: whether mechanistic proximity and identification strength are distinct axes. If both routes proceed, the Boundary paper retains the full identification theorem/Γ–κ development; the TREE Opinion uses that work only as the geometry-failure exemplar within the broader anti-monotonicity synthesis.
