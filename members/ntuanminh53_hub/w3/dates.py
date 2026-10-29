"""Utilities for parsing due date representations."""

import re
from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Parse relative or fixed due date strings into a date object.

    Accepted formats:
    - 'YYYY-MM-DD' (ISO format)
    - 'tomorrow'
    - 'in N days' / 'in N day'
    - Weekday abbreviations: 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun' (next occurrence)
    """
    if text == "tomorrow":
        return today + timedelta(days=1)

    match = re.match(r"^in\s+(\d+)\s+days?$", text)
    if match:
        days = int(match.group(1))
        return today + timedelta(days=days)

    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    if text in weekdays:
        target_idx = weekdays.index(text)
        diff = (target_idx - today.weekday()) % 7
        return today + timedelta(days=7 if diff == 0 else diff)

    try:
        return date.fromisoformat(text)
    except ValueError as err:
        raise ValueError(f"Unknown deadline: {text}") from err
