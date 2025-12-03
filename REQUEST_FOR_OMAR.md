# 📧 طلب من Omar - تفعيل Google Cloud APIs

## 👋 مرحباً Omar،

أحتاج مساعدتك في تفعيل بعض APIs في المشروع `eg-konecta-sandbox` حتى أتمكن من الـ deployment على Google Cloud Run.

---

## ✅ APIs المطلوب تفعيلها

يرجى تفعيل APIs التالية في المشروع:

### 1. Cloud Run API
**الرابط المباشر:**
https://console.cloud.google.com/apis/library/run.googleapis.com?project=eg-konecta-sandbox

**الخطوات:**
1. افتح الرابط أعلاه
2. اضغط **"Enable"**

---

### 2. Cloud Build API
**الرابط المباشر:**
https://console.cloud.google.com/apis/library/cloudbuild.googleapis.com?project=eg-konecta-sandbox

**الخطوات:**
1. افتح الرابط أعلاه
2. اضغط **"Enable"**

---

### 3. Vertex AI API
**الرابط المباشر:**
https://console.cloud.google.com/apis/library/aiplatform.googleapis.com?project=eg-konecta-sandbox

**الخطوات:**
1. افتح الرابط أعلاه
2. اضغط **"Enable"**

---

### 4. Artifact Registry API
**الرابط المباشر:**
https://console.cloud.google.com/apis/library/artifactregistry.googleapis.com?project=eg-konecta-sandbox

**الخطوات:**
1. افتح الرابط أعلاه
2. اضغط **"Enable"**

---

## 🔧 بديل: عبر gcloud CLI

إذا كنت تفضل استخدام gcloud CLI:

```bash
gcloud config set project eg-konecta-sandbox

gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable aiplatform.googleapis.com
gcloud services enable artifactregistry.googleapis.com
```

---

## 📋 السبب

هذه APIs مطلوبة لـ:
- ✅ **Cloud Run API**: لنشر التطبيقات
- ✅ **Cloud Build API**: لبناء Docker images من GitHub
- ✅ **Vertex AI API**: لاستخدام Gemini عبر Service Account
- ✅ **Artifact Registry API**: لتخزين Docker images

---

## ✅ بعد التفعيل

بعد تفعيل APIs، سأتمكن من:
1. Deploy التطبيقات على Cloud Run
2. استخدام Service Account (`sa-vertex@eg-konecta-sandbox.iam.gserviceaccount.com`)
3. الاستفادة من Vertex AI بدلاً من API Keys

---

## 🔒 ملاحظة أمنية

كما ذكرت سابقاً، استخدام **Service Account مع Vertex AI** هو الطريقة الموصى بها من Google بدلاً من API Keys، لأنها:
- ✅ أكثر أماناً
- ✅ لا تحتاج لتخزين API Keys
- ✅ صلاحيات محكومة ومحددة

---

## 📞 إذا كان لديك أي أسئلة

يمكنني شرح أي تفاصيل إضافية عن:
- لماذا نحتاج كل API
- كيف سيتم استخدامها
- التكلفة المتوقعة (ضمن Free Tier)

---

**شكراً لمساعدتك!** 🙏

Ahmed
