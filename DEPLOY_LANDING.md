# 🌐 Deploy Landing Page - 5 Minutes

**Status:** 100% Free, GitHub Pages  
**Time:** 5 minutes  
**Result:** Live marketing page at `https://yourusername.github.io/ai-job-automation-risk-nlp`

---

## ✅ What You'll Get

- 📱 Professional landing page
- 📧 Email signup form
- 💰 Pricing tiers
- 🎯 Problem/solution explanation
- 📊 Statistics display
- ✨ Responsive design

---

## 🎯 Step-by-Step Deployment

### **STEP 1: Create GitHub Pages Directory**

We already have `landing/index.html`, now we need to configure GitHub Pages.

**Go to your repo:**
1. GitHub → `dipdhru/ai-job-automation-risk-nlp`
2. Click **"Settings"** tab
3. Left sidebar → **"Pages"**

---

### **STEP 2: Enable GitHub Pages**

In the Pages section:

1. **Source:** Select **"Deploy from a branch"**
2. **Branch:** Select **"main"**
3. **Folder:** Select **"/landing"** (or create `/docs` folder)
4. Click **"Save"**

GitHub will build and deploy your page

---

### **STEP 3: Wait 1-2 Minutes**

GitHub processes the deployment.

You'll see a green checkmark when ready:
```
✅ Your site is published at: 
https://yourusername.github.io/ai-job-automation-risk-nlp
```

---

### **STEP 4: Visit Your Site**

Open the URL shown in GitHub Pages settings.

You should see:
- 🤖 Logo at top
- Problem/solution sections
- Pricing tiers
- Email signup form
- Professional styling

✅ **Your landing page is LIVE!**

---

## 🔗 **Connect to Streamlit & Backend**

The landing page currently has a demo signup form. To make it functional:

### **Option A: Collect Emails (Simple)**

1. Edit `landing/index.html`
2. Find the form submission code (around line 300)
3. Replace with your email service (Mailchimp, ConvertKit, etc)

### **Option B: Connect to Backend Waitlist**

1. Create a waitlist endpoint in your backend
2. Update the form to post to your API
3. Backend saves emails to database

---

## 📋 **URL Structure**

Your landing page will be at:
```
https://YOUR-USERNAME.github.io/ai-job-automation-risk-nlp/
```

For example:
```
https://dipdhru.github.io/ai-job-automation-risk-nlp/
```

---

## 📧 **Make Signup Form Work**

The signup form currently has a demo. To make it real:

### **Using Mailchimp (Easiest - Free)**

1. Go to **mailchimp.com**
2. Sign up (free)
3. Create audience/list
4. Get your form embed code
5. Replace the form in `landing/index.html`

### **Using Backend API**

1. Create endpoint in FastAPI: `POST /api/v1/waitlist`
2. Update form in HTML to POST to backend
3. Backend saves to database

---

## 🔄 **Update Landing Page**

If you need to update the page:

1. Edit `landing/index.html`
2. Commit and push to GitHub:
```bash
git add landing/index.html
git commit -m "Update landing page"
git push origin main
```

3. GitHub auto-redeploys in 1-2 minutes

---

## ✅ Deployment Checklist

- [ ] GitHub Pages enabled in Settings
- [ ] Source set to "main" branch
- [ ] Folder set to "/landing"
- [ ] Green checkmark shown
- [ ] Public URL generated
- [ ] Page loads in browser
- [ ] Can see all content
- [ ] Form appears

---

## 📊 Your URLs

| Page | URL |
|------|-----|
| **Landing** | `https://yourusername.github.io/ai-job-automation-risk-nlp/` |
| **About** | `https://yourusername.github.io/ai-job-automation-risk-nlp/#about` |
| **Pricing** | `https://yourusername.github.io/ai-job-automation-risk-nlp/#pricing` |

---

## 🎯 What to Do Next

1. ✅ Deploy Streamlit (10 min)
2. ✅ Deploy Landing (5 min) ← You're here!
3. → Build Pitch Deck (30 min)
4. → Backend goes live (already deploying)
5. → Connect everything

---

## 💡 Pro Tips

**Share Your Landing Page:**
- Send to friends for feedback
- Share in social media
- Include in event materials
- Link from your pitch deck

**Track Signups:**
- If using Mailchimp, you get analytics
- Can see how many visitors
- Track conversion rates

**Custom Domain (Later):**
- You can point your own domain to GitHub Pages
- Settings → Custom domain
- Professional look for investors

---

## 📞 Troubleshooting

### "Page not showing"
- Make sure folder is `/landing`
- Wait 2-3 minutes for deployment
- Check green checkmark in Settings

### "URL is weird"
- GitHub pages URL includes repo name
- Format: `username.github.io/repo-name/`
- You can set custom domain later

### "Form doesn't work"
- Demo form is just a placeholder
- Connect to Mailchimp or backend
- Instructions above ⬆️

---

Your landing page is ready to deploy in 5 minutes! 🎉
