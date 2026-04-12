"""Authentication routes."""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.requests import UserRegister, UserLogin, PasswordChange
from schemas.responses import UserResponse, TokenResponse
from services.auth_service import AuthService
from models.database import User
from auth.dependencies import get_current_user

router = APIRouter(prefix="/api/v1/auth", tags=["authentication"])


@router.post("/register", response_model=UserResponse, status_code=201)
async def register(
    user_data: UserRegister,
    db: Session = Depends(get_db),
):
    """Register a new user account."""
    user = AuthService.register_user(db, user_data)
    return user


@router.post("/login", response_model=TokenResponse)
async def login(
    credentials: UserLogin,
    db: Session = Depends(get_db),
):
    """Login and get access token."""
    user = AuthService.authenticate_user(
        db,
        email=credentials.email,
        password=credentials.password,
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = AuthService.create_access_token_for_user(user)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": 30 * 60,  # 30 minutes in seconds
    }


@router.get("/me", response_model=UserResponse)
async def get_current_user_profile(
    current_user: User = Depends(get_current_user),
):
    """Get current user profile."""
    return current_user


@router.post("/password-change")
async def change_password(
    password_data: PasswordChange,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Change user password."""
    AuthService.change_password(
        db,
        current_user,
        password_data.current_password,
        password_data.new_password,
    )
    return {"message": "Password changed successfully"}
