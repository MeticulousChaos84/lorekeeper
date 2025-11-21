#!/usr/bin/env python3
"""
Obsidian Vault Connector - MCP Server for Claude Desktop
=========================================================

This is an MCP (Model Context Protocol) server that gives Claude Desktop
proper access to your Obsidian vault. Instead of just raw filesystem access,
Gale gets actual TOOLS that understand Obsidian's structure.

WHAT YOU NEED TO SET UP (on the Obsidian side):
1. Install the "Local REST API" plugin in Obsidian
2. Enable it and note the API key it generates
3. Default runs on http://127.0.0.1:27123

For the bonus plugins:
- Omnisearch: Just install it, the REST API plugin exposes its endpoints
- Smart Connections: Same deal - install it, REST API exposes it

Then configure Claude Desktop to use this MCP server (see bottom of file).

Author: Cody @ MeticulousChaos Creative Labs
Glitch approves this message.
"""

import os
import json
import httpx
from typing import Any
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
    CallToolResult,
)

# =============================================================================
# CONFIGURATION
# =============================================================================
# These can be overridden with environment variables
# (useful when you configure the MCP server in Claude Desktop)

OBSIDIAN_API_URL = os.getenv("OBSIDIAN_API_URL", "http://127.0.0.1:27123")
OBSIDIAN_API_KEY = os.getenv("OBSIDIAN_API_KEY", "")

# =============================================================================
# THE MCP SERVER ITSELF
# =============================================================================
# MCP servers expose "tools" that Claude can use. Think of each tool as a
# specific capability - "read this note", "search the vault", etc.
#
# The server communicates via stdio (standard input/output), which is how
# Claude Desktop talks to MCP servers.

server = Server("obsidian-vault-connector")

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================
# These do the actual work of talking to Obsidian's REST API

def get_headers(content_type: str | None = None) -> dict:
    """
    Build the headers for Obsidian REST API requests.
    The API key is required - without it, Obsidian won't talk to us.

    Args:
        content_type: The Content-Type for the request body, if any.
                     Use "text/markdown" for note content, "application/json" for JSON.
                     Leave None for GET/DELETE requests with no body.
    """
    headers = {
        # Accept tells the API what format we want BACK
        "Accept": "application/json",
    }
    # Content-Type tells the API what format we're SENDING
    # Only include this when we actually have a body to send
    if content_type:
        headers["Content-Type"] = content_type

    if OBSIDIAN_API_KEY:
        headers["Authorization"] = f"Bearer {OBSIDIAN_API_KEY}"
    return headers


async def obsidian_get(endpoint: str, params: dict | None = None) -> dict | str | list:
    """
    Make a GET request to the Obsidian REST API.

    Args:
        endpoint: API endpoint (e.g., "/vault/", "/search/simple/")
        params: Optional query parameters
    """
    url = f"{OBSIDIAN_API_URL}{endpoint}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                url,
                headers=get_headers(),  # No Content-Type for GET
                params=params
            )
            response.raise_for_status()

            content_type = response.headers.get("content-type", "")
            if "application/json" in content_type:
                return response.json()
            else:
                return response.text

        except httpx.HTTPStatusError as e:
            return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
        except httpx.ConnectError:
            return {
                "error": "Could not connect to Obsidian. "
                "Is it running? Is the Local REST API plugin enabled?"
            }
        except Exception as e:
            return {"error": str(e)}


async def obsidian_write(
    method: str,
    endpoint: str,
    content: str
) -> dict | str | list:
    """
    Write content to the Obsidian REST API (for note creation/updates).

    The Obsidian API expects raw markdown content with text/markdown Content-Type,
    NOT JSON-wrapped content.

    Args:
        method: HTTP method (PUT for create/overwrite, POST for append)
        endpoint: API endpoint (e.g., "/vault/path/to/note.md")
        content: Raw markdown content to write
    """
    url = f"{OBSIDIAN_API_URL}{endpoint}"

    async with httpx.AsyncClient() as client:
        try:
            # Send raw content with text/markdown Content-Type
            headers = get_headers(content_type="text/markdown")

            if method == "PUT":
                response = await client.put(url, headers=headers, content=content)
            elif method == "POST":
                response = await client.post(url, headers=headers, content=content)
            else:
                return {"error": f"Unsupported method for write: {method}"}

            response.raise_for_status()

            content_type = response.headers.get("content-type", "")
            if "application/json" in content_type:
                return response.json()
            else:
                return response.text

        except httpx.HTTPStatusError as e:
            return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
        except httpx.ConnectError:
            return {
                "error": "Could not connect to Obsidian. "
                "Is it running? Is the Local REST API plugin enabled?"
            }
        except Exception as e:
            return {"error": str(e)}


async def obsidian_delete(endpoint: str) -> dict | str | list:
    """
    Delete a file via the Obsidian REST API.

    Args:
        endpoint: API endpoint (e.g., "/vault/path/to/note.md")
    """
    url = f"{OBSIDIAN_API_URL}{endpoint}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(url, headers=get_headers())
            response.raise_for_status()

            content_type = response.headers.get("content-type", "")
            if "application/json" in content_type:
                return response.json()
            else:
                return response.text

        except httpx.HTTPStatusError as e:
            return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
        except httpx.ConnectError:
            return {
                "error": "Could not connect to Obsidian. "
                "Is it running? Is the Local REST API plugin enabled?"
            }
        except Exception as e:
            return {"error": str(e)}


async def obsidian_post_json(endpoint: str, data: dict) -> dict | str | list:
    """
    Make a POST request with JSON body to the Obsidian REST API.
    Used for plugin endpoints that expect JSON.

    Args:
        endpoint: API endpoint
        data: JSON data to send
    """
    url = f"{OBSIDIAN_API_URL}{endpoint}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                url,
                headers=get_headers(content_type="application/json"),
                json=data
            )
            response.raise_for_status()

            content_type = response.headers.get("content-type", "")
            if "application/json" in content_type:
                return response.json()
            else:
                return response.text

        except httpx.HTTPStatusError as e:
            return {"error": f"HTTP {e.response.status_code}: {e.response.text}"}
        except httpx.ConnectError:
            return {
                "error": "Could not connect to Obsidian. "
                "Is it running? Is the Local REST API plugin enabled?"
            }
        except Exception as e:
            return {"error": str(e)}


# =============================================================================
# TOOL DEFINITIONS
# =============================================================================
# This is where we tell the MCP protocol what tools we offer.
# Claude Desktop reads this list and knows what it can ask us to do.

@server.list_tools()
async def list_tools() -> list[Tool]:
    """
    Return the list of tools this MCP server provides.

    Each tool has:
    - name: What Claude calls it
    - description: What it does (Claude reads this to decide when to use it)
    - inputSchema: JSON Schema describing the parameters
    """
    return [
        # =====================================================================
        # CORE VAULT TOOLS
        # =====================================================================
        Tool(
            name="vault_list_files",
            description=(
                "List all files and folders in the Obsidian vault, or in a "
                "specific directory. Returns the vault structure so you can "
                "understand what's available."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "directory": {
                        "type": "string",
                        "description": (
                            "Optional subdirectory path to list. "
                            "Leave empty for root vault."
                        )
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="vault_read_note",
            description=(
                "Read the contents of a specific note from the Obsidian vault. "
                "Provide the path relative to vault root (e.g., 'folder/note.md')."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the note, relative to vault root"
                    }
                },
                "required": ["path"]
            }
        ),
        Tool(
            name="vault_create_note",
            description=(
                "Create a new note in the Obsidian vault. "
                "Provide the path and content for the new note."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path for the new note (e.g., 'folder/new-note.md')"
                    },
                    "content": {
                        "type": "string",
                        "description": "Markdown content for the note"
                    }
                },
                "required": ["path", "content"]
            }
        ),
        Tool(
            name="vault_update_note",
            description=(
                "Update/overwrite an existing note in the Obsidian vault. "
                "This replaces the entire content of the note."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the existing note"
                    },
                    "content": {
                        "type": "string",
                        "description": "New markdown content for the note"
                    }
                },
                "required": ["path", "content"]
            }
        ),
        Tool(
            name="vault_append_to_note",
            description=(
                "Append content to the end of an existing note. "
                "Great for adding to daily notes, logs, or ongoing documents."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the existing note"
                    },
                    "content": {
                        "type": "string",
                        "description": "Content to append to the note"
                    }
                },
                "required": ["path", "content"]
            }
        ),
        Tool(
            name="vault_delete_note",
            description=(
                "Delete a note from the Obsidian vault. "
                "Use with caution - this is permanent!"
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the note to delete"
                    }
                },
                "required": ["path"]
            }
        ),
        Tool(
            name="vault_search",
            description=(
                "Search for text across all notes in the vault using "
                "Obsidian's built-in search. Returns matching notes and context."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": (
                            "Search query. Supports Obsidian search syntax "
                            "(e.g., 'tag:#mytag', 'path:folder/', etc.)"
                        )
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="vault_get_active_note",
            description=(
                "Get the currently active/open note in Obsidian. "
                "Useful for context-aware operations."
            ),
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),

        # =====================================================================
        # OMNISEARCH PLUGIN TOOLS
        # =====================================================================
        # These only work if you have Omnisearch installed in Obsidian

        Tool(
            name="omnisearch_search",
            description=(
                "Search the vault using Omnisearch plugin (if installed). "
                "Omnisearch provides better fuzzy matching and ranking than "
                "the built-in search. Returns results with relevance scores."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query for Omnisearch"
                    }
                },
                "required": ["query"]
            }
        ),

        # =====================================================================
        # SMART CONNECTIONS PLUGIN TOOLS
        # =====================================================================
        # These only work if you have Smart Connections installed

        Tool(
            name="smart_connections_find_similar",
            description=(
                "Find notes semantically similar to a given note using the "
                "Smart Connections plugin (if installed). Uses AI embeddings "
                "to find conceptually related notes, not just keyword matches."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the note to find similar notes for"
                    }
                },
                "required": ["path"]
            }
        ),
        Tool(
            name="smart_connections_search",
            description=(
                "Semantic search across the vault using Smart Connections "
                "(if installed). Finds notes by meaning, not just keywords."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Natural language search query"
                    }
                },
                "required": ["query"]
            }
        ),
    ]


# =============================================================================
# TOOL IMPLEMENTATIONS
# =============================================================================
# This is where the magic happens. When Claude calls a tool, we handle it here.

@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> CallToolResult:
    """
    Handle tool calls from Claude.

    This is the dispatcher - it routes the tool name to the right implementation.
    """

    try:
        # =====================================================================
        # CORE VAULT OPERATIONS
        # =====================================================================

        if name == "vault_list_files":
            directory = arguments.get("directory", "")
            # The REST API uses /vault/ endpoint for file listing
            endpoint = f"/vault/{directory}" if directory else "/vault/"
            result = await obsidian_get(endpoint)

        elif name == "vault_read_note":
            path = arguments["path"]
            # Reading a specific file
            result = await obsidian_get(f"/vault/{path}")

        elif name == "vault_create_note":
            path = arguments["path"]
            content = arguments["content"]
            # PUT creates or overwrites - send raw markdown content
            result = await obsidian_write("PUT", f"/vault/{path}", content)
            if not isinstance(result, dict) or "error" not in result:
                result = {"success": True, "message": f"Created note: {path}"}

        elif name == "vault_update_note":
            path = arguments["path"]
            content = arguments["content"]
            # PUT overwrites - send raw markdown content
            result = await obsidian_write("PUT", f"/vault/{path}", content)
            if not isinstance(result, dict) or "error" not in result:
                result = {"success": True, "message": f"Updated note: {path}"}

        elif name == "vault_append_to_note":
            path = arguments["path"]
            content = arguments["content"]
            # POST appends - send raw markdown content
            result = await obsidian_write("POST", f"/vault/{path}", content)
            if not isinstance(result, dict) or "error" not in result:
                result = {"success": True, "message": f"Appended to note: {path}"}

        elif name == "vault_delete_note":
            path = arguments["path"]
            result = await obsidian_delete(f"/vault/{path}")
            if not isinstance(result, dict) or "error" not in result:
                result = {"success": True, "message": f"Deleted note: {path}"}

        elif name == "vault_search":
            query = arguments["query"]
            # Search uses POST with JSON body
            result = await obsidian_post_json("/search/", {"query": query})

        elif name == "vault_get_active_note":
            # Get the currently active file
            result = await obsidian_get("/active/")

        # =====================================================================
        # OMNISEARCH PLUGIN
        # =====================================================================

        elif name == "omnisearch_search":
            query = arguments["query"]
            # Omnisearch exposes its API - try GET with query param first
            result = await obsidian_get("/omnisearch/", params={"query": query})

        # =====================================================================
        # SMART CONNECTIONS PLUGIN
        # =====================================================================

        elif name == "smart_connections_find_similar":
            path = arguments["path"]
            # Smart Connections API endpoint for finding similar notes
            result = await obsidian_post_json(
                "/smart-connections/find-similar/",
                {"path": path}
            )

        elif name == "smart_connections_search":
            query = arguments["query"]
            # Smart Connections semantic search
            result = await obsidian_post_json(
                "/smart-connections/search/",
                {"query": query}
            )

        else:
            result = {"error": f"Unknown tool: {name}"}

        # Format the result for MCP
        if isinstance(result, dict):
            result_text = json.dumps(result, indent=2)
        elif isinstance(result, list):
            result_text = json.dumps(result, indent=2)
        else:
            result_text = str(result)

        return CallToolResult(
            content=[TextContent(type="text", text=result_text)]
        )

    except Exception as e:
        return CallToolResult(
            content=[TextContent(type="text", text=f"Error: {str(e)}")]
        )


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

async def main():
    """
    Start the MCP server.

    This runs the server using stdio transport - Claude Desktop connects to it
    by launching this script and communicating over stdin/stdout.
    """
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())


# =============================================================================
# SETUP INSTRUCTIONS
# =============================================================================
#
# 1. OBSIDIAN SETUP:
#    - Install "Local REST API" plugin from Community Plugins
#    - Enable it in settings
#    - Copy the API key from its settings
#    - (Optional) Install Omnisearch and/or Smart Connections for bonus features
#
# 2. INSTALL DEPENDENCIES:
#    pip install mcp httpx
#
# 3. CONFIGURE CLAUDE DESKTOP:
#    Add this to your Claude Desktop config (usually ~/Library/Application Support/Claude/claude_desktop_config.json on Mac):
#
#    {
#      "mcpServers": {
#        "obsidian": {
#          "command": "python",
#          "args": ["/path/to/this/server.py"],
#          "env": {
#            "OBSIDIAN_API_KEY": "your-api-key-here"
#          }
#        }
#      }
#    }
#
# 4. RESTART CLAUDE DESKTOP
#    The Obsidian tools should now be available!
#
# =============================================================================
