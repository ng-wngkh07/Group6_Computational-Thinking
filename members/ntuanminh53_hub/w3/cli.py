"""Command-line study planner tool."""

import argparse
import math
import sys
from datetime import date
from pathlib import Path

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise


def main() -> int:
    """Run CLI tool to schedule study blocks from a tasks CSV file."""
    parser = argparse.ArgumentParser(description="Study planner CLI")
    parser.add_argument("csv_path", help="Path to tasks CSV file")
    parser.add_argument("--hours", type=float, required=True, help="Available study hours")
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        help="Current date in YYYY-MM-DD format (default: today)",
    )
    args = parser.parse_args()

    today = args.today or date.today()

    csv_file = Path(args.csv_path)
    if not csv_file.is_file():
        print(f"Error: file not found: {args.csv_path}", file=sys.stderr)
        return 1

    if not math.isfinite(args.hours) or args.hours < 0:
        print("Error: hours must be a finite, non-negative number.", file=sys.stderr)
        return 1

    try:
        tasks = parse_csv(csv_file)
    except (OSError, ValueError) as err:
        print(f"Error parsing CSV: {err}", file=sys.stderr)
        return 1

    sorted_tasks = prioritise(tasks, today)
    blocks = allocate(sorted_tasks, args.hours)

    print(f"Tonight ({args.hours:.1f} h):")
    for idx, block in enumerate(blocks, start=1):
        dots = "." * max(2, 18 - len(block.task.title))
        print(f"  {idx}. {block.task.title} {dots} {block.hours:.1f} h")

    return 0


if __name__ == "__main__":
    sys.exit(main())
