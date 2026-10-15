def summary(scores: list[float]) -> dict:
    """Return the minimum, maximum, mean, and median of the scores."""
    if not scores:
        raise ValueError("scores must not be empty")

    ordered = sorted(scores)
    n = len(ordered)

    mean = round(sum(ordered) / n, 2)

    if n % 2 == 1:
        median = ordered[n // 2]
    else:
        median = (ordered[n // 2 - 1] + ordered[n // 2]) / 2

    return {
        "min": min(ordered),
        "max": max(ordered),
        "mean": mean,
        "median": round(median, 2),
    } 