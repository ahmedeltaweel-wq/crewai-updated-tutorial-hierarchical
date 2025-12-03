# 🔒 الحل الآمن: استخدام AWS Secrets في App Runner

## ⚠️ المشكلة
GitHub اكتشف المفاتيح السرية في `apprunner.yaml` - هذا **غير آمن**!

## ✅ الحل الصحيح: AWS Console Environment Variables

### الخطوة 1: حذف المفاتيح من GitHub (تم ✅)
الملف `apprunner.yaml` الآن **بدون مفاتيح**.

### الخطوة 2: إضافة المفاتيح في AWS Console

#### في AWS App Runner:

1. **أثناء إنشاء Service:**
   - في صفحة "Configure service"
   - scroll لأسفل إلى **"Environment variables"**
   - اضغط **"Add environment variable"**

2. **أضف المتغيرين:**

   **Variable 1:**
   - Key: `TELEGRAM_BOT_TOKEN`
   - Value: `8529682573:AAEiqj1ujm3peulewO_n8KYtaDje_0c1ZAE`

   **Variable 2:**
   - Key: `GEMINI_API_KEY`
   - Value: `AIzaSyBXiQVCJsln1_0EKQ2z2zOkkCLSvWm4XCE`

3. **اضغط "Next" ثم "Create & deploy"**

---

## 🔐 الطريقة الأكثر أماناً: AWS Secrets Manager

### 1. إنشاء Secrets في AWS

```bash
# في AWS CloudShell أو Terminal مع AWS CLI:

aws secretsmanager create-secret \
    --name telegram-bot-token \
    --secret-string "8529682573:AAEiqj1ujm3peulewO_n8KYtaDje_0c1ZAE" \
    --region us-east-1

aws secretsmanager create-secret \
    --name gemini-api-key \
    --secret-string "AIzaSyBXiQVCJsln1_0EKQ2z2zOkkCLSvWm4XCE" \
    --region us-east-1
```

### 2. تعديل telegram_bot.py

أضف في بداية الملف:

```python
import boto3
import json
from botocore.exceptions import ClientError

def get_secret(secret_name, region_name="us-east-1"):
    """Get secret from AWS Secrets Manager"""
    try:
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        return get_secret_value_response['SecretString']
    except ClientError as e:
        logger.error(f"Error getting secret {secret_name}: {e}")
        return None

# استبدل هذه الأسطر:
# TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
# api_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')

# بهذه:
TELEGRAM_TOKEN = get_secret('telegram-bot-token') or os.getenv('TELEGRAM_BOT_TOKEN')
api_key = get_secret('gemini-api-key') or os.getenv('GEMINI_API_KEY')
```

### 3. إضافة boto3 إلى requirements.txt

```
python-telegram-bot==20.7
google-generativeai==0.8.3
python-dotenv==1.0.0
requests==2.32.3
boto3==1.34.0
```

### 4. إعطاء صلاحيات لـ App Runner

في AWS Console:
1. اذهب إلى **IAM**
2. ابحث عن Role: `AppRunnerInstanceRole`
3. أضف Policy: `SecretsManagerReadWrite`

---

## 📋 الخطوات الموصى بها (الأسهل)

### ✅ استخدم AWS Console Environment Variables

**لماذا؟**
1. ✅ سهل - لا تحتاج تعديل كود
2. ✅ آمن - المفاتيح في AWS فقط
3. ✅ سريع - 2 دقائق

**الخطوات:**
1. ارفع `apprunner.yaml` الجديد (بدون مفاتيح) على GitHub
2. في AWS App Runner → Create Service
3. أضف Environment Variables في Console
4. Deploy!

---

## 🔄 تحديث GitHub (مهم!)

### 1. ارفع الملف المحدّث
- `apprunner.yaml` (بدون مفاتيح) ✅

### 2. Commit message:
```
Remove secrets from apprunner.yaml - use AWS Console instead
```

---

## ⚠️ ملاحظة أمنية

**المفاتيح القديمة في GitHub:**
- GitHub حفظ التاريخ (commits القديمة)
- **يُنصح بتغيير المفاتيح:**
  1. أنشئ Bot جديد في BotFather
  2. أنشئ Gemini API key جديد
  3. استخدم المفاتيح الجديدة في AWS

**أو:**
- إذا كان المشروع خاص (private)، لا مشكلة
- إذا كان عام (public)، **غيّر المفاتيح فوراً**

---

## ✅ الخلاصة

**افعل هذا:**
1. ارفع `apprunner.yaml` الجديد (بدون مفاتيح)
2. في AWS Console، أضف Environment Variables يدوياً
3. Deploy!

**المفاتيح الآن آمنة في AWS فقط!** 🔒
