from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "thesis" / "chapter_registry.json"
DRAFT_STATUS = ROOT / "thesis" / "draft_status.json"
OUTPUT = ROOT / "graphify-out" / "THESIS_WORKSPACE_REPORT.md"


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    draft_status = json.loads(DRAFT_STATUS.read_text(encoding="utf-8"))
    units = registry["units"]
    research = [unit for unit in units if unit["kind"] == "research_chapter"]
    source_status_counts = Counter(unit["status"] for unit in units)
    draft_stage_counts = Counter(draft_status["units"][unit["id"]]["stage"] for unit in units)
    source_count = sum(len(unit["canonical_sources"]) for unit in units)
    drafted = [unit for unit in units if draft_status["units"][unit["id"]]["stage"] != "brief_only"]

    lines = [
        "# Thesis Chapter Workspace Report", "", "## Purpose", "",
        "This report tracks the final forbidden-inference dissertation traversal. The order is editorial; source theorem and evidence ownership remain in the source repositories.",
        "", "## Editorial thesis", "", f"> **{registry['editorial_thesis']}**", "", "## Summary", "",
        f"- total writing units: {len(units)}", f"- source-owned research chapters: {len(research)}",
        f"- general introduction and synthesis units: {len(units)-len(research)}", f"- units with prose drafts: {len(drafted)}",
        f"- canonical source handoffs: {source_count}", f"- unique primary forbidden inferences: {len({unit['forbidden_inference'] for unit in units})}",
        f"- embedded TU modules: {len(registry['embedded_module_allocation'])}", f"- hard scientific dependencies in chapter order: {len(registry['hard_dependencies'])}",
        "", "## Final chapter registry", "", "| # | Chapter | Primary owner | Embedded | Source state | Draft stage |", "|---:|---|---|---|---|---|",
    ]
    for unit in units:
        progress = draft_status["units"][unit["id"]]
        owner = ", ".join(repo.removeprefix("repo:") for repo in unit["primary_source_repositories"])
        embedded = ", ".join(unit["embedded_modules"]) or "—"
        lines.append(f"| {unit['order']} | {unit['title']} | {owner} | {embedded} | `{unit['status']}` | `{progress['stage']}` |")
    lines += ["", "## Forbidden-inference spine", ""]
    for unit in units:
        lines.append(f"- **{unit['order']} {unit['title']}** — `{unit['forbidden_inference']}`")
    lines += ["", "## Companion programmes", ""]
    for name, info in registry["companion_programmes"].items(): lines.append(f"- **{name}** — {info['role']}")
    lines += ["", "## Source preconditions", ""]
    for item in registry["source_preconditions"]: lines.append(f"- `{item['chapter']}`: {item['condition']}")
    lines += ["", "## Draft-stage counts", ""]
    for stage, count in sorted(draft_stage_counts.items()): lines.append(f"- `{stage}`: {count}")
    lines += ["", "## Source-state counts", ""]
    for status, count in sorted(source_status_counts.items()): lines.append(f"- `{status}`: {count}")
    lines += ["", "## Writing boundary", "", "The former CREST-first draft sequence remains in git history but is not current prose. Every final chapter must be redrafted from its canonical handoffs around exactly one forbidden inference. The reset changes editorial traversal only; it does not reopen source analyses, transfer theorem ownership, or turn a prohibited inference into proof of its converse.", ""]
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)} for the final 10-chapter spine.")


if __name__ == "__main__":
    main()
