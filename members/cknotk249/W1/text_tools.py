def word_count(text: str) -> dict[str, int]:
    
    for p in ".,!?;:":
        text = text.replace(p, "")
        
    
    words = text.lower().split()
    
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
    return counts

def top_k(text: str, k: int) -> list[tuple[str, int]]:
    counts = word_count(text)
    
    sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    return sorted_items[:k]
