import csv
import json
from datetime import date
from pathlib import Path

from .models import Task

EXPECTED_HEADER = ["title", "importance", "effort_h", "deadline"]


def _parse_row(row: list[str], line_num: int) -> Task:
    if len(row) != 4:
        raise ValueError(f"line {line_num}: expected 4 columns, got {len(row)}")

    try:
        title = row[0].strip()
        importance = int(row[1])
        effort_h = float(row[2])
        deadline = date.fromisoformat(row[3].strip())
        return Task(
            title=title, importance=importance, effort_h=effort_h, deadline=deadline
        )
    except ValueError as err:
        raise ValueError(f"line {line_num}: {err}") from err


def load_tasks(path: str | Path) -> list[Task]:
    file_path = Path(path)
    tasks: list[Task] = []

    with file_path.open(mode="r", encoding="utf-8", newline="") as csv_file:
        reader = csv.reader(csv_file)
        try:
            header = next(reader)
        except StopIteration:
            raise ValueError("line 1: empty file") from None

        cleaned_header = [col.strip() for col in header]
        if cleaned_header != EXPECTED_HEADER:
            expected_str = ",".join(EXPECTED_HEADER)
            raise ValueError(
                f"line 1: expected header '{expected_str}', got '{','.join(cleaned_header)}'"
            )

        for line_num, row in enumerate(reader, start=2):
            if not row:
                continue
            tasks.append(_parse_row(row, line_num))

    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    file_path = Path(path)
    data = [
        {
            "title": task.title,
            "importance": task.importance,
            "effort_h": task.effort_h,
            "deadline": task.deadline.isoformat(),
        }
        for task in tasks
    ]
    with file_path.open(mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=2)
