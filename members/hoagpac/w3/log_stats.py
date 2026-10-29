from collections import Counter
import math


def analyse(pairs: list[tuple[str, float]]) -> dict:
    counts: Counter[str] = Counter()
    latencies: dict[str, list[float]] = {}

    for route, latency in pairs:
        counts[route] += 1
        latencies.setdefault(route, []).append(latency)

    p95: dict[str, float] = {}
    for route, lats in latencies.items():
        s = sorted(lats)
        idx = max(0, math.ceil(0.95 * len(s)) - 1)
        p95[route] = s[idx]

    slowest = max(p95, key=p95.get) if p95 else None
    return {"counts": dict(counts), "p95": p95, "slowest": slowest}
