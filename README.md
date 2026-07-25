# TITMAS Demo

## TITMAS First Experience

## Run the TITMAS Golden Path in 10 Minutes

TITMAS Demo is the first-experience gateway for exploring verifiable AI agents.

TITMAS enables AI agents to become:

- Observable
- Verifiable
- Evaluated

This repository focuses on runnable entry points, examples, and quick verification paths.

## Quick Start

```bash
git clone https://github.com/joy7758/titmas-demo.git
cd titmas-demo/examples/universal-agent
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

Read the canonical workflow specification:
[TITMAS Golden Path v0.1](docs/golden-path-v0.1.md).

## Golden Path v0.1

```text
User Task
  -> Universal Agent
  -> Execution Record
  -> Evidence Bundle
  -> Health Assessment
  -> Audit Receipt
  -> Human Review
```

The first example is a deterministic File Analysis Agent. It uses only the
Python standard library and local files:

- [Universal Agent Demo](examples/universal-agent/README.md)

The example produces contract-shaped local artifacts aligned with:

- `agent-evidence` for execution evidence
- `titmas-health` for state-based health assessment
- `aro-audit` for audit receipts
- `SAEE` for future long-term evaluation

It does not call or modify those repositories and does not claim current
runtime integration.

## Scope

This repository is an entry portal. Golden Path v0.1 demonstrates a
deterministic local lifecycle; it is not a production runtime, certification,
legal-compliance assessment, intelligence ranking, or safety guarantee.

```text
DEMO_CLASS=DETERMINISTIC_LOCAL_REFERENCE
CURRENT_TITMAS_RUNTIME_INTEGRATION=false
PRODUCTION_READY=false
```
