<!-- draft-id: chapter:2:v0.2 -->
# Chapter 2 — When Closed Simplicity Fails under Open Futures

> **Draft status:** dissertation-adapted v0.2. The theorem, proof, bounded-local witness, figures, code, and manuscript remain owned by `zuizui0223/ccoc`.

## 1. From a capability gap to a grammar gap

Chapter 1 showed that a fixed small expansion of conservation capability can coexist with an arbitrarily large increase in the state and monitoring resolution required for a retained present slice. That result compares several quantities inside one management architecture: growth of the robustly controllable carrier, growth of the least adequate state, evidence debt, and target reportability.

This chapter asks a related but more structural question. Suppose a controlled ecological system can be studied under several restricted futures. In each restricted context, the exact response relevant to the focal task admits a small state interface. Can those individually successful compressions be combined into one comparably small interface when the future interaction grammar is opened?

The answer is no in general.

\[
\boxed{
\text{small exact interfaces under closed futures}
\not\Rightarrow
\text{one comparably small exact interface under an open future grammar}.
}
\]

The distinction is not that an open system has more states merely because more events are imaginable. The physical controlled plant is held fixed. What changes is the legal family of future action words that the representation is required to answer. A latent difference that never affects the focal response under one closed grammar can be safely omitted there. If a larger grammar later contains a concrete future word that exposes the difference, the old merge is no longer exact for the enlarged responsibility.

The central quantity is therefore not the number of current variables or the complexity of the local update rule. It is the amount of state information made **operationally addressable** by the declared future grammar.

This chapter develops three results. First, independently addressable exterior coordinates imply a cross-grammar lower bound on exact interface memory. Second, an explicit one-action family changes the exact quotient from two classes to a discrete quotient on \(2^{m+1}\) states, achieving the maximum possible \(m\)-bit increase on the comparison domain. Third, the same gap can be realized with a fixed action alphabet, bounded local alphabets, radius-one dynamics, maximum degree three, a one-edge focal/exterior cut, and logarithmic access. A complementary positive theorem identifies when a macro-law does remain portable as the grammar expands.

## 2. Closed-context functional equivalence and open-future causal equivalence

Ecological models routinely merge configurations that are functionally indistinguishable under the interactions currently represented. A set of source patches may be inaccessible, an interaction partner absent, a dispersal branch closed, or a reservoir unable to influence a focal system. Differences inside those unavailable components can be irrelevant to every trajectory admitted by the current model. Ignoring them is not an approximation if no legal future can make them affect the focal response.

The difficulty appears when the future contract changes. A corridor may reopen. A colonist may arrive. A source population may become reachable. A pathogen, predator, mutualist, or delayed reservoir may gain a legal interaction path. Rewiring can make a previously dormant component addressable without changing every present focal variable at the instant the connection becomes available.

CCOC formalizes this distinction as a change in legal future grammar rather than as an automatic change in the controlled plant. “Open” is used in this narrow sense: the open grammar admits future action sequences that are not legal in the closed comparison grammars. It does not mean that the model contains every possible ecological event or that real ecosystems are literally finite automata.

Two configurations can therefore be:

- equivalent under every future legal in one closed context;
- equivalent under every future legal in another closed context;
- distinguishable when a jointly open grammar allows the dormant contexts to be selectively queried.

The earlier closed interfaces are not wrong. Each is exact for its own future contract. The failure occurs when their success is transported to a larger grammar without checking whether the new futures preserve the old equivalence classes.

## 3. Exact response interface for a declared future grammar

Let

\[
\mathcal M=(S,A,T,h)
\]

be a finite deterministic controlled system. Here \(S\) is the finite raw state space, \(A\) the primitive action alphabet, \(T\) the transition rule, and \(h:S\to Y\) the focal output.

A legal future grammar

\[
\mathcal L\subseteq A^*
\]

specifies which finite action words count as admissible futures for the scientific task. For a state \(s\) and legal word \(w\), let

\[
\operatorname{Tr}(s,w)
\]

be the focal output trace produced by executing \(w\), including the current output and the subsequent outputs.

Two raw states are exactly response-equivalent under \(\mathcal L\) when no legal future distinguishes them:

\[
\boxed{
s\equiv_{\mathcal L}s'
\iff
\forall w\in\mathcal L,
\operatorname{Tr}(s,w)=\operatorname{Tr}(s',w).
}
\]

The quotient

\[
Q_{\mathcal L}=S/\!\equiv_{\mathcal L}
\]

is the coarsest exact deterministic response interface for that future contract, with exact interface memory

\[
K_{\mathcal L}=\log_2|Q_{\mathcal L}|.
\]

This continuation-based equivalence is classical finite-state substrate. Context-dependent minimization, incomplete specifications, and environment-dependent reduction have long histories. The chapter's claim does not rest on inventing exact response equivalence.

Grammar enlargement is monotone. If

\[
\mathcal L_1\subseteq\mathcal L_2,
\]

then any pair indistinguishable under the larger grammar is also indistinguishable under the smaller one. Hence

\[
\equiv_{\mathcal L_2}
\subseteq
\equiv_{\mathcal L_1}
\]

and

\[
K_{\mathcal L_1}\le K_{\mathcal L_2}.
\]

The monotonicity is immediate. The substantive question is quantitative: how large can the increase become when every restricted context admits strong exact compression and the underlying local implementation remains uniformly simple?

## 4. Cross-grammar addressability lower bound

Consider a reachable comparison subsystem with product form

\[
S^*\cong I\times E_1\times\cdots\times E_q.
\]

The coordinate \(I\) represents a focal or inside state. Each \(E_j\) represents an exterior coordinate: for example, a dormant source, an inaccessible interaction branch, or the state of a module that can become connected in one future context.

### 4.1 Operational addressability

An exterior coordinate is operationally addressable under the open grammar when a concrete legal future word can recover that coordinate from the focal response. Suppose a legal word \(r_0\) decodes the inside coordinate and, for every \(j\), a legal open word \(r_j\) with decoder \(d_j\) satisfies

\[
d_j\!\left(
\operatorname{Tr}((i,e_1,\ldots,e_q),r_j)
\right)=e_j
\]

for every jointly realizable comparison state.

The requirement is stronger than saying that the exterior variable exists in the raw state. It demands a legal counterfactual experiment that exposes it at the focal output. The decoder for coordinate \(j\) must work independently of the other exterior coordinates.

### 4.2 The lower bound

Take two distinct states in \(S^*\). If their inside coordinates differ, \(r_0\) separates them. Otherwise some exterior coordinate differs, and its decoder word separates them. Every distinct pair therefore lies in different open response classes. The exact open quotient is discrete on the comparison subsystem, so

\[
\boxed{
K_{\mathrm{open}}
\ge
\log_2|I|
+
\sum_{j=1}^{q}\log_2|E_j|.
}
\]

Now suppose closed context \(j\) exposes only \((I,E_j)\): every response legal in that context factors through the projection

\[
(i,e_1,\ldots,e_q)
\mapsto
(i,e_j).
\]

Then

\[
K_{\mathrm{closed},j}
\le
\log_2|I|
+
\log_2|E_j|.
\]

Subtracting the largest closed requirement yields

\[
\boxed{
K_{\mathrm{open}}
-
\max_jK_{\mathrm{closed},j}
\ge
\sum_j\log_2|E_j|
-
\max_j\log_2|E_j|.
}
\]

The proof is an operational injection, not an assumption that every raw coordinate contributes additive memory. Each term in the lower bound is backed by a legal future word that can expose the corresponding distinction.

### 4.3 Constrained codebooks

The full Cartesian product is not essential. Let \(C\) be any finite jointly realizable codebook inside the comparison domain. If the open future family separates every pair in \(C\), then the open quotient is discrete on \(C\):

\[
|Q_{\mathrm{open}}|\ge |C|.
\]

If closed context \(j\) factors through a smaller projection \(\pi_j(C)\), then

\[
K_{\mathrm{open}}
-
\max_jK_{\mathrm{closed},j}
\ge
\log_2|C|
-
\max_j\log_2|\pi_j(C)|.
\]

This strengthening matters because ecological configurations are often constrained. Exterior possibilities need not occur in every formal combination. A large gap persists whenever the realizable configurations remain pairwise addressable by legal open futures while each closed projection remains small.

The codebook result is support for the main mechanism, not a second headline theorem.

## 5. A maximal one-action family

The general lower bound explains why addressability forces memory. The next construction shows that the gap can be maximal even when the grammar edit is minimal.

For every integer \(m\ge1\), define comparison states

\[
D_m=\{0,1\}^{m+1}
=
\{(y,b_1,\ldots,b_m)\}.
\]

The focal bit \(y\) is immediately visible. The \(m\) bits \(b_j\) are dormant exterior memories. The primitive action alphabet is fixed for every \(m\):

\[
A=\{0,1,\mathsf{fire},\mathsf{tick}\}.
\]

The physical transition system is identical in the closed and open comparisons. Only legal action grammar changes.

### 5.1 Closed grammar

The closed grammar is

\[
L_C=\{0,1,\mathsf{tick}\}^{*}.
\]

Address actions may move a selector, and `tick` may update local relay states, but no dormant memory leaf can emit its bit. Every focal trace therefore depends only on \(y\). The exact closed response quotient has

\[
\boxed{
|P_C|=2,
\qquad
K_C=1.
}
\]

### 5.2 Open grammar

The open grammar is

\[
L_O=A^*.
\]

Opening legalizes one primitive action: `fire`. The address symbols and propagation symbol were already legal.

Let leaf \(j\) have binary address \(a_j\) and depth \(d_j\) in a relay tree. The legal word

\[
w_j
=a_j\,\mathsf{fire}\,\mathsf{tick}^{d_j+1}
\]

selects that leaf, emits its stored bit, and propagates the pulse to the focal output. Thus

\[
\operatorname{finaloutput}(s,w_j)=b_j.
\]

Distinct focal bits are separated immediately. States with equal focal bit but different exterior memory are separated by the query word for a differing coordinate. Therefore the open quotient is discrete:

\[
\boxed{
|P_O|=2^{m+1},
\qquad
K_O=m+1.
}
\]

The exact interface increase is

\[
\boxed{
K_O-K_C=m.
}
\]

A two-class quotient on a domain of size \(2^{m+1}\) can gain at most \(m\) bits before becoming discrete. The family therefore reaches the absolute finite-domain maximum.

The gap is not produced by adding one primitive action per dormant variable. The alphabet remains four symbols and the closed/open grammar descriptions remain constant size. What scales is the amount of dormant state that the now-legal addressing protocol can reach.

## 6. Local simplicity does not bound open-interface memory

A centralized lookup table could trivially store and reveal \(m\) bits. That construction would leave the possibility that the response gap is simply a disguised increase in local rule complexity. The fixed-regular relay removes that explanation.

### 6.1 Bounded-local realization

Dormant memory sites are leaves of a balanced binary tree. Address symbols move a selector down the tree through radius-one local updates. `fire` emits a pulse only from the selected leaf. `tick` propagates that pulse back toward the root. Internal relays use fixed local state and message alphabets.

For all \(m\):

- the primitive action alphabet has four symbols;
- the interaction graph is a tree;
- maximum degree is at most three;
- the focal node is separated from the exterior relay body by one edge;
- node and message alphabets are bounded independently of \(m\);
- updates are pairwise and radius one.

Yet the open response interface contains \(2^{m+1}\) exact classes.

Consequently, bounded degree, tree topology, bounded local alphabets, a one-edge focal/exterior cut, and a one-transition grammar edit do not by themselves bound exact open response memory.

This is a property of the constructed finite family. It is not a claim that a narrow ecological corridor or sparse interaction network automatically contains the same hidden information structure.

### 6.2 Access length

In a balanced tree the deepest memory leaf has depth

\[
H(m)=\lceil\log_2m\rceil.
\]

A canonical query requires \(d_j\) address actions, one `fire`, and \(d_j+1\) propagation ticks. The worst query length is therefore

\[
\boxed{
L_{\mathrm{query}}^{\mathrm{worst}}
=2\lceil\log_2m\rceil+2.
}
\]

The horizon grows only logarithmically even though the exact response class count is exponential in \(m\). A separate causal-cone argument gives a logarithmic lower-order requirement under a broad bounded-local contract, so the relay has order-optimal access scaling, although the exact constant is construction-specific.

### 6.3 Historical boundary

The relay is used as a constrained extremal witness, not as a historical-firstness claim for modular finite-state synthesis. Contextual minimization, incomplete specifications, composition-aware reduction, and state-reduction/realization noncommutation have classical ancestry. The chapter's scientific burden is narrower: the maximal closed/open response gap is compatible with uniformly bounded local implementation and one newly legal primitive action.

## 7. When compression does travel

The negative theorem does not imply that every enlarged future grammar destroys a macro-law. A positive sufficient condition identifies when the old interface remains portable.

Consider nested finite stages that all project to one finite macrostate set \(Q\). Suppose:

1. macro outputs have the same meaning at every stage;
2. legal actions have consistent macro semantics;
3. macro successors are uniform inside each macro fiber;
4. embeddings preserve the macro labels of old states.

Then every stage realizes the same exact macro dynamics, and the compatible restrictions define one portable macro-law across the nested chain.

Schematically,

\[
\boxed{
\text{common finite macro dynamics}
+
\text{trajectory-preserving embeddings}
+
\text{label coherence}
\Rightarrow
\text{portable macro-law}.
}
\]

Equal label counts are not sufficient. Three labels at every stage do not define one portable law if their outputs or transition meanings change.

The local obstruction is equally direct. If two states occupy one proposed macro fiber but a newly legal future word yields different required traces from their embedded images, the merge cannot remain exact. The word is an explicit witness of non-portability.

The positive and negative results meet at one boundary: opening the future is harmless when every new response continues to factor through the old macro semantics. It forces refinement when a newly legal word exposes a distinction hidden inside an old fiber.

## 8. Ecological interpretation

### 8.1 Dormant difference versus current function

The exterior coordinates can represent differences that are presently silent: states of inaccessible source populations, delayed mutualists, pathogen reservoirs, closed dispersal branches, or neighbouring communities whose influence is blocked. Under a restricted future, an exact model may legitimately omit them. Under an enlarged future, they become state-defining only if a legal response can expose them.

The result therefore does not advocate retaining all latent ecological detail. It supplies a criterion for when omission ceases to be exact.

### 8.2 Colonization, reconnection, and rewiring

Colonization can be more than a current-state update. It can open a new family of future interactions. Corridor restoration can expose source-specific dispersal responses. Reconnection can make different exterior population states relevant. Rewiring can allow a dormant interaction branch to affect focal function.

In each case the empirical burden is to justify the future grammar and the response map. CCOC does not infer them from observations. Once they are declared, the theorem identifies a possible reason that a previously adequate interface fails: future addressability, not necessarily local dynamical complexity, forces the missing distinctions.

### 8.3 Functional redundancy is future-contract-relative

Two configurations can be functionally redundant under every currently legal trajectory and non-redundant under an open future. This is not semantic wordplay. It means that the equivalence relation used by the functional category is indexed by the future operations the category must support.

Functional groups and coarse variables remain legitimate when new behaviour is uniform inside their classes. The positive portability theorem gives precisely that countercase. The diagnostic requirement is to test whether the enlarged future still factors through the old macrostate.

### 8.4 Difference from the conservation-capacity theorem

Chapter 1 and Chapter 2 share a motif but not a theorem.

CREST asks how a change in management capability affects the size of a robust carrier, the least state required on a present slice, evidence debt, and target reportability. Its no-bound result fixes the carrier gain at one while state and monitoring debt grow by \(m\) bits.

CCOC asks whether exact interfaces optimized for closed future grammars can be combined into one small exact interface when those futures are opened. Its main gap compares

\[
K_{\mathrm{open}}
\quad\text{with}\quad
\max_jK_{\mathrm{closed},j}.
\]

The open-grammar theorem explains a structural mechanism by which latent differences become response-relevant, but it neither computes CREST's carrier gain nor owns its evidence and target gates.

## 9. Relation to classical minimization and composition

The exact response quotient belongs to continuation-based state equivalence. Enlarging a legal test family refines that quotient by elementary logic. Incompletely specified sequential-machine minimization already showed that restricted specifications change which state distinctions must be retained (Paull and Unger 1959). Interacting-machine work made environment-imposed input restrictions explicit (Wang and Brayton 1993; Aziz et al. 1993; Watanabe and Brayton 1993). Hartmanis and Stearns (1962) showed that state reduction and machine realization can fail to commute.

CCOC therefore does not claim that environmental context can affect compression, that generic composition and reduction fail to commute, or that pair separation yields a new counting principle.

The defensible chapter-level contribution is the explicit quantitative package:

\[
|P_C|=2,
\qquad
|P_O|=2^{m+1},
\qquad
K_O-K_C=m,
\]

with one newly legal primitive action and a bounded-local realization satisfying fixed alphabet, bounded local states/messages, radius-one updates, maximum degree three, one-edge focal/exterior cut, and logarithmic causal access. The relay is a direct sharpness witness even if related modular synthesis techniques have classical ancestry.

This framing turns the prior-art firewall into a positive contribution statement rather than a catalogue of concessions. The novelty is not that context matters. It is the exact closed-to-open response gap under the declared fixed-plant contract and its simultaneous extremal structural constraints.

## 10. Limits and transition

The headline theory is finite, deterministic, exact, and contract-relative. It does not identify the correct future grammar from field data, estimate the frequency of extremal gaps in ecosystems, or supply a complete stochastic or approximate portability theory. The approximate-addressability extension shows only that bounded decoding error need not collapse the memory requirement immediately; it is not a general rate-distortion result.

Interface memory is also one notion of ecological complexity. The theorem separates it from several local and static structural quantities in one family. It does not imply that degree, cut width, energy, stability, sampling effort, or persistence are irrelevant to other ecological questions.

The chapter has held one controlled plant fixed while changing its legal futures. The next chapter changes the problem. Species turnover, extinction, recolonization, or rewiring can replace the system itself, perhaps with a non-nested target state space. Then the question is no longer only whether the exact minimum interface grows under a new grammar. It is whether an inherited macro-law retains its meaning across replacement and, if not, what source-relative repair is minimally necessary. Chapter 3 develops that transport problem.

## References

Aziz A, Singhal V, Swamy GM, Brayton RK (1993) *Minimizing Interacting Finite State Machines*. UCB/ERL M93/68, University of California, Berkeley.

Hartmanis J, Stearns RE (1962) Some dangers in state reduction of sequential machines. *Information and Control* 5:252–260. https://doi.org/10.1016/S0019-9958(62)90588-0

Paull MC, Unger SH (1959) Minimizing the number of states in incompletely specified sequential switching functions. *IRE Transactions on Electronic Computers* EC-8:356–367. https://doi.org/10.1109/TEC.1959.5222697

Wang H-Y, Brayton RK (1993) *Input Don't Care Sequences in FSM Networks*. UCB/ERL M93/64, University of California, Berkeley.

Watanabe Y, Brayton RK (1993) *The Maximum Set of Permissible Behaviors for FSM Networks*. UCB/ERL M93/61, University of California, Berkeley.
