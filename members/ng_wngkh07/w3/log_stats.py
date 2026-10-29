"""Utilities for calculating request latency statistics from chat logs."""

from collections import Counter
from math import ceil
from typing import TypedDict


class AnalysisResult(TypedDict):
    """Summary statistics returned by :func:`analyse`."""

    counts: dict[str, int]
    p95: dict[str, float]
    slowest: str | None


def analyse(pairs: list[tuple[str, float]]) -> AnalysisResult:
    """Count requests and calculate each route's nearest-rank p95 latency.

    The slowest route is the one with the highest p95 latency, or ``None`` if
    ``pairs`` is empty.
    """
    counts: Counter[str] = Counter()
    latencies: dict[str, list[float]] = {}

    for route, latency_ms in pairs:
        counts[route] += 1
        latencies.setdefault(route, []).append(latency_ms)

    p95: dict[str, float] = {}
    for route, values in latencies.items():
        sorted_values = sorted(values)
        rank = ceil(0.95 * len(sorted_values))
        p95[route] = sorted_values[rank - 1]

    slowest = max(p95, key=p95.__getitem__, default=None)
    return {"counts": dict(counts), "p95": p95, "slowest": slowest}
