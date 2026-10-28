from datetime import date

from shared.contract import Task
from shared.study_planner.prioritise import prioritise

TODAY = date(2026, 10, 26)


def test_priority_ratio_and_original_list_unchanged():
    exam = Task("DS exam", 5, 6, date(2026, 10, 30))
    assignment = Task("Assignment", 4, 1.5, date(2026, 10, 27))
    tasks = [exam, assignment]
    assert prioritise(tasks, TODAY) == [assignment, exam]
    assert tasks == [exam, assignment]


def test_today_and_overdue_use_one_day():
    future = Task("Future", 5, 1, date(2026, 10, 31))
    due = Task("Due", 2, 1, TODAY)
    overdue = Task("Overdue", 3, 1, date(2026, 10, 25))
    assert prioritise([future, due, overdue], TODAY) == [overdue, due, future]


def test_equal_scores_preserve_input_order():
    first = Task("Z", 4, 1, date(2026, 10, 28))
    second = Task("A", 2, 1, date(2026, 10, 27))
    assert prioritise([first, second], TODAY) == [first, second]


def test_empty_list():
    assert prioritise([], TODAY) == []
