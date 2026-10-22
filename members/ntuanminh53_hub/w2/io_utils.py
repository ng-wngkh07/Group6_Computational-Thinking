
import csv
import json
from datetime import date
from dataclasses import asdict

from .models import Task


def load_tasks(path) -> list[Task]:
    tasks = []

    with open(path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        required_fields = ["title", "importance", "effort_h", "deadline"]

        if reader.fieldnames != required_fields:
            raise ValueError("Invalid CSV header")

        for row in reader:
            line_number = reader.line_num

            try:
                task = Task(
                    title=row["title"],
                    importance=int(row["importance"]),
                    effort_h=float(row["effort_h"]),
                    deadline=date.fromisoformat(row["deadline"])
                )

                tasks.append(task)

            except (ValueError, TypeError, KeyError) as error:
                raise ValueError(
                    f"Invalid data at line {line_number}: {error}"
                ) from error

    return tasks


def save_json(tasks: list[Task], path) -> None:
    data = []

    for task in tasks:
        task_data = asdict(task)
        task_data["deadline"] = task.deadline.isoformat()
        data.append(task_data)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
