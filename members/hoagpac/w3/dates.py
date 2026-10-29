import re
from datetime import date, timedelta


def parse_due(text: str, today: date) -> date:
    if text == "tomorrow":
        return today + timedelta(days=1)

    m = re.match(r"^in\s+(\d+)\s+days?$", text)
    if m:
        return today + timedelta(days=int(m.group(1)))

    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    if text in weekdays:
        diff = (weekdays.index(text) - today.weekday()) % 7
        return today + timedelta(days=7 if diff == 0 else diff)

    try:
        return date.fromisoformat(text)
    except ValueError:
        raise ValueError(f"Unknown deadline: {text}")
