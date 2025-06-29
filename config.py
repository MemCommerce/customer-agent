from os import getenv

from dotenv import load_dotenv


load_dotenv()

CUSTOMER_MCP_URL = getenv("CUSTOMER_MCP_URL", "http://localhost:8000/mcp")
