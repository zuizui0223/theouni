# Theory Universe Revision Reserve v0.1

Status: **self-application safeguard outside the frozen v0.5 semantic core**.

The Theory Universe applies TU-1 to itself.

`FREEZE_v0.5.json` guarantees the identity of the **stored compressed theory representation**. It does not guarantee that a later scientific contract can be reconstructed from that compressed representation alone.

Therefore:

```text
Freeze integrity
    !=
Future revisability
```

This document defines a bounded **Revision Reserve**: provenance and richer source material retained so that some distinctions omitted by the frozen synthesis can be reopened later.

It is intentionally not called a universal revision guarantee.

---

## 1. Self-application of TU-1

Let

\[
P_{v0.5}
\]

be the stored semantic representation frozen by `FREEZE_v0.5.json`.

A later theory contract may require a revised representation

\[
Q_{future}.
\]

TU-1 says state-only revision is possible only if

\[
Q_{future}
\text{ factors through }
P_{v0.5}.
\]

Nothing about a checksum or immutable file manifest makes that factorization true.

The freeze therefore answers:

> "What exactly did we store?"

not:

> "Will this stored representation answer every future question?"

---

## 2. What the reserve retains

The revision reserve points to material richer than the frozen synthesis:

1. **source-repository theorem/evidence snapshots** — provenance pointers in `universe/PROVENANCE.json` and the source repositories themselves;
2. **Git history** — earlier and later versions of theory, registry, proofs, non-claims, and rejected formulations;
3. **source-owned detailed theorem documents** — CREST, CCOC, MLTR, MRM, CED, RACH, eco-genetic and warning repositories remain separate rather than being physically collapsed into `theouni`;
4. **explicit open-obligation and non-claim ledgers** — distinctions intentionally not resolved by the frozen core;
5. **semantic patches** — e.g. `CLARIFICATION_v0.5.1.md`, which narrows interpretation without overwriting the historical freeze;
6. **bridge provenance** — typed bridge registries preserve where a compressed cross-repository statement came from.

The reserve therefore protects against one avoidable failure mode: losing a distinction merely because the synthesis omitted it while the richer source material still existed.

---

## 3. What the reserve cannot guarantee

The reserve does **not** solve TU-1 in general.

A future contract may require distinctions that were never measured, modeled, recorded, or even conceived. No repository manifest can reconstruct information that never existed in the retained record.

Therefore the Theory Universe explicitly rejects:

```text
source history retained
    =>
universal future revisability
```

The strongest claim is:

> **Known source distinctions and historical formulations remain reopenable when their provenance has been retained; arbitrary future-contract adequacy is not guaranteed.**

This is the self-consistent application of TU-1.

---

## 4. Identity, provenance, and revisability are three different guarantees

| Guarantee | Question | Current mechanism |
|---|---|---|
| identity | what exact compressed theory was frozen? | `FREEZE_v0.5.json` + blob SHA validation |
| provenance | where did each compressed claim/object come from? | source SHAs, source paths, portfolio registry, bridge registry |
| bounded revisability | can richer known distinctions be reopened? | source repositories + Git history + explicit reserve pointers |

None implies the other automatically.

---

## 5. Reserve policy for future theory revisions

A future v0.6+ change should, where possible, record:

- which old distinction became insufficient;
- which future/new contract exposed the insufficiency;
- whether the needed distinction existed in the reserve;
- which source file/commit restored it;
- whether genuinely new information/theory was required;
- whether the revision changes an axiom, theorem, claim ceiling, or only notation.

This creates a practical revision ledger rather than pretending the old frozen state was universally sufficient.

---

## 6. Relation to the v0.6 quotient-transport draft

`DRAFT_v0.6_CONTRACT_INDEXED_QUOTIENT_TRANSPORT.md` states the general reuse criterion:

\[
R\models\beta
\iff
\Sigma_\beta\text{ factors through }R.
\]

The freeze is one retained representation `R`. The revision reserve does not change its fibers; it provides access to **richer alternative representations** that can be reopened when `R` fails for a new task.

Thus the reserve is not a theorem escape hatch. It is an operational response to theorem failure.

---

## 7. Design consequence

The Theory Universe should preserve both:

```text
compressed canonical synthesis
```

and

```text
reopenable provenance to richer source descriptions
```

rather than trying to make one object do both jobs.

This separation mirrors the general worldview:

> **Compression is useful precisely because it forgets; responsible science therefore also records how to reopen richer descriptions when future responsibilities change.**
