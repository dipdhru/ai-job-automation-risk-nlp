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


@router.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
        "docs": "/docs",
    }
