def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("LIST MUST NOT EMPTY!")
    
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    
    min_score = sorted_scores[0]
    max_score = sorted_scores[-1]
    mean_score = sum(sorted_scores) / n
    
    if n % 2 == 0:
        median_score = (sorted_scores[n//2 - 1] + sorted_scores[n//2]) / 2.0
    else:
        median_score = sorted_scores[n//2]
        
    return {
        "min": min_score,
        "max": max_score,
        "mean": round(mean_score, 2),
        "median": round(median_score, 2)
    }
