<!-- draft-id: chapter:8:v0.1 -->
# 反復は、多様性の代わりにならない

*English working title: Repetition Does Not Substitute for Diversity*

> **Draft status:** source-bounded v0.1 from CED snapshot `590f6459a7c3ef31e8a527319771fd3d736a704a`. The chapter concerns finite evidence under a declared common-mode imperfect-detection contract. It proves a finite-effort repeat-versus-mode allocation boundary and a separate worst-case availability ceiling. It does not infer failure domains, availability, or sensitivity from data.

## 1. Replicate count is not yet an evidence architecture

Ecological monitoring often reports effort through counts: number of cameras, visits, PCR replicates, quadrats, dates, observers, or repeated reads. More replicates usually sound like stronger evidence. But replicate count alone does not say whether those observations fail independently.

Ten camera clips collected during the same power outage do not create ten independent opportunities to see an animal. Ten laboratory repeats sharing one extraction failure do not create ten independent extractions. Repeated surveys made by one route in one weather window can share a failure cause that another observer, date, instrument, or route would not share.

The forbidden inference of this chapter is:

> **同じ手法を繰り返した ⇒ 証拠が強くなった**

The first useful correction is familiar: repeated observations can be correlated. That statement alone is too weak for this dissertation. CED asks a design question with a quantitative answer:

> **At the same finite read effort, when is it better to deepen repetition inside one failure mode, and when is it better to create an independent failure opportunity?**

The answer is not “always diversify.” Under the declared two-read comparison, the preferred design reverses at an exact sensitivity threshold. At larger effort, a second theorem shows why unlimited repetition inside a fixed number of modes eventually hits a worst-case availability ceiling. [C1,C2]

Together these results replace a slogan with a depth-versus-diversity design law.

## 2. The observation contract separates mode failure from read failure

Let \(k\ge1\) denote truly present target coordinates. A coordinate might represent one species, allele, interaction, feature, or other prespecified binary component whose presence must be detected.

Let \(m\) denote declared failure modes. A mode can represent a camera–power–weather domain, sampling date, observer route, laboratory batch, or another observation context that can fail jointly across all coordinates assigned to it.

CED's probabilistic contract separates two layers.

First, each mode is operational with probability at least \(a\), independently across declared modes. If a mode fails, every observation assigned to that mode is negative for every coordinate.

Second, conditional on a mode operating, each read detects a truly present coordinate with probability at least \(p\), with reads conditionally independent and no false positives. [C2]

These assumptions are declared. They are not estimated from the same observations and then treated as exact. The theorems therefore yield **worst-case guarantees over the declared lower-bound contract**, not unconstrained estimates of realized field detection.

This type discipline matters because within-mode repetition and cross-mode diversification attack different failure mechanisms. Repetition improves sensitivity conditional on an operating mode. Diversification reduces exposure to the event that the only mode fails entirely.

## 3. The exact joint-detection frontier keeps both mechanisms visible

Let each operating mode take \(r\) reads per coordinate and define

\[
q_r=(1-p)^r,
\]

the probability that one truly present coordinate is missed by all \(r\) reads conditional on mode operation.

CED's exact least-favourable joint-detection theorem gives, for \(m\) independent modes and \(k\) truly present coordinates, the contract guarantee

\[
G(k,m,r;a,p)
=
\sum_{s=0}^{k}(-1)^s {k\choose s}
\left[1-a+a q_r^s\right]^m.
\]

The expression is exact when mode availability and read sensitivity equal their declared lower bounds. Larger true availability or sensitivity may yield better realized detection. [C2]

The value of this formula is not that it is complicated. It exposes the two levers separately. Increasing \(r\) pushes \(q_r\) toward zero, reducing conditional read misses. Increasing \(m\) supplies additional independent mode-availability opportunities.

The design problem is therefore not determined by raw read count alone.

## 4. Equal effort can favor repetition or diversity

The strongest anti-obviousness result comes from fixing total effort rather than comparing a cheap design with an expensive one.

Consider exactly \(2k\) reads and two designs.

**Depth design \(R\):** use one failure mode and take two reads per coordinate.

**Diversity design \(D\):** use two independent failure modes and take one read per coordinate in each mode.

The target is strict: all \(k\) truly present coordinates must be detected.

Let

\[
d=1-(1-p)^2=p(2-p)
\]

be the conditional probability that one coordinate is detected at least once in two reads.

For the depth design, the one shared mode must operate and then all coordinates must succeed in their two-read detection:

\[
G_R=a[p(2-p)]^k.
\]

For the diversity design, either exactly one mode operates, probability \(2a(1-a)\), in which case all coordinates must succeed in one read, probability \(p^k\), or both modes operate, probability \(a^2\), in which case every coordinate has two reads and joint detection is \(d^k\). Thus

\[
G_D=2a(1-a)p^k+a^2[p(2-p)]^k.
\]

Subtracting gives

\[
G_D-G_R
=
a(1-a)p^k\left[2-(2-p)^k\right].
\]

For interior \(0<a<1\) and \(p>0\), the prefactor is positive. Therefore the entire design comparison is controlled by one term. [C1]

## 5. The exact allocation boundary

Define

\[
p_k^*=2-2^{1/k}.
\]

Then CED proves

\[
\boxed{G_D>G_R\iff p>p_k^*},
\]

\[
\boxed{G_D<G_R\iff p<p_k^*},
\]

with equality at \(p=p_k^*\). [C1]

This is the chapter's primary finite-effort result.

It immediately blocks two opposite slogans.

The first slogan is the original forbidden inference: more repetitions automatically mean stronger evidence. False. At sufficiently high read sensitivity, reallocating the same number of reads across independent failure modes is better.

The second slogan is the tempting correction: failure-mode diversity is always better than repetition. Also false. For a multi-coordinate all-detected target at sufficiently low read sensitivity, deeper repetition inside one operating mode gives the stronger guarantee.

The scientific result is the condition separating these regimes.

## 6. Why the target dimension changes the answer

For one coordinate,

\[
p_1^*=0.
\]

Thus at any interior \(a,p\), splitting two reads across independent modes beats placing both in one mode. With only one target coordinate, there is no multiplicative penalty from requiring simultaneous recovery of many coordinates.

For \(k>1\), the threshold becomes positive and increases with \(k\):

| \(k\) | \(p_k^*\) |
|---:|---:|
| 1 | 0 |
| 2 | \(2-\sqrt 2\approx0.5858\) |
| 3 | \(2-2^{1/3}\approx0.7401\) |
| 5 | approximately 0.8513 |

As the number of coordinates that must all be recovered increases, one-read-per-mode designs need higher per-read sensitivity before mode diversity dominates. [C1]

This result is useful beyond the specific algebra because it shows that evidence architecture is target-relative. The same cameras, samples, or laboratory effort can be optimal for detecting one target and suboptimal for certifying a joint multi-coordinate state.

## 7. Both sides of the boundary are real

Take \(k=3\) and \(a=0.8\).

The threshold is approximately

\[
p_3^*\approx0.7401.
\]

At \(p=0.6\), which lies below the threshold, the depth design gives approximately

\[
G_R\approx0.4742,
\]

while the diversity design gives approximately

\[
G_D\approx0.4485.
\]

Repetition wins.

At \(p=0.9\), above the threshold, the ordering reverses:

\[
G_R\approx0.7762,
\]

while

\[
G_D\approx0.8543.
\]

Diversity wins. [C1]

The examples are not the evidence for the theorem; the factorized sign proof is. Their role is to show that both strict regimes are attainable rather than mathematical edge cases.

The executable tests cross-check the closed forms against the general mode-detection implementation over grids of \(k,a,p\), verify equality at the threshold, confirm monotonic increase of \(p_k^*\), and reproduce examples on both sides. [C3]

## 8. Finite-effort preference is not the asymptotic story

The threshold theorem answers the smallest equal-effort allocation problem: two reads per coordinate. It does not say what happens when the number of within-mode repeats becomes very large.

That requires the separate availability-ceiling theorem.

Fix \(m\) failure modes and allow \(r\to\infty\). If \(p>0\), conditional read misses vanish. But the declared contract still permits the least-favourable event that all \(m\) modes fail. Its probability is

\[
(1-a)^m.
\]

Therefore no uniform guarantee over the entire lower-bound contract can exceed

\[
\boxed{1-(1-a)^m}.
\]

CED also proves that the exact joint-detection lower bound converges to this value as \(r\to\infty\). [C2]

This is a genuine structural ceiling on the **worst-case guarantee under the declared availability lower bound**. It is not an upper bound on realized detection when actual mode availability is higher than \(a\).

## 9. A target confidence imposes a necessary mode floor

Suppose the desired uniformly certified joint-detection confidence is \(c\), with \(0<a<1\). The availability ceiling implies that certification is possible only if

\[
1-(1-a)^m\ge c.
\]

Solving gives the necessary condition

\[
\boxed{
m\ge
\left\lceil
\frac{\log(1-c)}{\log(1-a)}
\right\rceil}.
\]

This mode floor is necessary but not sufficient. Finite read sensitivity can still require more within-mode repetition after the mode-count requirement is met. [C2]

The result cleanly separates two design failures:

- too few repeats can leave conditional sensitivity inadequate;
- too few independent modes can make the desired guarantee impossible no matter how many extra repeats are added inside those modes.

This is the precise sense in which repetition cannot substitute indefinitely for failure diversity.

## 10. Equal raw effort can hide very different guarantees

The broader CED theorem gives a useful equal-effort example with \(k=3\), \(a=0.8\), \(p=0.6\), and 30 total reads.

One mode with 10 reads per coordinate gives a guaranteed joint detection of approximately

\[
0.799748,
\]

and cannot exceed the worst-case guarantee ceiling \(0.8\) even with infinitely many more within-mode reads.

Two independent modes with five reads per coordinate in each mode use the same 30 total reads but give a guarantee of approximately

\[
0.950069,
\]

with a higher ceiling \(0.96\). [C2]

This example does not contradict the two-read \(p=0.6,k=3\) result in which depth wins. The allocations are different. With enough repeated sensitivity inside each of two modes, diversification can overcome the initial low-sensitivity penalty and exploit the higher mode-availability ceiling.

That contrast is exactly why a design theorem is more informative than a slogan.

## 11. Detection is only one layer of honest reporting

CED's broader paper asks what finite evidence is justified in reporting about a declared ecological target.

A complete experiment record induces an exact equivalence relation on latent worlds: worlds are compatible when they produce the same record. A deterministic target value is licensed only when the target is constant on the current compatible class; otherwise the honest report is the set of compatible target values. [C4]

A target-safe quotient then describes the minimum refinement that **would be sufficient** for target-safe deterministic state tracking. It does not imply the current evidence has already resolved which target-safe block contains the true world. [C4]

Failure architecture enters between required resolution and trustworthy resolution. A nominal ideal record may separate two worlds, but if the observation architecture cannot support that distinction under its error contract, the split is not yet evidentially licensed.

This keeps Chapter 8 connected to the dissertation's larger theme without turning it into a general CED chapter. The focus here remains the conditions under which additional observation effort actually strengthens a target-relevant evidence guarantee.

## 12. More evidence can resolve irrelevant details

CED also contains an adaptive experiment-design result: within a declared finite policy family, experiment choice is evaluated by correct deterministic reporting, wrong deterministic reporting, honest ambiguity, and cost.

A benchmark shows that full-world information gain can prefer a measurement that resolves more latent entropy but leaves the declared target ambiguous, while a target-safe design chooses the measurement that resolves the prediction. [C4]

This result reinforces the chapter's conclusion. Evidence strength is not just a function of amount or entropy. The observation must both survive its failure architecture and separate worlds that matter for the target.

However, the dissertation should not let this result displace the Chapter 8 peak. MROD already owns mechanism-information-guided measurement ordering in Chapter 3. Here the adaptive result serves only as a target-reporting boundary: independent evidence is valuable only relative to the distinction the report must support.

## 13. What this chapter establishes—and what it does not

Under the declared independent-mode, one-sided imperfect-detection contract, this chapter establishes that:

1. the exact joint-detection guarantee depends on both within-mode repeat depth and number of independent failure modes;
2. at equal two-read effort, diversity beats depth iff \(p>2-2^{1/k}\), depth beats diversity below that threshold, and the two tie at the threshold;
3. the threshold increases with the number of coordinates that must all be detected;
4. both strict regimes are realizable and executable tests verify the sign boundary;
5. with a fixed number of modes, unlimited within-mode repetition cannot raise the uniform worst-case guarantee above \(1-(1-a)^m\);
6. a desired certified confidence therefore imposes a necessary mode floor;
7. target-safe reporting remains set-valued when the evidence architecture has not resolved target-relevant alternatives.

It does **not** say repetition is useless. It does not say diversification is always preferable. It does not cover correlated mode failures, heterogeneous sensitivities or costs, false positives, adaptive allocation, unknown failure modes, or arbitrary target loss functions. It does not infer \(a\) or \(p\) from the same evidence being certified. It does not turn a lower-bound availability assumption into an upper bound on realized field detection. [C1,C2]

The safe headline is:

> **Repeated effort strengthens evidence according to where it is placed in the failure architecture: finite-effort depth and diversity have an exact tradeoff, while a fixed number of shared failure opportunities imposes a guarantee ceiling that repetition alone cannot cross.**

## 14. Transition: after eight boundaries, can adequacy be put on one axis?

Chapter 8 closes the final source-owned research chapter. The sequence has now encountered several different quantities that can become “larger”: observation precision, temporal precedence, measurement information, state detail, memory, intervention capability, structural reuse, and replicate count.

None of the chapters proves that increasing these quantities is generally bad. Each instead supplies a typed condition specifying when a particular increase is relevant to one scientific responsibility.

The final synthesis therefore should not search for one universal anti-monotonicity theorem. It asks whether these heterogeneous richness measures can legitimately be collapsed into one privileged direction of scientific adequacy, and uses TU-1's exact revision theorem to clarify what successful reuse would require. [TR]

## Internal source keys

- **[C1]** CED `docs/repeat_vs_mode_allocation_theorem_2026-09-03.md` — exact equal-effort threshold, proof, corollaries and both-side examples.
- **[C2]** `docs/mode_diverse_detection_theorem.md` — exact joint-detection frontier, worst-case availability ceiling, necessary mode floor and equal-total-effort example.
- **[C3]** `tests/test_repeat_vs_mode_allocation_boundary.py` — implementation cross-check, threshold grid, equality case, monotonicity and both-side witnesses.
- **[C4]** `docs/paper_b_theorem_consolidation.md` and `manuscript/paper_b_supplement.tex` — experiment-induced quotient, honest report criterion, target-safe resolution requirement and adaptive risk-limited design boundaries.
- **[TR]** theouni `thesis/transition_recovery_matrix.json` and typed synthesis matrix — Chapter 8→9 is a synthesis handoff, not a proof of a global richness theorem.
