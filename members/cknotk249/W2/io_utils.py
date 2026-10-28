import csv
import json
from datetime import date
from pathlib import Path
from typing import Iterable

from .models import Task

EXPECTED_HEADER = ["title", "importance", "effort_h", "deadline"]


def load_tasks(path: str | Path) -> list[Task]:
    """Đọc danh sách Task từ file CSV. Quăng ValueError kèm số dòng nếu dòng không hợp lệ."""
    tasks: list[Task] = []
    with open(path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            raise ValueError("Line 1: Empty CSV file, missing header")

        if [col.strip() for col in header] != EXPECTED_HEADER:
            raise ValueError(f"Line 1: Invalid header {header}, expected {EXPECTED_HEADER}")

        for line_num, row in enumerate(reader, start=2):
            if len(row) != 4:
                raise ValueError(f"Line {line_num}: Expected 4 columns, got {len(row)}")

            raw_title, raw_importance, raw_effort, raw_deadline = [cell.strip() for cell in row]
            if not raw_title:
                raise ValueError(f"Line {line_num}: Title cannot be empty")

            try:
                importance = int(raw_importance)
                effort_h = float(raw_effort)
                deadline = date.fromisoformat(raw_deadline)
                task = Task(
                    title=raw_title,
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
            except ValueError as err:
                raise ValueError(f"Line {line_num}: {err}") from err

            tasks.append(task)

    return tasks


def save_json(tasks: Iterable[Task], path: str | Path) -> None:
    """Lưu danh sách Task ra file JSON."""
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