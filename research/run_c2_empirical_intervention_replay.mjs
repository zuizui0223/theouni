// C2 exploratory empirical intervention replay (2026-10-19).
// Source: Findlay public CT-Detection data, pinned at upstream commit and Git blob SHAs.
// No raw data redistributed. Only event-review/camera-pass opportunity costs are compared.
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { mkdirSync, writeFileSync } from "node:fs";
import { dirname } from "node:path";

const commit = "abc72f535bb59ebed202fb7acca852fc1647e97a";
const source = "https://raw.githubusercontent.com/melaniefindlay/CT-Detection/" + commit + "/";
async function csv(name, sha, expectedRows) {
  const resp = await fetch(source + encodeURIComponent(name));
  if (!resp.ok) throw new Error("Source fetch " + name + " HTTP " + resp.status);
  const data = Buffer.from(await resp.arrayBuffer());
  const blob = Buffer.concat([Buffer.from("blob " + data.length + "\0"), data]);
  assert.equal(createHash("sha1").update(blob).digest("hex"), sha, "source Git blob: " + name);
  const lines = data.toString("utf8").trim().split(/\r?\n/);
  const headers = lines.shift().split(",");
  const rows = lines.map((line, i) => {
    const values = line.split(",");
    assert.equal(values.length, headers.length, name + " row " + i);
    return Object.fromEntries(headers.map((key, j) => [key, values[j]]));
  });
  assert.equal(rows.length, expectedRows);
  return rows;
}
function random(seed) {
  let z = seed >>> 0;
  return () => {
    z = (z + 0x6D2B79F5) >>> 0;
    let t = z;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}
function shuffle(input, rng) {
  const v = input.slice();
  for (let i = v.length - 1; i > 0; i--) {
    const j = Math.floor(rng() * (i + 1));
    [v[i], v[j]] = [v[j], v[i]];
  }
  return v;
}
const avg = (rows, key) => rows.reduce((s, x) => s + x[key], 0) / rows.length;
const binaryMean = (rows, key) => rows.reduce((s, x) => s + x[key], 0) / rows.length;

function foxReplay(rows) {
  const groups = {};
  for (const r of rows) {
    assert(["0","1"].includes(r.TRIGGER), "unresolved fox trigger");
    (groups[r["CT.POS"]] ??= []).push({
      badger: Number(r.SPECIES === "BADGER"), trigger: r.TRIGGER === "1"
    });
  }
  const positions = Object.keys(groups).sort(), byPosition = [];
  assert.equal(positions.length, 4);
  for (let q = 0; q < positions.length; q++) {
    const pos = positions[q], entries = groups[pos];
    const accum = Object.fromEntries([1, 2, 3].map(c => [c, { n: 0, base: 0, more: 0, ref: 0 }]));
    for (let rep = 0; rep < 4000; rep++) {
      const rng = random(1012026 + q * 1000003 + rep * 7919);
      const shuffled = shuffle(entries, rng), cut = Math.floor(shuffled.length / 2);
      const pilot = shuffled.slice(0, cut), test = shuffled.slice(cut);
      const baselinePool = shuffle(pilot.filter(x => x.trigger), rng);
      const cameraPool = shuffle(test.filter(x => x.trigger), rng);
      if (baselinePool.length < 20 || cameraPool.length < 20) continue;
      const referencePool = shuffle(test, rng);
      const truth = binaryMean(test, "badger");
      const base = binaryMean(baselinePool.slice(0, 20), "badger");
      const more = (20 * base + cameraPool.slice(0, 20).reduce((s, x) => s + x.badger, 0)) / 40;
      for (const cost of [1, 2, 3]) {
        const nRef = Math.floor(20 / cost);
        const ref = binaryMean(referencePool.slice(0, nRef), "badger"), a = accum[cost];
        a.n++;
        a.base += Math.abs(base - truth);
        a.more += Math.abs(more - truth);
        a.ref += Math.abs(ref - truth);
      }
    }
    for (const cost of [1, 2, 3]) {
      const a = accum[cost];
      assert(a.n >= 3900, "insufficient replay draws");
      byPosition.push({position: pos, real_passes: entries.length,
        relative_reference_cost: cost, draws: a.n, baseline_camera_n: 20,
        added_camera_n: 20, added_reference_n: Math.floor(20 / cost),
        mae_baseline: a.base / a.n, mae_more_camera: a.more / a.n,
        mae_reference: a.ref / a.n});
    }
  }
  const aggregated = [1, 2, 3].map(cost => {
    const arr = byPosition.filter(x => x.relative_reference_cost === cost);
    return {relative_reference_cost: cost, mae_baseline: avg(arr, "mae_baseline"),
      mae_more_camera: avg(arr, "mae_more_camera"), mae_reference: avg(arr, "mae_reference"),
      reference_wins_positions: arr.filter(x => x.mae_reference < x.mae_more_camera).length};
  });
  return {design: "Half-split, 4000 replays per position; reference receives 20/cost additional labeled true passes versus 20 additional triggered camera records. Costs are synthetic review-unit ratios.", by_position: byPosition, equal_position_mean: aggregated};
}

function matchedOtter(rows) {
  const keys = ["CT.POS","ORIENT","GAIT","DIST","wet.dry","LOIT","AIR","ABS.DIFF"];
  const groups = {}, ordering = {};
  let matched = 0, droppedUnresolved = 0;
  for (let i = 0; i < rows.length - 2;) {
    const tr = rows.slice(i, i + 3), cams = tr.map(x => x["CAMERA.ID"]);
    const ok = new Set(cams).size === 3 && ["A","BS","BV"].every(x => cams.includes(x))
      && keys.every(k => tr.every(x => x[k] === tr[0][k]));
    if (!ok) {i++;continue;}
    matched++;
    ordering[cams.join(",")] = (ordering[cams.join(",")] ?? 0) + 1;
    if (tr.some(x => x.TRIGGER === "NA")) { droppedUnresolved++;i+=3;continue; }
    assert(tr.every(x => ["0","1"].includes(x.TRIGGER)));
    const by = Object.fromEntries(tr.map(x => [x["CAMERA.ID"], x]));
    (groups[by.A["CT.POS"]] ??= []).push({
      wet: Number(by.A["wet.dry"] === "wet"),
      a: by.A.TRIGGER === "1", bs: by.BS.TRIGGER === "1", bv: by.BV.TRIGGER === "1"
    });
    i += 3;
  }
  assert.equal(matched, 220);
  assert.equal(droppedUnresolved, 0);
  assert.equal(rows.length - 3 * matched, 46);
  return {groups, audit: {matched_triplets: matched, unmatched_rows: 46,
    unresolved_rows_in_matched: droppedUnresolved, camera_order: ordering}};
}

function otterEqualCost(matched) {
  const positions = Object.keys(matched.groups).sort(), byPosition = [];
  for (let q = 0; q < positions.length; q++) {
    const pos = positions[q], group = matched.groups[pos];
    const truth = binaryMean(group, "wet"), sums = {A40: 0, AB20: 0, AV20: 0};
    for (let rep = 0; rep < 5000; rep++) {
      const x = shuffle(group, random(1012026 + q * 1000003 + rep * 7919));
      const detected = {A40:x.slice(0,40).filter(z=>z.a),
        AB20:x.slice(0,20).filter(z=>z.a||z.bs),
        AV20:x.slice(0,20).filter(z=>z.a||z.bv)};
      for (const [arm, obs] of Object.entries(detected)) {
        assert(obs.length, "zero detection");
        sums[arm] += Math.abs(binaryMean(obs, "wet") - truth);
      }
    }
    byPosition.push({position: pos, matched_passes: group.length,
      truth_wet: truth, mae_A40: sums.A40/5000,
      mae_AB20: sums.AB20/5000, mae_AV20: sums.AV20/5000});
  }
  return {design: "5000 within-position replays; 40 camera-pass opportunities: A across 40 passes vs A+BS or A+BV across 20 passes.",by_position: byPosition,
    equal_position_mean: Object.fromEntries(["mae_A40","mae_AB20","mae_AV20"].map(k=>[k,avg(byPosition,k)]))};
}

function otterPilotPolicy(matched) {
  const positions = Object.keys(matched.groups).sort();
  const arms = { A20: [20, x=>x.a], AB10: [10,x=>x.a||x.bs], AV10:[10,x=>x.a||x.bv]};
  const byPosition = [];
  for (let q = 0; q < positions.length; q++) {
    const pos = positions[q], group = matched.groups[pos];
    const sums = {A20:0, AB10:0, AV10:0, biasOnly:0, costAware:0};
    const counts = {biasOnly:{A20:0,AB10:0,AV10:0},costAware:{A20:0,AB10:0,AV10:0}};
    for (let rep = 0; rep < 6000; rep++) {
      const x = shuffle(group, random(1122026 + q*1000003 + rep*7919));
      const pilot = x.slice(0,Math.floor(x.length/2)), heldout=x.slice(Math.floor(x.length/2));
      const pilotTruth=binaryMean(pilot,"wet"), testTruth=binaryMean(heldout,"wet");
      const biases={}, risks={}, errors={};
      for (const [name,[n,filter]] of Object.entries(arms)) {
        const pilotDetected = pilot.filter(filter);
        const p = pilotDetected.length ? binaryMean(pilotDetected,"wet") : pilotTruth;
        const bias = Math.abs(p-pilotTruth);
        biases[name] = bias;
        risks[name] = bias*bias + p*(1-p)/Math.max(1,n*pilotDetected.length/pilot.length);
        const detected=heldout.slice(0,n).filter(filter);
        errors[name]=detected.length ? Math.abs(binaryMean(detected,"wet")-testTruth):1;
        sums[name]+=errors[name];
      }
      const choose = scores => Object.keys(arms).reduce((a,b)=>scores[a]<=scores[b]?a:b);
      const biasArm=choose(biases),costArm=choose(risks);
      counts.biasOnly[biasArm]++;counts.costAware[costArm]++;
      sums.biasOnly+=errors[biasArm];sums.costAware+=errors[costArm];
    }
    byPosition.push({position:pos, matched_passes:group.length, choices:counts,
      ...Object.fromEntries(Object.entries(sums).map(([k,v])=>["mae_"+k,v/6000]))});
  }
  return {design: "6000 random half-splits per position; pilot CCTV truth sets choice A20, AB10 or AV10; test half withheld until after class choice. Pilot bias-only and bias-square-plus-variance policies. Retrospective, not protected.",
    by_position:byPosition, equal_position_mean:Object.fromEntries(
      ["A20","AB10","AV10","biasOnly","costAware"].map(k=>["mae_"+k,avg(byPosition,"mae_"+k)]))};
}

const fox = await csv("REGISTRATION_FOX_BADGER.csv","d2dc9852ca1f2a1380b991acba425d16e12327d5",881);
const otter = await csv("TRIGGER_OTTER_WET.DRY.csv","1f2fef008470ad1263d76beeb5be2b7006ff85aa",706);
const matched = matchedOtter(otter);
const results = {
  schema: "c2-exploratory-realdata-replay-v1", date: "2026-10-19",
  scientific_status: "RETROSPECTIVE EXPLORATORY — no protected confirmation of C2 design-prediction superiority",
  source: {repository: "melaniefindlay/CT-Detection", commit,
    fox_blob: "d2dc9852ca1f2a1380b991acba425d16e12327d5",
    otter_blob: "1f2fef008470ad1263d76beeb5be2b7006ff85aa"},
  interpretive_limits: ["Repeated passes are not independent individuals",
    "Four CT positions are not four population-level replicates",
    "Real costs of CCTV and two-camera systems not estimated",
    "220 matched otter triplets only; no unique event ID",
    "Pilot diagnosis requires a CCTV reference and does not outperform always A+BS",
    "Original results were inspected; this is not independent prospective validation"],
  fox: foxReplay(fox),
  otter: {matching:matched.audit, equal_camera_pass_cost:otterEqualCost(matched),pilot_diagnosis:otterPilotPolicy(matched)}
};
const output = process.argv[2] || "results/C2_EMPIRICAL_INTERVENTION_REPLAY_2026-10-19.json";
mkdirSync(dirname(output),{recursive:true});
writeFileSync(output,JSON.stringify(results,null,2)+"\n");
console.log("C2_REPLAY_PASS fox=881 otter=706 matched_triplets=220");
console.log("FOX",JSON.stringify(results.fox.equal_position_mean));
console.log("OTTER",JSON.stringify(results.otter.equal_camera_pass_cost.equal_position_mean));
console.log("DIAG",JSON.stringify(results.otter.pilot_diagnosis.equal_position_mean));
