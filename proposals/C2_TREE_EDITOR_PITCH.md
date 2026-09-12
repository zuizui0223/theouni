# Editor-facing pitch — Trends in Ecology & Evolution

## Proposed Opinion

**More measurement is not more evidence: four failures of monotonic reasoning in ecology**

Ecologists can now measure more often, more precisely and with increasingly automated tools. Yet extra measurements do not automatically strengthen the evidence for the question at hand. We propose an Opinion built around four recurrent ways that the intuitive rule “more is better” breaks. **Same-dimension failure (geometry):** measuring an already observed quantity more precisely need not separate competing ecological mechanisms. **Wrong-target failure (objective):** a measurement can reveal more about the system overall while revealing less about the particular ecological quantity or decision we care about. **False-independence failure (dependence):** many repeated observations can still share the same blind spot or failure mode. **Too-late failure (pipeline):** better downstream classification cannot recover events or distinctions that never entered the retained record, and thresholds can lose their meaning when representations change.

The contribution is not another warning that “more data can be bad,” nor a universal evidence score. It is a **remedy-matched diagnostic** for deciding what kind of additional measurement could actually change an ecological conclusion. The four failures point to four different next moves:

| diagnosed failure | question before collecting more data | appropriate next move |
|---|---|---|
| same dimension | does the new measurement separate a previously unresolved alternative? | add a new identification direction, not merely precision on the old one |
| wrong target | can the new distinction change the declared prediction or decision? | measure target-relevant information rather than maximizing generic information |
| shared dependence | does the added observation create a genuinely independent opportunity for evidence to survive failure? | diversify failure domains rather than only increasing repeat count |
| upstream loss | is the needed distinction still present in the retained record? | capture it earlier in the pipeline; downstream accuracy cannot recreate deleted information |

This mapping is the unifying ecological claim: a measurement can fail to become evidence for different structural reasons, and diagnosing the wrong reason leads to the wrong remedy.

## Prior-art position

Each component has a mature literature. Structural-identifiability work distinguishes structural resolution from estimation precision (Villaverde et al. 2016). Targeted and goal-oriented experimental design, together with ecological value-of-information analysis, shows that information value depends on the prediction or decision of interest (Vanlier et al. 2012; Canessa et al. 2015; Attia et al. 2018). Ecological experimental design has long distinguished sample count from independent replication (Hurlbert 1984). Imperfect-detection, calibration and dataset-shift literatures show that observed records and classifier outputs cannot be read naively as biological truth (MacKenzie et al. 2002; Dormann 2020).

What is missing is a cross-cutting ecological diagnosis of **why** an additional measurement failed to become additional evidence. The four failures are not interchangeable, and neither are their remedies: more precision cannot solve a missing-identification-direction problem; more total information cannot solve a target mismatch; more repeats cannot solve shared dependence; and a better downstream classifier cannot recreate information deleted upstream.

Two worked ecological examples make the synthesis concrete. In an island *Campanula* system, several mechanism structures can remain compatible with the same coarse clinal pattern, so a targeted nectar-guide measurement can be more informative than simply increasing observations of the original pattern. In island pollination, questions about pollinator occurrence, effective service and service-to-reproduction links require different observations; collecting more of one kind does not substitute for measuring another link in the chain. These are explicitly worked design examples, not new empirical-validation claims.

The framework is intended to travel across field sampling, biodiversity monitoring, sensor networks, experimental ecology, mechanistic inference and adaptive management. The practical message is deliberately sharper than “collect better data”:

> **Additional measurement becomes additional evidence only when it preserves or creates a distinction that can change the ecological question being asked.**

## Proposed elements

- **Figure 1:** the central decision map: each of the four failures leads to a different diagnostic question and a different next measurement action.
- **Box 1:** island *Campanula* mechanism discrimination as a worked observation-design example.
- **Box 2:** island pollination from ecological question to required measurement.
- **Outstanding questions:** how to infer shared failure structure, how robust target-relative evidence is to model misspecification, and how lost observation opportunities can be audited prospectively.

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

The Boundary proposal asks the narrower question of whether mechanistic proximity and identification strength are distinct axes. If both routes proceed, the Boundary paper retains the full identification theorem and Γ–κ development; the TREE Opinion uses Boundary only as the geometry-failure exemplar within the broader four-failure synthesis.
