import pandas as pd
from typing import Callable, Dict, Any

class BacktestEngine:
    """
    Simple backtesting engine for evaluating trading strategies.
    """

    def __init__(
        self,
        price_data: pd.DataFrame,
        strategy_fn: Callable[[pd.DataFrame], pd.Series],
        initial_cash: float = 100000.0
    ):
        """
        :param price_data: DataFrame with a DateTime index and at least a 'close' column.
        :param strategy_fn: Function that takes price_data and returns a Series of positions (-1, 0, 1).
        :param initial_cash: Starting cash balance.
        """
        self.price_data = price_data
        self.strategy_fn = strategy_fn
        self.initial_cash = initial_cash
        self.trades = None
        self.equity_curve = None

    def run(self) -> pd.DataFrame:
        """
        Execute the backtest and generate an equity curve.
        :return: DataFrame with 'cash', 'position', 'holdings', and 'total' equity over time.
        """
        signals = self.strategy_fn(self.price_data)
        cash = self.initial_cash
        position = 0
        equity = []

        for timestamp, row in self.price_data.iterrows():
            price = row["close"]
            target_pos = signals.loc[timestamp]
            # Determine trade size (all-in/all-out for now)
            if target_pos != position:
                # Sell existing
                cash += position * price
                # Buy new
                cash -= target_pos * price
                position = target_pos

            holdings = position * price
            total = cash + holdings
            equity.append({
                "timestamp": timestamp,
                "cash": cash,
                "position": position,
                "holdings": holdings,
                "total": total
            })

        self.equity_curve = pd.DataFrame(equity).set_index("timestamp")
        return self.equity_curve

    def stats(self) -> Dict[str, Any]:
        """
        Compute basic backtest statistics: total return, CAGR, max drawdown, etc.
        :return: Dict of performance metrics.
        """
        df = self.equity_curve["total"]
        total_return = df.iloc[-1] / df.iloc[0] - 1
        # (Additional metrics can be implemented here.)
        return {
            "total_return": total_return,
            # "cagr": ...,
            # "max_drawdown": ...,
        }

git add src/backtest.py
git commit -m "Add backtesting engine scaffold in src/backtest.py"
