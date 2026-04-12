"""SQLAlchemy database models."""
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from database import Base


class SubscriptionTier(str, enum.Enum):
    """Subscription tier levels."""
    FREE = "free"
    PRO = "pro"
    ENTERPRISE = "enterprise"


class User(Base):
    """User model for authentication and subscription."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    subscription = relationship("Subscription", back_populates="user", uselist=False)
    job_analyses = relationship("JobAnalysis", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User {self.email}>"


class Subscription(Base):
    """User subscription tracking."""
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    tier = Column(Enum(SubscriptionTier), default=SubscriptionTier.FREE)
    analyses_remaining = Column(Integer, default=5)  # For free tier
    stripe_customer_id = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    renews_at = Column(DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="subscription")

    def __repr__(self):
        return f"<Subscription {self.user_id} - {self.tier}>"


class JobAnalysis(Base):
    """Job analysis result history."""
    __tablename__ = "job_analyses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    job_title = Column(String, nullable=False)
    job_description = Column(Text, nullable=False)
    sector = Column(String, nullable=False)
    ai_proneness = Column(Float, nullable=False)
    resistance_factors = Column(Float, nullable=False)
    skills = Column(String, nullable=True)  # JSON string
    knowledge = Column(String, nullable=True)  # JSON string
    abilities = Column(String, nullable=True)  # JSON string
    risk_level = Column(String, nullable=False)  # 'low', 'medium', 'high'
    created_at = Column(DateTime, default=datetime.utcnow, index=True)

    # Relationships
    user = relationship("User", back_populates="job_analyses")

    def __repr__(self):
        return f"<JobAnalysis {self.id} - {self.job_title}>"


class ApiKey(Base):
    """API keys for programmatic access."""
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    key = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    last_used = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ApiKey {self.name}>"
