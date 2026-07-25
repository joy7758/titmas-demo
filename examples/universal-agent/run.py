#!/usr/bin/env python3
"""Run the deterministic TITMAS Golden Path v0.1 local reference demo."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


DEMO_ROOT = Path(__file__).resolve().parent
INPUT_DIR = DEMO_ROOT / "input"
OUTPUT_DIR = DEMO_ROOT / "output"
EVIDENCE_DIR = OUTPUT_DIR / "evidence-bundle"

TASK_PATH = INPUT_DIR / "task.json"
EXECUTION_RECORD_PATH = OUTPUT_DIR / "execution-record.json"
RECORDS_PATH = EVIDENCE_DIR / "records.jsonl"
MANIFEST_PATH = EVIDENCE_DIR / "manifest.json"
INTEGRITY_PATH = EVIDENCE_DIR / "integrity.json"
HEALTH_REPORT_PATH = OUTPUT_DIR / "health-report.json"
AUDIT_RECEIPT_PATH = OUTPUT_DIR / "audit-receipt.json"

AGENT_ID = "universal-agent"
EVIDENCE_ID = "evidence-001"
AUDIT_RECEIPT_ID = "audit-001"


def canonical_json(value: Any) -> str:
    """Return stable, human-readable JSON with a trailing newline."""

    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def sha256_file(path: Path) -> str:
    """Return the SHA-256 digest of a local file."""

    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path: Path, value: Any) -> None:
    """Write canonical JSON to an explicitly scoped demo path."""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(canonical_json(value), encoding="utf-8")


def read_task() -> tuple[dict[str, Any], Path]:
    """Load and validate the bounded local task."""

    task = json.loads(TASK_PATH.read_text(encoding="utf-8"))
    required = {"task_id", "goal", "input", "recovery_policy"}
    missing = required.difference(task)
    if missing:
        raise ValueError(f"task.json is missing fields: {sorted(missing)}")

    input_name = task["input"]
    if not isinstance(input_name, str) or Path(input_name).name != input_name:
        raise ValueError("task input must be one local file name")

    input_path = INPUT_DIR / input_name
    if not input_path.is_file():
        raise FileNotFoundError(f"input file not found: {input_path}")
    return task, input_path


def analyze_file(input_path: Path) -> dict[str, Any]:
    """Produce a deterministic summary without an external model."""

    content = input_path.read_text(encoding="utf-8")
    nonempty_lines = [line.strip() for line in content.splitlines() if line.strip()]
    if not nonempty_lines:
        raise ValueError("input file must contain at least one non-empty line")

    return {
        "content_sha256": sha256_file(input_path),
        "line_count": len(content.splitlines()),
        "summary": nonempty_lines[0],
        "word_count": len(content.split()),
    }


def build_execution_record(
    task: dict[str, Any], input_path: Path, analysis: dict[str, Any]
) -> dict[str, Any]:
    """Build the canonical execution record."""

    return {
        "actions": [
            {
                "input": input_path.name,
                "sequence": 1,
                "sha256": analysis["content_sha256"],
                "status": "success",
                "type": "file_read",
            },
            {
                "method": "first_nonempty_line",
                "sequence": 2,
                "status": "success",
                "type": "analysis",
            },
        ],
        "agent_id": AGENT_ID,
        "goal": task["goal"],
        "output": {
            "line_count": analysis["line_count"],
            "summary": analysis["summary"],
            "word_count": analysis["word_count"],
        },
        "result": "completed",
        "schema_version": "titmas.execution-record.v0.1",
        "task_id": task["task_id"],
    }


def write_records(execution_record: dict[str, Any]) -> None:
    """Write ordered execution events as deterministic JSON Lines."""

    events = [
        {
            "agent_id": AGENT_ID,
            "event_id": f"event-{action['sequence']:03d}",
            "event_type": action["type"],
            "sequence": action["sequence"],
            "status": action["status"],
            "task_id": execution_record["task_id"],
        }
        for action in execution_record["actions"]
    ]
    events.append(
        {
            "agent_id": AGENT_ID,
            "event_id": "event-003",
            "event_type": "task_completed",
            "sequence": 3,
            "status": "success",
            "task_id": execution_record["task_id"],
        }
    )
    RECORDS_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = "".join(
        json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n"
        for event in events
    )
    RECORDS_PATH.write_text(payload, encoding="utf-8")


def build_evidence_bundle(execution_record: dict[str, Any]) -> dict[str, Any]:
    """Create and verify the bounded evidence-bundle artifacts."""

    manifest = {
        "agent_id": AGENT_ID,
        "artifacts": [
            {
                "path": "../execution-record.json",
                "sha256": sha256_file(EXECUTION_RECORD_PATH),
            },
            {"path": "records.jsonl", "sha256": sha256_file(RECORDS_PATH)},
        ],
        "evidence_id": EVIDENCE_ID,
        "schema_version": "titmas.evidence-bundle-manifest.v0.1",
        "task_id": execution_record["task_id"],
    }
    write_json(MANIFEST_PATH, manifest)

    declared_digests = {
        artifact["path"]: artifact["sha256"] for artifact in manifest["artifacts"]
    }
    known_paths = {
        "../execution-record.json": EXECUTION_RECORD_PATH,
        "manifest.json": MANIFEST_PATH,
        "records.jsonl": RECORDS_PATH,
    }
    checks = [
        {
            "path": "../execution-record.json",
            "sha256": declared_digests["../execution-record.json"],
        },
        {"path": "manifest.json", "sha256": sha256_file(MANIFEST_PATH)},
        {"path": "records.jsonl", "sha256": declared_digests["records.jsonl"]},
    ]
    verified = all(
        sha256_file(known_paths[check["path"]]) == check["sha256"]
        for check in checks
    )
    integrity = {
        "algorithm": "SHA-256",
        "checks": checks,
        "evidence_id": EVIDENCE_ID,
        "schema_version": "titmas.evidence-integrity.v0.1",
        "verification": "passed" if verified else "failed",
    }
    write_json(INTEGRITY_PATH, integrity)
    if not verified:
        raise RuntimeError("evidence bundle verification failed")
    return integrity


def build_health_report(
    task: dict[str, Any], execution_record: dict[str, Any], integrity: dict[str, Any]
) -> dict[str, Any]:
    """Express operational health as explicit states, never a composite score."""

    all_actions_succeeded = all(
        action["status"] == "success" for action in execution_record["actions"]
    )
    return {
        "agent": AGENT_ID,
        "assessment": {
            "evidence_integrity": (
                "verified" if integrity["verification"] == "passed" else "unverified"
            ),
            "execution_stability": (
                "healthy" if all_actions_succeeded else "needs_review"
            ),
            "recovery_ability": (
                "available"
                if task["recovery_policy"] == "retry_once"
                else "not_declared"
            ),
        },
        "basis": {
            "evidence_integrity": "all declared SHA-256 digests matched",
            "execution_stability": "all actions completed in one controlled run",
            "recovery_ability": "retry_once policy declared",
        },
        "limitations": [
            "single deterministic local run",
            "recovery path declared but not exercised",
            "not a safety, correctness, or production assessment",
        ],
        "schema_version": "titmas.health-report.v0.1",
        "task_id": execution_record["task_id"],
    }


def build_audit_receipt(
    execution_record: dict[str, Any], integrity: dict[str, Any]
) -> dict[str, Any]:
    """Create a local receipt linked to verified evidence artifacts."""

    return {
        "evidence_id": EVIDENCE_ID,
        "health_report_sha256": sha256_file(HEALTH_REPORT_PATH),
        "integrity_record_sha256": sha256_file(INTEGRITY_PATH),
        "limitations": [
            "local demo receipt only",
            "not legal compliance, certification, or execution authorization",
        ],
        "receipt_id": AUDIT_RECEIPT_ID,
        "schema_version": "titmas.audit-receipt.v0.1",
        "task_id": execution_record["task_id"],
        "verification": integrity["verification"],
    }


def run() -> None:
    """Execute the complete Golden Path and write deterministic outputs."""

    task, input_path = read_task()
    analysis = analyze_file(input_path)
    execution_record = build_execution_record(task, input_path, analysis)

    write_json(EXECUTION_RECORD_PATH, execution_record)
    write_records(execution_record)
    integrity = build_evidence_bundle(execution_record)

    health_report = build_health_report(task, execution_record, integrity)
    write_json(HEALTH_REPORT_PATH, health_report)

    audit_receipt = build_audit_receipt(execution_record, integrity)
    write_json(AUDIT_RECEIPT_PATH, audit_receipt)

    print("TITMAS Golden Path Complete")
    print("Execution Record: CREATED")
    print("Evidence Bundle: VERIFIED")
    print("Health Report: GENERATED")
    print("Audit Receipt: CREATED")


if __name__ == "__main__":
    run()
