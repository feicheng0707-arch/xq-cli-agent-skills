---
name: xq-cli-bid-generation
description: "Use when a local agent tool such as Codex, Claude Code, or WorkBuddy needs to operate Xique xq-cli for bid generation: login/runtime checks, uploading tender files, parse status, outline generation, content generation, status inspection, or DOCX export. This is a portable user-installed skill, not a repo-local sidecar skill."
---

# XQ CLI Bid Generation

Use this skill when the user wants a local agent tool to drive Xique bid-generation through `xq-cli`.

This skill is for external agent-tool users. Do not assume the `xq-sidecar-service` repo, sidecar APIs, or repo-local `.agents/skills` exist.

## Safety Boundary

- Treat `xq-cli` as a local business adapter, not a general shell.
- Never print tokens, saved config contents, base URLs with credentials, raw headers, raw command argv containing secrets, or private local paths in final user-facing summaries.
- Ask for explicit user approval before upload, generation, paid/charge flows, content write, or export.
- Prefer machine-readable JSON commands. Do not use interactive menus unless the user is actively driving the terminal.
- Summarize xq-cli JSON into user-safe status, `cid`, phase, artifacts, and next action. Do not paste large raw JSON unless the user asks for debugging details.
- If a command fails due to login/config, report the blocked state and ask the user to run `xq-cli login` or authorize browser login.

For details, read [references/safety-contract.md](references/safety-contract.md).

## Preferred Workflow

1. Runtime check:
   ```bash
   python scripts/xq_cli_safe.py health
   ```

2. Inspect choices before setting outline/export options:
   ```bash
   python scripts/xq_cli_safe.py choices --scope outline
   python scripts/xq_cli_safe.py choices --scope export
   ```

3. Upload and initialize a task after explicit user approval:
   ```bash
   python scripts/xq_cli_safe.py init --file /path/to/tender.docx --wait --i-understand-upload
   ```

4. Wait for parse completion when needed:
   ```bash
   python scripts/xq_cli_safe.py parse-status --cid <cid> --uuid <uuid> --wait
   ```

5. Generate outline after explicit user approval:
   ```bash
   python scripts/xq_cli_safe.py outline --cid <cid> --wait --i-understand-mutation \
     --outline-options-json '{"pageScopeCode":2,"base":"0","themeStyle":4,"tableQuantity":2,"tableColor":"BLUE"}'
   ```

6. Generate content after explicit user approval:
   ```bash
   python scripts/xq_cli_safe.py write --cid <cid> --type 1 --wait --i-understand-mutation
   ```

7. Inspect status:
   ```bash
   python scripts/xq_cli_safe.py status --cid <cid> --content
   ```

8. Export DOCX after explicit user approval:
   ```bash
   python scripts/xq_cli_safe.py export --cid <cid> --out /path/to/output --i-understand-export \
     --export-options-json '{"template":2,"layout":"enhanced","tableColor":"BLUE","tableStyle":"zebra"}'
   ```

For supported command shapes and option names, read [references/xq-cli-commands.md](references/xq-cli-commands.md).

## When Not To Use

- Do not use this skill for repo-local Xique Agent runtime implementation work. Use the repo's own adapter/capability contracts there.
- Do not bypass a product backend or approval process if the user is working inside a governed service that already exposes a safer API.
- Do not use raw shell commands for mutation/export when `scripts/xq_cli_safe.py` supports the operation.

## Output Shape

When reporting to the user, include only:

- whether the command succeeded, failed, or is blocked
- `cid` and `uuid` when present and useful
- current phase/status/progress
- generated artifact summary, such as exported DOCX name or outline availability
- the next safe action

Keep raw CLI output in local logs unless requested for debugging.
