# ⚠️ ملاحظة مهمة: Environment Variables في AWS

## المشكلة
AWS App Runner **لا يقرأ** ملف `.env` تلقائياً.

## الحل (اختر واحد)

### ✅ الحل 1: استخدام apprunner.yaml (الأسهل)

الملف `apprunner.yaml` **يحتوي بالفعل** على المتغيرات:

```yaml
env:
  - name: TELEGRAM_BOT_TOKEN
    value: "8529682573:AAEiqj1ujm3peulewO_n8KYtaDje_0c1ZAE"
  - name: GEMINI_API_KEY
    value: "AIzaSyBXiQVCJsln1_0EKQ2z2zOkkCLSvWm4XCE"
```

**ما تحتاج فعله:**
1. ارفع `apprunner.yaml` على GitHub
2. عند إنشاء Service في App Runner، سيقرأ المتغيرات تلقائياً ✅

---

### الحل 2: إضافة المتغيرات يدوياً في AWS Console

**إذا لم تجد زر "Environment Variables":**

#### في App Runner:
1. بعد إنشاء Service، اذهب إلى **"Configuration"** tab
2. اضغط **"Edit"**
3. scroll لأسفل إلى **"Environment variables"**
4. اضغط **"Add environment variable"**

#### أو في ECS:
1. في Task Definition
2. Container definitions
3. اضغط على Container name
4. scroll إلى **"Environment"**
5. أضف المتغيرات

---

### الحل 3: استخدام AWS Secrets Manager (الأكثر أماناً)

#### 3.1 إنشاء Secrets
```bash
aws secretsmanager create-secret \
    --name telegram-bot-token \
    --secret-string "8529682573:AAEiqj1ujm3peulewO_n8KYtaDje_0c1ZAE"

aws secretsmanager create-secret \
    --name gemini-api-key \
    --secret-string "AIzaSyBXiQVCJsln1_0EKQ2z2zOkkCLSvWm4XCE"
```

#### 3.2 تعديل telegram_bot.py
```python
import boto3
import json

def get_secret(secret_name):
    client = boto3.client('secretsmanager', region_name='us-east-1')
    response = client.get_secret_value(SecretId=secret_name)
    return response['SecretString']

# في بداية الملف، بدلاً من os.getenv:
TELEGRAM_TOKEN = get_secret('telegram-bot-token')
GEMINI_KEY = get_secret('gemini-api-key')
```

---

## ✅ التوصية: استخدم apprunner.yaml

**لماذا؟**
1. ✅ بسيط - لا تحتاج تعديل كود
2. ✅ تلقائي - App Runner يقرأه مباشرة
3. ✅ موجود - الملف جاهز بالقيم

**الخطوات:**
1. ارفع `apprunner.yaml` على GitHub ✅
2. عند Create Service، اختر **"Use configuration file"**
3. App Runner يقرأ المتغيرات من الملف تلقائياً
4. تم! 🎉

---

## مكان زر Environment Variables في AWS

### في App Runner:
```
Service → Configuration → Edit → scroll down → Environment variables
```

### في ECS:
```
Task Definition → Container → Environment → Environment variables
```

### في Lambda:
```
Function → Configuration → Environment variables
```

---

**استخدم `apprunner.yaml` وكل شيء سيعمل تلقائياً!** ✅
