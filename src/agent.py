"""
agent.py
--------
Quant LLM Assistant agent that uses MCPClient to call external tools.
This is where the LLM (or any AI reasoning module) connects to MCP.
"""

from mcp_client.py import MCPClient
import json

class QuantLLMAgent:
    def __init__(self):
        self.client = MCPClient()

    def analyze_stock(self, symbol: str):
        """
        Example reasoning step:
        1. Query stock data via MCP
        2. Format the response
        3. Return structured result
        """
        try:
            raw_data = self.client.call_tool("get_stock_data", symbols=symbol)

            # Extract relevant fields
            quote = raw_data.get("quoteResponse", {}).get("result", [])[0]
            price = quote.get("regularMarketPrice", "N/A")
            currency = quote.get("currency", "USD")
            name = quote.get("shortName", symbol)

            return {
                "symbol": symbol,
                "name": name,
                "price": price,
                "currency": currency
            }

        except Exception as e:
            return {"error": str(e)}

    def run(self, query: str):
        """
        Basic dispatcher:
        - If the query looks like a stock lookup, call analyze_stock()
        - Later, you can extend with more reasoning/tool use
        """
        query = query.strip().upper()

        if query.isalpha() and len(query) <= 5:  # crude stock symbol check
            return self.analyze_stock(query)
        else:
            return {"message": f"Sorry, I don't understand '{query}' yet."}


# Example usage
if __name__ == "__main__":
    agent = QuantLLMAgent()
    result = agent.run("AAPL")
    print(json.dumps(result, indent=2))
