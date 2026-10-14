def word_count(text: str) -> dict[str, int]:
    punctuation = ".,!?;:"
    cleaned_text = text.lower()
    for char in punctuation:
        cleaned_text = cleaned_text.replace(char, " ")
    words = cleaned_text.split()
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts
def top_k(text: str, k: int) -> list[tuple[str, int]]:
    if k <= 0:
        return []
    counts = word_count(text)
    danh_sach_cap = list(counts.items())
    def tieu_chi_sap_xep(cap):
        tu = cap[0]
        so_lan = cap[1]
        return (-so_lan, tu)
    danh_sach_da_sap_xep = sorted(danh_sach_cap, key=tieu_chi_sap_xep)
    return danh_sach_da_sap_xep[:k]