from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import router
import logging

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router, prefix="/api/v1")

    async def startup_event():
        logger.info("Application starting up...")

    async def shutdown_event():
        logger.info("Application shutting down...")

    app.add_event_handler("startup", startup_event)
    app.add_event_handler("shutdown", shutdown_event)

    return app