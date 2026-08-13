# Academic Audit: Quant LLM Assistant

## Scope and evidence standard

This audit evaluates the repository as a research-software portfolio artifact. A statement is classified as **MEASURED** only when an implementation and versioned output support it; **DERIVED** when it follows directly from source; **OBSERVED** when it describes the checked-in repository; and **ASPIRATIONAL** when it is a plan rather than an established capability.

The repository is a hybrid research CLI: it validates external market-data responses, passes bounded and labeled context to an LLM, and includes a deterministic single-instrument backtest engine. It deliberately excludes brokerage execution.

## Evidence currently present

| Dimension | Assessment | Evidence |
|---|---|---|
| Direct algorithmic work | **DERIVED** | `src/backtest.py` implements position transitions, equity accounting, total return, and maximum drawdown directly. |
| Data-boundary engineering | **OBSERVED** | `src/data_client.py` validates symbols, provider payload shape, status failures, throttling messages, timeouts, and HTTPS configuration. |
| LLM-boundary engineering | **OBSERVED** | `src/llm_agent.py` constrains prompt size, generation parameters, retries, and a research-only system policy. |
| Mathematical correctness tests | **OBSERVED** | `tests/test_core.py` checks an analytical long-position return/drawdown example plus invalid data and position cases. |
| Runtime evidence | **OBSERVED** | `benchmarks/latency_benchmark.py` writes commit-bound raw timing samples and summary statistics; CI stores the generated JSON as an artifact. |
| Deployment maturity | **ASPIRATIONAL** | Container and deployment reference assets exist, but the README correctly states that no deployment target is configured. |

## Strengths for an academic reviewer

1. **The core financial accounting is explicit.** The backtester does not hide its state transition under a portfolio framework. Its cash, position, holdings, equity, return, and drawdown definitions can be inspected and tested.
2. **The system makes trust boundaries concrete.** Provider responses and model output are handled as fallible inputs rather than authoritative financial truth.
3. **The latency harness records protocol and environment metadata.** It preserves sample-level data, summary statistics, workload dimensions, runner information, and commit provenance instead of relying on a static performance claim.
4. **Tests emphasize failure paths.** The suite covers malformed external data, invalid symbols, invalid prices, illegal position values, and empty model output.

## Gaps and limitations

| Gap | Classification | Why it matters |
|---|---|---|
| No versioned market dataset or temporal train/validation/test protocol | **OBSERVED** | The repository cannot support predictive, calibration, or out-of-sample financial-performance claims. |
| No strategy baseline comparison | **OBSERVED** | The backtester evaluates a supplied signal but does not compare it with buy-and-hold, cash, or a stated benchmark. |
| No transaction-cost, slippage, liquidity, borrow, tax, or corporate-action model | **OBSERVED** | Raw single-unit returns materially overstate what an executable strategy result would mean. |
| No repeated-seed model evaluation or confidence interval | **OBSERVED** | The code has no stochastic predictive model evaluation; latency repeats are performance samples, not statistical evidence of financial efficacy. |
| LLM analysis delegates semantics to an external model | **OBSERVED** | The LLM is a constrained explanation boundary, not a demonstrated forecasting or optimization method. |
| The CI latency threshold is a budget, not a benchmark result | **DERIVED** | `0.25 s` is a failure threshold for a fixed synthetic workload and must not be presented as production capacity or an SLO. |

## Research questions the repository can support after additional data and experiment work

1. How do long/flat/short signals compare with cash and buy-and-hold under a chronological, leakage-controlled split?
2. How do results change after fees, spread, slippage, and borrow costs are added?
3. How sensitive are total return and maximum drawdown to signal timing and the convention for trade execution?
4. How does deterministic backtest latency scale with number of price rows and strategy-computation cost?
5. Does an LLM summary improve analyst workflow quality under a blinded rubric without increasing unsupported certainty?

## Claims policy

Appropriate current language is “research CLI,” “deterministic backtest example,” “CI regression budget,” and “research-only output.” Inappropriate language without further evidence includes “profitable,” “accurate forecast,” “low-latency service,” “production proven,” “robust trading system,” and “enterprise-grade execution.”

## Recommended next experiments

Before making model-quality claims, add a licensed, versioned dataset with date lineage; pre-register a chronological split; compare against cash and buy-and-hold; apply realistic costs; retain per-period equity curves; and report multiple periods or resamples with uncertainty. Keep those experiments separate from fast unit tests and avoid sending private data or secrets to model providers.
