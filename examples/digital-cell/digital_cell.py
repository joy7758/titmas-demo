#!/usr/bin/env python3
"""Deterministic TITMAS Digital Cell Demo v0.1 domain model."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field, replace
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
from typing import Any


DEMO_EPOCH = datetime(2026, 7, 26, 0, 0, 0, tzinfo=timezone.utc)

LIFECYCLE_TRANSITIONS = {
    "BIRTH": {"REGISTERED"},
    "REGISTERED": {"EXECUTING"},
    "EXECUTING": {"OBSERVED"},
    "OBSERVED": {"ASSESSED"},
    "ASSESSED": {"RECOVERED"},
    "RECOVERED": {"EVOLVED"},
    "EVOLVED": set(),
}


def canonical_json(value: Any) -> str:
    """Serialize a value deterministically for hashing."""

    return json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )


def pretty_json(value: Any) -> str:
    """Serialize a value deterministically for readable artifacts."""

    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def sha256_value(value: Any) -> str:
    """Return the SHA-256 digest of a canonical JSON value."""

    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class Identity:
    """Versioned identity declaration for one Digital Cell."""

    cell_id: str
    owner: str
    version: str
    purpose: str
    capabilities: tuple[str, ...]


@dataclass(frozen=True)
class Boundary:
    """Explicit action and resource boundary."""

    allowed_actions: tuple[str, ...]
    forbidden_actions: tuple[str, ...]
    resource_limits: dict[str, int]


@dataclass(frozen=True)
class EvidenceRecord:
    """Integrity-verifiable history record, not a correctness claim."""

    event_id: str
    timestamp: str
    intent: str
    action: str
    execution_event: dict[str, Any]
    input_hash: str
    output_hash: str
    evidence_hash: str
    verification_status: str
    integrity_status: str

    @classmethod
    def create(
        cls,
        *,
        event_id: str,
        timestamp: str,
        intent: str,
        action: str,
        execution_event: dict[str, Any],
        input_data: Any,
        output_data: Any,
    ) -> EvidenceRecord:
        """Create a verified evidence record from immutable event material."""

        unsigned = {
            "action": action,
            "event_id": event_id,
            "execution_event": execution_event,
            "input_hash": sha256_value(input_data),
            "intent": intent,
            "output_hash": sha256_value(output_data),
            "timestamp": timestamp,
        }
        return cls(
            **unsigned,
            evidence_hash=sha256_value(unsigned),
            verification_status="VERIFIED",
            integrity_status="MATCH",
        )

    def unsigned_payload(self) -> dict[str, Any]:
        """Return the exact material covered by evidence_hash."""

        return {
            "action": self.action,
            "event_id": self.event_id,
            "execution_event": self.execution_event,
            "input_hash": self.input_hash,
            "intent": self.intent,
            "output_hash": self.output_hash,
            "timestamp": self.timestamp,
        }

    def verify(self) -> bool:
        """Verify integrity without claiming that an output is correct."""

        return (
            self.evidence_hash == sha256_value(self.unsigned_payload())
            and self.verification_status == "VERIFIED"
            and self.integrity_status == "MATCH"
        )


@dataclass
class HealthState:
    """Derived operational view with no authority effect."""

    identity_health: str = "UNKNOWN"
    evidence_health: str = "UNKNOWN"
    execution_health: str = "UNKNOWN"
    adaptation_state: str = "BASELINE"
    risk_level: str = "UNKNOWN"


@dataclass
class Memory:
    """Append-only demo memory for execution, failure, recovery, and evolution."""

    execution_history: list[dict[str, Any]] = field(default_factory=list)
    failure_history: list[dict[str, Any]] = field(default_factory=list)
    recovery_history: list[dict[str, Any]] = field(default_factory=list)
    immune_response_history: list[dict[str, Any]] = field(default_factory=list)
    evolution_history: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class Reputation:
    """Contextual demo assessment, never authority or permission."""

    reliability: float = 0.0
    evidence_quality: float = 0.0
    contribution_score: float = 0.0


@dataclass(frozen=True)
class ImmuneResponse:
    """Bounded response record for one observed abnormal event."""

    response_id: str
    level: int
    name: str
    trigger_event_id: str
    action: str
    recovery_possible: bool
    status: str


@dataclass
class DigitalCell:
    """Minimal Digital Cell = agent identity plus immune structure."""

    identity: Identity
    boundary: Boundary
    health: HealthState
    memory: Memory
    reputation: Reputation
    lifecycle_state: str
    evidence: list[EvidenceRecord] = field(default_factory=list)
    immune_responses: list[ImmuneResponse] = field(default_factory=list)
    _event_counter: int = field(default=0, repr=False)

    @classmethod
    def create(
        cls,
        *,
        cell_id: str,
        owner: str,
        version: str,
        purpose: str,
        capabilities: tuple[str, ...],
        boundary: Boundary,
    ) -> DigitalCell:
        """Create a Digital Cell and evidence its Birth state."""

        cell = cls(
            identity=Identity(
                cell_id=cell_id,
                owner=owner,
                version=version,
                purpose=purpose,
                capabilities=capabilities,
            ),
            boundary=boundary,
            health=HealthState(),
            memory=Memory(),
            reputation=Reputation(),
            lifecycle_state="BIRTH",
        )
        cell._record_event(
            intent="Create a bounded digital subject",
            action="lifecycle_transition",
            execution_event={"from": None, "to": "BIRTH", "status": "SUCCESS"},
            input_data={},
            output_data=asdict(cell.identity),
        )
        return cell

    def _next_event_identity(self) -> tuple[str, str]:
        """Return deterministic event identity and logical timestamp."""

        self._event_counter += 1
        event_id = f"event-{self._event_counter:03d}"
        timestamp = (DEMO_EPOCH + timedelta(seconds=self._event_counter)).isoformat()
        return event_id, timestamp

    def _record_event(
        self,
        *,
        intent: str,
        action: str,
        execution_event: dict[str, Any],
        input_data: Any,
        output_data: Any,
    ) -> EvidenceRecord:
        """Append one integrity-verifiable event to the evidence history."""

        event_id, timestamp = self._next_event_identity()
        record = EvidenceRecord.create(
            event_id=event_id,
            timestamp=timestamp,
            intent=intent,
            action=action,
            execution_event=execution_event,
            input_data=input_data,
            output_data=output_data,
        )
        self.evidence.append(record)
        return record

    def transition(self, target_state: str, reason: str) -> EvidenceRecord:
        """Perform an allowed lifecycle transition and generate evidence."""

        allowed_targets = LIFECYCLE_TRANSITIONS[self.lifecycle_state]
        if target_state not in allowed_targets:
            raise ValueError(
                f"invalid lifecycle transition: {self.lifecycle_state} -> {target_state}"
            )

        previous_state = self.lifecycle_state
        self.lifecycle_state = target_state
        return self._record_event(
            intent=reason,
            action="lifecycle_transition",
            execution_event={
                "from": previous_state,
                "status": "SUCCESS",
                "to": target_state,
            },
            input_data={"state": previous_state},
            output_data={"state": target_state},
        )

    def register(self) -> EvidenceRecord:
        """Register the cell in the local demo lifecycle."""

        return self.transition("REGISTERED", "Register Digital Cell identity")

    def check_boundary(self, action: str, resource_cost: int = 1) -> bool:
        """Return whether an action is declared and within local resource limits."""

        if action in self.boundary.forbidden_actions:
            return False
        if action not in self.boundary.allowed_actions:
            return False
        max_units = self.boundary.resource_limits.get("max_units_per_action", 0)
        return 0 <= resource_cost <= max_units

    def execute_document_task(self, content: str) -> dict[str, Any]:
        """Execute one deterministic, bounded document-analysis task."""

        if self.lifecycle_state != "REGISTERED":
            raise ValueError("cell must be REGISTERED before task execution")
        if not self.check_boundary("analyze_document", resource_cost=1):
            raise PermissionError("analyze_document is outside the cell boundary")

        self.transition("EXECUTING", "Begin bounded document analysis")
        nonempty_lines = [line.strip() for line in content.splitlines() if line.strip()]
        if not nonempty_lines:
            raise ValueError("document must contain at least one non-empty line")

        result = {
            "line_count": len(content.splitlines()),
            "summary": nonempty_lines[0],
            "word_count": len(content.split()),
        }
        execution = {
            "action": "analyze_document",
            "input_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
            "result": result,
            "status": "SUCCESS",
        }
        self.memory.execution_history.append(execution)
        self._record_event(
            intent="Analyze a local document",
            action="analyze_document",
            execution_event={"status": "SUCCESS"},
            input_data={"content": content},
            output_data=result,
        )
        self.transition("OBSERVED", "Record task execution observation")
        self.transition("ASSESSED", "Assess evidence-backed operational health")
        self.assess_health()
        self.reputation.reliability = 1.0
        self.reputation.evidence_quality = 1.0
        self.reputation.contribution_score = 1.0
        return result

    def assess_health(self) -> HealthState:
        """Derive health from identity, evidence, execution, and recovery history."""

        identity_complete = bool(
            self.identity.cell_id
            and self.identity.owner
            and self.identity.version
            and self.identity.purpose
            and self.identity.capabilities
        )
        evidence_complete = bool(self.evidence) and all(
            record.verify() for record in self.evidence
        )
        execution_success = bool(self.memory.execution_history) and all(
            event["status"] == "SUCCESS"
            for event in self.memory.execution_history
        )
        recovery_observed = bool(self.memory.recovery_history)

        self.health = HealthState(
            identity_health="HEALTHY" if identity_complete else "INCOMPLETE",
            evidence_health="VERIFIED" if evidence_complete else "DEGRADED",
            execution_health="HEALTHY" if execution_success else "DEGRADED",
            adaptation_state="RECOVERED" if recovery_observed else "BASELINE",
            risk_level=(
                "LOW"
                if identity_complete and evidence_complete and execution_success
                else "MEDIUM"
            ),
        )
        return self.health

    def attempt_abnormal_action(self, action: str) -> ImmuneResponse:
        """Simulate a denied boundary violation and record a Level 2 response."""

        if self.lifecycle_state != "ASSESSED":
            raise ValueError("abnormal event simulation requires ASSESSED state")
        if self.check_boundary(action):
            raise ValueError("abnormal action must be outside the declared boundary")

        violation = self._record_event(
            intent="Attempt an action outside the declared boundary",
            action="boundary_violation_attempt",
            execution_event={
                "attempted_action": action,
                "reason": "FORBIDDEN_OR_UNDECLARED",
                "status": "DENIED",
            },
            input_data={"action": action, "boundary": asdict(self.boundary)},
            output_data={"executed": False, "status": "DENIED"},
        )
        failure = {
            "action": action,
            "event_id": violation.event_id,
            "result": "DENIED",
            "type": "BOUNDARY_VIOLATION_ATTEMPT",
        }
        self.memory.failure_history.append(failure)
        self.health.execution_health = "DEGRADED"
        self.health.adaptation_state = "RESPONSE_REQUIRED"
        self.health.risk_level = "HIGH"
        self.reputation.reliability = 0.5

        response = ImmuneResponse(
            response_id=f"response-{len(self.immune_responses) + 1:03d}",
            level=2,
            name="RESTRICTION",
            trigger_event_id=violation.event_id,
            action="retain existing boundary and require recovery review",
            recovery_possible=True,
            status="APPLIED",
        )
        self.immune_responses.append(response)
        self.memory.immune_response_history.append(asdict(response))
        self._record_event(
            intent="Contain a recorded boundary violation",
            action="immune_response",
            execution_event={
                "level": response.level,
                "name": response.name,
                "status": response.status,
            },
            input_data=failure,
            output_data=asdict(response),
        )
        return response

    def recover(self) -> EvidenceRecord:
        """Record bounded recovery without erasing the abnormal event."""

        if self.lifecycle_state != "ASSESSED":
            raise ValueError("cell must be ASSESSED before recovery")
        if not self.memory.failure_history or not self.immune_responses:
            raise ValueError("recovery requires a recorded abnormal event")

        recovery = {
            "result": "RECOVERED_WITH_BOUNDARY_UNCHANGED",
            "response_id": self.immune_responses[-1].response_id,
            "retained_failure_event": self.memory.failure_history[-1]["event_id"],
        }
        self.memory.recovery_history.append(recovery)
        self._record_event(
            intent="Recover while preserving the original boundary",
            action="recovery",
            execution_event={"status": "SUCCESS"},
            input_data=asdict(self.immune_responses[-1]),
            output_data=recovery,
        )
        transition_record = self.transition(
            "RECOVERED", "Complete evidence-backed recovery"
        )
        self.assess_health()
        self.health.adaptation_state = "RECOVERED"
        self.health.risk_level = "LOW_AFTER_RECOVERY"
        return transition_record

    def evolve(self, new_version: str) -> EvidenceRecord:
        """Create a new identity version and preserve the version lineage."""

        if self.lifecycle_state != "RECOVERED":
            raise ValueError("cell must be RECOVERED before evolution")
        previous_version = self.identity.version
        evolution = {
            "from_version": previous_version,
            "reason": "incorporate recorded boundary-violation memory",
            "to_version": new_version,
        }
        self.identity = replace(self.identity, version=new_version)
        self.memory.evolution_history.append(evolution)
        self._record_event(
            intent="Evolve the cell identity version with preserved lineage",
            action="identity_version_evolution",
            execution_event={"status": "SUCCESS"},
            input_data={"version": previous_version},
            output_data=evolution,
        )
        return self.transition("EVOLVED", "Complete versioned Digital Cell evolution")

    def to_dict(self) -> dict[str, Any]:
        """Return the complete agent-readable Digital Cell state."""

        return {
            "boundary": asdict(self.boundary),
            "evidence": [asdict(record) for record in self.evidence],
            "health": asdict(self.health),
            "identity": asdict(self.identity),
            "immune_responses": [
                asdict(response) for response in self.immune_responses
            ],
            "lifecycle_state": self.lifecycle_state,
            "memory": asdict(self.memory),
            "reputation": asdict(self.reputation),
            "schema_version": "titmas.digital-cell-demo.v0.1",
        }

    def build_report(self) -> str:
        """Build the human-readable TITMAS Digital Cell report."""

        verified_count = sum(record.verify() for record in self.evidence)
        response = self.immune_responses[-1] if self.immune_responses else None
        execution_lines = [
            f"- `{event['action']}`: `{event['status']}`"
            for event in self.memory.execution_history
        ]
        failure_lines = [
            f"- `{event['type']}` / `{event['result']}` / `{event['event_id']}`"
            for event in self.memory.failure_history
        ]
        recovery_lines = [
            f"- `{event['result']}` linked to `{event['response_id']}`"
            for event in self.memory.recovery_history
        ]

        lines = [
            "# TITMAS DIGITAL CELL REPORT",
            "",
            "## Identity",
            "",
            f"- Cell ID: `{self.identity.cell_id}`",
            f"- Owner: `{self.identity.owner}`",
            f"- Version: `{self.identity.version}`",
            f"- Purpose: {self.identity.purpose}",
            f"- Capabilities: `{', '.join(self.identity.capabilities)}`",
            "",
            "## Boundary",
            "",
            f"- Allowed actions: `{', '.join(self.boundary.allowed_actions)}`",
            f"- Forbidden actions: `{', '.join(self.boundary.forbidden_actions)}`",
            f"- Resource limits: `{canonical_json(self.boundary.resource_limits)}`",
            "",
            "## Execution History",
            "",
            *(execution_lines or ["- No execution recorded"]),
            "",
            "## Evidence Summary",
            "",
            f"- Evidence records: `{len(self.evidence)}`",
            f"- Integrity verified: `{verified_count}/{len(self.evidence)}`",
            "- Evidence demonstrates execution history, not AI correctness.",
            "",
            "## Health State",
            "",
            f"- Identity health: `{self.health.identity_health}`",
            f"- Evidence health: `{self.health.evidence_health}`",
            f"- Execution health: `{self.health.execution_health}`",
            f"- Adaptation state: `{self.health.adaptation_state}`",
            f"- Risk level: `{self.health.risk_level}`",
            "- Health is a derived view, not Authority, Certification, or Permission.",
            "",
            "## Immune Response",
            "",
            (
                f"- Level {response.level}: `{response.name}` / `{response.status}`"
                if response
                else "- No immune response recorded"
            ),
            (
                f"- Trigger evidence: `{response.trigger_event_id}`"
                if response
                else ""
            ),
            "",
            "## Memory",
            "",
            "### Failure History",
            "",
            *(failure_lines or ["- No failure recorded"]),
            "",
            "### Recovery History",
            "",
            *(recovery_lines or ["- No recovery recorded"]),
            "",
            f"- Immune response records: `{len(self.memory.immune_response_history)}`",
            "",
            "## Evolution Status",
            "",
            f"- Lifecycle state: `{self.lifecycle_state}`",
            f"- Evolution records: `{len(self.memory.evolution_history)}`",
            f"- Current identity version: `{self.identity.version}`",
            "",
            "## Limitations",
            "",
            "- Local deterministic reference demo only.",
            "- No AI model, production runtime, external framework, or network service.",
            "- Does not prove digital life, AI consciousness, survival law, or production readiness.",
            "",
        ]
        return "\n".join(line for line in lines if line is not None)

    def write_outputs(self, output_dir: Path) -> None:
        """Write deterministic machine-readable evidence and readable report."""

        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "digital-cell-state.json").write_text(
            pretty_json(self.to_dict()),
            encoding="utf-8",
        )
        evidence_payload = "".join(
            canonical_json(asdict(record)) + "\n" for record in self.evidence
        )
        (output_dir / "evidence.jsonl").write_text(
            evidence_payload,
            encoding="utf-8",
        )
        (output_dir / "TITMAS-DIGITAL-CELL-REPORT.md").write_text(
            self.build_report(),
            encoding="utf-8",
        )


def run_demo(document: str) -> DigitalCell:
    """Execute the complete deterministic Digital Cell lifecycle."""

    cell = DigitalCell.create(
        cell_id="digital-cell-001",
        owner="local-demo-owner",
        version="v0.1",
        purpose="Analyze one bounded local document",
        capabilities=("analyze_document",),
        boundary=Boundary(
            allowed_actions=("analyze_document",),
            forbidden_actions=("delete_document", "external_network_call"),
            resource_limits={"max_units_per_action": 10},
        ),
    )
    cell.register()
    cell.execute_document_task(document)
    cell.attempt_abnormal_action("delete_document")
    cell.recover()
    cell.evolve("v0.2-demo")
    return cell
