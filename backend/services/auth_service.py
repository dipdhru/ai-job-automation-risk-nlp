"""Authentication service layer."""
from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.database import User, Subscription, SubscriptionTier
from auth.security import hash_password, verify_password, create_access_token
from schemas.requests import UserRegister, UserLogin


class AuthService:
    """Service for authentication operations."""

    @staticmethod
    def register_user(db: Session, user_data: UserRegister) -> User:
        """Register a new user."""
        # Check if user already exists
        existing_user = db.query(User).filter(User.email == user_data.email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

        # Validate passwords match
        if user_data.password != user_data.password_confirm:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Passwords do not match",
            )

        # Create user
        hashed_password = hash_password(user_data.password)
        user = User(
            email=user_data.email,
            full_name=user_data.full_name,
            hashed_password=hashed_password,
        )
        db.add(user)
        db.flush()  # Get the ID without committing

        # Create free subscription for new user
        subscription = Subscription(
            user_id=user.id,
            tier=SubscriptionTier.FREE,
            analyses_remaining=5,
        )
        db.add(subscription)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def authenticate_user(
        db: Session, email: str, password: str
    ) -> User | None:
        """Authenticate user by email and password."""
        user = db.query(User).filter(User.email == email).first()
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    @staticmethod
    def create_access_token_for_user(user: User) -> str:
        """Create JWT token for user."""
        access_token_expires = timedelta(
            minutes=30  # Set in settings
        )
        return create_access_token(
            data={"sub": user.id, "email": user.email},
            expires_delta=access_token_expires,
        )

    @staticmethod
    def change_password(
        db: Session, user: User, current_password: str, new_password: str
    ) -> bool:
        """Change user password."""
        if not verify_password(current_password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Current password is incorrect",
            )

        user.hashed_password = hash_password(new_password)
        db.commit()
        return True
