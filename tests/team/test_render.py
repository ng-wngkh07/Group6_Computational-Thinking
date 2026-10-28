from datetime import date

from shared.contract import Block, Task
from shared.study_planner.render import render


def test_readable_plan_has_titles_hours_and_total(capsys):
    assignment = Task("Assignment", 4, 1.5, date(2026, 10, 27))
    exam = Task("DS exam", 5, 6, date(2026, 10, 30))
    text = render([Block(assignment, 1.5), Block(exam, 0.5)])
    assert text == (
        "Study plan\n1. Assignment: 1.5 hours\n2. DS exam: 0.5 hours\nTotal: 2 hours"
    )
    assert capsys.readouterr().out == ""


def test_empty_plan():
    assert render([]) == "No study blocks."


def test_unicode_title():
    task = Task("Ôn Python", 3, 1, date(2026, 10, 30))
    assert "Ôn Python" in render([Block(task, 1)])
