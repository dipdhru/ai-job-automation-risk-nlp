"""Pydantic request schemas for API validation."""
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime


# ============================================================================
# Auth Schemas
# ============================================================================
class UserRegister(BaseModel):
    """User registration request."""
    email: EmailStr
    full_name: str
    password: str = Field(..., min_length=8)
    password_confirm: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "full_name": "John Doe",
                "password": "SecurePassword123",
                "password_confirm": "SecurePassword123",
            }
        }


class UserLogin(BaseModel):
    """User login request."""
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "password": "SecurePassword123",
            }
        }


class PasswordChange(BaseModel):
    """Password change request."""
    current_password: str
    new_password: str = Field(..., min_length=8)
    new_password_confirm: str


# ============================================================================
# Job Analysis Schemas
# ============================================================================
class JobAnalysisRequest(BaseModel):
    """Job analysis request payload."""
    job_title: str = Field(..., min_length=2, max_length=200)
    job_description: str = Field(..., min_length=10, max_length=5000)
    skills: List[str] = Field(default_factory=list)
    knowledge: List[str] = Field(default_factory=list)
    abilities: List[str] = Field(default_factory=list)

    class Config:
        json_schema_extra = {
            "example": {
                "job_title": "Data Scientist",
                "job_description": "Analyze large datasets and build predictive models",
                "skills": ["Programming", "Mathematics", "Statistics"],
                "knowledge": ["Computers and Electronics", "Mathematics"],
                "abilities": ["Mathematical Reasoning", "Problem Sensitivity"],
            }
        }


class JobAnalysisBatch(BaseModel):
    """Batch job analysis request (Pro/Enterprise only)."""
    jobs: List[JobAnalysisRequest]
    export_format: Optional[str] = Field("json", pattern="^(json|csv|pdf)$")


# ============================================================================
# Subscription Schemas
# ============================================================================
class SubscriptionUpgrade(BaseModel):
    """Subscription upgrade request."""
    tier: str = Field(..., pattern="^(pro|enterprise)$")
    stripe_token: Optional[str] = None


# ============================================================================
# API Key Schemas
# ============================================================================
class ApiKeyCreate(BaseModel):
    """Create API key request."""
    name: str = Field(..., min_length=1, max_length=100)


class ApiKeyRevoke(BaseModel):
    """Revoke API key request."""
    key_id: int
