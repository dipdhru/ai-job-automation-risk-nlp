# 🚀 Deploy to Render.com - Complete Guide

**Status:** 100% Free, No Credit Card Required  
**Time:** 5-10 minutes  
**Result:** Live API at `https://your-app.onrender.com`

---

## ✅ Why Render.com?

- 🆓 Completely free tier
- 💳 No credit card required
- ⚡ Simple 1-click deployment
- 🔗 Works with GitHub directly
- 📊 Professional URL
- 🎯 Perfect for MVP/demo

---

## 📋 Step-by-Step Deployment

### **STEP 1: Go to Render.com**

1. Open browser: **https://render.com**
2. Click **"Sign Up"** button
3. Choose **"Continue with GitHub"**
4. Authorize Render to access your GitHub account
5. ✅ Account created!

**Takes: 2 minutes**

---

### **STEP 2: Create Web Service**

1. On Render dashboard, click **"New +"** button (top right)
2. Select **"Web Service"**
3. A page appears asking to select a repository
4. Find and select: **`dipdhru/ai-job-automation-risk-nlp`**
5. Click **"Connect"**

**Takes: 1 minute**

---

### **STEP 3: Configure Deployment**

Now fill in the form with these exact values:

#### Name
```
ai-job-analyzer
```
(This becomes part of your URL)

#### Root Directory
```
./
```
(Leave as is - current directory)

#### Environment
```
Python 3
```
(Should be auto-detected)

#### Build Command
```
pip install -r backend/requirements.txt
```

#### Start Command
```
cd backend && uvicorn main:app --host 0.0.0.0 --port 8000
```

**IMPORTANT:** This is exactly how to start FastAPI on Render

#### Instance Type
**Select: "Free"** (bottom option)

This is the crucial step - make sure you click "Free" tier!

#### Environment Variables

Click **"Add Environment Variable"** for each:

```
Name: DEBUG
Value: False
```

```
Name: APP_NAME
Value: AI Job Risk Analyzer
```

```
Name: ALGORITHM
Value: HS256
```

```
Name: ACCESS_TOKEN_EXPIRE_MINUTES
Value: 30
```

```
Name: CORS_ORIGINS
Value: ["https://ai-job-analyzer.onrender.com"]
```

#### Generate SECRET_KEY

Open Terminal and run:
```bash
openssl rand -hex 32
```

Copy the output, then add:
```
Name: SECRET_KEY
Value: <paste-your-random-string>
```

#### DATABASE_URL

**For MVP testing**, use SQLite (no setup needed):
```
Name: DATABASE_URL
Value: sqlite:///./test.db
```

Or if you want PostgreSQL (requires setup):
- Render offers free PostgreSQL
- But SQLite is simpler for MVP

**Recommendation:** Use SQLite for now ✓

---

### **STEP 4: Deploy!**

1. Scroll down to bottom
2. Click **"Create Web Service"** button
3. Render will:
   - Clone your GitHub repo
   - Install dependencies (pip install)
   - Start your FastAPI app
   - Takes 3-5 minutes

**Watch the logs** in the "Logs" tab for progress

---

### **STEP 5: Wait for "Live"**

1. You'll see deployment progress in real-time
2. Wait for message: **"Your service is live!"**
3. Status should show: ✅ **"Live"** (green)

**If you see red ❌:** Check the logs for error (usually a typo)

---

### **STEP 6: Get Your Public URL**

Once deployment is complete:

1. At the top of the page, you'll see:
```
https://ai-job-analyzer.onrender.com
```

2. **Copy this URL** - this is your live backend!

---

### **STEP 7: Test Your API**

1. Open in browser:
```
https://ai-job-analyzer.onrender.com/docs
```

You should see **Swagger API documentation** 🎉

2. Test the health endpoint:
```
https://ai-job-analyzer.onrender.com/health
```

Should return:
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "app_name": "AI Job Risk Analyzer"
}
```

✅ **Your backend is LIVE!**

---

## ⚙️ Common Issues & Fixes

### "Build failed"
**Solution:**
1. Click on the service
2. Go to **"Logs"** tab
3. Look for the error message
4. Common: Typo in start command or build command
5. Edit and redeploy

### "Application crashed"
**Solution:**
1. Check start command: `cd backend && uvicorn main:app --host 0.0.0.0 --port 8000`
2. Make sure all environment variables are set
3. Restart service in settings

### "Service spins down after 15 minutes"
**This is normal on free tier!**
- Free tier goes to sleep after 15 min of inactivity
- When you visit again, it wakes up (takes ~10 seconds)
- **For your event:** Visit the URL 5 min before demo to wake it up

### "Port already in use"
**Solution:**
- Don't use a fixed port, Render assigns it
- Start command should use: `--port 8000` (Render will map it)

---

## 🔄 Redeploying After Code Changes

After you push new code to GitHub:

1. Go to Render dashboard
2. Click your service
3. Click **"Manual Deploy"** → **"Deploy latest commit"**
4. OR enable auto-deploy in settings

---

## 📊 Monitoring Your Service

After deployment, you can:

1. **View Logs** - See all requests in real-time
2. **Check Metrics** - CPU, Memory usage
3. **Update Settings** - Change environment variables
4. **Restart** - Restart the service

All available in the dashboard

---

## 💰 Cost Breakdown

**Forever FREE:**
- ✅ 1 free web service
- ✅ Free tier sleeps after 15 min (fine for MVP)
- ✅ Full FastAPI support
- ✅ Custom domain support (later)

**When you grow:**
- Starter tier: $7/month (no sleep)
- Upgrade anytime

---

## 🎯 Your Service URLs

After deployment:

| Purpose | URL |
|---------|-----|
| **API Backend** | `https://ai-job-analyzer.onrender.com` |
| **API Docs** | `https://ai-job-analyzer.onrender.com/docs` |
| **Health Check** | `https://ai-job-analyzer.onrender.com/health` |

**Save these!** You'll need them for Streamlit and your pitch.

---

## ✅ Deployment Checklist

- [ ] Account created at render.com
- [ ] GitHub connected
- [ ] Web Service created
- [ ] Build command set: `pip install -r backend/requirements.txt`
- [ ] Start command set: `cd backend && uvicorn main:app --host 0.0.0.0 --port 8000`
- [ ] Environment variables added
- [ ] Free tier selected
- [ ] Deployment started
- [ ] Status shows "Live" (green)
- [ ] `/docs` endpoint works
- [ ] `/health` endpoint returns 200

---

## 🚀 Timeline

- Sign up & connect GitHub: 2 min
- Configure deployment: 3 min
- Deploy & wait: 5 min
- Test API: 2 min
- **Total: ~12 minutes**

---

## 📞 Next Steps

After backend is deployed:

1. ✅ Backend on Render (you're doing this!)
2. → Deploy landing page
3. → Deploy Streamlit app
4. → Build pitch deck
5. → Practice pitch

Your API URL will be used in all of these! 🎉

---

## 💡 Pro Tips

**Before Your Event:**
- Visit your API URL 5 minutes before demo (wakes it up)
- Have the `/docs` page bookmarked
- Screenshot of `/health` response as backup

**For Production (Later):**
- Add PostgreSQL database
- Upgrade to Starter tier ($7/month, no sleep)
- Set up custom domain

---

## Questions?

**"How do I update the code?"**
- Push to GitHub → Click "Manual Deploy" in Render

**"Can I see the logs?"**
- Yes! Click service → "Logs" tab

**"How do I rollback if something breaks?"**
- Render keeps deployment history
- Click a previous deployment to revert

**"Is it really free?"**
- Yes! Completely free tier with no credit card

---

## 🎉 You're Ready!

Your backend will be live in ~10 minutes at:
```
https://ai-job-analyzer.onrender.com
```

This is completely free and requires no credit card.

Perfect for your MVP demo! 🚀
