from .models import Task


class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float) -> None:
        """Store the hours needed and available."""
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(needed_h, available_h)

    def __str__(self) -> str:
        """Describe why the plan is infeasible."""
        message = (
            f"Need {self.needed_h:g} hours, "
            f"but only {self.available_h:g} hours are available."
        )
        return message


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Raise an error if tasks need more than the available hours."""
    needed_hours = 0
    for task in tasks:
        needed_hours = needed_hours + task.effort_h

    if needed_hours > available_h:
        raise InfeasiblePlan(needed_hours, available_h)
