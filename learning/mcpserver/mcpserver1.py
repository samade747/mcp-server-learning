from mcp.server.fastmcp import FastMCP


mcp = FastMCP(name="my_mcp", stateless_http=True)

# tools

@mcp.tool 
def hello():
    """Returns a greeting message."""
    # api calling logics
    # db calling logics

    return "Hello from MCP Server 1!"


#----- resouces -----




mcp_app = mcp.streamable_http_app()
 


# run command
# uv run uvicorn --host 0.0.0.0 mcp_server1:mcp_app --reload
