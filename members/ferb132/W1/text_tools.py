def word_count(text: str) -> dict[str, int]:
    text = text.lower()
    clean_text = text.translate(str.maketrans("", "", ".,!?;:"))
    count = {}
    words = clean_text.split()
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count 
def top_k(text: str, k: int):
    counts = word_count(text)
    sorted_words = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    return sorted_words[:k]
def main():
    kq = top_k("Git is fun. Git is fast!", 2)
    print(kq)

if __name__ == "__main__":
    main()
