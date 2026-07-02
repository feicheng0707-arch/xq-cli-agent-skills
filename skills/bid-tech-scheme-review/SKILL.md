---
name: bid-tech-scheme-review
description: 甲方审标视角的技术标技术方案质量审查 skill。用于根据招标文件、附件和最终生成的技术方案正文，找出所有会影响技术标高分、合规性、可信度和可投性的正文质量问题，并输出可交给正文修复 Agent 使用的结构化问题列表。只审查最终技术方案正文，不打总分、不做竞品排名、不评生成链路、耗时、下载、卡住、过程提取数据或内部知识库行为。
---

# Bid Tech Quality Review

## Core Frame

Use this skill as a buyer-side technical-bid reviewer and issue finder, not as a scoring benchmark.

Only judge the final technical-scheme artifact. Assume the full generated document exists. Do not score generation success rate, latency, download behavior, task status, internal extraction traces, prompts, knowledge-base usage, or any process data unavailable from the final document.

The review answers one question:

> What visible quality issues in this technical scheme would prevent the bidder from getting a high technical score or being trusted by the buyer, and what precise repair task should be handed to a correction agent?

Do not output a 100-point score, final score, redline cap, vendor ranking, or winner/loser conclusion. If the user asks for comparison or scoring, explain that this skill produces a review issue ledger; use `$bid-tech-quality-benchmark` for numeric benchmark/comparison work.

## Inputs

Use the smallest complete set:

- Tender document and all attachments relevant to the technical scheme: score method, technical requirements, BOQ, service list, product list, drawings, brand table, format requirements, package/lot files.
- User-selected configuration when available: package/lot, bid section, page/length target, dark-bid requirement, image/layout option, selected response mode.
- Final generated technical scheme or technical bid body.

If package/lot selection is essential and unknowable, ask before final review. If user configuration is missing, infer only from the tender and mark assumptions.

## Boundaries

Do:

- Build an independent tender requirement inventory from the tender and attachments.
- Review only buyer-visible final-document behavior.
- Use buyer-visible language: "irrelevant historical project appears", not "knowledge base citation failed".
- Require evidence anchors for important findings.
- Include enough short source excerpts in important findings so the reader can understand the defect without reopening the tender or bid.
- Separate technical-scheme obligations from business bid, qualification, and proof attachments.
- Mark proof-only business/qualification requirements as `不属于技术方案正文可修复范围` unless the tender explicitly requires them inside the technical方案正文 being reviewed.
- Produce a repair-ready issue ledger with clear target scope, expected correction, repair strategy, and post-repair validation.

Do not:

- Give a numeric score, redline cap, score band, or ranking.
- Reward or punish hidden workflow steps.
- Treat generated outline quality as separate from final document quality unless the outline appears in the final document.
- Use internal labels such as prompt, trace, extractor, retrieval, knowledge base, vector search, or model failure in the user-facing report.
- Let fluent writing hide wrong package, wrong project scope, hard-requirement violations, or major score-item nonresponse.
- Treat absence of certificates, licenses, contracts, social-security records, authorization letters, or scanned proof materials as a technical-scheme正文 issue unless the tender places those proof materials inside the evaluated technical document.

## Workflow

1. **Confirm scope**
   - Confirm this is a technical-scheme final-document review.
   - Exclude business bid, pricing, qualification proof, runtime stability, and UX issues unless they visibly appear inside the final technical scheme.
   - If the artifact is only a technical scheme, mark objective proof-only scoring items as out of scope rather than as正文缺陷.

2. **Build tender requirement inventory**
   - Extract project profile: project name, buyer, package/lot, domain, service or construction scope, delivery site, service period or construction period.
   - Classify procurement type as `工程`, `服务`, `货物`, or `混合`; if mixed, identify the dominant technical-scheme review logic and secondary constraints.
   - Extract technical score requirements by hierarchy and weight. Classify each as `technical_scheme_response`, `business_or_qualification_proof`, `mixed`, or `not_applicable_to_technical_scheme`.
   - Extract technical/service requirements, BOQ/product/service lists, attachments, drawings, brand tables, formats, schedules, and hard facts.
   - Mark each requirement as `critical`, `high`, `medium`, or `low` from the buyer perspective.
   - Load `references/issue-taxonomy.md` when reviewing a real bid or auditing coverage against customer feedback issue families.
   - Load `references/procurement-type-rubrics.md` for the procurement-type overlay.
   - Load `references/rubric.md` for review dimensions, severity calibration, and repairability rules. Use it for issue triage only, not scoring.

3. **Run core compliance response analysis**
   - Separately analyze the two compliance foundations:
     1. `score_item_response`: subjective/technical score items such as plans, measures, systems, procedures, implementation方案, assurance措施, management制度, training, risk control, emergency plans, and similar technical-service scoring content.
     2. `tender_demand_response`: tender technical/service requirements, procurement demand, service scope, BOQ/product/service lists, package scope, hard facts, formats, schedules, drawings, and attachments that the technical scheme should address.
   - Produce two response matrices:
     - requirement/score item
     - tender excerpt
     - expected technical-scheme response
     - bid excerpt or absence basis
     - response status: `已覆盖 | 部分覆盖 | 泛化 | 缺失 | 矛盾 | 不属于技术方案正文可修复范围`
     - reasoning
     - resulting issue ids, if any
   - Treat these matrices as evidence sources for the issue ledger.

4. **Segment the final technical scheme**
   - Identify table of contents, section hierarchy, body sections, tables, schedules, charts, images, appendices, and repeated material.
   - For very long documents, chunk by section and maintain stable section anchors.
   - When an issue appears repeatedly, create one canonical issue with multiple occurrence anchors rather than many duplicate findings.

5. **Classify unresolved placeholders and bidder-confirmation fields**
   - Do not treat every placeholder as the same defect. First classify each unresolved field by what it represents:
     - `tender_known`: the tender already gives the value, such as period, site, package, list item, service standard, staffing count, hard parameter, or required response frequency.
     - `bidder_truth`: the value depends on the bidder's real capability or proof material, such as personnel names, certificates, social-security records, contracts, training-base name, vehicle plates, accounts, proprietary equipment, or actual partner names.
     - `scheme_commitment`: the value is a technical-service commitment the bidder may reasonably choose, such as inspection frequency, patrol route rule, training cadence, reporting path, escalation role, response time, record form, or acceptance checkpoint.
     - `template_residue`: the value is a leftover template marker, empty bracket, fake name, "XX", "某", "待推荐", or "以实际为准" that does not carry a defensible confirmation purpose.
   - Judge final-document risk from a buyer perspective:
     - `tender_known` placeholders are AI/document quality defects; replace from the tender or mark the response as contradictory/missing.
     - `bidder_truth` placeholders must not be fabricated. If they appear in final正文, mark as a submission-readiness risk and move them to a bidder confirmation list or proof-material checklist.
     - `scheme_commitment` placeholders weaken executability. Replace them with conservative role/frequency/process commitments when the tender allows; otherwise mark them for bidder confirmation before submission.
     - `template_residue` should be deleted or rewritten because it signals an unfinished document.
   - For each material placeholder cluster, record `placeholder_field_type`, `repair_owner_hint`, and `recommended_handling`: `replace_from_tender | move_to_bidder_confirmation_list | rewrite_as_role_or_process_commitment | delete_template_residue`.
   - Do not require all placeholders to become fabricated concrete values. Require that the final technical正文 contains no naked unresolved placeholder that a buyer would read as unfinished, evasive, or nonresponsive.

6. **Generate issue ledger**
   - Convert every material defect into a repair-ready issue.
   - Each issue must include tender evidence, bid evidence, expected correction, target scope, suggested repair strategy, and validation rule.
   - Use severity labels, not point deductions:
     - `阻断级`: wrong project/package/core scenario, major nonresponse, hard facts that make the scheme untrustworthy.
     - `高`: likely major technical score loss or material buyer concern.
     - `中`: hurts specificity, consistency, executability, or reviewer confidence but is locally repairable.
     - `低`: presentation or wording polish with limited scoring impact.
   - Use repair strategy labels:
     - `delete`: remove irrelevant/wrong content.
     - `replace`: deterministic replacement or parameter correction.
     - `insert`: add missing response under an existing suitable section.
     - `rewrite_section`: rewrite a target section or subsection.
     - `sync_global_fact`: unify a repeated fact across the document.
     - `rebuild_schedule`: rebuild schedule/table/Gantt/network logic from one source of truth.
     - `restructure_outline`: adjust directory/section structure before rewriting正文.
     - `move_to_bidder_confirmation_list`: remove a bidder-truth field from正文 and hand it to the bidder for truthful completion before submission.
     - `out_of_scope_for_technical_scheme`: leave to business/qualification artifact, not a正文 repair.

7. **Prepare repair-agent handoff**
   - For each repairable issue, provide a compact handoff payload:
     - `issue_id`
     - `issue_family`
     - `severity`
     - `target_scope`
     - `occurrence_anchors`
     - `tender_truth`
     - `current_wrong_text`
     - `expected_change`
     - `repair_strategy`
     - `do_not_change`
     - `validation_rule`
   - If the issue requires upstream task/process-data correction rather than final DOCX patching, mark `repair_owner_hint` as `upstream_generation_basis`.
   - If the issue can be repaired in the final document only, mark `repair_owner_hint` as `final_document_patch`.
   - If the issue requires truthful bidder input, mark `repair_owner_hint` as `bidder_confirmation_required`; the repair agent may only move, label, or bracket the field, not invent a value.

8. **Produce report**
   - Use `references/report-template.md` for formal reports.
   - Lead with `质量问题总览` and `修复优先级`.
   - Include `核心合规响应分析` after the issue overview so the repair team can see why each issue exists.
   - Include `待确认字段与占位符分析` when unresolved placeholders appear in the final document.
   - Do not include numeric scoring tables.
   - In user-facing Markdown reports, use Chinese section names and Chinese table column headers. Keep English enum/schema names only inside handoff payload tables when useful for downstream automation.

## Output Contract

Default output:

```markdown
## 技术方案质量审查

- 评估文件：
- 招标文件：
- 选择包件/标段：
- 采购类型：
- 适用子标准：
- 审查结论：
- 是否适合直接投标：
- 需要修复后再投的原因：

## 质量问题总览

| 严重程度 | 问题数量 | 主要问题族 | 对技术分/甲方信心的影响 | 修复优先级 |
| --- | ---: | --- | --- | --- |

## 修复优先级

| 优先级 | 问题ID | 问题族 | 目标范围 | 建议修复策略 | 修复后验证 |
| ---: | --- | --- | --- | --- | --- |

## 质量问题列表

| 问题ID | 严重程度 | 问题族 | 问题表现 | 招标文件证据 | 技术方案证据 | 为什么影响高分 | 目标范围 | 修复建议 | 验证规则 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 待确认字段与占位符分析

| 字段类型 | 代表性位置 | 当前文本 | 审查判断 | 推荐处理 | 修复责任 | 关联问题ID |
| --- | --- | --- | --- | --- | --- | --- |

## 核心合规响应分析

### 评分项响应完整性

| 评分项 | 招标文件摘录 | 期望的技术方案响应 | 技术方案摘录/缺失依据 | 响应状态 | 判断理由 | 关联问题ID |
| --- | --- | --- | --- | --- | --- | --- |

### 招标需求响应完整性

| 招标需求 | 招标文件摘录 | 期望的技术方案响应 | 技术方案摘录/缺失依据 | 响应状态 | 判断理由 | 关联问题ID |
| --- | --- | --- | --- | --- | --- | --- |

## 修复 Agent 交接清单

| issue_id | repair_owner_hint | repair_strategy | target_scope | occurrence_anchors | tender_truth | current_wrong_text | expected_change | do_not_change | validation_rule |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## 不属于技术方案正文可修复范围

| 要求 | 招标文件依据 | 为什么不纳入正文修复 | 建议处理 |
| --- | --- | --- | --- |

## 复查清单

- ...
```

## Quality Checks

Before finalizing:

- Verify no numeric score, score band, redline cap, vendor ranking, or winner/loser conclusion is included.
- Verify every high or blocking issue has both tender evidence and bid evidence with short quoted excerpts, or explicitly says the bid evidence is absent.
- Verify the issue table is self-contained: a reader should understand the problematic paragraph and issue manifestation without opening the source files.
- Verify `核心合规响应分析` includes separate matrices for score-item response and tender-demand response.
- Verify unresolved placeholders are classified into `tender_known`, `bidder_truth`, `scheme_commitment`, or `template_residue`, and that bidder-truth fields are not fabricated.
- Verify proof-only business/qualification items are not listed as technical-scheme正文 repair tasks.
- Verify wrong package, wrong core project scope, hard requirement violations, and major score-item nonresponse are surfaced as high or blocking issues.
- Verify no internal process terms leak into the buyer-facing report.
- Verify the report states the procurement type and applies the right 工程/服务/货物 overlay.
- Verify each repairable issue has target scope, repair strategy, and validation rule.
- Verify repeated occurrences are grouped under a canonical issue with all key anchors.
