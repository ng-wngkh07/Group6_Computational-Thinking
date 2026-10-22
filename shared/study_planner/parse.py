import csv
from datetime import date
from pathlib import Path

from shared.contract import Task

HEADER = ["title", "importance", "effort_h", "deadline"]


def read_csv_row(reader, line_number):
    try:
        row = next(reader, None)
    except csv.Error as error:
        raise ValueError(f"line {line_number}: {error}") from error
    return row


def create_task_from_row(row: list[str], line_number: int) -> Task:
    try:
        if len(row) != 4:
            raise ValueError("expected 4 columns")

        title = row[0]
        importance = int(row[1])
        effort_hours = float(row[2])
        deadline = date.fromisoformat(row[3])

        task = Task(title, importance, effort_hours, deadline)
    except ValueError as error:
        raise ValueError(f"line {line_number}: {error}") from error
    return task


def parse_csv(path: str | Path) -> list[Task]:
    tasks = []

    with open(path, encoding="utf-8", newline="") as csv_file:
        reader = csv.reader(csv_file, strict=True)
        header = read_csv_row(reader, 1)
        if header != HEADER:
            expected_header = ",".join(HEADER)
            raise ValueError(f"line 1: expected header {expected_header}")

        while True:
            line_number = reader.line_num + 1
            row = read_csv_row(reader, line_number)
            if row is None:
                break

            task = create_task_from_row(row, line_number)
            tasks.append(task)

    return tasks
