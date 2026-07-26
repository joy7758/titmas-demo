# TITMAS Digital Cell Demo Release Assets v0.1

## 1. Asset Package Identity

| Field | Value |
|---|---|
| Project | TITMAS Digital Cell Demo |
| Version | v0.1 |
| Asset package version | v0.1 |
| Prepared at | 2026-07-26 (Asia/Shanghai) |
| Purpose | Prepare bounded public-release visuals and metadata |
| Publication execution authorized | false |

This record identifies prepared assets. It does not publish, deploy, or authorize the demo.

## 2. Screenshot Package

| Screenshot | Purpose | Required content | Artifact | Review status |
|---|---|---|---|---|
| Digital Cell lifecycle view | Explain the bounded lifecycle | Birth, execution, evidence, health assessment, recovery, and evolution | `release-assets/digital-cell-lifecycle.png` | PASS |
| Execution report and evidence result | Show observable output without implying certification | Execution result, evidence count, health state, replay result, and integrity digest | `release-assets/digital-cell-report.png` | PASS |
| Repository and demo structure | Show the minimal public package | README, license, implementation, runner, input, tests, and release records | `release-assets/digital-cell-repository-structure.png` | PASS |

### Screenshot Integrity

| Artifact | SHA-256 |
|---|---|
| `release-assets/digital-cell-lifecycle.png` | `85a841d3f8cb9248bae4003386677cd58c077bc6bc8dcd8fb6382648d9b28074` |
| `release-assets/digital-cell-report.png` | `74c72aad82703f3219db670cea008da233c808e78166da6c7b7082bcf9374b7b` |
| `release-assets/digital-cell-repository-structure.png` | `28ec7c46d596d79afe6153a67811c9f28a7eaa3a1d55ed388c09bfc361df0781` |

SCREENSHOTS_READY=true

## 3. Architecture Image Package

### Required Diagram

**Digital Cell v0.1 Architecture**

The diagram shows the six bounded objects:

- Identity
- Boundary
- Evidence
- Health
- Memory
- Reputation

The diagram explicitly excludes:

- production architecture
- runtime platform
- enterprise governance
- AI consciousness claims

| Artifact | Status | Review status | SHA-256 |
|---|---|---|---|
| `release-assets/digital-cell-architecture.png` | CREATED | PASS | `eaa58235aeb689f9335d50008949d254964de0cbc57ce99211e31a8a9f0e4312` |

ARCHITECTURE_IMAGE_READY=true

## 4. Final Publication Metadata

### GitHub

| Field | Prepared value |
|---|---|
| Repository URL | `https://github.com/joy7758/titmas-demo` |
| Release version | `v0.1.0` |
| Release title | `TITMAS Digital Cell Demo v0.1` |

### redcrag.cn

| Field | Prepared value |
|---|---|
| Page title | `TITMAS Digital Cell Demo v0.1` |
| Description | `TITMAS 数字细胞 Demo 是一个展示 AI Agent 如何具备身份、边界、执行证据和健康状态的最小参考实现。` |
| URL | `https://redcrag.cn/digital-cell/` |

URL placeholders remain intentionally unresolved until a human-authorized publication action creates the final public locations.

## 5. Release Readiness Update

| Check | Status |
|---|---|
| Screenshots ready | PASS |
| Architecture image ready | PASS |
| README final review | PASS |
| License confirmed | PASS: Apache-2.0 |
| Publication authorization record exists | PASS |

RELEASE_ASSETS_READY=true
PUBLICATION_EXECUTION_AUTHORIZED=false

## 6. Boundary

- Assets are descriptive release materials only.
- Assets do not certify safety, correctness, intelligence, or production readiness.
- Assets do not create a runtime platform or governance authority.
- Human confirmation remains required before any publication action.

## 7. Non-goals

```text
NO_COMMIT=true
NO_PUSH=true
NO_PUBLISH=true
NO_DEPLOY=true
NO_CODE_CHANGE=true
PUBLICATION_EXECUTION_AUTHORIZED=false
```
