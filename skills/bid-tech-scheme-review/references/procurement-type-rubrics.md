# Procurement Type Overlays

Use this file after classifying the tender as `工程`, `服务`, `货物`, or `混合`. The common review framework stays unchanged; this overlay explains what evidence deserves deeper review and what wrong-content patterns are severe for each procurement type.

## Classification

| 采购类型 | 判断依据 | 主导评审问题 |
| --- | --- | --- |
| 工程 | 招标范围以施工、改造、安装工程、装修、土建、机电、弱电、园林、市政等为主 | 施工组织是否可落地，工期/资源/工序/安全质量是否闭合 |
| 服务 | 招标范围以物业、保安、运维、咨询、运营、维保、培训、检测、监理、外包等连续服务为主 | 人员、班次、SLA、流程、考核、风险处置是否可信 |
| 货物 | 招标范围以设备、材料、软件产品、耗材、车辆、家具、仪器等供货为主 | 技术参数、清单数量、兼容性、供货安装调试、质保售后是否响应 |
| 混合 | 同时包含工程/服务/货物且技术方案需要同时响应 | 先确定主导类型，再检查次要类型的关键硬约束是否缺失或混入错误逻辑 |

## 工程类技术标

### 高权重证据

- 施工范围、工程量清单、图纸、施工界面、现场条件、临设和交通组织。
- 施工组织设计、施工顺序、工艺方法、关键工序、样板/首件/隐蔽验收。
- 总进度计划、网络图/横道图、节点工期、资源投入、机械设备、劳动力计划。
- 质量保证、安全文明施工、环保扬尘、成品保护、季节性施工、应急预案。
- 项目管理机构、岗位职责、分包/协作界面、验收和移交。

### 严重问题

- 工期、网络图、横道图、正文计划互相冲突。
- 工程量清单、图纸范围、关键工艺、材料规格或施工界面明显遗漏。
- 把服务运营、货物销售、售后模板当成施工方案主体。
- 安全、质量、环保只有口号，没有检查点、责任人、频次、记录和闭环。
- 施工组织无法支持承诺工期，例如资源投入和进度节点不匹配。

### 履约可执行性重点

工程类的可执行性重点看“工序-资源-时间-质量安全控制”是否闭合。好的方案应能让甲方看到施工怎么组织、谁来干、什么时候干、风险怎么控、验收怎么过。

## 服务类技术标

### 高权重证据

- 服务范围、服务对象、服务地点、服务时段、服务标准、SLA/响应时限。
- 人员配置、岗位职责、排班轮岗、替补机制、培训、稳定性、进退场交接。
- 日常服务流程、重点场景处理、投诉/异常/突发事件闭环。
- 考核奖惩、质量巡检、台账记录、月报/季报、持续改进机制。
- 与甲方部门、第三方、现场人员的协同边界。

### 严重问题

- 人员数量、年龄、证书、岗位、班次、响应时限与招标文件冲突。
- 只有制度名称，没有岗位、频次、记录、责任人、升级路径。
- 服务场景错位，例如保安服务写成设备安装、物业服务写成工程施工。
- 考核和服务承诺泛化为“以实际为准”，关键服务标准悬空。
- 进驻、交接、连续服务保障、应急替补缺失。

### 履约可执行性重点

服务类的可执行性重点看“人员-班次-流程-响应-考核”是否闭合。好的方案应能让甲方相信中标后服务不会断档，关键岗位有人、异常有人管、服务质量能被持续检查。

## 货物类技术标

### 高权重证据

- 采购清单、品目、数量、规格型号、核心技术参数、配置清单、备品备件。
- 参数逐条响应、偏离表、检测报告/认证/兼容性说明中可见的技术承诺。
- 供货周期、运输包装、到货验收、安装调试、试运行、培训。
- 售后服务、质保期、备件供应、响应时限、维保网点、升级/扩展能力。
- 与现有系统、场地、电力、网络、接口、数据或耗材的兼容性。

### 严重问题

- 清单漏项、数量错误、型号/参数/单位错误，或把其他产品参数写入。
- 只写品牌宣传，不逐项响应招标参数、配置和验收要求。
- 供货、安装、调试、培训、质保、备件和售后响应缺失。
- 与现场环境或既有系统兼容性未说明，或者承诺明显不可实现。
- 把施工组织或服务运营模板当成货物技术响应主体。

### 履约可执行性重点

货物类的可执行性重点看“参数-清单-交付-安装调试-售后”是否闭合。好的方案应能让甲方确认买到的东西是什么、是否满足参数、何时交付、如何验收、后续谁负责。

## Mixed Procurement

For mixed tenders:

1. Identify the dominant procurement type from scoring weight, contract value, and main performance risk.
2. Apply that type as the main overlay.
3. Add rows in the core compliance matrices for secondary-type hard constraints, such as engineering schedule in a goods-plus-installation tender or service SLA in a product-plus-maintenance tender.
4. Treat wrong overlay logic as a scenario-fit defect: for example, a goods bid dominated by construction-site language or a service bid dominated by product-sales language.
