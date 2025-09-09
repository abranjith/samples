# MCP-PY: Running server.py & client.py Locally with uv

This guide explains how to run the MCP server and client locally using [uv](https://github.com/astral-sh/uv) as the Python package manager.

## Prerequisites
- Python (version specified in `pyproject.toml`, e.g., >=3.13)
- [uv](https://github.com/astral-sh/uv) installed. You can install it via pipx:
  ```pwsh
  pipx install uv
  ```

## Install Dependencies
Navigate to the `mcp-py` directory and install dependencies:
```pwsh
cd mcp-py
uv pip install -e .
```

## Running the Server
Start the MCP server `server.py`:
```pwsh
uv python server.py
```
The server will start and listen for requests (default: http://localhost:8000/mcp).

## Running the Client
In a separate terminal, run the client to interact with the server:
```pwsh
uv python client.py
```

## Notes
- Ensure the server is running before starting the client.
- The database (`app.db`) will be created automatically in the project directory.
- You can modify the server/client code as needed and rerun using the above commands.

---
For more details, see the code in `server.py` and `client.py`.
