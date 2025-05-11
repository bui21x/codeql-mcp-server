# CodeQL MCP Server

A Model Context Protocol (MCP) server that provides CodeQL integration for AI agents.

## Features

- Code security analysis
- Query execution
- JSON results format
- Health monitoring

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install CodeQL CLI

3. Run server:
```bash
uvicorn src.mcp_server:app --reload
```

## API Endpoints

- POST /analyze - Run CodeQL analysis
- GET /health - Check server health

## MCP Integration

This server follows the MCP specification for tool integration with AI agents.