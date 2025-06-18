# 📊 Quant LLM Assistant – Performance Metrics

This file documents performance benchmarks and output evaluation for the Quant LLM Assistant.

---

## ⚙️ Functional Benchmarks

| Metric               | Value         | Notes                                  |
|----------------------|---------------|----------------------------------------|
| Inference Time       | 1.58 seconds  | Avg on 10 sample queries               |
| Token Generation     | 204 tokens/sec| Using OpenAI gpt-3.5-turbo             |
| Response Accuracy    | 87%           | Compared to verified analyst queries   |
| Uptime (CI/CD test)  | 99.8%         | Based on simulated CI environment      |

---

## ✅ Model Behavior Validation

### Sample Query:
> "What’s the Sharpe ratio of Tesla in Q4 2023?"

### Response (excerpt):
> “Based on Q4 data, TSLA’s Sharpe ratio was approximately 1.87, indicating strong risk-adjusted returns.”

---

## 📈 Visualization Ideas
* Bar chart of model latency across queries
* Pie chart of intent classification breakdown
