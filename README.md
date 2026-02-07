
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


## 🚀 Features
- 🔍 **Stock Analysis** – Query real-time market prices (e.g., AAPL, TSLA, GOOG).  
- 📡 **MCP Integration** – Uses [Model Context Protocol (MCP)](https://modelcontextprotocol.io) to standardize tool access.  
- 🔄 **n8n Automation** – Automates alerts and workflows (e.g., sending daily stock updates to Slack/Discord).  
- 🏗️ **Production-Ready** – Modular code, automation-ready, and extendable.  


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


git clone https://github.com/Trojan3877/Quant-LLM-Assistant.git
cd Quant-LLM-Assistant
pip install -r requirements.txt
python src/agent.py


## 📌 Overview
Overview
- **Purpose:** Answer finance-related queries using LLMs, real-time or historical data.
- **Application:** Tailored for analysts, portfolio managers, and traders.
- **Why it Matters:** Saves time with smart, data-backed financial insights.


Tech Stack
![Python](https://img.shields.io/badge/Python-3.9-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-enabled-informational)
![CI/CD](https://img.shields.io/badge/CI/CD-enabled-brightgreen)
![Docker](https://img.shields.io/badge/Docker-ready-blue)
![MIT License](https://img.shields.io/badge/License-MIT-green)


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

Design Questions & Reflections
Q: What problem does this project aim to solve?
A: The QUANT LLM Assistant project was built to explore how a language model interface could be combined with quantitative reasoning, data retrieval, and structured responses to support real analytical workflows, rather than just casual chat. My focus was on understanding how to translate complex requests into actionable, structured outputs.
Q: Why did I choose this architecture and approach instead of a simpler model interaction?
A: I chose to build wrappers and prompts that guide the model toward quantitative reasoning because generic chat responses often lack the precision needed for analytical tasks. This meant spending time on prompt engineering, context structuring, and evaluation patterns instead of relying on default model interactions.
Q: What were the main trade-offs I made?
A: The main trade-off was between having a flexible assistant versus having a domain-structured one. By constraining prompts and focusing on quantitative tasks, I limited the breadth of the model’s responses in exchange for more accurate and reliable outputs in targeted analytical contexts.
Q: What didn’t work as expected?
A: Some prompts produced inconsistent output structure even when designed carefully, which highlighted how sensitive LLM interactions are to subtle wording changes. Fixing this required iterative prompt refinement and testing with varying input examples.
Q: What did I learn from building this project?
A: I learned that working with language models for structured reasoning isn’t just about the model itself — it’s about how you frame problems, engineer prompts, and validate outputs. I also gained experience in building repeatable evaluation patterns so I could track how changes in prompts affected responses.
Q: If I had more time or resources, what would I improve next?
A: I would build automated test suites with expected output patterns so prompt changes can be evaluated systematically, and explore ways to combine symbolic reasoning modules with the language model to reduce inconsistency and improve factual precision.