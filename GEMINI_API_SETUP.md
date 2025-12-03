# 🔑 دليل استخدام Gemini API (الطريقة الموصى بها)

## ⚠️ لماذا API Key أفضل من Service Account Key؟

| المعيار | API Key | Service Account Key |
|---------|---------|---------------------|
| **الأمان** | ✅ آمن للتطوير | ⚠️ خطر أمني إذا تسرّب |
| **السهولة** | ✅ بسيط جداً | ❌ معقد |
| **الصلاحيات** | ✅ محدودة (Gemini فقط) | ⚠️ صلاحيات كثيرة |
| **التكلفة** | ✅ مجاني (حد معين) | ✅ مجاني |
| **للتطوير المحلي** | ✅ مثالي | ⚠️ غير موصى |

---

## 🎯 الخطوة 1: احصل على Gemini API Key

### الطريقة السريعة:

1. افتح: https://aistudio.google.com/app/apikey
2. اضغط **"Create API Key"**
3. اختر المشروع: **eg-konecta-sandbox**
4. انسخ المفتاح

---

## ⚙️ الخطوة 2: أضف المفتاح إلى `.env`

افتح ملف `.env` وأضف:

```bash
# Gemini API Key (الطريقة الموصى بها)
GOOGLE_API_KEY=AIzaSy...your-api-key-here

# أو استخدم هذا الاسم (كلاهما يعمل)
GEMINI_API_KEY=AIzaSy...your-api-key-here
```

---

## 💻 الخطوة 3: استخدم في الكود

### الطريقة الأولى (الأبسط):

```python
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# سيستخدم GOOGLE_API_KEY تلقائياً من .env
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    temperature=0.7
)
```

### الطريقة الثانية (صريحة):

```python
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    temperature=0.7,
    google_api_key=os.getenv('GOOGLE_API_KEY')
)
```

---

## ✅ الخطوة 4: اختبر الاتصال

شغّل هذا الأمر:

```bash
python test_gemini_simple.py
```

---

## 🚀 الخطوة 5: لا حاجة لتعديل الكود الموجود!

جميع تطبيقاتك الحالية ستعمل مباشرة:
- ✅ `telegram_bot.py`
- ✅ `electric_web_app.py`
- ✅ `web_app.py`
- ✅ `whatsapp_bot.py`

**فقط تأكد من وجود `GOOGLE_API_KEY` في `.env`**

---

## 📊 Rate Limits للـ Free Tier

| Model | Requests/Minute | Tokens/Minute |
|-------|----------------|---------------|
| gemini-2.0-flash-exp | 15 | 1,000,000 |
| gemini-1.5-flash | 15 | 1,000,000 |
| gemini-1.5-pro | 2 | 32,000 |

---

## 🔒 نصائح الأمان

1. ✅ **لا ترفع** `.env` على GitHub
2. ✅ **استخدم** `.env.example` للمشاركة
3. ✅ **قيّد** API Key بـ IP أو Domain (من Console)
4. ✅ **راقب** الاستخدام من Google AI Studio

---

## 🆘 حل المشاكل

### مشكلة: `RESOURCE_EXHAUSTED`
**الحل**: انتظر دقيقة (Rate Limit) أو استخدم model أقل استخداماً

### مشكلة: `Invalid API Key`
**الحل**: تأكد من نسخ المفتاح كاملاً بدون مسافات

### مشكلة: `API Key not found`
**الحل**: تأكد من وجود `GOOGLE_API_KEY` في `.env`

---

## 💡 متى تستخدم Service Account؟

استخدم Service Account **فقط** في هذه الحالات:
- ✅ عند Deploy على Cloud (Cloud Run, GKE)
- ✅ عند استخدام Workload Identity Federation
- ✅ عند الحاجة لصلاحيات متقدمة (BigQuery, Storage)

**للتطوير المحلي**: استخدم API Key دائماً! 🎯
