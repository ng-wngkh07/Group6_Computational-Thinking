from pathlib import Path

from .io_utils import load_tasks
from .models import Task


def print_tasks(tasks: list[Task]) -> None:
    """Print the details of each task."""
    for task in tasks:
        task_details = (
            f"{task.title} | importance={task.importance} | "
            f"effort={task.effort_h:g} h | deadline={task.deadline.isoformat()}"
        )
        print(task_details)


def main() -> None:
    """Load and print the sample tasks."""
    project_root = Path(__file__).resolve().parents[3]
    sample_path = project_root / "samples" / "tasks.csv"
    tasks = load_tasks(sample_path)
    print_tasks(tasks)


if __name__ == "__main__":
    main()
