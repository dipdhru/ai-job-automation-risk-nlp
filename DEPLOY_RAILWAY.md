# 🚀 Deploy to Railway.app (5 Minutes)

**Goal:** Get your FastAPI backend live with a production URL in under 5 minutes.

## What is Railway.app?

- **Simple**: Deploy from GitHub in 1 click
- **Free**: $5/month free tier (enough for MVP)
- **Fast**: Automatic deploys on git push
- **Professional**: Custom domains, environment variables, monitoring

## Prerequisites

✅ GitHub account (you already have this)  
✅ Railway.app account (free, takes 1 min)  
✅ Backend code pushed to GitHub (✅ just did this)  

---

## Step 1: Create Railway.app Account (1 min)

1. Go to https://railway.app
2. Click **"Start Project"**
3. **Sign up with GitHub** (easiest option)
4. Authorize Railway to access your repos
5. Done!

---

## Step 2: Create New Project (2 min)

1. On Railway dashboard, click **"New Project"**
2. Choose **"Deploy from GitHub repo"**
3. Select your repo: `dipdhru/ai-job-automation-risk-nlp`
4. Railway will auto-detect it's a Python project
5. Click **"Deploy"**

---

## Step 3: Configure Database (1 min)

Your backend needs PostgreSQL. Railway makes this simple:

1. In your new project, click **"+ New"**
2. Select **"Database"** → **"PostgreSQL"**
3. Name it: `ai-analyzer-db`
4. Click **"Create"**

Railway auto-generates the connection string. It will appear in your backend's environment variables as `DATABASE_URL`.

---

## Step 4: Set Environment Variables (1 min)

Your backend needs these secrets:

1. Click on your **backend service**
2. Go to **"Variables"** tab
3. Add these variables:

```
SECRET_KEY=generate-a-random-string-here
DATABASE_URL=postgresql://postgres:password@host:port/dbname
DEBUG=False
APP_NAME=AI Job Risk Analyzer
CORS_ORIGINS=["https://your-domain.railway.app"]
```

**For SECRET_KEY**, generate a random string:
```bash
# Run this in your terminal
openssl rand -hex 32
```

Then paste the output as your SECRET_KEY.

---

## Step 5: Configure Railway to Run Backend (Important!)

Railway auto-detects your Python app, but needs to know **where** to start:

1. Click your **backend service**
2. Go to **"Settings"** tab
3. Find **"Start Command"** 
4. Set it to:
```
cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
```

5. Click **"Save"**

---

## Step 6: Deploy & Get Your URL (1 min)

1. Railway should auto-deploy
2. Go to **"Deployments"** tab
3. Wait for green checkmark (✅ Deployed)
4. Click on your backend service
5. Look for **"Public URL"** - something like:
```
https://ai-job-analyzer-production.railway.app
```

✅ **Your backend is now live!**

---

## Step 7: Test Your API

Open this in your browser:
```
https://your-url-here.railway.app/docs
```

You should see the **Swagger API documentation** with all your endpoints!

Try these:
- `GET /health` - Should return `{"status": "healthy"}`
- `POST /api/v1/auth/register` - Test user registration

---

## Step 8: Enable Auto-Deploy from Git (Optional)

So every time you push code, Railway automatically redeploys:

1. In your service settings
2. Find **"GitHub Integration"**
3. Toggle **"Auto-deploy on push"** to ON
4. Done! Now each `git push` triggers a new deploy

---

## Troubleshooting

### "Deployment Failed"
Check the **Build Logs**:
1. Click service → **"Deployments"**
2. Click the failed deployment
3. Scroll down to see error logs
4. Common issues:
   - Wrong Python version (should be 3.11+)
   - Missing dependencies in `requirements.txt`
   - Wrong start command

### "Application Crashed"
Check the **Runtime Logs**:
1. Click service → **"Logs"**
2. See what error happened
3. Fix locally, push to git, auto-redeploy

### "DATABASE_URL not connecting"
Make sure:
- PostgreSQL service is created
- `DATABASE_URL` is set in Variables
- Looks like: `postgresql://user:pass@host:port/dbname`

---

## Next Steps

### After Deployment

1. **Test endpoints** - Use Postman or curl:
```bash
# Test health
curl https://your-url.railway.app/health

# Test registration
curl -X POST https://your-url.railway.app/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "full_name": "Test User",
    "password": "TestPassword123",
    "password_confirm": "TestPassword123"
  }'
```

2. **Save your URL** - You'll need it for:
   - Landing page
   - Streamlit frontend configuration
   - Pitch demo

3. **Add custom domain** (later):
   - Settings → Custom Domain
   - Points your domain to Railway URL
   - Great for professional pitch!

---

## URL Formats by Service

After deployment, you have:

| Service | URL |
|---------|-----|
| **Backend API** | `https://ai-job-analyzer-production.railway.app` |
| **API Docs** | `https://ai-job-analyzer-production.railway.app/docs` |
| **Health Check** | `https://ai-job-analyzer-production.railway.app/health` |

---

## Monitoring & Logs

### View Live Logs
1. Click service → **"Logs"** tab
2. See all API requests in real-time
3. Helpful for debugging

### Monitor Performance
1. Click service → **"Metrics"** tab
2. See CPU, memory, response times
3. Free tier should be plenty for MVP

---

## Cost Breakdown

| Item | Cost |
|------|------|
| Backend service | Included in $5/month |
| PostgreSQL database | Included in $5/month |
| Bandwidth (first 100GB) | Free |
| Custom domain | Free |
| **Total** | **$5/month** |

Way cheaper than Heroku ($50+/month)!

---

## What's Next?

Once your backend is deployed:

✅ **Option B**: Create landing page with signup  
✅ **Option C**: Design pitch deck  
✅ **Option D**: Polish Streamlit MVP  

Your Streamlit app will call this backend API when deployed!

---

## Commands for Later (Development)

If you need to check logs locally:

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# View logs
railway logs

# View variables
railway variables

# Pull latest environment
railway pull
```

---

## Questions?

Stuck on any step? Common issues:

- **Can't see your URL?** - Deployment still in progress (check status)
- **API returning 500 errors?** - Check Runtime Logs for details
- **Environment variables not loading?** - Restart service (Settings → Restart)

Good luck! Your backend is about to be live! 🚀
