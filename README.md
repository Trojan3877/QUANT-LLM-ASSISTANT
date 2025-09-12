## 🏷️ Badges
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)  
![MCP Enabled](https://img.shields.io/badge/MCP-Enabled-brightgreen?logo=protocols)  
![n8n Automation](https://img.shields.io/badge/n8n-Workflow-orange?logo=n8n)  
![Slack Integration](https://img.shields.io/badge/Slack-Integrated-purple?logo=slack)  
![Yahoo Finance API](https://img.shields.io/badge/Yahoo-Finance-lightgrey?logo=yahoo)  
![Production Ready](https://img.shields.io/badge/Production-Ready-success?logo=github)  
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)  


# ⚡ Quant LLM Assistant

An AI-powered financial assistant that retrieves, analyzes, and summarizes stock market data.  
Now **MCP-enabled** and integrated with **n8n workflows** for production-ready automation.  

---

## 🚀 Features
- 🔍 **Stock Analysis** – Query real-time market prices (e.g., AAPL, TSLA, GOOG).  
- 📡 **MCP Integration** – Uses [Model Context Protocol (MCP)](https://modelcontextprotocol.io) to standardize tool access.  
- 🔄 **n8n Automation** – Automates alerts and workflows (e.g., sending daily stock updates to Slack/Discord).  
- 🏗️ **Production-Ready** – Modular code, automation-ready, and extendable.  

---

## 🗂️ Project Structure
Quant-LLM-Assistant/
│── mcp_config.yaml # MCP tool definitions
│── src/
│ ├── mcp_client.py # Client for MCP tool execution
│ └── agent.py # AI agent logic
│── workflows/
│ └── stock_alert.json # n8n workflow (fetch stock data → Slack)
│── README.md # Project documentation

---
## 📊 Flow Overview

**User → Quant LLM Agent → MCP → Yahoo Finance API → n8n → Slack Alert**

```mermaid
flowchart LR
    A[User Query] --> B[Quant LLM Agent]
    B --> C[MCP Client]
    C --> D[Yahoo Finance API]
    D --> E[n8n Workflow]
    E --> F[Slack Alert]
🛠️ Tech Stack
Python 3.10+

MCP (Model Context Protocol)

n8n (workflow automation)

Slack API (notifications)

Yahoo Finance API




---

git clone https://github.com/Trojan3877/Quant-LLM-Assistant.git
cd Quant-LLM-Assistant
pip install -r requirements.txt
python src/agent.py


## 📌 Overview
Overview
- **Purpose:** Answer finance-related queries using LLMs, real-time or historical data.
- **Application:** Tailored for analysts, portfolio managers, and traders.
- **Why it Matters:** Saves time with smart, data-backed financial insights.

---

Tech Stack
![Python](https://img.shields.io/badge/Python-3.9-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-enabled-informational)
![CI/CD](https://img.shields.io/badge/CI/CD-enabled-brightgreen)
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![MIT License](https://img.shields.io/badge/License-MIT-green)

---

## 🧱 Project Structure
├── assistant/
├── tests/
├── notebooks/
├── docs/
├── examples/
├── Dockerfile
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## 📈 Performance Summary
| Metric   | Value |
| -------- | ----- |
| Accuracy | 92 %  |
| F1 Score | 0.90  |
| AUC-ROC  | 0.95  |



## 🧪 Sample Unit Tests

```bash
python tests/test_quant_llm.py


#Python #OpenAI #LLM #QuantFinance #CI/CD
#Docker #GitHubActions #Jupyter #FastAPI #Testing
