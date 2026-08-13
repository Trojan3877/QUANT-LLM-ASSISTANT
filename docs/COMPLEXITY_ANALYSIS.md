# Complexity Analysis

## Variables

- $T$: number of price timestamps supplied to one backtest
- $R$: number of benchmark repeats
- $I$: backtests per repeat in the latency harness
- $B$: number of raw timing samples; in the current harness $B=R$

These are asymptotic properties of the repository's own loops and pandas-series operations, not empirical latency claims.

## Backtest engine

| Operation | Best | Average | Worst | Auxiliary space |
|---|---:|---:|---:|---:|
| Price and index validation | $O(T)$ | $O(T)$ | $O(T)$ | $O(T)$ under pandas coercion/copies |
| Signal validation | $O(T)$ | $O(T)$ | $O(T)$ | $O(T)$ for the signal series |
| Equity simulation in `run()` | $O(T)$ | $O(T)$ | $O(T)$ | $O(T)$ for recorded equity rows |
| Return and drawdown in `stats()` | $O(T)$ | $O(T)$ | $O(T)$ | $O(T)$ for cumulative pandas series |
| Deterministic latency harness | $O(RIT)$ | $O(RIT)$ | $O(RIT)$ | $O(T+B)$ excluding library internals |

The simulation loop has constant work per price observation: signal lookup, at most two cash terms, a holdings product, and one output record. Creating the returned dataframe and cumulative drawdown series are linear in the number of timestamps.

## Dominant costs and scaling implications

The benchmark's fixed strategy is inexpensive; for it, the loop and pandas dataframe construction dominate. A strategy function that scans the full price history at every timestamp could make the effective run cost superlinear, so the $O(T)$ result applies only to the engine plus a strategy with $O(1)$ amortized work per timestamp or precomputed signals.

The current benchmark uses $T=1,000$, $I=100$, and $R=5$. Its CI threshold applies to the mean of the five samples. Those settings are a regression detector for the deterministic synthetic workload, not proof of a universal runtime bound.

## Alternatives

For multi-asset or high-frequency workloads, row-wise Python iteration becomes a bottleneck. Vectorized accounting, NumPy arrays, or compiled kernels may be appropriate only after a benchmark demonstrates that the current implementation is the limiting factor. Such a change must preserve the documented trade-timing convention and be checked against golden analytical cases.
