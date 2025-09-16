from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name='my_mcp', stateless_http=True)

mcp_app = mcp.streamable_http_app()