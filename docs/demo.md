# Study Planner Demo

This document demonstrates the execution and behavior of the integrated Study Planner tool (`shared.study_planner`).

**Author:** Vo Nguyen Hoang Bach ([@hoagpac](https://github.com/hoagpac))

## Sample Input

Using `samples/tasks.csv`:

```csv
title,importance,effort_h,deadline
DS exam,5,6,2026-10-30
Assignment,4,1.5,2026-10-27
```

- **DS exam**: Importance 5, 6.0 hours required.
- **Assignment**: Importance 4, 1.5 hours required.

---

## Demo Scenarios

### Scenario 1: Partial Study Session (2 hours available)

When available time is limited, the planner prioritizes the most urgent task and allocates time up to the budget.

**Command:**

```bash
$ python -m shared.study_planner samples/tasks.csv --hours 2
```

**Output:**

```text
Study plan
1. DS exam: 2 hours
Total: 2 hours
```

*Explanation:* DS exam is scheduled first and receives the full 2.0 hours budget (a partial allocation toward its 6.0 hours total effort).

---

### Scenario 2: Extended Study Session (8 hours available)

When sufficient hours are available, multiple tasks are scheduled in priority order.

**Command:**

```bash
$ python -m shared.study_planner samples/tasks.csv --hours 8
```

**Output:**

```text
Study plan
1. DS exam: 6 hours
2. Assignment: 1.5 hours
Total: 7.5 hours
```

*Explanation:* Both tasks are fully satisfied with 7.5 hours total, leaving the remaining 0.5 hours unallocated.
