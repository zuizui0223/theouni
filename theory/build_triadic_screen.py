from __future__ import annotations

import json
from collections import Counter
from itertools import combinations
from pathlib import Path

from build_contradiction_certificate import canonical_digest

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "theory" / "contradiction_matrix.json"
SCREEN = ROOT / "theory" / "triadic_screen.json"
DOCUMENT = ROOT / "theory" / "TRIADIC_SCREEN_v0.6.md"

RELATION_PRIORITY = (
    "actual-conflict",
    "open-bridge",
    "conditional-on-common-carrier-or-map",
    "orthogonal-estimand",
    "compatible",
)

SCREEN_CLASS = {
    "actual-conflict": "contains-declared-pair-conflict",
    "open-bridge": "contains-open-bridge",
    "conditional-on-common-carrier-or-map": "requires-common-carrier-or-map",
    "orthogonal-estimand": "contains-orthogonal-estimand",
    "compatible": "all-three-pairs-compatible",
}

WITNESSES = [
    {
        "id": "TRIAD-W1-RACH-MRM-CED",
        "modules": ["MRM", "CED", "RACH"],
        "status": "bounded-shared-carrier-witness",
        "verifier": "theory/validate_triadic_screen.py",
        "claim": "One finite bridge carrier jointly realizes RACH causal multiplicity, MRM response equivalence, and CED deterministic target licensing.",
    },
    {
        "id": "TRIAD-W2-TU1-TU3-TU4",
        "modules": ["TU-1", "TU-3", "TU-4"],
        "status": "bounded-shared-carrier-witness",
        "verifier": "theory/validate_triadic_screen.py",
        "claim": "One four-world carrier jointly realizes TU-1 reverse-reuse failure, TU-3 loss-response adequacy, and TU-4 strict warning refinement.",
    },
]


def build_screen(matrix: dict) -> dict:
    modules = [item["id"] for item in matrix["modules"]]
    pair_lookup = {
        (item["left"], item["right"]): item["relation"] for item in matrix["pairs"]
    }
    witnesses = {tuple(item["modules"]): item["id"] for item in WITNESSES}
    triads = []

    for triple in combinations(modules, 3):
        pair_relations = []
        for left, right in combinations(triple, 2):
            pair_relations.append(
                {"left": left, "right": right, "relation": pair_lookup[(left, right)]}
            )
        counts = Counter(item["relation"] for item in pair_relations)
        controlling_relation = next(
            relation for relation in RELATION_PRIORITY if counts[relation]
        )
        witness_id = witnesses.get(triple)
        triads.append(
            {
                "modules": list(triple),
                "pair_relations": pair_relations,
                "pair_relation_counts": {
                    relation: counts[relation] for relation in RELATION_PRIORITY
                },
                "screen_class": SCREEN_CLASS[controlling_relation],
                "executable_assessment": (
                    {
                        "status": "verified-in-bounded-witness",
                        "witness_id": witness_id,
                    }
                    if witness_id
                    else {"status": "not-executably-assessed"}
                ),
            }
        )

    class_counts = Counter(item["screen_class"] for item in triads)
    assessment_counts = Counter(
        item["executable_assessment"]["status"] for item in triads
    )
    return {
        "schema_version": "theouni-triadic-screen.v0.6-draft",
        "id": "THEORY-TRIADIC-SCREEN-v0.6-draft",
        "status": "complete_pairwise-derived_screen_with_bounded_witnesses",
        "source_matrix": "theory/contradiction_matrix.json",
        "source_matrix_canonical_sha256": canonical_digest(matrix),
        "method": {
            "description": "Enumerate every unordered triple and copy its three registered pair relations. The highest-priority pair gate determines screen_class; this is triage, not a satisfiability decision.",
            "relation_priority": list(RELATION_PRIORITY),
            "screen_class_rule": "The first present relation in relation_priority supplies one mutually exclusive screen class.",
            "pairwise_relation_truth_revalidated": False,
            "emergent_three_way_conflict_excluded": False,
        },
        "counts": {
            "modules": len(modules),
            "unordered_triples": len(triads),
            "screen_classes": {
                name: class_counts[name] for name in sorted(SCREEN_CLASS.values())
            },
            "executable_assessments": dict(sorted(assessment_counts.items())),
        },
        "executable_witnesses": WITNESSES,
        "triads": triads,
        "claim_ceiling": "Complete 220-triple pair-profile coverage and two bounded shared-carrier witnesses only. Pairwise labels remain human judgments, and the screen neither discovers nor excludes emergent three-way inconsistency in unmodelled triples.",
        "documentation": "theory/TRIADIC_SCREEN_v0.6.md",
        "builder": "theory/build_triadic_screen.py",
        "validator": "theory/validate_triadic_screen.py",
    }


def render_json(screen: dict) -> str:
    return json.dumps(screen, ensure_ascii=False, indent=2) + "\n"


def render_document(screen: dict) -> str:
    counts = screen["counts"]
    lines = [
        "# Draft v0.6 Triadic Consistency Screen",
        "",
        "Status: **machine-generated complete pair-profile screen with bounded executable witnesses; outside the frozen v0.5 core**.",
        "",
        "Registry: [`triadic_screen.json`](triadic_screen.json)",
        f"Source pairwise registry SHA-256: `{screen['source_matrix_canonical_sha256']}`",
        "",
        "## Result",
        "",
        f"- Modules: **{counts['modules']}**",
        f"- Unordered triples: **{counts['unordered_triples']}**",
        f"- Executably assessed in a bounded shared-carrier witness: **{counts['executable_assessments'].get('verified-in-bounded-witness', 0)}**",
        f"- Not executably assessed: **{counts['executable_assessments'].get('not-executably-assessed', 0)}**",
        "",
        "Screen-class counts:",
        "",
    ]
    for name, count in counts["screen_classes"].items():
        lines.append(f"- `{name}`: {count}")

    lines.extend(
        [
            "",
            "These are mutually exclusive triage buckets under the conservative priority "
            "`actual-conflict > open-bridge > conditional-on-common-carrier-or-map > "
            "orthogonal-estimand > compatible`; they are not triple-level truth labels.",
        ]
    )

    lines.extend(["", "## Executable bounded witnesses", ""])
    for witness in screen["executable_witnesses"]:
        modules = " / ".join(witness["modules"])
        lines.append(f"- `{witness['id']}` ({modules}) — {witness['claim']}")

    lines.extend(
        [
            "",
            "## Claim ceiling",
            "",
            screen["claim_ceiling"],
            "",
            "Every triple and its three pair relations is recorded in `triadic_screen.json`. "
            "The screen is a complete triage ledger, not a three-way satisfiability proof. "
            "Only the two registered witnesses are jointly realized by executable finite models.",
            "",
            "Regenerate with `python theory/build_triadic_screen.py` and validate with "
            "`python theory/validate_triadic_screen.py`.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    screen = build_screen(matrix)
    SCREEN.write_text(render_json(screen), encoding="utf-8", newline="\n")
    DOCUMENT.write_text(render_document(screen), encoding="utf-8", newline="\n")
    print(
        f"Wrote {SCREEN.relative_to(ROOT)} and {DOCUMENT.relative_to(ROOT)} "
        f"with {screen['counts']['unordered_triples']} unordered triples."
    )


if __name__ == "__main__":
    main()
