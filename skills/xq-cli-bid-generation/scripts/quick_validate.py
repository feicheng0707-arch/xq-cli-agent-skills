#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    required = [
        ROOT / "SKILL.md",
        ROOT / "agents" / "openai.yaml",
        ROOT / "references" / "safety-contract.md",
        ROOT / "references" / "xq-cli-commands.md",
        ROOT / "scripts" / "xq_cli_safe.py",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        print(json.dumps({"ok": False, "missing": missing}, ensure_ascii=False, indent=2))
        return 1

    checks = [
        [sys.executable, "-m", "py_compile", str(ROOT / "scripts" / "xq_cli_safe.py")],
        [sys.executable, str(ROOT / "scripts" / "xq_cli_safe.py"), "health"],
        [
            sys.executable,
            str(ROOT / "scripts" / "xq_cli_safe.py"),
            "--dry-run",
            "outline",
            "--cid",
            "demo-cid",
            "--wait",
            "--i-understand-mutation",
            "--outline-options-json",
            '{"pageScopeCode":2,"base":"0","themeStyle":4}',
        ],
    ]
    results = []
    for command in checks:
        completed = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        results.append(
            {
                "command": " ".join(command[:3]),
                "returnCode": completed.returncode,
                "stdoutPreview": completed.stdout[:500],
                "stderrPreview": completed.stderr[:500],
            }
        )
        if completed.returncode != 0:
            print(json.dumps({"ok": False, "results": results}, ensure_ascii=False, indent=2))
            return completed.returncode
    print(json.dumps({"ok": True, "results": results}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
