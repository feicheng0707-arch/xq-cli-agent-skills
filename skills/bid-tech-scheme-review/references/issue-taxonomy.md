# Customer Feedback Issue Taxonomy

Use this taxonomy to make sure the review covers the customer-visible final-document problems seen in `喜鹊标书AI问题记录表.xlsx`.

This is not a process-debug taxonomy and not a scoring benchmark. Convert internal causes into buyer-visible final-document findings, then place them into the repair-ready issue ledger.

Map issue families to the current review dimensions:

- 评分项理解、技术/主观评分项响应、大纲融合 -> 评分项响应完整性.
- 招标需求、工程量清单、产品/服务清单、附件、图纸、包件范围 -> 招标需求响应完整性 and 项目场景贴合度.
- 工期、参数、数量、人员、型号、标准、横道图/网络图 -> 关键事实与硬约束一致性.
- 人员、资源、流程、SLA、安装调试、质保、验收和风险闭环 -> 履约可执行性.
- 章节边界、重点错配、低价值内容过度扩写 -> 招标重点权重与内容组织.
- 目录、标题、编号、评审定位 -> 结构与评审可读性.
- 重复、占位符、泛化表达、过期规范 -> 专业表达与可信度.
- 图片、表格、流程图、暗标暴露、价格或敏感信息泄漏 -> 呈现/图表/格式质量.

Then apply the procurement-type overlay from `procurement-type-rubrics.md`: 工程 issues are judged around construction organization and schedule-resource closure; 服务 issues around staffing, shifts, SLA, process, and assessment; 货物 issues around parameter/list response, supply, installation, commissioning, warranty, and compatibility.

## In-Scope Final-Document Issues

| 问题族 | xlsx 问题类型覆盖 | 通常影响的审查维度 | 甲方可见判断 |
| --- | --- | --- | --- |
| 评分项响应 | 评分理解问题, 评分提取问题 when it appears as missing/wrong final response, 评分理解, 评分理解、大纲修改遵循, 融合评分目录效果不佳, 目录融合问题 | 评分项响应完整性; 招标重点权重与内容组织; 结构与评审可读性 | 技术/主观评分项、子项、顺序或层级没有在最终目录和正文中得到实质响应。 |
| 招标需求与项目范围覆盖 | 需求提取问题 when visible as final omission, 需求理解问题, 需求响应度问题, 未准确响应需求, 项目背景提取问题 | 招标需求响应完整性; 项目场景贴合度; 招标重点权重与内容组织 | 最终方案遗漏或误解项目背景、服务范围、技术范围、地点、对象或主要需求。 |
| 包件/标段隔离 | 多包需求拆分问题, 多包目录要求未拆分, selected package mixed with other lots | 项目场景贴合度; 关键事实与硬约束一致性 | 最终方案混入其他包件/标段内容，或未能围绕所选包件单独成文。 |
| 工程量清单、产品清单、服务清单遵循 | 清单遵循问题, 工程量清单遵循, 工程量清单没有遵循, 工程量清单提取问题 when visible as final omission, 清单识别, 清单提取问题, 未遵循清单工艺要求, 货物清单响应不全 | 招标需求响应完整性; 关键事实与硬约束一致性; 项目场景贴合度 | 最终方案漏清单项、发明清单外项目、数量/规格/工艺错误，或未按要求逐项响应。 |
| 硬事实与技术参数 | 工期遵循问题, 工期时间错误, 工期提取问题 when visible as missing/wrong final period, 工期理解问题, 工期安排不统一, 工期内部安排不统一, 人员数量没有遵循, 人员安排不一致, 型号识别错误, 审查问题 when final bid shows wrong thresholds/personnel facts | 关键事实与硬约束一致性; 专业表达与可信度 | 日期、周期、数量、人员、型号、阈值、单位、项目名、地点或技术参数与招标文件或正文内部相矛盾。 |
| 进度图、网络图、横道图和流程图一致性 | 横道图和正文工期对不上, 正文和横道图工期不能对应, 生成流程图问题, 生成流程图进度问题, 网络图优化需求 when final diagram is present | 关键事实与硬约束一致性; 结构与评审可读性; 呈现/图表/格式质量 | 正文、表格、横道图、网络图或流程图相互冲突，或无法支撑甲方理解履约计划。 |
| 目录与大纲结构 | 目录要求提取, 特殊目录要求识别错误, 技术格式提取问题, 响应文件格式提取问题 when the technical format is visible, 目录重复问题, 大纲结构不稳定, 大纲与目录不一致, 大纲、目录规划不合理, 标题编号显示问题, 标题内容不符 | 结构与评审可读性; 评分项响应完整性; 呈现/图表/格式质量 | 技术目录/格式缺失、重复、扁平、编号混乱，或标题与正文不匹配，影响评委定位响应。 |
| 章节边界与内容重点 | 内容超出章节主题边界, 超出小节写作边界, 超出章节写作边界, 超出本节写作范围, 篇幅不匀问题, 篇幅页数分布不均匀 | 招标重点权重与内容组织; 结构与评审可读性; 专业表达与可信度 | 某章节写成全项目总述、混入其他模块，或关键要求薄弱而低优先级内容过度扩写。不要按章节等长判断。 |
| 整体篇幅适配 | 篇幅过少问题, 篇幅过长问题, 篇幅不准 | 招标重点权重与内容组织; 结构与评审可读性; 呈现/图表/格式质量 | 最终方案明显达不到用户选择的篇幅目标或招标深度预期；判断重点是重要要求是否获得足够深度。 |
| 项目/行业/场景贴合 | 垂直领域写作角度问题, 写作角度问题, 正文内容和需求无关, 内容偏离主题, 正文内容不合理, 内容不合理, 内容不专业 | 项目场景贴合度; 专业表达与可信度 | 最终方案使用错误行业、错误服务阶段、错误施工/服务/供货逻辑、错误甲乙方视角，或读起来像另一个项目。 |
| 复用或引用材料质量 | 知识库引用效果, 图片库引用效果, 图库引用问题 when visible in final artifact | 项目场景贴合度; 专业表达与可信度; 呈现/图表/格式质量 | 最终方案可见地出现无关历史项目地点、公司名、案例、图片或证明材料。报告中不要提内部知识库机制。 |
| 图片、图表和版式适配 | 图片场景不匹配, 图片生成不匀, 生成旧版本带颜色图片, 表格包围样式适应 | 呈现/图表/格式质量; 项目场景贴合度; 结构与评审可读性 | 图片、表格、流程图和视觉样式与项目不匹配，包含无关主体/场景，或在技术标中制造暗标、敏感信息、可读性风险。 |
| 重复、占位和泛化表达 | 正文内容重复问题, 内容重复问题, repeated boilerplate, unresolved placeholders such as XX or 以实际为准 | 专业表达与可信度; 结构与评审可读性; 呈现/图表/格式质量 | 最终方案重复、空泛、占位符未清理，或缺乏项目化措施，导致甲方难以信任履约能力。审查占位符时必须区分招标已给定字段、投标方真实能力字段、方案策略承诺字段和模板残留。 |
| 敏感或不适当内容泄漏 | 正文体现价格, irrelevant license plates or private identifiers, business/pricing content leaking into technical scheme | 呈现/图表/格式质量; 专业表达与可信度; 关键事实与硬约束一致性 | 技术方案中出现不应出现的价格、商务信息、敏感标识或无关私人/车辆信息。 |
| 标准规范适用性 | 规范标准过期, outdated or wrong standards | 关键事实与硬约束一致性; 专业表达与可信度 | 引用标准、规范或法规过期、适用领域错误，或与招标文件指定依据冲突。 |
| 用户编辑/自定义要求 | 修改大纲未严格遵循, 修改大纲不遵循, user-selected dark-bid/no-image/format/length constraints when known | 结构与评审可读性; 评分项响应完整性; 呈现/图表/格式质量 | 最终方案没有遵循可见的用户自定义大纲、格式、暗标、图片或篇幅约束。 |

## Out-of-Scope For Technical-Scheme Issue Review

Do not list these as technical-scheme正文 repair issues:

| 问题类型 | xlsx 示例 | 处理方式 |
| --- | --- | --- |
| 生成链路稳定性 | 生成卡住, 正文为空, 下载失败, 大纲一直加载, 状态卡住 | 排除。这些属于产品链路稳定性，不属于最终技术方案正文质量。 |
| 计费、登录、账号、体验卡、发票、套餐 | 喜币消耗, 重复付款, 体验卡, 登录, 发票, 充值 | 排除。 |
| 产品 UX 或生成后编辑能力 | 生成后改字数, 局部修改, 批量删除图片库, 消费记录入口 | 排除；除非最终文档本身可见地违反已知输出约束。 |
| 商务标或资格证明材料 | licenses, certificates, social security proofs, contracts, authorization forms, legal representative forms | 不作为技术方案正文问题；除非招标文件明确要求这些证明材料进入本次审查的技术方案正文。 |
| 隐藏的过程提取失败 | "未提取到" only known from workflow state, without observable final-bid omission | 只有当最终正文实际遗漏、矛盾或错置要求时，才转为正文问题。 |
| 审查报告产品缺陷 | 审查漏废标项没查出来, empty review report, duplicate review billing | 排除；除非当前审查对象就是该报告，而不是技术方案正文。 |

## Severity Hints

- Wrong package, wrong industry, wrong core project scope, or large amounts of another project: mark as `阻断级`.
- Many technical/subjective scoring requirements or major technical requirements missing: mark as `阻断级` or `高`, depending on scope.
- Core BOQ/list/spec/period/personnel facts that conflict with the tender: mark as `阻断级` when they affect contract substance; otherwise `高`.
- Reviewable but placeholder-heavy, locally off-topic, locally repetitive, or visually mismatched: usually `中` or `高` if it affects a key scoring section.
- Placeholder severity depends on field type: tender-known hard facts are normal response defects; bidder-truth fields should be moved to confirmation/proof checklists rather than fabricated; scheme commitments should usually be rewritten as role/process/frequency commitments; template residue should be deleted.
- A single local wording or minor format defect is usually `低`.

Severity orders repair priority. It is not a point deduction and does not imply a numeric grade.

## Exact Xlsx Type Coverage Checklist

Use this list when auditing whether the review skill still covers all customer-feedback issue types. Types that are process-only are intentionally excluded from final technical-scheme issue review.

| 审查问题族 | exact xlsx issue types |
| --- | --- |
| 评分项响应 | 评分理解问题; 评分提取问题 when visible as missing/wrong final response; 评分理解; 评分理解、大纲修改遵循; 融合评分目录效果不佳; 目录融合问题 |
| 招标需求与项目范围覆盖 | 需求提取问题 when visible as final omission; 需求理解问题; 需求响应度问题; 未准确响应需求; 项目背景提取问题 |
| 包件/标段隔离 | 多包需求拆分问题 |
| 工程量清单、产品清单、服务清单遵循 | 清单遵循问题; 工程量清单遵循; 工程量清单没有遵循; 工程量清单提取问题 when visible as final omission; 清单识别; 清单提取问题; 未遵循清单工艺要求; 货物清单响应不全; 工期，清单遵循问题， |
| 硬事实与技术参数 | 工期遵循问题; 工期时间错误; 工期提取问题 when visible as wrong/missing final period; 工期理解问题; 工期安排不统一; 工期内部安排不统一; 人员数量没有遵循; 人员安排不一致; 型号识别错误，施工逻辑错误; 审查问题 when the final bid visibly contains wrong thresholds, age/personnel mapping, or hard facts |
| 进度图、网络图、横道图和流程图一致性 | 横道图和正文工期对不上; 正文和横道图工期不能对应; 生成流程图问题; 生成流程图进度问题 |
| 目录与大纲结构 | 响应文件格式提取问题 when it concerns technical/service format; 响应格式要求提取; 响应格式要求提取问题; 目录要求提取; 特殊目录要求识别错误; 技术格式提取问题; 目录重复问题; 大纲结构不稳定; 大纲与目录不一致; 大纲、目录规划不合理; 标题编号显示问题; 标题内容不符 |
| 章节边界与内容重点 | 内容超出章节主题边界; 超出小节写作边界; 超出章节写作边界; 超出本节写作范围; 篇幅不匀问题; 篇幅页数分布不均匀 |
| 整体篇幅适配 | 篇幅过少问题; 篇幅过长问题; 篇幅不准 |
| 项目/行业/场景贴合 | 垂直领域写作角度问题; 写作角度问题; 正文内容和需求无关; 正文内容不合理; 内容不合理; 内容不专业; 内容偏离主题 |
| 复用或引用材料质量 | 知识库引用效果 when visible as irrelevant final material or known user-reference nonuse; 图片库引用效果; 图库引用问题 |
| 图片、图表和版式适配 | 图片场景不匹配; 图片生成不匀; 表格包围样式适应; old or mismatched flowchart/image assets visible in final document |
| 重复、占位和泛化表达 | 正文内容重复问题; 内容重复问题 when visible in the generated bid |
| 敏感或不适当内容泄漏 | 正文体现价格; irrelevant license plates or private identifiers visible in final technical scheme |
| 标准规范适用性 | 规范标准过期 |
| 用户编辑/自定义要求 | 修改大纲未严格遵循; 修改大纲不遵循 |
| 排除的流程/产品问题 | bug; 审查漏废标项没查出来 unless the final technical document itself is being reviewed; generation stuck/empty/download/payment/login/account/trial/invoice/post-generation editing feature requests |
