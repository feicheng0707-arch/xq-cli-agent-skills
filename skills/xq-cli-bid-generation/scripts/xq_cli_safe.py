#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


DEFAULT_XQ_CLI = Path.home() / ".hermes" / "node" / "bin" / "xq-cli"
DEFAULT_CONFIG = Path.home() / ".xq-opencli" / "config.json"
DEFAULT_CONFIG_DISPLAY = "~/.xq-opencli/config.json"

OUTLINE_VALUE_FLAGS = {
    "pageScope": "--page-scope",
    "page_scope": "--page-scope",
    "pageScopeCode": "--page-scope-code",
    "page_scope_code": "--page-scope-code",
    "base": "--base",
    "themeStyle": "--theme-style",
    "theme_style": "--theme-style",
    "tableQuantity": "--table-quantity",
    "table_quantity": "--table-quantity",
    "tableColor": "--table-color",
    "table_color": "--table-color",
    "tableStyle": "--table-style",
    "table_style": "--table-style",
    "planMode": "--plan-mode",
    "plan_mode": "--plan-mode",
    "referenceType": "--reference-type",
    "reference_type": "--reference-type",
    "multiBidId": "--multi-bid-id",
    "multi_bid_id": "--multi-bid-id",
    "multiBidType": "--multi-bid-type",
    "multi_bid_type": "--multi-bid-type",
    "epcEngineerType": "--epc-engineer-type",
    "epc_engineer_type": "--epc-engineer-type",
    "infoImg": "--info-img",
    "info_img": "--info-img",
    "sceneImg": "--scene-img",
    "scene_img": "--scene-img",
    "onlineImg": "--online-img",
    "online_img": "--online-img",
    "mermaidImg": "--mermaid-img",
    "mermaid_img": "--mermaid-img",
    "knowledgeImg": "--knowledge-img",
    "knowledge_img": "--knowledge-img",
    "mermaidStyle": "--mermaid-style",
    "mermaid_style": "--mermaid-style",
}

OUTLINE_BOOL_FLAGS = {
    "ignoreShortRequirement": "--ignore-short-requirement",
    "ignore_short_requirement": "--ignore-short-requirement",
    "ignoreMissingBill": "--ignore-missing-bill",
    "ignore_missing_bill": "--ignore-missing-bill",
}

EXPORT_VALUE_FLAGS = {
    "template": "--template",
    "layout": "--layout",
    "tableColor": "--table-color",
    "table_color": "--table-color",
    "tableStyle": "--table-style",
    "table_style": "--table-style",
    "startIndex": "--start-index",
    "start_index": "--start-index",
    "autoNumber": "--auto-number",
    "auto_number": "--auto-number",
    "addMark": "--add-mark",
    "add_mark": "--add-mark",
    "topMargin": "--top-margin",
    "top_margin": "--top-margin",
    "bottomMargin": "--bottom-margin",
    "bottom_margin": "--bottom-margin",
    "leftMargin": "--left-margin",
    "left_margin": "--left-margin",
    "rightMargin": "--right-margin",
    "right_margin": "--right-margin",
    "skeletonColor": "--skeleton-color",
    "skeleton_color": "--skeleton-color",
}

SECRET_KEYS = ("token", "password", "cookie", "authorization", "secret", "key")


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    exe = resolve_executable(args.xq_cli)

    if args.command == "health":
        emit(health(exe))
        return 0

    if args.command == "login-status":
        status = login_status(exe)
        emit(status)
        return 0 if status["ok"] else 1

    if args.command == "choices":
        if args.scope == "all":
            emit(
                {
                    "ok": True,
                    "outline": run_json(exe, ["choices", "outline", "--json"], timeout=args.run_timeout_sec),
                    "export": run_json(exe, ["choices", "export", "--json"], timeout=args.run_timeout_sec),
                }
            )
            return 0
        emit(run_json(exe, ["choices", args.scope, "--json"], timeout=args.run_timeout_sec))
        return 0

    if not exe.is_file():
        emit(failure("not_installed", "xq-cli executable was not found.", {"checkedPath": str(exe)}))
        return 2

    command_args = command_to_argv(args)
    if args.dry_run:
        emit({"ok": True, "dryRun": True, "argv": redact_argv([str(exe), *command_args])})
        return 0

    result = run_json(exe, command_args, timeout=args.run_timeout_sec)
    emit(result)
    return 0 if result.get("ok") else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Safe wrapper for Xique xq-cli bid generation.")
    parser.add_argument("--xq-cli", default="", help="Optional xq-cli executable path. Defaults to XQ_CLI_PATH, PATH, then ~/.hermes/node/bin/xq-cli.")
    parser.add_argument("--run-timeout-sec", type=float, default=3700, help="Subprocess timeout in seconds.")
    parser.add_argument("--dry-run", action="store_true", help="Print the redacted command that would run.")

    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("health")
    sub.add_parser("login-status")

    choices = sub.add_parser("choices")
    choices.add_argument("--scope", choices=("outline", "export", "all"), default="all")

    init = sub.add_parser("init")
    init.add_argument("--file", required=True)
    init.add_argument("--wait", action="store_true")
    init.add_argument("--i-understand-upload", action="store_true", required=True)
    init.add_argument("--poll-timeout-sec", type=int, default=0)

    parse_status = sub.add_parser("parse-status")
    parse_status.add_argument("--cid", required=True)
    parse_status.add_argument("--uuid", default="")
    parse_status.add_argument("--wait", action="store_true")
    parse_status.add_argument("--poll-timeout-sec", type=int, default=0)

    outline = sub.add_parser("outline")
    outline.add_argument("--cid", required=True)
    outline.add_argument("--uuid", default="")
    outline.add_argument("--wait", action="store_true")
    outline.add_argument("--outline-options-json", default="{}")
    outline.add_argument("--i-understand-mutation", action="store_true", required=True)
    outline.add_argument("--poll-timeout-sec", type=int, default=0)

    write = sub.add_parser("write")
    write.add_argument("--cid", required=True)
    write.add_argument("--type", type=int, default=1)
    write.add_argument("--wait", action="store_true")
    write.add_argument("--i-understand-mutation", action="store_true", required=True)
    write.add_argument("--poll-timeout-sec", type=int, default=0)

    status = sub.add_parser("status")
    status.add_argument("--cid", required=True)
    status.add_argument("--content", action="store_true")

    export = sub.add_parser("export")
    export.add_argument("--cid", required=True)
    export.add_argument("--out", required=True)
    export.add_argument("--export-options-json", default="{}")
    export.add_argument("--i-understand-export", action="store_true", required=True)
    export.add_argument("--poll-timeout-sec", type=int, default=0)

    return parser


def command_to_argv(args: argparse.Namespace) -> list[str]:
    if args.command == "init":
        file_path = Path(args.file).expanduser()
        if not file_path.is_file():
            emit(failure("source_missing", "Tender file does not exist or is not a file.", {"file": str(file_path)}))
            raise SystemExit(2)
        argv = ["init", "--file", str(file_path), "--json"]
        if args.wait:
            argv.append("--wait")
        append_poll_timeout(argv, args.poll_timeout_sec)
        return argv

    if args.command == "parse-status":
        argv = ["parse-status", "--cid", args.cid, "--json"]
        if args.uuid:
            argv.extend(["--uuid", args.uuid])
        if args.wait:
            argv.append("--wait")
        append_poll_timeout(argv, args.poll_timeout_sec)
        return argv

    if args.command == "outline":
        options = load_json_object(args.outline_options_json, "outline_options_invalid")
        argv = ["outline", "--cid", args.cid, "--json"]
        if args.uuid:
            argv.extend(["--uuid", args.uuid])
        if args.wait:
            argv.append("--wait")
        append_options(argv, options, OUTLINE_VALUE_FLAGS, OUTLINE_BOOL_FLAGS)
        append_poll_timeout(argv, args.poll_timeout_sec)
        return argv

    if args.command == "write":
        argv = ["write", "--cid", args.cid, "--type", str(args.type), "--json"]
        if args.wait:
            argv.append("--wait")
        append_poll_timeout(argv, args.poll_timeout_sec)
        return argv

    if args.command == "status":
        argv = ["status", "--cid", args.cid, "--json"]
        if args.content:
            argv.append("--content")
        return argv

    if args.command == "export":
        out_dir = Path(args.out).expanduser()
        out_dir.mkdir(parents=True, exist_ok=True)
        options = load_json_object(args.export_options_json, "export_options_invalid")
        argv = ["export", "--cid", args.cid, "--out", str(out_dir), "--json"]
        append_options(argv, options, EXPORT_VALUE_FLAGS, {})
        append_poll_timeout(argv, args.poll_timeout_sec)
        return argv

    raise SystemExit(f"Unsupported command: {args.command}")


def resolve_executable(value: str) -> Path:
    configured = value or os.environ.get("XQ_CLI_PATH", "")
    if configured:
        return Path(configured).expanduser()
    discovered = shutil.which("xq-cli")
    if discovered:
        return Path(discovered)
    return DEFAULT_XQ_CLI


def health(exe: Path) -> dict[str, Any]:
    installed = exe.is_file()
    config = inspect_config(DEFAULT_CONFIG)
    result: dict[str, Any] = {
        "ok": False,
        "installed": installed,
        "executable": str(exe),
        "config": config,
        "choices": {},
    }
    if installed:
        outline = run_json(exe, ["choices", "outline", "--json"], timeout=30)
        export = run_json(exe, ["choices", "export", "--json"], timeout=30)
        result["choices"] = {"outlineOk": bool(outline.get("ok")), "exportOk": bool(export.get("ok"))}
        result["ok"] = bool(installed and config["tokenConfigured"] and outline.get("ok") and export.get("ok"))
    result["login"] = login_evidence(result)
    return result


def login_status(exe: Path) -> dict[str, Any]:
    result = health(exe)
    login = result["login"]
    return {
        "ok": bool(login["authenticated"]),
        "state": login["state"],
        "evidence": login["evidence"],
        "rule": "Only report login success when ok is true. Do not infer or search guessed config paths.",
        "repair": login["repair"],
    }


def login_evidence(health_result: dict[str, Any]) -> dict[str, Any]:
    config = health_result.get("config", {})
    choices = health_result.get("choices", {})
    evidence = {
        "xqCliInstalled": bool(health_result.get("installed")),
        "configPathChecked": DEFAULT_CONFIG_DISPLAY,
        "configExists": bool(config.get("exists")),
        "baseUrlConfigured": bool(config.get("baseUrlConfigured")),
        "tokenConfigured": bool(config.get("tokenConfigured")),
        "outlineChoicesOk": bool(choices.get("outlineOk")),
        "exportChoicesOk": bool(choices.get("exportOk")),
    }
    if not evidence["xqCliInstalled"]:
        state = "not_installed"
        repair = "Install xq-cli first, then run xq-cli login --browser."
    elif not evidence["configExists"]:
        state = "login_required"
        repair = f"Run xq-cli login --browser and wait for it to finish. The current CLI config path checked is {DEFAULT_CONFIG_DISPLAY}."
    elif not evidence["baseUrlConfigured"]:
        state = "base_url_missing"
        repair = "Run xq-cli login --browser or login with the required --base-url."
    elif not evidence["tokenConfigured"]:
        state = "token_missing"
        repair = "Run xq-cli login --browser again and wait for the command to exit successfully."
    elif not evidence["outlineChoicesOk"] or not evidence["exportChoicesOk"]:
        state = "cli_probe_failed"
        repair = "Run xq-cli choices outline --json and xq-cli choices export --json to inspect the CLI error."
    else:
        state = "authenticated"
        repair = ""
    return {"authenticated": state == "authenticated", "state": state, "evidence": evidence, "repair": repair}


def inspect_config(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"exists": False, "checkedPath": DEFAULT_CONFIG_DISPLAY, "baseUrlConfigured": False, "tokenConfigured": False, "taskCacheConfigured": False}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {"exists": True, "checkedPath": DEFAULT_CONFIG_DISPLAY, "baseUrlConfigured": False, "tokenConfigured": False, "taskCacheConfigured": False, "unreadable": True}
    lower_keys = {str(k).lower(): v for k, v in data.items()} if isinstance(data, dict) else {}
    return {
        "exists": True,
        "checkedPath": DEFAULT_CONFIG_DISPLAY,
        "baseUrlConfigured": bool(lower_keys.get("baseurl") or lower_keys.get("base_url")),
        "tokenConfigured": bool(lower_keys.get("token") or lower_keys.get("access_token")),
        "taskCacheConfigured": bool(lower_keys.get("taskcache") or lower_keys.get("task_cache")),
    }


def run_json(exe: Path, argv: list[str], *, timeout: float) -> dict[str, Any]:
    try:
        completed = subprocess.run(
            [str(exe), *argv],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return failure("command_timeout", "xq-cli command timed out.", {"argv": redact_argv([str(exe), *argv])})
    except OSError as exc:
        return failure("command_failed", str(exc), {"argv": redact_argv([str(exe), *argv])})

    if completed.returncode != 0:
        return failure(
            failure_code(completed.stderr or completed.stdout),
            redact_text(completed.stderr or completed.stdout or "xq-cli command failed."),
            {"returnCode": completed.returncode, "argv": redact_argv([str(exe), *argv])},
        )

    try:
        data = json.loads(completed.stdout or "{}")
    except json.JSONDecodeError:
        return failure(
            "json_parse_failed",
            "xq-cli did not return valid JSON.",
            {"stdoutPreview": redact_text((completed.stdout or "")[:800]), "argv": redact_argv([str(exe), *argv])},
        )
    return {"ok": True, "data": redact_json(data)}


def append_options(argv: list[str], options: dict[str, Any], value_flags: dict[str, str], bool_flags: dict[str, str]) -> None:
    for key, value in options.items():
        if key in bool_flags:
            if value is True:
                argv.append(bool_flags[key])
            elif value in (False, None, ""):
                continue
            else:
                raise SystemExit(f"{key} must be boolean true/false")
            continue
        if key not in value_flags:
            raise SystemExit(f"Unsupported option: {key}")
        if isinstance(value, (dict, list)) or value is None or value == "":
            raise SystemExit(f"{key} must be a scalar value")
        argv.extend([value_flags[key], str(value)])


def append_poll_timeout(argv: list[str], value: int) -> None:
    if value > 0:
        argv.extend(["--timeout-sec", str(value)])


def load_json_object(value: str, code: str) -> dict[str, Any]:
    try:
        data = json.loads(value or "{}")
    except json.JSONDecodeError as exc:
        emit(failure(code, str(exc), {}))
        raise SystemExit(2)
    if not isinstance(data, dict):
        emit(failure(code, "Expected a JSON object.", {}))
        raise SystemExit(2)
    return data


def failure(code: str, message: str, details: dict[str, Any]) -> dict[str, Any]:
    return {"ok": False, "failure": {"code": code, "message": message, "retryable": True, "details": details}}


def failure_code(text: str) -> str:
    lowered = text.lower()
    if "login" in lowered or "token" in lowered or "unauthor" in lowered:
        return "login_required"
    if "not found" in lowered or "no such file" in lowered:
        return "not_found"
    if "parse" in lowered and "pending" in lowered:
        return "parse_pending"
    return "command_failed"


def redact_argv(argv: list[str]) -> list[str]:
    redacted: list[str] = []
    skip_next = False
    secret_flags = {"--password", "--token", "--authorization", "--api-key", "--base-url"}
    for item in argv:
        if skip_next:
            redacted.append("[REDACTED]")
            skip_next = False
            continue
        redacted.append(item)
        if item in secret_flags:
            skip_next = True
    return redacted


def redact_text(text: str) -> str:
    cleaned = text
    for key in SECRET_KEYS:
        cleaned = cleaned.replace(key.upper(), key)
    return cleaned[:2000]


def redact_json(value: Any) -> Any:
    if isinstance(value, dict):
        result: dict[str, Any] = {}
        for key, item in value.items():
            if any(secret in str(key).lower() for secret in SECRET_KEYS):
                result[key] = "[REDACTED]"
            else:
                result[key] = redact_json(item)
        return result
    if isinstance(value, list):
        return [redact_json(item) for item in value]
    return value


def emit(payload: dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    sys.exit(main())
