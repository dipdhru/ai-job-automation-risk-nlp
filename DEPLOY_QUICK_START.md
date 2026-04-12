# 🚀 Railway.app Deployment - Quick Start (5 Minutes)

## Step 1: Create Railway Account (1 minute)

1. Go to **https://railway.app**
2. Click **"Start Project"** or **"Sign In"**
3. Choose **"Sign up with GitHub"**
4. Authorize Railway to access your GitHub account
5. ✅ Done!

---

## Step 2: Create New Project (2 minutes)

1. On Railway dashboard, click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Find and select: `dipdhru/ai-job-automation-risk-nlp`
4. Click **"Deploy"**
5. Railway will auto-detect Python project and start building

---

## Step 3: Create PostgreSQL Database (1 minute)

**While backend is building:**

1. In your project, click **"+ New"** or **"Add Service"**
2. Select **"Database"** → **"PostgreSQL"**
3. Name it (default is fine)
4. Click **"Create"**
5. Wait for database to finish initializing

---

## Step 4: Set Environment Variables (1 minute)

1. Click on your **backend service** in the project
2. Go to **"Variables"** tab
3. Add these variables:

```
DEBUG=False
APP_NAME=AI Job Risk Analyzer
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
CORS_ORIGINS=["https://your-domain.railway.app"]
```

### Generate SECRET_KEY

Open Terminal and run:
```bash
openssl rand -hex 32
```

Copy the output and paste as:
```
SECRET_KEY=<paste-the-long-string-here>
```

### Database URL
Railway should auto-populate `DATABASE_URL` from the PostgreSQL service. If not, click the PostgreSQL service and copy its connection string.

---

## Step 5: Configure Start Command (IMPORTANT!)

1. Click your **backend service**
2. Go to **"Settings"** tab
3. Find **"Start Command"** field
4. Replace with:

```
cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
```

5. Click **"Save"**
6. Service will restart automatically

---

## Step 6: Wait for Deployment ✅

1. Go to **"Deployments"** tab
2. Watch for green checkmark (✅ Deployed)
3. Should take 2-3 minutes
4. If it fails, check **Build Logs** for errors

---

## Step 7: Get Your Public URL 🎉

1. Click your **backend service**
2. Look for **"Public URL"** - it looks like:
```
https://ai-job-analyzer-production.railway.app
```

3. **Copy this URL** - you'll need it for Streamlit app

---

## Step 8: Test Your API

Open this in your browser:
```
https://your-url-here.railway.app/docs
```

You should see **Swagger API documentation** with all endpoints!

Try this:
```
https://your-url-here.railway.app/health
```

Should return:
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "app_name": "AI Job Risk Analyzer"
}
```

✅ **Your backend is live!**

---

## Troubleshooting

### "Build Failed"
Check the **Build Logs**:
1. Click service → **"Deployments"** 
2. Click the failed deployment
3. Scroll down to see error
4. Common issues:
   - Wrong start command
   - Missing Python version
   - Typo in environment variable

### "Application crashed"
Check **Runtime Logs**:
1. Click service → **"Logs"**
2. See what error happened
3. Usually it's missing `DATABASE_URL`

### "Cannot connect to database"
Make sure:
1. PostgreSQL service is created
2. `DATABASE_URL` is set in Variables
3. It has format: `postgresql://user:pass@host:5432/dbname`

---

## Enable Auto-Deploy (Optional)

So every `git push` automatically redeploys:

1. Click your backend service
2. Find **"Auto-Deploy"** toggle
3. Turn it ON
4. Now it auto-deploys on each GitHub push!

---

## Environment Variables Reference

If you need to add more later:

| Variable | Example | Purpose |
|----------|---------|---------|
| `DATABASE_URL` | `postgresql://...` | DB connection (auto-set) |
| `SECRET_KEY` | `abc123def456...` | JWT signing key |
| `DEBUG` | `False` | Disable debug mode |
| `CORS_ORIGINS` | `["https://..."]` | Allowed domains |

---

## Save Your URLs

Once deployed, save these:

```
API Backend: https://YOUR-URL.railway.app
API Docs: https://YOUR-URL.railway.app/docs
Health Check: https://YOUR-URL.railway.app/health
```

Use the backend URL in your Streamlit app configuration!

---

## Next Steps

After backend is deployed:

✅ Backend deployed ← You are here
→ Deploy landing page
→ Deploy Streamlit app
→ Build pitch deck
→ Practice pitch

---

## Support

**Still stuck?** 

Check these files:
- `DEPLOY_RAILWAY.md` - Full detailed guide
- `backend/README.md` - Backend documentation
- Railway docs: https://docs.railway.app

Or run this to check backend locally:
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
# Visit http://localhost:8000/docs
```
