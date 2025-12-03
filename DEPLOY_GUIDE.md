# Deploy Telegram Bot to Render.com - Step by Step

## What You'll Need
- GitHub account (free)
- Render.com account (free)
- Your bot token and Gemini API key

---

## Step 1: Create GitHub Repository (5 minutes)

### 1.1 Go to GitHub
- Visit: https://github.com
- Sign in (or create free account)

### 1.2 Create New Repository
- Click green "New" button (top right)
- Repository name: `telegram-health-bot`
- Description: "AI Health Insurance Bot"
- **Public** (required for free Render)
- ✅ Add README file
- Click "Create repository"

### 1.3 Upload Files
Click "Add file" → "Upload files", then drag these files:

**Required Files:**
- `telegram_bot.py`
- `company_knowledge.md`
- `company_loader.py`
- `knowledge_base.py`
- `language_detector.py`
- `response_formatter.py`
- `requirements.txt`
- `.gitignore`
- `README.md`

**Click "Commit changes"**

---

## Step 2: Deploy to Render.com (5 minutes)

### 2.1 Sign Up
- Visit: https://render.com
- Click "Get Started"
- Sign up with GitHub (easiest)
- Authorize Render to access GitHub

### 2.2 Create Web Service
- Click "New +" (top right)
- Select "Web Service"
- Click "Connect" next to your `telegram-health-bot` repo
- If you don't see it, click "Configure account" and grant access

### 2.3 Configure Service
Fill in these fields:

**Name:** `telegram-health-bot`

**Region:** Frankfurt (or closest to you)

**Branch:** `main`

**Runtime:** Python 3

**Build Command:** 
```
pip install -r requirements.txt
```

**Start Command:**
```
python telegram_bot.py
```

**Instance Type:** Free

### 2.4 Add Environment Variables
Click "Advanced" → "Add Environment Variable"

Add these TWO variables:

**Variable 1:**
- Key: `TELEGRAM_BOT_TOKEN`
- Value: `8529682573:AAEiqj1ujm3peulewO_n8KYtaDje_0c1ZAE`

**Variable 2:**
- Key: `GEMINI_API_KEY`
- Value: `AIzaSyBXiQVCJsln1_0EKQ2z2zOkkCLSvWm4XCE`

### 2.5 Deploy!
- Click "Create Web Service"
- Wait 2-3 minutes for deployment
- Watch the logs scroll by

---

## Step 3: Verify It Works (2 minutes)

### 3.1 Check Logs
In Render dashboard, you should see:
```
✅ Bot is ready!
🤖 You can now send messages to your bot on Telegram
```

### 3.2 Test on Telegram
- Open Telegram
- Search: `@My_konecta_bot`
- Send: "مرحبا"
- Bot should respond! 🎉

---

## Troubleshooting

### Bot doesn't respond?
1. Check Render logs for errors
2. Verify environment variables are correct
3. Make sure bot token is valid

### "Application failed to respond"?
- This is normal! Render expects a web server
- Bot still works fine on Telegram
- Ignore this error

### Want to update the bot?
1. Edit files on GitHub
2. Commit changes
3. Render auto-deploys in 1-2 minutes!

---

## Important Notes

✅ **Free Tier Limits:**
- Bot sleeps after 15 min inactivity
- Wakes up when someone sends a message
- First message might take 30 seconds

✅ **24/7 Operation:**
- Bot runs without your computer
- Always available on Telegram
- Free forever!

✅ **Updating Company Info:**
- Edit `company_knowledge.md` on GitHub
- Commit changes
- Render auto-updates!

---

## Next Steps

1. **Customize:** Edit `company_knowledge.md` for your company
2. **Monitor:** Check Render logs occasionally
3. **Share:** Give bot link to customers!

**Your bot is now live! 🚀**
