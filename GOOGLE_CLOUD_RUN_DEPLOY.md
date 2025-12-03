# 🚀 Deploy to Google Cloud Run - دليل شامل محدّث

## ✨ الجديد: دعم Service Account (بدون API Keys!)

هذا الدليل محدّث ليدعم **طريقتين للمصادقة**:
1. ✅ **API Key** (للتطوير السريع)
2. ✅ **Service Account** (الموصى به للـ Production)

---

## 📋 المتطلبات

- ✅ حساب Google Cloud
- ✅ GitHub repository
- ✅ Service Account: `sa-vertex@eg-konecta-sandbox.iam.gserviceaccount.com`
- ✅ المشروع: `eg-konecta-sandbox`

---

## 🎯 الطريقة 1: Deploy باستخدام Service Account (الموصى بها)

### الخطوة 1: تفعيل APIs المطلوبة

> **ملاحظة:** إذا لم يكن لديك صلاحيات لتفعيل APIs، اطلب من **Omar** أو مدير المشروع تفعيلها.

#### الطريقة 1: عبر Console (الموصى بها)

افتح Cloud Console وفعّل APIs التالية:

1. **Cloud Run API**
   - https://console.cloud.google.com/apis/library/run.googleapis.com?project=eg-konecta-sandbox
   - اضغط **"Enable"**

2. **Cloud Build API**
   - https://console.cloud.google.com/apis/library/cloudbuild.googleapis.com?project=eg-konecta-sandbox
   - اضغط **"Enable"**

3. **Vertex AI API**
   - https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?project=eg-konecta-sandbox
   - اضغط **"Enable"**

4. **Artifact Registry API** (بدلاً من Container Registry)
   - https://console.cloud.google.com/apis/library/artifactregistry.googleapis.com?project=eg-konecta-sandbox
   - اضغط **"Enable"**

#### الطريقة 2: عبر gcloud CLI (يحتاج صلاحيات Admin)

```bash
# فقط إذا كنت Admin أو لديك صلاحيات Service Usage Admin
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable aiplatform.googleapis.com
gcloud services enable artifactregistry.googleapis.com
```

> **إذا حصلت على `PERMISSION_DENIED`:** اطلب من Omar تفعيل APIs عبر Console.

---

### الخطوة 2: منح صلاحيات Service Account

تأكد من أن Service Account لديه الصلاحيات التالية:

```bash
gcloud projects add-iam-policy-binding eg-konecta-sandbox \
    --member="serviceAccount:sa-vertex@eg-konecta-sandbox.iam.gserviceaccount.com" \
    --role="roles/aiplatform.user"

gcloud projects add-iam-policy-binding eg-konecta-sandbox \
    --member="serviceAccount:sa-vertex@eg-konecta-sandbox.iam.gserviceaccount.com" \
    --role="roles/run.invoker"
```

**أو في Console:**
1. اذهب إلى: IAM & Admin > IAM
2. ابحث عن: `sa-vertex@eg-konecta-sandbox.iam.gserviceaccount.com`
3. تأكد من وجود:
   - ✅ Vertex AI User
   - ✅ Cloud Run Invoker

---

### الخطوة 3: رفع الكود على GitHub

تأكد من أن repository يحتوي على:

```
telegram-health-bot/
├── telegram_bot.py           ✅ (محدّث لدعم Vertex AI)
├── electric_web_app.py       ✅ (محدّث لدعم Vertex AI)
├── requirements.txt          ✅ (يحتوي على google-cloud-aiplatform)
├── Dockerfile
├── .dockerignore
├── company_knowledge.md
├── knowledge_base.py
├── language_detector.py
├── response_formatter.py
└── company_loader.py
```

---

### الخطوة 4: Deploy على Cloud Run

#### 4.1 في Cloud Run Console

1. اذهب إلى: https://console.cloud.google.com/run
2. اضغط **"Create Service"**
3. اختر **"Continuously deploy from a repository"**
4. اضغط **"Set up with Cloud Build"**

#### 4.2 ربط GitHub

1. اضغط **"Authenticate with GitHub"**
2. اختر repository: `telegram-health-bot`
3. Branch: `main`
4. اضغط **"Next"**

#### 4.3 إعدادات Build

- **Build Type:** `Dockerfile`
- **Source location:** `/Dockerfile`
- اضغط **"Save"**

#### 4.4 إعدادات Service

**Service name:** `telegram-health-bot`

**Region:** اختر الأقرب:
- `us-central1` (Iowa) - موصى به (نفس منطقة Vertex AI)
- `europe-west1` (Belgium)
- `asia-southeast1` (Singapore)

**Authentication:**
- ✅ **Allow unauthenticated invocations**

**CPU allocation:**
- ✅ **CPU is only allocated during request processing**

**Autoscaling:**
- Minimum instances: `0` (مجاني)
- Maximum instances: `1` (أو أكثر حسب الحاجة)

#### 4.5 Environment Variables

اضغط **"Container, Variables & Secrets, Connections, Security"**

في تبويب **"Variables & Secrets"**:

**للـ Telegram Bot:**
```
TELEGRAM_BOT_TOKEN=your-telegram-token
GOOGLE_CLOUD_PROJECT=eg-konecta-sandbox
USE_VERTEX_AI=true
VERTEX_AI_LOCATION=us-central1
```

**للـ Electric Web App:**
```
GOOGLE_CLOUD_PROJECT=eg-konecta-sandbox
```

> **ملاحظة:** لا حاجة لـ `GEMINI_API_KEY` عند استخدام Vertex AI!

#### 4.6 Service Account

في تبويب **"Security"**:

- **Service account:** اختر `sa-vertex@eg-konecta-sandbox.iam.gserviceaccount.com`

> **مهم جداً!** هذا يسمح للتطبيق باستخدام Service Account للوصول إلى Vertex AI.

#### 4.7 Deploy!

اضغط **"Create"** (أزرق في الأسفل)

---

### الخطوة 5: انتظر النشر (2-3 دقائق)

سترى:
1. **Building...** - يبني Docker image
2. **Deploying...** - ينشر على Cloud Run
3. ✅ **Service deployed** - جاهز!

---

### الخطوة 6: تحقق من النجاح

#### 6.1 شاهد Logs

- في صفحة Service، اضغط تبويب **"Logs"**
- ابحث عن:
```
☁️ Using Google Cloud Vertex AI (Service Account)
✅ Vertex AI initialized: eg-konecta-sandbox / us-central1
✅ Bot is ready!
```

#### 6.2 اختبر التطبيق

**Telegram Bot:**
- افتح Telegram
- ابحث عن بوتك
- أرسل: **"مرحبا"**
- البوت يرد! 🎉

**Electric Web App:**
- افتح URL من Cloud Run
- اختبر الواجهة

---

## 🎯 الطريقة 2: Deploy باستخدام API Key (بديل)

إذا أردت استخدام API Key بدلاً من Service Account:

### Environment Variables:

```
TELEGRAM_BOT_TOKEN=your-telegram-token
GOOGLE_API_KEY=your-gemini-api-key
```

**لا تضيف:**
- ❌ `USE_VERTEX_AI`
- ❌ `GOOGLE_CLOUD_PROJECT`

**Service Account:**
- يمكنك استخدام Default Compute Service Account

---

## 📊 مقارنة الطرق

| الميزة | API Key | Service Account |
|--------|---------|-----------------|
| **الأمان** | ⚠️ متوسط | ✅ عالي |
| **الإعداد** | ✅ سهل | ⚠️ متوسط |
| **Rate Limits** | محدودة | أعلى |
| **للـ Production** | ❌ غير موصى | ✅ موصى به |
| **التكلفة** | مجاني (حد معين) | مجاني (Free Tier) |

---

## 🔧 Troubleshooting

### المشكلة: `Permission denied` في Logs

**الحل:**
1. تأكد من اختيار Service Account الصحيح
2. تأكد من صلاحيات `Vertex AI User`
3. تحقق من تفعيل Vertex AI API

### المشكلة: `Model not found`

**الحل:**
1. تأكد من `VERTEX_AI_LOCATION=us-central1`
2. جرب model آخر: `gemini-1.5-pro`

### المشكلة: Build فشل

**الحل:**
1. تحقق من `requirements.txt` يحتوي على:
   ```
   google-cloud-aiplatform>=1.38.0
   ```
2. تحقق من وجود `Dockerfile` في GitHub
3. شاهد Build logs للتفاصيل

---

## 💰 التكلفة

### Free Tier (مجاني):

**Cloud Run:**
- 2 مليون طلب/شهر
- 360,000 GB-seconds
- 180,000 vCPU-seconds

**Vertex AI:**
- أول 1000 طلب مجاناً
- بعدها: ~$0.00025 لكل 1000 حرف

**تطبيق صغير مثل Telegram Bot:**
- استخدام: ~1% من Free Tier
- التكلفة المتوقعة: **$0.00 - $0.50/شهر**

---

## 🔄 تحديث التطبيق

**لتحديث الكود:**

1. عدّل الملفات في GitHub
2. Commit changes
3. Cloud Build ينشر تلقائياً (2-3 دقائق)
4. التطبيق محدّث! ✅

**لتحديث Environment Variables:**

1. في Cloud Run Console
2. اضغط **"Edit & Deploy New Revision"**
3. عدّل Variables
4. اضغط **"Deploy"**

---

## 📚 الملفات المحدّثة

تم تحديث الملفات التالية لدعم Vertex AI:

- ✅ `telegram_bot.py` - يدعم API Key و Vertex AI
- ✅ `electric_web_app.py` - يدعم API Key و Vertex AI
- ✅ `requirements.txt` - يحتوي على `google-cloud-aiplatform`
- ✅ `GOOGLE_CLOUD_RUN_DEPLOY.md` - هذا الدليل

---

## 🎉 مميزات الحل الجديد

✅ **آمن:** لا حاجة لتخزين API Keys
✅ **مرن:** يدعم كلا الطريقتين
✅ **موصى به من Google:** Best Practice
✅ **Always-On:** يعمل 24/7
✅ **Auto-Deploy:** تحديثات تلقائية من GitHub
✅ **Scalable:** يتوسع تلقائياً

---

## 🔗 روابط مفيدة

- [Cloud Run Console](https://console.cloud.google.com/run)
- [Vertex AI Console](https://console.cloud.google.com/vertex-ai)
- [IAM & Admin](https://console.cloud.google.com/iam-admin)
- [Vertex AI Pricing](https://cloud.google.com/vertex-ai/pricing)

---

## ✅ الخلاصة

**للـ Production:**
- ✅ استخدم **Service Account** (الطريقة 1)
- ✅ Region: `us-central1`
- ✅ Service Account: `sa-vertex@eg-konecta-sandbox.iam.gserviceaccount.com`

**للتطوير السريع:**
- ✅ استخدم **API Key** (الطريقة 2)

**كلا الطريقتين مدعومتان في الكود الجديد!** 🚀
