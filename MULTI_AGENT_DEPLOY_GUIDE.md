# 🚀 Deploy Multi-Agent Apps to Fly.io - Step by Step

## المشروعان:

### 1. AI Newsletter Crew
**URL المتوقع:** https://ai-newsletter-crew.fly.dev

### 2. Electric Call Center
**URL المتوقع:** https://electric-call-center.fly.dev

---

## 📋 الخطوات التفصيلية:

### المشروع 1: AI Newsletter Crew

#### 1. إنشاء GitHub Repository

1. اذهب إلى: https://github.com/new
2. **Repository name:** `ai-newsletter-crew`
3. **Description:** `AI-powered newsletter generation using multi-agent system`
4. **Private** ✅
5. اضغط **"Create repository"**

#### 2. رفع الملفات

**الملفات المطلوبة:**
```
web_app.py
agents.py
tasks.py
file_io.py
templates/index.html
Dockerfile (rename from Dockerfile.newsletter)
requirements.txt (rename from requirements_newsletter.txt)
.gitignore
```

**في GitHub:**
1. اضغط **"Add file"** → **"Upload files"**
2. ارفع الملفات المذكورة
3. **مهم:** غيّر أسماء:
   - `Dockerfile.newsletter` → `Dockerfile`
   - `requirements_newsletter.txt` → `requirements.txt`
4. Commit: `Initial commit - AI Newsletter Crew`

#### 3. Deploy على Fly.io

1. اذهب إلى: https://fly.io/dashboard
2. اضغط **"New App"**
3. اختر **"Deploy from GitHub"**
4. Select: `ai-newsletter-crew`
5. **App name:** `ai-newsletter-crew`
6. **Region:** `cdg` (Paris)

#### 4. إضافة Secrets

**في Fly.io Dashboard:**
1. اذهب إلى App → **"Secrets"**
2. اضغط **"Add Secret"**
3. أضف:
```
GOOGLE_API_KEY = AIzaSyB3m8Pm-7V6y8uf9rwl5gGiwKpO7DiAkRw
PORT = 5000
```

#### 5. Deploy!

1. اضغط **"Deploy"**
2. انتظر 3-5 دقائق
3. افتح: https://ai-newsletter-crew.fly.dev
4. اختبر النظام! ✅

---

### المشروع 2: Electric Call Center

#### 1. إنشاء GitHub Repository

1. اذهب إلى: https://github.com/new
2. **Repository name:** `electric-call-center`
3. **Description:** `Saudi Electric Company AI Call Center System`
4. **Private** ✅
5. اضغط **"Create repository"**

#### 2. رفع الملفات

**الملفات المطلوبة:**
```
electric_web_app.py
electric_agents.py
electric_tasks.py
electric_file_io.py
templates/electric_index.html
Dockerfile (rename from Dockerfile.electric)
requirements.txt (rename from requirements_electric.txt)
.gitignore
```

**في GitHub:**
1. اضغط **"Add file"** → **"Upload files"**
2. ارفع الملفات المذكورة
3. **مهم:** غيّر أسماء:
   - `Dockerfile.electric` → `Dockerfile`
   - `requirements_electric.txt` → `requirements.txt`
4. Commit: `Initial commit - Electric Call Center`

#### 3. Deploy على Fly.io

1. اذهب إلى: https://fly.io/dashboard
2. اضغط **"New App"**
3. اختر **"Deploy from GitHub"**
4. Select: `electric-call-center`
5. **App name:** `electric-call-center`
6. **Region:** `cdg` (Paris)

#### 4. إضافة Secrets

**في Fly.io Dashboard:**
1. اذهب إلى App → **"Secrets"**
2. اضغط **"Add Secret"**
3. أضف:
```
GOOGLE_API_KEY = AIzaSyB3m8Pm-7V6y8uf9rwl5gGiwKpO7DiAkRw
PORT = 5001
```

#### 5. Deploy!

1. اضغط **"Deploy"**
2. انتظر 3-5 دقائق
3. افتح: https://electric-call-center.fly.dev
4. اختبر النظام! ✅

---

## ✅ النتيجة النهائية:

### 3 تطبيقات على Fly.io:

1. ✅ **Telegram Bot:** https://telegram-health-bot.fly.dev
2. ✅ **AI Newsletter:** https://ai-newsletter-crew.fly.dev
3. ✅ **Electric Call Center:** https://electric-call-center.fly.dev

---

## 📊 الملخص:

**التكلفة:** مجاني (Fly.io Free Tier)
**الوقت:** ~30 دقيقة للثلاثة
**النتيجة:** 3 تطبيقات تعمل 24/7

**مبروك! 🎉**
