<!-- draft-id: chapter:1:v0.1 -->
# 観測が原理的に届かない範囲

*English working title: Where Observation Cannot Reach in Principle*

> **Draft status:** source-bounded v0.1 from Boundary snapshot `d950cf9fe4d21d4677f1e16f29e8fbe3c7af8f84`. The chapter owns an identification boundary under declared observation models. It does not claim that biologically richer measurements are generally uninformative or that unidentifiable mechanisms do not exist.

## 1. Mechanistic proximity and identification strength are different questions

Ecology often treats a measurement as more mechanistic when it lies closer to biological machinery. Physiological rates, genomic states, molecular interactions and direct process measurements can indeed reveal structures that coarse endpoint observations do not. But biological proximity and identification strength answer different questions.

The first asks where a measurement sits in the biological chain. The second asks whether the observation distinguishes the competing mechanisms relevant to the inference. A proximal measurement can be shared by several mechanisms and therefore remain non-identifying. Conversely, a relatively simple field observation can be highly discriminating when alternative mechanisms make different predictions for it. [B1]

The forbidden inference of this chapter is therefore:

> **観測を豊かにした ⇒ 潜在機構に近づいた**

Here “richer” cannot mean merely more precise, higher-dimensional or biologically closer. To move closer in the inferential sense, the observation map must break an equivalence among mechanisms that was previously preserved.

This distinction matters because ecological studies frequently contain many observations without containing the particular observation needed to identify a mechanism. A field system may have detailed plant traits, visitor identities, community composition and interaction frequencies, yet still fail to identify the mechanism connecting community change to reproduction if per-interaction effectiveness or reproductive dependency is absent from the same inferential chain. The resulting problem is not a lack of data in general. It is a lack of the right identifying coordinate. [B2]

The appropriate output in that case is not an unqualified mechanistic story. It is a boundary statement: which mechanism distinctions remain compatible with the observation map, which additional measurements would reduce that ambiguity, and which conclusions remain not evaluable.

## 2. Endpoint-only observation can leave a continuous mechanism-equivalence class

Boundary makes this argument exact for a recurring positive multiplicative architecture. Let a declared ecological output be

\[
W(z)=\prod_{j=1}^{k}F_j(z),\qquad F_j(z)>0.
\]

The factorization is not assumed for all ecological processes. It is a conditional model: when investigators already represent a response as a product of positive stages, what can observation of the product identify about the stages?

Suppose the observation depends only on the net output \(W\), possibly through a deterministic functional \(\Phi(W)\). For any positive multipliers \(c_j\) satisfying

\[
\prod_{j=1}^{k}c_j=1,
\]

the transformation

\[
F_j\mapsto c_jF_j
\]

leaves \(W\) unchanged. In log coordinates the admissible perturbations satisfy

\[
\sum_{j=1}^{k}d_j=0,
\]

which defines a \((k-1)\)-dimensional product-preserving subspace. Endpoint-only observation therefore leaves a \((k-1)\)-dimensional mechanism-equivalence class. [B3]

The two-channel case makes the point visually obvious. If

\[
W=FE,
\]

then for any positive function \(c\),

\[
(F,E)\mapsto(cF,E/c)
\]

leaves the product unchanged. An arbitrarily precise observation of \(W\) cannot tell which point on that orbit generated the product. More endpoint precision shrinks sampling uncertainty around the same invariant map; it does not break the structural equivalence.

This is the first direct failure of the chapter's forbidden inference. Richer observation in the sense of more accurate endpoint measurement can leave the mechanism-identification problem exactly unchanged.

## 3. Direct channel anchors reduce the unidentified dimension one coordinate at a time

The same model gives a constructive field-design rule. If \(r\) independent channel values, or independent channel ratios in a before/after comparison, are observed directly, then each fixes one independent coordinate. The remaining unidentified dimension is

\[
\boxed{k-1-r},\qquad 0\le r\le k-1.
\]

When \(r=k-1\), the final stage is recovered from the product, so all stages are point-identified within the declared model. [B3]

This formula turns a vague call for “more mechanistic data” into a countable design question. For a four-stage chain observed only at its endpoint, three structural degrees of freedom remain. One independent channel anchor leaves two. Two anchors leave one. Three point-identify the remaining channel from the product.

The result does not rank biological measurement technologies. It says what kind of information an observation must supply relative to the equivalence class. A molecular variable that varies only along an already observed coordinate may add biological detail without reducing \(k-1-r\). A field measurement that directly fixes one missing channel can reduce the dimension by one even if it is biologically less proximal.

The Boundary implementation and regression tests check this dimension formula across multiple channel/anchor combinations and fail closed when an impossible number of independent anchors is requested. [B4] The point of the executable layer is not numerical approximation; it is to ensure that the chapter's qualitative language remains attached to the exact dimension rule rather than drifting into “more data is better” rhetoric.

## 4. A joint-measurement bottleneck can survive a data-rich field programme

The algebra becomes ecologically consequential when an inferential chain contains several named stages that are often measured in separate studies or at different units.

Consider pollination as one example. For visitor type \(m\), an effective contribution may be represented as

\[
S_m=V_mE_m,
\]

where \(V_m\) is interaction quantity such as visitation rate and \(E_m\) is per-interaction effectiveness. Community service may then aggregate contributions across visitor types. Further downstream, realized reproduction may also depend on plant reproductive dependency, pollen limitation, autonomous selfing or other stages.

Visitor identity is not the same object as effective service. Interaction quantity is not per-visit effectiveness. Effective service is not reproductive dependency. A final reproductive contrast does not reveal which unobserved link changed.

A study can therefore be “data rich” while mechanism identification remains structurally poor. If community composition and visitation are measured but effectiveness is not, the quantity-quality allocation remains ambiguous. If effective service is measured but reproductive dependency is not, the mechanism linking service to realized reproduction can remain ambiguous. Adding more records of the already observed stages need not close the missing coordinate.

This is the joint-measurement bottleneck recovered from the Boundary introduction. [B2] It is especially useful for the dissertation because it shows that the identification result is not merely a property of algebraic toy models. The mathematical object tells us what a field design must jointly observe if it wants to distinguish the declared alternatives.

The correct scientific response to a missing joint measurement is fail-closed. The result should be classified as not evaluable for the mechanistic contrast rather than repaired after the fact by promoting a nearby proxy into the missing stage.

## 5. Proxies introduce a second problem: calibration transport

Even when one channel has a proxy, identification can depend on whether the proxy-to-channel relation transports across regimes.

Let

\[
W_i=F_iE_i,
\qquad
X_i=q_iF_i,
\qquad i\in\{0,1\},
\]

with positive quantities. Define ratios

\[
\rho_W=W_1/W_0,
\quad
\rho_X=X_1/X_0,
\quad
\rho_F=F_1/F_0,
\quad
\rho_E=E_1/E_0,
\quad
\kappa=q_1/q_0.
\]

Then

\[
\rho_F=\rho_X/\kappa,
\qquad
\rho_E=(\rho_W/\rho_X)\kappa.
\]

A ratio does not eliminate calibration change unless \(\kappa=1\). Stable calibration is therefore an identifying assumption, not a mathematical consequence of taking relative changes.

Boundary places stable, bounded and unrestricted calibration transport in one family by declaring

\[
1/\Gamma\le\kappa\le\Gamma,
\qquad \Gamma\ge1.
\]

For finite \(\Gamma\), the sharp joint identified set is

\[
J_\Gamma=
\{(\rho_X/\kappa,\widehat{\rho}_E\kappa):
1/\Gamma\le\kappa\le\Gamma\},
\]

where \(\widehat{\rho}_E=\rho_W/\rho_X\) is the stable-calibration value. [B5]

Three cases follow continuously:

- \(\Gamma=1\): point identification under stable calibration;
- finite \(\Gamma>1\): sharp partial identification;
- unrestricted transport: non-identification.

The identified object is a coupled joint set. The same \(\kappa\) moves one channel ratio upward and the other downward while preserving their product. Reporting the two marginal intervals as if they could vary independently would therefore invent combinations that are not compatible with the declared model.

## 6. Breakdown factors turn hidden calibration assumptions into sensitivity statements

A finite transport bound is generally not identified from the same observations whose identifying power is under study. It must come from calibration data, prior validation, instrument knowledge or an explicit sensitivity analysis.

For a stable-calibration estimate \(\widehat\rho\), Boundary defines the smallest symmetric multiplicative calibration distortion needed to reach no change as

\[
\Gamma^*=\max(\widehat\rho,1/\widehat\rho),
\qquad
\eta^*=|\log\widehat\rho|.
\]

The expression is invariant to reversing the reference regime. [B6]

This changes the role of an assumption. Instead of choosing one convenient \(\Gamma\) and speaking as though it were known, the analyst can report the breakpoint at which a directional conclusion ceases to be robust. If the observed ratio implies \(\Gamma^*=1.34\), the conclusion survives symmetric calibration-ratio drift smaller than the corresponding boundary and is overturned at or beyond that sensitivity threshold under the declared model.

This is partial identification used constructively. The output is not “we cannot know.” It is “the conclusion is identified only within this region of the calibration assumption, and here is the exact breakpoint.”

## 7. Two anchor ladders solve different identification problems

Boundary uses the word anchor for two distinct interventions on uncertainty.

**Channel anchors** directly observe latent stages in the product chain. With \(r\) independent channel anchors, the residual mechanism dimension becomes \(k-1-r\).

**Calibration anchors** observe the proxy conversion itself. Zero calibration anchors leave cross-regime conversion transport unrestricted unless externally bounded. One anchor identifies conversion locally but does not by itself identify cross-regime drift. Two regime-specific anchors measure both \(q_0\) and \(q_1\), so \(\kappa=q_1/q_0\) is directly measured for the comparison.

Conflating these ladders would create another forbidden inference: measuring a proxy more directly is not necessarily the same as measuring the latent ecological channel the proxy represents. The first can remove calibration uncertainty; the second can remove mechanism-equivalence dimensions. [B7]

The design principle is therefore specific: measure the information missing for the inference you want to make.

## 8. What this chapter establishes—and what it does not

The chapter establishes an identification boundary under declared multiplicative/channel and proxy-calibration models.

It establishes that:

1. net-only observation of a positive \(k\)-stage product leaves \(k-1\) mechanism dimensions unresolved;
2. \(r\) independent direct channel anchors leave \(k-1-r\);
3. richer endpoint precision does not change this structural dimension when the observation map remains invariant;
4. calibration transport creates a point/partial/non-identification family;
5. calibration uncertainty must be represented as a coupled joint set;
6. breakdown factors expose how much calibration drift overturns a conclusion;
7. field design can target channel anchors and calibration anchors according to the specific identification gap.

It does **not** establish that molecular or genomic measurements are generally weak evidence. It does not establish that field observations are generally stronger. It does not infer a latent mechanism when the observation map leaves several compatible. It does not prove that every ecological chain is multiplicative. It does not convert a partial identified set into a point estimate. It does not infer the correct \(\Gamma\) from the endpoint/proxy data alone. [B8]

The broader lesson is narrower than “more observation is not useful.” More observation is useful when it changes the distinctions that the observation map can support. Richness measured along an invariant direction can leave identification unchanged; a strategically chosen anchor can change the inferential object immediately.

## 9. Transition: identification is not prediction

After this chapter, one shortcut is closed. Biological proximity, dimensionality and precision cannot by themselves certify mechanism identification.

But this leaves a different scientific responsibility unresolved. Suppose an observed signal is real and reproducible. Even if it does not identify the mechanism that generated it, the signal might still be useful if it predicts a consequential future event. Identification and prediction are different estimands. The failure of one does not prove failure of the other. [TR]

Chapter 2 therefore asks a new question rather than drawing a consequence from Chapter 1:

> **If a signal consistently appears before ecological loss, does that temporal precedence make it a warning?**

The answer requires event and non-event denominators, discrimination and a warning-specific validity contract—not more mechanism identification.

## Internal source keys

- **[B1]** Boundary `paper/manuscript.md`, Abstract and Introduction — biological proximity versus identification strength.
- **[B2]** Boundary `paper/manuscript.md`, Introduction — joint-measurement bottleneck and fail-closed `not evaluable` interpretation.
- **[B3]** Boundary `paper/manuscript.md`, Theorems N1/N1-k — product-preserving invariance and `k-1-r` dimension.
- **[B4]** Boundary `tests/test_identification_obligations.py`, `tests/test_boundary_core.py` — exhaustive/edge regression checks, gauge basis, anchor validation and breakdown invariance.
- **[B5]** Boundary `paper/manuscript.md`, Theorem T1 — sharp joint calibration-transport identified set.
- **[B6]** Boundary `paper/manuscript.md`, breakdown factor section; tests of reciprocal reference invariance.
- **[B7]** Boundary `paper/manuscript.md`, channel-anchor versus calibration-anchor ladder.
- **[B8]** `thesis/verification_recovery_registry.json`, Chapter 1 claim ceiling; Boundary discussion limits.
- **[TR]** `thesis/transition_recovery_matrix.json`, Chapter 1→2 handoff — identification and warning discrimination are orthogonal estimands; transition is not theorem implication.
