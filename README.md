# Potato-MCP

## Overview
This is my first attempt at creating an MCP (Model-Code-Protocol) for Claude. The project provides a simple filesystem interface that can be used to interact with files and directories.

## Requirements
- Python 3.11+
- Dependencies listed in `pyproject.toml`

## Features
This MCP is built using the FastMCP framework from the `mcp` package, providing tools for file management operations. It exposes four main functions:

- `list_files`: Lists all files in a specified directory
- `create_directory`: Creates a new directory at the specified path
- `create_object`: Creates a new file with optional content
- `delete_object`: Deletes a specified file

## Contributing
This is an experimental project. Feel free to fork and modify as needed.
