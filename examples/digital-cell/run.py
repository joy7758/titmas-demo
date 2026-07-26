#!/usr/bin/env python3
"""Run the local deterministic TITMAS Digital Cell Demo v0.1."""

from pathlib import Path

from digital_cell import run_demo


DEMO_ROOT = Path(__file__).resolve().parent
INPUT_PATH = DEMO_ROOT / "input" / "sample.txt"
OUTPUT_DIR = DEMO_ROOT / "output"


def main() -> None:
    """Run the demonstration and write its local artifacts."""

    document = INPUT_PATH.read_text(encoding="utf-8")
    cell = run_demo(document)
    cell.write_outputs(OUTPUT_DIR)

    verified = all(record.verify() for record in cell.evidence)
    response = cell.immune_responses[-1]

    print("TITMAS Digital Cell Demo Complete")
    print("Digital Cell: CREATED")
    print("Task Execution: COMPLETED")
    print(f"Evidence: {'VERIFIED' if verified else 'FAILED'}")
    print("Health: DERIVED")
    print(f"Immune Response: LEVEL_{response.level}_{response.name}")
    print("Memory: UPDATED")
    print(f"Lifecycle: {cell.lifecycle_state}")
    print(f"Report: {OUTPUT_DIR / 'TITMAS-DIGITAL-CELL-REPORT.md'}")


if __name__ == "__main__":
    main()
