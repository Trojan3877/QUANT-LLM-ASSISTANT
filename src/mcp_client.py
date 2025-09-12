"""
mcp_client.py
--------------
This module loads the MCP configuration and executes tool calls
defined in mcp_config.yaml. It currently supports API-type tools.
"""

import yaml
import requests
import os

class MCPClient:
    def __init__(self, config_path: str = "mcp_config.yaml"):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self):
        """Load MCP config from YAML file."""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"MCP config not found: {self.config_path}")

        with open(self.config_path, "r") as f:
            return yaml.safe_load(f)

    def get_tool(self, tool_name: str):
        """Retrieve a tool definition by name."""
        for tool in self.config.get("tools", []):
            if tool["name"] == tool_name:
                return tool
        raise ValueError(f"Tool '{tool_name}' not found in MCP config.")

    def call_tool(self, tool_name: str, **kwargs):
        """Call a tool defined in the MCP config."""
        tool = self.get_tool(tool_name)

        if tool["type"] == "api":
            endpoint = tool["endpoint"]
            response = requests.get(endpoint, params=kwargs)
            if response.status_code == 200:
                return response.json()
            else:
                raise RuntimeError(
                    f"API call failed ({response.status_code}): {response.text}"
                )
        else:
            raise NotImplementedError(
                f"Tool type '{tool['type']}' not supported yet."
            )


# Example usage
if __name__ == "__main__":
    client = MCPClient()
    result = client.call_tool("get_stock_data", symbols="AAPL")
    print(result)
