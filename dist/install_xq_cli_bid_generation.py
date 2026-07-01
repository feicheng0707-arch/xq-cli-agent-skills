#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
import zipfile
from pathlib import Path


SKILL_NAME = "xq-cli-bid-generation"


def main() -> int:
    args = build_parser().parse_args()
    archive = fetch_archive(args.archive)
    if args.sha256:
        actual = sha256(archive)
        if actual.lower() != args.sha256.lower():
            print_json({"ok": False, "error": "sha256_mismatch", "expected": args.sha256, "actual": actual})
            return 2

    target_root = resolve_target_root(args)
    if target_root is None:
        print_json(
            {
                "ok": False,
                "error": "target_required",
                "message": "Could not safely infer this agent tool's skills directory. Re-run with --target /path/to/skills.",
                "examples": {
                    "codex": "python3 install_xq_cli_bid_generation.py --archive <zip> --tool codex",
                    "custom": "python3 install_xq_cli_bid_generation.py --archive <zip> --target ~/.your-agent/skills",
                },
            }
        )
        return 2

    with tempfile.TemporaryDirectory(prefix="xq-skill-install-") as tmp:
        extracted_root = extract_archive(archive, Path(tmp))
        skill_dir = find_skill_dir(extracted_root)
        if skill_dir is None:
            print_json({"ok": False, "error": "skill_not_found", "message": f"Archive does not contain {SKILL_NAME}/SKILL.md"})
            return 2

        target_root.mkdir(parents=True, exist_ok=True)
        destination = target_root / SKILL_NAME
        if destination.exists():
            if not args.force:
                print_json(
                    {
                        "ok": False,
                        "error": "already_exists",
                        "destination": str(destination),
                        "message": "Use --force to replace the existing skill.",
                    }
                )
                return 2
            shutil.rmtree(destination)
        shutil.copytree(skill_dir, destination, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    validation = validate(destination)
    result = {
        "ok": validation["ok"],
        "skill": SKILL_NAME,
        "destination": str(destination),
        "targetRoot": str(target_root),
        "validation": validation,
        "nextStep": "Restart or refresh the agent tool if it does not hot-load skills.",
    }
    print_json(result)
    return 0 if validation["ok"] else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=f"Install {SKILL_NAME} into a local agent skill directory.")
    parser.add_argument("--archive", required=True, help="Path or https URL to the skill .zip or .tar.gz archive.")
    parser.add_argument("--sha256", default="", help="Optional expected SHA256 for the archive.")
    parser.add_argument("--target", default="", help="Explicit skills directory. Recommended for Claude Code, WorkBuddy, or unknown tools.")
    parser.add_argument(
        "--tool",
        choices=("auto", "codex", "custom"),
        default="auto",
        help="Use codex for ${CODEX_HOME:-~/.codex}/skills. auto only uses known safe local indicators.",
    )
    parser.add_argument("--force", action="store_true", help="Replace an existing skill with the same name.")
    return parser


def fetch_archive(value: str) -> Path:
    if value.startswith(("http://", "https://")):
        suffix = ".tar.gz" if value.endswith(".tar.gz") else ".zip"
        path = Path(tempfile.gettempdir()) / f"{SKILL_NAME}-download{suffix}"
        urllib.request.urlretrieve(value, path)
        return path
    return Path(value).expanduser().resolve()


def resolve_target_root(args: argparse.Namespace) -> Path | None:
    if args.target:
        return Path(args.target).expanduser().resolve()
    if args.tool == "codex":
        return Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex").expanduser().resolve() / "skills"
    if args.tool == "custom":
        return None
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home).expanduser().resolve() / "skills"
    codex_dir = Path.home() / ".codex"
    if codex_dir.exists():
        return codex_dir / "skills"
    return None


def extract_archive(archive: Path, target: Path) -> Path:
    if not archive.is_file():
        raise SystemExit(f"Archive not found: {archive}")
    if archive.name.endswith(".zip"):
        with zipfile.ZipFile(archive) as zf:
            zf.extractall(target)
        return target
    if archive.name.endswith((".tar.gz", ".tgz")):
        with tarfile.open(archive, "r:gz") as tf:
            tf.extractall(target)
        return target
    raise SystemExit("Unsupported archive type. Use .zip or .tar.gz.")


def find_skill_dir(root: Path) -> Path | None:
    direct = root / SKILL_NAME / "SKILL.md"
    if direct.is_file():
        return root / SKILL_NAME
    for path in root.rglob("SKILL.md"):
        if path.parent.name == SKILL_NAME:
            return path.parent
    return None


def validate(skill_dir: Path) -> dict[str, object]:
    required = [
        "SKILL.md",
        "agents/openai.yaml",
        "references/safety-contract.md",
        "references/xq-cli-commands.md",
        "scripts/xq_cli_safe.py",
        "scripts/quick_validate.py",
    ]
    missing = [name for name in required if not (skill_dir / name).is_file()]
    if missing:
        return {"ok": False, "missing": missing}
    quick_validate = skill_dir / "scripts" / "quick_validate.py"
    completed = subprocess.run(
        [sys.executable, str(quick_validate)],
        cwd=str(skill_dir),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return {
        "ok": completed.returncode == 0,
        "returnCode": completed.returncode,
        "stdoutPreview": completed.stdout[:1200],
        "stderrPreview": completed.stderr[:1200],
    }


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def print_json(payload: dict[str, object]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    raise SystemExit(main())
