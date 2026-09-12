# Live journal-rule snapshot — 2026-09-12

Status: **submission-preparation snapshot, not a substitute for the live upload portal**.

Purpose: record only requirements verified from current official publisher/journal sources. Journal-specific items that could not be independently verified remain explicitly unresolved and must be checked immediately before upload.

## M1/M2 — Methods in Ecology and Evolution

Official MEE Author Guidelines were rechecked on 2026-09-12.

Verified current requirements relevant to TNOA/MROD:

- Standard/Research Articles: maximum stated range **7000–8000 words**, including tables/figure captions, statements and references;
- initial submission: single column, double line spacing, continuous line numbering and page numbering;
- separate title page, uploaded as a title-page/Supplemental Document Not for Review, containing author names, institutions/addresses, acknowledgements, contributions, data availability and related declarations;
- double-anonymous peer review;
- Abstract numbered **1–4**, aiming not to exceed **350 words**;
- no more than **8 keywords**, listed alphabetically;
- code/data must be available to editors/reviewers in anonymized form, either as files or through a suitable private-for-review repository;
- computational methods normally should be tested using simulations or benchmark datasets;
- substantive LLM/comparable-AI use must be disclosed in Materials and Methods, including application name and version; a corresponding or senior human author must take responsibility for generated code/text;
- submission confirmation includes a third-party-data condition: reused third-party datasets must either be publicly available for unrestricted reuse or have owner permission for reuse.

Implications already implemented:

- TNOA has formatted anonymous DOCX, reviewer bundle and a new `submission/MEE_AI_DISCLOSURE_TEMPLATE.md` human-finalization gate;
- MROD has anonymous Main/SI PDFs and already tracks exact AI application/model-version confirmation as a human blocker;
- no further scientific analysis is implied by these publisher requirements.

## M3 — Ecological Modelling

Current official Elsevier/ScienceDirect journal description was rechecked on 2026-09-12.

Verified scope:

- publishes new mathematical models and systems analysis for ecological processes;
- welcomes process-based models embedded in theory, explicit causative agents and innovative applications of models;
- uses mathematical/conceptual modelling, systems analysis, computer simulation and ecological theory;
- article families currently displayed include original/research articles, reviews, viewpoints and short communications.

Current Elsevier-wide requirements/policies relevant to the package:

- Highlights, when required by the journal, use **3–5 bullets**, each **<=85 characters including spaces**;
- substantive generative-AI manuscript preparation requires a separate declaration immediately before References, identifying the tool, purpose/scope and human responsibility;
- graphical-abstract requirements are journal-specific; Elsevier-wide graphical-abstract specifications do not establish that Ecological Modelling requires one.

Still live-check at upload:

- exact current Ecological Modelling article-type labels in the submission portal;
- whether Highlights are mandatory or optional for the chosen article type;
- whether a graphical abstract is required, optional or unsupported;
- journal-specific abstract/keyword limits not independently confirmed in this snapshot.

## M4 — Ecological Informatics

Current official Elsevier journal description was rechecked on 2026-09-12.

Verified scope:

- computational ecology, ecological data science, biogeography and ecosystem analysis;
- novel concepts/tools for ecological monitoring, acquisition, management, analysis and synthesis;
- sensor- and multimedia-based data acquisition;
- data archiving/sharing and data assimilation;
- modelling of ecological data and uncertainty analysis;
- eco-acoustics, digital image processing, machine/deep learning and quantitative decision support.

This remains a strong scope match for the V3+REC paper's sensing/record-entry/information-processing focus.

Current Elsevier-wide requirements/policies relevant to the package:

- Highlights, when required, use **3–5 bullets**, each **<=85 characters including spaces**;
- substantive generative-AI manuscript preparation requires a declaration immediately before References;
- graphical-abstract requirements are journal-specific and must not be inferred from Elsevier-wide guidance alone.

Still live-check at upload:

- exact current article type;
- whether Highlights/graphical abstract are mandatory for that article type;
- abstract/keyword limits and any journal-specific upload details.

## C2 — Trends in Ecology & Evolution

The current live TREE journal page could not be independently retrieved in the automated check, so the repository must **not** promote a historical contact route to a current verified address.

Publisher/editor guidance previously retrieved supports a proposal-first strategy and emphasizes:

- a clear statement of novelty;
- usefulness to a broad ecology/evolution readership;
- testing the proposal on readers outside the immediate specialist niche;
- avoiding unnecessary author inflation and being able to justify author contributions.

The existing C2 send gate therefore remains correct:

1. final authorship approval;
2. one broad-interest ecological read;
3. current TREE contact/submission route checked manually on the live site immediately before sending.

## C1 — Ecology Letters Perspective / Boundary

Official Ecology Letters Author Guidelines and the journal's Perspective/Synthesis editorial guidance were rechecked on 2026-09-12.

Verified current requirements relevant to Boundary:

- Perspective is **proposal-first** unless directly invited;
- unsolicited proposals must be **no more than 300 words**;
- the proposal should describe the nature and novelty of the work and its contribution to the discipline;
- the journal's Perspective/Synthesis editorial guidance additionally recommends stating the qualifications of the proposed author(s);
- proposals are sent to the Editorial Office at **both** `ecolets@cefe.cnrs.fr` and `ecolets2@cefe.cnrs.fr`;
- a full Perspective manuscript submitted without an invitation or approved proposal will not be considered;
- if invited, Perspective allows up to **7500 words** of main text and up to **10** figures/tables/text boxes;
- the journal states that Perspective has the **same novelty expectation as a Letter**;
- successful Perspectives should be broadly relevant to ecology and are not meant to be primarily reviews, unsupported opinion pieces, or summaries of the authors' own work;
- quantitative analysis is described by the journal as common in successful Perspectives and can strengthen justification for a new perspective.

Current Boundary implementation:

- `zuizui0223/boundary/paper/ecology_letters_proposal.md` is the proposal asset;
- `zuizui0223/boundary/paper/ecology_letters_proposal_email.md` already addresses both official Editorial Office emails;
- `zuizui0223/boundary/paper/BOUNDARY_ROLE_CONTRACT_2026-09-12.json` fixes C1 as the independent owner of structural identification geometry;
- C1 remains parked by publication strategy, not because of a machine or scientific blocker.

Human gate before any C1 dispatch:

1. decide whether C1 is activated now or remains parked behind C2;
2. confirm final author list and the author-qualification sentence used in the proposal/email;
3. confirm corresponding-author/contact metadata;
4. recheck the live Ecology Letters instructions immediately before sending.

## Elsevier AI declaration rule used for M3/M4

The current Elsevier journal policy (updated June 2026) requires authors who used generative-AI tools substantively in manuscript preparation to include a separate declaration before the References. The declaration should identify the tool/service, purpose of use and human review/responsibility. Basic grammar/spelling/punctuation checks alone do not require disclosure.

Templates now live at:

- CED: `zuizui0223/ced/submission/ECOLOGICAL_MODELLING_AI_DECLARATION_TEMPLATE.md`;
- M4: `zuizui0223/v3/submission/ECOLOGICAL_INFORMATICS_AI_DECLARATION_TEMPLATE.md`.

Exact model/version fields remain human-confirmation items; they must not be guessed from repository history.

## Governance rule

A publisher-rule update may change formatting, metadata, declarations or upload packaging. It must **not** silently reopen or modify a frozen scientific claim, theorem, benchmark or numerical result. If a journal requirement would require scientific redesign, record that as a new scientific version rather than treating it as routine production work.
