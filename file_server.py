@mcp.tool()
def read_file(path: str) -> str:
    """Read a file and return its contents."""
    with open(os.path.expanduser(path), 'r') as f:
        return f.read()
