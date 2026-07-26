"""Acceptance tests for the deterministic TITMAS Digital Cell Demo v0.1."""

from dataclasses import replace
from pathlib import Path
import sys
import unittest


DEMO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(DEMO_ROOT))

from digital_cell import Boundary, DigitalCell, run_demo  # noqa: E402


SAMPLE_DOCUMENT = (
    "Digital cells preserve bounded execution history as verifiable evidence.\n"
    "This test uses no external model.\n"
)


def create_registered_cell() -> DigitalCell:
    """Create a minimal registered cell for focused tests."""

    cell = DigitalCell.create(
        cell_id="test-cell-001",
        owner="test-owner",
        version="v0.1",
        purpose="Analyze a bounded test document",
        capabilities=("analyze_document",),
        boundary=Boundary(
            allowed_actions=("analyze_document",),
            forbidden_actions=("delete_document",),
            resource_limits={"max_units_per_action": 10},
        ),
    )
    cell.register()
    return cell


class DigitalCellDemoTests(unittest.TestCase):
    """Verify every acceptance capability without external dependencies."""

    def test_identity_creation(self) -> None:
        cell = DigitalCell.create(
            cell_id="test-cell-identity",
            owner="test-owner",
            version="v0.1",
            purpose="Identity test",
            capabilities=("analyze_document",),
            boundary=Boundary(
                allowed_actions=("analyze_document",),
                forbidden_actions=("delete_document",),
                resource_limits={"max_units_per_action": 1},
            ),
        )

        self.assertEqual(cell.identity.cell_id, "test-cell-identity")
        self.assertEqual(cell.lifecycle_state, "BIRTH")
        self.assertEqual(cell.evidence[0].execution_event["to"], "BIRTH")

    def test_boundary_check(self) -> None:
        cell = create_registered_cell()

        self.assertTrue(cell.check_boundary("analyze_document"))
        self.assertFalse(cell.check_boundary("delete_document"))
        self.assertFalse(cell.check_boundary("unknown_action"))
        self.assertFalse(cell.check_boundary("analyze_document", resource_cost=11))

    def test_evidence_generation(self) -> None:
        cell = create_registered_cell()
        cell.execute_document_task(SAMPLE_DOCUMENT)

        self.assertGreaterEqual(len(cell.evidence), 6)
        self.assertTrue(all(record.event_id for record in cell.evidence))
        self.assertTrue(all(record.verify() for record in cell.evidence))

    def test_hash_verification(self) -> None:
        cell = create_registered_cell()
        original = cell.evidence[0]
        tampered = replace(original, action="tampered_action")

        self.assertTrue(original.verify())
        self.assertFalse(tampered.verify())

    def test_health_calculation(self) -> None:
        cell = create_registered_cell()
        cell.execute_document_task(SAMPLE_DOCUMENT)

        self.assertEqual(cell.health.identity_health, "HEALTHY")
        self.assertEqual(cell.health.evidence_health, "VERIFIED")
        self.assertEqual(cell.health.execution_health, "HEALTHY")
        self.assertEqual(cell.health.risk_level, "LOW")

    def test_abnormal_event_response(self) -> None:
        cell = create_registered_cell()
        cell.execute_document_task(SAMPLE_DOCUMENT)
        response = cell.attempt_abnormal_action("delete_document")

        self.assertEqual(response.level, 2)
        self.assertEqual(response.name, "RESTRICTION")
        self.assertEqual(cell.health.risk_level, "HIGH")
        self.assertEqual(len(cell.memory.failure_history), 1)
        self.assertEqual(len(cell.memory.immune_response_history), 1)

    def test_lifecycle_transition(self) -> None:
        cell = run_demo(SAMPLE_DOCUMENT)
        observed_states = [
            record.execution_event["to"]
            for record in cell.evidence
            if record.action == "lifecycle_transition"
        ]

        self.assertEqual(
            observed_states,
            [
                "BIRTH",
                "REGISTERED",
                "EXECUTING",
                "OBSERVED",
                "ASSESSED",
                "RECOVERED",
                "EVOLVED",
            ],
        )
        self.assertEqual(cell.lifecycle_state, "EVOLVED")
        self.assertEqual(len(cell.memory.recovery_history), 1)
        self.assertEqual(len(cell.memory.evolution_history), 1)


if __name__ == "__main__":
    unittest.main()
