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
    drafted = [
        unit
        for unit in units
        if draft_status["units"][unit["id"]]["stage"] != "brief_only"
    ]

    lines = [
        "# Thesis Chapter Workspace Report",
        "",
        "## Purpose",
        "",
        "This report tracks the source-bounded writing workspace for the preferred novelty-first dissertation traversal. It coordinates chapter drafting without transferring source theorem or evidence ownership to `theouni`.",
        "",
        "## Editorial thesis",
        "",
        f"> **{registry['editorial_thesis']}**",
        "",
        "## Summary",
        "",
        f"- total writing units: {len(units)}",
        f"- source-owned research chapters: {len(research)}",
        f"- general introduction and synthesis units: {len(units) - len(research)}",
        f"- units with prose drafts: {len(drafted)}",
        f"- canonical source handoffs: {source_count}",
        f"- unique primary forbidden inferences: {len({unit['forbidden_inference'] for unit in units})}",
        f"- embedded TU modules: {len(registry['embedded_module_allocation'])}",
        f"- hard scientific dependencies: {len(registry['hard_dependencies'])}",
        "",
        "## Chapter registry",
        "",
        "| Order | Unit | Primary owner | Embedded | Source state | Draft stage | Draft |",
        "|---:|---|---|---|---|---|---|",
    ]

    for unit in units:
        progress = draft_status["units"][unit["id"]]
        owner = ", ".join(repo.removeprefix("repo:") for repo in unit["primary_source_repositories"])
        embedded = ", ".join(unit["embedded_modules"]) or "—"
        draft_file = f"`{progress['draft_file']}`" if progress["draft_file"] else "—"
        lines.append(
            f"| {unit['order']} | {unit['title']} | {owner} | {embedded} | `{unit['status']}` | `{progress['stage']}` | {draft_file} |"
        )

    lines.extend(["", "## Drafted units", ""])
    if not drafted:
        lines.append("- none")
    for unit in drafted:
        progress = draft_status["units"][unit["id"]]
        lines.append(
            f"- `{unit['id']}` — `{progress['stage']}`, draft `{progress['draft_file']}`, source map `{progress['source_map_file']}`"
        )
        lines.append(f"  - next: {progress['next_action']}")

    lines.extend(["", "## Source-state counts", ""])
    for status, count in sorted(source_status_counts.items()):
        lines.append(f"- `{status}`: {count}")

    lines.extend(["", "## Draft-stage counts", ""])
    for stage, count in sorted(draft_stage_counts.items()):
        lines.append(f"- `{stage}`: {count}")

    lines.extend(["", "## Embedded module allocation", ""])
    for module, chapter in registry["embedded_module_allocation"].items():
        lines.append(f"- `{module}` -> `{chapter}`")

    lines.extend(["", "## Hard scientific dependency", ""])
    for edge in registry["hard_dependencies"]:
        lines.append(f"- `{edge['source']}` -> `{edge['target']}`: {edge['relation']}")

    lines.extend(
        [
            "",
            "## Writing boundary",
            "",
            "Each chapter must preserve its source-owned headline result, one primary forbidden inference, an explicit claim ceiling, and canonical source handoffs. Draft progress is tracked separately from claim status. Minimum draft length is enforced by the validator rather than repeated in this generated report. The workspace may coordinate prose and transitions, but it may not absorb source theorem ownership, upgrade bridge modules into independent novelty claims, or infer natural-state adequacy without the Reality-to-Theory admission bridge.",
            "",
        ]
    )

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(
        f"Wrote {OUTPUT.relative_to(ROOT)} with {len(units)} writing units, {len(drafted)} prose draft(s), "
        f"and {source_count} source handoffs."
    )


if __name__ == "__main__":
    main()
