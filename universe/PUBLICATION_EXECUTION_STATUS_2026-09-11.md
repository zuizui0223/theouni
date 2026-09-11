# Observation / Evidence track execution status — 2026-09-11

Status: **validated track-local execution companion to `PUBLICATION_PROGRAMME_2026-09-11.json`**.

Whole-owner publication governance lives in `PORTFOLIO_GOVERNANCE_2026-09-11.json`. This file tracks production state only for the Observation/Evidence 5+1 track. It does not transfer theorem/evidence ownership, define the whole publication portfolio, or alter the ten-chapter dissertation architecture.

## C2 — TREE Opinion pitch

**More measurement is not more evidence: four failures of monotonic reasoning in ecology**

State: **machine-ready for presubmission; human send gates only; not sent**.

Completed:

- four failure classes fixed and rewritten for broad ecological readership as same dimension / wrong target / shared dependence / upstream loss;
- long source-backed proposal: `proposals/C2_MORE_MEASUREMENT_NOT_MORE_EVIDENCE_TREE_PROPOSAL.md`;
- editor-facing pitch: `proposals/C2_TREE_EDITOR_PITCH.md`;
- external prior-art firewall: `proposals/C2_PRIOR_ART_MAP.md`;
- source ledger with pinned Boundary/CED/REC/TNOA/MROD blobs: `proposals/C2_SOURCE_LEDGER.json`;
- frozen presubmission send candidate: `proposals/C2_TREE_SEND_CANDIDATE.md`;
- authorship evidence ledger and metadata template: `proposals/C2_AUTHORSHIP_LEDGER.json`, `proposals/C2_TREE_AUTHOR_METADATA_TEMPLATE.md`;
- outside-reader packet: `proposals/C2_OUTSIDE_READER_PACKET.md`;
- TREE editorial red-team: `proposals/C2_TREE_RED_TEAM.md`;
- machine-readable send gate: `proposals/C2_SEND_READINESS.json`;
- latest validation run `34603216300` — **success** for send-candidate/outside-reader/red-team contracts.

Current novelty statement:

> C2 does not discover that “more data can fail.” It separates four different reasons why more measurement fails to become more evidence, and ties each failure to a different ecological design remedy.

Working proposal authorship is **Ruiqi Zhang — provisional first/corresponding author** because this is the only fully documented named-author/corresponding-author metadata currently present in the source set. Additional authors require substantive C2-level synthesis, drafting and accountability contributions; supervision, source-result ownership or repository commits alone are insufficient.

Remaining human send gates:

1. final authorship/corresponding-author approval;
2. one broad-interest ecologist outside the immediate theory/methods niche reads the pitch;
3. live TREE contact route is rechecked immediately before dispatch.

Do not write a full C2 manuscript before editorial interest unless strategy changes.

## C1 — Boundary / Ecology Letters

State: **proposal-ready, parked conditional**.

Assets:

- `zuizui0223/boundary/paper/ecology_letters_proposal.md`;
- `zuizui0223/boundary/paper/ecology_letters_proposal_email.md`;
- `zuizui0223/boundary/paper/PUBLICATION_ROUTE_2026-09-11.md`.

Activation rule: fallback if C2 is declined/too broad, or proceed only with the explicit firewall where C1 owns the full identification-axis argument and C2 uses Boundary only as the geometry exemplar.

## M1 — TNOA / Methods in Ecology and Evolution

State: **science complete; production validated; human metadata/visual inspection only**.

Canonical status: `zuizui0223/tnoa/submission/TNOA_SUBMISSION_STATUS_2026-09-11.json`.

Scientific/package state:

- `scientific_submission_blockers = 0` in the canonical submission manifest;
- standalone MEE manuscript and numbered abstract fixed;
- MIT licence present;
- anonymous DOCX built with double spacing, continuous line numbering, page numbering and rendered citations/references;
- deterministic anonymous reviewer bundle built and validated against pinned PolliPi/InsePi source checkouts;
- Figures 1–4 and Supplementary Figure S2 code-assembled from pinned quantitative sources;
- status itself is now CI-validated.

Validation receipts:

- source/package validation SHA `1f78e65ba3cb2c8fdfb622107b06cc16879a9bec`;
- original route/package run `34564310098` — **success**;
- anonymous DOCX artifact `10185463934`, digest `sha256:5a010f2524669732cf9f7f87eb6946e4865c986edb39c49b381a60fa5bdddfaf`;
- anonymous reviewer bundle artifact `10185463162`, digest `sha256:a08e8a45488ad495bd6c8fa7d2cd6c8c88ded030ce8fcb38fcaed8b4c08fb345`;
- initial-submission readiness artifact `10185463542`, digest `sha256:fe6bfc0ab53540b83b4c2e6c26b6bee1c3ec6296fe53d5851c889dade2f74b18`;
- composite-figure artifact `10185464425`, digest `sha256:439945387667f1af43fe48f963e1e62f622c1487ce5ca40cb2f4e53139712b1e`;
- latest status-contract HEAD `83e62cc446528453bd2f4ff5c0c14fbc9d4eef15`;
- latest validation run `34604066032` — **success**.

Remaining before submission:

- final author names/affiliations and corresponding-author details;
- CRediT contributions, acknowledgements, funding and competing interests;
- final human visual inspection of DOCX and code-assembled figures;
- live publisher word-count/submission-rule check;
- rebuild final private reviewer ZIP with final identity literals supplied to the scanner;
- rerun claim audit only if manuscript text materially changes.

**Science blocker: 0. Machine production blocker: 0.**

## M2 — MROD / Methods in Ecology and Evolution

State: **science frozen; anonymous Main/SI PDF production validated; human metadata/title page only**.

Scientific version-of-record SHA: `a8d21b30646df4dc337f1455ca7d89662b4d7ba3`.

G2, G5, Python 3.10/3.11/3.12 and the anonymous reviewer bundle already passed. MIT licence, cover-letter draft and ScholarOne contracts exist.

New presentation-only PDF production:

- `paper/submission_header.tex` adds double spacing, continuous line numbering and page numbering;
- `paper/build_submission_source.py` appends only frozen Figure 1–3 / S1 outputs to canonical Main/SI Markdown;
- `.github/workflows/manuscript_pdf.yml` rebuilds the frozen figures, scans anonymous sources and renders XeLaTeX PDFs;
- production run `34603759786` — **success**;
- production source SHA `4a1637844583fdfe3fdf2886fc6741fc60001f79`;
- PDF artifact `10265242618` — `mrod-mee-anonymous-pdfs-4a1637844583fdfe3fdf2886fc6741fc60001f79`;
- artifact digest `sha256:cb430f7bc68bfcc91d1f64b459b4cf11f6a0784e379506dbb9eb4a06ad85ce0d`;
- receipt: `paper/PDF_PRODUCTION_STATUS_2026-09-11.json`.

This production layer is presentation-only and does not supersede the frozen scientific validation SHA.

Remaining human blockers:

- correspondence postal address and email;
- acknowledgements and funding statement;
- ORCID;
- confirm/report the ChatGPT application/model version(s) used for final manuscript preparation;
- complete/export the non-anonymous title page;
- final human visual inspection of Main/SI PDFs;
- after the submitted file set is frozen, tag/archive and mint DOI according to the double-anonymous release plan.

**Science blocker: 0. Anonymous Main/SI PDF production blocker: 0.**

## M3 — CED / Ecological Modelling

State: **standalone scientific core closed; journal production validated**.

Canonical scientific unit:

- `zuizui0223/ced/manuscript/paper_b_main.tex`;
- `manuscript/paper_b_supplement.tex`;
- `manuscript/CED_SUBMISSION_STATUS_2026-09-11.json`.

Integrated `EVIDENCE_*` assets are synthesis/provenance only and are not submission units.

Ecological Modelling package includes submission checklist, five Highlights, cover-letter draft, Data/Code statement, title-page template, machine-readable package manifest, and standalone main + supplement production workflow.

Validation receipt:

- production source SHA `60258505aa5bcdcf9adc3befa3207f359a0de0db`;
- reproducibility run `34575265031` — **success**;
- manuscript build run `34575265062` — **success**;
- artifact `10189451673` — `ced-ecological-modelling-package`;
- artifact digest `sha256:81a4ec9bd871c73fab03b29b77f374f0eefc1099b5736eaa652d9840475f9394`;
- final route/status-contract HEAD `381b17b9f11772c5c1ed52b0eb5db3ebd0219387`;
- final route/status reproducibility run `34576313642` — **success**.

Remaining: live Guide-for-Authors check, final visual/reference/overlap audit and human author/declaration metadata.

**Science blocker: 0. Known CI/status-contract blockers: 0.**

## M4 — V3 + REC / Ecological Informatics

State: **scientific analysis blocker 0; journal/figure/reviewer production validated**.

Canonical unit:

- `zuizui0223/v3/manuscript/M4_V3_REC_DRAFT_V1.md`;
- `manuscript/M4_V3_REC_CLAIM_MANIFEST.json`;
- `manuscript/M4_SUBMISSION_STATUS_2026-09-11.json`.

TNOA is explicitly excluded and remains M1.

Production includes Ecological Informatics checklist, Highlights, cover letter, Data/Code statement, title-page template, Figure 1–5 architecture with no TNOA panel, deterministic Figure 2–5 generator, figure-value regression tests, and fail-closed reviewer package policy/manifest.

Validation receipt:

- production source SHA `bb6aa2589d73dedea980fe5f8fbdbd46ead84808`;
- v3-ci run `34575119019` — **success** on Python 3.10 and 3.11;
- artifact `10189408057` — `m4-v3-rec-quantitative-figures`;
- artifact digest `sha256:52998fa71ab5ee46631cab7d187911675530cbb84784cfa86b43d3a577fff1f4`;
- canonical status receipt HEAD `24278fe47f6e51139f9d09b255cafc5e858602d4`;
- metadata/status v3-ci run `34575758824` — **success**.

Third-party data state:

- BirdVox: documented CC BY 4.0;
- Findlay article: CC BY 4.0 and explicitly links `melaniefindlay/CT-Detection` as the online R/data resource;
- Findlay GitHub repository: no explicit root licence found;
- scientific reanalysis/publication preparation may proceed;
- original Findlay CSV redistribution remains fail-closed;
- reviewer reproduction retrieves original files from the source repository using pinned identities and distributes derived summaries/code, not copied original CSVs.

Remaining: live Guide-for-Authors check, final human visual Figure 1–5 assembly, final safe reviewer bundle, author/declaration metadata, final text-overlap audit and preferably written repository-level reuse clarification before any original-source redistribution.

**Science blocker: 0. Known CI/status-contract blockers: 0.**

## Observation / Evidence track summary

```text
C2  TREE Opinion pitch                 machine-ready / 3 human send gates
C1  Ecology Letters Perspective        proposal-ready / parked conditional
M1  TNOA -> MEE                        production validated / human+visual only
M2  MROD -> MEE                        production validated / human metadata+title page only
M3  CED -> Ecological Modelling        production validated / blockers 0
M4  V3+REC -> Ecological Informatics   production validated / blockers 0
```

Hard rule:

> Concept papers own cross-programme forbidden-inference synthesis inside this track. Method papers own their algorithms, theorems, benchmarks and claim ceilings. No publication unit may silently re-own another repository's result, and this track summary must never be reported as the whole-owner publication portfolio.
