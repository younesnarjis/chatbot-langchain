import pytest
from langchain.schema import AIMessage
from app.core.dependencies import chat_manager
from app.config.settings import settings

@pytest.mark.asyncio
async def test_chat_manager_basic_response():
    messages = [{"role": "user", "content": "Hello"}]
    response = await chat_manager.process_message(messages)
    assert response is not None
    assert isinstance(response, AIMessage)

@pytest.mark.asyncio
async def test_chat_manager_with_translator_tool():
    response = await chat_manager.process_message(
        tool="translator",
        text="Hello world",
        target_language="Spanish"
    )
    assert response is not None
    assert isinstance(response, AIMessage)

@pytest.mark.asyncio
async def test_chat_manager_with_summarizer_tool():
    response = await chat_manager.process_message(
        tool="summarizer",
        text="This is a sample text for summarization."
    )
    assert response is not None
    assert isinstance(response, str)