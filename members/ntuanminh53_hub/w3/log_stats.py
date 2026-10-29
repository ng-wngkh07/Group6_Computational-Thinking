"""Utilities for calculating chat log request latency statistics."""

import math
from collections import Counter


def analyse(pairs: list[tuple[str, float]]) -> dict:
    """Analyse a list of (route, latency_ms) pairs.

    Returns a dict with:
    - 'counts': dict of request count per route
    - 'p95': dict of 95th percentile latency per route
    - 'slowest': the route with highest p95 latency (or None if empty)
    """
    counts: Counter[str] = Counter()
    latencies: dict[str, list[float]] = {}

    for route, latency in pairs:
        counts[route] += 1
        latencies.setdefault(route, []).append(latency)

    p95: dict[str, float] = {}
    for route, lats in latencies.items():
        sorted_lats = sorted(lats)
        idx = max(0, math.ceil(0.95 * len(sorted_lats)) - 1)
        p95[route] = sorted_lats[idx]

    slowest = max(p95, key=p95.get) if p95 else None
    return {"counts": dict(counts), "p95": p95, "slowest": slowest}
