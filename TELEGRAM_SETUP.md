# Telegram Bot Setup Guide

## 🚀 Quick Start (5 Minutes)

### Step 1: Create Your Telegram Bot

1. Open **Telegram** app on your phone or computer
2. Search for **@BotFather**
3. Start a chat and send: `/newbot`
4. Choose a **name** for your bot (e.g., "Health Insurance Assistant")
5. Choose a **username** (must end with 'bot', e.g., "my_health_insurance_bot")
6. **Copy the API Token** (looks like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

### Step 2: Add Token to .env File

Open `.env` file and add this line:
```
TELEGRAM_BOT_TOKEN=paste_your_token_here
```

**Example:**
```
GEMINI_API_KEY=AIzaSyB3m8Pm-7V6y8uf9rwl5gGiwKpO7DiAkRw
GOOGLE_API_KEY=AIzaSyB3m8Pm-7V6y8uf9rwl5gGiwKpO7DiAkRw
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
```

### Step 3: Install Dependencies

```bash
pip install -r requirements_telegram.txt
```

### Step 4: Run the Bot

**Option A: Double-click**
- Double-click `START_TELEGRAM.bat`

**Option B: Command line**
```bash
python telegram_bot.py
```

### Step 5: Test Your Bot

1. Open Telegram
2. Search for your bot (the username you created)
3. Click **Start** or send `/start`
4. Try these commands:
   - `/help` - Get help
   - `/coverage` - See coverage info
   - `/claims` - Claims process
   - `/contact` - Contact info
5. Or just send a message:
   - "مرحبا" (Arabic)
   - "hello" (English)
   - "What does the premium package cover?"

## ✅ Features

- 🌍 **Bilingual**: Arabic & English
- 🤖 **AI Powered**: Google Gemini 1.5 Flash
- 📚 **Knowledge Base**: Health insurance info
- ⚡ **Quick Commands**: /coverage, /claims, /contact
- 💬 **Natural Chat**: Ask anything!

## 🛠️ Troubleshooting

### "TELEGRAM_BOT_TOKEN not found"
- Make sure you added the token to `.env` file
- Check there are no extra spaces
- Restart the bot

### "ModuleNotFoundError"
- Run: `pip install -r requirements_telegram.txt`

### Bot doesn't respond
- Check the terminal for errors
- Make sure the bot is running
- Try `/start` command first

## 📝 Available Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the bot and get welcome message |
| `/help` | Show help message |
| `/coverage` | View insurance coverage options |
| `/claims` | Learn how to file claims |
| `/contact` | Get contact information |

## 🎯 What's Reused from WhatsApp Bot

✅ **Same AI Brain** (`knowledge_base.py`, Gemini AI)
✅ **Same Language Detection** (`language_detector.py`)
✅ **Same Response Formatting** (`response_formatter.py`)
✅ **Same Bilingual Support** (Arabic/English)

**Only New File:** `telegram_bot.py` (Telegram connector)

## 🔒 Security

- Token is stored in `.env` (not committed to git)
- Bot only responds to direct messages
- No data is stored permanently

## 📞 Support

If you have issues:
1. Check the terminal output for errors
2. Make sure `.env` has both `GEMINI_API_KEY` and `TELEGRAM_BOT_TOKEN`
3. Verify bot is running (you should see "Bot is ready!")

---

**That's it! Your Telegram bot is ready! 🎉**
