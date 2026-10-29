import csv
import json
from datetime import datetime
from .models import Task

def load_tasks(path: str) -> list[Task]:
    tasks = []
    with open(path, mode='r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)
        for i, row in enumerate(reader, start=2):
            try:
                title, importance, effort_h, deadline_str = row
                tasks.append(Task(
                    title=title,
                    importance=int(importance),
                    effort_h=float(effort_h),
                    deadline=datetime.strptime(deadline_str, "%Y-%m-%d").date()
                ))
            except (ValueError, IndexError) as e:
                raise ValueError(f"Invalid row on line {i}: {e}")
                
    return tasks

def save_json(tasks: list[Task], path: str) -> None:
    data = [
        {
            "title": t.title,
            "importance": t.importance,
            "effort_h": t.effort_h,
            "deadline": t.deadline.isoformat()
        } for t in tasks
    ]
    with open(path, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
