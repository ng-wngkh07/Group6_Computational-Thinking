def by_day(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Given a list of (course, day) tuples, return a dict mapping day to a sorted list of courses."""
    result: dict[str, list[str]] = {}
    for course, day in pairs:
        result.setdefault(day, []).append(course)

    for day in result:
        result[day].sort()

    return result


if __name__ == "__main__":
    print(by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]))
