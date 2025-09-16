
# mcp server using fastmcp
from mcp.server.fastmcp import FastMCP

# create an instance of FastMCP
app = FastMCP(name="mcp_server", stateless_http=True)

# 
mcp = app.streamable_http_app()



# run
# uv run uvicorn server_basic.mcpserver2:mcp --reload 