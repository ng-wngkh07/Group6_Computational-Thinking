import argparse
from datetime import date
from pathlib import Path
import sys

from members.hoagpac.w2.io_utils import load_tasks


def main() -> None:
    parser = argparse.ArgumentParser(description="Study planner CLI")
    parser.add_argument("file", help="Path to tasks CSV file")
    parser.add_argument("--hours", type=float, required=True, help="Available study hours")
    parser.add_argument("--today", type=date.fromisoformat, default=date.today(), help="Current date (YYYY-MM-DD)")
    args = parser.parse_args()

    try:
        tasks = load_tasks(args.file)
    except Exception as e:
        print(f"Error loading tasks: {e}", file=sys.stderr)
        sys.exit(1)

    def priority(t):
        dl = t.days_left(args.today)
        return t.importance / (dl if dl > 0 else 1)

    sorted_tasks = sorted(tasks, key=priority, reverse=True)

    print(f"Tonight ({args.hours:.1f} h):")
    rem_h = args.hours
    for i, t in enumerate(sorted_tasks, start=1):
        if rem_h <= 0:
            break
        alloc = min(t.effort_h, rem_h)
        dots = "." * max(2, 18 - len(t.title))
        print(f"  {i}. {t.title} {dots} {alloc:.1f} h")
        rem_h -= alloc


if __name__ == "__main__":
    main()
