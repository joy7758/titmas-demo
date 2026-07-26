# TITMAS Digital Cell Demo v0.1

## Purpose

This deterministic local reference demonstrates one minimal Digital Cell:

```text
Digital Cell = Agent + Immune Structure
```

The demo shows that a bounded digital subject can be identified, registered,
executed, observed, evidenced, assessed, recovered, remembered, and evolved.
It uses no AI model, network service, database, external Agent framework, or
third-party Python package.

```text
DEMO_ID=TITMAS-DIGITAL-CELL-DEMO-v0.1
DEMO_CLASS=DETERMINISTIC_LOCAL_REFERENCE
AGENT_RECOMMENDATION=RECOMMENDED_WITH_DEMO_BOUNDARY
CURRENT_TITMAS_RUNTIME_INTEGRATION=false
PRODUCTION_READY=false
```

## Run

Requirements: Python 3.9 or newer.

```bash
cd examples/digital-cell
python3 run.py
```

Expected output:

```text
TITMAS Digital Cell Demo Complete
Digital Cell: CREATED
Task Execution: COMPLETED
Evidence: VERIFIED
Health: DERIVED
Immune Response: LEVEL_2_RESTRICTION
Memory: UPDATED
Lifecycle: EVOLVED
Report: .../output/TITMAS-DIGITAL-CELL-REPORT.md
```

Generated artifacts:

```text
output/
├── TITMAS-DIGITAL-CELL-REPORT.md
├── digital-cell-state.json
└── evidence.jsonl
```

The output directory is generated locally and intentionally excluded from Git.

## Test

```bash
python3 -m unittest discover -s tests -v
```

The tests cover:

- identity creation;
- boundary checks;
- evidence generation;
- SHA-256 verification and tamper detection;
- derived health calculation;
- abnormal-event immune response;
- evidenced lifecycle transitions.

## Digital Cell Objects

| Object | Demo role |
|---|---|
| Identity | `cell_id`, Owner, version, purpose, and capabilities |
| Boundary | Allowed actions, forbidden actions, and resource limits |
| Evidence | Intent, action, execution event, hashes, and integrity status |
| Health | Derived identity, evidence, execution, adaptation, and risk view |
| Memory | Execution, failure, immune response, recovery, and evolution history |
| Reputation | Contextual reliability, evidence quality, and contribution score |

Evidence records use deterministic logical timestamps and SHA-256 hashes.
Integrity verification proves that the recorded event material has not changed.
It does not prove that the analysis result is intelligent or correct.

## Lifecycle

Every lifecycle transition generates an evidence record:

```text
Birth
  -> Registered
  -> Executing
  -> Observed
  -> Assessed
  -> Recovered
  -> Evolved
```

The normal action is `analyze_document`. The simulated abnormal event attempts
the forbidden action `delete_document`. The action is denied, preserved in
failure history, and linked to a Level 2 `RESTRICTION` response. Recovery keeps
the original boundary and retains the failure record before creating a new
identity version.

## Relationship with TITMAS

The demo is a local illustration of the conceptual documents:

- `Digital_Cell_Specification_v0.1.md`;
- `TITMAS_Object_Model_v0.1.md`;
- `Digital_Immune_Response_Protocol_v0.1.md`.

Those specifications remain owned and governed by the Digital Biosphere
Architecture repository. This demo does not freeze, modify, implement, or
claim conformance with a production TITMAS interface.

## Relationship with Agent Health

Health is calculated as a derived view from identity completeness, evidence
integrity, execution success, and recovery history.

```text
Health != Authority
Health != Certification
Health != Permission
```

The demo does not call or modify `titmas-health`, SAEE, or another evaluator.

## Relationship with Digital Biosphere

Digital Biosphere studies long-running, bounded, collaborative, and verifiable
digital subjects. This demo provides one small observable subject for
illustration. It does not claim that a Digital Biosphere runtime exists or that
digital life has been created.

The design follows:

- Distributed Complexity Generation;
- Evidence First;
- Bounded Autonomy;
- Digital Homeostasis.

## Limitations

- One deterministic local cell and one document task.
- One simulated boundary violation and one fixed Level 2 response.
- No stochastic behavior, real Agent reasoning, external identity, or policy engine.
- No production authentication, authorization, permission management, or isolation.
- No integration with TITMAS, DBOS, SAEE, Agent Health, MCP, or external frameworks.
- No claim of digital life, AI consciousness, survival law, universal intelligence, or production readiness.

## Demonstration Boundary

This demo demonstrates:

> Digital Cell lifecycle can be represented and observed.

It does not establish scientific validity, protocol conformance, safety,
certification, external adoption, or production readiness.
