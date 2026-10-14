def summary(scores: list[float]) -> dict:
    if not scores:
        raise ValueError("scores list cannot be empty")

    s = sorted(scores)
    n = len(s)

    if n % 2 == 1:
        median = s[n // 2]
    else:
        median = (s[n // 2 - 1] + s[n // 2]) / 2

    return {
        "min": min(scores),
        "max": max(scores),
        "mean": round(sum(scores) / n, 2),
        "median": round(median, 2),
    }


if __name__ == "__main__":
    print(summary([7.5, 9, 6, 8]))
