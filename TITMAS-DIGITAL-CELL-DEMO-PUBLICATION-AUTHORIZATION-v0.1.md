# TITMAS Digital Cell Demo Publication Authorization v0.1

## Authorization Record Status

```text
DOCUMENT_TYPE=PUBLICATION_AUTHORIZATION_RECORD
DOCUMENT_VERSION=v0.1
DECISION=PUBLICATION_HOLD
PUBLICATION_EXECUTION_AUTHORIZED=false
COMMIT_AUTHORIZED=false
PUSH_AUTHORIZED=false
GITHUB_PUBLICATION_AUTHORIZED=false
REDCRAG_PUBLICATION_AUTHORIZED=false
DEPLOYMENT_AUTHORIZED=false
```

This record establishes the human decision boundary before the first public
release of TITMAS Digital Cell Demo v0.1. It does not publish, commit, push,
deploy, or modify the release candidate.

The current decision is `PUBLICATION_HOLD` because human publication
confirmation is not yet recorded and the screenshot and architecture image
remain pending. Technical readiness does not override these open release
conditions.

## 1. Publication Identity

| Field | Value |
|---|---|
| `authorization_id` | `TITMAS-DIGITAL-CELL-DEMO-PUBLICATION-AUTHORIZATION-v0.1` |
| `project_id` | `TITMAS-DIGITAL-CELL-DEMO` |
| `release_version` | `v0.1` |
| `release_candidate` | `TITMAS-DIGITAL-CELL-DEMO-v0.1-LOCAL-UNCOMMITTED-REFERENCE-PACKAGE` |
| `decision_date` | `2026-07-26` |

The release candidate is a local, uncommitted preparation package. This
identity does not claim that a Git tag, GitHub Release, public website version,
or immutable remote release currently exists.

## 2. Release Scope

Decision scope:

```text
RELEASE_SCOPE=TITMAS_DIGITAL_CELL_DEMO_v0.1_REFERENCE_PACKAGE
```

The bounded release candidate includes:

| Component | Reference | Status |
|---|---|---|
| Reference implementation | `examples/digital-cell/` | `FROZEN_REFERENCE_IMPLEMENTATION` |
| External developer README | `README.md` | `REVIEWED` |
| License | `LICENSE` | `Apache-2.0` |
| Test results | Seven acceptance tests | `PASS` |
| Deterministic replay | Report, state, and Evidence outputs | `PASS` |
| Freeze record | `TITMAS-DIGITAL-CELL-DEMO-FREEZE-v0.1.md` | `EXISTS` |
| Release checklist | `PUBLIC-RELEASE-CHECKLIST-v0.1.md` | `PREPARED_WITH_ASSETS_PENDING` |
| Publication copy | `PUBLIC-RELEASE-DRAFT-v0.1.md` | `DRAFT_NOT_PUBLISHED` |

The release scope excludes:

- any TITMAS production Runtime;
- external framework integration;
- MCP server or API;
- cloud or enterprise service;
- multi-agent ecosystem;
- production governance or certification system.

## 3. Publication Targets

The only candidate publication targets covered by this record are:

1. GitHub public repository;
2. redcrag.cn project page.

Each target requires a separate execution action after explicit human
publication approval.

```text
GITHUB_PUBLICATION_STATUS=NOT_EXECUTED_PENDING_HUMAN_CONFIRMATION
REDCRAG_PUBLICATION_STATUS=NOT_EXECUTED_PENDING_HUMAN_CONFIRMATION
```

| Target | Candidate scope | Current authority |
|---|---|---|
| GitHub public repository | Source, README, LICENSE, review, freeze and release records | `NOT_AUTHORIZED_TO_PUBLISH` |
| redcrag.cn project page | Approved positioning, screenshot, architecture image, running instructions and verified GitHub link | `NOT_AUTHORIZED_TO_PUBLISH` |

Approval or execution for one target must not be inherited by the other.

## 4. License

```text
LICENSE=Apache-2.0
LICENSE_FILE=LICENSE
LICENSE_CONFIRMED=true
```

Apache License 2.0 permits reuse, modification, and redistribution under its
terms. Contributions intentionally submitted for inclusion are governed by
the license terms unless separately stated.

Contribution incorporation still requires repository review. The license does
not create a formal TITMAS contribution authority or guarantee that a proposed
change will be accepted.

The license does not grant:

- certification;
- a safety guarantee;
- production approval;
- Architecture Authority;
- permission to make unsupported TITMAS compatibility claims;
- warranty or production support.

## 5. Human Publication Decision

```text
DECISION=PUBLICATION_HOLD
APPROVED_BY=NONE_PENDING_HUMAN_CONFIRMATION
TIMESTAMP=2026-07-26T17:53:33+08:00
RELEASE_SCOPE=TITMAS_DIGITAL_CELL_DEMO_v0.1_REFERENCE_PACKAGE
```

Decision rationale:

- technical release readiness is `PASS`;
- Apache License 2.0 is present;
- final publication audit is `PASS`;
- README and publication copy preserve the small reference demo positioning;
- screenshot capture and review are pending;
- architecture image creation and review are pending;
- placeholder replacement and final rendered-page review are pending;
- no explicit human authorization to publish either target has been recorded.

`PUBLICATION_HOLD` is not a rejection of the reference demo. It preserves the
release candidate while preventing preparation status from being interpreted
as publication authority.

To replace this hold, a human decision must explicitly identify:

- the decision maker;
- timezone timestamp;
- exact release candidate;
- target or targets authorized;
- approved asset identities;
- whether commit, push, GitHub Release, or redcrag.cn deployment is separately
  authorized.

## 6. Public Communication Boundary

Approved description:

> TITMAS Digital Cell Demo is a minimal reference implementation showing how
> an AI agent can become observable, verifiable, and health-assessable.

Chinese approved description:

> TITMAS 数字细胞 Demo 是一个展示 AI Agent 如何具备身份、边界、执行证据和健康状态的
> 最小参考实现。

Public communication must not claim:

- digital life has been created;
- AI consciousness has been demonstrated;
- a universal AI safety solution exists;
- production certification has been granted;
- TITMAS has autonomous AI governance authority;
- the demo is a production Runtime, cloud service, or enterprise platform.

```text
DIGITAL_LIFE_CLAIM_ALLOWED=false
AI_CONSCIOUSNESS_CLAIM_ALLOWED=false
UNIVERSAL_AI_SAFETY_CLAIM_ALLOWED=false
PRODUCTION_CERTIFICATION_CLAIM_ALLOWED=false
AUTONOMOUS_AI_GOVERNANCE_AUTHORITY_CLAIM_ALLOWED=false
```

## 7. Future Release Rules

Any future behavioral or semantic change requires:

1. a new version;
2. a change description against v0.1;
3. new validation evidence;
4. deterministic replay verification where applicable;
5. a new review and freeze record;
6. a new release preparation and publication decision.

Future versions must preserve the lineage of:

```text
TITMAS-DIGITAL-CELL-DEMO-v0.1
```

They must not overwrite, delete, silently reinterpret, or reuse the frozen v0.1
identity for changed behavior.

```text
HISTORY_OVERWRITE_ALLOWED=false
SILENT_BEHAVIOR_CHANGE_ALLOWED=false
NEW_VERSION_REQUIRED=true
CHANGE_DESCRIPTION_REQUIRED=true
NEW_VALIDATION_REQUIRED=true
```

## 8. Final Verification Checklist

| Verification item | Evidence | Status |
|---|---|---|
| Tests passed | Seven acceptance tests | `PASS` |
| Deterministic replay passed | Byte-identical report, state, and Evidence artifacts | `PASS` |
| License confirmed | Standard Apache License 2.0 text in `LICENSE` | `PASS` |
| README reviewed | Minimal, observable, verifiable, health-assessable positioning | `PASS` |
| Freeze record exists | `TITMAS-DIGITAL-CELL-DEMO-FREEZE-v0.1.md` | `PASS` |
| Release checklist exists | `PUBLIC-RELEASE-CHECKLIST-v0.1.md` | `PASS` |
| Publication drafts prepared | GitHub and RedCrag.cn drafts | `PASS` |
| Screenshot ready | Description prepared; image not captured or reviewed | `NOT_READY` |
| Architecture image ready | Description prepared; image not created or reviewed | `NOT_READY` |
| GitHub release link verified | Placeholder remains | `NOT_READY` |
| Human publication confirmation | No approving human identity recorded | `NOT_READY` |

```text
FINAL_VERIFICATION_RESULT=HOLD_WITH_ASSETS_AND_HUMAN_CONFIRMATION_PENDING
RELEASE_ASSETS_READY=false
HUMAN_PUBLICATION_CONFIRMATION=false
```

## 9. Non-goals

```text
NO_CODE_CHANGE=true
NO_SIMULATOR_CHANGE=true
NO_RUNTIME=true
NO_API=true
NO_PRODUCTION_DEPLOYMENT=true
NO_CERTIFICATION_AUTHORITY=true
NO_DIGITAL_LIFE_CLAIM=true
NO_NEW_FEATURES=true
```

This record does not authorize a commit, push, tag, GitHub Release, repository
metadata change, website publication, deployment, external announcement, or
production operation.

## 10. Stop Condition

```text
NEXT_REQUIRED_ACTION=HUMAN_PUBLICATION_CONFIRMATION_AFTER_RELEASE_ASSET_REVIEW
```

Stop after this record. Do not publish, commit, push, or deploy until a new,
explicitly scoped human decision authorizes the intended external action.
