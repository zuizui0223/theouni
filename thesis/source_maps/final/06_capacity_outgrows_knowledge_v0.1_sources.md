# Source map — Chapter 6 v0.1: 能力は知識を追い越す

This map supports `thesis/drafts/final/06_capacity_outgrows_knowledge_v0.1.md` and is locked to CREST snapshot `2ff41e18cdbf100932813fbef9851078ec60413a`.

## Snapshot and chapter contract

- owning repository: `zuizui0223/crest`
- recovered/current snapshot: `2ff41e18cdbf100932813fbef9851078ec60413a`
- verification class: `verified_exact_connected_capability_resolution_divergence_plus_no_bound_and_target_reportability`
- forbidden inference: `介入の規模が小さい ⇒ 表現と監視の負担も小さい`
- chapter claim ceiling: finite deterministic existence/no-bound theorem under declared controlled-system, evidence and target contracts; no claim that every small intervention creates a large burden, no empirical monitoring-cost estimate, and no causal proportionality from carrier gain to state complexity.

## A. Headline theorem: fixed capability gain, arbitrary resolution burden

### A1 — `docs/crest_capability_resolution_divergence_theorem_2026-08-22.md`

For every integer `m>=1`, CREST constructs one connected finite deterministic controlled system with one newly admitted controllable action `probe` such that:

1. the greatest robust controlled carrier gains exactly one compatible world;
2. a retained present slice `U_0` refines from one exact future-sensitive state to `2^m` exact states;
3. present-slice state complexity therefore increases by exactly `m` bits;
4. unchanged one-block evidence moves from zero monitoring debt to exactly `m` bits of debt;
5. full required-state identification changes from licensed to unlicensed;
6. a declared coarse target can remain deterministically reportable.

The action and output alphabets remain bounded independently of `m`.

## B. Proof obligations

### B1 — carrier gain exactly one

Under the old repertoire, all chain worlds and safe sink `s` have legal safe action `hold`; special world `r` lacks safe control and is excluded. Under the expanded repertoire, `r --probe--> s`, while all old safe `hold` transitions remain unchanged. Therefore

`K_m^{*+}=K_m^{*-} union {r}`

and `Delta |K^*|=1` exactly.

### B2 — old state on the retained slice is one block

Every world in `U_0` is `neutral` and self-loops under the only old legal action `hold`. All have the same complete old legal future trace, so

`|J_m^- |_{U_0}|=1`

and present-slice state complexity is zero.

### B3 — new state is discrete over `2^m` addresses

For any distinct address vectors `x,y`, repeated use of `probe` reaches the first differing address readout and produces `bit0` versus `bit1`. Hence no exact future-sensitive state can merge distinct present addresses after expansion. Therefore

`|J_m^+ |_{U_0}|=2^m`

and `K_{U_0}(J_m^+)=m`.

### B4 — fixed evidence debt

Keep the evidence map one-block on `U_0`. It identifies the old one-block required state but not the new `2^m`-block state. Under the declared finite monitoring-resolution debt,

`D_{U_0}(E,J_m^-)=0`,

`D_{U_0}(E,J_m^+)=m`.

### B5 — target-only reportability

Choose a target constant on `U_0`. The unchanged evidence continues to identify that target even though it no longer identifies the full new required state. This separates target licensing from full-state licensing.

### B6 — no-bound corollary

Because `Delta |K^*|=1` for every `m` while `Delta K_{U_0}=m`, no finite universal function depending only on carrier-size gain can upper-bound required present-state resolution across the declared class.

## C. Connectedness removes the disjoint-gadget shortcut

The same `probe` trajectories that read the address bits eventually enter the uniquely newly viable world `r`, and `r` becomes viable because `probe` reaches safe sink `s`.

Authorized interpretation:

> one fixed-size capability expansion can simultaneously have constant viability effect and unbounded representational/evidence effect in one connected response system.

Forbidden interpretation:

> the +1 carrier gain causes the `m`-bit debt or determines its magnitude.

The theorem is a coexistence/no-bound result, not a proportional causal law.

## D. Executable verification

### D1 — `tests/test_crest_capability_resolution_divergence.py`

The source tests verify the connected arbitrary-scaling witness and its no-bound contract.

### D2 — source manuscript/supplement controls

`manuscript/crest_biology_philosophy_blinded_submission.md` and `manuscript/CREST_supplementary_information.md` carry the theorem in the active submission architecture and retain novelty/claim firewalls around state abstraction, control theory and classical finite refinement substrate.

The dissertation may re-explain the result but does not take theorem ownership from CREST.

## E. Monitoring-resolution debt semantics

### E1 — `docs/crest_monitoring_resolution_debt_2026-08-21.md`

The monitoring debt is a finite partition-resolution quantity: how much additional evidence refinement is needed to identify the required state under the declared evidence contract.

It is **not**:

- monetary field cost;
- sample size;
- Shannon entropy under an empirical probability distribution unless separately defined;
- psychological knowledge;
- a claim that nature itself stores `m` scientific bits.

The chapter uses `m bits` in this exact finite quotient sense only.

## F. Controlled carrier, required state, evidence and target remain different gates

### F1 — `docs/crest_mathematical_spine.md`

CREST keeps the following typed objects separate:

- greatest robust controlled carrier / viability;
- least exact future-sensitive required state;
- evidence/monitoring partition;
- report target.

The headline theorem is powerful because the same capability expansion moves these gates by different amounts:

- carrier: `+1` world;
- state: `+m` bits on `U_0`;
- evidence debt: `+m` bits;
- coarse target: still reportable.

Do not collapse these into one scalar “system complexity”.

## G. Positive/non-universal boundary

The theorem does not say every capability expansion creates debt. The burden grows only when the newly legal controlled futures split worlds that the old exact state/evidence merged.

If the expanded action repertoire leaves all old merged present worlds future-response equivalent for the declared responsibility, no such refinement is forced on that slice. Likewise, if the requested target factors through the retained evidence, target reporting can remain licensed even when the full state refines.

This positive side is used as interpretation of the exact quotient/target conditions, not claimed as a separate novelty theorem.

## H. Neighboring chapter boundaries

### H1 — Chapter 5 → 6

CCOC changes legal future grammar and proves open-future response-interface inflation under fixed local resources. CREST changes controllable repertoire and viability and proves +1 carrier versus arbitrary state/evidence burden. Similar language about future actions does not make the estimands identical.

### H2 — Chapter 6 → 7

CREST remains within one controlled carrier/system description. MLTR changes source/target structure and asks whether an inherited law transports through a declared replacement relation. Capability expansion does not prove structural law portability or failure.

## Section-to-source matrix

| Draft section | Primary source | Proof/verification | Main boundary |
|---|---|---|---|
| 1. Nontrivial question | A1 | recovery/proved-condition registry | +1 viability effect fixed |
| 2. Controlled carrier | F1 | carrier theorems | action count ≠ capability consequence |
| 3. Connected construction | A1 | D1 | one action/output alphabet bounded |
| 4. Carrier theorem | B1 | D1 | exact +1 world |
| 5. Old present state | B2 | D1 | one old future-response block |
| 6. New state | B3 | D1 | `2^m` exact response classes |
| 7. Monitoring debt | B4/E1 | D1 | partition debt, not field cost |
| 8. No-bound corollary | B6 | all-m proof | carrier gain alone insufficient |
| 9. Target-only report | B5/F1 | source target tests | full state ≠ target licensing |
| 10. Connectedness | C | source witness | coexistence, not causal proportionality |
| 11. CREST gates | F1 | source proof ledger | typed objects remain separate |
| 12. Positive boundary | G | exact quotient logic | theorem is possibility/no-bound, not inevitability |
| 13. Ch5 relation | H1 | transition validator | grammar ≠ capability |
| 14. Scope | A–G | claim firewall | no empirical monitoring cost |
| 15. Transition to MLTR | H2 | transition validator | capability ≠ structural replacement |

## Drafting gate

1. Keep `Delta |K^*|=1` and `Delta K=m` on the same visual/argument line; the contrast is the theorem.
2. Show the old one-block state and new `2^m` address distinction before introducing monitoring debt.
3. Keep the coarse-target-retention result visible so “full state unlicensed” is not misread as “nothing can be reported.”
4. State explicitly that the connected construction blocks a disjoint-gadget objection but does not establish carrier-gain causation.
5. Use monitoring `m bits` only in the declared partition-resolution sense.
6. Keep CCOC grammar expansion and MLTR structural replacement outside CREST theorem ownership.
