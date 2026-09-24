#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

from audit_c2_citations import main as audit_citations

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "C2_TREE_OPINION_DRAFT_V7.md"
FIGURE1 = ROOT / "manuscript" / "figures" / "C2_FIGURE1_MEASUREMENT_TO_EVIDENCE.svg"
FIGURE1_SPEC = ROOT / "proposals" / "C2_FIGURE1_DECISION_MAP_SPEC.md"

WORD_RE = re.compile(r"\b[\w*<>/=+.-]+\b", re.UNICODE)


def main() -> None:
    for path in (MANUSCRIPT, FIGURE1, FIGURE1_SPEC):
        assert path.exists(), path

    text = MANUSCRIPT.read_text(encoding="utf-8")
    lower = text.lower()
    semantic_lower = lower.replace("**", "")

    required = [
        "# When more measurement is not more evidence",
        "## Highlights",
        "## Abstract",
        "## The bottleneck is not always data quantity",
        "### A necessary non-harm caveat",
        "## From measurement to evidence: four interacting interfaces",
        "## Interface 1 — Timely preservation",
        "### Failure when missing: too late",
        "## Interface 2 — Separation",
        "### Failure when missing: same dimension",
        "## Interface 3 — Relevance",
        "### Failure when missing: wrong target",
        "## Interface 4 — Failure diversity",
        "### Failure when missing: false independence",
        "## A four-question distinction-flow audit",
        "## Box 1. Island *Campanula*",
        "## Box 2. Metabarcoding",
        "## What this stance changes",
        "## One core prediction: diagnosis should predict the best intervention",
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

    # Operational definition and unified conditional-locality thesis.
    for phrase in (
        "we use **evidential progress** in this operational sense",
        "increased ability to distinguish among live alternatives",
        "shared conditional structure",
        "precision is conditional on the observational axis already chosen",
        "conditional local metric as a universal proxy",
        "what those metrics are conditional on",
    ):
        assert phrase in lower, phrase

    # Historical and ecological identifiability prior art is explicit.
    for phrase in (
        "chamberlin's multiple working hypotheses",
        "platt's strong inference",
        "parameter-redundancy",
        "capture–recapture",
        "state-space models",
        "big observational data and experiments",
    ):
        assert phrase in lower, phrase

    # Decision-theoretic non-harm ceiling remains explicit.
    for phrase in (
        "extra information is intrinsically harmful",
        "cost-free observation that can simply be ignored",
        "does not guarantee more resolution of the claim",
    ):
        assert phrase in lower, phrase

    # Interface order must match Figure 1 and failure diversity must be cross-cutting.
    order = [
        lower.index("## interface 1 — timely preservation"),
        lower.index("## interface 2 — separation"),
        lower.index("## interface 3 — relevance"),
        lower.index("## interface 4 — failure diversity"),
    ]
    assert order == sorted(order)
    assert "failure diversity is cross-cutting rather than a fourth downstream stage" in semantic_lower

    # Cross-interface interaction is part of the synthesis, not left only as an outstanding question.
    for phrase in (
        "adding a second sensor may increase failure diversity while introducing a different detection function",
        "primer diversity can protect against one amplification blind spot while reducing depth per primer",
        "highly target-specific measurement can improve relevance while sacrificing information",
        "trade-offs in the flow of distinctions",
    ):
        assert phrase in lower, phrase

    # Relevance example must not be pure nuisance-vs-target strawman.
    for phrase in (
        "noisy target signal that is correct 75% of the time",
        "is not useless for the target",
        "two reasonable objectives rank the same candidate measurements differently",
    ):
        assert phrase in lower, phrase

    # Operating-semantics drift is explicitly nearby but not preservation failure.
    assert "that is not preservation failure because the record still exists" in lower

    # Box 1 now uses decoupling/intervention logic, not nectar-guide uniqueness.
    for phrase in (
        "design a contrast that decouples pollinators from climate",
        "island or site pairs that overlap in climate and elevation but differ in pollinator community",
        "pollinator exclusions",
        "visitor identity, visitation, effective pollen transfer and reproductive consequence",
        "not a new empirical validation claim",
    ):
        assert phrase in lower, phrase
    assert "nectar-guide phenotype could be one such measurement" not in lower

    # Main prediction is prospective intervention ranking, with concrete validation routes.
    for phrase in (
        "given a predeclared claim and several equal-cost measurement expansions",
        "diagnosing the limiting interface before collecting new data should predict",
        "simulations with known truth",
        "higher-quality reference channel or audit sample",
        "randomize equal effort",
        "it is weakened if the diagnoses do not predict",
    ):
        assert phrase in lower, phrase

    # Broad ecology/evolution surface.
    for phrase in (
        "ecology and evolution",
        "genomic",
        "environmental-dna",
        "evolutionary biology",
        "metabarcoding",
    ):
        assert phrase in lower, phrase

    # C1/Boundary keeps exact theorem/diagnostic surface.
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

    assert "not a necessary-and-sufficient theorem for all evidence" in lower
    assert "are the four failures exhaustive?" in lower
    assert "no. they are intended as a useful cross-cutting set" in lower

    references = text.split("## References", 1)[1]
    numbered_refs = re.findall(r"(?m)^\d+\. ", references)
    assert len(numbered_refs) == 20, len(numbered_refs)
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
        "10.1126/science.ns-15.366.92",
        "10.1126/science.146.3642.347",
        "10.1111/j.2517-6161.1996.tb02114.x",
        "10.1002/bimj.201400239",
        "10.1016/j.tree.2023.05.010",
        "10.1016/j.tree.2011.11.016",
    ):
        assert doi in text, doi

    # Figure contract remains compatible with the v7 ordering and cross-cutting diversity layer.
    svg = FIGURE1.read_text(encoding="utf-8").lower()
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
    ):
        assert label in svg, label

    spec = FIGURE1_SPEC.read_text(encoding="utf-8").lower()
    assert "failure diversity is not a fourth sequential arrow" in spec
    assert "measurement-to-evidence" in spec

    audit_citations()

    print(
        f"C2_TREE_MANUSCRIPT_V7 PASS words_before_references={word_count} "
        f"refs={len(numbered_refs)} synthesis=conditionality interactions=explicit citations=validated"
    )


if __name__ == "__main__":
    main()
