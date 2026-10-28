def by_day(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Group and sort courses by weekday."""
    thoi_khoa_bieu = {}
    for cap in pairs:
        mon_hoc = cap[0]
        ngay = cap[1]
        danh_sach_mon = thoi_khoa_bieu.setdefault(ngay, [])
        danh_sach_mon.append(mon_hoc)
    for danh_sach_mon in thoi_khoa_bieu.values():
        danh_sach_mon.sort()
    return thoi_khoa_bieu