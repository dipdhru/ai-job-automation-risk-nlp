# AI Job Risk Analyzer - FastAPI Backend

Production-ready backend for the AI Job Risk Analyzer application built with FastAPI, PostgreSQL, and JWT authentication.

## Features

✅ **Authentication** - User registration, login, JWT tokens  
✅ **Job Analysis** - AI automation risk assessment API  
✅ **User History** - Persistent job analysis storage  
✅ **Subscription Management** - Free/Pro/Enterprise tiers  
✅ **API Keys** - Programmatic access for integrations  
✅ **Database** - PostgreSQL with SQLAlchemy ORM  
✅ **Docker Ready** - Containerized deployment  
✅ **Production Safe** - Environment-based configuration, CORS, security headers  

## Quick Start

### Prerequisites
- Python 3.11+
- PostgreSQL 13+
- Docker & Docker Compose (optional)

### Local Development

1. **Clone & Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Configure Environment**
```bash
cp .env.example .env
# Edit .env with your database credentials
```

3. **Initialize Database**
```bash
# If using PostgreSQL locally:
createdb ai_risk_analyzer
```

4. **Run Server**
```bash
uvicorn main:app --reload --port 8000
```

Visit: http://localhost:8000/docs (interactive API docs)

### With Docker Compose

```bash
# From project root
docker-compose up -d

# Backend runs on http://localhost:8000
# PostgreSQL on localhost:5432
# Streamlit Frontend on http://localhost:8501
```

## API Documentation

### Authentication Endpoints

#### Register
```http
POST /api/v1/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "full_name": "John Doe",
  "password": "SecurePassword123",
  "password_confirm": "SecurePassword123"
}
```

#### Login
```http
POST /api/v1/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "SecurePassword123"
}

Response:
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

### Job Analysis Endpoints

#### Get Options
```http
GET /api/v1/jobs/options

Response:
{
  "skills": ["Programming", "Mathematics", ...],
  "knowledge": ["Computers and Electronics", ...],
  "abilities": ["Mathematical Reasoning", ...]
}
```

#### Analyze Job
```http
POST /api/v1/jobs/analyze
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "job_title": "Data Scientist",
  "job_description": "Analyze datasets and build predictive models...",
  "skills": ["Programming", "Mathematics"],
  "knowledge": ["Computers and Electronics"],
  "abilities": ["Mathematical Reasoning"]
}

Response:
{
  "id": 1,
  "job_title": "Data Scientist",
  "sector": "Technology & Analytics",
  "ai_proneness": 0.65,
  "risk_level": "moderate",
  "resistance_factors": 2.5,
  "created_at": "2024-01-15T10:30:00"
}
```

#### Get Analysis History
```http
GET /api/v1/jobs/history?skip=0&limit=20
Authorization: Bearer {access_token}

Response:
{
  "total": 42,
  "page": 1,
  "page_size": 20,
  "items": [...]
}
```

#### Get Single Analysis
```http
GET /api/v1/jobs/{analysis_id}
Authorization: Bearer {access_token}
```

#### Delete Analysis
```http
DELETE /api/v1/jobs/{analysis_id}
Authorization: Bearer {access_token}
```

## Project Structure

```
backend/
├── main.py                 # FastAPI app entry point
├── database.py             # SQLAlchemy setup
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container image
├── .env.example            # Environment template
├── config/
│   └── settings.py         # Configuration
├── models/
│   └── database.py         # SQLAlchemy models
├── schemas/
│   ├── requests.py         # Request validators
│   └── responses.py        # Response schemas
├── services/
│   ├── auth_service.py     # Authentication logic
│   └── job_analysis_service.py  # Analysis logic
├── auth/
│   ├── security.py         # Password & JWT
│   └── dependencies.py     # Route dependencies
└── api/
    └── routes/
        ├── auth.py         # Auth endpoints
        ├── jobs.py         # Analysis endpoints
        └── health.py       # Health checks
```

## Environment Variables

```bash
# Application
APP_NAME=AI Job Risk Analyzer
APP_VERSION=1.0.0
DEBUG=False

# Database (PostgreSQL)
DATABASE_URL=postgresql://user:password@localhost:5432/ai_risk_analyzer

# JWT Secrets
SECRET_KEY=your-super-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Stripe (optional)
STRIPE_API_KEY=sk_test_xxx
STRIPE_WEBHOOK_SECRET=whsec_test_xxx

# CORS
CORS_ORIGINS=["http://localhost:3000","http://localhost:8501"]
```

## Database Migrations

Using Alembic for migrations:

```bash
# Create migration
alembic revision --autogenerate -m "Add new table"

# Apply migrations
alembic upgrade head

# Revert
alembic downgrade -1
```

## Testing

```bash
# Run all tests
pytest

# With coverage
pytest --cov=.

# Specific test file
pytest tests/api/test_jobs.py -v
```

## Deployment

### Railway.app
```bash
railway link
railway up
```

### DigitalOcean App Platform
1. Connect GitHub repo
2. Configure environment variables
3. Deploy

### AWS/GCP/Azure
Use their respective container deployment services with the Dockerfile.

## Performance Tips

- Use connection pooling (configured in database.py)
- Enable GZIP compression (middleware)
- Cache options response (rarely changes)
- Paginate history queries (default 20 items)
- Consider Redis for session caching

## Security Best Practices

✅ JWT tokens with 30-min expiry  
✅ Bcrypt password hashing  
✅ CORS configured  
✅ SQL injection prevention (ORM)  
✅ Rate limiting (can be added)  
✅ Environment-based secrets  
✅ Non-root Docker user  

## Monitoring & Logging

To add:
- Sentry for error tracking
- Structlog for structured logging
- Prometheus for metrics
- ELK stack for log aggregation

## Support

For issues, see main project README or create a GitHub issue.
