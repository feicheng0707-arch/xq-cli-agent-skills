# Safety Contract

## Public vs Private

Public-safe:

- `cid`, `uuid`, task title, phase, status, progress
- chosen user-facing generation options
- exported file name when the user asked for export
- concise failure code and repair instruction

Private:

- saved config file contents
- tokens, cookies, headers, account/password values
- base URL if it contains credentials or private deployment details
- raw CLI argv in user-facing output
- full local absolute paths unless the user needs the file location
- large raw JSON payloads

## Approval

Require explicit user approval before:

- `init`: uploads a tender file
- `outline`: changes task generation state
- `write`: may trigger charge/order/content generation
- `export`: writes a DOCX to local disk
- any command using `--interactive` or browser login

The wrapper script enforces confirmation flags for side-effect commands. If bypassing the wrapper for a valid reason, ask the user first and state the exact command category.

## Login Verification

Do not infer login state from guessed config paths, common CLI conventions, or a browser window being opened.

Use:

```bash
python scripts/xq_cli_safe.py login-status
```

Only report login success when the JSON response has:

- `ok: true`
- `state: authenticated`

The wrapper checks the current xq-cli config location `~/.xq-opencli/config.json` for the presence of non-empty `baseUrl`/`base_url` and `token`/`access_token` keys without printing their values. Do not read or output the config contents.

If `xq-cli login --browser` is still running or waiting for user authorization, report login as pending. If it exits non-zero or `login-status` returns another state, report the state and repair instruction.

## Failure Handling

Map failures into one of these user-facing states:

- `login_required`: user must run or authorize `xq-cli login`
- `not_installed`: `xq-cli` is not available on PATH or `XQ_CLI_PATH`
- `source_missing`: tender file path does not exist or is unreadable
- `parse_pending`: task exists but parsing has not completed
- `generation_blocked`: xq-cli reports a business precondition such as short requirement or missing bill
- `command_failed`: xq-cli failed for another reason

Do not claim generation is complete just because a trigger command succeeded. Confirm with `status --content`, exported artifact existence, or a CLI result that explicitly reports completion.
