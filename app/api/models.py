import logging
from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional

logger = logging.getLogger(__name__)

class ToolType(str, Enum):
    CHAT = "chat"
    SUMMARIZER = "summarizer"
    TRANSLATOR = "translator"

class RoleType(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"

class Message(BaseModel):
    role: RoleType = Field(..., description="Role of the message sender (user or assistant)")
    content: str = Field(..., description="Content of the message")

class ChatRequest(BaseModel):
    messages: Optional[List[Message]] = Field(None, description="List of chat messages")
    tool: Optional[ToolType] = Field(None, description="Name of the tool to use")
    text: Optional[str] = Field(None, description="Text input for tools")
    target_language: Optional[str] = Field(None, description="Target language for translation")

class ChatResponse(BaseModel):
    response: str = Field(..., description="Response from the chat or tool")
    tool_used: Optional[ToolType] = Field(None, description="Name of the tool that was used")
    thoughts: Optional[str] = Field(None, description="Thought process during the chat")
    response_metadata: Optional[dict] = Field(None, description="Metadata about the response")