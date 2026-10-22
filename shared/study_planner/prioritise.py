from datetime import date

from shared.contract import Task


def prioritise(tasks: list[Task], today: date) -> list[Task]:
    def calculate_priority(task: Task) -> float:
        remaining_days = task.days_left(today)
        if remaining_days == 0:
            return float(task.importance)

        priority_score = task.importance / remaining_days
        return priority_score

    sorted_tasks = sorted(tasks, key=calculate_priority, reverse=True)
    return sorted_tasks
