# LLM-Powered Quantitative Research Assistant

[![CI Status](https://github.com/Trojan3877/quant-llm-assistant/actions/workflows/ci.yml/badge.svg)](https://github.com/Trojan3877/quant-llm-assistant/actions/workflows/ci.yml)
[![Docker Pulls](https://img.shields.io/docker/pulls/trojan3877/quant-llm-assistant)](https://hub.docker.com/r/trojan3877/quant-llm-assistant)
[![Helm Chart Version](https://img.shields.io/helm/v/quant-llm-assistant?repository_url=https://github.com/Trojan3877/quant-llm-assistant)](https://github.com/Trojan3877/quant-llm-assistant/tree/main/helm/quant-llm-assistant)
[![Documentation](https://img.shields.io/badge/docs-latest-blue)](https://github.com/Trojan3877/quant-llm-assistant/tree/main/docs)
[![Issues](https://img.shields.io/github/issues/Trojan3877/quant-llm-assistant)](https://github.com/Trojan3877/quant-llm-assistant/issues)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A Python tool that leverages large language models to fetch, analyze, and report on financial market data via natural-language prompts. Ideal for quant analysts, data scientists, and anyone wanting ad-hoc financial insights.

---

## 🚀 Features

- **Natural-Language Queries**  
  Ask questions like “What was AAPL’s daily volatility last month?” or “Plot the 200-day moving average for SPY.”

- **Data API Integration**  
  Plug in your favorite market-data provider (Alpha Vantage, Yahoo Finance, etc.) via a simple wrapper.

- **LLM-Powered Analysis**  
  Use LangChain/OpenAI under the hood to synthesize data, generate commentary, and propose trading signals.

- **Extensible Architecture**  
  Modular code: swap in new data sources, customize analysis routines, or add plotting capabilities.

---

## 📦 Installation

1. Clone the repo  
   ```bash
   git clone git@github.com:Trojan3877/quant-llm-assistant.git
   cd quant-llm-assistant

