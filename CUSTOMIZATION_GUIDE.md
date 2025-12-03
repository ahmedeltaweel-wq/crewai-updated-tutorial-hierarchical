# How to Customize for Different Companies

## Quick Start

To use this bot for a different company, simply edit `company_knowledge.md`:

### Step 1: Edit Company Information

Open `company_knowledge.md` and update:

```markdown
## Company Information

**Company Name:** YOUR COMPANY NAME
**Established:** YEAR
**Customer Service:** PHONE NUMBER
**Email:** EMAIL
```

### Step 2: Update Coverage Plans

Replace the coverage details with your company's plans:

```markdown
### Basic Plan (PRICE/month)

**Medical Services:**
- Your services here
- ...
```

### Step 3: Update Contact Information

```markdown
### Contact Information
- **Hotline:** YOUR NUMBER
- **Email:** YOUR EMAIL
```

### Step 4: Restart the Bot

```bash
START_TELEGRAM.bat
```

**That's it!** The bot will automatically load the new information.

---

## File Structure

```
company_knowledge.md    ← Edit this for each company
company_loader.py       ← Don't touch (loads the MD file)
telegram_bot.py         ← Don't touch (main bot)
```

---

## Agent Personality

The agent is named "Ahmed" and has this personality:
- Warm and friendly
- Patient and understanding
- Uses emojis appropriately
- Greets naturally
- Remembers conversation context

You can customize the personality in `telegram_bot.py` (search for "شخصيتك" or "Your Personality").

---

## Testing

1. Run `START_TELEGRAM.bat`
2. Open Telegram
3. Send: "Hello"
4. Agent should greet you warmly!
5. Ask: "What's covered?"
6. Agent uses info from `company_knowledge.md`

---

## Examples of Customization

### For a Dental Clinic:
Edit `company_knowledge.md`:
- Change company name to clinic name
- Update services to dental services
- Change prices to dental prices

### For a Different Insurance Company:
- Update all coverage details
- Change contact information
- Update provider network

**The bot adapts automatically!** 🎯
