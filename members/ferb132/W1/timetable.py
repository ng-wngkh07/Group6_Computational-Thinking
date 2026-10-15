def by_day(course_schedule: list[tuple[str, str]]) -> dict[str, list[str]]: 
    result = {}
    for course, day in course_schedule:
        result.setdefault(day, []).append(course)
    for day in result:
        result[day].sort()
    return result
def main():
    print(by_day([("CSC10014", "Mon"), ("MTH00003", "Tue"), ("CSC10001", "Mon")]))
if __name__ == "__main__":
    main()