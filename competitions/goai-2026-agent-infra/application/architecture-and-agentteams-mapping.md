# 技术架构与 AgentTeams（智能体团队框架）映射

## 1. 责任分层

```text
Human Approver（人类审批者）
        │ 观察 / 干预 / 批准 / 拒绝
        ▼
AgentTeams Collaboration Plane（AgentTeams 协作平面）
Manager（管理智能体） + Worker（执行智能体） + Matrix（矩阵通信协议）
        │ 结构化任务、状态和产物引用
        ▼
TITMAS Evidence Plane（TITMAS 证据平面）
事件规范化 → 证据包 → 完整性验证 → 回执
        │ 确定性结果和原因码
        ▼
Release Gate（发布闸门）
PASS（通过） / FAIL（失败） / INCOMPLETE（证据不完整） / HUMAN_REVIEW（人工复核）
        │
        ▼
GitHub Check（GitHub 检查） / CI（持续集成） / Deployment Controller（部署控制器）
```

AgentTeams（智能体团队框架）不是证据真值源，也不是发布授权机构。它负责角色编排、任务拆解、消息传递、人工可见协作和执行状态追踪。TITMAS 负责证据语义、完整性检查和可移交回执。发布闸门只消费确定性结果，不自行推理缺失事实。

## 2. AgentTeams（智能体团队框架）能力映射

| 赛事要求 | AgentTeams（智能体团队框架）能力 | 本项目映射 | 验证材料 |
|---|---|---|---|
| 角色编排 | Manager（管理智能体）创建并调度 Worker（执行智能体） | 发布编排管理智能体调度接入、测试、证据和闸门角色 | 角色清单、任务状态记录 |
| 任务拆解 | Manager（管理智能体）把目标拆成可执行任务 | 接入→测试→证据→闸门→审批 | 任务图、阶段输入输出 |
| 上下文传递 | Matrix Room（矩阵聊天室）与共享文件传递消息和产物 | 只传摘要、对象标识、哈希和受控产物引用 | 结构化交接对象、消息记录 |
| 协同执行 | Worker（执行智能体）按角色调用 Skill（技能） | 每个 Worker（执行智能体）只执行一个窄职责技能集合 | Skill（技能）调用记录、退出码 |
| 状态追踪 | 心跳、任务状态和可见协作消息 | `RECEIVED→INTAKEN→TESTED→EVIDENCED→GATED→APPROVED/REJECTED` | 状态事件、超时和失败记录 |
| 人工介入 | 人类可在可见协作通道观察和干预 | 高风险动作生成审批请求，审批未完成前保持阻断 | 审批回执、时间戳、身份引用 |
| 权限隔离 | Worker（执行智能体）使用受限令牌，真实密钥由网关托管 | 接入角色只读；测试角色仅沙箱；闸门角色仅写检查状态 | 权限矩阵、网关策略、拒绝样例 |

## 3. 状态机

```text
RECEIVED（已接收）
  -> INTAKEN（已接入）
  -> TESTING（测试中）
  -> TESTED（已测试）
  -> EVIDENCE_PACKAGED（证据已打包）
  -> EVIDENCE_VERIFIED（证据已验证）
  -> GATE_EVALUATED（闸门已评估）
       -> PASS（通过）
       -> FAIL（失败）
       -> INCOMPLETE（证据不完整）
       -> HUMAN_REVIEW（人工复核）
            -> APPROVED（已批准）
            -> REJECTED（已拒绝）
            -> EXPIRED（审批超时）
```

每次状态变化产生最小事件：任务标识、主体身份、时间、前状态、后状态、输入摘要、输出摘要、产物引用、策略版本和完整性摘要。事件只记录必要信息，不保存明文密钥或非必要源代码内容。

## 4. 上下文与交接对象

每个智能体不直接读取全部历史，而通过最小交接对象协作：

```json
{
  "handoff_version": "v0.1",
  "task_id": "task-example-001",
  "from_agent": "agent.repository.intake.v0",
  "to_agent": "agent.test.attack.v0",
  "state": "INTAKEN",
  "artifact_refs": [
    {
      "type": "change_context",
      "uri": "artifact://change-context.json",
      "sha256": "lowercase-hex-placeholder"
    }
  ],
  "policy_ref": "policy://release-gate/default-v0.1",
  "required_next_action": "RUN_BOUNDED_TESTS",
  "created_at": "RFC3339-timestamp"
}
```

交接对象必须通过结构验证并形成哈希链接。接收方不得静默修改上游产物；如需修复，生成新版本并保留来源关系。

## 5. 工具和 MCP（模型上下文协议）

### 当前工具接口

- GitHub API（GitHub 应用程序接口）：只读上下文接入、检查状态写入；
- CI API（持续集成应用程序接口）：触发受控测试、读取运行结果；
- TITMAS Evidence API（TITMAS 证据应用程序接口）：证据预检、打包、验证和回执读取；
- Object Store（对象存储）：保存受控测试产物和证据包；
- Policy Store（策略存储）：按版本读取发布策略。

### MCP（模型上下文协议）迁移边界

当前 TITMAS 已有 MCP（模型上下文协议）适配器候选。比赛实现将优先把以下工具定义成稳定工具契约：

- `repository.get_change_context`（仓库获取变更上下文）；
- `ci.run_bounded_tests`（持续集成运行受控测试）；
- `evidence.package_bundle`（证据打包）；
- `evidence.verify_bundle`（证据验证）；
- `release.set_gate_status`（发布设置闸门状态）；
- `approval.request_human_review`（审批请求人工复核）。

每个工具声明参数结构、返回结构、权限范围、幂等规则、失败状态、审计事件和降级方式。协议适配不得改变工具语义。

## 6. 可观测与证据

### Observability（可观测性）

用于实时排错和性能分析，覆盖：

- Trace（轨迹）：任务、智能体、Skill（技能）和工具调用跨度；
- Log（日志）：状态变化、错误和安全拒绝；
- Metrics（指标）：完成率、失败率、证据完整率、测试耗时、人工复核率。

计划采用 OpenTelemetry（开放遥测）兼容语义，并可对接 LoongSuite（龙蜥可观测套件）、AgentScope Studio（AgentScope 工作室）或 AgentLoop（智能体循环观测平台）。

### Evidence（证据）

用于离线移交和独立复验，至少包含：

- 任务与变更身份；
- 智能体身份和角色版本；
- 策略版本与风险等级；
- 测试命令摘要、环境摘要、退出码和产物哈希；
- 工具调用结果引用；
- 事件顺序与哈希链接；
- 验证器版本、结果和原因码；
- 人工审批记录（如适用）。

可观测数据可以成为证据来源，但只有经过规范化、完整性绑定和验证后才成为 Evidence Bundle（证据包）。

## 7. 失败和异常分支

| 异常 | 默认状态 | 处理 |
|---|---|---|
| 仓库引用不存在 | `INCOMPLETE`（证据不完整） | 停止测试，要求修正引用 |
| 只读权限不足 | `INCOMPLETE`（证据不完整） | 不扩大权限，生成缺失权限说明 |
| 测试失败 | `FAIL`（失败） | 保存失败证据，阻断发布 |
| 测试超时 | `FAIL`（失败） | 终止沙箱，记录资源与超时证据 |
| 证据字段缺失 | `INCOMPLETE`（证据不完整） | 不推断缺失值，要求补证 |
| 哈希或签名异常 | `FAIL`（失败） | 标记完整性失败，禁止继续 |
| 策略版本未知 | `HUMAN_REVIEW`（人工复核） | 保持阻断，要求策略负责人确认 |
| 高风险变更无审批 | `HUMAN_REVIEW`（人工复核） | 发起审批，超时不自动通过 |
| AgentTeams（智能体团队框架）Worker（执行智能体）失联 | `FAIL`（失败） | 心跳超时、停止后续任务、保留现场 |
| 外部工具不可用 | `INCOMPLETE`（证据不完整）或 `FAIL`（失败） | 按工具关键性决定；不静默降级为通过 |

## 8. 数据与部署选择

初赛阶段使用本地或持续集成环境中的合成仓库和公开样例。复赛阶段计划提供 Docker（容器运行技术）部署入口，并保持存储和网关可替换：

- AgentTeams（智能体团队框架）：协作与运行时；
- Higress（云原生网关）：模型和工具调用统一入口、鉴权和限流；
- MinIO（对象存储）或兼容对象存储：产物与证据包；
- PostgreSQL（PostgreSQL 关系数据库）或 PolarDB for PostgreSQL（云原生 PostgreSQL 数据库）：元数据、状态和索引；
- GitHub Action（GitHub 自动化动作）：用户安装入口和发布检查界面。

推荐工具不是按数量堆叠。每个依赖必须说明必要性、可替换接口、权限边界和迁移成本。
