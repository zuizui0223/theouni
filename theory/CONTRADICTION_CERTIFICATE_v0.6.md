# Draft v0.6 Pairwise Contradiction Certificate

Status: **machine-generated finite typed audit; outside the frozen v0.5 core**.

Registry: [`contradiction_matrix.json`](contradiction_matrix.json)
Canonical registry SHA-256: `221db21006a287cd367007728bd9f9c16f8922cf4380c3eb978f709a1b82f831`

This certificate audits the current claim ceilings of 12 named theory modules. It proves registry completeness and the absence of a declared pairwise `actual-conflict`; it does not prove empirical truth, a missing bridge, joint-state existence, or higher-order consistency.

## Result

- Modules: **12**
- Unordered pairs: **66**
- `actual-conflict`: **0**
- Verdict: **PASS**

Relation counts:

- `compatible`: 6
- `conditional-on-common-carrier-or-map`: 19
- `orthogonal-estimand`: 23
- `open-bridge`: 18
- `actual-conflict`: 0

## Relation legend

| Code | Relation | Meaning |
|---|---|---|
| C | `compatible` | The two typed claims are directly co-satisfiable in their already-declared matched scope. This does not assert identity or mutual implication. |
| CM | `conditional-on-common-carrier-or-map` | No conflict follows once an explicit common carrier, common lift, typed map, response map, or commutation contract is supplied; composition is not licensed without it. |
| OE | `orthogonal-estimand` | The modules estimate or constrain different typed objects, so their claims are not logical negations and no automatic composition is implied. |
| OB | `open-bridge` | No current contradiction is identified, but the scientifically useful cross-layer identification or composition remains unproved at the stated generality. |
| X | `actual-conflict` | The modules make jointly unsatisfiable claims after carrier, types, scope, and estimand have been matched. |

## Symmetric pairwise matrix

| | CREST | CCOC | MLTR | MRM | CED | RACH | EGC | EGW | TU-1 | TU-2 | TU-3 | TU-4 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **CREST** | -- | CM | CM | CM | OE | OE | OB | OB | C | OE | CM | CM |
| **CCOC** | CM | -- | CM | CM | OE | OE | OB | OB | CM | OE | OB | OE |
| **MLTR** | CM | CM | -- | CM | OE | OE | OB | OB | OB | OE | OB | OB |
| **MRM** | CM | CM | CM | -- | CM | CM | OB | OB | CM | OE | CM | OB |
| **CED** | OE | OE | OE | CM | -- | CM | OB | OB | OE | C | OE | OB |
| **RACH** | OE | OE | OE | CM | CM | -- | OB | OB | OE | C | OE | OE |
| **EGC** | OB | OB | OB | OB | OB | OB | -- | CM | OE | OE | CM | CM |
| **EGW** | OB | OB | OB | OB | OB | OB | CM | -- | OE | OE | CM | CM |
| **TU-1** | C | CM | OB | CM | OE | OE | OE | OE | -- | OE | C | C |
| **TU-2** | OE | OE | OE | OE | C | C | OE | OE | OE | -- | OE | OE |
| **TU-3** | CM | OB | OB | CM | OE | OE | CM | CM | C | OE | -- | C |
| **TU-4** | CM | OE | OB | OB | OB | OE | CM | CM | C | OE | C | -- |

## Pair ledger

| Pair | Typed relation | Audit rationale |
|---|---|---|
| CREST / CCOC | `conditional-on-common-carrier-or-map` | CCOC future obstruction can refine a CREST required state when both act on one declared carrier; absent that match it is not a contradiction. |
| CREST / MLTR | `conditional-on-common-carrier-or-map` | MLTR transport or repair contributes to a joint required state only through a declared common lift or typed replacement map. |
| CREST / MRM | `conditional-on-common-carrier-or-map` | MRM mechanism-response distinctions enter a CREST contract only after candidate mechanisms and responses are typed on a common carrier. |
| CREST / CED | `orthogonal-estimand` | CREST asks which distinctions are structurally required; CED asks which required distinctions or targets current evidence licenses. |
| CREST / RACH | `orthogonal-estimand` | A required-state quotient and an evidence-conditioned admissible causal set are different typed objects with different objectives. |
| CREST / EGC | `open-bridge` | A bounded two-world eco-genetic bridge exists, but no full simulator-domain equality between CompleteSimulatorState and CREST RequiredState is established. |
| CREST / EGW | `open-bridge` | Empirical warning coordinates do not yet identify a complete natural CREST state; the empirical warning-state bridge remains open. |
| CREST / TU-1 | `compatible` | CREST adequacy under C0 and TU-1 failure of later reuse under C1 are co-satisfiable; TU-1 is the exact same-carrier reuse specialization plus repair cost. |
| CREST / TU-2 | `orthogonal-estimand` | Exact structural adequacy and graded causal-learning or report-licensing utility answer different questions. |
| CREST / TU-3 | `conditional-on-common-carrier-or-map` | The TU-3 loss quotient agrees with loss-specialized CREST only when the full loss signature exhausts the CREST responsibilities on the same carrier. |
| CREST / TU-4 | `conditional-on-common-carrier-or-map` | TU-4 is a CREST-style joint responsibility once loss and warning responses are defined on the same declared model-world carrier. |
| CCOC / MLTR | `conditional-on-common-carrier-or-map` | Future and history obstructions can join without conflict on a common carrier or lift, but neither supplies the other's transport map. |
| CCOC / MRM | `conditional-on-common-carrier-or-map` | Future and mechanism closures are co-satisfiable joint responsibilities after their response domains are aligned. |
| CCOC / CED | `orthogonal-estimand` | A future-grammar obstruction is structural, whereas CED concerns evidence compatibility and reporting. |
| CCOC / RACH | `orthogonal-estimand` | Opening a future grammar and selecting an observation for causal learning have distinct estimands. |
| CCOC / EGC | `open-bridge` | Simulator futures could instantiate a CCOC grammar, but no general source-faithful grammar map from EGC is registered. |
| CCOC / EGW | `open-bridge` | Warning-domain futures and CCOC composition futures have no completed typed bridge at their current generality. |
| CCOC / TU-1 | `conditional-on-common-carrier-or-map` | A CCOC future opening can instantiate the C0-to-C1 revision in TU-1 only after old and revised states are placed on a common carrier. |
| CCOC / TU-2 | `orthogonal-estimand` | Future obstruction does not rank causal-learning observations or license a report target. |
| CCOC / TU-3 | `open-bridge` | Mapping a changed future grammar into a contract-complete loss-response signature is a plausible but unproved bridge. |
| CCOC / TU-4 | `orthogonal-estimand` | Future-interface obstruction and warning-versus-loss refinement can both hold without being the same claim. |
| MLTR / MRM | `conditional-on-common-carrier-or-map` | History transport and mechanism robustness can be jointly audited when replacement and mechanism maps share a carrier or common lift. |
| MLTR / CED | `orthogonal-estimand` | Declared historical meaning and evidence-qualified reportability are different estimands. |
| MLTR / RACH | `orthogonal-estimand` | History transport does not identify a causal programme, and causal admissibility does not supply an inherited semantic map. |
| MLTR / EGC | `open-bridge` | A simulator history could provide an MLTR carrier, but no general history/replacement projection from EGC is completed. |
| MLTR / EGW | `open-bridge` | Historical replacement and warning portability are related transport problems, but their cross-domain semantic bridge remains open. |
| MLTR / TU-1 | `open-bridge` | TU-1 is same-carrier revision; the carrier-changing revision needed to subsume MLTR transport is explicitly open. |
| MLTR / TU-2 | `orthogonal-estimand` | Semantic/history transport and experiment utility do not estimate the same object. |
| MLTR / TU-3 | `open-bridge` | TU-3 representation faithfulness is same-carrier, while MLTR may change carriers; a lift-invariant loss map is not proved. |
| MLTR / TU-4 | `open-bridge` | Connecting historical transport to warning portability requires a declared cross-state correspondence and commutation result not yet supplied. |
| MRM / CED | `conditional-on-common-carrier-or-map` | The positive bridge composes MRM response classes with CED licensing on finite shared bridge worlds; it does not create a canonical natural embedding. |
| MRM / RACH | `conditional-on-common-carrier-or-map` | The positive bridge maps RACH-admissible programmes to MRM response classes under one declared action/target carrier. |
| MRM / EGC | `open-bridge` | EGC mechanisms or state coordinates require an explicit schema map before they become an MRM candidate-law family. |
| MRM / EGW | `open-bridge` | No general map currently shows which eco-genetic warning differences are mechanism-relevant MRM response distinctions. |
| MRM / TU-1 | `conditional-on-common-carrier-or-map` | TU-1 can audit a changed mechanism responsibility only when old and revised MRM states share a carrier or typed lift. |
| MRM / TU-2 | `orthogonal-estimand` | Mechanism-safe response equivalence is neither causal-learning value nor target-licensing status. |
| MRM / TU-3 | `conditional-on-common-carrier-or-map` | MRM distinctions enter TU-3 only when retained mechanism responsibilities are included in the full loss-response signature. |
| MRM / TU-4 | `open-bridge` | A general mechanism-to-warning response bridge is not established even though both can coexist on a declared carrier. |
| CED / RACH | `conditional-on-common-carrier-or-map` | The finite positive bridge keeps causal multiplicity while licensing a target on shared evidence-compatible bridge worlds. |
| CED / EGC | `open-bridge` | Simulator output does not become reliability-qualified evidence about nature without an empirical observation and calibration bridge. |
| CED / EGW | `open-bridge` | The empirical warning programme requires an explicit CED reliability/reportability projection before generic evidence licensing follows. |
| CED / TU-1 | `orthogonal-estimand` | Reportability under current evidence and revisability after stored compression are different axes. |
| CED / TU-2 | `compatible` | TU-2 preserves CED target licensing as a distinct utility and proves that RACH learning need not rank it the same way. |
| CED / TU-3 | `orthogonal-estimand` | Evidence licensing and loss-representation factorization are independent unless an empirical bridge is added. |
| CED / TU-4 | `open-bridge` | Mathematical warning-state adequacy does not yet imply empirical identification or CED-licensed portability. |
| RACH / EGC | `open-bridge` | EGC-generated mechanisms can enter RACH only through a declared model-family and observation map not completed here. |
| RACH / EGW | `open-bridge` | Warning observations do not automatically define a RACH causal-programme family or NOV objective. |
| RACH / TU-1 | `orthogonal-estimand` | Causal-set learning and later state revision answer different scientific responsibilities. |
| RACH / TU-2 | `compatible` | TU-2 uses RACH causal-learning utility on its graded branch while explicitly preserving the separation from target licensing. |
| RACH / TU-3 | `orthogonal-estimand` | Causal-learning value and loss-representation faithfulness are distinct estimands. |
| RACH / TU-4 | `orthogonal-estimand` | Admissible causal uncertainty and warning/loss response refinement can vary independently. |
| EGC / EGW | `conditional-on-common-carrier-or-map` | EGW can condition on an EGC-derived frozen loss domain when simulator version, endpoints, and observation semantics are explicitly aligned. |
| EGC / TU-1 | `orthogonal-estimand` | Complete simulator-state sufficiency does not by itself answer revision after scientific compression. |
| EGC / TU-2 | `orthogonal-estimand` | Simulator dynamics do not identify a universal experiment ranking between causal learning and report licensing. |
| EGC / TU-3 | `conditional-on-common-carrier-or-map` | TU-3 audits an EGC representation only after the full loss-contract signature and projection are declared on the simulator carrier. |
| EGC / TU-4 | `conditional-on-common-carrier-or-map` | TU-4 can refine an EGC loss domain when loss and warning responses share the declared simulator carrier. |
| EGW / TU-1 | `orthogonal-estimand` | Warning reproducibility or portability does not determine revision debt after an old state was stored. |
| EGW / TU-2 | `orthogonal-estimand` | Warning performance and causal-learning versus report-licensing utility are distinct outcomes. |
| EGW / TU-3 | `conditional-on-common-carrier-or-map` | EGW's warning-blind loss domain corresponds to TU-3 only through a full loss-response and representation map. |
| EGW / TU-4 | `conditional-on-common-carrier-or-map` | TU-4 formalizes EGW's within-state/portability distinction, but empirical application still requires matched loss, warning, and domain semantics. |
| TU-1 / TU-2 | `orthogonal-estimand` | Revision debt and graded learning/licensing utility are separate additions to the common task-indexed spine. |
| TU-1 / TU-3 | `compatible` | Both are exact specializations of representation adequacy: one changes the task after storage and the other changes the representation for a fixed loss task. |
| TU-1 / TU-4 | `compatible` | Reuse after contract change and warning-task refinement are co-satisfiable exact specializations of the task preorder. |
| TU-2 / TU-3 | `orthogonal-estimand` | TU-2's graded epistemic utility is deliberately a separate branch from TU-3 exact representation adequacy. |
| TU-2 / TU-4 | `orthogonal-estimand` | Graded causal/report utility and exact loss/warning task refinement are not the same ordering. |
| TU-3 / TU-4 | `compatible` | TU-3 supplies the contract-complete loss quotient that TU-4 jointly refines with the warning response. |

## Claim ceiling

`actual-conflict = 0` means that no pair is jointly unsatisfiable after respecting its registered types and current scope. `conditional-on-common-carrier-or-map` and `open-bridge` are not silently upgraded to completed compositions. Pairwise closure also does not establish three-way or global consistency.

Regenerate with `python theory/build_contradiction_certificate.py` and validate with `python theory/validate_contradiction_matrix.py`.
