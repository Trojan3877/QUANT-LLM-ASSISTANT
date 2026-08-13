# Mathematical Foundations

## Scope

This document specifies the deterministic backtest implemented in `src/backtest.py`. It does **not** define a forecasting model, an optimization objective, a portfolio allocator, or a claim of investment performance.

## Notation and input invariants

Let the input be a strictly ordered sequence of $T$ timestamps with positive, finite closing prices $C_t > 0$. The supplied strategy emits one position target per timestamp,

$ s_t \in \{-1,0,1\}, $

where $-1$, $0$, and $1$ mean one-unit short, flat, and one-unit long. The implementation requires that signal and price indexes match exactly. Let $K_0>0$ be initial cash and $s_0=0$ be the initial position.

These constraints map to constructor and `run()` validation in `src/backtest.py`.

## State transition

At timestamp $t$, the engine first changes the old position $s_{t-1}$ to the target $s_t$ at the current close $C_t$. Cash and marked-to-market holdings are

\[
K_t = K_{t-1} + s_{t-1}C_t - s_tC_t,
\]

\[
H_t=s_tC_t, \qquad E_t=K_t+H_t.
\]

Here $E_t$ is the equity recorded in the returned equity curve. A switch from long to flat therefore sells one unit at $C_t$; a switch from flat to long buys one unit at $C_t$; and a switch from long to short realizes the long and opens the short at the same price.

The code implements this transition as a cash adjustment only when the target differs from the current position, followed by `holdings = position * price` and `total = cash + holdings`.

## Reported statistics

After `run()`, the implementation reports total return

\[
R = \frac{E_T}{K_0}-1,
\]

and maximum drawdown

\[
\operatorname{MDD}=\min_{1\leq t\leq T}\left(\frac{E_t}{\max_{1\leq u\leq t}E_u}-1\right).
\]

The calculation uses the pandas cumulative maximum of the equity series and then takes the minimum drawdown. The analytical long-only case in `tests/test_core.py` checks both values.

## Interpretation and exclusions

The model trades at the supplied close with no fees, bid/ask spread, slippage, borrowing constraints, liquidity limits, margin rules, taxes, corporate actions, or execution delay. Consequently, $R$ and MDD are accounting outputs of the specified toy market model—not realized or forecast financial performance.

The LLM boundary is not part of these equations. It generates constrained research text after input validation; it does not produce a formally evaluated trading signal in this repository.
