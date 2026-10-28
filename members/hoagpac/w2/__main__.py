from pathlib import Path

from .io_utils import load_tasks


def main() -> None:
    project_root = Path(__file__).resolve().parents[3]
    sample_path = project_root / "samples" / "tasks.csv"
    tasks = load_tasks(sample_path)
    for task in tasks:
        print(f"{task.title}: importance={task.importance}, effort={task.effort_h}h, deadline={task.deadline}")


if __name__ == "__main__":
    main()
