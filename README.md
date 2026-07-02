# Xique Agent Skills

Portable agent skills for using Xique bid tooling and review workflows from local coding agents such as Codex, Claude Code, and other `skills.sh`-compatible tools.

## Quick Install

Install one skill:

```bash
npx skills add feicheng0707-arch/xq-cli-agent-skills --skill xq-cli-bid-generation --agent codex -g -y
npx skills add feicheng0707-arch/xq-cli-agent-skills --skill bid-tech-scheme-review --agent codex -g -y
npx skills add feicheng0707-arch/xq-cli-agent-skills --skill bid-dark-text-review --agent codex -g -y
```

Install the two review agents together:

```bash
npx skills add feicheng0707-arch/xq-cli-agent-skills --skill bid-tech-scheme-review --skill bid-dark-text-review --agent codex -g -y
```

For Claude Code, replace `--agent codex` with `--agent claude-code`. For all supported agents, use `--agent '*'`.

## XQ CLI Quick Install

For Codex:

```bash
npm install -g @xqyz/xq-cli@0.1.2
npx skills add feicheng0707-arch/xq-cli-agent-skills --skill xq-cli-bid-generation --agent codex -g -y
xq-cli --help
xq-cli login --browser
python3 "${CODEX_HOME:-$HOME/.codex}/skills/xq-cli-bid-generation/scripts/xq_cli_safe.py" login-status
```

For Claude Code:

```bash
npm install -g @xqyz/xq-cli@0.1.2
npx skills add feicheng0707-arch/xq-cli-agent-skills --skill xq-cli-bid-generation --agent claude-code -g -y
xq-cli --help
xq-cli login --browser
python3 "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills/xq-cli-bid-generation/scripts/xq_cli_safe.py" login-status
```

For all `skills.sh`-supported agents:

```bash
npm install -g @xqyz/xq-cli@0.1.2
npx skills add feicheng0707-arch/xq-cli-agent-skills --skill xq-cli-bid-generation --agent '*' -g -y
xq-cli --help
xq-cli login --browser
```

Then run `scripts/xq_cli_safe.py login-status` from the installed `xq-cli-bid-generation` skill directory for the current agent. Only report login success when it returns `ok: true` and `state: authenticated`.

## Copy-Paste Agent Prompt

```text
请帮我安装并登录喜鹊 xq-cli 标书生成能力：先执行 npm install -g @xqyz/xq-cli@0.1.2；再执行 npx skills add feicheng0707-arch/xq-cli-agent-skills --skill xq-cli-bid-generation --agent codex -g -y 安装 agent skill。如果你不是 Codex，请把 --agent codex 替换成当前 agent 对应的 skills.sh 名称，例如 claude-code；不确定时用 --agent '*'。然后运行 xq-cli --help 确认命令可用，再运行 xq-cli login --browser。登录时如果终端输出 verification_uri、verification URL、授权链接或 user_code，请发给我，并等登录命令结束。登录命令结束后不要猜配置目录，也不要查找 ~/.xq-cli；Codex 请运行 python3 "${CODEX_HOME:-$HOME/.codex}/skills/xq-cli-bid-generation/scripts/xq_cli_safe.py" login-status，Claude Code 请运行 python3 "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills/xq-cli-bid-generation/scripts/xq_cli_safe.py" login-status。只有 login-status 输出 ok: true 且 state: authenticated 时，才告诉我登录成功；否则告诉我 pending/failed 和 repair。不要输出 token、配置文件内容或任何密钥。
```

## Included Skills

- `xq-cli-bid-generation`: operate Xique `xq-cli` for bid-generation workflows, including login/runtime checks, tender upload, parse status, outline generation, content generation, status inspection, and DOCX export.
- `bid-tech-scheme-review`: review a final technical scheme body against tender documents from a buyer-side perspective, then output a repair-ready issue ledger without numeric scoring.
- `bid-dark-text-review`: review technical dark-bid body text for bidder identity exposure risks and output repair-agent handoff tasks.

## Validate

```bash
npx skills add . --list
npx skills add . --skill bid-tech-scheme-review --skill bid-dark-text-review --agent codex --copy -y
python3 skills/xq-cli-bid-generation/scripts/quick_validate.py skills/xq-cli-bid-generation
```

## Safety

These are external user-installed agent skills. They do not assume any Xique backend repository exists locally. The xq-cli skill avoids exposing tokens, saved config contents, raw headers, or private local paths in user-facing summaries. The review skills are report-only workflows and should not fabricate bidder-specific facts.
