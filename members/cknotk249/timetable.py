def by_day(timetable: list[tuple[str, str]]) -> dict[str, list[str]]:
    schedule = {}
    
    for course, day in timetable:
        schedule.setdefault(day, []).append(course)
        

    return {day: sorted(courses) for day, courses in schedule.items()}

