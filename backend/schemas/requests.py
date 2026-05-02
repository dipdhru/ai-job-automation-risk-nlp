"""Pydantic request schemas for API validation."""
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import List, Optional


class UserRegister(BaseModel):
    email: EmailStr
    full_name: str
    password: str = Field(..., min_length=8)
    password_confirm: str

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "email": "user@example.com",
            "full_name": "John Doe",
            "password": "SecurePassword123",
            "password_confirm": "SecurePassword123",
        }
    })


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "email": "user@example.com",
            "password": "SecurePassword123",
        }
    })


class PasswordChange(BaseModel):
    current_password: str
    new_password: str = Field(..., min_length=8)
    new_password_confirm: str


class JobAnalysisRequest(BaseModel):
    job_title: str = Field(..., min_length=2, max_length=200)
    job_description: str = Field(..., min_length=10, max_length=5000)
    skills: List[str] = Field(default_factory=list)
    knowledge: List[str] = Field(default_factory=list)
    abilities: List[str] = Field(default_factory=list)

    model_config = ConfigDict(json_schema_extra={
        "example": {
            "job_title": "Data Scientist",
            "job_description": "Analyze large datasets and build predictive models",
            "skills": ["Programming", "Mathematics", "Statistics"],
            "knowledge": ["Computers and Electronics", "Mathematics"],
            "abilities": ["Mathematical Reasoning", "Problem Sensitivity"],
        }
    })


class JobAnalysisBatch(BaseModel):
    jobs: List[JobAnalysisRequest]
    export_format: Optional[str] = Field("json", pattern="^(json|csv|pdf)$")


class SubscriptionUpgrade(BaseModel):
    tier: str = Field(..., pattern="^(pro|enterprise)$")
    stripe_token: Optional[str] = None


class ApiKeyCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)


class ApiKeyRevoke(BaseModel):
    key_id: int
