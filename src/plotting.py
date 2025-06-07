import matplotlib.pyplot as plt
from typing import List, Any

def plot_time_series(
    dates: List[Any],
    values: List[float],
    title: str = "",
    xlabel: str = "Date",
    ylabel: str = "Value",
    save_path: str = None
):
    """
    Plot a time-series line chart.
    :param dates: Sequence of date-like objects
    :param values: Sequence of numeric values
    :param title: Chart title
    :param xlabel: Label for x-axis
    :param ylabel: Label for y-axis
    :param save_path: If provided, path to save the figure
    """
    plt.figure()
    plt.plot(dates, values, marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_histogram(
    values: List[float],
    bins: int = 20,
    title: str = "",
    xlabel: str = "Value",
    ylabel: str = "Frequency",
    save_path: str = None
):
    """
    Plot a histogram.
    :param values: Sequence of numeric values
    :param bins: Number of histogram bins
    :param title: Chart title
    :param xlabel: Labe

git add src/plotting.py
git commit -m "Add plotting utilities for time-series and histogram charts"
