def by_day(courses: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group course names by day and sort each day's courses alphabetically."""
    result = {}

    for course, day in courses:
        result.setdefault(day, []).append(course)

    return {day: sorted(names) for day, names in result.items()}