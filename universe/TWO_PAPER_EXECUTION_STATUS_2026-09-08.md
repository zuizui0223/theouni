# Two-paper execution status — 2026-09-08

Status: **active implementation of the canonical two-paper submission architecture**.

## Paper 1 — OBSERVATION

Submission home: `zuizui0223/v3`.

Active manuscript:

- `manuscript/OBSERVATION_DRAFT_V1.md`

Integrated source repositories:

- V3 — retained-information refinement;
- REC — record-entry selection, external-data distortion, irreversibility and correction transport;
- TNOA — semantic preservation/coarsening.

Completed:

- integrated manuscript v1;
- claim/source manifest;
- overlap firewall;
- Figure 1–5 architecture;
- integrated quantitative figure-data manifest with pinned source blobs;
- regression tests binding figure values to claim values;
- GitHub Actions `v3-ci` success on integration test commit `4b70323b610d952c2f2ecd81838ea2a636df492c` (run `34233530342`).

Current scientific spine:

```text
retained augmentation -> refinement
record-entry selection -> support loss
semantic coarsening -> distinction loss
irreversible loss -> requires independent/new information for recovery
```

Primary reality-facing result is REC fox/badger record-entry distortion; V3 and TNOA supply controlled synthetic strictness/stress tests.

## Paper 2 — EVIDENCE

Submission home: `zuizui0223/ced`.

Active manuscript:

- `manuscript/EVIDENCE_DRAFT_V1.md`

Integrated source repositories:

- Boundary — current structural identification limit;
- MROD — mechanism-learning observation value;
- CED — target-safe reportability, failure-aware refinement and risk/cost reporting.

Completed:

- integrated manuscript v1;
- claim/source manifest;
- overlap firewall;
- Figure 1–5 architecture;
- exact eight-world learning-versus-licensing divergence benchmark;
- executable benchmark implementation and regression tests;
- frozen machine-readable divergence result.

New integrated Evidence result:

```text
same 8 worlds, same equal-cost candidates

nuisance_detail:
  mechanism information = 2 bits
  exact target resolution = 0

target_split:
  mechanism information = 1 bit
  exact target resolution = 1

therefore:
mechanism-learning top != target-licensing top
```

This is the central synthesis that turns MROD and CED into two complementary utilities inside one paper rather than two competing next-observation manuscripts.

Current Evidence CI workflows are running from the latest integration commits; final status should be read from GitHub Actions before marking the implementation gate closed.

## Cross-paper firewall

```text
OBSERVATION
what distinctions survive the recording system?
        |
        v
retained compatible-world set
        |
        v
EVIDENCE
what do those surviving distinctions identify/license,
and what additional measurement is warranted?
```

Observation does not own next-measurement optimization or target reportability.
Evidence does not re-own refinement, shadow/no-row support loss, or semantic-coarsening loss.

## Source-repository role after consolidation

The six source repositories remain reproducibility/provenance units, not independent near-term submission targets:

- `v3`, `rec`, `tnoa` -> Observation sources;
- `boundary`, `mrod`, `ced` -> Evidence sources.

Standalone source manuscripts remain archived/source material unless the two-paper architecture is explicitly revoked.

## Next production gates

### Observation

1. bibliography merge/deduplication;
2. quantitative Figure 2–5 generation from pinned data;
3. source-text overlap audit;
4. journal-specific package and anonymous reviewer bundle.

### Evidence

1. quantitative source manifest for Boundary/MROD/CED panels;
2. Figure 2 generator for learning-versus-licensing divergence;
3. migrate integrated Markdown draft into existing CED LaTeX/MEE production path;
4. bibliography merge and overlap audit;
5. update anonymous reviewer bundle to include pinned Boundary/MROD source snapshots.
