"""
Kimi 2 API Client Wrapper
=========================

Adapts the OpenAI SDK for Kimi 2 models to be compatible with the Claude SDK Client interface.
Implements specific tools locally since the API doesn't have a direct equivalent to the SDK's built-in tools.
Also bridges to the Puppeteer MCP server for browser automation.
"""

import json
import os
import subprocess
import asyncio
import shutil
from pathlib import Path
from typing import AsyncGenerator, Any, Optional

from openai import AsyncOpenAI
from dotenv import load_dotenv

# MCP Imports
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Define the message types to match Claude SDK's expected interface
class TextBlock:
    def __init__(self, text: str):
        self.text = text

class ToolUseBlock:
    def __init__(self, name: str, input: dict, id: str):
        self.name = name
        self.input = input
        self.id = id

class AssistantMessage:
    def __init__(self, content: list):
        self.content = content

class ToolResultBlock:
    def __init__(self, tool_use_id: str, content: str, is_error: bool = False):
        self.tool_use_id = tool_use_id
        self.content = content
        self.is_error = is_error

class UserMessage:
    def __init__(self, content: list):
        self.content = content

class KimiClient:
    """
    Client for interacting with Kimi 2 models via OpenAI SDK.
    Mimics the interface of ClaudeSDKClient for drop-in replacement.
    Includes built-in tool implementations and MCP client support.
    """
    
    def __init__(self, project_dir: Path, model: str):
        load_dotenv()
        self.project_dir = project_dir
        self.model = model
        self.api_key = os.environ.get("MOONSHOT_API_KEY")
        if not self.api_key:
             raise ValueError("MOONSHOT_API_KEY environment variable not set.")

        self.client = AsyncOpenAI(
            api_key=self.api_key,
            base_url="https://api.moonshot.ai/v1",
        )
        self.history = []
        self._setup_local_tools()
        
        # MCP State
        self.mcp_session: Optional[ClientSession] = None
        self.mcp_exit_stack = None

    def _setup_local_tools(self):
        """Define local tools (non-MCP)."""
        self.local_tools = [
            {
                "type": "function",
                "function": {
                    "name": "Bash",
                    "description": "Execute a bash command. Use this for file operations, running scripts, and system tasks.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "command": {
                                "type": "string",
                                "description": "The bash command to execute."
                            }
                        },
                        "required": ["command"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "Read",
                    "description": "Read the contents of a file.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "path": {
                                "type": "string",
                                "description": "Path to the file to read."
                            }
                        },
                        "required": ["path"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "Write",
                    "description": "Write content to a file. Overwrites existing content.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "path": {
                                "type": "string",
                                "description": "Path to the file to write."
                            },
                            "content": {
                                "type": "string",
                                "description": "Content to write to the file."
                            }
                        },
                        "required": ["path", "content"]
                    }
                }
            },
               {
                "type": "function",
                "function": {
                    "name": "glob",
                    "description": "List files matching a glob pattern.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "pattern": {
                                "type": "string",
                                "description": "The glob pattern to match (e.g., '*.py')."
                            },
                            "path": {
                                "type": "string",
                                "description": "Base directory path."
                            }
                        },
                        "required": ["pattern"]
                    }
                }
            }
        ]
        self.all_tools = self.local_tools.copy()

    async def _setup_mcp_server(self):
        """Connect to Puppeteer MCP server and load tools."""
        try:
            # Check for npx
            if not shutil.which("npx"):
                print("Warning: npx not found. Puppeteer MCP disabled.")
                return

            print("Starting Puppeteer MCP server...")
            server_params = StdioServerParameters(
                command="npx",
                args=["-y", "@modelcontextprotocol/server-puppeteer"],
                env=None
            )
            
            # Start the stdio client context
            self.mcp_ctx = stdio_client(server_params)
            read, write = await self.mcp_ctx.__aenter__()
            
            # Start the session
            self.mcp_session = ClientSession(read, write)
            await self.mcp_session.__aenter__()
            
            # Initialize
            await self.mcp_session.initialize()
            
            # List tools
            result = await self.mcp_session.list_tools()
            
            def sanitize_schema(schema):
                """Ensure schema is compatible with Kimi API/OpenAI SDK."""
                if schema.get("type") == "object" and "properties" not in schema:
                    # Kimi/OpenAI requires properties for type object
                    schema["properties"] = {}
                if "properties" in schema:
                    for prop, details in schema["properties"].items():
                        if isinstance(details, dict):
                            sanitize_schema(details)
                return schema

            # Convert to OpenAI format and register
            for tool in result.tools:
                # print(f"Registered MCP tool: {tool.name}")
                # Create a deep copy to avoid modifying original if needed, but here simple copy is fine for top level
                # json.loads(json.dumps(...)) is a cheap way to deep copy and ensure pure dicts
                schema_copy = json.loads(json.dumps(tool.inputSchema))
                sanitized_schema = sanitize_schema(schema_copy)

                openai_tool = {
                    "type": "function",
                    "function": {
                        "name": tool.name,  # Use raw name, e.g., "puppeteer_navigate"
                        "description": tool.description or "",
                        "parameters": sanitized_schema
                    }
                }
                self.all_tools.append(openai_tool)
                
        except Exception as e:
            print(f"Failed to setup Puppeteer MCP: {e}")
            # Don't crash, just proceed without MCP
            
    async def __aenter__(self):
        await self._setup_mcp_server()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.mcp_session:
            await self.mcp_session.__aexit__(exc_type, exc_val, exc_tb)
        if hasattr(self, 'mcp_ctx'):
            await self.mcp_ctx.__aexit__(exc_type, exc_val, exc_tb)

    async def query(self, prompt: str):
        """Add user message to history."""
        # If this is the first message, we might need to add a system prompt or just start
        if not self.history:
             self.history.append({
                "role": "system",
                "content": "You are an expert full-stack developer building a production-quality web application. Use the available tools to explore the codebase, write files, execute commands, and verify your work with the browser (puppeteer)."
            })

        self.history.append({"role": "user", "content": prompt})

    async def receive_response(self) -> AsyncGenerator[Any, None]:
        """
        Send request to Kimi and yield messages in the format expected by the agent.
        """
        
        while True:
            # Call Kimi API
            try:
                stream = await self.client.chat.completions.create(
                    model=self.model,
                    messages=self.history,
                    tools=self.all_tools,
                    temperature=0.6,
                    stream=True
                )
            except Exception as e:
                yield AssistantMessage(content=[TextBlock(text=f"Error calling Kimi API: {str(e)}")])
                return

            collected_text = ""
            tool_calls = []
            
            async for chunk in stream:
                delta = chunk.choices[0].delta
                if delta.content:
                    collected_text += delta.content
                if delta.tool_calls:
                   for tc_chunk in delta.tool_calls:
                       if tc_chunk.index >= len(tool_calls):
                           tool_calls.append({"id": "", "function": {"name": "", "arguments": ""}})
                       tc = tool_calls[tc_chunk.index]
                       if tc_chunk.id: tc["id"] += tc_chunk.id
                       if tc_chunk.function.name: tc["function"]["name"] += tc_chunk.function.name
                       if tc_chunk.function.arguments: tc["function"]["arguments"] += tc_chunk.function.arguments

            if collected_text:
                self.history.append({"role": "assistant", "content": collected_text})
                yield AssistantMessage(content=[TextBlock(text=collected_text)])
            
            if not tool_calls:
                break
            
            # Ensure all tool_calls have IDs
            import uuid
            for tc in tool_calls:
                if not tc["id"]:
                     tc["id"] = f"call_{uuid.uuid4().hex}"

            # Append full assistant message (with tool calls) to history FIRST
            tool_calls_data = []
            for tc in tool_calls:
                tool_calls_data.append({
                    "id": tc["id"],
                    "type": "function",
                    "function": {
                        "name": tc["function"]["name"],
                        "arguments": tc["function"]["arguments"]
                    }
                })
            
            # Update/Add Assistant message to history
            if collected_text and self.history[-1]["role"] == "assistant":
                # Replace the partial text message with full message including tool calls
                self.history.pop()
            
            self.history.append({
                "role": "assistant",
                "content": collected_text or None,
                "tool_calls": tool_calls_data
            })

            # Process tool calls AND append results
            assistant_content_blocks = []
            if collected_text:
                 assistant_content_blocks.append(TextBlock(text=collected_text))

            for tc in tool_calls:
                try:
                    name = tc["function"]["name"]
                    args_str = tc["function"]["arguments"]
                    args = json.loads(args_str)
                    tool_use_id = tc["id"]
                    
                    # Yield User-facing ToolUse event
                    tool_block = ToolUseBlock(name=name, input=args, id=tool_use_id)
                    assistant_content_blocks.append(tool_block)
                    yield AssistantMessage(content=[tool_block])
                    
                    # Execute
                    result_content = await self._execute_tool(name, args)
                    is_error = result_content.startswith("Error:")
                    
                    # Add to history (Tool Result)
                    self.history.append({
                        "role": "tool",
                        "tool_call_id": tool_use_id,
                        "name": name,
                        "content": result_content
                    })
                    
                    # Yield result event
                    yield UserMessage(content=[
                        ToolResultBlock(
                            tool_use_id=tool_use_id,
                            content=result_content,
                            is_error=is_error
                        )
                    ])
                    
                except json.JSONDecodeError:
                     error_msg = f"Error parsing arguments for tool {tc.get('function', {}).get('name')}"
                     yield AssistantMessage(content=[TextBlock(text=error_msg)])
                
            # Now the tool outputs are appended in the loop above.
            # Next iteration will send [..., Assistant(calls), Tool(result), Tool(result)]

    async def _execute_tool(self, name: str, args: dict) -> str:
        """Execute local or MCP tools."""
        try:
            # Local tools
            if name == "Bash":
                command = args.get("command")
                if not command: return "Error: No command provided"
                return self._run_bash(command)
            elif name == "Read":
                path = args.get("path")
                if not path: return "Error: No path provided"
                return self._read_file(path)
            elif name == "Write":
                path = args.get("path")
                content = args.get("content")
                if not path or content is None: return "Error: Path or content missing"
                return self._write_file(path, content)
            elif name == "glob":
                pattern = args.get("pattern")
                path = args.get("path", ".")
                return self._glob(pattern, path)
            
            # MCP Tools
            elif self.mcp_session:
                # Check if it's a known MCP tool (simplified check: try calling it if not local)
                # Ideally we check against registered list, but this is fine
                try:
                    result = await self.mcp_session.call_tool(name, arguments=args)
                    # Result content is a list of TextContent or ImageContent
                    # Flatten to string for LLM for now
                    output_text = []
                    for content in result.content:
                        if content.type == "text":
                            output_text.append(content.text)
                        elif content.type == "image":
                            output_text.append(f"[Image content: {content.mimeType}]")
                    return "\n".join(output_text)
                except Exception as mcp_err:
                     return f"Error executing MCP tool {name}: {str(mcp_err)}"
            
            else:
                return f"Error: Unknown tool {name}"
        except Exception as e:
            return f"Error executing {name}: {str(e)}"

    def _run_bash(self, command: str) -> str:
        try:
            result = subprocess.run(
                command,
                shell=True,
                cwd=self.project_dir,
                capture_output=True,
                text=True,
                timeout=30
            )
            output = result.stdout + result.stderr
            return output if output.strip() else "(No output)"
        except subprocess.TimeoutExpired:
            return "Error: Command timed out"
        except Exception as e:
            return f"Error running command: {str(e)}"

    def _read_file(self, path_str: str) -> str:
        path = self.project_dir / path_str
        try:
            if not path.is_relative_to(self.project_dir):
                return "Error: Access denied (outside project directory)"
            if not path.exists():
                return f"Error: File not found: {path_str}"
            return path.read_text(encoding="utf-8")
        except Exception as e:
            return f"Error reading file: {str(e)}"

    def _write_file(self, path_str: str, content: str) -> str:
        path = self.project_dir / path_str
        try:
            if not path.is_relative_to(self.project_dir):
                return "Error: Access denied (outside project directory)"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
            return f"Successfully wrote to {path_str}"
        except Exception as e:
            return f"Error writing file: {str(e)}"
            
    def _glob(self, pattern: str, path_str: str) -> str:
        try:
             base_path = self.project_dir / path_str
             if not base_path.is_relative_to(self.project_dir):
                 return "Error: Access denied"
             
             files = list(base_path.glob(pattern))
             return "\n".join([str(f.relative_to(self.project_dir)) for f in files])
        except Exception as e:
            return f"Error running glob: {str(e)}"
