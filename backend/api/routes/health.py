"""Health check and utility routes."""
from fastapi import APIRouter
from config.settings import get_settings

router = APIRouter(tags=["health"])

settings = get_settings()


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "version": settings.APP_VERSION,
        "app_name": settings.APP_NAME,
    }
