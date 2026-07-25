# TITMAS Golden Path v0.1

## Purpose

Demonstrate the complete local lifecycle of a verifiable AI agent through one
canonical, reproducible path.

Golden Path v0.1 answers:

> How does an ordinary agent enter TITMAS and produce reviewable execution
> artifacts?

## Canonical Workflow

```text
User Task
  -> Universal Agent
  -> Execution Record
  -> Evidence Bundle
  -> Health Assessment
  -> Audit Receipt
  -> Human Review
```

No alternative first-experience path is normative for v0.1.

## Demonstration Task

The Universal Agent is a deterministic File Analysis Agent. It:

1. receives `input/task.json`;
2. reads the referenced local text file;
3. generates a rule-based summary;
4. writes an execution record;
5. packages evidence records and SHA-256 integrity metadata;
6. generates a state-based health report;
7. issues a local audit receipt after digest verification.

The example uses no external API, model, database, network request, or current
TITMAS runtime.

## Artifact Contract

### Execution Record

Records the agent identity, task identity, ordered actions, action status, and
deterministic result.

### Evidence Bundle

```text
evidence-bundle/
├── manifest.json
├── records.jsonl
└── integrity.json
```

- `manifest.json` identifies the bundle and its source artifacts.
- `records.jsonl` preserves ordered execution events.
- `integrity.json` records SHA-256 digests and the local verification result.

### Health Report

Uses explicit states rather than a composite score:

```json
{
  "execution_stability": "healthy",
  "evidence_integrity": "verified",
  "recovery_ability": "available"
}
```

`available` means a retry policy is declared. Golden Path v0.1 does not inject
a failure, so recovery remains unexercised and is disclosed as a limitation.

### Audit Receipt

Links `audit-001` to `evidence-001` and records whether the declared evidence
digests passed local verification.

An audit receipt is not a legal judgment, certification, authorization, or
proof that the agent result is correct.

## What TITMAS Demonstrates

Golden Path v0.1 demonstrates:

- what the agent executed;
- what evidence was collected;
- how execution artifacts can be integrity-checked;
- how operational health can be expressed as reviewable states;
- how an audit receipt can link back to verified evidence;
- where human review remains required.

## What TITMAS Does Not Prove

Golden Path v0.1 does not prove:

- AI correctness;
- AI intelligence superiority;
- legal or regulatory compliance;
- safety certification;
- production readiness;
- external adoption;
- current integration with TITMAS core runtimes.

## Component Mapping

| Capability | Repository | Golden Path v0.1 relationship |
|---|---|---|
| Entry | `titmas-demo` | Runnable local reference |
| Execution evidence | `agent-evidence` | Future contract and integration reference |
| Health assessment | `titmas-health` | Future state-model reference |
| Audit receipt | `aro-audit` | Future receipt and verification reference |
| Long-term evaluation | `SAEE` | Future read-only evaluation reference; not run in v0.1 |

Golden Path v0.1 does not modify or invoke the source code of the referenced
repositories.

## Runnable Reference

```bash
cd examples/universal-agent
python3 run.py
```

Expected terminal output:

```text
TITMAS Golden Path Complete
Execution Record: CREATED
Evidence Bundle: VERIFIED
Health Report: GENERATED
Audit Receipt: CREATED
```

## Machine-readable Status

```text
GOLDEN_PATH_VERSION=v0.1
DEMO_CLASS=DETERMINISTIC_LOCAL_REFERENCE
EXTERNAL_API_REQUIRED=false
COMPOSITE_HEALTH_SCORE_USED=false
AGENT_EVIDENCE_SOURCE_MODIFIED=false
TITMAS_HEALTH_SOURCE_MODIFIED=false
ARO_AUDIT_SOURCE_MODIFIED=false
SAEE_SOURCE_MODIFIED=false
CURRENT_TITMAS_RUNTIME_INTEGRATION=false
HUMAN_REVIEW_REQUIRED=true
PRODUCTION_READY=false
```
