# C2 v7 Canonical Synchronization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restore the red Theory Universe Validation and make C2 v7 the internally consistent canonical manuscript surface without reopening C1/M1–M4 science.

**Architecture:** Treat the current failing publication-programme validator as the regression test. First make prior-art validation assert the v7 scientific concepts rather than stale v6 headings. Then propagate the already-preferred v7 manuscript through readiness/handoff/status receipts and add version-consistency assertions so a future manuscript promotion cannot leave canonical pointers stale. Verify the complete Theory Universe Validation workflow before integration.

**Tech Stack:** Python 3.12 validation scripts, JSON/Markdown governance files, GitHub Actions.

**Spec:** `universe/PUBLICATION_PROGRAMME_2026-09-11.json`, `universe/PUBLICATION_HANDOFF_2026-09-12.md`, `proposals/C2_TREE_RED_TEAM.md`, `manuscript/C2_TREE_OPINION_DRAFT_V7.md`.

## Global Constraints

- Keep the Observation/Evidence paper count at confirmed 5 + conditional 1.
- Do not transfer Boundary/C1 theorem ownership into C2.
- Do not reopen frozen M1–M4 science.
- Preserve TREE proposal-first routing and all human dispatch gates.
- Do not claim a v7 audit/status receipt that has not been generated and validated.

---

### Task 1: Repair v7 prior-art validator drift

**Files:**
- Modify: `scripts/validate_publication_programme.py`

**Interfaces:**
- Consumes: `proposals/C2_PRIOR_ART_MAP.md` v7 terminology.
- Produces: semantic assertions for the same six prior-art domains without depending on obsolete section-title wording.

- [ ] **Step 1: Preserve the failing evidence**

Use GitHub Actions run `34929121969`: `validate_publication_programme.py` currently fails in the prior-art exact-string loop.

- [ ] **Step 2: Replace stale literal requirements with v7-stable semantic anchors**

Require these v7 concepts: structural identification/identifiability; goal-oriented or targeted design; pseudoreplication; occupancy/imperfect detection; calibration/operating-semantics drift; shared conditional structure/four interacting interfaces.

- [ ] **Step 3: Push and run the workflow**

Expected: the previous line-145 failure disappears. Any next failure is treated as new evidence rather than bypassed.

### Task 2: Promote the validated v7 manuscript surface

**Files:**
- Modify as supported by generated evidence: `proposals/C2_SEND_READINESS.json`, `universe/PUBLICATION_HANDOFF_2026-09-12.json`, `universe/PUBLICATION_HANDOFF_2026-09-12.md`, `scripts/validate_publication_programme.py`, `scripts/validate_publication_handoff.py`.
- Create only if produced by current validators and needed as a canonical receipt: v7 manuscript/citation status artifacts.

**Interfaces:**
- Consumes: `manuscript/C2_TREE_OPINION_DRAFT_V7.md`, `scripts/validate_c2_manuscript.py`, `scripts/audit_c2_citations.py`.
- Produces: one consistent canonical C2 manuscript pointer and version-aware readiness/handoff assertions.

- [ ] **Step 1: Establish v7 machine facts**

Run/inspect the v7 manuscript and citation validators. Record actual word count, 20-reference audit state, and current validation evidence; do not copy v6 counts/runs into v7 fields.

- [ ] **Step 2: Propagate only verified v7 facts**

Update canonical pointers and prose from v6 to v7 while retaining historical v5→v6 compression as history if useful.

- [ ] **Step 3: Add a consistency guard**

Make publication/readiness/handoff validation fail if the preferred C2 manuscript, citation audit, and manuscript validator target different versions.

### Task 3: Full verification and integration

**Files:**
- No scientific manuscript edits unless a validator exposes an actual v7 defect.

**Interfaces:**
- Consumes: all changes from Tasks 1–2.
- Produces: green branch workflow and reviewable PR.

- [ ] **Step 1: Run the full Theory Universe Validation**

Expected: all workflow steps complete successfully, not merely the originally failing step.

- [ ] **Step 2: Search for stale canonical v6 references**

Historical v6 references may remain only where explicitly historical; active preferred/readiness/handoff pointers must resolve to v7.

- [ ] **Step 3: Open a PR with the failure, root cause, fix, and verification receipt**

Do not merge until the branch workflow is green and the diff shows no ownership/firewall changes.