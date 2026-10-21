import csv
import json
from datetime import date
from pathlib import Path

from .models import Task


def load_tasks(path: str | Path) -> list[Task]:
    tasks = []
    with open(path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header != ["title", "importance", "effort_h", "deadline"]:
            raise ValueError("line 1: invalid header")

        for line_num, row in enumerate(reader, start=2):
            if not row:
                continue
            try:
                if len(row) != 4:
                    raise ValueError("expected 4 columns")
                title = row[0]
                importance = int(row[1])
                effort_h = float(row[2])
                deadline = date.fromisoformat(row[3])
                tasks.append(Task(title, importance, effort_h, deadline))
            except Exception as e:
                raise ValueError(f"line {line_num}: {e}") from e

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    data = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat(),
        }
        for t in tasks
    ]
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
