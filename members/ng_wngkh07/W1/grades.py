def summary(scores: list[float]) -> dict[str, float]:
    """Calculate score statistics, using zeros for an empty list."""
    if not scores:
        return {
            "min": 0,
            "max": 0,
            "mean": 0,
            "median": 0
        }
    minimum = min(scores)
    maximum = max(scores)
    mean=sum(scores)/len(scores)
    scores.sort()
    n = len(scores)
    if n % 2 == 0:
        median = (scores[n // 2 - 1] + scores[n // 2]) / 2
    else:
        median = scores[n // 2]
    return {
        "average": mean,
        "min": minimum,
        "max": maximum,
        "median": median
    }