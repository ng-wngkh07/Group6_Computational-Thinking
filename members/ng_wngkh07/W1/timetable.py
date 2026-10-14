def by_day(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    thoi_khoa_bieu = {}
    for cap in pairs:
        mon_hoc = cap[0]
        ngay = cap[1]
        danh_sach_mon = thoi_khoa_bieu.setdefault(ngay, [])
        danh_sach_mon.append(mon_hoc)
    for ngay in thoi_khoa_bieu:
        thoi_khoa_bieu[ngay].sort()
    return thoi_khoa_bieu