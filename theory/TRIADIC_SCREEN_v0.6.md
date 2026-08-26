# Draft v0.6 Triadic Consistency Screen

Status: **machine-generated complete pair-profile screen with bounded executable witnesses; outside the frozen v0.5 core**.

Registry: [`triadic_screen.json`](triadic_screen.json)
Source pairwise registry SHA-256: `6a7724e482b25b3ef11bfaf6a396e83f8bfe0e6b045d24bf2bd8ca6326519575`

## Result

- Modules: **12**
- Unordered triples: **220**
- Executably assessed in a bounded shared-carrier witness: **2**
- Not executably assessed: **218**

Screen-class counts:

- `all-three-pairs-compatible`: 1
- `contains-declared-pair-conflict`: 0
- `contains-open-bridge`: 125
- `contains-orthogonal-estimand`: 25
- `requires-common-carrier-or-map`: 69

These are mutually exclusive triage buckets under the conservative priority `actual-conflict > open-bridge > conditional-on-common-carrier-or-map > orthogonal-estimand > compatible`; they are not triple-level truth labels.

## Executable bounded witnesses

- `TRIAD-W1-RACH-MRM-CED` (MRM / CED / RACH) — One finite bridge carrier jointly realizes RACH causal multiplicity, MRM response equivalence, and CED deterministic target licensing.
- `TRIAD-W2-TU1-TU3-TU4` (TU-1 / TU-3 / TU-4) — One four-world carrier jointly realizes TU-1 reverse-reuse failure, TU-3 loss-response adequacy, and TU-4 strict warning refinement.

## Claim ceiling

Complete 220-triple pair-profile coverage and two bounded shared-carrier witnesses only. Pairwise labels remain human judgments, and the screen neither discovers nor excludes emergent three-way inconsistency in unmodelled triples.

Every triple and its three pair relations is recorded in `triadic_screen.json`. The screen is a complete triage ledger, not a three-way satisfiability proof. Only the two registered witnesses are jointly realized by executable finite models.

Regenerate with `python theory/build_triadic_screen.py` and validate with `python theory/validate_triadic_screen.py`.
