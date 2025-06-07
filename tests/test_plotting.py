import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing
import os
from src.plotting import plot_time_series, plot_histogram

def test_plot_time_series(tmp_path):
    dates = ["2025-06-01", "2025-06-02", "2025-06-03"]
    values = [1.0, 2.0, 3.0]
    out_file = tmp_path / "ts_plot.png"

    # Should run without error and save the file
    plot_time_series(dates, values, title="Test TS", save_path=str(out_file))
    assert out_file.exists()

def test_plot_histogram(tmp_path):
    values = [1, 2, 2, 3, 3, 3]
    out_file = tmp_path / "hist_plot.png"

    # Should run without error and save the file
    plot_histogram(values, bins=3, title="Test Histogram", save_path=str(out_file))
    assert out_file.exists()

git add tests/test_plotting.py
git commit -m "Add pytest suite for plotting utilities"
