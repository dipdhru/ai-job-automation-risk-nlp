"""Job analysis routes."""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from database import get_db
from schemas.requests import JobAnalysisRequest
from schemas.responses import (
    JobAnalysisResponse,
    JobAnalysisHistoryResponse,
    OptionsResponse,
)
from services.job_analysis_service import JobAnalysisService
from models.database import User
from auth.dependencies import get_current_user

router = APIRouter(prefix="/api/v1/jobs", tags=["job-analysis"])


@router.get("/options", response_model=OptionsResponse)
async def get_analysis_options():
    """Get available skills, knowledge, and abilities options."""
    options = JobAnalysisService.get_options()
    return OptionsResponse(**options)


@router.post("/analyze", response_model=JobAnalysisResponse, status_code=201)
async def analyze_job(
    job_data: JobAnalysisRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Analyze a job for AI automation risk."""
    try:
        analysis = JobAnalysisService.analyze_job(
            db=db,
            user_id=current_user.id,
            title=job_data.job_title,
            description=job_data.job_description,
            skills=job_data.skills,
            knowledge=job_data.knowledge,
            abilities=job_data.abilities,
        )
        return analysis
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=str(e),
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Analysis failed. Please try again.",
        )


@router.get("/history", response_model=JobAnalysisHistoryResponse)
async def get_analysis_history(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get user's job analysis history with pagination."""
    analyses, total = JobAnalysisService.get_user_analyses(
        db=db,
        user_id=current_user.id,
        skip=skip,
        limit=limit,
    )

    return JobAnalysisHistoryResponse(
        total=total,
        page=skip // limit + 1,
        page_size=limit,
        items=analyses,
    )


@router.get("/{analysis_id}", response_model=JobAnalysisResponse)
async def get_analysis(
    analysis_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get a specific job analysis."""
    analysis = JobAnalysisService.get_analysis_by_id(
        db=db,
        user_id=current_user.id,
        analysis_id=analysis_id,
    )

    if not analysis:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Analysis not found",
        )

    return analysis


@router.delete("/{analysis_id}", status_code=204)
async def delete_analysis(
    analysis_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Delete a job analysis."""
    deleted = JobAnalysisService.delete_analysis(
        db=db,
        user_id=current_user.id,
        analysis_id=analysis_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Analysis not found",
        )

    return None
