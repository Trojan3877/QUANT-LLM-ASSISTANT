import argparse
from .data_client import DataClient
from .llm_agent import LLMAgent

def main():
    parser = argparse.ArgumentParser(
        description="LLM-Powered Quantitative Research Assistant"
    )
    parser.add_argument(
        "--query", "-q", type=str, required=True,
        help="Natural-language query for the assistant"
    )
    parser.add_argument(
        "--symbol", "-s", type=str, default=None,
        help="Optional ticker symbol context (e.g., AAPL)"
    )
    args = parser.parse_args()

    # Initialize clients
    data_client = DataClient()
    agent = LLMAgent()

    # If a symbol is provided, fetch some data to give context
    context = ""
    if args.symbol:
        ts = data_client.get_daily_time_series(args.symbol, outputsize="compact")
        # Simple context prep: latest close price
        latest_date = sorted(ts["Time Series (Daily)"].keys())[-1]
        latest_close = ts["Time Series (Daily)"][latest_date]["4. close"]
        context = (
            f"The latest closing price for {args.symbol} on {latest_date} "
            f"was {latest_close}.\n"
        )

    prompt = context + args.query
    print("🧠 Sending to LLM…")
    response = agent.ask(prompt)
    print("\n💡 Assistant Response:\n")
    print(response)

if __name__ == "__main__":
    main()

git add src/main.py
git commit -m "Add CLI entrypoint script in src/main.py"
