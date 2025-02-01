import logging
from langchain.schema import AIMessage
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.api.models import ChatRequest, ChatResponse
from app.core.dependencies import chat_manager

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/")
async def health_check():
    """Health check endpoint"""
    return JSONResponse(content={"health_check": "OK"}, status_code=200)

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Process chat message with optional tool usage"""
    try:
        messages = [msg.dict() for msg in request.messages] if request.messages else None
        response = await chat_manager.process_message(
            messages=messages,
            tool=request.tool,
            text=request.text,
            target_language=request.target_language
        )

        content = response.content if isinstance(response, AIMessage) else response

        thoughts = None
        if "<think>" in content and "</think>" in content:
            start = content.find("<think>") + len("<think>")
            end = content.find("</think>")
            thoughts = content[start:end].strip()
            content = content[:content.find("<think>")] + content[content.find("</think>") + len("</think>"):]

        return ChatResponse(
            response=content.lstrip('\n'),
            thoughts=thoughts,
            tool_used=request.tool if request.tool else "chat",
            response_metadata=response.response_metadata if isinstance(response, AIMessage) else None
        )
    except Exception as e:
        logger.error(f"Error processing chat request: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))