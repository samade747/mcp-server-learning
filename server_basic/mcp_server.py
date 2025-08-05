# mcp server
# fastmcp is class we get it her 
# server ko clients request bhejte hain request ko handle krte hain
# and response bhejte hain
# fastmcp is a class we get it here
# the server sends requests to clients, handles the requests, and sends responses


from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="mcp_server", stateless_http=True)

#------------------ tools --------------------

@mcp.tool
def hello(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}!"

@mcp.tool
def add(a: int, b: int) -> int:
    return a + b

#------------------ app --------------------


mcp_app = mcp.streamable_http_app()


