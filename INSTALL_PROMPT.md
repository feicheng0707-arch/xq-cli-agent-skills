# Copy-Paste Install Prompt

Use this when a user wants Codex, Claude Code, WorkBuddy, or another local agent tool to install the XQ CLI bid-generation skill.

## Recommended User Prompt

This mirrors the simple Jimeng-style flow while using the `skills.sh` ecosystem for the skill install.

Replace `{{GITHUB_REPO}}` with the public skill repository, for example `xqyz/xq-cli-agent-skills` after that repository exists.

```text
请帮我安装并登录喜鹊 xq-cli 标书生成能力：先执行 npm install -g @xqyz/xq-cli@0.1.2；再执行 npx skills add {{GITHUB_REPO}} --skill xq-cli-bid-generation --agent codex -g -y 安装 agent skill。如果你不是 Codex，请把 --agent codex 替换成当前 agent 对应的 skills.sh 名称，例如 claude-code；不确定时用 --agent '*'。然后运行 xq-cli --help 确认命令可用，再运行 xq-cli login --browser。登录时如果终端输出 verification_uri、verification URL、授权链接或 user_code，请发给我，并等登录命令结束。登录命令结束后不要猜配置目录，也不要查找 ~/.xq-cli；Codex 请运行 python3 "${CODEX_HOME:-$HOME/.codex}/skills/xq-cli-bid-generation/scripts/xq_cli_safe.py" login-status，Claude Code 请运行 python3 "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills/xq-cli-bid-generation/scripts/xq_cli_safe.py" login-status。只有 login-status 输出 ok: true 且 state: authenticated 时，才告诉我登录成功；否则告诉我 pending/failed 和 repair。不要输出 token、配置文件内容或任何密钥。
```

## Direct Commands

For Codex:

```bash
npm install -g @xqyz/xq-cli@0.1.2
npx skills add {{GITHUB_REPO}} --skill xq-cli-bid-generation --agent codex -g -y
xq-cli --help
xq-cli login --browser
python3 "${CODEX_HOME:-$HOME/.codex}/skills/xq-cli-bid-generation/scripts/xq_cli_safe.py" login-status
```

For Claude Code:

```bash
npm install -g @xqyz/xq-cli@0.1.2
npx skills add {{GITHUB_REPO}} --skill xq-cli-bid-generation --agent claude-code -g -y
xq-cli --help
xq-cli login --browser
python3 "${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills/xq-cli-bid-generation/scripts/xq_cli_safe.py" login-status
```

For all skills.sh-supported agents on the machine:

```bash
npm install -g @xqyz/xq-cli@0.1.2
npx skills add {{GITHUB_REPO}} --skill xq-cli-bid-generation --agent '*' -g -y
xq-cli --help
xq-cli login --browser
```

Then run `scripts/xq_cli_safe.py login-status` from the installed `xq-cli-bid-generation` skill directory for the current agent. Only report login success when it returns `ok: true` and `state: authenticated`.

For WorkBuddy or another agent that is not recognized by `skills.sh`, use the fallback installer with that tool's skill directory:

```bash
npm install -g @xqyz/xq-cli@0.1.2
python3 install_xq_cli_bid_generation.py \
  --archive {{SKILL_ARCHIVE_URL}} \
  --sha256 {{SHA256}} \
  --target /path/to/workbuddy/skills
xq-cli --help
xq-cli login --browser
```

## Repository Shape

The public repository must include:

- `skills.sh.json`
- `skills/xq-cli-bid-generation/SKILL.md`
- `skills/xq-cli-bid-generation/agents/openai.yaml`
- `skills/xq-cli-bid-generation/references/*`
- `skills/xq-cli-bid-generation/scripts/*`

Local validation:

```bash
npx skills add . --list
npx skills add . --skill xq-cli-bid-generation --agent codex -g -y
```

## Fallback Installer

Keep `install.sh` for tools that cannot use `npx skills add` or for a hosted Jimeng-style `curl | bash` quickstart. Replace `{{INSTALL_SH_URL}}` with the hosted `install.sh` URL.

```text
请帮我安装并登录喜鹊 xq-cli 标书生成能力：先执行 curl -fsSL {{INSTALL_SH_URL}} | bash，这会安装 @xqyz/xq-cli@0.1.2 和 agent skill；然后运行 xq-cli --help 确认命令可用，再运行 xq-cli login --browser。登录时如果终端输出 verification_uri、verification URL、授权链接或 user_code，请发给我，并等登录命令结束。登录命令结束后不要猜配置目录，也不要查找 ~/.xq-cli；请运行已安装 skill 里的 scripts/xq_cli_safe.py login-status。只有 login-status 输出 ok: true 且 state: authenticated 时，才告诉我登录成功；否则告诉我 pending/failed 和 repair。不要输出 token、配置文件内容或任何密钥。
```

## Archive Hosting Shape

Host these files under the same public base URL:

- `install.sh`
- `install-skill.sh`
- `install_xq_cli_bid_generation.py`
- `xq-cli-bid-generation-20260701.zip`
- optional `xq-cli-bid-generation-20260701.tar.gz`

Then publish one final install prompt with the real `install.sh` URL.
