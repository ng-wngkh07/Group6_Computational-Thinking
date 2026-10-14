def can_register_thesis(credits: int, gpa: float) -> bool:
    """True if credits >= 120 and gpa >= 2.0."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return human-readable reasons if ineligible for thesis registration."""
    reasons: list[str] = []
    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        reasons.append("GPA must be at least 2.0")
    return reasons


if __name__ == "__main__":
    print(can_register_thesis(120, 2.0))
    print(missing(118, 3.1))
    print(missing(100, 1.5))
