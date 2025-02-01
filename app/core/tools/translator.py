import logging
from pydantic import BaseModel, Field
from .base import BaseTool, ToolInput
from langchain_groq import ChatGroq

logger = logging.getLogger(__name__)

class TranslatorInput(ToolInput):
    """Input schema for translator tool"""
    text: str = Field(..., description="Text to translate")
    target_language: str = Field(..., description="Target language for translation")

class Translator(BaseTool):
    def __init__(self, **kwargs):
        self.llm = ChatGroq(**kwargs)

    @property
    def name(self) -> str:
        return "translator"

    @property
    def description(self) -> str:
        return "Translate the provided text into another language"

    @property
    def input_schema(self) -> type[ToolInput]:
        return TranslatorInput

    async def run(self, **kwargs) -> str:
        validated_input = TranslatorInput(**kwargs)
        prompt = f"Translate the following text to {validated_input.target_language}:\n\n{validated_input.text}"
        return await self.llm.ainvoke(prompt)