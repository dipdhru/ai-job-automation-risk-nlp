"""Pydantic response schemas for API."""
from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    full_name: Optional[str]
    is_verified: bool
    created_at: datetime


class JobAnalysisResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True, json_schema_extra={
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
    })

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


class JobAnalysisHistoryResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: List[JobAnalysisResponse]


class JobAnalysisBatchResponse(BaseModel):
    results: List[JobAnalysisResponse]
    successful: int
    failed: int
    export_url: Optional[str] = None


class SubscriptionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    tier: str
    is_active: bool
    analyses_remaining: Optional[int]
    renews_at: Optional[datetime]
    stripe_customer_id: Optional[str]


class ApiKeyResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    is_active: bool
    created_at: datetime
    last_used: Optional[datetime]


class ApiKeyCreateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    key: str
    created_at: datetime


class OptionsResponse(BaseModel):
    skills: List[str]
    knowledge: List[str]
    abilities: List[str]


class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None
    status_code: int
