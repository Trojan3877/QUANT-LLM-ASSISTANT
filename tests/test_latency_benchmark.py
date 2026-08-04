import json

import pytest

from benchmarks.latency_benchmark import build_evidence, write_evidence


def test_benchmark_evidence_is_versioned_and_commit_bound(tmp_path):
    evidence = build_evidence(
        [0.01, 0.02, 0.03],
        rows=1_000,
        iterations=10,
        max_seconds=0.25,
        commit="abc123",
    )

    assert evidence["schema_version"] == 1
    assert evidence["commit"] == "abc123"
    assert evidence["workload"]["sample_count"] == 3
    assert evidence["summary_seconds_per_backtest"]["median"] == pytest.approx(0.02)
    assert evidence["summary_seconds_per_backtest"]["p95_nearest_rank"] == pytest.approx(0.03)

    output = tmp_path / "latency.json"
    write_evidence(output, evidence)
    assert json.loads(output.read_text(encoding="utf-8")) == evidence


def test_benchmark_evidence_rejects_empty_samples():
    with pytest.raises(ValueError, match="timing sample"):
        build_evidence([], rows=1_000, iterations=10, max_seconds=0.25, commit="abc123")
