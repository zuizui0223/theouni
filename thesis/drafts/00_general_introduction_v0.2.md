<!-- draft-id: chapter:introduction:v0.2 -->
# General Introduction — The Reuse Problem in Ecology

> **Draft status:** citation-audited v0.2. Source-owned results are introduced only to define the dissertation problem and are developed in their owning chapters.

## 1. Ecology is built from representations that are reused

Ecological systems contain more detail than any scientific description can retain. Researchers therefore work with representations that compress. Lakes are described as clear or turbid, populations as viable or declining, landscapes as connected or fragmented, and communities as functionally intact or impaired. Reduced models replace large dynamical systems with a few variables. Monitoring programmes use indicators rather than complete system descriptions. Management rules map measured conditions to actions. Early-warning studies ask whether a small set of signals can anticipate a transition. Such representations are useful precisely because they treat many physically different systems as equivalent for a specified scientific purpose.

The philosophy of science has long emphasized that model evaluation is purpose-relative rather than governed by one context-free measure of fidelity (Odenbaugh 2005, 2019; Potochnik 2015, 2017, 2020; Parker 2020; Bokulich and Parker 2021). Abstraction and idealization allow heterogeneous lower-level systems to support higher-level regularities, while multiple realization raises the complementary question of which micro-level differences are irrelevant to a macro-description (Batterman 2000; Wimsatt 2007). Ecology has its own versions of this problem. State-and-Transition Models make ecological classifications explicitly relevant to management (Stringham et al. 2003); conservation POMDPs ask which states matter for decisions (Nicol and Chadès 2012; Chadès et al. 2021); ecological model-adequacy frameworks scrutinize variables, controls, and intended uses (Getz et al. 2018); and model transferability under novel conditions remains a recognized challenge (Yates et al. 2018).

This dissertation accepts that representations are selective and purpose-relative. Its central problem begins one step later. A state, law, measurement, causal interpretation, or warning is often reused beyond the task or domain for which it was first built. A present-status category is later asked to choose among interventions. A macro-law is carried through species turnover. A visible state is treated as mechanism-independent. An observation chosen to distinguish explanations is assumed to resolve a management target. A signal that leads loss in one calibrated domain is exported as a warning in another. In each case, the representation may have been adequate for its original purpose. The scientific question is whether that success travels.

The dissertation therefore asks:

> **When may a scientific representation built for one ecological responsibility be reused for another?**

This is the **reuse problem in ecology**. It is related to model transfer, abstraction, and adequacy-for-purpose, but its object is specifically the movement of a retained representation across a change in scientific responsibility. The changed element may be the management repertoire, the legal future grammar, the ecological system, the mechanism family, the evidence architecture, the report target, the raw model representation, the loss process, or the warning domain. Reuse can fail even when the original model or measurement was internally correct.

## 2. A minimal criterion for adequacy and reuse

Let \(\Omega\) be a declared universe of model worlds. A scientific task \(\alpha\) is represented by a contract-complete response signature

\[
\Sigma_\alpha:\Omega\to Y_\alpha,
\]

where \(\Sigma_\alpha\) contains the responses that the representation must preserve for that task. Depending on the chapter, these may include intervention-indexed futures, inherited macro-meanings, mechanism-specific responses, a report target, a loss trajectory, or a warning relation. A retained representation is a map

\[
R:\Omega\to Z.
\]

The minimal common criterion is

\[
\boxed{
R\models\alpha
\iff
\exists f:Z\to Y_\alpha
\text{ such that }
\Sigma_\alpha=f\circ R.
}
\]

A representation is adequate for \(\alpha\) when the task-complete response can be reconstructed from what the representation retains. Equivalently, it does not merge two model worlds that task \(\alpha\) requires to yield different answers. The canonical task state is the quotient induced by equality of \(\Sigma_\alpha\).

Reuse is a second question. Suppose a representation was retained for task \(\alpha\), and a later task \(\beta\) is introduced. Reuse is licensed only if the \(\beta\)-response also factors through what was retained. If the stored representation is the canonical \(\alpha\)-state \(q_\alpha\), then reuse requires

\[
\boxed{
\Sigma_\beta=h\circ q_\alpha
}
\]

for some \(h\). A representation can therefore be adequate for \(\alpha\) and inadequate for \(\beta\) without contradiction. The old result answered one question; the new task demands distinctions that the old representation may have merged.

The factorization and quotient mathematics is classical substrate. This dissertation does not claim novelty for purpose relativity, partition refinement, or fixed-task sufficiency. The formal language is valuable because it lets distinct ecological programmes state exactly where reuse fails, where it succeeds, and what repair or additional evidence is required. The scientific novelty remains in the source-owned theorems, constructions, algorithms, and empirical results developed in Chapters 1–8.

Task relativity does not imply conventionalism. Scientists may choose which prediction or decision matters, but they cannot choose the ecological response. A task is scientifically meaningful only if its responsibility is specified independently of the preferred representation, its domain is non-vacuous, and a proposed merge can fail when merged worlds disagree on a required response. The task selects which difference matters; dynamics and evidence determine whether that difference exists and whether it is identifiable.

## 3. Five kinds of change that can break reuse

The chapters can be grouped by what changes between the original and later scientific responsibility.

### 3.1 What can happen or be done changes

A management repertoire can expand, or a previously closed future grammar can be opened. New actions need not change the physical ecosystem before they are applied, yet they can make previously irrelevant differences management-relevant. Chapter 1 develops the conservation-capacity result: a fixed small gain in capability need not bound the increase in required state or monitoring resolution. Chapter 2 studies the related but distinct cross-grammar problem: interfaces that are small under separately optimized closed futures need not remain small when those futures are opened jointly.

These chapters forbid two tempting scale arguments. A small intervention gain does not guarantee a small epistemic burden, and simple interfaces under every closed context do not guarantee a simple interface under open composition.

### 3.2 The system or its mechanistic interpretation changes

An ecological system may undergo turnover, extinction, recolonization, habitat reconfiguration, or interaction rewiring. Chapter 3 asks whether a macro-law with inherited source meaning can travel through that replacement. When it cannot, the response is not an unrelated target aggregation but a source-relative repair that preserves every inherited merge still valid.

Alternatively, the visible system may remain the same while multiple mechanisms remain admissible. Chapter 4 asks when those mechanisms support a common law. Mechanistic differences are not automatically state-relevant; they become relevant exactly where retained response types disagree on a future required by the task.

### 3.3 What is observed or valued as information changes

Knowing which distinctions a task requires does not imply that an experiment has identified them. Chapter 5 distinguishes evidence-compatible world classes, target-safe resolution requirements, observation failure architecture, and licensed reporting. More data can resolve target-irrelevant detail, and repetition within one shared failure domain need not earn the same guarantee as independent observation modes.

Chapter 6 then separates two kinds of epistemic value. RACH asks which causal programmes remain admissible and which observation would reduce causal ambiguity. Target licensing asks whether the evidence supports the requested decision or report. TU-2 shows that these objectives can vary independently and can rank observations differently. Learning more about explanation is not the same achievement as earning a decision.

### 3.4 The dynamic target changes from system evolution to loss and warning

A complete simulator state may be sufficient for its declared Markov dynamics without being minimal for a particular ecological loss target. Conversely, familiar demographic, functional, and genetic marginals may be too coarse when their spatial alignment changes the next transition. Chapter 7 uses the eco-genetic programme to identify this representation boundary and specializes adequacy to a contract-complete loss response.

Warning adds another responsibility. Chapter 8 begins only after the loss domain has been fixed without inspecting warning outcomes. It then asks whether a signal discriminates impending loss and whether that relation transports. A signal can precede every observed loss and still fail as a warning if it also fires in every non-event. The warning-evaluation state may therefore be finer than the loss-generating state.

### 3.5 The task changes after compression has already been stored

The previous changes concern what a representation would need to preserve while model worlds remain conceptually available. The General Synthesis asks a time-indexed question: what if science retained only the old state label and discarded the distinctions within its classes? TU-1 tests whether a revised state factors through the stored one. If it does not, the missing distinction cannot be recreated by post-processing the old label alone. This is revision after scientific compression, not physical irreversibility in nature.

## 4. Invariants across the dissertation

The scientific objects differ by chapter, but seven rules are held fixed.

1. **Ecological reality is not a ModelWorld universe.** A valid theorem on declared model worlds is not automatically a theorem about nature.
2. **State is task-indexed.** No repository-local state becomes an intrinsic state of nature merely by being useful in one model or domain.
3. **Merging is safe only while required responses are preserved.** Reuse requires an explicit factorization through what was retained.
4. **Evidence does not create structural distinctions.** It identifies, fails to identify, or licenses reports about distinctions specified by a task.
5. **Required state, identified state, and reportable target are not interchangeable.** Full state can remain unresolved while a coarser target is answerable, or the target itself may remain ambiguous.
6. **No bridge is not a contradiction.** Two worldlines may be mutually consistent even when no valid transport map between them has been established.
7. **Validity here does not imply portability elsewhere.** Cross-worldline movement requires an appropriate common carrier, faithful lift, replacement relation, evidence projection, causal-response map, or portability correspondence.

These invariants provide unity without turning all chapters into one theorem. The Theory Universe is not a licence to explain every failure by assigning it to a different perspective. Each chapter must provide a positive adequacy condition, a minimal repair, a quantitative impossibility result, an executable method, or an empirical falsification. Otherwise task-indexed separation would create coherence only by insulation.

## 5. Reality, model worlds, and legitimate endings

A representation can be adequate within a declared model and still fail to represent the empirical system. Every application therefore requires a Reality-to-Theory admission bridge: a declared empirical unit and temporal or cohort scale, observed and unobserved coordinates, candidate model-world support, task and target, observation and reliability model, validation unit, and bounded claim. Without that bridge, the formal results remain conditional statements about model worlds.

Failure to transport also does not imply that the original representation was false. A state may remain adequate for status reporting but fail for a new intervention. A source macro-law may be exact before replacement. A measurement may be excellent for causal learning but irrelevant to a target. A genetic trajectory may be reproducibly early while lacking discrimination. The relevant question is what responsibility the old representation had earned and whether the new one factors through it.

Scientific worldlines can therefore end in several legitimate ways. A task can be resolved. The full state can remain unknown while a target is licensed. Honest ambiguity can be the sharp result. A result can be valid within one domain but non-portable elsewhere. A worldline can remain open because a bridge or empirical adequacy condition is missing. These endings should not be conflated with logical contradiction, carrier collapse, an ill-posed task, or a Reality-to-Model failure.

## 6. Dissertation claim and boundary

The common object of this dissertation is not one privileged ecological state. It is the set of conditions governing whether a scientific representation can travel from one ecological responsibility to another.

The dissertation makes three programme-level claims.

First, successful representation is directional. A representation may answer a weaker task while failing for a stronger or incomparable task. Fineness, sufficiency, and information value do not automatically transfer across responsibilities.

Second, non-transport has several scientifically different causes. The relevant obstruction may lie in future addressability, inherited meaning, mechanism disagreement, evidence reliability, causal estimand, loss-state representation, warning discrimination, or information already discarded by an earlier compression. Treating all of these as generic “state uncertainty” would erase the results that make the chapters independently valuable.

Third, bridge conditions are scientific results rather than administrative metadata. A claim crosses worldlines only after the relevant factorization, lift, replacement map, evidence link, or portability correspondence has been established. The absence of such a bridge is not evidence of contradiction, but neither is it permission to transport the claim.

The dissertation does **not** claim a new generic theory of quotient construction, a universal natural state, global consistency of all modules on one carrier, or empirical adequacy of every theoretical state. Source theorem and evidence ownership remains with the research programmes developed in their respective chapters.

## 7. Roadmap

Part I asks when doing more requires knowing more. Chapter 1 develops the conservation-capacity paradox and the capability–resolution no-bound result. Chapter 2 isolates the cross-grammar failure of closed compression under open futures.

Part II asks when scientific laws fail to travel. Chapter 3 studies inherited macro-law transport and minimal repair after ecological replacement. Chapter 4 studies deterministic law under retained mechanism uncertainty.

Part III asks why more information need not give the needed answer. Chapter 5 separates target-relative resolution from evidence and failure architecture. Chapter 6 develops causal-set learning and next-observation selection while separating learning from decision licensing.

Part IV moves into an explicit eco-genetic dynamic system. Chapter 7 asks which representation generates the declared functional-loss process. Chapter 8 shows how temporal precedence can reproduce while warning discrimination fails, and why portability is a separate test.

The General Synthesis returns to representations after they have been stored. It asks whether an old compression remains revisable when the scientific task changes and reconstructs the chapters as a typed universe of transport, non-transport, and repair. The chosen chapter sequence exposes the strongest prohibitions first, but it is one traversal of a non-linear dependency structure rather than the identity of the theory.

## References

Batterman RW (2000) Multiple realizability and universality. *British Journal for the Philosophy of Science* 51:115–145. https://doi.org/10.1093/bjps/51.1.115

Bokulich A, Parker W (2021) Data models, representation and adequacy-for-purpose. *European Journal for Philosophy of Science* 11:31. https://doi.org/10.1007/s13194-020-00345-2

Chadès I, Pascal LV, Nicol S, Fletcher CS, Ferrer-Mestres J (2021) A primer on partially observable Markov decision processes (POMDPs). *Methods in Ecology and Evolution* 12:2058–2072. https://doi.org/10.1111/2041-210X.13692

Getz WM, Marshall CR, Carlson CJ, Giuggioli L, Ryan SJ, Romañach SS, Boettiger C, Chamberlain SD, Larsen L, D'Odorico P, O'Sullivan D (2018) Making ecological models adequate. *Ecology Letters* 21:153–166. https://doi.org/10.1111/ele.12893

Nicol S, Chadès I (2012) Which states matter? An application of an intelligent discretization method to solve a continuous POMDP in conservation biology. *PLoS ONE* 7:e28993. https://doi.org/10.1371/journal.pone.0028993

Odenbaugh J (2005) Idealized, inaccurate but successful: a pragmatic approach to evaluating models in theoretical ecology. *Biology & Philosophy* 20:231–255. https://doi.org/10.1007/s10539-004-0478-6

Odenbaugh J (2019) *Ecological Models*. Cambridge University Press, Cambridge. https://doi.org/10.1017/9781108685283

Parker WS (2020) Model evaluation: an adequacy-for-purpose view. *Philosophy of Science* 87:457–477. https://doi.org/10.1086/708691

Potochnik A (2015) The diverse aims of science. *Studies in History and Philosophy of Science Part A* 53:71–80. https://doi.org/10.1016/j.shpsa.2015.05.008

Potochnik A (2017) *Idealization and the Aims of Science*. University of Chicago Press, Chicago.

Potochnik A (2020) Idealization and many aims. *Philosophy of Science* 87:933–943. https://doi.org/10.1086/710622

Stringham TK, Krueger WC, Shaver PL (2003) State and transition modeling: an ecological process approach. *Journal of Range Management* 56:106–113. https://doi.org/10.2307/4003893

Wimsatt WC (2007) *Re-Engineering Philosophy for Limited Beings: Piecewise Approximations to Reality*. Harvard University Press, Cambridge, MA.

Yates KL, Bouchet PJ, Caley MJ, Mengersen K, Randin CF, Parnell S, Fielding AH, Bamford AJ, Ban S, Barbosa AM et al (2018) Outstanding challenges in the transferability of ecological models. *Trends in Ecology & Evolution* 33:790–802. https://doi.org/10.1016/j.tree.2018.08.001
