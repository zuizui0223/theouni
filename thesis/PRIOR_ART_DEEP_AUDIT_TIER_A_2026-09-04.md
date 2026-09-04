# Tier-A nearest-neighbour audit — 2026-09-04

## Purpose and status

This note deepens the prior-art firewall for the three theorem-heavy chapters where a correct finite theorem could still be oversold if a classical construction already carries the same quantified burden.

The status is **nearest-neighbour audit, not priority clearance**. A focused search can identify direct precedents and force claims downward. Failure to find an exact match cannot establish historical firstness.

Search focus:

- CCOC: future equivalence, minimal automata/transducers, sequential-machine composition, bounded-local/outerplanar realization, one-transition state blow-up;
- CREST: requisite variety, good-regulator/model requirements, control-state abstraction, MDP/POMDP sufficient state;
- MLTR: exact MDP abstraction, bisimulation/lumpability, homomorphisms and transfer between tasks with different state/action spaces, path-dependent representation.

## Chapter 5 / CCOC — direct motifs found, package-only novelty posture

### Direct classical or modern neighbours

1. **Future equivalence and minimal state are classical.** Myhill–Nerode identifies a right-invariant future-equivalence relation whose classes give the minimum deterministic automaton. Computational-mechanics causal states likewise group histories by predictive equivalence and are minimal sufficient statistics for prediction. CCOC must not present future-equivalence minimization itself as new.

2. **Sequential-machine composition/decomposition is classical.** Krohn, Mateosian & Rhodes (1967), *Methods of the algebraic theory of machines: I. Decomposition theorem for generalized machines; Properties preserved under series and parallel compositions of machines*, JCSS 1:55–85, DOI `10.1016/S0022-0000(67)80007-2`, studies decomposition and properties preserved by series/parallel machine composition.

3. **Bounded-local / planar realization is not a safe novelty claim.** Dömösi & Nehaniv (2000), *On complete systems of automata*, Theoretical Computer Science 245:27–54, DOI `10.1016/S0304-3975(99)00274-1`, constructs primitive automata products where each factor depends on and influences only a bounded number of factors and notes an outerplanar realization. Therefore CCOC should not claim historical novelty merely from bounded degree/local dependence/planarity-style implementation.

4. **A one-transition blow-up motif already exists in automata complexity.** Baburin & Cotterell (2024), *Blow-up in Non-Deterministic Automata*, arXiv:2407.09891, explicitly discusses how adding or removing transitions affects state/subset complexity; the paper notes that adding a single transition can lead to exponential state-complexity blow-up. This is not the same object as CCOC's closed/open exact response quotient, but it blocks any generic claim that “one transition can reveal exponentially many states” is itself a new phenomenon.

### What remains defensible

The defensible object is the **simultaneous response-interface package** under one declared comparison:

- same finite controlled plant;
- fixed four-symbol primitive action alphabet;
- one-state closed/open future grammars differing by one legal `fire` transition;
- bounded degree and bounded local alphabets;
- one-edge focal/exterior cut;
- closed quotient `|P_C|=2`;
- open quotient `|P_O|=2^(m+1)`;
- exact gap `K_O-K_C=m` for every `m>=1`;
- equality with the finite-domain response-memory upper bound;
- a no-static-resource-only-bound corollary for the declared resource list;
- separate positive coherence conditions for a portable macro-law.

Current focused search did **not** establish that this entire conjunction is absent from prior work. Therefore the status is `package_distinctness_plausible_but_priority_unresolved`.

### Claim rule

Allowed without stronger historical audit:

> We construct, for the declared finite response-interface class, a fixed-resource family that attains an `m`-bit closed/open response-memory gap after a one-transition future-grammar opening.

Not allowed:

- first demonstration of one-transition exponential state blow-up;
- first bounded-local realization of arbitrary finite machine complexity;
- invention of future equivalence/minimal response state;
- first proof that narrow physical boundaries can hide large information in any general sense.

## Chapter 6 / CREST — classical regulatory variety is close; exact cross-gate scaling remains unresolved

### Direct neighbours

1. **Ashby's requisite variety is a direct conceptual neighbour.** It makes regulation depend on sufficient regulator variety/information relative to disturbances and already rejects naive regulation with too little variety.

2. **Conant & Ashby (1970) is an even closer knowledge/model neighbour.** *Every good regulator of a system must be a model of that system*, International Journal of Systems Science 1:89–97, DOI `10.1080/00207727008920220`, proves under its assumptions that a maximally successful and simple regulator must model the system being regulated.

3. **Exact control-relevant state abstraction is classical.** Givan, Dean & Greig (2003), *Equivalence notions and model minimization in Markov decision processes*, Artificial Intelligence 147:163–223, DOI `10.1016/S0004-3702(02)00376-4`, develops exact state equivalence/minimization for MDPs. Bisimulation and homomorphism literatures broaden this substrate.

### Focused-search result

The focused search did **not** locate a direct predecessor with the exact CREST joint quantification:

- add exactly one controllable action;
- robust viable-carrier gain exactly one world;
- retained present slice required state `1 -> 2^m` for arbitrary `m`;
- fixed-monitoring debt `0 -> m` bits under unchanged evidence;
- full required state becomes unlicensed;
- a declared coarse target remains deterministically reportable.

That absence is not a priority certificate. Status: `exact_cross_gate_neighbour_not_found_in_focused_search_priority_unresolved`.

### Claim rule

Foreground the **separation theorem**, not the broad idea that regulators need information:

> For every `m`, we give one connected finite witness in which the smallest nonzero carrier gain coexists with an arbitrary `m`-bit increase in required present-state/monitoring resolution, while a coarser declared target remains reportable.

Do not claim invention of requisite variety, good-regulator modeling, state abstraction, or the general proposition that additional control can require additional knowledge.

## Chapter 7 / MLTR — transfer/homomorphism literature is direct; inherited route semantics is the defensible locus

### Direct neighbours

1. **MDP bisimulation/model minimization is classical.** Givan, Dean & Greig (2003) gives exact equivalence and model minimization machinery.

2. **MDP/SMDP homomorphisms explicitly address abstraction and transfer across related domains.** Ravindran & Barto's homomorphism programme characterizes similarities/projections between MDPs, including transfer, task-specific representation and cases where source/target state or action spaces differ. Their 2003 SMDP-homomorphism work is a direct nearest-neighbour family.

3. **Modern transfer literature treats task similarity as a condition for reusing source knowledge.** Current surveys explicitly distinguish source/target structural mappings from performance-based transfer and note that mappings are required when state/action spaces differ.

### Focused-search result

The focused search did **not** locate a direct theorem with MLTR's exact source-relative route statement:

- carry one already meaningful source label map through each declared replacement route;
- route-independent inherited semantics iff complete carried terminal maps agree;
- when they disagree, equality classes of complete carried maps are exactly the minimum immutable history modes needed to preserve all inherited route semantics;
- source-relative fixed-point repair is the unique coarsest exact refinement after a carried map is fixed;
- distinct carried maps are allowed to refine to the same unlabeled terminal partition.

Again, this is not proof of firstness. Status: `route_semantics_history_neighbour_not_found_in_focused_search_priority_unresolved`.

### Claim rule

Foreground **preservation of inherited semantics**, not generic target abstraction or generic path dependence:

> We characterize when one inherited source macro-law has a route-independent carried meaning after declared structural replacement, and when it does not, the equality classes of complete carried terminal maps give the necessary-and-sufficient immutable history context before source-relative exact repair.

Do not claim invention of bisimulation, homomorphism, partition refinement, transfer learning, or the generic observation that history/path dependence may matter.

## Secondary focused check — Chapter 8 exact threshold

A focused search for the literal form `2-2^(1/k)` and close common-mode/redundancy wording did not return a direct predecessor for the CED two-read allocation boundary. General imperfect-detection allocation and common-mode-failure/diversity literatures are clearly prior art, so the threshold remains `formula_priority_unresolved`, not priority-cleared.

Safe wording remains:

> Under the declared equal-cost two-read contract, we derive the exact boundary `p*=2-2^(1/k)` separating depth-favoured from independent-mode-favoured joint detection.

## Resulting novelty posture

| Chapter | Direct prior motif found? | Priority status | Defensible locus |
|---:|---|---|---|
| 5 CCOC | yes: future equivalence, bounded-local machine composition, one-transition state blow-up motifs | package-only; priority unresolved | simultaneous fixed-resource exact response-interface extremal package |
| 6 CREST | yes: requisite variety/model requirements/state abstraction | exact cross-gate neighbour not found; priority unresolved | +1 carrier versus arbitrary required-resolution debt with coarse-target retention |
| 7 MLTR | yes: bisimulation/homomorphism/transfer | exact route-semantic neighbour not found; priority unresolved | inherited carried-map route coherence and minimum history modes |
| 8 CED | yes: detection allocation/common-mode failure generally | exact formula neighbour not found; priority unresolved | target-specific exact two-read boundary plus separate availability ceiling |

## Global publication firewall

A focused nearest-neighbour search can downgrade a claim but cannot promote it to historical firstness. Until a chapter-specific exhaustive historical audit is completed, use result language (`we prove`, `we derive`, `we construct`) and avoid priority language (`first`, `novel theorem`, `previously unknown`, `new mathematical principle`).
