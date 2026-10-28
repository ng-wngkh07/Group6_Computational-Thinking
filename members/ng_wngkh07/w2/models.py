from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        """Validate the task importance."""
        if self.importance < 1 or self.importance > 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Return days until the deadline, with a minimum of zero."""
        remaining_days = (self.deadline - today).days
        if remaining_days < 0:
            return 0
        return remaining_days
