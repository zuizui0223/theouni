# TU-1 — Contract revision, irreversible forgetting, and revision debt

> **Status:** finite exact theorem module. The factorization and finite coding substrate are elementary / closely related to classical quotient and zero-error side-information ideas; no standalone mathematical novelty claim is made yet. The programme-level contribution sought here is the ecological interpretation of **scientific forgetting under contract revision** and its separation from CREST's existing common-lift joint-state theorem.

## 1. Why TU-1 is not CREST-J1 again

CREST-J1 already proves the following on one declared finite common lift:

- Future, History, Mechanism, and Evidence/Target audits may be represented by monotone inflationary idempotent refinement closures.
- Their least common fixed point is unique.
- Pairwise commutation is unnecessary.
- Any fair repeated audit schedule converges to the same least-information joint state.

Therefore TU-1 does **not** claim that closure-operator joins commute, nor that audit order independence is new.

TU-1 asks a different question:

> **After a scientific contract has already compressed the world into a state, can a later contract be satisfied using only that stored state label, or did the earlier compression erase distinctions that must now be recovered from raw worlds or auxiliary information?**

This is a theory of **revision after forgetting**, not a second theory of joint-state construction.

## 2. Setup

Let \(\Omega\) be a finite model-world carrier.

Let \(P\in\Pi(\Omega)\) be the partition stored under an old scientific contract \(\mathcal C_0\), with quotient map

\[
q_P:\Omega\to S_P.
\]

Let \(Q\in\Pi(\Omega)\) be the required partition under a later or joint scientific contract \(\mathcal C_1\), with quotient map

\[
q_Q:\Omega\to S_Q.
\]

`Q` may be obtained by rerunning the full CREST common-lift construction after changing Future, History, Mechanism, Evidence, Target, or any combination of them. TU-1 begins **after** that world-level required partition has been defined.

The central question is whether there exists a deterministic recoding

\[
f:S_P\to S_Q
\]

such that

\[
q_Q=f\circ q_P.
\]

If so, the new state can be computed from the old state label alone. If not, the old scientific compression has erased information required by the new contract.

## 3. TU-1A — state-only revision criterion

### Theorem

The following are equivalent:

1. there exists \(f:S_P\to S_Q\) with \(q_Q=f\circ q_P\);
2. whenever two worlds have the same old state, they have the same new state;
3. every block of \(P\) is contained in one block of \(Q\);
4. the equivalence relation induced by \(P\) is a subset of the equivalence relation induced by \(Q\).

Equivalently, the old partition is at least as informative as the new partition.

### Proof

If \(q_Q=f\circ q_P\), then \(q_P(\omega)=q_P(\omega')\) implies
\(q_Q(\omega)=q_Q(\omega')\), proving 1 => 2. Statement 2 is exactly the assertion that every old-state block lies inside one new-state block, so 2 <=> 3 <=> 4. If 3 holds, define \(f(B)\) as the unique \(Q\)-block containing the \(P\)-block \(B\). This is well-defined and gives \(q_Q=f\circ q_P\), proving 3 => 1. ∎

### Corollary — irreversible forgetting under strengthening

If the revised contract requires a strict refinement of the old state,

\[
Q\text{ strictly refines }P,
\]

then no deterministic transformation of the old state label alone can recover \(Q\).

A distinction erased by \(q_P\) cannot later be recreated by post-processing \(q_P\).

This is not metaphysical irreversibility. It is an information-factorization statement relative to the stored scientific representation.

## 4. Auxiliary revision information

State-only revision is often impossible, but exact revision may become possible if a finite auxiliary code is retained or newly observed.

Let

\[
m:\Omega\to M
\]

be an auxiliary finite label. We say that `m` is **revision-sufficient** for \(P\to Q\) if there exists

\[
g:S_P\times M\to S_Q
\]

such that

\[
q_Q(\omega)=g(q_P(\omega),m(\omega))
\]

for every \(\omega\in\Omega\).

For each old-state block \(B\in P\), define its **new-state split multiplicity**

\[
r_B(P,Q)
=
\left|\{C\in Q:B\cap C\neq\varnothing\}\right|.
\]

Define

\[
K_{\rm rev}(P\to Q)
=
\max_{B\in P}r_B(P,Q).
\]

## 5. TU-1B — exact minimum auxiliary alphabet

### Theorem

The minimum possible cardinality of an auxiliary alphabet \(M\) that permits exact revision from \(P\) to \(Q\) is

\[
\boxed{
|M|_{\min}=K_{\rm rev}(P\to Q)
=
\max_{B\in P}r_B(P,Q).
}
\]

Hence the minimum fixed-length binary side memory is

\[
\boxed{
b_{\rm rev}(P\to Q)
=
\left\lceil\log_2 K_{\rm rev}(P\to Q)\right\rceil.}
\]

For algebraic comparisons we also use the idealized real-valued quantity

\[
D_{\rm rev}(P\to Q)
=
\log_2 K_{\rm rev}(P\to Q).
\]

### Proof

**Lower bound.** Fix any old block \(B\). Worlds in \(B\) share the same old-state label. If \(B\) intersects \(r_B\) distinct new-state blocks, those \(r_B\) possibilities must receive distinct auxiliary labels inside \(B\); otherwise two worlds with the same old label and same auxiliary label would require different new-state outputs. Thus

\[
|M|\ge r_B
\]

for every \(B\), so \(|M|\ge K_{\rm rev}\).

**Upper bound.** Let \(K=K_{\rm rev}\) and choose a common alphabet \(M=\{1,\ldots,K\}\). Within each old block \(B\), assign distinct labels to the distinct nonempty intersections \(B\cap C\) with \(C\in Q\). Labels may be reused in different old blocks because \(q_P\) already identifies which old block is occupied. The pair \((q_P,m)\) then identifies the unique new-state block. Hence \(|M|=K\) suffices. ∎

### Interpretation

Revision cost is controlled by the **worst locally hidden split**, not by the total number of new states in the whole universe.

This distinction matters because different old states can reuse the same auxiliary code alphabet.

## 6. TU-1C — monotonicity

### Proposition 1 — stronger revised contract cannot lower revision debt

If \(Q'\) refines \(Q\), then

\[
K_{\rm rev}(P\to Q')\ge K_{\rm rev}(P\to Q),
\]

and therefore

\[
D_{\rm rev}(P\to Q')\ge D_{\rm rev}(P\to Q).
\]

**Reason.** Refining \(Q\) cannot reduce the number of target blocks intersecting any fixed old block.

### Proposition 2 — retaining a finer old state cannot increase revision debt

If \(P'\) refines \(P\), then

\[
K_{\rm rev}(P'\to Q)\le K_{\rm rev}(P\to Q).
\]

Thus storing more distinctions now weakly reduces the worst-case side information needed for later revision.

This is the precise finite tradeoff behind the programme phrase **safe forgetting**: coarser current compression is cheaper now but can create larger future revision obligations.

## 7. Average refinement debt versus worst-case revision debt

Let

\[
P\vee Q
\]

be the common refinement whose blocks are the nonempty intersections \(B\cap C\) for \(B\in P\), \(C\in Q\).

Because

\[
|P\vee Q|=\sum_{B\in P}r_B(P,Q),
\]

define the **average refinement debt**

\[
D_{\rm avg}(P,Q)
=
\log_2|P\vee Q|-\log_2|P|
=
\log_2\left(\frac{1}{|P|}\sum_{B\in P}r_B(P,Q)\right).
\]

When `P` is a retained evidence partition and `Q` is a required state, this has the same partition-count form as CREST monitoring-resolution debt.

## 8. TU-1D — average debt is bounded by worst-case revisability debt

### Theorem

\[
\boxed{
0\le D_{\rm avg}(P,Q)\le D_{\rm rev}(P\to Q).
}
\]

Equality on the right holds exactly when every old block has the same maximal split multiplicity.

### Proof

Each \(r_B\ge1\), so their arithmetic mean is at least one, giving the lower bound. Their mean is at most their maximum:

\[
\frac{1}{|P|}\sum_B r_B\le\max_B r_B=K_{\rm rev}.
\]

Apply \(\log_2\), which is monotone. Equality between mean and maximum occurs exactly when every \(r_B\) equals the maximum. ∎

### Meaning

A small global increase in partition count does not guarantee that every old state is easy to revise. The average can conceal one rare old state that requires a large internal split.

## 9. TU-1E — arbitrarily large hidden revision burden under arbitrarily small average debt

### Theorem

For every integer \(m\ge1\) and every \(\varepsilon>0\), there exist finite partitions \(P,Q\) such that

\[
\boxed{
D_{\rm rev}(P\to Q)=m
\qquad\text{while}\qquad
D_{\rm avg}(P,Q)<\varepsilon.
}
\]

### Construction

Take \(N\) old-state blocks. Split one exceptional old block into exactly \(2^m\) new-state blocks and leave each of the other \(N-1\) old blocks unsplit.

Then

\[
K_{\rm rev}=2^m,
\qquad
D_{\rm rev}=m,
\]

while

\[
D_{\rm avg}
=
\log_2\left(1+\frac{2^m-1}{N}\right).
\]

Choose

\[
N>\frac{2^m-1}{2^{\varepsilon}-1}.
\]

Then \(D_{\rm avg}<\varepsilon\). ∎

### Interpretation

A representation can look globally cheap to update while containing a scientifically rare region in which earlier forgetting makes later revision arbitrarily demanding.

This is a different scale separation from CREST's capability-resolution divergence. CREST compares management-carrier gain with state/evidence resolution burden; TU-1E compares **average global refinement** with **worst-case local revisability after compression**.

## 10. Contract-composition corollary

Suppose an old contract \(\mathcal C_0\) has already produced stored state partition \(P\). A revised scientific programme declares \(\mathcal C_1\), and the full world-level CREST construction for the combined obligations yields joint required partition

\[
Q=J(\mathcal C_0\cup\mathcal C_1).
\]

Then:

1. the joint state can be produced from the old state label alone **iff** \(P\) refines \(Q\);
2. otherwise the exact minimum reusable auxiliary alphabet has size \(K_{\rm rev}(P\to Q)\);
3. if the old archive retained neither raw-world access nor revision-sufficient auxiliary information, exact joint-state recovery is impossible from the stored state label alone.

Thus contract composition has two mathematically distinct stages:

```text
full worlds available
    -> CREST-J1 / common-lift joint-state construction
    -> required revised partition Q

only old compressed state retained
    -> TU-1 revisability test
    -> state-only recoding OR exact revision debt
```

This separation prevents a hidden assumption that a scientifically adequate state remains indefinitely adequate after the scientific responsibility changes.

## 11. Relation to CCOC, MLTR, MRM, and CED

TU-1 does not replace the companion theorem programmes.

- **CCOC** can generate a revised `Q` because newly legal futures expose distinctions hidden by `P`.
- **MLTR** can generate a revised `Q` after a declared replacement/history system is lifted to a common carrier.
- **MRM** can generate a revised `Q` when newly retained mechanism response types disagree.
- **CED** can make an old stored evidence representation inadequate for a newly requested target or reliability contract.

TU-1 asks the common downstream question:

> Once those programmes say a finer/different representation is now required, was enough information retained to revise the old scientific state without reopening the world description?

## 12. Type and claim firewall

TU-1 concerns **representational revision**, not physical reversal or ecological memory.

It does not claim:

- that nature forgets information when scientists compress it;
- that one intrinsic ecological state exists independently of contract;
- that all contract changes require refinement;
- that `D_rev` is financial cost, sampling effort, Shannon entropy, or expected information under a probability distribution;
- that the elementary finite coding lemma is itself a new information-theory theorem;
- that empirical systems supply the exact partitions `P` and `Q` without a Reality-to-Model bridge.

## 13. Prior-art boundary

The finite factorization criterion is elementary quotient theory. The auxiliary-label problem is closely related to zero-error functional coding / coding with side information and partition refinement. Therefore publication novelty must **not** be claimed from TU-1A/B alone.

The candidate programme-level contribution requiring further prior-art audit is the conjunction:

1. scientific states are contract-relative ecological quotients;
2. contract revision is tested after an already licensed compression;
3. revisability is separated from world-level joint-state existence;
4. worst-case local revision debt is distinguished from global average refinement debt; and
5. the TU-1E family shows these burdens can diverge arbitrarily.

## 14. Next mathematical extension

The finite same-carrier theorem is now closed enough to use as substrate. The next nontrivial extension should address **carrier-changing revision**:

\[
\Omega_0\rightsquigarrow\Omega_1,
\]

where the old and revised states do not live on the same raw world set. This requires an explicit correspondence / lift and should connect to MLTR without merely relabeling its transport theorem.

A candidate TU-1F question is:

> Under what conditions does a replacement relation admit a revision-sufficient pullback whose minimum auxiliary code is invariant to the chosen faithful common lift?

That is not established here.
