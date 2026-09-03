# Source map — Chapter 5 v0.1: 未来を開くと、記憶が要る

This map supports `thesis/drafts/final/05_open_future_memory_v0.1.md` and is locked to CCOC snapshot `96d823309ce04affb33446f1996aedf0a163a039`.

## Snapshot and chapter contract

- owning repository: `zuizui0223/ccoc`
- recovered/current snapshot: `96d823309ce04affb33446f1996aedf0a163a039`
- verification class: `verified_exact_extremal_all_m_theorem_plus_finite_certificates_and_positive_portability_boundary`
- forbidden inference: `物理的境界が狭い ⇒ 必要な因果記憶も小さい`
- chapter claim ceiling: exact finite synthetic theorem family under declared deterministic controlled systems and legal future grammars; no empirical inference that real narrow ecological boundaries carry large hidden causal memory, and no historical-firstness claim for classical minimization/compilation substrate.

## A. Headline theorem: fixed local resources do not bound open-future interface inflation

### A1 — `docs/fixed_regular_extremal_theorem_2026-08-13.md`

For every integer `m>=1`, CCOC constructs a finite deterministic synchronous controlled network with:

- comparison domain `D_m={0,1}^{m+1}`;
- fixed primitive action alphabet `{0,1,fire,tick}`;
- a closed grammar excluding `fire` and an open grammar adding exactly that one primitive transition;
- one-state grammar automata independent of `m`;
- a tree interaction graph with maximum degree at most three;
- a focal/exterior edge cut exactly one;
- local node and message alphabets bounded independently of `m`;
- radius-one local dynamics.

The exact closed response quotient satisfies

`|P_C|=2`, `K_C=1`,

while the exact open quotient is discrete:

`|P_O|=2^(m+1)`, `K_O=m+1`.

Therefore

`K_O-K_C=m`

for arbitrary `m` despite the fixed local/static resource budget.

## B. Proof obligations

### B1 — closed all-word invariant

Without legal `fire`, no pulse is created. Address/tick actions preserve the exterior memory bits and focal output, so every closed legal response depends only on focal bit `y`. This proves exactly two closed classes.

### B2 — open addressability

For leaf `j` with address `a_j` and depth `d_j`, legal word

`w_j = a_j fire tick^(d_j+1)`

returns `b_j` at the focal output. Hence any pair differing in one exterior bit is distinguishable by a legal future word. Together with the current focal output, this makes the open quotient discrete.

### B3 — sharpness

The finite comparison domain has `2^(m+1)` states and the closed quotient already has two classes. At most `m` additional bits can be exposed by any exact refinement on this domain. The construction attains exactly `m`, so its innovation slack is zero.

### B4 — no static-resource-only bound

Every member of the family obeys the same bounded action alphabet, grammar size/edit, degree, cut width, local alphabets and update radius, while the gap equals arbitrary `m`. Therefore no finite upper bound depending only on those resource constants exists.

### B5 — local access length

For a midpoint-balanced relay, the deepest selector path has length `ceil(log2 m)` and the worst canonical query length is

`2 ceil(log2 m)+2`.

The source relates this to a general bounded-local causal-cone lower bound, making logarithmic access order-optimal in the broader declared class.

## C. Executable finite certification

### C1 — `causal_model/extremal_open_composition.py`

`certify_fixed_regular_extremal_theorem(m)` checks the simultaneous finite certificate at a supplied `m`.

### C2 — `tests/test_extremal_open_composition.py`

The active source tests exercise the certificate across finite module counts and verify the structural/resource conditions and zero innovation slack.

Executable certification is an implementation guard. It does not replace the analytic quantifier “for every `m>=1`” proved in A1.

## D. General cross-grammar lower-bound spine

### D1 — `docs/theorem_spine.md`

CCOC's current proof spine distinguishes:

- CORE-1: canonical exact dynamic interface for one legal grammar;
- CORE-2: operational extension–compression lower bound from future decoder addressability;
- CORE-3: bounded-local extremal sharpness supplied by the fixed-regular family;
- CORE-4: positive conservative/coherent portability boundary;
- CORE-5: local future-word/new-action obstruction.

The dissertation should present CORE-3 as sharpness support for the cross-grammar claim, not as an unrelated theorem catalogue.

## E. Positive portability theorem

### E1 — `docs/coherent_portable_macrolaw.md`

Let nested stages map into one finite macro alphabet `Q`. If every stage factors through the same macro output, legal-action relation and successor dynamics, and embeddings preserve macro labels, then all stages carry one exact extension-portable macro-law.

This is a sufficient positive condition:

`common finite dynamics + trajectory-preserving embeddings + label coherence => portable macro-law`.

The chapter uses this theorem to avoid the false converse “future expansion always forces memory growth.”

### E2 — future-word obstruction

If two old states remain merged but a newly legal later word yields different traces from their embedded images, the proposed shared macrostate cannot belong to an exact coherent portable law. This supplies a concrete finite failure witness even before a global memory lower bound is derived.

## F. Ecological interpretation boundary

Allowed interpretation:

- current physical narrowness is not, by itself, a mathematical upper bound on exact response memory under future grammar expansion;
- an ecological interface intended for future composition/intervention must justify portability in response terms, not only current graph topology;
- newly legal ecological exposures/actions can invalidate an old compression when they distinguish formerly merged states.

Forbidden upgrades:

- a real one-edge or narrow corridor has `m` hidden bits;
- sparse ecological networks generally require large memory;
- the fixed relay is a fitted empirical ecosystem;
- finite-state minimization, generic regular-language machinery or bounded-local sequential-machine compilation was invented by CCOC.

## G. Relation to TU-1 and neighboring chapters

### G1 — TU-1

CCOC determines when the revised open future requires a finer response quotient. TU-1 can then ask whether an already stored old quotient retained enough information for revision. TU-1 does not own the CCOC lower bound.

### G2 — Chapter 4 → 5

Chapter 4 changes the target responsibility; Chapter 5 changes legal future response grammar. The scalar-state crossing does not prove open-future memory inflation.

### G3 — Chapter 5 → 6

CCOC changes which future words are legal. CREST's next chapter changes management capability/viability and proves a separate one-action/+1-world versus `m`-bit monitoring divergence. Do not collapse grammar expansion and capability expansion.

## Section-to-source matrix

| Draft section | Primary source | Proof/verification | Main boundary |
|---|---|---|---|
| 1. Nontrivial question | A1/D1 | recovery registry | fixed resources, not trivial growing alphabet |
| 2. Exact response interface | D1 | source dynamic-interface tests | classical substrate, not novelty claim alone |
| 3. Fixed resource construction | A1 | C1/C2 | finite deterministic class |
| 4. Closed quotient | A1 B1 | C1/C2 | all closed words, not sampled futures |
| 5. Open quotient | A1 B2 | C1/C2 | decoder words force discreteness |
| 6. Sharpness | A1 B3 | finite certificates | gap hits domain capacity |
| 7. No resource-only bound | A1 B4 | all-m family | only declared resource list |
| 8. Local access | A1 B5 | causal-cone theorem | order claim, architecture-specific constants |
| 9. Positive portability | E1 | source positive witness | sufficient, not necessary universal criterion |
| 10. Future-word obstruction | E2 | source examples | local certificate, not full lower bound |
| 11. Ecological interpretation | F | claim firewall | no real-system memory estimate |
| 12. Ch4 relation | G2 | transition validator | question handoff |
| 13. Scope | A–F | recovery/proved-condition registry | theorem ownership remains CCOC |
| 14. Transition to CREST | G3 | transition validator | grammar ≠ capability |

## Drafting gate

1. Keep the fixed-resource/no-bound question as the chapter headline; do not lead with the generic phrase “more futures need more memory.”
2. Show the closed invariant and open decoder construction before reporting the `m`-bit gap.
3. Keep sharpness (`innovation slack = 0`) visible so the family is not presented as merely a large example.
4. Pair the negative extremal result with the coherent portability sufficient condition.
5. Keep the one-edge cut as a mathematical resource bound, not an empirical ecological memory estimate.
6. Preserve the CCOC/CREST distinction in the chapter transition.
