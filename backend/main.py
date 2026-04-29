"""FastAPI application entry point."""
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZIPMiddleware
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
from config.settings import get_settings
from database import Base, engine
from api.routes import auth, jobs, health

LANDING_DIR = Path(__file__).parent.parent / "landing"

# Initialize database
Base.metadata.create_all(bind=engine)

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup/shutdown."""
    # Startup
    print(f"🚀 Starting {settings.APP_NAME} v{settings.APP_VERSION}")
    yield
    # Shutdown
    print(f"🛑 Shutting down {settings.APP_NAME}")


# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)

# Middleware
app.add_middleware(GZIPMiddleware, minimum_size=1000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(health.router)
app.include_router(auth.router)
app.include_router(jobs.router)

# Serve landing pages
@app.get("/", include_in_schema=False)
async def serve_index():
    return FileResponse(LANDING_DIR / "index.html")

@app.get("/signup", include_in_schema=False)
async def serve_signup():
    return FileResponse(LANDING_DIR / "signup.html")


# Error handlers
from fastapi import HTTPException
from fastapi.responses import JSONResponse


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions."""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status_code": exc.status_code,
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
    )
