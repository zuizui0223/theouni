# Source map — Chapter 8 v0.1: 反復は、多様性の代わりにならない

This map supports `thesis/drafts/final/08_repetition_not_diversity_v0.1.md` and is locked to merged CED snapshot `590f6459a7c3ef31e8a527319771fd3d736a704a`.

## Snapshot and chapter contract

- owning repository: `zuizui0223/ced`
- recovered theorem snapshot: `590f6459a7c3ef31e8a527319771fd3d736a704a`
- verification class: `verified_equal_effort_allocation_boundary_plus_availability_ceiling`
- forbidden inference: `同じ手法を繰り返した ⇒ 証拠が強くなった`
- chapter claim ceiling: exact finite/worst-case results under a declared independent common-mode imperfect-detection contract; no inference of mode availability/sensitivity from the record, no universal claim that repetition is useless or diversity always wins.

## A. Headline finite-effort allocation theorem

### A1 — `docs/repeat_vs_mode_allocation_theorem_2026-09-03.md`

For `k>=1` truly present coordinates, mode availability lower bound `a`, read sensitivity lower bound `p`, no false positives and exactly `2k` reads, compare:

- depth `R`: one mode, two reads per coordinate;
- diversity `D`: two independent modes, one read per coordinate in each mode.

For the target requiring joint detection of all `k` coordinates:

`G_R = a[p(2-p)]^k`

and

`G_D = 2a(1-a)p^k + a^2[p(2-p)]^k`.

Their difference factors exactly as

`G_D-G_R = a(1-a)p^k [2-(2-p)^k]`.

Therefore for interior `0<a<1`, `p>0`, defining

`p_k* = 2-2^(1/k)`,

- `G_D > G_R` iff `p > p_k*`;
- `G_D < G_R` iff `p < p_k*`;
- the designs tie at `p=p_k*`.

This is the chapter's primary anti-obviousness result: neither “repeat more” nor “always diversify modes” is uniformly valid at fixed finite effort.

### Corollaries

- `k=1` gives `p_1*=0`, so diversity wins for every interior `a,p`;
- for `k>1`, the threshold is positive;
- `p_k*` increases with `k` and tends to one;
- the target dimension therefore changes the allocation decision.

## B. Executable allocation obligations

### B1 — `tests/test_repeat_vs_mode_allocation_boundary.py`

The source tests:

- cross-check the closed forms against the general `ModeDiverseDetectionPanel` implementation;
- verify the sign boundary over grids of `k,a,p`;
- verify equality at `p=2-2^(1/k)`;
- verify the `k=1` corollary;
- verify threshold monotonicity in `k`;
- reproduce a below-threshold case where depth wins and an above-threshold case where diversity wins.

The executable layer verifies implementation/proof obligations; the written factorization proof owns the quantified condition.

## C. Exact general frontier and asymptotic availability ceiling

### C1 — `docs/mode_diverse_detection_theorem.md`

For `m` independent modes and `r` reads per coordinate per operating mode, define `q_r=(1-p)^r`. The least-favourable contract guarantee for detecting all `k` truly present coordinates is

`sum_{s=0}^k (-1)^s binom(k,s) [1-a+a q_r^s]^m`.

The contract permits all `m` modes to fail simultaneously with probability `(1-a)^m`. Hence no uniform guarantee over the declared lower-bound contract can exceed

`1-(1-a)^m`.

For `p>0`, the exact guarantee converges to this ceiling as within-mode repeats `r -> infinity`.

### Necessary mode floor

A target uniform confidence `c` can be certified only if

`m >= ceil[ log(1-c) / log(1-a) ]`

for `0<a<1`.

This is necessary, not sufficient: finite read sensitivity can still demand greater repeat depth.

### Interpretation boundary

`1-(1-a)^m` is a worst-case **guarantee ceiling implied by the lower-bound contract**. It is not an upper bound on realized detection when true mode availabilities exceed `a`.

## D. Same effort can yield different guarantees

The source's 30-read example (`k=3,a=0.8,p=0.6`) gives:

- one mode × 10 reads/coordinate: guaranteed joint detection approximately `0.799748`, ceiling `0.8`;
- two independent modes × 5 reads/coordinate/mode: approximately `0.950069`, ceiling `0.96`.

This does not contradict the two-read threshold case where `p=0.6,k=3` favors depth. The allocation scale differs; the combination of within-mode depth and mode diversity changes the result.

The dissertation should use this contrast to show why the theorem is a design law rather than a slogan.

## E. Broader CED reporting infrastructure

### E1 — `docs/paper_b_theorem_consolidation.md`

CED's broader paper separates four results:

1. experiment-induced compatible-world quotient and honest set-valued report criterion;
2. unique coarsest target-safe resolution requirement;
3. failure architecture determining trustworthy refinement;
4. risk-limited adaptive target resolution.

For Chapter 8, Result 3 is the headline. Results 1–2 explain why a nominal record split is meaningful only relative to a target report, and Result 4 is a secondary boundary showing that full-world information can resolve target-irrelevant distinctions.

### Evidence boundary

The target-safe quotient is a **resolution requirement**, not a statement that the current record has already resolved the corresponding block. If the compatible record class contains multiple target values, the honest report remains set-valued until evidence actually separates them.

## F. What the chapter may and may not claim

Allowed:

- repeat depth and independent failure diversity attack different error mechanisms;
- at equal two-read effort their ordering has an exact threshold;
- a fixed number of modes imposes an asymptotic worst-case guarantee ceiling no amount of within-mode repetition can cross;
- target dimension changes the finite-effort allocation threshold;
- raw replicate count is not sufficient to characterize evidence strength.

Forbidden:

- repetition is generally useless;
- failure-mode diversity always dominates repetition;
- true mode failures are independent because the model declares them independent;
- `a` or `p` are empirically estimated by the theorem;
- the lower-bound availability ceiling is an upper bound on realized detection;
- the results cover correlated failures, heterogeneous sensitivities/costs, false positives or arbitrary adaptive allocation without new analysis.

## G. Relation to Chapter 7 and Chapter 9

### G1 — Chapter 7 → 8

MLTR asks whether inherited semantics remain exact under structural replacement. CED asks whether repeated observations provide genuinely independent opportunities to resolve target-relevant worlds.

Exact law transport does not imply evidential independence. The transition is a question handoff.

### G2 — Chapter 8 → 9

The finite-effort theorem itself contains a local non-monotonicity: adding failure diversity can improve or worsen the guarantee depending on sensitivity and target dimension. The synthesis must not inflate this into a universal theorem that richness is always non-monotone.

Chapter 9 should retain this as one typed evidence-allocation result among eight different responsibility-specific conditions.

## Section-to-source matrix

| Draft section | Primary source | Executable/formal support | Main boundary |
|---|---|---|---|
| 1. Replicate count problem | C1/E1 | proved-condition registry | architecture, not raw count |
| 2. Observation contract | C1 | source assumptions | assumptions declared, not inferred |
| 3. Joint frontier | C1 | `ced/mode_detection.py` | worst-case lower-bound contract |
| 4–5. Equal-effort threshold | A1 | B1 | exact two-read comparison only |
| 6. Target dimension | A1 | B1 | all-coordinate target |
| 7. Both sides | A1 | B1 | examples illustrate theorem |
| 8–9. Ceiling/mode floor | C1 | source implementation | guarantee ceiling, not realized upper bound |
| 10. Equal total effort | C1 | source example | different allocation scale |
| 11–12. Reporting context | E1 | CED supplement/tests | target-relative supporting infrastructure |
| 13. Scope | A1/C1 | proved-condition registry | declared failure contract only |
| 14. Transition | G2 | typed synthesis/transition validators | no global richness theorem |

## Drafting gate

1. Keep the exact threshold theorem before the asymptotic ceiling so the chapter does not read as “diversify modes.”
2. Keep both strict sides of the threshold visible.
3. State the availability ceiling as a worst-case guarantee ceiling every time it appears.
4. Keep target-safe reporting as supporting context, not a competing chapter headline.
5. Verify detection/repeatability/monitoring-design literature before citation-ready status.
