from collections import Counter
from math import ceil


def analyse(pairs: list[tuple[str, float]]) -> dict:
    """Count requests and calculate the nearest-rank p95 per route."""
    counts: Counter[str] = Counter()
    latencies: dict[str, list[float]] = {}

    for route, latency_ms in pairs:
        counts[route] += 1
        if route not in latencies:
            latencies[route] = []
        latencies[route].append(latency_ms)

    p95: dict[str, float] = {}
    slowest = None
    highest_p95 = None

    for route, values in latencies.items():
        sorted_values = sorted(values)
        rank = ceil(0.95 * len(sorted_values))
        route_p95 = sorted_values[rank - 1]
        p95[route] = route_p95

        if highest_p95 is None or route_p95 > highest_p95:
            highest_p95 = route_p95
            slowest = route

    return {"counts": dict(counts), "p95": p95, "slowest": slowest}
