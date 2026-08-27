# Audit — MLTR source-relative transport, repair, and history boundary

## Purpose

MLTR uses familiar partition and transport language and is therefore vulnerable to three reductions:

1. “ordinary target bisimulation after replacement”;
2. “CCOC with a changed state space”;
3. “history always matters.”

This audit fixes what the chapter actually owns.

## 1. Source-relative repair versus target-only abstraction

Let `carry(q_S)` be the inherited target partition. MLTR solves

\[
\min_{q_T\text{ exact},\;q_T\succeq\operatorname{carry}(q_S)}|q_T|.
\]

The carried labels constrain the admissible target partitions. Generic target-only minimization instead solves for any exact target quotient and can merge across inherited labels.

### Consequence

The unique coarsest MLTR repair is not necessarily the globally smallest target abstraction. It is the smallest exact target interface that preserves every source merge and distinction the carried semantics require.

### Wording lock

Preferred:

> Standard refinement machinery, initialized by the carried source labels, returns the unique coarsest exact repair of the inherited law.

Avoid:

> MLTR introduces a new coarsest-bisimulation algorithm.

## 2. Transport defect versus quotient size

The defect

\[
\Delta_{\#}=|Q_T^{\min}|-|Q_S|,
\qquad
\Delta_K=\log_2|Q_T^{\min}|-\log_2|Q_S|
\]

is relative to the accepted source law and its unique repaired target refinement.

It is not:

- target quotient size alone;
- a distance between ecosystems;
- financial repair cost;
- empirical sampling effort;
- a claim that the inherited semantics should always be retained.

Without the source-relative constraint, the defect loses its canonical interpretation.

## 3. CCOC versus MLTR

| Question | CCOC | MLTR |
|---|---|---|
| What changes? | legal future grammar | source system is replaced by a possibly non-nested target |
| What is fixed? | controlled plant | inherited source partition and declared relation |
| Optimization | independent closed minima versus open minimum | target minimum constrained by carried source labels |
| Main quantity | cross-grammar interface gap | source-relative transport defect |
| History | not owned | route coherence and minimum history completion |

A target-only action can expose an MLTR obstruction, but that is an instance of inherited-law failure, not CCOC's independently optimized closed/open comparison.

## 4. History is conditional, not mandatory

MLTR does not state that ecological history always belongs in state.

- If all declared root-to-terminal paths carry the same terminal label map, the inherited partition, exact repair, and defect are route independent. No history mode is needed.
- If paths carry different complete terminal maps, a route-free inherited law is impossible. The minimum number of immutable modes equals the number of distinct carried maps.
- After history slicing, exact refinement may merge contexts again if all carried labels and legal futures agree.

### Wording lock

Preferred:

> History enters the transported state only when different declared histories carry different operational meanings that do not factor through the terminal configuration alone.

Avoid:

> MLTR proves that ecological states are historical.

## 5. MLTR versus MRM

MLTR assumes declared source/target dynamics and relations. MRM begins with retained candidate mechanisms on an aligned observable response domain.

- A replacement path is not automatically a mechanism candidate.
- A repaired MLTR state is not automatically mechanism-robust.
- MRM response-type disagreement can require a further split after MLTR repair.
- Conversely, mechanism agreement does not supply an inherited source-label map.

The legitimate transition is from semantic transport after system change to law robustness under unresolved mechanism alternatives.

## 6. Plant–pollinator witness

The finite label split

\[
(0,0,1)\to(0,1,2)
\]

is a local source-relative repair. The new state records substitute-pollinator response capacity and can change the restoration priority under the declared target action.

It does not establish:

- empirical pollinator turnover classes;
- deterministic natural restoration outcomes;
- universal priority rules;
- a field-identified replacement relation.

## 7. Chapter-level novelty statement

Use:

> Existing exact aggregation theories characterize valid quotients within a specified system. MLTR instead fixes an accepted source macro-law, carries it through a declared possibly non-nested replacement, and characterizes unchanged portability, local failure, the unique coarsest exact source-relative repair, the associated transport defect, and the minimum historical context required when replacement routes carry incompatible meanings.

Do not sell generic refinement, bisimulation, lumpability, or “history matters” as the novelty.

## Claim ceiling

This audit is editorial and type-theoretic. It does not establish historical priority over all constrained-bisimulation or model-evolution literatures, infer ecological replacement maps, or create a theorem connecting MLTR to CCOC or MRM beyond the declared boundaries.
