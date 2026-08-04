"""Small, deterministic backtesting engine for research—not trade execution."""

from __future__ import annotations

import math
from collections.abc import Callable
from typing import Any

import pandas as pd


class BacktestEngine:
    def __init__(
        self,
        price_data: pd.DataFrame,
        strategy_fn: Callable[[pd.DataFrame], pd.Series],
        initial_cash: float = 100_000.0,
    ) -> None:
        if price_data.empty or "close" not in price_data:
            raise ValueError("price_data must contain at least one row and a 'close' column")
        if not price_data.index.is_unique or not price_data.index.is_monotonic_increasing:
            raise ValueError("price_data index must be unique and ordered")
        closes = pd.to_numeric(price_data["close"], errors="coerce")
        if closes.isna().any() or not closes.map(math.isfinite).all() or (closes <= 0).any():
            raise ValueError("close prices must be finite positive numbers")
        if initial_cash <= 0:
            raise ValueError("initial_cash must be positive")
        self.price_data = price_data.copy()
        self.price_data["close"] = closes
        self.strategy_fn = strategy_fn
        self.initial_cash = float(initial_cash)
        self.equity_curve: pd.DataFrame | None = None

    def run(self) -> pd.DataFrame:
        signals = self.strategy_fn(self.price_data)
        if not signals.index.equals(self.price_data.index):
            raise ValueError("strategy signals must exactly align with price_data")
        if signals.isna().any() or not signals.isin((-1, 0, 1)).all():
            raise ValueError("strategy positions must be -1, 0, or 1")

        cash, position, equity = self.initial_cash, 0, []
        for timestamp, price in self.price_data["close"].items():
            target = int(signals.loc[timestamp])
            if target != position:
                cash += position * price
                cash -= target * price
                position = target
            holdings = position * price
            equity.append(
                {
                    "timestamp": timestamp,
                    "cash": cash,
                    "position": position,
                    "holdings": holdings,
                    "total": cash + holdings,
                }
            )
        self.equity_curve = pd.DataFrame(equity).set_index("timestamp")
        return self.equity_curve.copy()

    def stats(self) -> dict[str, Any]:
        if self.equity_curve is None:
            raise RuntimeError("run() must be called before stats()")
        totals = self.equity_curve["total"]
        running_peak = totals.cummax()
        drawdown = totals / running_peak - 1
        return {
            "total_return": float(totals.iloc[-1] / self.initial_cash - 1),
            "max_drawdown": float(drawdown.min()),
        }
