import string


def word_count(text: str) -> dict[str, int]:
    """Count words case-insensitively, ignoring the specified punctuation."""
    for char in ".,!?;:":
        text = text.replace(char, "")

    words = text.lower().split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def top_k(text: str, k: int) -> list[tuple[str, int]]:
    """Return the k most frequent words, alphabetically breaking ties."""
    counts = word_count(text)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:k]