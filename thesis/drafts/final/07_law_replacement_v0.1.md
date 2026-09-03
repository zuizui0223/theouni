<!-- draft-id: chapter:7:v0.1 -->
# 法則は構造置換を越えない

*English working title: Laws Do Not Automatically Survive Structural Replacement*

> **Draft status:** source-bounded v0.1 from MLTR snapshot `d9e23d27c385759b9e1fea93a556f30618122fe1`. The chapter concerns exact reuse of an inherited source macro-law under a declared finite source–target replacement relation. It does not infer natural replacement history from data and does not claim novelty for generic partition refinement, lumpability, or bisimulation.

## 1. Reusing a law after structural change is a testable proposition

Ecological laws are often carried across structural change almost silently. A state variable calibrated in one community is retained after species turnover. A functional grouping defined before rewiring is reused after links change. A response law estimated under one management configuration is applied after a component is replaced. Sometimes this is scientifically reasonable. The problem is that the validity of reuse is often treated as a matter of naming continuity rather than a property that can be tested.

The forbidden inference of this chapter is:

> **ある構造で成り立った法則 ⇒ 置換後の構造でも成り立つ法則**

MLTR asks a sharper question. Suppose a source system already has an exact macro-law and a declared relation tells us how source states are carried into a structurally changed target. Under exactly what condition does the inherited law remain exact? If it fails, what is the least source-relative repair? And if the same terminal target can be reached by several replacement routes, when can those routes still share one inherited law without recording history?

The answer is not “structural change usually breaks laws.” It is a sequence of exact conditions. First, portability has a necessary-and-sufficient fiber test. Second, failure has a finite local witness. Third, relative refinement produces a unique coarsest exact repair. Fourth, route independence is possible exactly when complete carried terminal maps agree; otherwise one immutable history mode per distinct carried map is necessary and sufficient to preserve inherited semantics. [L1]

This converts transfer from a vague extrapolation judgment into an auditable structural statement.

## 2. Start with a source law and a declared replacement relation

Let a finite controlled source system possess an exact source partition \(P_S\). Its blocks are source macrostates: within each block the output, legal-action structure, and successor macrostate are representative-independent.

A target system need not have the same microstate space. Instead, MLTR assumes a declared total label-consistent source–target relation. That relation induces a carried target label map and therefore a carried partition \(P_C\) on the target.

This distinction is important. MLTR does not ask for the best target abstraction from scratch. It asks whether **this inherited source semantics** survives the declared replacement. The source labels are therefore a constraint, not merely an initialization convenience.

That source-relative framing also fixes the claim ceiling. A positive transport defect does not prove that the target admits no compact abstraction whatsoever. It proves that the inherited source law cannot remain exact without a minimum amount of source-relative repair. Abandoning source provenance defines a different problem. [L2]

## 3. Portability has an exact if-and-only-if condition

Consider one carried target fiber: all target microstates that inherit the same source label. For the inherited law to remain exact, three quantities must be independent of which representative of that fiber is chosen:

1. the target output;
2. the row of legal actions;
3. for every declared legal action, the carried label of the target successor.

The MLTR master theorem states:

> **The carried source partition is an exact target macro-law if and only if output, legal-action rows, and successor carried labels are constant inside every carried target fiber.** [L1]

### Necessity

If the inherited quotient is exact, quotient output cannot depend on the representative microstate. Nor can action legality. And when an action is legal, the quotient successor must be well-defined. Therefore every two target states inside one inherited fiber must agree on all three quantities.

### Sufficiency

Conversely, if all three quantities are constant inside every carried fiber, they define representative-independent quotient functions on the inherited labels. The target dynamics therefore descend to the carried quotient. The inherited source labels remain an exact target macro-law.

The condition matters because “same variable name” or “same biological category” is weaker than exact portability. A source label survives only when the target dynamics treat all of its inherited members as the same macrostate for the responsibilities encoded by the law.

## 4. Failure has a finite local certificate

The portability theorem immediately gives a useful converse. If inherited portability fails, one need not diagnose the entire target model globally. At least one carried fiber contains a finite pair of target states that disagree in one of the required quotient quantities.

A failure certificate can therefore be one pair \(x,y\) with the same inherited source label such that either:

- their outputs differ;
- their legal-action rows differ; or
- some declared action takes them to successors with different carried source labels.

Any such pair is sufficient to reject unchanged portability. [L1]

This local obstruction is scientifically important. Structural failure does not need to be described as “the model changed a lot.” One can identify the exact inherited state that has become semantically heterogeneous and the target operation that exposes the difference.

An ecological example is a target-only intervention. Two target configurations may both inherit the same source functional state, yet removal of a competitor or exclusion of a pollinator may send them to different inherited successor labels. Before that intervention the inherited grouping may look harmless. Once the new target action is included in the declared responsibility, the within-fiber successor disagreement is a direct certificate that the old law no longer descends exactly. [L3]

## 5. Failure does not mean starting over: there is a unique coarsest exact repair

Once unchanged portability fails, a common response is to rebuild a target model from scratch. MLTR instead asks for the least exact repair that preserves source provenance.

Starting from the carried partition \(P_C\), repeatedly split blocks whenever states inside a block disagree in:

- output;
- legal-action row; or
- successor block under a declared legal action.

Because the target is finite and each operation only refines the current partition, the process terminates.

The fixed point is exact by construction. More importantly, it is not merely *an* exact refinement. The master theorem proves it is the **unique coarsest exact target partition refining the carried source partition**. [L1]

### Why coarsest is proved, not asserted

Let \(E\) be any exact target partition that refines the carried source labels. At the first refinement step, exactness of \(E\) forces \(E\) to distinguish every output, legality, or successor difference used by the operator. Thus \(E\) refines the first iterate. Repeating the argument inductively shows that \(E\) refines every iterate and therefore refines the stabilized partition.

Hence no source-relative exact repair can be coarser than the fixed point. Since the fixed point itself is exact, it is uniquely minimal in the refinement order.

This distinction removes another source of “obviousness.” The result is not merely that more states may be required after replacement. It identifies the least exact state increase compatible with keeping the inherited source meaning.

## 6. Transport defect is tied to that minimal repair

Once the unique coarsest repair \(P_R\) is established, MLTR records the source-relative repair burden through increases such as

\[
\Delta_{\mathrm{states}}=|P_R|-|P_C|
\]

and the associated log-state or bit increase. These quantities are called transport defects in the source programme. [L2]

The defect is not a theorem by itself. Its meaning comes from the minimality theorem: because every exact source-relative target description must refine \(P_R\), no competing source-relative exact representation can use fewer repaired states.

An accumulating witness family shows that repair can grow strongly: the repaired-state count can reach \(2^m+1\) with state-count defect \(2^m-1\) in the declared family. [L1]

The dissertation should therefore avoid presenting “defect” as a newly invented distance with automatic ecological interpretation. It is a bookkeeping quantity attached to a proved minimal repair. Its scientific content is source-relative: how much extra distinction must be retained before this inherited law becomes exact again?

## 7. Route independence is a separate problem from single-route repair

So far the source-to-target relation has been treated as one route. Structural replacement can instead occur through several sequences. A terminal community or network may be reachable after different turnover orders, management histories, or module replacements.

The key question is not whether the final target microstate space is the same. It is whether the **inherited source labels carried to the terminal target are the same maps** under all declared routes.

For each root-to-terminal path \(h\), let \(c_h\) denote the complete carried terminal label map. MLTR proves:

> **One route-independent inherited terminal law exists exactly when all declared root-to-terminal paths induce the same complete carried terminal map.** [L1]

If all \(c_h\) agree, the target receives one route-free inherited labeling. Since relative repair is a deterministic function of that carried assignment and the terminal controlled system, the repaired partition and transport defect are route independent as well.

This condition is stronger than saying the paths induce partitions with the same number of blocks. It is also stronger than saying their unlabeled partition shapes look the same. The inherited labels themselves carry source semantics.

## 8. Different carried maps force history context—but only in a precise sense

Suppose two paths induce different terminal carried maps. Then at least one terminal configuration receives different inherited source labels along those paths. A single route-free carried label map cannot preserve both assignments simultaneously.

This is the exact obstruction repaired by history augmentation.

Index the distinct carried maps by an immutable history mode \(H\). Within each history slice the carried label map is now well-defined, so the source-relative exact repair can be applied normally.

The central Section 5 result is:

> **Two replacement histories may share one immutable history mode if and only if their complete carried terminal maps are identical. Therefore the minimum number of history modes equals the number of distinct carried terminal maps.** [L1,L4]

### Necessity

If two different carried maps were assigned the same history mode, that mode would have to give one inherited source label to a terminal state where the two routes require different labels. It could not preserve both path-specific inherited semantics.

### Sufficiency

If two paths carry exactly the same map, one mode preserves the same inherited assignment for both. Grouping paths by equality of carried maps therefore supplies a compatible history assignment using exactly one mode per distinct map.

The source tests exhaust small path families, verify that any assignment using fewer modes than the number of distinct maps is incompatible, and confirm invariance to path ordering up to renaming of mode labels. [L4]

This is much stronger than saying “history can matter.” It says exactly when history can be forgotten and exactly how much immutable route context is minimally required when it cannot.

## 9. The claim is about inherited label semantics, not unlabeled partition shape

The history theorem has an important boundary. Two different carried terminal maps can, after all required exact refinements, happen to yield the same **unlabeled** final partition shape. MLTR does not claim otherwise. [L1]

Why then are different history modes still necessary? Because the problem is not only to reproduce an unlabeled grouping of terminal states. The scientific responsibility is to preserve which inherited source macrostate each target state came to represent.

The proof tests explicitly include distinct inherited label maps with identical partition shape. They still require distinct history modes because the inherited assignments differ. [L4]

This is the right place to keep “history” from becoming metaphysical. MLTR does not infer a natural historical variable from target data. The immutable mode is a representation device required by the declared source-relative semantics when replacement routes disagree.

## 10. Portability, repair, and history answer three different questions

The chapter is easiest to understand if the three levels remain separate.

**Portability:** Can the inherited source law be reused unchanged on one declared target relation?

Answer: yes **iff** output, legal-action rows, and successor carried labels are constant within every carried fiber.

**Repair:** If unchanged portability fails, what is the least exact source-relative target law?

Answer: the fixed-point refinement initialized by the carried labels gives the unique coarsest exact repair; its state/bit increase is minimal.

**History:** If several replacement routes reach the same terminal target, can they share one inherited semantics?

Answer: yes **iff** their complete carried terminal maps agree. Otherwise one mode per distinct map is necessary and sufficient before relative exact refinement.

The three results should not be collapsed. A law can fail unchanged portability on every route yet have the same repaired result across routes. Conversely, routes can require different inherited label modes even if their final unlabeled repaired partition shapes coincide.

## 11. Executable proof obligations prevent semantic drift

The MLTR codebase treats these results as proof obligations rather than decorative formulas.

The history tests enumerate small families of carried maps and check that:

- minimum mode count equals the number of distinct complete carried maps;
- two paths share a mode exactly when their maps are equal;
- every attempted assignment with fewer modes is incompatible;
- permutation of path order changes at most the arbitrary names of modes;
- identical maps need no extra context;
- distinct inherited maps remain distinct even when their partition shape is the same. [L4]

Other source tests and certificates cover portability obstruction and repair behavior. The executable layer does not replace the written proof, but it locks the implementation and manuscript semantics to the theorem.

That distinction is important for this dissertation programme: a theorem is not “verified” merely because a test reproduces a few finite examples. The proof establishes the quantified statement; the tests make accidental implementation or manuscript drift harder.

## 12. Ecological interpretation: transferability is responsibility-relative

The ecological payoff is a disciplined way to discuss transfer across turnover, rewiring, replacement, restoration, or management change.

A source functional category may remain valid after replacement if every target state inheriting that category has the same output, legal interventions, and inherited successor behavior. If a newly relevant target intervention splits those responses, the old category has a finite portability obstruction. One can then retain precisely the missing distinction rather than abandoning the entire source vocabulary.

Likewise, historical context need not always be added. If two replacement routes induce the same complete inherited terminal map, history is representationally redundant for this source-relative task. Only route disagreement in the carried maps forces immutable context.

This is a more useful conclusion than “ecological laws are context dependent.” It says what context must do to become necessary.

## 13. What this chapter establishes—and what it does not

The chapter establishes, for declared finite controlled source and target systems linked by explicit source–target relations, that:

1. unchanged inherited portability has an exact necessary-and-sufficient within-fiber condition;
2. failure has a finite local witness;
3. iterative source-relative refinement terminates at the unique coarsest exact repair;
4. repair state/bit increases are minimal among exact target descriptions that preserve source provenance;
5. route-independent inherited semantics exist exactly when complete carried terminal maps agree;
6. when they disagree, one immutable history mode per distinct carried map is necessary and sufficient;
7. different carried maps need not imply different unlabeled repaired partition shapes.

It does **not** infer source–target relations from observational data. It does not claim that every ecological change requires history. It does not claim a positive transport defect rules out all compact target-only abstractions. It does not infer real replacement histories. It does not claim novelty for classical partition refinement, lumpability, bisimulation, or generic path dependence. [L2]

The safe headline is:

> **An inherited ecological macro-law survives structural replacement exactly when the target preserves the inherited distinctions needed for output, legal action and successor semantics; when it does not, source-relative repair and historical context have exact minimal forms.**

## 14. Transition: structural reuse is not evidential independence

Chapter 7 closes a reuse question about laws: an inherited law cannot be carried across replacement merely because it worked before. Its transport must satisfy an explicit exactness condition.

The next chapter concerns a different kind of reuse. Suppose an observation method has worked repeatedly. Does running that same method again necessarily create a new independent opportunity for evidence, or can all repetitions remain exposed to one shared failure domain?

MLTR does not answer that reliability question. CED owns a separate evidence architecture. The transition is therefore an editorial handoff rather than a theorem implication. [TR]

Chapter 8 asks:

> **At fixed evidence effort, when is another repetition within one failure mode better or worse than creating an independent failure mode?**

## Internal source keys

- **[L1]** MLTR `docs/master_theorem_proof.md` — portability iff, local obstruction, unique coarsest repair, minimal defect, route coherence and necessary/sufficient history completion.
- **[L2]** `docs/novelty_and_journal_strategy.md` and `docs/paper_architecture.md` — source-relative novelty boundary, defect interpretation, classical-infrastructure firewall.
- **[L3]** `docs/publication_completion_spine.md` and `manuscript/paper_a_main.tex` — ecological target-only intervention witness and publication ordering.
- **[L4]** `tests/test_section5_proof_obligations.py` — exhaustive small carried-map families, minimal history modes, path-order invariance and same-shape/different-label guard.
- **[TR]** theouni `thesis/transition_recovery_matrix.json` — Chapter 7→8 is a question handoff from structural transport to evidence failure architecture.
