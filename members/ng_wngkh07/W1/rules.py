def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check whether credits and GPA meet thesis requirements."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """List the requirements that are not yet satisfied."""
    danh_sach_ly_do = []
    if credits < 120:
        danh_sach_ly_do.append("Chưa đủ 120 tín chỉ")
    if gpa < 2.0:
        danh_sach_ly_do.append("Điểm GPA chưa đạt 2.0")
    return danh_sach_ly_do