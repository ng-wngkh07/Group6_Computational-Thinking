def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    grouped = {}
    for course, day in timetable:
        grouped.setdefault(day, []).append(course)

    return {day: sorted(grouped[day]) for day in sorted(grouped)}


group_timetable = by_day


if __name__ == "__main__":
    my_day = [
        ("CSC10014", "Mon"),
        ("MTH00003", "Tue"),
        ("CSC10001", "Mon"),
    ]
    print(by_day(my_day))
