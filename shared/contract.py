from dataclasses import dataclass
from datetime import date
from math import isfinite


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        if self.importance < 1 or self.importance > 5:
            raise ValueError("importance must be 1-5")

        if not isfinite(self.effort_h):
            raise ValueError("effort_h must be finite and non-negative")
        if self.effort_h < 0:
            raise ValueError("effort_h must be finite and non-negative")

    def days_left(self, today: date) -> int:
        remaining_days = (self.deadline - today).days
        if remaining_days < 0:
            return 0
        return remaining_days


@dataclass
class Block:
    task: Task
    hours: float
