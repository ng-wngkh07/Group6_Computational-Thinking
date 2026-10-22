def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return whether a student meets the thesis registration requirements."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return the reasons a student is not eligible to register for a thesis."""
    reasons = []

    if credits < 120:
        reasons.append("Need at least 120 credits")

    if gpa < 2.0:
        reasons.append("GPA must be at least 2.0")

    return reasons