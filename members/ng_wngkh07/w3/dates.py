"""Utilities for parsing due-date expressions."""

import re
from datetime import date, timedelta

WEEKDAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")


def parse_due(text: str, today: date) -> date:
    """Parse an ISO date, relative day expression, or weekday abbreviation.

    A weekday matching ``today`` means its next occurrence, seven days later.
    Unsupported expressions raise ``ValueError``.
    """
    if text == "tomorrow":
        return today + timedelta(days=1)

    relative_date = re.fullmatch(r"in (\d+) days", text)
    if relative_date is not None:
        return today + timedelta(days=int(relative_date.group(1)))

    if text in WEEKDAYS:
        target_weekday = WEEKDAYS.index(text)
        days_ahead = (target_weekday - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
        return date.fromisoformat(text)

    raise ValueError(f"Unknown deadline: {text}")
