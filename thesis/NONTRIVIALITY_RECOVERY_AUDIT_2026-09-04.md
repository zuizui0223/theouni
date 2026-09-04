# Nontriviality recovery audit — 2026-09-04

## Purpose

The ten-chapter programme began with a real presentation risk: most chapter slogans can be paraphrased as “X does not necessarily imply Y.” Written that way, they sound obvious even when the source work is not. This audit asks a stricter question:

> **What, beyond a definition or slogan, actually forces the chapter conclusion?**

A chapter is counted as recovered only when the source supplies at least one non-definitional object such as an iff condition, contradiction/impossibility proof, sharp or minimal witness, locked numerical result, or executable exhaustive oracle. Numerical recovery is typed: locked source numbers are not confused with exact finite synthetic examples.

## Executive answer

The current research spine does **not** contain a Chapter 1–8 whose result is only a definition.

- **Locked source numerical recovery:** Chapters 2, 3, 4.
- **Exact finite numerical/constructive recovery:** Chapters 1, 5, 6, 7, 8; TU-1 in Chapter 0 also has an exact finite scale-separation family.
- **Direct contradiction/impossibility or counterexample logic:** Chapters 1–8 all have one; the form differs by chapter.
- **Necessary/sufficient or exact boundary result:** Chapters 1, 3, 4, 7, 8; Chapter 2 gives an exact identified/unidentified split and sharp endpoint; Chapters 5–6 give sharp/no-bound existence families instead of an iff.
- **Sharpness/minimality:** present across the research spine, but in different forms.
- **Chapter 9:** intentionally has no pooled numeric or new global theorem. It is a typed synthesis and must remain so.

So the answer to “did we weaken obviousness?” is **yes, but not by pretending every chapter is an empirical numerical paper**. We weakened it by replacing slogans with exact conditions and then requiring either a numerical locked application or a contradiction/sharp construction showing that the tempting inference genuinely fails under controlled conditions.

## Scorecard

| Ch. | Weak slogan that would be obvious | Non-definitional recovery | Numeric status | Contradiction / counterexample | Sharpness / minimality | Remaining risk |
|---:|---|---|---|---|---|---|
| 0 | “a compression may become inadequate later” | revision iff factorization; exact minimum side alphabet; average-vs-worst divergence | exact finite | two worlds same old label but different new labels defeat any decoder; pigeonhole lower bound | exact min alphabet; arbitrary debt separation | classical coding/factorization prior art; framing only |
| 1 | “more data may not identify mechanism” | `dim=k-rank(M)` and added row helps iff outside row span | exact finite matrix | null-space pair gives distinct mechanisms with identical observations | useful scalar row drops dimension exactly one | no natural/locked numeric application yet; mathematical substrate classical |
| 2 | “false positives can happen” | perfect precedence fixes sensitivity=1 but leaves specificity free | **locked source numeric** | keep all event leads and make every non-event fire | entire specificity grid reachable; AUC=.5 sharp endpoint | prior early-warning false-positive literature is strong |
| 3 | “adaptive measurement can help” | adaptive > best static iff branchwise argmax intersection empty | **locked G2 + exact finite** | equality plus no common maximizer contradicts zero expected nonnegative gap | four-world witness minimal in declared class | G2 implementation still compared mainly with random ordering |
| 4 | “multiple state variables differ” | common monotone scalar exists iff target vectors form product-order chain | **locked source numeric** | one crossing pair contradicts monotone reconstruction | one crossing is complete impossibility certificate | finite simulation target set; no claim against approximate scores |
| 5 | “more futures may need more memory” | fixed-resource family with exact `m`-bit open/closed gap | exact finite | any resource-only finite bound is defeated by larger `m` | equality/sharpness under bounded local resources | no empirical bits; strongest issue is prior-art positioning |
| 6 | “more capability may need more knowledge” | `Δ|K*|=1` with arbitrary `m`-bit state/evidence burden | exact finite | choose `m>f(1)` to contradict any carrier-gain-only bound | minimum nonzero carrier gain with arbitrary burden; connected construction | theoretical existence, not prevalence or field cost |
| 7 | “laws/history may change under replacement” | portability iff; unique coarsest repair; history modes necessary and sufficient | exact finite | two carried maps force incompatible labels under one route-free map | unique minimal repair; one mode per distinct carried map | source-relative inherited semantics only; priority audit unresolved |
| 8 | “correlated repeats are not independent” | exact finite-effort depth/diversity reversal threshold + availability ceiling | exact finite | parameter points on both sides refute both universal slogans | exact threshold; asymptotic ceiling | simple declared model; formula priority unresolved |
| 9 | “everything is task-dependent” | typed synthesis of eight source-owned conditions; TU-1 retained as exact substrate | deliberately no pooled number | no independent global contradiction claimed | no global scalar theorem invented | must resist becoming philosophy without chapter-specific anchors |

## Numerical recovery in detail

### Chapter 2 — warning

The locked result is as strong as the theorem permits. The inherited ensemble has `35/35` event leads and `48/48` non-event firings; the fresh ensemble has `33/33` event leads and `49/49` non-event firings. Therefore every frozen binary horizon rule has sensitivity `1`, specificity `0`, and AUC `0.5`. PPV collapses to event prevalence: about `0.422` and `0.402` respectively.

This is not “we observed some false positives.” It is a successful replication at the original event-conditioned estimand that lands at the **sharp worst-discrimination endpoint** once the deleted denominator is restored.

### Chapter 3 — next measurement

The minimal four-world witness gives adaptive second-step information `1.0 bit` versus best-static `0.5 bit`. This directly addresses the objection that “adaptive beats random” is too easy.

The independent G2 implementation layer is numerical: at budget 2, guided versus random confound resolution is `1.000` versus `0.6045`, convergence `0.990` versus `0.435`, and nuisance selection `0.001` versus `0.974`. At budget 4, guided uses `1.518` observations versus `2.673` and `0.014` nuisance measurements versus `1.169`, with false exclusion zero throughout.

The remaining implementation weakness is explicit: G2 does **not yet** benchmark against several strong nonrandom policies. The theorem solves the conceptual best-static second-step objection, but a publication claim of broad policy superiority would still need stronger baselines.

### Chapter 4 — multiple states

The locked H3 crossing directly violates the scalar chain condition. From 2 to 16 patches, retained interaction falls `0.001744 -> 0.001244` and local effective size falls `0.221311 -> 0.033058`, while realised high-trait mass moves oppositely `0.282918 -> 0.393880`.

A separate state-separation result is even more visually decisive: potential high-trait viability is absent in `1037/1037` subdivided outcomes, while realised high-trait occupancy persists at approximately `99.6–100%` over the tested horizon. Thus “potential support” and “realised occupancy” are not merely differently named variables in this finite model.

## Exact finite numerical witnesses are not empirical data

For the theorem-heavy chapters, numbers are used to make the construction inspectable, not to mimic an empirical dataset.

- **TU-1 / Ch0:** with `m=4`, one old block split into 16 revised blocks gives `D_rev=4` bits. With `N=4096` old blocks, `D_avg=log2(1+15/4096)≈0.00527` bits. This makes the average-versus-worst revisability separation concrete.
- **Ch1:** for `k=3`, observation rows `(1,1,1)` and `(1,0,0)` have rank 2 and residual dimension 1. Adding `(2,0,0)` does nothing; adding `(0,1,0)` yields rank 3 and residual dimension 0.
- **Ch5:** at `m=4`, `|P_C|=2`, `|P_O|=32`, and the exact open-minus-closed interface gap is 4 bits under the same bounded-local resource family.
- **Ch6:** at `m=4`, one action adds one viable world, the retained present slice refines `1 -> 16` states, and monitoring debt changes `0 -> 4` bits, while a coarse target remains reportable.
- **Ch7:** the accumulating witness at `m=4` has 17 repaired states and minimal source-relative defect 15; two distinct carried maps require exactly two history modes.
- **Ch8:** for `k=3`, `p*=2-2^(1/3)≈0.74008`. At `a=.8,p=.6`, depth `≈.47416` beats diversity `≈.44845`; at `p=.9`, diversity `≈.85427` beats depth `≈.77624`.

These are **exact witness numbers**, not fitted natural-system estimates. The distinction must remain visible in the manuscript.

## How contradiction/impossibility removes definition-only circularity

A common failure mode in theory papers is to define an object so that the conclusion follows by naming. The current spine avoids that in the following ways.

### Ch0

If a revised state is not constant within an old stored block, assume a state-only decoder exists. The two worlds have the same decoder input but require different outputs, contradiction. The side-alphabet lower bound follows by pigeonhole inside the worst split old block. Thus revision debt is not defined to be large; it is forced by incompatible required outputs.

### Ch1

A null-space vector gives a family of distinct latent mechanisms with exactly the same observations. Conversely, a new row outside the span changes rank. The useful/useless measurement distinction is therefore not a semantic label attached to a variable; it is testable against the observation operator.

### Ch2

Perfect event precedence is held fixed while non-event marker states are varied freely. The all-fire construction preserves the apparently strongest positive result and still yields chance discrimination. This directly refutes the tempting implication without redefining either precedence or discrimination.

### Ch3

The equality proof is a contradiction argument. If best static equals adaptive, the best static candidate must have zero branchwise gap on every positive-probability branch. If no common branchwise maximizer exists, that is impossible. The strict-gain condition is therefore necessary, not an algorithmic convention.

### Ch4

A crossing pair defeats any proposed monotone scalar. Because real scalar values are comparable, whichever state is placed higher must be no worse on every reconstructed target. A pair with one target up and another down makes that impossible. The numerical H3 crossing then activates this impossibility theorem on locked model states.

### Ch5

The no-bound claim is not a definition of memory. Hold the advertised resource descriptors fixed and let `m` increase. If a finite bound depending only on those descriptors existed, choose `m` beyond it. The exact response-interface gap equals `m`, contradiction.

### Ch6

The same pattern is stronger: the carrier gain is fixed exactly at one. Any proposed finite function of carrier gain alone has some value at one; choose `m` larger. The connected construction then violates the bound while preserving the one-world gain.

### Ch7

If two routes give different inherited labels to the same terminal configuration, a route-free carried map would have to assign two labels to one input. For history compression, fewer modes than distinct carried maps forces two maps into one mode, again requiring incompatible inherited labels. This is a direct incompatibility/pigeonhole proof, not a definition that “history matters.”

### Ch8

The difference between diversity and depth factors as a positive term times `2-(2-p)^k`. Therefore its sign genuinely reverses at `p*=2-2^(1/k)`. Parameter points on opposite sides refute both one-direction slogans. Separately, the all-modes-fail event prevents any uniform guarantee above the fixed-mode availability ceiling.

## Which chapters are now strongest against the “obvious” objection?

### Strongest mixed theorem + locked-number recovery

1. **Ch4** — iff representability theorem + locked crossing + 1037-source state separation.
2. **Ch2** — exact denominator theorem + two locked source ensembles at the sharp AUC=.5 endpoint.
3. **Ch3** — iff adaptive theorem + minimal witness + large frozen controlled benchmark.

These chapters can show both the formal condition and a numerical case where it bites.

### Strongest pure-theory recovery

4. **Ch6** — fixed +1 capability gain with arbitrary `m`-bit burden and a no-bound contradiction.
5. **Ch7** — portability iff + unique minimal repair + exact minimal history modes.
6. **Ch5** — sharp fixed-resource open/closed memory gap plus positive portability boundary.
7. **Ch8** — exact reversal threshold on both sides plus asymptotic ceiling.
8. **Ch1** — exact observation-rank iff and exhaustive oracle; scientifically useful, but closest to classical linear identifiability and still lacks a locked natural/finite-model application comparable to Ch2–4.

This ordering is about resistance to the **obviousness** objection, not publication quality or biological importance.

## Remaining development gates

### Highest priority: Chapter 1 application layer

Ch1 is now mathematically exact but still vulnerable to “rank-nullity applied to ecology.” The next useful recovery is not another theorem. It is one locked field-like or archived joint-measurement design in which many observations leave the same row span and one targeted effectiveness/calibration measurement changes the identified set. If no such dataset is admissible, the chapter must present itself explicitly as a design theorem rather than implying empirical validation.

### Chapter 3 stronger implementation comparators

Theorem A2 already compares adaptation to the strongest fixed second candidate. G2, however, remains primarily guided-versus-random. A stronger implementation appendix should compare at least a static-MI order and one cost-aware/nonadaptive information baseline under the same frozen systems. This would prevent a reviewer from treating the theorem and benchmark as unrelated strengths.

### Chapters 5–7: do not chase fake empirical numerics

These are finite exact theory chapters. Adding arbitrary ecological simulations merely to produce plots would weaken the architecture. Their remaining burden is nearest-neighbour prior art, interpretable finite witnesses, and clear positive boundaries—not pretending synthetic bits are measured natural quantities.

### Chapter 8: broaden only if the application claim requires it

The exact two-read threshold is already nontrivial. General correlated failures, heterogeneous costs or adaptive allocations would be genuine extensions, but should be added only if the paper needs applied breadth. Otherwise the exact simple boundary plus the separate availability ceiling is cleaner.

## Final verdict

The programme has moved materially beyond definition-level claims.

The important change is not “more formulas.” It is that each source-owned research chapter now has a way for the tempting shortcut to **fail while the definitions remain fixed**:

- a same-observation null direction,
- a same-precedence chance-discrimination construction,
- a branchwise incompatibility that forces adaptive gain,
- a locked target crossing that forbids scalarization,
- an unbounded exact response gap under fixed local resources,
- an unbounded monitoring burden under a fixed one-world capability gain,
- incompatible route semantics that force history modes,
- or a parameter threshold whose two sides reverse the design recommendation.

That is the main answer to the obviousness problem. The remaining work is not to invent more definitions, but to strengthen the few application/comparator layers that are still weaker than the theorem spine.
