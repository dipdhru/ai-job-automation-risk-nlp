"""FastAPI application entry point."""
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
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
app.add_middleware(GZipMiddleware, minimum_size=1000)
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

# Public analyze endpoint (no auth)
from pydantic import BaseModel as _Base

class _PublicAnalyzeRequest(_Base):
    job_title: str
    job_description: str

@app.post("/api/v1/analyze")
async def public_analyze(body: _PublicAnalyzeRequest):
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    try:
        from app.model import analyze_single_job
        result = analyze_single_job(
            title=body.job_title,
            description=body.job_description,
        )
        return {
            "sector": result["Sector"],
            "ai_proneness": result["AI_Proneness"],
            "risk_level": (
                "high" if result["AI_Proneness"] > 0.66 else
                "moderate" if result["AI_Proneness"] > 0.33 else "low"
            ),
            "resistance_factors": result["Resistance_Factors"],
        }
    except Exception as e:
        from fastapi import HTTPException
        raise HTTPException(status_code=500, detail=str(e))

# Serve landing pages
@app.get("/", include_in_schema=False)
async def serve_index():
    return FileResponse(LANDING_DIR / "index.html")

@app.get("/signup", include_in_schema=False)
async def serve_signup():
    return FileResponse(LANDING_DIR / "signup.html")

@app.get("/dashboard", include_in_schema=False)
async def serve_dashboard():
    return FileResponse(LANDING_DIR / "dashboard.html")

@app.get("/login", include_in_schema=False)
async def serve_login():
    return FileResponse(LANDING_DIR / "login.html")

@app.get("/analyzer", include_in_schema=False)
async def serve_analyzer():
    return FileResponse(LANDING_DIR / "analyzer.html")


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
