"""Pydantic response schemas for API."""
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# ============================================================================
# Auth Responses
# ============================================================================
class TokenResponse(BaseModel):
    """Token response after login."""
    access_token: str
    token_type: str = "bearer"
    expires_in: int


class UserResponse(BaseModel):
    """User profile response."""
    id: int
    email: str
    full_name: Optional[str]
    is_verified: bool
    created_at: datetime

    class Config:
        orm_mode = True


# ============================================================================
# Job Analysis Responses
# ============================================================================
class JobAnalysisResponse(BaseModel):
    """Job analysis result response."""
    id: int
    job_title: str
    job_description: str
    sector: str
    ai_proneness: float
    resistance_factors: float
    risk_level: str
    created_at: datetime
    skills: Optional[List[str]] = None
    knowledge: Optional[List[str]] = None
    abilities: Optional[List[str]] = None

    class Config:
        orm_mode = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "job_title": "Data Scientist",
                "sector": "Technology & Analytics",
                "ai_proneness": 0.65,
                "risk_level": "moderate",
                "resistance_factors": 2.5,
                "created_at": "2024-01-15T10:30:00",
                "skills": ["Programming", "Mathematics"],
            }
        }


class JobAnalysisHistoryResponse(BaseModel):
    """Paginated job analysis history."""
    total: int
    page: int
    page_size: int
    items: List[JobAnalysisResponse]


class JobAnalysisBatchResponse(BaseModel):
    """Batch analysis response."""
    results: List[JobAnalysisResponse]
    successful: int
    failed: int
    export_url: Optional[str] = None


# ============================================================================
# Subscription Responses
# ============================================================================
class SubscriptionResponse(BaseModel):
    """Subscription details."""
    tier: str
    is_active: bool
    analyses_remaining: Optional[int]
    renews_at: Optional[datetime]
    stripe_customer_id: Optional[str]

    class Config:
        orm_mode = True


# ============================================================================
# API Key Responses
# ============================================================================
class ApiKeyResponse(BaseModel):
    """API key response (key only shown on creation)."""
    id: int
    name: str
    is_active: bool
    created_at: datetime
    last_used: Optional[datetime]

    class Config:
        orm_mode = True


class ApiKeyCreateResponse(BaseModel):
    """API key creation response with secret."""
    id: int
    name: str
    key: str  # Only shown on creation
    created_at: datetime

    class Config:
        orm_mode = True


# ============================================================================
# Options/Dropdown Responses
# ============================================================================
class OptionsResponse(BaseModel):
    """Available options for skills, knowledge, abilities."""
    skills: List[str]
    knowledge: List[str]
    abilities: List[str]


# ============================================================================
# Error Responses
# ============================================================================
class ErrorResponse(BaseModel):
    """Standard error response."""
    error: str
    detail: Optional[str] = None
    status_code: int

    class Config:
        json_schema_extra = {
            "example": {
                "error": "Validation Error",
                "detail": "Job description must be at least 10 characters",
                "status_code": 422,
            }
        }
