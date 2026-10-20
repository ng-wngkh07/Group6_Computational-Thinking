from datetime import date

import pytest

from shared.contract import Block, Task
from shared.study_planner.allocate import allocate


def create_sample_tasks():
    return [
        Task("Assignment", 4, 1.5, date(2026, 10, 27)),
        Task("DS exam", 5, 6, date(2026, 10, 30)),
    ]


def test_partial_task_and_input_unchanged():
    sample_tasks = create_sample_tasks()
    assert allocate(sample_tasks, 2) == [
        Block(sample_tasks[0], 1.5),
        Block(sample_tasks[1], 0.5),
    ]
    assert sample_tasks[0].effort_h == 1.5
    assert sample_tasks[1].effort_h == 6


def test_exact_budget():
    sample_tasks = create_sample_tasks()
    assert allocate(sample_tasks, 1.5) == [Block(sample_tasks[0], 1.5)]


def test_excess_budget_is_not_forced_into_create_sample_tasks():
    sample_tasks = create_sample_tasks()
    blocks = allocate(sample_tasks, 20)
    assert blocks == [Block(sample_tasks[0], 1.5), Block(sample_tasks[1], 6)]
    total_hours = 0
    for block in blocks:
        total_hours = total_hours + block.hours
    assert total_hours == 7.5


def test_empty_and_zero_budget():
    assert allocate([], 2) == []
    assert allocate(create_sample_tasks(), 0) == []


def test_zero_effort_is_skipped():
    zero = Task("Done", 3, 0, date(2026, 10, 30))
    sample_tasks = create_sample_tasks()
    assert allocate([zero, *sample_tasks], 1) == [Block(sample_tasks[0], 1)]


@pytest.mark.parametrize("budget", [-1, float("nan"), float("inf")])
def test_invalid_budget(budget):
    with pytest.raises(ValueError, match="hours"):
        allocate(create_sample_tasks(), budget)


@pytest.mark.parametrize("budget", [0.1, 1.5, 2, 7.5, 8])
def test_never_exceeds_budget_or_effort(budget):
    blocks = allocate(create_sample_tasks(), budget)
    total_hours = 0
    for block in blocks:
        total_hours = total_hours + block.hours
        assert block.hours > 0
        assert block.hours <= block.task.effort_h
    assert total_hours <= budget + 1e-12
