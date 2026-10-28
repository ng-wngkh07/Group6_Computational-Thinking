import argparse
import math
import sys
from datetime import date

from members.ng_wngkh07.w2.io_utils import load_tasks
from members.ng_wngkh07.w2.models import Task


def order_tasks(tasks: list[Task], today: date) -> list[Task]:
    """Order tasks by importance divided by remaining days."""
    def priority(task: Task) -> float:
        """Calculate the priority of one task, using one day at minimum."""
        days_left = task.days_left(today)
        if days_left == 0:
            days_left = 1
        return task.importance / days_left

    return sorted(tasks, key=priority, reverse=True)


def print_plan(tasks: list[Task], hours: float) -> None:
    """Print tasks in order until the available hours are used."""
    print(f"Tonight ({hours:.1f} h):")
    remaining_hours = hours
    number = 1

    for task in tasks:
        if remaining_hours <= 0:
            break
        if task.effort_h <= 0:
            continue

        if task.effort_h > remaining_hours:
            allocated_hours = remaining_hours
        else:
            allocated_hours = task.effort_h

        print(f"  {number}. {task.title} ...... {allocated_hours:.1f} h")
        remaining_hours -= allocated_hours
        number += 1


def main() -> int:
    """Read arguments and print a plan from a Week 2 task CSV."""
    parser = argparse.ArgumentParser(description="Create a study plan.")
    parser.add_argument("csv_path", help="Path to the task CSV file")
    parser.add_argument("--hours", type=float, required=True)
    parser.add_argument("--today", type=date.fromisoformat, default=None)
    args = parser.parse_args()

    if not math.isfinite(args.hours) or args.hours < 0:
        print("Error: hours must be a finite, non-negative number.", file=sys.stderr)
        return 1

    today = args.today
    if today is None:
        today = date.today()

    try:
        tasks = load_tasks(args.csv_path)
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    for task in tasks:
        if not math.isfinite(task.effort_h) or task.effort_h < 0:
            print("Error: task hours must be finite and non-negative.", file=sys.stderr)
            return 1

    ordered_tasks = order_tasks(tasks, today)
    print_plan(ordered_tasks, args.hours)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
