# TITMAS Digital Cell Demo Public Release Draft v0.1

## Draft Status

```text
DOCUMENT_TYPE=PUBLICATION_DRAFT
DOCUMENT_VERSION=v0.1
DEMO_ID=TITMAS-DIGITAL-CELL-DEMO-v0.1
POSITIONING=SMALL_REFERENCE_DEMO
LICENSE=Apache-2.0
GITHUB_RELEASE_STATUS=PENDING
REDCRAG_PUBLICATION_STATUS=PENDING
PUBLICATION_AUTHORIZED=false
```

This document prepares copy for GitHub and RedCrag.cn. It is not a published
announcement, release, deployment, certification, or production claim.

## 1. Shared Positioning Boundary

Approved English description:

> TITMAS Digital Cell Demo is a minimal reference implementation of an
> observable and verifiable digital agent.

Approved Chinese description:

> TITMAS 数字细胞 Demo 是一个展示 AI Agent 如何具备身份、边界、执行证据和健康状态的
> 最小参考实现。

All publication copy must preserve:

```text
REFERENCE_IMPLEMENTATION_ONLY=true
OBSERVABLE=true
VERIFIABLE=true
HEALTH_ASSESSABLE=true
PRODUCTION_READY=false
CERTIFICATION_CLAIM=false
DIGITAL_LIFE_CLAIM=false
AI_CONSCIOUSNESS_CLAIM=false
UNIVERSAL_AI_SAFETY_CLAIM=false
```

## 2. GitHub Announcement Draft

### Release Title

```text
TITMAS Digital Cell Demo v0.1
```

### Short Announcement

TITMAS Digital Cell Demo v0.1 is a small, deterministic reference
implementation showing how an AI Agent can be represented as an observable,
verifiable, and health-assessable digital subject.

The demo combines six bounded structures:

- Identity;
- Boundary;
- Evidence;
- Health;
- Memory;
- Reputation.

It runs one local document-analysis task, records every lifecycle transition,
generates SHA-256 integrity-verifiable Evidence, derives a Health view, and
simulates one denied boundary violation followed by a Level 2 restriction,
recovery, and versioned evolution.

### What the Demo Shows

```text
Birth
  -> Execution
  -> Evidence
  -> Health Assessment
  -> Recovery
  -> Evolution
```

The reviewed implementation generates:

- a human-readable Digital Cell report;
- ordered Evidence records;
- a complete machine-readable Cell state;
- deterministic byte-identical output under the fixed local configuration.

### Quick Start

```bash
git clone https://github.com/joy7758/titmas-demo.git
cd titmas-demo/examples/digital-cell
python3 run.py
python3 -m unittest discover -s tests -v
```

Requirements:

- Python 3.9 or newer;
- no third-party package;
- no API key;
- no external AI model.

### Verification Summary

```text
TEST_COUNT=7
TEST_RESULT=PASS
DEMO_RUN=PASS
DETERMINISTIC_REPLAY=PASS
REFERENCE_DEMO_REVIEW=APPROVE_REFERENCE_DEMO
FREEZE_STATUS=FROZEN_REFERENCE_IMPLEMENTATION
```

### Release Boundary

This is a local reference demo. It is not a production TITMAS Runtime,
certification system, AI safety replacement, AGI governance solution, cloud
service, MCP server, or multi-agent platform.

It does not prove:

- AI consciousness;
- digital life;
- a survival law;
- universal AI safety;
- production readiness.

### License

TITMAS Digital Cell Demo v0.1 is available under the Apache License 2.0.

### Prepared Links

```text
REPOSITORY_URL=https://github.com/joy7758/titmas-demo
RELEASE_URL=GITHUB_RELEASE_LINK_PLACEHOLDER
DOCUMENTATION_URL=REDCRAG_PAGE_LINK_PLACEHOLDER
```

## 3. GitHub Release Notes Draft

### Included

- minimal Digital Cell object model;
- deterministic lifecycle simulation;
- SHA-256 Evidence generation and verification;
- derived Health State;
- bounded immune response simulation;
- failure, response, recovery, and evolution memory;
- seven acceptance tests;
- concept and implementation review;
- reference implementation freeze record;
- Apache License 2.0.

### Generated Local Artifacts

```text
output/
  TITMAS-DIGITAL-CELL-REPORT.md
  digital-cell-state.json
  evidence.jsonl
```

Generated outputs are intentionally local and excluded from Git. Their reviewed
SHA-256 values are recorded in the freeze record.

### Known Limitations

- one deterministic local Cell;
- one rule-based task;
- one simulated abnormal event;
- one fixed Level 2 response;
- no real AI reasoning;
- no external identity, authentication, policy, or isolation service;
- no integration with TITMAS Runtime, DBOS, SAEE, Agent Health, MCP, or Agent frameworks.

## 4. RedCrag.cn Page Draft

### Page Title

```text
TITMAS Digital Cell Demo
```

### Page Subtitle

English:

> A minimal reference implementation showing how an AI agent can become
> observable, verifiable, and health-assessable.

中文：

> 一个展示 AI Agent 如何具备身份、边界、执行证据和健康状态的最小参考实现。

### Introduction

AI Agent 的输出通常只能告诉我们“产生了什么结果”，却不能完整回答“谁执行、允许做什么、
实际做了什么、记录是否被修改、当前状态如何，以及失败后发生了什么”。

TITMAS Digital Cell Demo v0.1 用一个小型、确定性的本地示例回答这些问题。它把一个简单
文档分析 Agent 表示为由 Identity、Boundary、Evidence、Health、Memory 和 Reputation
组成的 Digital Cell。每次生命周期变化都会留下可校验的 Evidence。

这是参考实现，不是生产平台，也不是关于数字生命或 AI 意识的声明。

### Architecture

```text
Digital Cell
  |
  +-- Identity
  +-- Boundary
  +-- Evidence
  +-- Health (derived view)
  +-- Memory
  +-- Reputation
```

Identity 说明哪个主体执行；Boundary 说明行动范围；Evidence 保存执行历史与 SHA-256
完整性材料；Health 从身份、证据、执行和恢复历史派生；Memory 保存失败、响应、恢复和
演化；Reputation 只表达当前 Demo 上下文中的历史评价。

```text
Evidence != AI correctness
Health != Authority
Health != Certification
Health != Permission
Reputation != Authority
```

### Demonstration Flow

```text
Birth
  -> Execution
  -> Evidence
  -> Health Assessment
  -> Recovery
  -> Evolution
```

正常路径分析一个本地文档。异常路径尝试执行被禁止的 `delete_document` 动作。该动作
不会执行，而是生成 Evidence、触发本地 Level 2 `RESTRICTION`、更新 Memory，并在保留
失败历史的前提下进入恢复和版本演化。

### What You Can Inspect

- `TITMAS-DIGITAL-CELL-REPORT.md`: 人类可读报告；
- `evidence.jsonl`: 有序 Evidence 历史；
- `digital-cell-state.json`: 完整机器可读状态；
- `test_digital_cell.py`: 七项验收测试。

### Run Locally

```bash
git clone https://github.com/joy7758/titmas-demo.git
cd titmas-demo/examples/digital-cell
python3 run.py
python3 -m unittest discover -s tests -v
```

不需要第三方 Python 包、API key、外部模型或云服务。

### Screenshot Placement

```text
SCREENSHOT_ASSET=SCREENSHOT_ASSET_PLACEHOLDER
```

Caption:

> Deterministic terminal output showing verified Evidence, a local Level 2
> restriction response, updated memory, and an evolved lifecycle state.

### Architecture Image Placement

```text
ARCHITECTURE_IMAGE=ARCHITECTURE_IMAGE_PLACEHOLDER
```

Caption:

> The six bounded structures of a Digital Cell and the path from execution to
> Evidence, Health assessment, recovery, and evolution.

### Source and License

```text
GITHUB_RELEASE_LINK=GITHUB_RELEASE_LINK_PLACEHOLDER
LICENSE=Apache-2.0
```

### Limitations

本 Demo 只有一个本地主体、一个规则任务和一次固定异常事件。它不创建 TITMAS Runtime、
生产隔离系统、认证服务、MCP server、云平台或多智能体生态。

本 Demo 不证明：

- 数字生命已经出现；
- AI 具有意识；
- 发现了生存规律；
- 提供通用 AI 安全方案；
- 已达到生产就绪。

## 5. Publication Asset Status

```text
LICENSE_CONFIRMED=true
README_REVIEWED=true
SCREENSHOT_STATUS=PENDING
ARCHITECTURE_IMAGE_STATUS=PENDING
GITHUB_RELEASE_STATUS=PENDING
REDCRAG_PUBLICATION_STATUS=PENDING
HUMAN_CONFIRMATION_REQUIRED=true
```

## 6. Human Publication Gate

Before using either draft:

- [ ] Capture and review the Demo screenshot.
- [ ] Create and review the architecture image.
- [ ] Verify the final GitHub release URL.
- [ ] Replace all placeholders.
- [ ] Review rendered Markdown and RedCrag.cn layout.
- [ ] Confirm attribution and Apache-2.0 presentation.
- [ ] Authorize commit separately.
- [ ] Authorize push separately.
- [ ] Authorize GitHub release publication separately.
- [ ] Authorize RedCrag.cn deployment separately.

```text
COMMIT_AUTHORIZED=false
PUSH_AUTHORIZED=false
GITHUB_PUBLICATION_AUTHORIZED=false
REDCRAG_PUBLICATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
```
