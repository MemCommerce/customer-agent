from os import getenv, environ

from dotenv import load_dotenv


load_dotenv()

CUSTOMER_MCP_URL = getenv("CUSTOMER_MCP_URL", "http://localhost:8000/mcp")

MONGO_USER = getenv("MONGO_USER")
MONGO_PASS = getenv("MONGO_PASS")
MONGO_URI = getenv("MONGO_URI")
MONGO_APP = getenv("MONGO_APP")
MONGO_DB = environ["MONGO_DB"]
