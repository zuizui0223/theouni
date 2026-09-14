#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "C2_TREE_OPINION_DRAFT_V6.md"
OUT = ROOT / "manuscript" / "C2_CITATION_AUDIT_2026-09-14.json"

CITATION_RE = re.compile(r"\[([0-9,–\- ]+)\]")
REF_RE = re.compile(r"(?m)^(\d+)\. ")


def expand_group(group: str) -> set[int]:
    values: set[int] = set()
    for part in group.replace(" ", "").split(","):
        if not part:
            continue
        if "–" in part or "-" in part:
            sep = "–" if "–" in part else "-"
            a, b = part.split(sep, 1)
            if a.isdigit() and b.isdigit():
                values.update(range(int(a), int(b) + 1))
        elif part.isdigit():
            values.add(int(part))
    return values


def cited_numbers(text: str) -> set[int]:
    values: set[int] = set()
    for match in CITATION_RE.finditer(text):
        values |= expand_group(match.group(1))
    return values


def section(text: str, start: str, end: str) -> str:
    a = text.index(start)
    b = text.index(end, a)
    return text[a:b]


def main() -> None:
    text = MANUSCRIPT.read_text(encoding="utf-8")
    body, refs_text = text.split("## References", 1)
    refs = {int(x) for x in REF_RE.findall(refs_text)}
    cited = cited_numbers(body)

    expected = set(range(1, 15))
    assert refs == expected, {"references": sorted(refs)}
    assert cited == expected, {"cited": sorted(cited), "missing": sorted(expected - cited), "invalid": sorted(cited - expected)}

    section_requirements = {
        "introduction": (
            "## The bottleneck is not always data quantity",
            "### A necessary non-harm caveat",
            expected,
        ),
        "separation": (
            "## Interface 1 — Separation: does the measurement distinguish a live alternative?",
            "## Interface 2 — Relevance: can the distinction change the declared target?",
            {1},
        ),
        "relevance": (
            "## Interface 2 — Relevance: can the distinction change the declared target?",
            "## Interface 3 — Failure diversity: is this a genuinely new opportunity for evidence to survive?",
            {2, 3, 4, 5, 6},
        ),
        "failure_diversity": (
            "## Interface 3 — Failure diversity: is this a genuinely new opportunity for evidence to survive?",
            "## Interface 4 — Timely preservation: is the needed distinction still available downstream?",
            {7, 8},
        ),
        "timely_preservation": (
            "## Interface 4 — Timely preservation: is the needed distinction still available downstream?",
            "## A four-question distinction-flow audit",
            {9, 10, 11, 12, 13, 14},
        ),
        "metabarcoding_box": (
            "## Box 2. Metabarcoding: improve the interface that lost the taxon",
            "## What this stance changes",
            {11, 12, 13, 14},
        ),
    }

    coverage = {}
    for name, (start, end, required) in section_requirements.items():
        actual = cited_numbers(section(text, start, end))
        missing = required - actual
        assert not missing, {name: {"required": sorted(required), "actual": sorted(actual), "missing": sorted(missing)}}
        coverage[name] = {
            "required": sorted(required),
            "actual": sorted(actual),
        }

    first_anchor_expectations = {
        "## Interface 1 — Separation: does the measurement distinguish a live alternative?": {1},
        "## Interface 2 — Relevance: can the distinction change the declared target?": {2, 3, 4},
        "## Interface 3 — Failure diversity: is this a genuinely new opportunity for evidence to survive?": {7, 8},
        "## Interface 4 — Timely preservation: is the needed distinction still available downstream?": {9, 10},
    }
    local_anchor = {}
    for heading, required in first_anchor_expectations.items():
        tail = text.split(heading, 1)[1]
        next_heading = tail.find("\n## ")
        block = tail if next_heading < 0 else tail[:next_heading]
        paragraphs = [p for p in block.split("\n\n") if p.strip() and not p.lstrip().startswith("###")]
        early = "\n\n".join(paragraphs[:2])
        actual = cited_numbers(early)
        assert required & actual, {heading: {"expected_any": sorted(required), "early_actual": sorted(actual)}}
        local_anchor[heading] = sorted(actual)

    report = {
        "schema": "c2-citation-audit-v1",
        "manuscript": str(MANUSCRIPT.relative_to(ROOT)),
        "reference_count": len(refs),
        "all_references_cited": True,
        "invalid_citations": [],
        "section_coverage": coverage,
        "early_claim_anchor_citations": local_anchor,
        "status": "pass",
    }
    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("C2_CITATION_AUDIT PASS refs=14 all_cited=true section_coverage=true manuscript=v6")


if __name__ == "__main__":
    main()
