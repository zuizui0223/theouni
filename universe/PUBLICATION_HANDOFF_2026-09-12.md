# Publication handoff — 2026-09-12

Status: **science and machine production closed for M1–M4; C2 machine-ready; remaining work is human metadata, visual review and dispatch decisions.**

This is the concise operational handoff for the Observation/Evidence publication track. The full historical execution log remains in `PUBLICATION_EXECUTION_STATUS_2026-09-11.md`; thesis order remains in `thesis/final_chapter_architecture.json`; the track publication architecture remains in `PUBLICATION_PROGRAMME_2026-09-11.json`.

## Current portfolio

| Unit | Target | Current state | Next true gate |
|---|---|---|---|
| C2 | Trends in Ecology & Evolution Opinion | machine-ready presubmission pitch | final authorship + one broad-interest read + live contact check |
| C1 | Ecology Letters Perspective | proposal-ready, parked conditional | activate only if C2 route warrants it |
| M1 | TNOA → Methods in Ecology and Evolution | science closed; DOCX/reviewer bundle/figures validated | human metadata + AI disclosure + visual check |
| M2 | MROD → Methods in Ecology and Evolution | science frozen; anonymous Main/SI PDFs validated | human metadata/title page + AI disclosure + visual check |
| M3 | CED → Ecological Modelling | science closed; audited package/PDFs validated | human metadata + AI declaration + visual check |
| M4 | V3+REC → Ecological Informatics | science closed; figures/safe reviewer ZIP/overlap audit validated | human metadata + AI declaration + visual check |

## C2 — TREE

Machine assets complete:

- proposal, editor pitch and frozen send candidate;
- prior-art firewall and pinned source ledger;
- authorship ledger and author-metadata template;
- outside-reader packet and editorial red-team;
- machine-readable send gate.

Working proposal authorship: **Ruiqi Zhang — provisional first/corresponding author**. Do not add authors based only on supervision, seniority, source ownership or commits.

Human send gates:

1. approve final author list/corresponding author;
2. obtain one broad-interest ecological read;
3. manually verify the current TREE contact/submission route immediately before dispatch.

Do not write the full Opinion before editorial interest unless strategy changes.

## M1 — TNOA / MEE

Machine status: **closed**.

Key receipts:

- latest package/status CI: `34665544834` — success;
- validated anonymous DOCX artifact: `10185463934`;
- validated anonymous reviewer bundle: `10185463162`;
- validated readiness package: `10185463542`;
- validated composite figures: `10185464425`.

Current live-guideline additions:

- `submission/MEE_AI_DISCLOSURE_TEMPLATE.md`;
- exact application/model version(s) and actual AI-use scope must be confirmed by a human before the Methods statement is finalized.

Remaining: final author metadata/CRediT/funding/COI/acknowledgements, AI disclosure, visual inspection and final private reviewer ZIP identity scan.

## M2 — MROD / MEE

Scientific version of record: `a8d21b30646df4dc337f1455ca7d89662b4d7ba3`.

Machine status: **closed**.

Presentation-only PDF receipt:

- production run `34603759786` — success;
- source SHA `4a1637844583fdfe3fdf2886fc6741fc60001f79`;
- artifact `10265242618`;
- digest `sha256:cb430f7bc68bfcc91d1f64b459b4cf11f6a0784e379506dbb9eb4a06ad85ce0d`.

Remaining: final author/correspondence metadata, ORCID, funding/acknowledgements, exact AI version/scope disclosure, title page, human visual check, then archive/tag/DOI after final file freeze.

## M3 — CED / Ecological Modelling

Machine status: **closed**.

Final scientific/audit facts:

- citation audit: `16/16`, missing `0`, unused `0`;
- historical Evidence self-overlap: no exact sentence of >=12 words reused;
- compatibility regression was repaired by retaining old production-status aliases; reproducibility returned to success.

Latest package including the Elsevier AI-declaration template:

- source SHA `074bdf82e9fe4be47246de25210d798b546bdf6c`;
- manuscript build run `34665521229` — success;
- artifact `10289241067` — `ced-ecological-modelling-package`;
- digest `sha256:568c8107ae66faa9272a5c40a19b5099b9f54cee4123365c4c29ab7623cd5f40`.

Remaining: final author/declaration metadata, exact AI tool/version/scope wording, human visual inspection, live portal article-type/details, and archive/DOI if required.

## M4 — V3+REC / Ecological Informatics

Machine status: **closed**.

Receipts:

- final status CI `34665099839` — success;
- safe reviewer-package run `34604732209` — success;
- reviewer artifact `10265608917`, digest `sha256:eb3c2f33a1fc4e1ce1e1160c501180091f718088243a6bc245d2cfa9bcf261df`;
- self-overlap run `34604836830` — success;
- overlap artifact `10265494094`, digest `sha256:b064fdd5f2c4a178fdc65992b389d25f3b319ed0526803de2312da7d5201a068`;
- current AI-declaration contract CI `34665388809` — success.

Rights boundary:

- Findlay reanalysis is not a science blocker;
- original Findlay CSV redistribution remains fail-closed;
- validated reviewer package contains derived/provenance material, not copied original CSVs.

Remaining: final author/declaration metadata, exact AI tool/version/scope wording, Figure 1–5 human visual inspection, live portal details and permanent submitted-source freeze.

## Live publisher-rule snapshot

Canonical snapshot: `LIVE_JOURNAL_RULES_2026-09-12.md`.

Important production implications:

- MEE requires the current double-anonymous formatting/code-review surface already implemented for M1/M2; substantive LLM use requires Methods disclosure with application name/version and human responsibility.
- Elsevier Highlights, when required, use 3–5 bullets of <=85 characters.
- substantive generative-AI manuscript preparation under current Elsevier policy requires a declaration immediately before References.
- exact Ecological Modelling/Ecological Informatics article-type, graphical-abstract and portal-specific rules remain upload-time checks rather than scientific tasks.

## Single human-input ledger

Use:

- `HUMAN_SUBMISSION_INPUTS_2026-09-12.md`
- `HUMAN_SUBMISSION_INPUTS_2026-09-12.json`

Known but **not automatically cross-propagated**:

- publication name: Ruiqi Zhang;
- `Kyoto University, Kyoto, Japan` is documented for MROD only and must be confirmed before reuse elsewhere.

Still human-supplied:

- final paper-specific author lists and order;
- correspondence details / ORCID;
- CRediT;
- funding / competing interests / acknowledgements;
- exact AI application/model version(s), use scope and responsible-author wording;
- final visual approval.

## Stop rule

> Do not reopen frozen science to solve an author, formatting, declaration, visual-QA or upload-field problem. The next phase is human completion and dispatch, not theorem hunting or new benchmark analysis.
