# 🚀 Deploy to Railway.app - Complete Step-by-Step

**Status:** ✅ Your backend code is 100% ready  
**Time needed:** 5-10 minutes  
**Result:** Live API running on Railway.app  

---

## ✅ What's Verified

Your backend has:
- ✅ All Python files correct
- ✅ Dockerfile ready
- ✅ requirements.txt with all dependencies
- ✅ Environment template (.env.example)
- ✅ Main entry point (main.py)
- ✅ Syntax validated

**You can deploy immediately!**

---

## 🎯 Deployment Walkthrough

### **STEP 1: Create Railway Account**

1. Open your browser and go to **https://railway.app**
2. Click **"Start Project"** button
3. Choose **"Sign up with GitHub"** (easiest)
4. When it asks to authorize, click **"Authorize"**
5. ✅ You're now logged in!

**Takes 2 minutes**

---

### **STEP 2: Create New Project**

1. On Railway dashboard, click **"New Project"** (or "Create Project")
2. Choose **"Deploy from GitHub repo"**
3. Find your repository: **`dipdhru/ai-job-automation-risk-nlp`**
4. Click on it to select
5. Click **"Deploy"** button

**Railway will automatically:**
- Detect it's a Python project
- Start building from your GitHub code
- Takes 1-2 minutes

**Watch the build progress** in the "Deployments" tab

---

### **STEP 3: Create PostgreSQL Database**

While your backend is building:

1. In your project view, click **"+ New"** or **"Add Service"**
2. Scroll down and select **"PostgreSQL"**
3. Database will be created automatically
4. ✅ You'll see it listed in your services

**Takes 1 minute**

---

### **STEP 4: Configure Environment Variables**

1. Click on your **"backend"** service (the Python one)
2. Go to the **"Variables"** tab (middle tab)
3. You should see `DATABASE_URL` already filled in (from PostgreSQL)
4. Click **"+ New Variable"** to add each of these:

**Copy & paste these variables:**

```
DEBUG
False

APP_NAME
AI Job Risk Analyzer

ALGORITHM
HS256

ACCESS_TOKEN_EXPIRE_MINUTES
30

CORS_ORIGINS
["https://your-app.railway.app"]
```

**For SECRET_KEY** (the important one):

1. Open Terminal on your computer
2. Run this command:
```bash
openssl rand -hex 32
```
3. Copy the output (long random string)
4. In Railway, add variable:
```
SECRET_KEY
<paste-your-random-string-here>
```

**Takes 2-3 minutes**

---

### **STEP 5: Set Start Command (CRITICAL!)**

This tells Railway how to start your backend:

1. Click your **"backend"** service
2. Go to **"Settings"** tab (right side)
3. Find **"Start Command"** field
4. Clear it and paste:

```
cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
```

5. Click **"Save"** or press Enter
6. Service will restart automatically

**Takes 1 minute**

---

### **STEP 6: Wait for Green Checkmark**

1. Go to **"Deployments"** tab
2. Watch for deployment status
3. Should show: ✅ **"Deployed"** (green checkmark)
4. If red ❌, click it and check **"Build Logs"** for error

**Takes 2-3 minutes**

---

### **STEP 7: Get Your Public URL**

Once deployment is ✅ successful:

1. Click your **"backend"** service
2. Look for **"Public URL"** (usually at the top)
3. It looks like: `https://something-something.railway.app`

**Copy this URL - you'll need it!**

---

### **STEP 8: Test Your API**

1. Take your URL from Step 7
2. Open in browser: `https://your-url.railway.app/docs`
3. You should see **Swagger API documentation** 🎉

**Try this endpoint to verify:**
```
https://your-url.railway.app/health
```

Should return:
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "app_name": "AI Job Risk Analyzer"
}
```

✅ **If you see this, your backend is LIVE!**

---

## 🚨 Troubleshooting

### Build Failed?
1. Click **"Deployments"** tab
2. Click the failed deployment
3. Scroll down to **"Build Logs"**
4. Look for error message
5. Common issues:
   - Typo in start command
   - Wrong environment variable
   - Missing `requirements.txt`

### API Returns Error?
1. Check **"Logs"** tab in Railway
2. Should show what's wrong
3. Most common: Missing `DATABASE_URL` variable

### Can't Connect to API?
1. Verify your URL is correct (no typos)
2. Wait 1-2 minutes (might still be deploying)
3. Restart the service: Settings → "Restart"

---

## 💾 Save These URLs

After successful deployment, save:

```
API Backend URL:
https://your-app.railway.app

API Documentation:
https://your-app.railway.app/docs

Health Check:
https://your-app.railway.app/health
```

**You'll need these for:**
- Streamlit app configuration
- Pitch demo
- Landing page integration

---

## 🔄 Enable Auto-Deploy (Optional)

So every time you push to GitHub, it auto-deploys:

1. Click your **backend** service
2. Go to **"Settings"**
3. Find **"Auto-Deploy"** and toggle it ON
4. Now each `git push` → automatic deploy!

---

## 📊 Your Service Status

After deployment, you can check anytime:

1. Click your **backend** service
2. **"Logs"** - See API requests in real-time
3. **"Metrics"** - CPU, Memory, Response time
4. **"Deployments"** - See deployment history
5. **"Settings"** - Modify configuration

---

## ✅ Success Checklist

- [ ] Railway.app account created
- [ ] GitHub repo connected
- [ ] Backend service deployed (✅ green checkmark)
- [ ] PostgreSQL database created
- [ ] Environment variables set
- [ ] Start command configured
- [ ] API docs accessible (`/docs`)
- [ ] Health check returns 200
- [ ] URL saved for later use

---

## 🎉 You're Done!

Your backend is now **live on the internet**!

### Next:
1. Update Streamlit app with this URL
2. Deploy landing page
3. Deploy Streamlit demo
4. You have a complete MVP! 🚀

---

## 📞 Need Help?

**Backend won't deploy?**
- Check Railway build logs
- Verify start command is exactly: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
- Make sure all environment variables are set

**API returns 500 error?**
- Check "Logs" tab in Railway
- Usually missing DATABASE_URL
- Add it from PostgreSQL service

**Can't find your URL?**
- Click backend service
- Should be shown at the top
- Format: `https://something.railway.app`

---

## 🚀 Timeline

- Create account: 2 min
- Deploy backend: 2-3 min
- Create database: 1 min
- Set variables: 2 min
- Test API: 1 min
- **Total: ~10 minutes**

Good luck! Your backend will be live in minutes. 🎉
