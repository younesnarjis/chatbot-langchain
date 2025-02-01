import logging
from abc import ABC, abstractmethod
from typing import Any, Dict
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

class ToolInput(BaseModel):
    """Base class for tool inputs"""
    pass

class BaseTool(ABC):
    """Base class for all tools"""
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Return the tool name"""
        pass
    
    @property
    @abstractmethod
    def description(self) -> str:
        """Return the tool description"""
        pass

    @property
    @abstractmethod
    def input_schema(self) -> type[ToolInput]:
        """Return the input schema for the tool"""
        pass
    
    @abstractmethod
    async def run(self, **kwargs: Any) -> str:
        """Execute the tool's main functionality"""
        pass