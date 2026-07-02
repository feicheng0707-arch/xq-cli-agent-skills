# Technical Scheme Review Rubric

Use this rubric to find and triage issues. Do not assign numeric scores.

The buyer is judging whether the technical scheme can win high technical marks and support confidence in performance. The repair agent needs precise, local, verifiable tasks.

## Review Dimensions

| 维度 | 审查重点 | 常见问题 |
| --- | --- | --- |
| 评分项响应完整性 | 技术/主观评分项及子项是否有实质响应，重点评分项是否容易被评委找到 | 评分点漏响应、只有标题无正文、措施泛化、重点分值章节过薄 |
| 招标需求响应完整性 | 技术要求、服务范围、BOQ、产品/服务清单、附件、图纸、格式、工期是否覆盖 | 清单漏项、附件未响应、服务范围少写、格式/表格缺失 |
| 项目场景贴合度 | 包件、行业、地点、服务对象、施工/服务/供货场景是否一致 | 错项目、错包件、错行业、旧项目或旧地点混入 |
| 关键事实与硬约束一致性 | 工期、日期、数量、人员、设备、型号、单位、标准、技术参数是否与招标一致且正文内部一致 | 工期表冲突、参数错写、数量不一致、旧标准、技术参数自相矛盾 |
| 履约可执行性 | 角色、资源、流程、计划、验收/控制点、风险应对是否能落地 | 只有口号、责任人/频次/记录缺失、资源计划不支撑工期 |
| 招标重点权重与内容组织 | 高分值、关键风险和主清单项是否获得足够深度；低价值内容是否过度扩写 | 关键要求薄弱、低优先级内容过长、章节写作边界混乱 |
| 结构与评审可读性 | 目录、章节层级、标题和正文是否对应，评委能否快速定位响应 | 目录重复、标题与正文不符、章节错位、编号混乱 |
| 专业表达与可信度 | 表达是否具体、专业、可信，是否避免模板、占位、虚假承诺 | 以实际为准、XX/某、空泛套话、不现实承诺 |
| 呈现/图表/格式质量 | 表格、进度图、流程图、图片、附件是否支持本项目且不引入风险 | 图表与正文不一致、图片错场景、暗标暴露、敏感/价格泄漏 |

## Severity Calibration

| 严重程度 | Buyer meaning | Typical conditions | Repair urgency |
| --- | --- | --- | --- |
| 阻断级 | Buyer would not trust the scheme without major correction | Wrong project/package/core scope; severe score-item nonresponse; major BOQ/list omission; construction/service/delivery period clearly violates tender; hard parameter conflict on core item | 必须先修，修后重新审查 |
| 高 | Likely major technical-score loss or material buyer concern | Local but important BOQ/spec conflict; schedule tables and正文 disagree; key technical score item is thin/missing; project-specific scenario partly wrong; repeated critical fact inconsistency | 优先修复，通常需要同步多处正文 |
| 中 | Hurts specificity, consistency, executability, or reviewer confidence | Generic measures; missing responsibility/frequency/records; local section boundary issue; brand/category overgeneralization; unresolved bidder-confirmation fields in non-core tables | 进入修复批次，按影响范围处理 |
| 低 | Presentation or polish issue with limited scoring impact | Minor wording, local formatting, occasional awkward table, non-critical repetition | 可在高/中问题后统一优化 |

Do not use severity as a point deduction. Severity only orders repair work.

## Repair Strategy Calibration

| repair_strategy | Use when | Expected repair behavior |
| --- | --- | --- |
| delete | Content is irrelevant, wrong-project, duplicate, or harmful | Remove the content and verify surrounding section still reads coherently |
| replace | A specific fact, parameter, brand, quantity, date, term, or phrase is wrong | Replace all same-source occurrences with tender-true value; preserve unrelated valid content |
| insert | A required response is missing but an appropriate section already exists | Add a focused subsection/table/paragraph under the existing section |
| rewrite_section | A section is too generic, internally inconsistent, or based on wrong assumptions | Rewrite only that section or subsection using tender evidence |
| sync_global_fact | A fact appears in many places and must be unified | Establish one source of truth and update all conflicting occurrences |
| rebuild_schedule | Progress plan, Gantt/network chart, milestones, or resource schedule is inconsistent | Rebuild schedule from tender period and one coherent work plan; sync text/tables/diagrams |
| restructure_outline | The directory or chapter hierarchy itself carries the wrong scope or misses scoring structure | Adjust outline before rewriting body content |
| move_to_bidder_confirmation_list | A field depends on the bidder's real people, certificates, contracts, facilities, partner names, accounts, or other proof-backed capability and should not be invented in正文 | Remove or neutralize the naked placeholder in正文; create a bidder confirmation item or proof-material checklist entry |
| out_of_scope_for_technical_scheme | Requirement belongs to business/qualification/proof artifact | Do not send to正文 repair; hand off to business/qualification review if needed |

## Placeholder and Confirmation Field Calibration

Do not judge all placeholders with one rule. Classify the field first:

| placeholder_field_type | Meaning | Buyer-visible risk | Expected handling |
| --- | --- | --- | --- |
| `tender_known` | The tender already provides the value or rule, such as service period, site, package, staffing count, hard parameter, required frequency, or assessment rule | Looks like the bid failed to extract or respond to the tender | Replace from tender; usually `高` when tied to hard requirements or scoring |
| `bidder_truth` | The value depends on the bidder's actual capability or proof material, such as names, certificates, social-security records, contracts, training bases, vehicles, proprietary equipment, or partner names | Should not be fabricated, but a naked placeholder makes the submitted document look unfinished | Move to bidder confirmation/proof checklist; severity depends on whether it affects a scored technical section |
| `scheme_commitment` | The bidder can choose a reasonable service commitment, such as frequency, role owner, response path, record form, patrol rule, or escalation standard | "以实际为准" weakens executability and makes the measure hard to evaluate | Rewrite as a conservative role/process/frequency commitment, or mark for bidder confirmation if commercial or operational risk is high |
| `template_residue` | Leftover marker such as "XX", "某", "待推荐", empty parentheses, fake generic name, or copied placeholder with no legitimate confirmation purpose | Signals unfinished or template-generated writing | Delete or rewrite; usually at least `中` when repeated |

Rules:

- A final technical正文 should not expose naked unresolved placeholders that the buyer would read as unfinished, evasive, or nonresponsive.
- Do not force `bidder_truth` placeholders into invented values. The correct repair is a bidder confirmation item, a neutral role-based statement, or a proof-material handoff.
- If a tender-known value is missing, do not excuse it as a placeholder. It is a normal response defect.
- If a scheme-commitment value is needed for evaluability, prefer role/frequency/process language over exact names when names are unavailable.

## Issue Ledger Schema

Use this shape for every material issue:

```json
{
  "issue_id": "I-001",
  "severity": "阻断级 | 高 | 中 | 低",
  "issue_family": "score_item_response | tender_demand_response | package_scope | boq_or_list_adherence | hard_fact_consistency | schedule_consistency | executability | structure | professional_expression | presentation | out_of_scope_for_technical_scheme",
  "review_dimension": "",
  "requirement_id": "",
  "tender_evidence": {
    "anchor": "",
    "excerpt": "",
    "summary": ""
  },
  "bid_evidence": {
    "anchor": "",
    "excerpt": "",
    "summary": ""
  },
  "issue_manifestation": "",
  "why_it_blocks_high_score": "",
  "target_scope": "",
  "occurrence_anchors": [],
  "placeholder_field_type": "tender_known | bidder_truth | scheme_commitment | template_residue | not_placeholder",
  "recommended_handling": "replace_from_tender | move_to_bidder_confirmation_list | rewrite_as_role_or_process_commitment | delete_template_residue | normal_repair",
  "repair_strategy": "delete | replace | insert | rewrite_section | sync_global_fact | rebuild_schedule | restructure_outline | move_to_bidder_confirmation_list | out_of_scope_for_technical_scheme",
  "repair_owner_hint": "upstream_generation_basis | final_document_patch | bidder_confirmation_required | business_or_qualification_artifact",
  "expected_change": "",
  "do_not_change": "",
  "validation_rule": ""
}
```

## Response Matrix Row Schemas

### Score Item Response Row

```json
{
  "score_item_id": "S001",
  "score_item_title": "",
  "score_weight": null,
  "technical_bid_relevance": "technical_scheme_response | business_or_qualification_proof | mixed | not_applicable_to_technical_scheme",
  "tender_excerpt": "",
  "expected_technical_response": "",
  "bid_excerpt_or_absence_basis": "",
  "status": "已覆盖 | 部分覆盖 | 泛化 | 缺失 | 矛盾 | 不属于技术方案正文可修复范围",
  "reasoning": "",
  "related_issue_ids": []
}
```

For score items, usually include subjective/technical items first: service plans, measures, management systems, implementation schemes, assurance measures, training, emergency plans, risk controls, quality controls, organization, staffing plans, and other technical-service scoring content. Classify certificate/social-security/contract proof requirements separately so they do not become technical-scheme repair tasks.

### Tender Demand Response Row

```json
{
  "requirement_id": "R001",
  "requirement_title": "",
  "category": "technical_requirement | service_scope | list_item | BOQ | package_scope | hard_fact | period | format | attachment | drawing",
  "priority": "critical | high | medium | low",
  "tender_excerpt": "",
  "expected_technical_response": "",
  "bid_excerpt_or_absence_basis": "",
  "status": "已覆盖 | 部分覆盖 | 泛化 | 缺失 | 矛盾 | 不属于技术方案正文可修复范围",
  "reasoning": "",
  "related_issue_ids": []
}
```

## Rules

- Judge response substance, not keyword presence.
- Treat a heading with no concrete project-specific measures as a weak or missing response.
- Do not create a repair issue for absent certificates, licenses, contracts, social-security proofs, legal forms, authorization letters, or other proof materials when reviewing a technical-scheme-only artifact, unless the tender explicitly requires those proof materials inside that technical document.
- For mixed scoring items, review only the technical plan/commitment visible in the technical scheme and mark proof-material evaluation as out of scope.
- For placeholders, separate tender-known facts, bidder-truth fields, scheme commitments, and template residue before assigning severity or repair owner.
- Treat unsupported extra content as a precision error. It can lower project fit, content organization, and credibility.
- Treat contradictions in visible personnel quantities, qualifications, dates, schedules, models, standards, BOQ/list items, or diagrams as final-document issues even if proof materials are out of scope.
- Do not flag unequal section length by itself. Flag content weighting only when key tender priorities are thin while low-priority or unsupported content is overdeveloped.
- Keep buyer-facing language observable: "irrelevant old project address appears", not "retrieval pulled old material".
- Do not hide evidence behind anchors alone. Anchors help auditability, but reasons must be readable from the report body.
