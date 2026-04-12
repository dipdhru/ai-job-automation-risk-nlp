# 🚀 Deploy Streamlit App - Complete Guide

**Status:** 100% Free, No Credit Card Required  
**Time:** 10 minutes  
**Result:** Live interactive demo at `https://your-app.streamlit.app`

---

## ✅ What You'll Get

- 🔐 Login page
- 📝 Signup page
- 📊 Job analysis demo
- 📜 User history tracking
- 🎨 Professional UI
- 📱 Mobile responsive

---

## 🎯 Step-by-Step Deployment

### **STEP 1: Prepare Streamlit Configuration**

We need to create a `.streamlit/config.toml` file to configure the app:

**Create file:** `app/.streamlit/config.toml`

Add this content:

```toml
[theme]
primaryColor = "#667eea"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f8f9fa"
textColor = "#333333"
font = "sans serif"

[client]
showErrorDetails = false
toolbarMode = "viewer"

[server]
port = 8501
headless = true
runOnSave = true
```

---

### **STEP 2: Update Streamlit App Configuration**

Edit: `app/app_production.py`

Find this line (around line 40):
```python
API_BASE_URL = "https://ai-job-analyzer-production.railway.app"
```

Update to your Render URL once it's ready, OR leave as is for now:
```python
API_BASE_URL = "https://ai-job-analyzer.onrender.com"
```

---

### **STEP 3: Create requirements.txt for Streamlit**

Create: `app/requirements.txt`

```
streamlit==1.32.2
requests==2.31.0
pandas==2.1.3
plotly==5.18.0
```

---

### **STEP 4: Go to Streamlit Cloud**

1. Open **https://streamlit.io/cloud**
2. Click **"Sign in"**
3. Choose **"Sign in with GitHub"**
4. Authorize Streamlit to access your GitHub

---

### **STEP 5: Deploy App**

1. Click **"New app"** button
2. Fill in details:
   - **Repository:** `dipdhru/ai-job-automation-risk-nlp`
   - **Branch:** `main`
   - **Main file path:** `app/app_production.py`
3. Click **"Deploy!"**

---

### **STEP 6: Wait for Deployment**

Streamlit will:
- Clone your repo
- Install dependencies
- Start your app
- Takes 2-3 minutes

You'll see: **"Your app is ready!"** when done

---

### **STEP 7: Get Your Public URL**

Once deployed, you'll get a URL like:
```
https://ai-job-analyzer.streamlit.app
```

✅ **Your Streamlit app is LIVE!**

---

### **STEP 8: Test the App**

1. Visit your Streamlit URL
2. Try the demo without login
3. Register a new account
4. Try job analysis
5. Check user history

---

## 🔗 **Connect to Backend**

When your Render backend is ready:

1. Edit `app/app_production.py` line ~40:
```python
API_BASE_URL = "https://ai-job-analyzer.onrender.com"
```

2. Commit and push to GitHub:
```bash
git add app/app_production.py
git commit -m "Update backend API URL"
git push origin main
```

3. Streamlit auto-redeploys!
4. Now login/signup will work with real backend

---

## 🔄 Auto-Redeployment

After deployment:
- **Automatic:** Every git push → auto-redeploys
- **Manual:** Streamlit Cloud shows redeployment button

---

## 📊 Monitoring

In Streamlit Cloud dashboard:
- **Logs:** See app output and errors
- **Settings:** Change deployment settings
- **Reboot:** Restart the app

---

## ✅ Deployment Checklist

- [ ] `.streamlit/config.toml` created
- [ ] `app/requirements.txt` created
- [ ] GitHub connected to Streamlit
- [ ] Deployed from `app/app_production.py`
- [ ] Status shows "Your app is ready!"
- [ ] Public URL generated
- [ ] App loads in browser
- [ ] Demo works (without login)

---

## 🎯 Your Streamlit URLs

| Page | URL |
|------|-----|
| **App** | `https://ai-job-analyzer.streamlit.app` |
| **Demo** | Visit URL → "Try Demo" section |
| **Login** | Visit URL → Click "Login" |
| **Signup** | Visit URL → Click "Register" |

---

## 📞 Troubleshooting

### "App won't load"
- Check Streamlit logs
- Usually missing import or syntax error
- Fix in code and commit

### "API requests fail"
- Make sure `API_BASE_URL` points to your backend
- Backend must be deployed first
- Check network tab in browser

### "Import errors"
- Check `app/requirements.txt`
- Add missing packages
- Commit and push

---

## 🚀 Next Steps

1. ✅ Deploy Streamlit (you're here!)
2. → Backend goes live (already deploying)
3. → Connect them together
4. → Deploy landing page
5. → Build pitch deck

---

## 💡 Pro Tips

**Before Your Event:**
- Test login/signup flow
- Try job analysis demo
- Have backup screenshots
- Know how to refresh if issues

**User Testing:**
- Share the URL with friends
- Get feedback on UI/UX
- Fix any issues

---

You're ready to deploy! Follow the steps above and you'll have a live Streamlit demo in 10 minutes. 🎉
