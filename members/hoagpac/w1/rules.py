def can_register(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0


def can_register_thesis(credits: int, gpa: float) -> bool:
    return can_register(credits, gpa)


def missing(credits: int, gpa: float) -> list[str]:
    reasons = []
    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        reasons.append("GPA must be at least 2.0")
    return reasons


if __name__ == "__main__":
    print(can_register(120, 2.0))
    print(can_register(119, 3.5))
    print(can_register(120, 1.9))
    print(can_register(130, 3.2))
    print(missing(118, 2.5))
