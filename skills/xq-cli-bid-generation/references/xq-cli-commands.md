# xq-cli Command Reference

Prefer the safe wrapper:

```bash
python scripts/xq_cli_safe.py <command> ...
```

The underlying `xq-cli` supports:

- `login`: save account token locally
- `init`: upload files and initialize a task
- `parse-status`: query or wait for parse completion
- `outline`: pre-set task parameters and trigger outline generation
- `write`: charge if needed, enter content phase, and trigger content generation
- `status`: query task status
- `choices`: print selectable outline/export config values
- `wizard`: interactive init -> outline -> write -> export
- `export`: download generated DOCX

## Common Checks

```bash
xq-cli --help
xq-cli choices outline --json
xq-cli choices export --json
```

## Login Checks

After `xq-cli login --browser` exits, prefer the wrapper:

```bash
python scripts/xq_cli_safe.py login-status
```

Do not guess config paths. The wrapper checks `~/.xq-opencli/config.json` and redacts credentials. Only treat login as successful when it prints `ok: true` and `state: authenticated`.

## Typical Raw Commands

Use these only when the wrapper does not cover the needed operation.

```bash
xq-cli init --file /path/to/tender.docx --wait --json
xq-cli parse-status --cid <cid> --uuid <uuid> --wait --json
xq-cli outline --cid <cid> --uuid <uuid> --wait --json
xq-cli write --cid <cid> --type 1 --wait --json
xq-cli status --cid <cid> --content --json
xq-cli export --cid <cid> --out /path/to/output --json
```

## Outline Options

Common option keys accepted by the wrapper:

- `pageScope`, `pageScopeCode`, `page_scope`
- `base`
- `themeStyle`, `theme_style`
- `tableQuantity`, `table_quantity`
- `tableColor`, `table_color`
- `tableStyle`, `table_style`
- `planMode`, `plan_mode`
- `referenceType`, `reference_type`
- `multiBidId`, `multi_bid_id`
- `multiBidType`, `multi_bid_type`
- `epcEngineerType`, `epc_engineer_type`
- `infoImg`, `sceneImg`, `onlineImg`, `mermaidImg`, `knowledgeImg`
- `mermaidStyle`, `mermaid_style`
- `ignoreShortRequirement`, `ignoreMissingBill`

Check current allowed values with:

```bash
python scripts/xq_cli_safe.py choices --scope outline
```

## Export Options

Common option keys accepted by the wrapper:

- `template`
- `layout`
- `tableColor`, `table_color`
- `tableStyle`, `table_style`
- `startIndex`, `start_index`
- `autoNumber`, `auto_number`
- `addMark`, `add_mark`
- `topMargin`, `bottomMargin`, `leftMargin`, `rightMargin`
- `skeletonColor`, `skeleton_color`

Check current allowed values with:

```bash
python scripts/xq_cli_safe.py choices --scope export
```
