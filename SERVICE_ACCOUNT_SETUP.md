# 🔐 دليل استخدام Google Cloud Service Account

> [!CAUTION]
> **تحذير أمني مهم من Google:**
> - Service Account Keys تشكل **خطر أمني** إذا تسربت
> - Google **توصي بعدم** تنزيل Service Account Keys
> - Google **تعطّل تلقائياً** أي مفاتيح تُكتشف في GitHub
> - **للتطوير المحلي**: استخدم [Gemini API Key](GEMINI_API_SETUP.md) بدلاً من ذلك
> - **للـ Production**: استخدم Workload Identity Federation

> [!IMPORTANT]
> **الطريقة الموصى بها:**
> - ✅ **للتطوير المحلي**: استخدم [Gemini API Key](GEMINI_API_SETUP.md) (أبسط وأكثر أماناً)
> - ✅ **للـ Production**: استخدم Workload Identity Federation أو Cloud Run Service Account
> - ⚠️ **Service Account Keys**: فقط إذا كنت مضطراً ولديك خبرة أمنية

---

## 📌 معلومات Service Account الخاص بك

- **Email**: `sa-vertex@eg-konecta-sandbox.iam.gserviceaccount.com`
- **Project**: `eg-konecta-sandbox`
- **Project ID**: `106118533546388607119`

---

## 🎯 الخطوة 1: استخراج JSON Key

### الطريقة اليدوية (الموصى بها):

1. افتح: https://console.cloud.google.com/iam-admin/serviceaccounts?project=eg-konecta-sandbox
2. اضغط على service account: `sa-vertex@eg-konecta-sandbox.iam.gserviceaccount.com`
3. اذهب لتبويب **"Keys"**
4. اضغط **"Add Key"** → **"Create new key"**
5. اختر **JSON** format
6. سيتم تنزيل ملف JSON مثل: `eg-konecta-sandbox-xxxxx.json`

---

## 📂 الخطوة 2: وضع الملف في المشروع

1. **انقل** الملف المُنزّل إلى مجلد المشروع:
   ```
   c:\Users\Ahmed\OneDrive - Konecta\Documents\mcp\New folder\crewai-updated-tutorial-hierarchical\
   ```

2. **أعد تسمية** الملف إلى اسم بسيط:
   ```
   service-account-key.json
   ```

3. **تأكد** من إضافة الملف إلى `.gitignore` (لحماية المفتاح):
   ```
   service-account-key.json
   *.json
   ```

---

## ⚙️ الخطوة 3: تحديث ملف `.env`

أضف المتغير التالي إلى ملف `.env`:

```bash
# Google Cloud Service Account
GOOGLE_APPLICATION_CREDENTIALS=service-account-key.json

# أو استخدم المسار الكامل:
# GOOGLE_APPLICATION_CREDENTIALS=c:\Users\Ahmed\OneDrive - Konecta\Documents\mcp\New folder\crewai-updated-tutorial-hierarchical\service-account-key.json
```

---

## 💻 الخطوة 4: تحديث الكود Python

### الطريقة الأولى: استخدام متغير البيئة (الأسهل)

```python
import os
from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()

# سيتم استخدام Service Account تلقائياً
# لا حاجة لكود إضافي!
```

### الطريقة الثانية: تحديد المسار مباشرة

```python
import os
from google.oauth2 import service_account
from google.cloud import aiplatform

# تحديد مسار المفتاح
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service-account-key.json'

# أو استخدام credentials مباشرة
credentials = service_account.Credentials.from_service_account_file(
    'service-account-key.json',
    scopes=['https://www.googleapis.com/auth/cloud-platform']
)

# استخدام credentials مع Vertex AI
aiplatform.init(
    project='eg-konecta-sandbox',
    credentials=credentials
)
```

### الطريقة الثالثة: للاستخدام مع CrewAI و LangChain

```python
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# تأكد من وجود المفتاح
if not os.getenv('GOOGLE_APPLICATION_CREDENTIALS'):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service-account-key.json'

# استخدام Gemini مع Service Account
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    temperature=0.7
)
```

---

## 🔧 الخطوة 5: تثبيت المكتبات المطلوبة

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2
pip install google-cloud-aiplatform
pip install langchain-google-genai
```

---

## ✅ الخطوة 6: اختبار الاتصال

أنشئ ملف `test_service_account.py`:

```python
import os
from dotenv import load_dotenv
from google.oauth2 import service_account
from google.auth.transport.requests import Request

load_dotenv()

# تحميل credentials
credentials = service_account.Credentials.from_service_account_file(
    os.getenv('GOOGLE_APPLICATION_CREDENTIALS', 'service-account-key.json'),
    scopes=['https://www.googleapis.com/auth/cloud-platform']
)

# اختبار الاتصال
credentials.refresh(Request())

print("✅ Service Account يعمل بنجاح!")
print(f"📧 Service Account Email: {credentials.service_account_email}")
print(f"🆔 Project ID: {credentials.project_id}")
```

شغّل الاختبار:
```bash
python test_service_account.py
```

---

## 🚀 الخطوة 7: تحديث التطبيقات الموجودة

### تحديث `telegram_bot.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

# تأكد من وجود Service Account credentials
if not os.getenv('GOOGLE_APPLICATION_CREDENTIALS'):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service-account-key.json'

# باقي الكود كما هو...
```

### تحديث `electric_web_app.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

# تأكد من وجود Service Account credentials
if not os.getenv('GOOGLE_APPLICATION_CREDENTIALS'):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'service-account-key.json'

# باقي الكود كما هو...
```

---

## 🔒 الخطوة 8: تأمين المفتاح

### تحديث `.gitignore`:

```
# Google Cloud Service Account Keys
service-account-key.json
*-service-account-*.json
*.json

# Environment files
.env
.env.local
.env.*.local
```

---

## 📊 مقارنة بين الطرق

| الميزة | API Key | Service Account |
|--------|---------|-----------------|
| **الأمان** | ⚠️ متوسط | ✅ عالي |
| **الصلاحيات** | محدودة | كاملة |
| **الاستخدام** | بسيط | احترافي |
| **للـ Production** | ❌ غير موصى | ✅ موصى به |
| **Rate Limits** | محدودة | أعلى |

---

## ⚠️ ملاحظات مهمة

1. **لا تشارك** ملف JSON مع أحد
2. **لا ترفع** الملف على GitHub
3. **استخدم** `.gitignore` دائماً
4. **للـ Production**: استخدم Google Cloud Secret Manager

---

## 🆘 حل المشاكل الشائعة

### مشكلة: `FileNotFoundError: service-account-key.json`
**الحل**: تأكد من وضع الملف في نفس مجلد المشروع

### مشكلة: `Permission denied`
**الحل**: تأكد من أن Service Account لديه صلاحيات Vertex AI User

### مشكلة: `Invalid credentials`
**الحل**: تأكد من تنزيل JSON key جديد من Google Cloud Console

---

## 📞 الدعم

إذا واجهت أي مشكلة، راجع:
- [Google Cloud Authentication Docs](https://cloud.google.com/docs/authentication)
- [Vertex AI Python SDK](https://cloud.google.com/vertex-ai/docs/python-sdk/use-vertex-ai-python-sdk)
