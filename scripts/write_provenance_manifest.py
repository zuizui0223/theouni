from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANAGED = (
    ".gitignore",
    "README.md",
    "universe/ARCHITECTURE.md",
    "universe/registry.json",
    "universe/bridges/eco_genetic_crest_bridge_registry.json",
    "universe/schemas/eco_genetic_crest_bridge.schema.json",
    "graphify-out/graph.json",
    "graphify-out/graph.html",
    "graphify-out/GRAPH_REPORT.md",
    "scripts/build_curated_graph.py",
    "scripts/build_graph.py",
    "scripts/write_provenance_manifest.py",
    "scripts/validate_universe.py",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    registry = json.loads((ROOT / "universe" / "registry.json").read_text(encoding="utf-8"))
    files = []
    for relative in MANAGED:
        path = ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        files.append({"path": relative, "bytes": path.stat().st_size, "sha256": sha256(path)})
    payload = {
        "schema_version": "theouni-provenance.v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repository_role": "theory-first core plus meta-registry; no transfer of source scientific ownership",
        "registry_version": registry["schema_version"],
        "repository_count": registry["scope"]["repository_count"],
        "source_snapshots": {
            repo["name"]: repo["snapshot_sha"] for repo in registry["repositories"]
        },
        "managed_files": files,
    }
    (ROOT / "universe" / "PROVENANCE.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
