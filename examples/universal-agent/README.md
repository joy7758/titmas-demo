# Universal Agent Demo

## 通用智能体可信执行演示

This deterministic File Analysis Agent is the runnable reference for
[TITMAS Golden Path v0.1](../../docs/golden-path-v0.1.md).

It exists to show one complete and reviewable story:

```text
Task
  -> Agent Execution
  -> Execution Record
  -> Evidence Bundle
  -> Health Report
  -> Audit Receipt
  -> Human Review
```

## Run

Requirements: Python 3.9 or newer. No third-party dependency or external API is
required.

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

The command deterministically regenerates the committed files under `output/`.

## Input

`input/task.json` identifies the task and `input/sample.txt` is the local file
to analyze. The agent reads the file, selects the first non-empty line as a
rule-based summary, and records deterministic file statistics.

## Output

```text
output/
├── execution-record.json
├── evidence-bundle/
│   ├── manifest.json
│   ├── records.jsonl
│   └── integrity.json
├── health-report.json
└── audit-receipt.json
```

## What This Demo Verifies

- the requested local file was read;
- the declared agent actions completed;
- the execution record was packaged into ordered evidence records;
- manifest, record, and execution-record SHA-256 digests match;
- the audit receipt links back to the verified evidence bundle.

## What This Demo Does Not Claim

- that the summary is objectively correct;
- intelligence superiority;
- legal compliance or certification;
- a safety guarantee;
- production readiness;
- current runtime integration with `agent-evidence`, `titmas-health`,
  `aro-audit`, or `SAEE`.

## Ecosystem Relationship

| Repository | Relationship |
|---|---|
| `agent-evidence` | Execution-evidence contract reference |
| `titmas-health` | State-based health-report reference |
| `aro-audit` | Audit-receipt reference |
| `SAEE` | Future long-term, read-only evaluation reference |

The generated files are local, contract-shaped demonstration artifacts. They
do not establish conformance with, or execution by, the referenced projects.

```text
DEMO_ID=TITMAS-GOLDEN-PATH-v0.1
AGENT_KIND=DETERMINISTIC_FILE_ANALYSIS
CURRENT_CORE_RUNTIME_INTEGRATION=false
EXTERNAL_VALIDATION=false
PRODUCTION_READY=false
```
