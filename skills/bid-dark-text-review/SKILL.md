---
name: bid-dark-text-review
description: 甲方暗标评审视角的技术暗标正文文字内容审查 skill。用于根据招标文件暗标要求和最终技术暗标正文，找出正文文字中可能暴露投标人身份、供应商身份、人员身份、公司痕迹、品牌/业绩/资质等可识别线索的问题清单，并输出可交给正文修复 Agent 的结构化修复任务。只审查正文文字内容，不审查 Word 排版、字体字号、页眉页脚、页码、水印、文件名、文档属性、元数据或下载链路。
---

# Bid Dark Text Review

## Core Frame

Use this skill as a dark-bid text reviewer. The core question is:

> Does the final technical dark-bid body contain any visible textual clue that could let a reviewer identify, infer, or narrow down the bidder?

Only review text that belongs to the submitted technical dark-bid body. Do not score quality, rank vendors, judge generation workflow, or review Word formatting.

This skill produces an issue ledger for a repair agent. It does not rewrite the bid unless the user separately asks for repair.

## Inputs

Use the smallest available set:

- Tender dark-bid requirement, when available.
- Final technical dark-bid body text.
- Bidder/company name and known aliases, when the user provides them.
- Optional known sensitive terms: personnel names, contact details, legal entity names, product brands, proprietary platform names, prior project names, certificate numbers, partner names.

If the tender dark-bid rule is missing, use the conservative default: technical dark-bid body must not contain supplier name, bidder name, logo text, personnel names, contact details, unique organization traces, or any marker that may identify bidder identity.

## Boundaries

Do:

- Find visible text that may reveal bidder identity.
- Separate direct identity exposure from indirect inference clues.
- Judge from a buyer/reviewer perspective: can the reviewer identify, infer, or narrow the bidder?
- Prefer exact short excerpts and stable anchors.
- Group repeated occurrences into one canonical issue.
- Mark uncertain matches as `需人工确认`, not as proven identity leakage.
- Provide repair-ready instructions: delete, replace with neutral wording, anonymize, move to business/qualification file, or ask bidder confirmation.

Do not:

- Review Word layout: font, color, line spacing, margins, cover, catalog, page numbers, table layout, inserted image/table format.
- Review file-layer clues: file name, document properties, author metadata, comments, tracked changes, hidden text, watermark, header/footer, footer page number.
- Treat every occurrence of "我公司/我方/本公司" as severe identity exposure by itself. It is usually a dark-bid style risk, not direct identification, unless combined with unique org facts.
- Invent bidder-truth facts such as real company name, personnel names, certificates, partners, vehicles, addresses, or brands.
- Punish missing business proof unless the tender explicitly requires it inside the technical dark-bid body.

If the provided extraction includes file-layer material such as headers, footers, metadata, comments, or file names, put those in a separate `文件层线索提示` section and state that they belong to a later Word/file-format dark-bid review.

## Workflow

1. **Confirm scope**
   - Identify whether the user wants text-only dark-bid review.
   - If the artifact is not a tender rule but an uploaded bidder document, treat it as the target body, not as a source of dark-bid rules.
   - Ignore files that only contain scoring items unless they help define what text sections should exist.

2. **Extract dark-bid identity rule**
   - Pull exact tender wording about prohibited identity clues.
   - Capture whether the rule says `投标人`, `供应商`, `人员名称`, `徽标`, `可识别身份字符`, or broader `任何标记`.
   - If no rule exists, use the conservative default in Inputs.

3. **Build sensitive term inventory**
   - From user-provided bidder facts: company full names, aliases, abbreviations, brand names, personnel names, phones, addresses, URLs, email domains, certificates, awards, projects, branch names, partner names.
   - From the target body itself: named companies, people, URLs, phones, email addresses, address-like strings, certificate/license numbers, awards, named cases, proprietary platform names, vehicle plates, seals/signature text.
   - From tender context: buyer/project names are not bidder identity and should not be flagged unless reused as a bidder's prior case or private relationship.

4. **Scan and classify identity risks**
   - Load `references/identity-risk-taxonomy.md` for categories and severity calibration.
   - Classify each finding as:
     - `direct_bidder_identity`
     - `person_identity`
     - `contact_or_address`
     - `legal_or_certificate_identifier`
     - `brand_or_proprietary_trace`
     - `past_case_or_award_trace`
     - `organization_process_trace`
     - `neutral_subject_style`
     - `uncertain_possible_match`
     - `file_layer_clue_out_of_scope`
   - Do not over-flag generic role names, generic process names, tender/buyer names, or required product technical terms unless they can identify the bidder.

5. **Decide repair handling**
   - `delete`: remove nonessential identity clue.
   - `replace_neutral`: replace with neutral role/process wording, such as `投标人`, `项目组`, `服务团队`, `供应商`, `承包人`, or `拟派人员`.
   - `anonymize`: keep the capability/commitment but remove the identifying name/code.
   - `move_to_business_bid`: content belongs in明标/business/qualification proof, not technical dark-bid body.
   - `bidder_confirmation_required`: do not fabricate; ask bidder whether the term may remain, must be anonymized, or belongs to another file.
   - `file_layer_review_required`: hand to later Word/file-layer review.

6. **Produce report**
   - Use `references/report-template.md` for formal output.
   - Default to Chinese section names and Chinese table headers.
   - Include short excerpts enough for the reader to understand the issue without opening the file.
   - Include a repair-agent handoff table.

## Severity

- `阻断级`: explicit bidder/supplier legal name, logo text, personnel real names, phone/email/address, seal/signature text, or unique certificate/award/case clue that can identify the bidder under the tender's dark-bid rule.
- `高`: strong indirect identification risk, such as proprietary product/platform name, rare branch/team/warehouse/partner name, public past case/award, or repeated organization traces that narrow the bidder.
- `中`: dark-bid style or inference risk, such as many "我公司/本公司" with internal department/process claims, or named third-party traces that may need bidder confirmation.
- `低`: isolated neutral phrasing issue with low identification value.
- `需人工确认`: possible named entity or alias match where evidence is insufficient.

## Quality Checks

Before finalizing:

- Verify the report only reviews text content, or clearly separates file-layer clues as out of scope.
- Verify every `阻断级` or `高` issue includes an exact excerpt.
- Verify "我公司/我方/本公司" is not automatically escalated unless it creates actual identity inference.
- Verify repair advice never fabricates bidder-specific facts.
- Verify repeated occurrences are grouped.
- Verify the handoff gives target scope, current text, expected change, and validation rule.
