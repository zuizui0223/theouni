# Portfolio governance — 2026-09-11

Status: **canonical whole-owner publication governance**.

This file separates four objects that had previously been conflated:

```text
repository inventory
!=
independent paper units
!=
track-local publication routers
!=
submission/readiness state
```

The machine-readable source of truth is [`PORTFOLIO_GOVERNANCE_2026-09-11.json`](PORTFOLIO_GOVERNANCE_2026-09-11.json).

## Core rules

1. One repository can own zero, one, or multiple papers.
2. One paper can span multiple repositories.
3. A source repository can feed a flagship without becoming a simultaneous submission.
4. A DOI/technical module is not a failed or low-ranked paper.
5. A future programme is not an active paper until its activation condition is met.
6. Track routers are local. In particular, `PUBLICATION_PROGRAMME_2026-09-11.json` governs only the Observation/Evidence track.
7. Thesis order, theory-map order, paper units and submission order are different objects.
8. Readiness is not a scientific-quality ranking.

## Whole-portfolio inventory

The current owner inventory contains **38 repositories** and maps to **34 paper units** under this governance snapshot.

Paper-state counts:

- **2 `ACTIVE_SUBMISSION`** — outward-facing proposal/submission is the immediate task.
- **19 `SUBMISSION_READY`** — scientific claim set is closed enough for production/submission.
- **7 `ACTIVE_MANUSCRIPT`** — independent paper exists but the current surface is still being developed.
- **2 `PAPER_ASSET`** — independent paper/theorem asset exists but is not in the immediate execution queue.
- **1 `CONDITIONAL`** — valid paper unit with an explicit activation rule.
- **3 `FUTURE`** — requires new data, a terminal result or a remaining qualification gate.

These counts are operational, not rankings.

## Track map

### Azami capitulum

```text
AZAMI_CH1   azami     GEB                             SUBMISSION_READY
EAZAMI_CH2  EAzami    Journal of Evolutionary Biology SUBMISSION_READY
AZA3_CH3    aza3      own-data Chapter 3              FUTURE
```

`azami` Chapter 1 is an independent paper. It is not a reproducibility-only repository and it is not absorbed into EAzami.

### Island pollination

```text
ISLAND_CH1  island                 SUBMISSION_READY
IZU_CH2     izu-core               SUBMISSION_READY
SHIMA_CH3   shimahotarubukuro      SUBMISSION_READY
```

These three chapters answer different questions: global filtering/branching, proximal response geometry, and directly realized Izu phenotype.

### Flower-colour programme

```text
HOTARUBUKURO    hotarubukuro       SUBMISSION_READY
FCP_SPATIAL     fcp                SUBMISSION_READY
FCP_COMPARATIVE fcp                SUBMISSION_READY
CHUN_P1         chun               SUBMISSION_READY
```

`fcp` is explicitly a **two-paper home**. The held-out six-species spatial lane and the 34-species comparative climatic-niche lane must never be collapsed because they share a repository.

### Niche-to-survey

```text
SDMR_A    sdmr    SUBMISSION_READY
ODSP_CH2  odsp    ACTIVE_MANUSCRIPT
EOG_WF    eog     SUBMISSION_READY
ACSP      acsp    SUBMISSION_READY
```

Product B in SDMR remains blocked and is not counted as a paper unit.

### Eco-genetic programme

```text
EGWE_NEE    egwe   ACTIVE_MANUSCRIPT
EGWEE_META  egwee  ACTIVE_MANUSCRIPT
```

`egc` is a load-bearing source for the current EGWE/NEE flagship and is not a simultaneous standalone submission under this snapshot.

### SLK architecture programme

```text
SLK       slk      ACTIVE_MANUSCRIPT
SCH       sch      ACTIVE_MANUSCRIPT
BITA      bita     SUBMISSION_READY
PAYOFF_B  payoff   ACTIVE_MANUSCRIPT
```

`balance` is a DOI-oriented technical module. PAYOFF-A, spatial spectral transport and topology/edgewise modularization are also modules. They are not standalone papers in the active queue.

### Observation / Evidence track

This track is governed locally by [`PUBLICATION_PROGRAMME_2026-09-11.json`](PUBLICATION_PROGRAMME_2026-09-11.json):

```text
C2_TREE      theouni      ACTIVE_SUBMISSION
BOUNDARY_C1  boundary     CONDITIONAL
TNOA_M1      tnoa         SUBMISSION_READY
MROD_M2      mrod         SUBMISSION_READY
CED_M3       ced          SUBMISSION_READY
V3_REC_M4    v3 + rec     SUBMISSION_READY
```

The famous **5+1** count belongs only to this track. It is forbidden to report it as the size of the whole publication portfolio.

### State-theory programme

```text
CREST  crest  SUBMISSION_READY
CCOC   ccoc   ACTIVE_MANUSCRIPT
MLTR   mltr   PAPER_ASSET
MRM    mrm    PAPER_ASSET
```

CREST uses companion results but does not erase the independent paper assets of CCOC, MLTR or MRM.

### Standalone / future validation

```text
ADAPTIVE_GAIN  adaptive-gain  SUBMISSION_READY
P284B_P1       284b           ACTIVE_SUBMISSION
TTF_METHOD     TTF            FUTURE
INSEPI_V13     insepi         FUTURE
```

The 284b pre-field Paper 1 is already a paper unit; Level-C field values are not a completion requirement for Paper 1.

## Repository roles that are not papers

- `balance` — module-only under current SLK routing.
- `egc` — source-only to the EGWE/NEE flagship under current routing.
- `pollipi` — acquisition/experimental testbed and infrastructure.
- `zuizui0223.github.io` — portfolio visualization only.
- `theouni` — governance/theory home **and** home of C2; its governance authority does not make it the owner of source results.

## Governance fix to the old 5+1 router

`PUBLICATION_PROGRAMME_2026-09-11.json` used to describe itself as the canonical publication programme and its 5+1 count was therefore easy to misread as owner-wide governance.

It is now explicitly a **track-local Observation/Evidence publication programme**. The whole-owner source of truth is this portfolio governance layer.

Hard invariant:

```text
whole-owner portfolio
    -> PORTFOLIO_GOVERNANCE_2026-09-11.json

Observation/Evidence track
    -> PUBLICATION_PROGRAMME_2026-09-11.json

thesis traversal
    -> thesis/final_chapter_architecture.json

theory/worldline topology
    -> WORLDLINE_ATLAS.md
```

No one of these files may infer the others' counts or order.
