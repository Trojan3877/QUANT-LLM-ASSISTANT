"""Deterministic backtest benchmark with commit-bound CI evidence."""

from __future__ import annotations

import argparse
import json
import math
import os
import platform
import statistics
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import pandas as pd

from src.backtest import BacktestEngine


def _positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("value must be positive")
    return parsed


def run(iterations: int = 100, rows: int = 1_000, repeats: int = 5) -> list[float]:
    """Return mean seconds per backtest for each deterministic timing sample."""
    if iterations <= 0 or rows <= 0 or repeats <= 0:
        raise ValueError("iterations, rows, and repeats must be positive")
    frame = pd.DataFrame(
        {"close": [100.0 + (index % 20) for index in range(rows)]},
        index=pd.date_range("2020-01-01", periods=rows, freq="min"),
    )
    def always_long(data: pd.DataFrame) -> pd.Series:
        return pd.Series(1, index=data.index)

    samples: list[float] = []
    for _ in range(repeats):
        started = time.perf_counter()
        for _ in range(iterations):
            BacktestEngine(frame, always_long).run()
        samples.append((time.perf_counter() - started) / iterations)
    return samples


def _nearest_rank(values: list[float], quantile: float) -> float:
    if not values:
        raise ValueError("at least one timing sample is required")
    index = max(0, math.ceil(len(values) * quantile) - 1)
    return sorted(values)[index]


def resolve_commit() -> str | None:
    """Resolve the evidence commit without failing local benchmark execution."""
    if github_sha := os.environ.get("GITHUB_SHA"):
        return github_sha
    try:
        result = subprocess.run(  # noqa: S603 -- command and arguments are static
            ["git", "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip() or None


def build_evidence(
    samples: list[float],
    *,
    rows: int,
    iterations: int,
    max_seconds: float,
    commit: str | None = None,
) -> dict[str, Any]:
    """Build a versioned, reviewable record for a single benchmark invocation."""
    if not samples:
        raise ValueError("at least one timing sample is required")
    return {
        "schema_version": 1,
        "commit": commit if commit is not None else resolve_commit(),
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "workload": {
            "rows": rows,
            "iterations_per_sample": iterations,
            "sample_count": len(samples),
            "strategy": "always_long",
        },
        "summary_seconds_per_backtest": {
            "mean": statistics.fmean(samples),
            "median": statistics.median(samples),
            "p95_nearest_rank": _nearest_rank(samples, 0.95),
            "max": max(samples),
        },
        "threshold_seconds_per_backtest": max_seconds,
        "samples_seconds_per_backtest": samples,
        "runner": {
            "python": sys.version.split()[0],
            "platform": platform.platform(),
        },
    }


def write_evidence(path: Path, evidence: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Measure deterministic BacktestEngine latency and optionally retain JSON evidence."
    )
    parser.add_argument("--max-seconds", type=float, default=0.25)
    parser.add_argument("--iterations", type=_positive_int, default=100)
    parser.add_argument("--rows", type=_positive_int, default=1_000)
    parser.add_argument("--repeats", type=_positive_int, default=5)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.max_seconds <= 0:
        raise SystemExit("--max-seconds must be positive")
    samples = run(args.iterations, args.rows, args.repeats)
    evidence = build_evidence(
        samples,
        rows=args.rows,
        iterations=args.iterations,
        max_seconds=args.max_seconds,
    )
    if args.output:
        write_evidence(args.output, evidence)

    mean = evidence["summary_seconds_per_backtest"]["mean"]
    print(f"mean_backtest_latency_seconds={mean:.6f}")
    if args.output:
        print(f"benchmark_evidence={args.output}")
    if mean > args.max_seconds:
        raise SystemExit(f"latency regression: {mean:.6f}s > {args.max_seconds:.6f}s")


if __name__ == "__main__":
    main()
