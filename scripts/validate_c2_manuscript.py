#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "C2_TREE_OPINION_DRAFT_V5.md"

WORD_RE = re.compile(r"\b[\w*<>/=+.-]+\b", re.UNICODE)


def main() -> None:
    assert MANUSCRIPT.exists(), MANUSCRIPT
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

    # Internal drafting range only; not a claim about a live journal word limit.
    body = text.split("## References", 1)[0]
    word_count = len(WORD_RE.findall(body))
    assert 3500 <= word_count <= 6000, word_count

    # Explicit operational definition of evidential progress.
    assert "we use **evidential progress** in this operational sense" in lower
    assert "increased ability to distinguish among live alternatives" in lower
    assert "observation process actually preserves" in lower

    # Broad ecology/evolution surface and deliberately cross-domain boxes.
    for phrase in (
        "ecology and evolution",
        "genomic",
        "environmental-dna",
        "evolutionary biology",
        "populations",
        "biodiversity sequencing",
        "metabarcoding",
    ):
        assert phrase in lower, phrase
    assert "## box 2. island pollination" not in lower

    # Protect the decision-theoretic caveat: C2 is about proxy failure, not a theorem that information harms.
    for phrase in (
        "extra information is intrinsically harmful",
        "cost-free observation that can simply be ignored",
        "proxy-to-responsibility mapping",
        "does not guarantee more resolution of the claim",
    ):
        assert phrase in lower, phrase

    # Unified positive spine: four interfaces in a measurement-to-evidence chain.
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

    # The four interfaces map to distinct failures/remedies.
    for phrase in (
        "same dimension",
        "wrong target",
        "false independence",
        "too late",
        "measure a new distinction",
        "target-relevant information",
        "diversify failure domains",
        "capture earlier",
    ):
        assert phrase in lower, phrase

    # The Opinion must take a stance and project a prospective research programme.
    for phrase in (
        "ecological and evolutionary measurement design should be organized around the flow of distinctions",
        "design reports should name the limiting interface",
        "benchmarks should follow the scientific responsibility through the pipeline",
        "additional measurement should compete against alternative measurement",
        "predictions for a distinction-design research programme",
        "diagnosing the missing interface predicts which design intervention produces the largest gain",
    ):
        assert phrase in lower, phrase

    # C1/Boundary keeps its exact theorem/diagnostic surface.
    for forbidden in (
        "k-rank(M)",
        "Gamma/kappa",
        "Γ/κ",
        "breakdown factor",
        "anchor-ladder",
    ):
        assert forbidden not in text, forbidden

    # Submission-facing manuscript must not expose internal provenance labels.
    for forbidden in (
        "zuizui0223",
        "manuscript placeholder",
        "source ledger",
        "source programme",
        "repository ownership",
    ):
        assert forbidden not in lower, forbidden

    # Worked examples retain explicit epistemic ceilings.
    assert "worked design example, not a new empirical validation claim" in lower
    assert "worked design illustration based on established metabarcoding and ecological-inference problems" in lower

    # Avoid converting the audit into an overclaimed theorem.
    assert "not a necessary-and-sufficient theorem for all evidence" in lower
    assert "are the four failures exhaustive?" in lower
    assert "no. they are intended as a useful cross-cutting set" in lower
    assert "universal proxy for evidence" in lower or "universal proxy for evidential strength" in lower

    # Reference surface: enough external literature to keep the Opinion externally grounded.
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

    print(f"C2_TREE_MANUSCRIPT_V5 PASS words_before_references={word_count} refs={len(numbered_refs)}")


if __name__ == "__main__":
    main()
