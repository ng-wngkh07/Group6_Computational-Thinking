# Study Planner

A command-line study planner integrated for CSC10014. The tool reads a list of tasks from a CSV file, calculates priorities, greedily allocates available study hours, and renders a structured study plan.

**Author:** Vo Nguyen Hoang Bach ([@hoagpac](https://github.com/hoagpac))

## Architecture

The application is structured into four sequential pipeline stages:

1. **Parse (`parse.py`)**: `parse_csv(path) -> list[Task]`  
   Parses the CSV file into a list of validated `Task` objects defined in `shared.contract`.
2. **Prioritise (`prioritise.py`)**: `prioritise(tasks, today) -> list[Task]`  
   Ranks tasks in descending order of urgency using the priority ratio:
   $$\text{Priority} = \frac{\text{importance}}{\max(1, \text{days\_left})}$$
3. **Allocate (`allocate.py`)**: `allocate(tasks, hours) -> list[Block]`  
   Greedily distributes available study hours to the highest-priority tasks, splitting tasks into partial blocks if necessary.
4. **Render (`render.py`)**: `render(blocks) -> str`  
   Formats the scheduled study blocks into a clean, human-readable plan.

The pipeline is integrated in `__main__.py` to provide the CLI entrypoint.

## Usage

Run the package directly with Python from the repository root:

```bash
python -m shared.study_planner <path_to_csv> --hours <hours>
```

### Options

- `csv_file`: Path to the CSV file containing tasks (required positional argument).
- `--hours`: Total available study hours as a positive number (required).

### Examples

Generate a 2-hour study plan:

```bash
python -m shared.study_planner samples/tasks.csv --hours 2
```

Output:
```text
Study plan
1. DS exam: 2 hours
Total: 2 hours
```

Generate an 8-hour study plan:

```bash
python -m shared.study_planner samples/tasks.csv --hours 8
```

Output:
```text
Study plan
1. DS exam: 6 hours
2. Assignment: 1.5 hours
Total: 7.5 hours
```

## Input Format

Task CSV files must include the following header and column format:

```csv
title,importance,effort_h,deadline
DS exam,5,6,2026-10-30
Assignment,4,1.5,2026-10-27
```

- `title`: Name of the task (string).
- `importance`: Integer rating from 1 to 5.
- `effort_h`: Estimated hours required (finite, non-negative float).
- `deadline`: Target completion date in ISO format (`YYYY-MM-DD`).

## Running Tests

Run the team test suite using pytest:

```bash
pytest tests/team/
```
