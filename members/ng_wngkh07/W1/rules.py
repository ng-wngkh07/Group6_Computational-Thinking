def can_register_thesis(credits: int, gpa: float) -> bool:
    if credits >= 120 and gpa >= 2.0:
        return True
    else:
        return False


def missing(credits: int, gpa: float) -> list[str]:
    danh_sach_ly_do = []
    if credits < 120:
        danh_sach_ly_do.append("Chưa đủ 120 tín chỉ")
    if gpa < 2.0:
        danh_sach_ly_do.append("Điểm GPA chưa đạt 2.0")
    return danh_sach_ly_do