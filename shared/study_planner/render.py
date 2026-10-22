from shared.contract import Block


def render(blocks: list[Block]) -> str:
    if len(blocks) == 0:
        return "No study blocks."

    lines = ["Study plan"]
    total_hours = 0
    block_number = 1

    for block in blocks:
        task_title = block.task.title
        allocated_hours = block.hours
        line = f"{block_number}. {task_title}: {allocated_hours:g} hours"
        lines.append(line)

        total_hours = total_hours + allocated_hours
        block_number = block_number + 1

    total_line = f"Total: {total_hours:g} hours"
    lines.append(total_line)
    plan_text = "\n".join(lines)
    return plan_text
