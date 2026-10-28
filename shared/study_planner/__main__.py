"""Run the shared study planner from the command line."""

import argparse
from datetime import date

from shared.study_planner.allocate import allocate
from shared.study_planner.parse import parse_csv
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def main() -> None:
    """Read tasks, make a study plan, and display it."""
    parser = argparse.ArgumentParser(description="Create a study plan from a CSV file.")
    parser.add_argument("csv_file", help="path to the task CSV file")
    parser.add_argument("--hours", type=float, required=True, help="available study hours")
    args = parser.parse_args()

    tasks = parse_csv(args.csv_file)
    sorted_tasks = prioritise(tasks, date.today())
    blocks = allocate(sorted_tasks, args.hours)
    plan = render(blocks)
    print(plan)


if __name__ == "__main__":
    main()
