# XQ CLI Agent Skills

Portable agent skills for using Xique `xq-cli` from local coding agents such as Codex, Claude Code, and other `skills.sh`-compatible tools.

## Quick Install

For Codex:

```bash
npm install -g @xqyz/xq-cli@0.1.2
npx skills add feicheng0707-arch/xq-cli-agent-skills --skill xq-cli-bid-generation --agent codex -g -y
xq-cli --help
xq-cli login --browser
```

For Claude Code:

```bash
npm install -g @xqyz/xq-cli@0.1.2
npx skills add feicheng0707-arch/xq-cli-agent-skills --skill xq-cli-bid-generation --agent claude-code -g -y
xq-cli --help
xq-cli login --browser
```

For all `skills.sh`-supported agents:

```bash
npm install -g @xqyz/xq-cli@0.1.2
npx skills add feicheng0707-arch/xq-cli-agent-skills --skill xq-cli-bid-generation --agent '*' -g -y
xq-cli --help
xq-cli login --browser
```

## Copy-Paste Agent Prompt

```text
请帮我安装并登录喜鹊 xq-cli 标书生成能力：先执行 npm install -g @xqyz/xq-cli@0.1.2；再执行 npx skills add feicheng0707-arch/xq-cli-agent-skills --skill xq-cli-bid-generation --agent codex -g -y 安装 agent skill。如果你不是 Codex，请把 --agent codex 替换成当前 agent 对应的 skills.sh 名称，例如 claude-code；不确定时用 --agent '*'。然后运行 xq-cli --help 确认命令可用，再运行 xq-cli login --browser。登录时如果终端输出 verification_uri、verification URL、授权链接或 user_code，请发给我，并等登录命令结束后告诉我 skill 安装校验和 xq-cli 登录是否成功。不要输出 token、配置文件内容或任何密钥。
```

## Included Skill

- `xq-cli-bid-generation`: operate Xique `xq-cli` for bid-generation workflows, including login/runtime checks, tender upload, parse status, outline generation, content generation, status inspection, and DOCX export.

## Validate

```bash
npx skills add . --list
python3 skills/xq-cli-bid-generation/scripts/quick_validate.py skills/xq-cli-bid-generation
```

## Safety

The skill is an external user-installed agent skill. It does not assume any Xique backend repository exists locally. It avoids exposing tokens, saved config contents, raw headers, or private local paths in user-facing summaries.
