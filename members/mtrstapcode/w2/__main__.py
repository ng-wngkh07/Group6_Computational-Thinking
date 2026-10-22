import sys
from pathlib import Path

from .io_utils import load_tasks
from .models import Task


def print_tasks(tasks: list[Task]) -> None:
    for task in tasks:
        print(
            f"{task.title} | importance={task.importance} | "
            f"effort={task.effort_h:g} h | deadline={task.deadline.isoformat()}"
        )


def main() -> None:
    project_root = Path(__file__).resolve().parents[3]
    sample_path = project_root / "samples" / "tasks.csv"

    if not sample_path.is_file():
        print(f"Error: Sample tasks file not found at {sample_path}", file=sys.stderr)
        sys.exit(1)

    tasks = load_tasks(sample_path)
    print_tasks(tasks)


if __name__ == "__main__":
    main()
