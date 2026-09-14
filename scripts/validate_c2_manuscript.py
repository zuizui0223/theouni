#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

from audit_c2_citations import main as audit_citations

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "C2_TREE_OPINION_DRAFT_V6.md"
FIGURE1 = ROOT / "manuscript" / "figures" / "C2_FIGURE1_MEASUREMENT_TO_EVIDENCE.svg"
FIGURE1_SPEC = ROOT / "proposals" / "C2_FIGURE1_DECISION_MAP_SPEC.md"

WORD_RE = re.compile(r"\b[\w*<>/=+.-]+\b", re.UNICODE)


def main() -> None:
    for path in (MANUSCRIPT, FIGURE1, FIGURE1_SPEC):
        assert path.exists(), path

    text = MANUSCRIPT.read_text(encoding="utf-8")
    lower = text.lower()

    required = [
        "# When more measurement is not more evidence",
        "## Highlights",
        "## Abstract",
        "## The bottleneck is not always data quantity",
        "### A necessary non-harm caveat",
        "## From measurement to evidence: four interfaces, not one quantity",
        "## Interface 1 — Separation",
        "### Failure when missing: same dimension",
        "## Interface 2 — Relevance",
        "### Failure when missing: wrong target",
        "## Interface 3 — Failure diversity",
        "### Failure when missing: false independence",
        "## Interface 4 — Timely preservation",
        "### Failure when missing: too late",
        "## A four-question distinction-flow audit",
        "## Box 1. Island *Campanula*",
        "## Box 2. Metabarcoding",
        "## What this stance changes",
        "## Predictions for a distinction-design research programme",
        "## A measurement contract for ecological and evolutionary studies",
        "## Outstanding questions",
        "## Conclusion: design distinctions, not just data volume",
        "## Figure 1. Measurement-to-evidence interfaces and the four-question audit",
        "## References",
    ]
    for item in required:
        assert item.lower() in lower, item

    body = text.split("## References", 1)[0]
    word_count = len(WORD_RE.findall(body))
    assert 3500 <= word_count <= 5500, word_count

    assert "we use **evidential progress** in this operational sense" in lower
    assert "increased ability to distinguish among live alternatives" in lower
    assert "observation process actually preserves" in lower

    for phrase in (
        "ecology and evolution",
        "genomic",
        "environmental-dna",
        "evolutionary biology",
        "populations",
        "metabarcoding",
    ):
        assert phrase in lower, phrase
    assert "## box 2. island pollination" not in lower

    for phrase in (
        "extra information is intrinsically harmful",
        "cost-free observation that can simply be ignored",
        "proxy-to-responsibility mapping",
        "does not guarantee more resolution of the claim",
    ):
        assert phrase in lower, phrase

    for phrase in (
        "measurement-to-evidence",
        "timely preservation",
        "separation",
        "relevance",
        "failure diversity",
        "flow of distinctions",
        "diagnostic distinction design",
        "measurement escalation should be diagnostic-first, not quantity-first",
    ):
        assert phrase in lower, phrase

    for phrase in (
        "same dimension",
        "wrong target",
        "false independence",
        "too late",
        "measure a new distinction",
        "target-relevant information",
        "diversify failure domains",
        "capture the distinction earlier",
    ):
        assert phrase in lower, phrase

    for phrase in (
        "ecological and evolutionary measurement design should be organized around the flow of distinctions",
        "design reports should name the limiting interface",
        "benchmarks should follow the scientific responsibility through the pipeline",
        "additional measurement should compete against alternative measurement",
        "predictions for a distinction-design research programme",
        "does the matched remedy outperform an equal-cost quantity-first expansion",
    ):
        assert phrase in lower, phrase

    for forbidden in (
        "k-rank(M)",
        "Gamma/kappa",
        "Γ/κ",
        "breakdown factor",
        "anchor-ladder",
    ):
        assert forbidden not in text, forbidden

    for forbidden in (
        "zuizui0223",
        "manuscript placeholder",
        "source ledger",
        "source programme",
        "repository ownership",
    ):
        assert forbidden not in lower, forbidden

    assert "worked design example, not a new empirical validation claim" in lower
    assert "worked design illustration based on established metabarcoding and ecological-inference problems" in lower

    assert "not a necessary-and-sufficient theorem for all evidence" in lower
    assert "are the four failures exhaustive?" in lower
    assert "no. they are intended as a useful cross-cutting set" in lower
    assert "universal proxy for evidence" in lower or "universal proxy for evidential strength" in lower

    references = text.split("## References", 1)[1]
    numbered_refs = re.findall(r"(?m)^\d+\. ", references)
    assert len(numbered_refs) >= 14, len(numbered_refs)
    for doi in (
        "10.1371/journal.pcbi.1005153",
        "10.1093/bioinformatics/bts092",
        "10.1088/1361-6420/aad210",
        "10.1111/2041-210X.12423",
        "10.1016/j.tree.2006.08.007",
        "10.1016/j.tree.2009.03.005",
        "10.2307/1942661",
        "10.1111/ele.14400",
        "10.1890/0012-9658(2002)083[2248:ESORWD]2.0.CO;2",
        "10.1111/geb.12138",
        "10.1111/geb.13070",
        "10.1111/2041-210X.14485",
        "10.1111/2041-210X.12849",
        "10.1002/lom3.10659",
    ):
        assert doi in text, doi

    svg = FIGURE1.read_text(encoding="utf-8")
    svg_lower = svg.lower()
    for label in (
        "biological opportunity",
        "retained record",
        "distinguishable alternatives",
        "declared target",
        "timely preservation",
        "separation",
        "relevance",
        "failure diversity across observation paths",
        "too late",
        "same dimension",
        "wrong target",
        "false independence",
        "capture earlier",
        "measure a new distinction",
        "measure target-relevant information",
        "diversify failure domains",
        "before collecting more data",
    ):
        assert label in svg_lower, label

    spec = FIGURE1_SPEC.read_text(encoding="utf-8").lower()
    assert "failure diversity is not a fourth sequential arrow" in spec
    assert "measurement-to-evidence" in spec
    assert "campanula" in spec
    assert "edna" in spec

    audit_citations()

    print(
        f"C2_TREE_MANUSCRIPT_V6 PASS words_before_references={word_count} "
        f"refs={len(numbered_refs)} figure1=validated citations=validated"
    )


if __name__ == "__main__":
    main()
