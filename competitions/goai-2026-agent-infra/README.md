# GOAI 2026：TITMAS 智能体可信发布闸门

> 项目英文名：TITMAS Verified Agent Release Gate（TITMAS 智能体可信发布闸门）

本目录是 GOAI 2026 世界人工智能开源大赛 Agent Infra（智能体基础设施）“新智基座”赛道的公开安全参赛工作区。

```text
COMPETITION=GOAI-2026
TRACK=AGENT-INFRA
PROJECT=TITMAS-VERIFIED-AGENT-RELEASE-GATE
SUBMISSION_STAGE=PRELIMINARY-DRAFT
REGISTRATION_CONFIRMED=false
PRELIMINARY_SUBMISSION_CONFIRMED=false
AGENTTEAMS_RUNTIME_INTEGRATION=DESIGN-IN-PROGRESS
PRODUCTION_READY=false
```

## 一句话定位

在代码合并、发布或部署之前，由多个简单智能体协同检查任务来源、授权边界、测试结果和执行证据，输出 `PASS`（通过）、`FAIL`（失败）、`INCOMPLETE`（证据不完整）或 `HUMAN_REVIEW`（人工复核），阻止未经验证的智能体变更直接进入生产环境。

## 为什么是这个场景

企业引入编程智能体后，风险不只来自代码质量，还来自以下事实无法被统一回答：

- 这次变更为什么发生；
- 哪个智能体执行了什么操作；
- 使用了哪些工具和权限；
- 测试是否真实执行并通过；
- 证据是否完整、可复验且未被篡改；
- 高风险动作是否获得人工批准；
- 失败后是否能够阻断、降级或回滚。

普通日志和轨迹有助于排错，但不天然形成可移交、可离线复验的证据对象。本项目把“协作执行”和“独立验证”分开：AgentTeams（智能体团队框架）负责编排，TITMAS 证据能力负责生成和验证证据，发布闸门负责执行确定性决策。

## 多智能体闭环

```text
Repository Intake Agent（仓库接入智能体）
        ↓
Test and Attack Agent（测试与攻击智能体）
        ↓
Evidence Verification Agent（证据验证智能体）
        ↓
Release Gate Agent（发布闸门智能体）
        ↓
PASS / FAIL / INCOMPLETE / HUMAN_REVIEW
```

AgentTeams（智能体团队框架）中的 Manager（管理智能体）负责任务拆解、角色调度、上下文传递和状态追踪；各 Worker（执行智能体）只承担窄职责。人类审批者通过可见协作通道介入高风险动作。

## 初赛公开材料

- [作品简介](application/project-introduction-zh.md)
- [Agent Identity（智能体身份）与 Skill（技能）清单](application/agent-identity-and-skills.md)
- [AgentTeams（智能体团队框架）映射与技术架构](application/architecture-and-agentteams-mapping.md)
- [安全边界与开放计划](application/security-and-open-source-plan.md)

## 当前可复用基础

本项目不从零重建所有能力，而是组合现有的公开安全资产：

- TITMAS Digital Cell Demo（TITMAS 数字单元演示）：身份、边界、证据、健康与生命周期的确定性参考实现；
- TITMAS Agent Integrations（TITMAS 智能体集成）：Python（Python 编程语言）/ TypeScript（TypeScript 编程语言）软件开发工具包、MCP（模型上下文协议）适配器和框架集成候选；
- Evidence Bundle（证据包）与 Receipt（回执）语义：用于结构化记录、完整性校验和离线复验；
- GitHub Action（GitHub 自动化动作）候选：作为企业研发流程中的安装入口和合并阻断点。

## 永久边界

- Evidence（证据）证明记录的执行历史和完整性，不证明代码在所有环境中都正确；
- Verification（验证）不等于 Authorization（授权）；
- Trace（轨迹）不自动等于可移交证据；
- `PASS`（通过）仅表示满足声明的策略和证据条件，不构成认证、法律结论或生产许可；
- 本目录不得包含密钥、令牌、客户数据、私有一致性测试题库或未公开的 TITMAS 核心实现。

## 许可证

计划将参赛公开安全部分按 Apache License 2.0（Apache 2.0 开源许可证）发布。第三方依赖、商业模型接口与云服务将单独声明，不把第三方能力误称为本项目自研成果。
