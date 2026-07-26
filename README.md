# TITMAS Digital Cell Demo

> A minimal reference implementation showing how an AI agent can become
> observable, verifiable, and health-assessable.

中文：TITMAS 数字细胞 Demo 是一个展示 AI Agent 如何具备身份、边界、执行证据和健康
状态的最小参考实现。

```text
DEMO_ID=TITMAS-DIGITAL-CELL-DEMO-v0.1
DEMO_STATUS=REFERENCE_COMPLETE
IMPLEMENTATION_TYPE=REFERENCE_DEMO_ONLY
CURRENT_TITMAS_RUNTIME_INTEGRATION=false
PUBLIC_RELEASE_AUTHORIZED=false
PRODUCTION_READY=false
```

## Reference Implementation Notice

This repository contains one small, non-normative reference implementation.
It demonstrates the reviewed Digital Cell v0.1 behavior but does not define the
only valid implementation, establish protocol conformance, or turn the demo
into a TITMAS Runtime.

Specification, implementation, review, release, and production status remain
separate. Reusing this code does not grant certification, Authority,
Permission, or a claim of TITMAS compatibility beyond the demonstrated scope.

## Overview

Digital Cell is a minimal model of a TITMAS-compatible digital subject.

This deterministic local demo represents one simple Agent together with the
structures needed to identify it, bound its actions, record what it executed,
derive an operational health view, preserve history, and represent contextual
reputation.

The demonstration task analyzes one local text document. It requires only
Python and does not call an AI model, external API, database, cloud service, or
Agent framework.

## Why Digital Cell

Future AI systems need explicit structures for:

- identity: which subject acted;
- boundaries: which actions are allowed or forbidden;
- evidence: what was executed and whether its record remains intact;
- state observation: what the available history says about current health.

An output alone does not provide these properties. The demo therefore records
the execution path and its limitations rather than claiming that the output is
intelligent or correct.

```text
Evidence proves execution history.
Evidence does not prove AI correctness.
```

## Architecture

![Digital Cell v0.1 architecture](release-assets/digital-cell-architecture.png)


```text
Digital Cell
  |
  +-- Identity
  +-- Boundary
  +-- Evidence
  +-- Health
  +-- Memory
  +-- Reputation
```

| Object | Demo responsibility |
|---|---|
| Identity | Stable Cell ID, Owner, version, purpose, and capabilities |
| Boundary | Allowed actions, forbidden actions, and resource limits |
| Evidence | Intent, action, execution event, SHA-256 hashes, and integrity state |
| Health | Derived identity, evidence, execution, adaptation, and risk view |
| Memory | Execution, failure, immune response, recovery, and evolution history |
| Reputation | Local reliability, evidence quality, and contribution assessment |

These objects form one bounded local representation. They do not create
authentication, Permission, Authority, certification, or a production
governance system.

## Lifecycle

![Digital Cell lifecycle](release-assets/digital-cell-lifecycle.png)


Public lifecycle summary:

```text
Birth
  -> Execution
  -> Evidence
  -> Health Assessment
  -> Recovery
  -> Evolution
```

The evidenced implementation states are:

```text
BIRTH
  -> REGISTERED
  -> EXECUTING
  -> OBSERVED
  -> ASSESSED
  -> RECOVERED
  -> EVOLVED
```

Every state transition generates an integrity-verifiable Evidence record. The
demo also attempts one forbidden action, records the denial, applies a local
Level 2 `RESTRICTION` response, preserves the failure, and records recovery
without expanding the original Boundary.

## Quick Start

Requirements: Python 3.9 or newer. No third-party package is required.

```bash
git clone https://github.com/joy7758/titmas-demo.git
cd titmas-demo/examples/digital-cell
python3 run.py
```

Run the acceptance tests:

```bash
python3 -m unittest discover -s tests -v
```

## Example Output

![Digital Cell execution report and evidence result](release-assets/digital-cell-report.png)


Terminal:

```text
TITMAS Digital Cell Demo Complete
Digital Cell: CREATED
Task Execution: COMPLETED
Evidence: VERIFIED
Health: DERIVED
Immune Response: LEVEL_2_RESTRICTION
Memory: UPDATED
Lifecycle: EVOLVED
```

Generated locally:

| Output | Purpose |
|---|---|
| `output/TITMAS-DIGITAL-CELL-REPORT.md` | Human-readable Digital Cell report |
| `output/evidence.jsonl` | Ordered Evidence history |
| `output/digital-cell-state.json` | Complete machine-readable Cell state |

Example derived health state:

```text
identity_health=HEALTHY
evidence_health=VERIFIED
execution_health=HEALTHY
adaptation_state=RECOVERED
risk_level=LOW_AFTER_RECOVERY
```

Health is a derived view:

```text
Health != Authority
Health != Certification
Health != Permission
```

## Review and Freeze

- [Concept and implementation review](examples/digital-cell/TITMAS-DIGITAL-CELL-DEMO-REVIEW-v0.1.md)
- [Reference demo freeze record](TITMAS-DIGITAL-CELL-DEMO-FREEZE-v0.1.md)
- [Public release checklist](PUBLIC-RELEASE-CHECKLIST-v0.1.md)

The v0.1 behavior is frozen as a reference demo. Behavioral changes require a
new version, new artifact identity, and explicit difference declaration.

## Limitations

This demo does not prove:

- AI consciousness;
- digital life;
- a survival law;
- universal intelligence or universal strategy superiority;
- production readiness.

The demo has one deterministic local Cell, one document task, one simulated
boundary violation, and one fixed response. It has no real AI reasoning,
external identity, authentication, permission service, policy engine,
production isolation, MCP server, cloud service, multi-agent ecosystem, or
external framework integration.

## Contributing

This release package does not create a formal TITMAS contribution program.
Proposed changes should remain focused on:

- reproducibility defects;
- test coverage for frozen v0.1 behavior;
- documentation clarity;
- accessibility and developer experience;
- explicitly versioned successor proposals.

Changes to the Digital Cell object model, lifecycle, Evidence semantics, Health
derivation, or immune response require a new version, new artifact identity,
difference declaration, tests, review, and freeze record. A submitted issue or
pull request does not grant Architecture Authority or imply acceptance.

## License

Licensed under the [Apache License 2.0](LICENSE).

The license permits use, modification, and redistribution under its terms. It
does not provide certification, warranty, trademark rights beyond customary
source attribution, production support, or permission to make unsupported
TITMAS compatibility claims.

## Public Release Status

The technical reference demo, Apache License 2.0, and release documentation are
prepared. Screenshots, the architecture image, final human confirmation, and
the external publication actions remain pending.

```text
LICENSE_STATUS=APACHE-2.0
PUBLIC_RELEASE_STATUS=PENDING_HUMAN_CONFIRMATION_AND_RELEASE_ASSETS
GITHUB_RELEASE_PUBLISHED=false
REDCRAG_PUBLICATION_DEPLOYED=false
```

Open-source availability must not be interpreted as certification, production
support, or TITMAS Runtime availability.
