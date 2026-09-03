# Proved-condition recovery ledger

## Why this ledger exists

The dissertation must not gain apparent depth by introducing names, definitions, or equations without establishing when a scientific conclusion follows. The recovery standard is therefore stronger than `forbidden_inference` alone.

For each research chapter, ask:

1. **Question** — what decision, identification, portability, or reporting problem is unresolved?
2. **Condition** — what necessary, sufficient, necessary-and-sufficient, lower-bound, no-bound, or exact finite condition answers it?
3. **Proof** — where is the argument establishing the condition?
4. **Sharpness / converse** — can the condition fail, reverse, or attain its bound?
5. **Verification** — is there an independent finite oracle, exhaustive test, or locked evidence application?
6. **Claim ceiling** — what stronger statement is still forbidden?

A formula without this chain is not counted as a recovered chapter result.

## Current chapter conditions

| Chapter | Proved condition | Recovery status |
|---|---|---|
| 0 Reuse | revised task is recoverable from stored state **iff** revised response factors through old quotient | TU-1 merged; framing only |
| 1 Boundary | new exact scalar measurement reduces structural ambiguity **iff** its observation row increases rank | merged in Boundary `2919842f...`; `k-1-r` is a corollary |
| 2 EGWE | perfect event precedence fixes sensitivity but not specificity; binary AUC follows the full denominator | source PR #140 pending CI/merge |
| 3 MROD | adaptive second-step choice strictly beats best precommitted static choice **iff** no candidate is optimal in every positive-probability branch | source PR #101 pending CI/merge |
| 4 Eco-genetic criticality | one exact directionally coherent scalar exists **iff** declared target vectors form a product-order chain | source PR #77 pending CI/merge; locked H3 crossing violates condition |
| 5 CCOC | decoder addressability gives lower bound; bounded-local family attains it; separate positive portability conditions are sufficient | already merged/proved |
| 6 CREST | one-action capability expansion can have fixed carrier gain but arbitrary `m`-bit burden; hence no bound from carrier gain alone | already merged/proved |
| 7 MLTR | carried law exactness has an iff test; repair is unique coarsest; history modes equal distinct carried maps necessarily and sufficiently | already merged/proved |
| 8 CED | at fixed two-read effort, diversity vs repetition reverses at `p*=2-2^(1/k)` under the declared failure contract | source PR #50 pending CI/merge |
| 9 Synthesis | no new global iff; combines TU-1 with typed source conditions | synthesis only |

## Anti-obviousness rule

The prose form `X does not necessarily imply Y` is not sufficient when a sharper result is available. Prefer one of:

- `Y is identified exactly when ...`;
- `the strategy is strictly better iff ...`;
- `a scalar representation exists iff ...`;
- `the lower bound is ... and is attained by ...`;
- `no bound depending only on ... can exist, because ...`;
- `the ordering reverses at the explicit threshold ...`.

The dissertation may use the forbidden inference as the motivating shortcut, but the scientific result must be the recovered condition that replaces that shortcut.

## Fail-closed import rule

A theorem still living only on an unmerged source PR is recorded as `pending_ci_merge` and must not replace the canonical source snapshot in a dissertation source map. Once source CI succeeds and the PR is merged:

1. record the merge SHA;
2. switch `source_status` to `merged`;
3. update the relevant chapter source map and verification recovery record;
4. rewrite the chapter's headline result around the proved condition rather than the old slogan;
5. run the full Theory Universe validation before merging the theouni import.
