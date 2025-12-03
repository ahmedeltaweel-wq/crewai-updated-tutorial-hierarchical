# Deploy Telegram Bot to Google Cloud Run - خطوة بخطوة

## ما تحتاجه
- ✅ حساب Google Cloud (عندك بالفعل)
- ✅ GitHub repository (أنشأته للتو)
- ✅ Bot token و Gemini API key

---

## الخطوة 1: تفعيل Google Cloud Run (دقيقة واحدة)

### 1.1 افتح Google Cloud Console
- اذهب إلى: https://console.cloud.google.com
- سجل دخول بحسابك

### 1.2 اختر أو أنشئ Project
- في الأعلى، اضغط على اسم المشروع
- اختر مشروع موجود أو اضغط **"New Project"**
- اسم المشروع: `telegram-health-bot`
- اضغط **"Create"**

### 1.3 تفعيل Cloud Run API
- في شريط البحث (أعلى الصفحة)، اكتب: `Cloud Run`
- اضغط على **"Cloud Run"**
- إذا طُلب منك، اضغط **"Enable API"**

---

## الخطوة 2: رفع الملفات الجديدة على GitHub (3 دقائق)

### 2.1 ملفات جديدة مطلوبة
ارفع هذين الملفين الجديدين على GitHub repository:

**في GitHub:**
1. افتح repository: `telegram-health-bot`
2. اضغط **"Add file"** → **"Upload files"**
3. ارفع:
   - `Dockerfile`
   - `.dockerignore`
4. Commit message: `Add Docker files`
5. اضغط **"Commit changes"**

---

## الخطوة 3: النشر من GitHub مباشرة (5 دقائق)

### 3.1 في Cloud Run Console
1. اضغط **"Create Service"**
2. اختر **"Continuously deploy from a repository"**
3. اضغط **"Set up with Cloud Build"**

### 3.2 ربط GitHub
1. اضغط **"Authenticate with GitHub"**
2. وافق على الصلاحيات
3. اختر repository: `telegram-health-bot`
4. Branch: `main`
5. اضغط **"Next"**

### 3.3 إعدادات Build
- **Build Type:** `Dockerfile`
- **Source location:** `/Dockerfile`
- اضغط **"Save"**

### 3.4 إعدادات Service
**Service name:** `telegram-health-bot`

**Region:** اختر الأقرب لك:
- `europe-west1` (Belgium) - أوروبا
- `us-central1` (Iowa) - أمريكا
- `asia-southeast1` (Singapore) - آسيا

**Authentication:** 
- اختر **"Allow unauthenticated invocations"** ✅

**CPU allocation:** 
- اختر **"CPU is only allocated during request processing"**

**Minimum instances:** `0` (مجاني)
**Maximum instances:** `1`

### 3.5 Environment Variables (مهم جداً!)

اضغط **"Container, Variables & Secrets, Connections, Security"**

في تبويب **"Variables & Secrets"**، اضغط **"Add Variable"**:

**Variable 1:**
- Name: `TELEGRAM_BOT_TOKEN`
- Value: `8529682573:AAEiqj1ujm3peulewO_n8KYtaDje_0c1ZAE`

**Variable 2:**
- Name: `GEMINI_API_KEY`
- Value: `AIzaSyBXiQVCJsln1_0EKQ2z2zOkkCLSvWm4XCE`

### 3.6 Deploy!
اضغط **"Create"** (أزرق في الأسفل)

---

## الخطوة 4: انتظر النشر (2-3 دقائق)

سترى:
1. **Building...** - يبني Docker image
2. **Deploying...** - ينشر على Cloud Run
3. ✅ **Service deployed** - جاهز!

---

## الخطوة 5: تحقق من النجاح

### 5.1 شاهد Logs
- في صفحة Service، اضغط تبويب **"Logs"**
- ابحث عن:
```
✅ Bot is ready!
🤖 You can now send messages to your bot on Telegram
```

### 5.2 اختبر البوت
- افتح Telegram
- ابحث عن: `@My_konecta_bot`
- أرسل: **"مرحبا"**
- البوت يرد! 🎉

---

## مميزات Google Cloud Run

✅ **Always-On:** يعمل 24/7 بدون توقف
✅ **Free Tier:** 2 مليون طلب مجاناً شهرياً
✅ **Fast:** يستجيب فوراً (بدون sleep)
✅ **Scalable:** يتوسع تلقائياً مع الاستخدام
✅ **Auto-Deploy:** أي تغيير في GitHub ينشر تلقائياً!

---

## تحديث البوت

**لتحديث company_knowledge.md أو أي ملف:**

1. عدّل الملف في GitHub
2. Commit changes
3. Cloud Build ينشر تلقائياً (2-3 دقائق)
4. البوت محدّث! ✅

---

## التكلفة

**Free Tier (مجاني):**
- 2 مليون طلب/شهر
- 360,000 GB-seconds
- 180,000 vCPU-seconds

**بوت Telegram صغير مثل هذا:**
- استخدام: ~0.5% من Free Tier
- التكلفة: **$0.00** (مجاني تماماً!)

---

## Troubleshooting

### البوت لا يرد؟
1. تحقق من Logs في Cloud Run
2. تأكد من Environment Variables صحيحة
3. تأكد من Service "deployed" بنجاح

### Build فشل؟
1. تحقق من وجود `Dockerfile` في GitHub
2. تحقق من `requirements.txt` صحيح
3. شاهد Build logs للتفاصيل

---

## 🎉 تم! البوت الآن يعمل 24/7 على Google Cloud!

**رابط Service:** سيظهر في Cloud Run Console
**رابط البوت:** https://t.me/My_konecta_bot

**استمتع! 🚀**
