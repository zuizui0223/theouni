# C2 exploratory real-data intervention replay — 2026-10-19

**Status:** empirical **retrospective / exploratory** replay; **NOT** a protected prospective validation of the C2 intervention-class prediction.

## What the bottleneck means operationally

A bottleneck is a specific missing distinction needed by a declared ecological target. For pass-level species composition, camera-triggered records lack the denominator of untriggered true animal passes (**upstream preservation/selection bottleneck**). For wet/dry otter composition, different cameras may rescue events lost by one camera, but sensor diversity can trade off against coverage of more biological passes (**shared observation-mode bottleneck**).

The C2 question is not whether detection bias exists (already known): does diagnosing the limitation before a measurement expansion identify the most useful intervention *at a given cost*?

## Source and reproducibility pins

- External field/CCTV source owner: **Findlay et al.**, public [melaniefindlay/CT-Detection](https://github.com/melaniefindlay/CT-Detection/tree/abc72f535bb59ebed202fb7acca852fc1647e97a), commit `abc72f535bb59ebed202fb7acca852fc1647e97a`.
- Fox/badger source `REGISTRATION_FOX_BADGER.csv`, Git blob `d2dc9852ca1f2a1380b991acba425d16e12327d5`, **881 true passes**. Raw source is not re-hosted here.
- Otter source `TRIGGER_OTTER_WET.DRY.csv`, Git blob `1f2fef008470ad1263d76beeb5be2b7006ff85aa`, **706 pass-camera rows**. Strict consecutive three-camera/full-metadata matching yields **220 matched pass triplets (660 rows)**; 46 unmatched rows excluded. The one unresolved trigger remains outside matched subset. There is **no unique pass ID**, so triplet matching is conservative but not ground-truth event linkage.
- C2 owns only the **measurement-intervention comparison** below; REC retains its record-entry empirical-result surface. These are public externally collected data, not new field data.

## Test 1: fox/badger — add rows or observe the missing denominator?

**Declared ecological target:** badger proportion among real passes, not proportion among triggered camera records.

For each of four physical positions, repeatedly split passes 50:50 into pilot and test partitions (4,000 deterministic draws/position). Start with 20 pilot camera-triggered records. At a fixed *review-count* budget, compare adding 20 more triggered-camera records versus adding independent CCTV-pass labels (20, 10 or 6 depending on assumed relative unit cost). The CCTV labels estimate the held-out pass composition; the camera alternative estimates it from selected trigger records.

| Upstream reference relative unit cost | Added camera records | Added reference passes | Mean abs. error: more camera | Mean abs. error: upstream reference | Positions favoring reference |
|---|---:|---:|---:|---:|---:|
| 1× | 20 | 20 | 0.12607 | **0.07769** | 4/4 |
| 2× | 20 | 10 | 0.12607 | **0.11572** | 3/4 |
| 3× | 20 | 6 | **0.12607** | 0.15200 | 0/4 |

Mean baseline (20 camera rows alone): **0.13974**. At the 1:1 event-review proxy, the reference alternative reduces error versus more camera rows by **38.4%**. At 3:1, the preference reverses. The assumed cost ratios are **sensitivity scenarios, not observed monetary costs**.

This supports a *system-specific* selection bottleneck and an important interaction with expense/sample variance. It does **not** show a universally superior new observation class.

## Test 2: otter — more passes in one mode or fewer passes in two modes?

**Declared ecological target:** wet proportion of true otter passes. Each arm receives **40 camera-pass observation opportunities** within a CT position:

- `A40`: camera A at 40 distinct passes;
- `AB20`: cameras A + BS at 20 passes;
- `AV20`: cameras A + BV at 20 passes.

Within-position deterministic random replays: 5,000 draws/position. Evaluate the detected wet fraction against the CCTV/reference wet fraction of the strict matched-triplet subset.

| Equal-observation-opportunity design | Four-position mean absolute error |
|---|---:|
| A40 (one mode; more biological passes) | 0.13936 |
| AB20 (two modes; fewer passes) | **0.08697** |
| AV20 (two modes; fewer passes) | 0.09413 |

AB20 and AV20 each improve the position-mean error at **3/4 positions**. At position BL, A40 is better: additional modes do not automatically improve the ecological estimand. Equal *camera-pass operations* do not mean equal financial/hardware costs or independent failure domains.

## Test 3: does a pilot diagnosis predict the best design?

A more direct, deliberately difficult C2 test was run on the otter triplets. Split each position's records into a pilot half and an untouched test half (6,000 deterministic replays/position). Pilot CCTV truth and camera outcomes are used to choose a **20-camera-pass** intervention for the test half: `A20`, `AB10`, or `AV10`.

Two policies were evaluated **without using the held-out test truth to choose the arm**:
1. `biasOnly`: smallest absolute pilot difference between detected and reference wet fraction;
2. `costAware`: smallest pilot estimated squared bias plus `p*(1-p)/expected detected n`.

| Held-out design / policy | Equal-position mean absolute error |
|---|---:|
| Always A20 (quantity-first) | 0.14552 |
| Always AB10 (fixed two-mode baseline) | **0.11742** |
| Always AV10 | 0.12206 |
| Pilot bias-only choice | 0.11894 |
| Pilot cost-aware choice | 0.12455 |

**Key adverse finding:** the pilot diagnosis improves on always A20, **but does not beat the best fixed two-mode design (always AB10)**. Thus the strong C2 claim that diagnosis adds predictive value beyond simple alternatives **is not validated** by this small retrospective replay. It must not be advertised as a positive prospective test.

## Inference limits and next gate

1. Original measurements and REC results were already visible; random test halves are replay holdouts, not a protected independent field trial.
2. Passes can repeat individuals; 4 CT positions are not 4 independent biological populations. Thousands of replays are Monte Carlo draws, **not sample size for population inference**.
3. One reference-labeled pass and one camera-pass operation are different resources. Price equivalence remains unmeasured.
4. The strict matched-triplet otter subset may not represent all 706 original rows.
5. The broad C2 thesis about all four interface types is **untested**. Here only upstream missing-denominator and observation-mode diversity/redundancy are illustrated and compared.
6. Pilot diagnosis requires a reference audit. A camera-only event table cannot identify the unrecorded pass composition without additional assumptions or observations.

**Scientific status:** quantitative real-data evidence that the useful measurement class changes with missing observations and cost; **no demonstrated novel prospective diagnostic advantage over the strongest fixed baseline**. The next decisive test requires prospective choice on new systems with true costs and an independent reference held out until intervention selection is frozen.
