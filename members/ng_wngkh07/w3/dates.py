import re
from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    """Convert a supported deadline description into a date."""
    if text == "tomorrow":
        return today + timedelta(days=1)

    relative_date = re.fullmatch(r"in (\d+) days", text)
    if relative_date:
        number_of_days = int(relative_date.group(1))
        return today + timedelta(days=number_of_days)

    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    if text in weekdays:
        target_weekday = weekdays.index(text)
        days_ahead = (target_weekday - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        return today + timedelta(days=days_ahead)

    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):
        return date.fromisoformat(text)

    raise ValueError(f"Unknown deadline: {text}")
