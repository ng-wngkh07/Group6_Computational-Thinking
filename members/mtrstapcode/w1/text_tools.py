def word_count(text: str) -> dict[str, int]:
    """Count words in text (lower-case, ignoring punctuation .,!?;:)."""
    for ch in ".,!?;:":
        text = text.replace(ch, " ")
    counts: dict[str, int] = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return top k words sorted by count (descending), then alphabetically."""
    counts = word_count(text)
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:k]


if __name__ == "__main__":
    print(word_count("Git is fun. Git is fast!"))
    print(top_k("Git is fun. Git is fast!", 2))
