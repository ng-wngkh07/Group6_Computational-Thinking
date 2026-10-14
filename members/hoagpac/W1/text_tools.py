def word_count(text: str) -> dict[str, int]:
    for p in ".,!?;:":
        text = text.replace(p, " ")

    words = text.lower().split()
    counts: dict[str, int] = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    if k <= 0:
        return []

    counts = word_count(text)
    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:k]


if __name__ == "__main__":
    print(top_k("Git is fun. Git is fast!", 2))
