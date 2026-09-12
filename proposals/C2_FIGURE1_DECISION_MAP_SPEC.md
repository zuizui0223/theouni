# C2 Figure 1 specification — diagnostic-first measurement escalation

Status: **canonical conceptual-figure specification for the TREE Opinion proposal**.

## Purpose

Figure 1 must make the paper's distinctive contribution visible without equations or repository knowledge.

It should not be a four-box catalogue of familiar warnings. It should show one common decision point:

> **Before collecting more data, diagnose why current evidence is inadequate.**

The figure then maps each diagnosis to a different next measurement action.

## Central layout

Use one left-to-right decision map.

```text
CURRENT EVIDENCE DOES NOT RESOLVE THE ECOLOGICAL QUESTION
                         |
                         v
          What kind of failure is limiting evidence?
                         |
      +------------------+------------------+------------------+
      |                  |                  |                  |
      v                  v                  v                  v
 SAME DIMENSION      WRONG TARGET     SHARED DEPENDENCE    UPSTREAM LOSS
  geometry             objective          dependence          pipeline
      |                  |                  |                  |
      v                  v                  v                  v
Does the next        Can the new       Is this a new       Is the needed
measurement         distinction       independent          distinction still
separate an          change the        opportunity for      present in the
unresolved           target/decision? evidence to survive? retained record?
explanation?
      |                  |                  |                  |
      v                  v                  v                  v
MEASURE A NEW        MEASURE            DIVERSIFY            CAPTURE EARLIER
DISTINCTION          TARGET-RELEVANT    FAILURE DOMAINS       IN THE PIPELINE
                     INFORMATION
```

## Four panel micro-examples

Each panel uses an ordinary ecological situation, not a theorem diagram.

### A — Same dimension

Visual: repeated measurements along the same environmental or phenotypic gradient become more precise, but two causal explanations remain overlapped.

Caption fragment:

> More precision does not identify what the observation geometry never separates.

Correct remedy:

> Measure a new distinction that separates an unresolved explanation.

### B — Wrong target

Visual: one measurement reveals substantial nuisance detail while the decision-relevant state remains unresolved; a smaller targeted measurement splits the decision.

Caption fragment:

> More information about the system is not necessarily more evidence for the declared target.

Correct remedy:

> Measure target-relevant information that can change the prediction or decision.

### C — Shared dependence

Visual: many replicates come from one sensor/site/batch/failure domain; a smaller set distributed across independent modes survives one common-mode failure.

Caption fragment:

> More repeats are not more independent opportunities for evidence to survive.

Correct remedy:

> Diversify failure domains, not only replicate count.

### D — Upstream loss

Visual: a biological event is missed before record creation; an increasingly accurate downstream classifier operates only on retained records and cannot recover the missing event.

Caption fragment:

> Downstream accuracy cannot recreate information deleted upstream.

Correct remedy:

> Capture the distinction earlier in the observation pipeline.

## Footer

Use one sentence spanning all four panels:

> **Measurement escalation should be diagnostic-first, not quantity-first: different failures require different new information.**

Secondary footer, if space permits:

> Additional measurement becomes additional evidence only when it creates or preserves a distinction that can change the ecological question being asked.

## Worked-example callouts

Do not turn Figure 1 into a Campanula or island-pollination figure. Those remain Boxes 1–2.

At most use small side labels:

- Campanula: new mechanism-separating observation rather than more of the same cline;
- island pollination: visitor occurrence, effective service and reproductive consequence require different measurements.

## What Figure 1 must not imply

- the four failures are exhaustive;
- one scalar evidence score exists;
- more measurement is generally harmful;
- all four failures occur in every study;
- the source programmes empirically validate the whole framework;
- Boundary's exact rank theorem, CED's finite witnesses, REC's numeric BirdVox result or TNOA's threshold numerics are themselves the TREE headline.

## Editorial test

A non-specialist ecologist should be able to look at Figure 1 for 30 seconds and answer:

1. why simply collecting more of the same data may fail;
2. why the four failures are not interchangeable;
3. what different action follows from each diagnosis.

If the figure only teaches the names of four failure classes, it has failed its purpose.
