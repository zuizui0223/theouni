<!-- draft-id: chapter:4:v0.1 -->
# 一つの系に、状態は一つではない

*English working title: One System Does Not Have One State*

> **Draft status:** theorem-refreshed source-bounded v0.1 from eco-genetic-criticality snapshot `2a35b2d2b11f4b8a00b8a4346bdba90773511a71`. The chapter no longer rests on the weak observation that different variables can behave differently. Its formal question is when several declared eco-genetic target responsibilities can be represented exactly by one directionally coherent scalar state, and its locked finite-model evidence supplies a crossing that violates that condition.

## 1. A single eco-genetic summary can answer the wrong state question

Ecological systems are routinely compressed into a small number of variables: abundance, occupancy, interaction strength, genetic diversity, trait composition, or a composite health score. Compression is unavoidable. The scientific problem begins when a summary that was adequate for one responsibility is silently treated as a sufficient state for several different responsibilities.

A population may remain occupied while the present interaction environment no longer supports its long-term trait configuration. Genetic diversity may decline without demographic disappearance. An allele may persist while realised ecological function changes. Conversely, a coarse aggregate can move monotonically even when one of its components reverses direction. These possibilities are familiar enough that simply listing them would not make a strong chapter.

The forbidden inference is therefore sharpened from a slogan into an existence question:

> **生態遺伝的に要約した ⇒ 五つの側面を代表した**

The source programme distinguishes five target-facing responsibilities: potential viability, realised occupancy, demographic state, genetic diversity, and allele persistence. The chapter asks something stronger than whether these variables have different names or units. It asks:

> **When does there exist one scalar state whose order and value are sufficient to reconstruct every declared target without reversing their ecological direction?**

This is an exact representability question. If such a scalar exists, then a one-dimensional state can in principle be scientifically adequate for the declared target set. If it does not, then the failure is not stylistic preference for multidimensional plots. It is a structural impossibility under the declared directional responsibility.

## 2. The common-scalar theorem

Let the finite set of model states be `Omega`. For each state `omega`, collect the declared target responsibilities into a vector

\[
T(\omega)=(T_1(\omega),\ldots,T_m(\omega)).
\]

Orient each coordinate in advance so that a larger value means "no worse" for that responsibility. The orientation is part of the scientific contract; it is not chosen after inspecting which scalarization is convenient.

Call a scalar `h:Omega->R` an **exact directionally coherent sufficient scalar** when, for every target coordinate `j`, there is a nondecreasing function `f_j` such that

\[
T_j=f_j\circ h.
\]

This requires two things simultaneously. First, the scalar is sufficient: knowing `h` is enough to recover every declared target value. Second, the scalar order is directionally coherent: moving upward on the scalar cannot make one declared target worse while another target reconstruction treats the same move as better.

The source theorem proves the following necessary-and-sufficient condition.

> **Common-scalar theorem.** An exact directionally coherent sufficient scalar exists **if and only if** the distinct target vectors `T(omega)` form a chain under coordinatewise product order.

Here `u <= v` in product order means `u_j <= v_j` for every target coordinate. A chain means every pair of distinct target vectors is comparable: for any two states, either all declared targets are no worse in the first state than the second, or all are no worse in the second than the first.

### Necessity

Assume an exact directionally coherent scalar `h` exists. Take any two model states `omega` and `omega'`. Their scalar values are comparable because real numbers are totally ordered. Suppose `h(omega)<=h(omega')`. Since every reconstruction function `f_j` is nondecreasing,

\[
T_j(\omega)=f_j(h(\omega))\le f_j(h(\omega'))=T_j(\omega')
\]

for every coordinate `j`. Therefore `T(omega)<=T(omega')` in product order. Reversing the scalar inequality gives the reverse product order. Thus every pair of target vectors must be comparable. The target vectors form a chain.

This proves that one crossing pair is enough to reject an exact common monotone scalar. If one target improves while another worsens between two states, no re-labeling of those states on one directionally coherent scalar can reconstruct both targets monotonically.

### Sufficiency

Now suppose the distinct target vectors form a finite product-order chain. Order those distinct vectors from lowest to highest and assign them scalar ranks `0,1,...,r-1`. Give every model state the rank of its target vector. For each target coordinate `j`, define `f_j` on the ranks by the corresponding coordinate of the ranked target vector. Because the vectors form a product-order chain, each coordinate sequence is nondecreasing. Hence each `f_j` is nondecreasing and reconstructs `T_j` exactly.

So the condition is not merely a way to reject scalar indices. It also tells us when an exact scalar is possible and constructs one. The result is therefore a boundary theorem, not a preference for multidimensional descriptions.

## 3. A crossing is an impossibility certificate, not just a different response shape

The theorem changes how the fragmentation results should be read. Previously the safe conclusion was that potential viability, realised occupancy, interaction, effective size, and high-trait mass did not all share one response curve. That is true, but it is weaker than what the locked results permit.

The fresh H3 fragmentation gradient contains an explicit crossing between two and sixteen isolated patches. Relative to the paired one-patch source, the pooled median retained interaction changes from approximately

\[
0.001744\quad\text{at two patches}
\]

to

\[
0.001244\quad\text{at sixteen patches},
\]

so interaction becomes lower. Retained local effective size likewise falls from approximately

\[
0.221311
\]

to

\[
0.033058.
\]

But realised high-trait mass moves in the opposite direction, from approximately

\[
0.282918
\]

to

\[
0.393880.
\]

After orienting all three quantities so that higher means no worse, neither the two-patch target vector nor the sixteen-patch target vector dominates the other. One state has better interaction and effective size; the other has more realised high-trait mass. The pair is incomparable in product order.

Therefore the theorem applies directly:

> **No exact directionally coherent scalar can simultaneously reconstruct these declared targets over the locked states containing this crossing pair.**

This conclusion is stronger than “the variables have different shapes.” It proves non-existence of a particular class of common state representation on the frozen finite-model evidence. It also remains bounded: approximate scores, target-specific scores, and arbitrary injective encodings are not ruled out.

## 4. Potential viability is not realised occupancy

The common-scalar result is complemented by a particularly sharp state separation. The preregistered fresh-seed sensitivity projected 1,037 independently prepared high-state sources into one, two, three, four, six, eight, twelve, and sixteen equal isolated patches.

In the one-patch condition, potential high-trait viability was present in

\[
1037/1037
\]

supported outcomes. At every tested subdivision from two through sixteen patches, potential high-trait viability was absent in

\[
1037/1037
\]

outcomes.

If potential viability and realised occupancy were interchangeable state labels, realised high-trait occupancy would have to disappear together with this viability transition. It did not. At the 30-generation endpoint, realised high-trait occupancy persisted in approximately 99.6–100% of supported trajectories across the subdivided conditions.

This gives a direct finite Type S separation:

> the declared environment can cease to support the potential high-trait component while the carried realised state remains occupied over the tested horizon.

The conclusion is not a universal lag theorem. It does not state that occupancy always persists for a fixed duration after viability loss. It establishes that these two responsibilities are not identical within the declared closure.

## 5. Keep theorem, closure, hypothesis, and simulation evidence separate

The source programme uses four evidence labels. A **Type T** statement is an exact theorem under explicit mathematical assumptions. A **Type C** result follows only after a particular ecological or life-cycle closure is declared. A **Type H** statement is a dynamic hypothesis. A **Type S** result is numerical evidence from a declared finite simulation.

This taxonomy prevents the common-scalar theorem from being overextended. The theorem is exact for a declared finite target table and directional orientation. The H3 crossing is finite-model evidence that the theorem's chain condition fails in the locked gradient. Neither component alone establishes that all natural ecosystems lack a scalar state.

Likewise, the canonical positive-feedback fixed-point theorem is exact for its stated map, not for every ecological system. A row-stochastic migration bound is exact for the declared mixing operator, not a theorem of demographic rescue. A 30-generation state separation is evidence at that horizon, not an infinite-time law.

## 6. Response-shape divergence is still biologically informative

At two patches, the pooled paired median retained fractions relative to the one-patch source were approximately 0.001744 for interaction, 0.221311 for local effective size, and 0.282918 for realised high-trait mass. All three were below their paired one-patch value in 1,037/1,037 supported sources.

The subsequent response shapes diverged. Interaction and local effective size continued to decline with patch count in every frozen primary cell. Realised high-trait mass instead showed a sharp initial reduction followed by partial recovery, reaching about 0.3018 at four patches and 0.3939 at sixteen patches.

This response-shape divergence now has two roles. Biologically, it distinguishes environmental support, local demographic capacity, and realised carried trait state. Formally, the opposite direction between interaction/effective size and realised mass supplies the crossing needed for the scalar impossibility result.

The scientific question therefore determines which quantity is a state variable. If the responsibility is potential trait support, realised occupancy is insufficient. If the responsibility is finite-time presence, potential viability is insufficient. If the responsibility is local genetic variation or allele persistence, both may be insufficient.

## 7. Diversity and allele persistence are not demographic synonyms

The finite model tracks local diversity, metapopulation diversity, allele frequencies, persistence, and differentiation separately. This matters because deterministic migration, finite drift, mutation, local effective size, and demographic turnover can affect these outputs differently.

For example, a row-stochastic migration operator can preserve a common allele-frequency floor under its exact assumptions without proving demographic rescue, trait rescue, or long-run diversity preservation. A decline in local effective size can increase expected stochastic erosion without implying immediate loss of every allele. Conversely, an allele can persist while its frequency, local diversity contribution, and ecological function change.

The common-scalar theorem says how these quantities could be compressed exactly if their declared target vectors were chain-ordered. The H3 crossing shows that at least part of the current target set does not satisfy that condition. It does not require every pair among all five named responsibilities to be incomparable.

## 8. Coarse marginals can agree while the next transition differs

A second structural counterexample shows why even a multidimensional summary can be insufficient when it erases response-relevant alignment.

The source programme constructs simulator states that agree in common coarse summaries, including census, interaction and allele-frequency marginals, realised trait-bin state, `H_alpha`, `H_gamma`, and `F_ST`, but differ in patchwise cross-layer alignment. Because the exact next interaction update depends on that alignment, the next transition can differ despite agreement in the listed marginals.

The safe conclusion is:

> matching common coarse marginals need not imply transition equivalence.

The long-horizon campaign did not establish a universal directional effect of one alignment pattern on loss incidence. That negative boundary is important. The representation counterexample establishes insufficiency of the coarse summary for an exact next response; it does not establish a universal natural risk direction.

## 9. TU-3: when raw detail is nuisance and when forgetting becomes invalid

TU-3 gives the representation-level condition complementary to the scalar theorem. Let a richer representation `B` map onto a coarser representation `A` through a surjection

\[
\pi:\Omega_B\twoheadrightarrow\Omega_A.
\]

Let `sigma_B` encode the declared loss-response responsibility. A coarse representation is loss-faithful exactly when `sigma_B` is constant on every fiber of `pi`, equivalently when

\[
\sigma_B=\sigma_A\circ\pi
\]

for some coarse signature `sigma_A`.

Thus a coordinate is nuisance only while forgetting it does not merge states with different required responses. TU-3 constructs arbitrary nuisance inflation: raw state can be enlarged by `m` irrelevant binary coordinates while the required loss quotient remains unchanged. Conversely, one hidden response-relevant coordinate is enough to violate fiber homogeneity and make the projection insufficient.

The common-scalar theorem and TU-3 answer different questions. The scalar theorem asks whether several target responses can be placed on one directionally coherent sufficient axis. TU-3 asks whether a particular raw representation coordinate can be forgotten for one declared response signature. Neither says that a complete simulator state is the natural state of the ecosystem.

## 10. What this chapter establishes—and what it does not

The chapter now establishes four levels of result.

First, it proves an exact necessary-and-sufficient condition for one directionally coherent scalar to preserve a finite declared set of target responses: the target vectors must form a product-order chain.

Second, it applies that condition to locked H3 finite-model evidence. The two-versus-sixteen-patch crossing violates chain comparability, so no exact common monotone scalar can preserve the crossed targets on that state set.

Third, independent H3 evidence separates potential viability from realised occupancy: viability is absent after every tested subdivision while occupancy remains in approximately 99.6–100% of supported finite trajectories.

Fourth, the alignment counterexample and TU-3 show that even familiar multidimensional marginals can omit a coordinate needed for a declared next response.

The chapter does **not** establish that all five state categories are pairwise distinct in every configuration. It does not claim they are a complete ontology for natural ecosystems. It does not rule out approximate composite indices. It does not prove a universal fragmentation threshold, a universal lag law, a universal alignment-risk direction, or empirical natural-state adequacy. The theorem and the finite evidence are only as broad as their declared carriers and target contracts.

The safe positive conclusion is therefore not merely “one system has many states.” It is:

> **A common eco-genetic scalar is exact only under an explicit order condition. When declared targets cross, the scalar representation fails; when a proposed coarse projection merges response-different worlds, that projection fails. State adequacy must therefore be earned relative to the responsibility being preserved.**

## 11. Transition: from multiple target responsibilities to open futures

Chapter 3 showed that the best next measurement can depend on the ambiguity being resolved. Chapter 4 now shows that the state representation itself can depend on which target responses must be preserved, and gives an exact condition for when those responses can share one scalar.

The next question changes from target multiplicity to future grammar. Suppose a compact state or interface is adequate under a restricted set of legal futures. What happens when previously forbidden future actions or compositions become legal? Can a narrow physical boundary guarantee a small causal memory burden?

Chapter 5 asks:

> **When the future grammar is opened, how much additional causal memory can be forced even across a narrow physical boundary?**

This is an editorial handoff, not a theorem implication. The H3 crossing does not prove CCOC's memory lower bound; CCOC owns a separate finite extremal construction.

## Internal source keys

- **[SCALAR]** eco-genetic-criticality `docs/common_scalar_state_theorem_2026-09-03.md` — product-order chain iff exact directionally coherent scalar; constructive sufficiency and crossing impossibility certificate.
- **[SCALAR-TEST]** `tests/test_common_scalar_state_theorem.py` — exhaustive finite scalar-label oracle and locked H3 crossing check.
- **[G1]** eco-genetic-criticality `manuscript/main_text.md` — state-separation programme and Type T/C/H/S taxonomy.
- **[G2]** `docs/H3_FRAGMENTATION_GRADIENT_SENSITIVITY_RESULTS.md` — 1,037-source gradient, viability/occupancy separation, retained response values and crossing.
- **[G3]** source README/manuscript alignment audit — coarse marginals matched, exact next interaction differs; no universal directional loss-incidence claim.
- **[T3]** `theory/TU3_LOSS_STATE_INVARIANCE.md` and `theory/verify_tu3.py` — fiber homogeneity, nuisance inflation and hidden response-relevant coordinate failure.
- **[TR]** `thesis/transition_recovery_matrix.json`, Chapter 4→5 question handoff.
