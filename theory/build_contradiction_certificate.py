from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "theory" / "contradiction_matrix.json"
CERTIFICATE = ROOT / "theory" / "CONTRADICTION_CERTIFICATE_v0.6.md"

ABBREVIATIONS = {
    "compatible": "C",
    "conditional-on-common-carrier-or-map": "CM",
    "orthogonal-estimand": "OE",
    "open-bridge": "OB",
    "actual-conflict": "X",
}


def canonical_digest(matrix: dict) -> str:
    payload = json.dumps(
        matrix, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def render_certificate(matrix: dict) -> str:
    modules = [item["id"] for item in matrix["modules"]]
    pairs = matrix["pairs"]
    lookup = {
        frozenset((item["left"], item["right"])): ABBREVIATIONS[item["relation"]]
        for item in pairs
    }
    counts = Counter(item["relation"] for item in pairs)
    digest = canonical_digest(matrix)

    lines = [
        "# Draft v0.6 Pairwise Contradiction Certificate",
        "",
        "Status: **machine-generated finite typed audit; outside the frozen v0.5 core**.",
        "",
        "Registry: [`contradiction_matrix.json`](contradiction_matrix.json)",
        f"Canonical registry SHA-256: `{digest}`",
        "",
        "This certificate audits the current claim ceilings of 12 named theory modules. "
        "It proves registry completeness and the absence of a declared pairwise `actual-conflict`; "
        "it does not prove empirical truth, a missing bridge, joint-state existence, or higher-order consistency.",
        "",
        "## Result",
        "",
        f"- Modules: **{len(modules)}**",
        f"- Unordered pairs: **{len(pairs)}**",
        f"- `actual-conflict`: **{counts['actual-conflict']}**",
        f"- Verdict: **{'PASS' if counts['actual-conflict'] == 0 else 'FAIL'}**",
        "",
        "Relation counts:",
        "",
    ]
    for relation in ABBREVIATIONS:
        lines.append(f"- `{relation}`: {counts[relation]}")

    lines.extend(
        [
            "",
            "## Relation legend",
            "",
            "| Code | Relation | Meaning |",
            "|---|---|---|",
        ]
    )
    for relation, abbreviation in ABBREVIATIONS.items():
        lines.append(
            f"| {abbreviation} | `{relation}` | {matrix['relation_vocabulary'][relation]} |"
        )

    lines.extend(["", "## Symmetric pairwise matrix", ""])
    lines.append("| | " + " | ".join(modules) + " |")
    lines.append("|---|" + "---|" * len(modules))
    for row in modules:
        cells = []
        for column in modules:
            cells.append("--" if row == column else lookup[frozenset((row, column))])
        lines.append(f"| **{row}** | " + " | ".join(cells) + " |")

    lines.extend(["", "## Pair ledger", ""])
    lines.append("| Pair | Typed relation | Audit rationale |")
    lines.append("|---|---|---|")
    for item in pairs:
        lines.append(
            f"| {item['left']} / {item['right']} | `{item['relation']}` | {item['rationale']} |"
        )

    lines.extend(
        [
            "",
            "## Claim ceiling",
            "",
            "`actual-conflict = 0` means that no pair is jointly unsatisfiable after respecting "
            "its registered types and current scope. `conditional-on-common-carrier-or-map` and "
            "`open-bridge` are not silently upgraded to completed compositions. Pairwise closure "
            "also does not establish three-way or global consistency.",
            "",
            "Regenerate with `python theory/build_contradiction_certificate.py` and validate with "
            "`python theory/validate_contradiction_matrix.py`.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    CERTIFICATE.write_text(render_certificate(matrix), encoding="utf-8", newline="\n")
    print(f"Wrote {CERTIFICATE.relative_to(ROOT)} from {MATRIX.relative_to(ROOT)}.")


if __name__ == "__main__":
    main()
