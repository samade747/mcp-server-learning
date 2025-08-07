from mcp.client.streamable_http import streamablehttp_client
from mcp.client.session import ClientSession
import rich

async def main():
    async with streamablehttp_client(url="http://localhost:8000")