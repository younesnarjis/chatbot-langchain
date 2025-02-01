import logging
from app.config.settings import settings
from app.core.chat_manager import ChatManager

logger = logging.getLogger(__name__)

chat_manager = ChatManager(
    api_key=settings.GROQ_API_KEY,
    model_name=settings.GROQ_MODEL_NAME,
    temperature=0.5,
    max_tokens=1000
)