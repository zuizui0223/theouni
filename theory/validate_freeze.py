from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "theory" / "FREEZE_v0.5.json"


def git_blob_sha(path: Path) -> str:
    """Hash canonical Git content after repository clean filters are applied."""
    relative = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "hash-object", f"--path={relative}", relative],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def main() -> None:
    freeze = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert freeze["schema_version"] == "theouni-theory-freeze.v0.5"
    assert freeze["status"] == "semantic_core_frozen"

    files = freeze["semantic_core_files"]
    paths = [item["path"] for item in files]
    assert len(paths) == len(set(paths)), "duplicate frozen path"

    for item in files:
        path = ROOT / item["path"]
        assert path.is_file(), f"missing frozen file: {item['path']}"
        actual = git_blob_sha(path)
        expected = item["git_blob_sha"]
        assert actual == expected, (
            f"frozen Theory Universe v0.5 drift at {item['path']}: "
            f"expected {expected}, got {actual}. "
            "Either restore the frozen file or increment the theory version."
        )

    module_ids = [item["id"] for item in freeze["theorem_modules"]]
    assert module_ids == ["TU-1", "TU-2", "TU-3", "TU-4"]
    assert all(item["publication_novelty"] == "not_asserted" for item in freeze["theorem_modules"])
    assert freeze["explicitly_open_after_freeze"]
    assert freeze["empirical_projection_policy"].strip()

    print(
        "Theory Universe v0.5 freeze validated: "
        f"{len(files)} frozen semantic-core files, {len(module_ids)} theorem modules."
    )


if __name__ == "__main__":
    main()
