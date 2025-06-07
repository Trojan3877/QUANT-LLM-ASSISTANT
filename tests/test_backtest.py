import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from src.backtest import BacktestEngine

def make_price_df(days=5, start_price=100.0):
    dates = [datetime(2025, 6, 1) + timedelta(days=i) for i in range(days)]
    # Simulate a simple upward price series
    prices = [start_price + i for i in range(days)]
    df = pd.DataFrame({
        "close": prices
    }, index=dates)
    return df

def test_backtest_all_in_strategy():
    # Strategy: always long (position = 1)
    def always_long(df):
        return pd.Series(1, index=df.index)

    price_df = make_price_df()
    engine = BacktestEngine(price_data=price_df, strategy_fn=always_long, initial_cash=1000.0)
    equity = engine.run()

    # After buying on first day, cash should be 1000 - price and holdings = price
    first_price = price_df["close"].iloc[0]
    assert np.isclose(equity["cash"].iloc[0], 1000.0 - first_price)
    assert np.isclose(equity["position"].iloc[0], 1)
    assert np.isclose(equity["holdings"].iloc[0], first_price)
    # Total equals initial_cash + gains from price increase
    last_price = price_df["close"].iloc[-1]
    total_return = last_price / first_price - 1
    stats = engine.stats()
    assert "total_return" in stats
    assert pytest.approx(total_return, rel=1e-6) == stats["total_return"]

def test_backtest_flat_strategy():
    # Strategy: flat (position = 0)
    def flat(df):
        return pd.Series(0, index=df.index)

    price_df = make_price_df()
    engine = BacktestEngine(price_data=price_df, strategy_fn=flat, initial_cash=500.0)
    equity = engine.run()

    # No trades: cash remains unchanged, holdings = 0
    assert all(equity["cash"] == 500.0)
    assert all(equity["position"] == 0)
    assert all(equity["holdings"] == 0)
    stats = engine.stats()
    assert pytest.approx(0.0, abs=1e-9) == stats["total_return"]

git add tests/test_backtest.py
git commit -m "Add pytest suite for BacktestEngine"
