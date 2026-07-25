# TITMAS Golden Path v0.1 — Example Mapping

The canonical specification is:

- [TITMAS Golden Path v0.1](../../../docs/golden-path-v0.1.md)

This directory implements that specification as a deterministic local File
Analysis Agent.

| Golden Path stage | Local artifact |
|---|---|
| User Task | `input/task.json` |
| Universal Agent | `run.py` |
| Execution Record | `output/execution-record.json` |
| Evidence Bundle | `output/evidence-bundle/` |
| Health Assessment | `output/health-report.json` |
| Audit Receipt | `output/audit-receipt.json` |
| Human Review | README, JSON artifacts, and SHA-256 checks |

This mapping is a runnable reference, not a claim of current TITMAS runtime
integration.
