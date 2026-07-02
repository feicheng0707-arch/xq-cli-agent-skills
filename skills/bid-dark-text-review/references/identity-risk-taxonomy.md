# 暗标正文身份暴露分类

Use this taxonomy when reviewing technical dark-bid body text.

## 问题分类

| 分类 | 判断标准 | 常见表现 | 默认严重度 | 推荐处理 |
| --- | --- | --- | --- | --- |
| `direct_bidder_identity` | 直接出现投标人/供应商/关联法人的名称或简称 | 公司全称、简称、集团名、分公司名、供应商名称、盖章文字 | 阻断级 | `delete` 或 `replace_neutral` |
| `person_identity` | 出现自然人姓名或可关联到投标人的人员身份 | 项目经理张三、法定代表人、联系人、授权代表、讲师姓名 | 阻断级 | `anonymize` 或 `move_to_business_bid` |
| `contact_or_address` | 出现联系或定位信息 | 电话、手机号、邮箱、网址、地址、办公地点、服务网点、邮编 | 阻断级 | `delete` 或 `move_to_business_bid` |
| `legal_or_certificate_identifier` | 出现可检索主体身份的证照编号或法律标识 | 统一社会信用代码、许可证编号、资质证书编号、专利号、软著号、银行账户 | 高/阻断级 | `move_to_business_bid` 或 `anonymize` |
| `brand_or_proprietary_trace` | 出现能指向某供应商的品牌、产品、平台、系统、商标、特有方法名 | 自有平台名、品牌口号、商标、专有工具、厂家授权品牌 | 中/高 | `bidder_confirmation_required` 或 `anonymize` |
| `past_case_or_award_trace` | 出现可公开检索并关联投标人的业绩、奖项、客户或项目 | 某客户项目、获奖名称、典型案例、合作院校/医院/政府部门 | 高 | `move_to_business_bid` 或 `anonymize` |
| `organization_process_trace` | 出现内部组织结构或流程痕迹，单独不一定识别，但可叠加推断 | 本公司仓储部、工程部、某地库房、某专项团队、车辆/仓库/物流安排 | 中 | `replace_neutral` |
| `neutral_subject_style` | 使用第一人称主体但无唯一识别信息 | 我公司、我方、本公司、我单位 | 低/中 | `replace_neutral` |
| `uncertain_possible_match` | 可能是主体、人员、品牌或项目名，但无法确认是否指向投标人 | 生僻中文名、缩写、英文词、地名+公司词、疑似品牌 | 需人工确认 | `bidder_confirmation_required` |
| `file_layer_clue_out_of_scope` | 非正文文字内容但可能暴露身份 | 文件名、作者、lastModifiedBy、页眉页脚、水印、批注、修订记录 | 不纳入正文问题 | `file_layer_review_required` |

## 不应误报

- 招标人、采购人、项目名称、采购地点、招标文件规定的服务对象。
- 法规、标准、规范、国家/行业通用技术术语。
- 通用角色：项目负责人、技术负责人、质检员、售后人员。
- 采购需求明确要求响应的产品技术名称，除非该名称同时是投标人的专有品牌或授权痕迹。
- 纯章节标题中的“投标人/供应商/承包人”，除非后面跟具体身份。

## 第一人称处理

`我公司/我方/本公司/我单位` 不一定让评委识别具体供应商，因此不要默认判为阻断级。但它会降低暗标匿名感，且和内部部门、地域、人员、案例、品牌组合时会形成识别链。

Recommended rewrite:

- `我公司将...` -> `投标人将...` or `项目组将...`
- `公司工程部...` -> `项目技术支持组...`
- `我方人员...` -> `拟派服务人员...`
- `本公司售后服务部...` -> `售后服务团队...`

## 识别链判断

Escalate severity when multiple weak clues combine:

- first-person subject + exact branch/department + local warehouse/address
- proprietary brand/platform + named prior customer/project
- named partner/manufacturer/logistics provider + unique implementation plan
- certificate/award name + field-specific rare capability

If a clue could identify a third party but not the bidder, mark `需人工确认` unless the tender bans any supplier-related identity marker broadly.
