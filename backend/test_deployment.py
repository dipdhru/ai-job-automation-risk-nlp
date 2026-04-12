#!/usr/bin/env python3
"""
Test script to verify backend is ready for deployment.
Run this locally before deploying to Railway.app
"""

import sys
import os

def test_imports():
    """Test that all dependencies can be imported."""
    print("🔍 Testing imports...")
    try:
        import fastapi
        print("  ✅ fastapi")
        import sqlalchemy
        print("  ✅ sqlalchemy")
        import pydantic
        print("  ✅ pydantic")
        import jwt
        print("  ✅ jwt")
        import passlib
        print("  ✅ passlib")
        print("✅ All imports successful!\n")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}\n")
        print("Run: pip install -r requirements.txt")
        return False


def test_config():
    """Test configuration loading."""
    print("🔍 Testing configuration...")
    try:
        from config.settings import get_settings
        settings = get_settings()
        print(f"  ✅ App Name: {settings.APP_NAME}")
        print(f"  ✅ App Version: {settings.APP_VERSION}")
        print(f"  ✅ Debug: {settings.DEBUG}")
        print("✅ Configuration loaded!\n")
        return True
    except Exception as e:
        print(f"❌ Config error: {e}\n")
        return False


def test_models():
    """Test database models."""
    print("🔍 Testing database models...")
    try:
        from models.database import User, Subscription, JobAnalysis, ApiKey
        print("  ✅ User model")
        print("  ✅ Subscription model")
        print("  ✅ JobAnalysis model")
        print("  ✅ ApiKey model")
        print("✅ All models imported!\n")
        return True
    except Exception as e:
        print(f"❌ Model error: {e}\n")
        return False


def test_schemas():
    """Test Pydantic schemas."""
    print("🔍 Testing schemas...")
    try:
        from schemas.requests import UserRegister, UserLogin, JobAnalysisRequest
        from schemas.responses import UserResponse, JobAnalysisResponse
        print("  ✅ Request schemas")
        print("  ✅ Response schemas")
        print("✅ All schemas valid!\n")
        return True
    except Exception as e:
        print(f"❌ Schema error: {e}\n")
        return False


def test_security():
    """Test security functions."""
    print("🔍 Testing security functions...")
    try:
        from auth.security import hash_password, verify_password, create_access_token, decode_token

        # Test password hashing
        password = "TestPassword123"
        hashed = hash_password(password)
        assert verify_password(password, hashed), "Password verification failed"
        print("  ✅ Password hashing")

        # Test JWT token
        token = create_access_token({"sub": 1, "email": "test@example.com"})
        payload = decode_token(token)
        assert payload is not None, "Token decoding failed"
        assert payload.get("sub") == 1, "Token payload incorrect"
        print("  ✅ JWT token generation and decoding")

        print("✅ Security functions working!\n")
        return True
    except Exception as e:
        print(f"❌ Security error: {e}\n")
        return False


def test_services():
    """Test service imports."""
    print("🔍 Testing services...")
    try:
        from services.auth_service import AuthService
        from services.job_analysis_service import JobAnalysisService
        print("  ✅ AuthService")
        print("  ✅ JobAnalysisService")
        print("✅ Services imported!\n")
        return True
    except Exception as e:
        print(f"❌ Service error: {e}\n")
        return False


def test_fastapi_app():
    """Test FastAPI app creation."""
    print("🔍 Testing FastAPI app...")
    try:
        from main import app
        print("  ✅ FastAPI app created")
        print(f"  ✅ App title: {app.title}")
        print(f"  ✅ App version: {app.version}")
        print(f"  ✅ Routes registered: {len(app.routes)}")
        print("✅ FastAPI app ready!\n")
        return True
    except Exception as e:
        print(f"❌ FastAPI error: {e}\n")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("🚀 BACKEND DEPLOYMENT READINESS TEST")
    print("=" * 60)
    print()

    tests = [
        ("Imports", test_imports),
        ("Configuration", test_config),
        ("Models", test_models),
        ("Schemas", test_schemas),
        ("Security", test_security),
        ("Services", test_services),
        ("FastAPI App", test_fastapi_app),
    ]

    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ {name} test failed with error: {e}\n")
            results.append((name, False))

    print("=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {name}")

    print()
    print(f"Score: {passed}/{total} tests passed")
    print()

    if passed == total:
        print("🎉 BACKEND IS READY FOR DEPLOYMENT!")
        print()
        print("Next steps:")
        print("1. Go to https://railway.app")
        print("2. Follow DEPLOY_QUICK_START.md")
        print("3. Your backend will be live in ~5 minutes!")
        return 0
    else:
        print("❌ BACKEND HAS ISSUES - FIX BEFORE DEPLOYING")
        print()
        print("Common fixes:")
        print("- Run: pip install -r requirements.txt")
        print("- Check .env file exists (copy from .env.example)")
        print("- Verify Python 3.11+ installed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
