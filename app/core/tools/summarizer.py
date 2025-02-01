import logging
from pydantic import BaseModel, Field
from .base import BaseTool, ToolInput
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document

logger = logging.getLogger(__name__)

class SummarizerInput(ToolInput):
    """Input schema for summarizer tool"""
    text: str = Field(..., description="Text to summarize")

class TextSummarizer(BaseTool):
    def __init__(self, **kwargs):
        self.llm = ChatGroq(**kwargs)

    @property
    def name(self) -> str:
        return "summarizer"

    @property
    def description(self) -> str:
        return "Summarize the provided text into a concise version"

    @property
    def input_schema(self) -> type[ToolInput]:
        return SummarizerInput

    async def run(self, **kwargs) -> str:
        validated_input = SummarizerInput(**kwargs)
        docs = [Document(page_content=validated_input.text)]
        chain = load_summarize_chain(self.llm, chain_type="stuff")
        return await chain.arun(docs)