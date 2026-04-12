"""Job analysis service layer."""
import json
from typing import List, Dict, Any
import os
import sys
from sqlalchemy.orm import Session
from models.database import JobAnalysis, Subscription

# Add parent directory to path to import existing model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, ".."))

try:
    from app.model import analyze_single_job
    from app.options import ALL_SKILLS, ALL_KNOWLEDGE, ALL_ABILITIES
except ImportError:
    # Fallback if imports fail
    analyze_single_job = None
    ALL_SKILLS = []
    ALL_KNOWLEDGE = []
    ALL_ABILITIES = []


class JobAnalysisService:
    """Service for job analysis operations."""

    @staticmethod
    def get_options() -> Dict[str, List[str]]:
        """Get available options for skills, knowledge, abilities."""
        return {
            "skills": ALL_SKILLS,
            "knowledge": ALL_KNOWLEDGE,
            "abilities": ALL_ABILITIES,
        }

    @staticmethod
    def analyze_job(
        db: Session,
        user_id: int,
        title: str,
        description: str,
        skills: List[str],
        knowledge: List[str],
        abilities: List[str],
    ) -> JobAnalysis:
        """Analyze a single job and save results."""

        if analyze_single_job is None:
            raise RuntimeError("Model artifacts not loaded properly")

        # Check user subscription limits
        subscription = db.query(Subscription).filter(
            Subscription.user_id == user_id
        ).first()

        if subscription and subscription.tier.value == "free":
            if subscription.analyses_remaining <= 0:
                raise ValueError("Analysis limit reached. Upgrade to Pro tier.")
            subscription.analyses_remaining -= 1

        # Run analysis
        result = analyze_single_job(
            title=title,
            description=description,
            skills=skills,
            knowledge=knowledge,
            abilities=abilities,
        )

        # Determine risk level
        ai_proneness = result["AI_Proneness"]
        if ai_proneness > 0.66:
            risk_level = "high"
        elif ai_proneness > 0.33:
            risk_level = "moderate"
        else:
            risk_level = "low"

        # Save analysis to database
        job_analysis = JobAnalysis(
            user_id=user_id,
            job_title=title,
            job_description=description,
            sector=result["Sector"],
            ai_proneness=ai_proneness,
            resistance_factors=result["Resistance_Factors"],
            risk_level=risk_level,
            skills=json.dumps(skills) if skills else None,
            knowledge=json.dumps(knowledge) if knowledge else None,
            abilities=json.dumps(abilities) if abilities else None,
        )

        db.add(job_analysis)
        db.commit()
        db.refresh(job_analysis)

        return job_analysis

    @staticmethod
    def get_user_analyses(
        db: Session,
        user_id: int,
        skip: int = 0,
        limit: int = 20,
    ) -> tuple[List[JobAnalysis], int]:
        """Get paginated job analyses for a user."""

        # Get total count
        total = db.query(JobAnalysis).filter(
            JobAnalysis.user_id == user_id
        ).count()

        # Get paginated results (sorted by created_at descending)
        analyses = db.query(JobAnalysis).filter(
            JobAnalysis.user_id == user_id
        ).order_by(
            JobAnalysis.created_at.desc()
        ).offset(skip).limit(limit).all()

        return analyses, total

    @staticmethod
    def get_analysis_by_id(
        db: Session,
        user_id: int,
        analysis_id: int,
    ) -> JobAnalysis | None:
        """Get a specific job analysis."""
        return db.query(JobAnalysis).filter(
            JobAnalysis.id == analysis_id,
            JobAnalysis.user_id == user_id,
        ).first()

    @staticmethod
    def delete_analysis(
        db: Session,
        user_id: int,
        analysis_id: int,
    ) -> bool:
        """Delete a job analysis."""
        analysis = JobAnalysisService.get_analysis_by_id(
            db, user_id, analysis_id
        )
        if not analysis:
            return False

        db.delete(analysis)
        db.commit()
        return True
