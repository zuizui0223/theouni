#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript" / "C2_TREE_OPINION_DRAFT_V2.md"

WORD_RE = re.compile(r"\b[\w*<>/=+.-]+\b", re.UNICODE)


def main() -> None:
    assert MANUSCRIPT.exists(), MANUSCRIPT
    text = MANUSCRIPT.read_text(encoding="utf-8")
    lower = text.lower()

    required = [
        "# When more measurement is not more evidence",
        "## Highlights",
        "## Abstract",
        "## The problem is no longer simply how to collect more data",
        "## Failure 1: more precision can stay in the same evidential dimension",
        "## Failure 2: more information can answer the wrong question",
        "## Failure 3: more replicates can share the same blind spot",
        "## Failure 4: better downstream processing can arrive too late",
        "## The synthesis is a decision rule, not a four-box warning",
        "## Box 1. Island *Campanula*",
        "## Box 2. Island pollination",
        "## A measurement contract for ecological and evolutionary studies",
        "## Outstanding questions",
        "## Conclusion: ask what the next measurement changes",
        "## Figure 1. Diagnostic-first measurement escalation",
        "## References",
    ]
    for item in required:
        assert item.lower() in lower, item

    # Internal drafting range only; not a claim about a live journal word limit.
    body = text.split("## References", 1)[0]
    word_count = len(WORD_RE.findall(body))
    assert 3000 <= word_count <= 6000, word_count

    # The broad-audience revision must explicitly address both ecology and evolution.
    assert "ecology and evolution" in lower
    for phrase in (
        "genomic",
        "environmental-dna",
        "evolutionary study",
        "populations",
        "biodiversity sequencing",
    ):
        assert phrase in lower, phrase

    # C1/Boundary keeps its exact theorem/diagnostic surface. C2 states only the
    # qualitative same-dimension lesson.
    for forbidden in (
        "k-rank(M)",
        "Gamma/kappa",
        "Γ/κ",
        "breakdown factor",
        "anchor-ladder",
    ):
        assert forbidden not in text, forbidden

    # C2 must stay remedy-matched rather than a four-box warning list.
    for phrase in (
        "diagnostic-first, not quantity-first",
        "measure a new distinction",
        "target-relevant information",
        "diversify failure domains",
        "capture the distinction earlier",
        "what distinction the next measurement must create or preserve",
    ):
        assert phrase.lower() in lower, phrase

    # Worked examples retain their epistemic ceilings.
    assert "worked design example, not a new empirical validation claim" in lower
    assert "translation contract for observation design, not an empirical causal conclusion" in lower

    # Source manuscripts remain explicit placeholders until citable versions exist.
    for placeholder in (
        "Boundary manuscript placeholder",
        "MROD manuscript placeholder",
        "MROD island-pollination translation placeholder",
    ):
        assert placeholder in text, placeholder

    # The manuscript explicitly rejects exhaustiveness and a universal score.
    assert "are the four failures exhaustive?" in lower
    assert "no. they are intended as a useful cross-cutting set" in lower
    assert "universal proxy for evidential strength" in lower

    print(f"C2_TREE_MANUSCRIPT_V2 PASS words_before_references={word_count}")


if __name__ == "__main__":
    main()
