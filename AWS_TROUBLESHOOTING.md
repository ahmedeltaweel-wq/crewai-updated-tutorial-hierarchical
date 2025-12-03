# 🔍 AWS App Runner - Troubleshooting Deployment Failure

## ✅ Build نجح، لكن Deploy فشل

**السبب المحتمل:**
AWS App Runner ينتظر استجابة HTTP على port 8080، لكن البوت لا يستجيب بسرعة كافية.

---

## ✅ الحل السريع

### تأكد أن `telegram_bot.py` المحدّث موجود على GitHub

**الملف يجب أن يحتوي على:**
```python
from flask import Flask

# Flask app for health check
flask_app = Flask(__name__)

@flask_app.route('/')
@flask_app.route('/health')
def health_check():
    return {'status': 'healthy'}, 200

def run_flask():
    port = int(os.getenv('PORT', 8080))
    flask_app.run(host='0.0.0.0', port=port)

# في main():
flask_thread = Thread(target=run_flask, daemon=True)
flask_thread.start()
```

---

## 🔧 إذا لم يعمل، جرب هذا

### الحل البديل: استخدام Dockerfile مباشرة

بدلاً من `apprunner.yaml`, استخدم `Dockerfile` فقط:

**في AWS App Runner:**
1. Source: GitHub
2. **Deployment settings:** 
   - **Source directory:** `/`
   - **Build command:** (leave empty)
   - **Start command:** `python telegram_bot.py`
3. **Port:** `8080`
4. **Environment variables:**
   - `TELEGRAM_BOT_TOKEN`
   - `GEMINI_API_KEY`

---

## 🚀 الحل الأفضل: استخدام Google Cloud Run

AWS App Runner معقد قليلاً. **Google Cloud Run أسهل بكثير:**

### لماذا Google Cloud Run؟
1. ✅ **أسهل** - Deploy مباشر من GitHub
2. ✅ **أسرع** - يشتغل من أول مرة
3. ✅ **مجاني** - Free tier كبير
4. ✅ **Always-on** - بدون sleep

### الخطوات (5 دقائق):
1. افتح: https://console.cloud.google.com/run
2. Click **"Create Service"**
3. **Source:** Deploy from GitHub
4. Connect GitHub → Select `telegram-health-bot`
5. **Region:** europe-west1
6. **Environment variables:**
   - `TELEGRAM_BOT_TOKEN`
   - `GEMINI_API_KEY`
7. **Deploy!**

---

## 💡 التوصية النهائية

**استخدم Google Cloud Run** - أسهل وأسرع وأكثر موثوقية.

**أو:**

إذا تريد AWS، استخدم **AWS Lambda + API Gateway** بدلاً من App Runner.

---

**ما رأيك؟ نجرب Google Cloud Run؟** 🎯
