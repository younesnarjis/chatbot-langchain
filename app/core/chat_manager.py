from typing import Dict, List, Optional, Any
from langchain_groq import ChatGroq
from app.core.tools.base import BaseTool
from app.core.tools.summarizer import TextSummarizer
from app.core.tools.translator import Translator
import logging

logger = logging.getLogger(__name__)

class ChatManager:
    def __init__(self, **kwargs):
        self.args = {
            "api_key": kwargs.get("api_key"),
            "model_name": kwargs.get("model_name", "mixtral-8x7b-32768"),
            "temperature": kwargs.get("temperature", 0.5),
            "max_tokens": kwargs.get("max_tokens", 1000),
        }

        # Initialize LLM
        self.llm = ChatGroq(**self.args)

        # Initialize tools
        self.tools: Dict[str, BaseTool] = {
            "summarizer": TextSummarizer(**self.args),
            "translator": Translator(**self.args)
        }

    async def process_message(
        self, 
        messages: Optional[List[Dict[str, str]] ] = None,
        tool: Optional[str] = None, 
        **kwargs
    ) -> str:
        """
        Process a message using either a specific tool or the general chat model
        """
        try:
            if tool is None or tool == "chat":
                return await self._handle_chat(messages)

            return await self._handle_tool_call(tool, **kwargs)
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")
            raise

    async def _handle_tool_call(self, tool_name: str, **kwargs) -> str:
        """Handle a specific tool call"""
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' not found")
        
        tool = self.tools[tool_name]
        try:
            # Validate input against tool's schema
            tool.input_schema(**kwargs)
            return await tool.run(**kwargs)
        except Exception as e:
            logger.error(f"Error executing tool '{tool_name}': {str(e)}")
            raise

    async def _handle_chat(self, messages: Optional[List[Dict[str, str]]] = None) -> str:
        """Handle a general chat message"""
        if not messages:
            raise ValueError("No messages provided")

        try:
            formatted_messages = [
                {"role": msg["role"], "content": msg["content"]}
                for msg in messages
            ]
            return await self.llm.ainvoke(formatted_messages[-1]["content"])
        except Exception as e:
            logger.error(f"Error in chat processing: {str(e)}")
            raise