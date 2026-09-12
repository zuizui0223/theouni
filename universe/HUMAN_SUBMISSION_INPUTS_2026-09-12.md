# Human submission inputs — Observation / Evidence publication track

Status: **single-entry human metadata ledger; no scientific blockers**.

Purpose: collect human-supplied submission metadata once, then propagate only where the same value is genuinely valid. Do not infer missing author, ORCID, funding, correspondence or AI-version information from Git commits, repository ownership or seniority.

## A. Reusable author metadata

Fill once for each actual author, then reuse across papers only after confirmation.

### Author record A1 — working identity

- Publication name: **Ruiqi Zhang** *(documented as the named author in the MROD title-page draft; confirm preferred publication form before upload)*
- Affiliation: **Kyoto University, Kyoto, Japan** *(documented for MROD only; confirm whether it is the correct affiliation for every submission before propagation)*
- Department / unit: **[human input]**
- Correspondence email: **[human input]**
- Correspondence postal address: **[human input]**
- ORCID: **[human input]**

Do not copy the MROD affiliation automatically into TNOA, CED, M4, C2 or Boundary/C1 until the responsible author confirms it applies to that manuscript.

## B. Reusable declaration metadata

These may be shared across papers only when the wording is factually the same.

- Funding statement: **[human input; include grant numbers where applicable]**
- Conflict / competing-interest statement: **[human input]**
- General acknowledgements: **[human input]**
- Data/code archive identity after final freeze: **[generated later; do not invent DOI]**

## C. Generative-AI / AI-assisted preparation record

Publisher rules now make this a cross-paper human metadata item.

Record actual use rather than inferring it from repository history:

- Tool/service name(s): **[human confirmation]**
- Exact application/model version(s) relevant to final manuscript preparation: **[human confirmation]**
- Scope of use: **[human confirmation: e.g. manuscript organization, wording revision, code/documentation review]**
- Human author who reviewed the output and takes responsibility: **[human confirmation]**
- Any AI-assisted code requiring annotation under the target journal's policy: **[human confirmation]**

Paper-specific placement:

- **M1 TNOA / MEE:** statement belongs in Materials and Methods; application name/version explicitly required by current MEE guidance.
- **M2 MROD / MEE:** existing Methods disclosure must be finalized with exact application/model version(s).
- **M3 CED / Elsevier:** finalized declaration belongs immediately before References.
- **M4 V3+REC / Elsevier:** finalized declaration belongs immediately before References.
- **C2 TREE:** use the live Cell Press rule if invited to submit a full manuscript; proposal-stage email should not invent a declaration requirement.
- **C1 Boundary / Ecology Letters:** no full-manuscript declaration work is needed while the proposal is parked; if invited, use the live Wiley/Ecology Letters requirements then current.

## D. Paper-specific authorship decisions

### C2 — TREE Opinion

Working proposal state: **Ruiqi Zhang — provisional first/corresponding author**.

The live proposal route was checked on 2026-09-12; only a dispatch-time route recheck remains.

Human decision required: does any additional person make a substantive C2-level synthesis/drafting/accountability contribution that warrants coauthorship?

Do not add someone solely for supervision, seniority, source-result ownership or repository commits.

### C1 — Boundary / Ecology Letters Perspective

Current state: **machine-ready, strategically parked until the C2 editorial outcome**.

This is not a science or production blocker. No C1 human metadata is required now. If C1 is later activated because C2 is declined/too broad, or because both routes are intentionally run under the ownership firewall, then fill:

- Final author list/order: **[human input]**
- Corresponding author: **[human input]**
- One concise factual author-qualification sentence for the proposal: **[human input]**
- Affiliation/contact metadata confirmed for C1: **[yes / no]**
- Live Ecology Letters proposal instructions rechecked immediately before dispatch: **[yes / no]**

The current proposal is 226/300 words under the canonical checker, leaving 74 words of headroom. Keep the qualification sentence concise (recommended <=40 words). Do not infer it from repository ownership, seniority or supervision alone.

### M1 — TNOA / MEE

- Final author list/order: **[human input]**
- Corresponding author: **[human input]**
- CRediT by author: **[human input]**

### M2 — MROD / MEE

Repository title-page draft currently documents **Ruiqi Zhang** as author and corresponding author.

- Confirm final author list/order: **[human confirmation]**
- Confirm corresponding author: **[human confirmation]**
- Confirm/finalize CRediT statement: **[human confirmation]**

### M3 — CED / Ecological Modelling

- Final author list/order: **[human input]**
- Corresponding author: **[human input]**
- CRediT by author: **[human input]**

### M4 — V3+REC / Ecological Informatics

- Final author list/order: **[human input]**
- Corresponding author: **[human input]**
- CRediT by author: **[human input]**
- Third-party data acknowledgement wording: use the frozen Findlay/BirdVox provenance and rights notes; do not invent permission language.

## E. Human visual checks

These cannot be meaningfully certified by CI alone:

- M1: final DOCX and Figures 1–4/S2 visual inspection;
- M2: final Main/SI PDF visual inspection;
- M3: main PDF, supplement and figure layout inspection;
- M4: Figure 1–5 assembly/legibility inspection;
- C2: one broad-interest ecologist reads the pitch before dispatch;
- C1: no visual or metadata work while parked; if activated, inspect only the proposal packet before sending.

## F. Final upload-only checks

Do these immediately before the relevant submission rather than freezing them months early:

- live journal Guide/portal requirements;
- current submission/contact route;
- exact article type;
- title/abstract/keyword fields as rendered by the portal;
- graphical-abstract requirement if any;
- current declarations and AI policy;
- final author approval;
- archive/DOI only after the submitted file set is fixed and anonymity policy permits release.

## Hard rule

> Missing human metadata is not scientific uncertainty. Do not reopen frozen science to solve an author, funding, disclosure, formatting or upload-field problem.
