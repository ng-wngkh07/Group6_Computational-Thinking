"""Run the shared study planner from the command line."""

import argparse
import math
import sys
from datetime import date
from pathlib import Path

from members.ng_wngkh07.w2.errors import InfeasiblePlan, check_feasible
from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def main() -> int:
    """Read tasks, report input issues, and display an available study plan."""
    parser = argparse.ArgumentParser(description="Create a study plan from a CSV file.")
    parser.add_argument("csv_file", help="path to the task CSV file")
    parser.add_argument("--hours", type=float, required=True, help="available study hours")
    parser.add_argument(
        "--today",
        type=date.fromisoformat,
        default=None,
        help="reference date in YYYY-MM-DD format (default: today)",
    )
    args = parser.parse_args()

    if not math.isfinite(args.hours) or args.hours < 0:
        print("Error: hours must be a finite, non-negative number.", file=sys.stderr)
        return 1

    csv_path = Path(args.csv_file)
    try:
        if csv_path.stat().st_size == 0:
            print(f"Error: CSV file is empty: {csv_path}", file=sys.stderr)
            return 1
        tasks = parse_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: CSV file not found: {csv_path}", file=sys.stderr)
        return 1
    except (OSError, ValueError) as error:
        print(f"Error: could not read tasks from {csv_path}: {error}", file=sys.stderr)
        return 1

    if not tasks:
        print(f"Error: CSV file contains no tasks: {csv_path}", file=sys.stderr)
        return 1

    try:
        check_feasible(tasks, args.hours)
    except InfeasiblePlan as error:
        print(
            f"Warning: {error} A partial plan will be shown.",
            file=sys.stderr,
        )

    today = args.today or date.today()
    sorted_tasks = prioritise(tasks, today)
    blocks = allocate(sorted_tasks, args.hours)
    plan = render(blocks)
    print(plan)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
