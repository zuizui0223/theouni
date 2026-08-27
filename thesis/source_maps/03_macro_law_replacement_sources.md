# Source map — Chapter 3 v0.2

This map supports `thesis/drafts/03_macro_law_replacement_v0.2.md`. MLTR remains the owner of the transport, repair, defect, history, proof, replay, figure, and manuscript assets.

## A. MLTR source package

### Publication manuscript

**Source:** `zuizui0223/mltr:manuscript/paper_a_main.tex`

Supports:

- the source-relative ecological model-reuse problem;
- relation to lumpability, bisimulation, transportability, resilience, and adaptive management;
- operational source/target setup;
- portability, local obstruction, repair, defect, and history results;
- plant–pollinator turnover example and restoration-priority interpretation;
- scope and non-claim language.

### Manuscript architecture and results

**Sources:**

- `zuizui0223/mltr:docs/paper_architecture.md`
- `zuizui0223/mltr:docs/paper_results_discussion.md`

Support the decision chain:

```text
unchanged transport
    -> if failure: local witness and unique coarsest repair
    -> transport defect
    -> if multiple routes agree: route-independent semantics
    -> if routes disagree: minimum history augmentation
```

### Core theorem notes

**Sources:**

- `zuizui0223/mltr:docs/transport_defect.md`
- `zuizui0223/mltr:docs/path_coherence.md`
- `zuizui0223/mltr:docs/history_augmentation.md`

Support:

- the relative exact-refinement theorem;
- defect definitions and accumulating binary family;
- path-label coherence and route-independent repair;
- minimum history-mode theorem;
- history-sliced coarsest exact repair;
- proof and claim ceilings.

### Finite examples

**Source:** `zuizui0223/mltr:manuscript/supplement_examples.tex`

Supports:

- the accumulating repair family;
- coherent and incoherent replacement-history witnesses;
- the plant–pollinator label split `(0,0,1) -> (0,1,2)`;
- interpretation of substitute-pollinator response capacity and restoration-priority reversal.

The example is finite and diagnostic, not an empirical fitted system.

## B. Defensible novelty boundary

**Source:** `zuizui0223/mltr:docs/novelty_and_journal_strategy.md`

MLTR does not claim novelty for:

- fixed-system lumpability;
- generic bisimulation;
- coarsest partition refinement;
- quotient construction;
- open-grammar interface lower bounds;
- statistical or causal transportability.

The chapter-level contribution is the constrained problem:

> an accepted source partition is carried through a declared, possibly non-nested replacement, and the target repair must preserve every inherited merge that remains exact.

That source-relative constraint makes the repair unique and minimal relative to inherited semantics, supports the transport-defect measure, and permits exact route/history completion.

## C. Boundary from CCOC Chapter 2

### CCOC

- one controlled plant remains fixed;
- legal future grammar changes;
- each closed interface may be independently optimized;
- headline compares closed minima with open minimum.

### MLTR

- source and target systems may be non-nested;
- one accepted source law is fixed;
- a relation carries source labels;
- every target repair must refine the carried partition;
- route coherence and history augmentation are owned.

Target-only actions can create an MLTR obstruction, but this does not transfer the CCOC cross-grammar theorem or its fixed-alphabet local realization to MLTR.

## D. Boundary toward MRM Chapter 4

MLTR treats source/target systems and replacement relations as declared. It does not ask which latent mechanism family is true or whether retained candidate mechanisms agree on intervention responses.

The Chapter 3 → Chapter 4 transition is:

- MLTR: can one inherited law retain meaning after structural replacement?
- MRM: after the state/response domain is declared, can one deterministic law survive retained mechanism uncertainty?

Do not reinterpret replacement histories as MRM mechanism candidates without an explicit bridge.

## E. Plant–pollinator example boundary

Allowed claims:

- a finite source binary functional classification can become insufficient after turnover;
- one target-only restoration response splits the inherited low-service fiber;
- the exact repair adds substitute-pollinator response capacity;
- the repaired classification can reverse a restoration priority under the declared target.

Prohibited upgrades:

- no natural pollinator turnover relation is inferred;
- no substitute pollinator taxon is identified;
- no field transition probability is estimated;
- no universal restoration rule is established;
- no empirical state sufficiency is claimed.

## F. Reproducibility and proof boundary

Canonical execution remains in MLTR:

```bash
python -m pip install -e '.[dev]'
pytest
python scripts/verify_transport_core.py --write-report
```

Deterministic replay and tests verify the implemented finite witnesses and theorem contracts. Analytic arguments in the theorem notes and manuscript remain the proof basis.

## Section-to-source matrix

| Chapter section | Primary source | Secondary source | Claim ceiling |
|---|---|---|---|
| 1–2. Replacement/reuse problem | paper manuscript | novelty strategy | Source-relative, not target redesign |
| 3. Operational setting | paper + theorem programme | README | Declared finite relation |
| 4. Portability/obstruction | paper + theorem notes | replay | No empirical relation inference |
| 5. Unique repair | transport-defect note | paper | Standard refinement substrate |
| 6. Defect family | transport-defect note | supplement examples | Growing probe alphabet; not empirical scaling |
| 7. Multiple histories | path coherence + history augmentation | paper | Declared histories only |
| 8. Plant–pollinator example | paper + supplement examples | figure specs | Finite diagnostic witness |
| 9. Related theory | novelty strategy + paper | cited literature | No generic bisimulation novelty |
| 10. Ecological implications | paper discussion | source map | No natural-state claim |
| 11. Limits/MRM transition | paper scope | dissertation architecture | No mechanism-truth claim |

## Remaining work

1. Verify final bibliography metadata and journal/style formatting.
2. Decide whether to reuse or redraw the MLTR figure set in dissertation style.
3. Cross-reference full proofs to MLTR theorem notes rather than duplicating all inductions.
4. Confirm the plant–pollinator action/state labels used in the chapter match the final source figure captions.
5. Preserve the distinction between raw history-mode cost and final history-aware exact repair.
