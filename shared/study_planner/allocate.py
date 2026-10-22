from math import isfinite

from shared.contract import Block, Task


def allocate(tasks: list[Task], hours: float) -> list[Block]:
    if not isfinite(hours):
        raise ValueError("hours must be finite and non-negative")
    if hours < 0:
        raise ValueError("hours must be finite and non-negative")

    blocks = []
    remaining_hours = hours

    for task in tasks:
        if remaining_hours <= 0:
            break

        if task.effort_h == 0:
            continue

        if task.effort_h > remaining_hours:
            block = Block(task=task, hours=remaining_hours)
        else:
            block = Block(task=task, hours=task.effort_h)

        blocks.append(block)
        remaining_hours = remaining_hours - block.hours

    return blocks
