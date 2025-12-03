# Deploy Telegram Bot to AWS - خطوة بخطوة

## ما تحتاجه
- ✅ حساب AWS (عندك بالفعل)
- ✅ GitHub repository مع Dockerfile (رفعته بالفعل ✅)
- ✅ Bot token و Gemini API key

---

## الطريقة 1: AWS App Runner (الأسهل - موصى بها)

### الخطوة 1: افتح AWS Console (دقيقة واحدة)

1. اذهب إلى: https://console.aws.amazon.com
2. سجل دخول
3. في شريط البحث (أعلى الصفحة)، اكتب: **App Runner**
4. اضغط على **"App Runner"**

### الخطوة 2: إنشاء Service (3 دقائق)

#### 2.1 Create Service
1. اضغط **"Create service"**
2. اختر **"Source code repository"**
3. اضغط **"Add new"** لربط GitHub

#### 2.2 ربط GitHub
1. اختر **"GitHub"**
2. اضغط **"Install another"** أو **"Manage connections"**
3. وافق على ربط GitHub مع AWS
4. اختر repository: **telegram-health-bot**
5. Branch: **main**
6. اضغط **"Next"**

#### 2.3 Build Settings
- **Deployment trigger:** Automatic ✅
- **Build configuration:** Use configuration file
- اضغ **"Next"**

### الخطوة 3: Service Settings (2 دقائق)

#### 3.1 Service Name
- **Service name:** `telegram-health-bot`

#### 3.2 Environment Variables
اضغط **"Add environment variable"** مرتين:

**Variable 1:**
- Key: `TELEGRAM_BOT_TOKEN`
- Value: `8529682573:AAEiqj1ujm3peulewO_n8KYtaDje_0c1ZAE`

**Variable 2:**
- Key: `GEMINI_API_KEY`
- Value: `AIzaSyBXiQVCJsln1_0EKQ2z2zOkkCLSvWm4XCE`

#### 3.3 Instance Configuration
- **CPU:** 1 vCPU
- **Memory:** 2 GB
- **Port:** 8080 (افتراضي)

#### 3.4 Auto Scaling
- **Min instances:** 1
- **Max instances:** 1

اضغط **"Next"**

### الخطوة 4: Review & Create

1. راجع الإعدادات
2. اضغ **"Create & deploy"**
3. انتظر 3-5 دقائق

---

## الطريقة 2: AWS ECS Fargate (أكثر تحكماً)

### الخطوة 1: إنشاء ECR Repository

1. ابحث عن: **ECR** (Elastic Container Registry)
2. اضغط **"Create repository"**
3. اسم Repository: `telegram-health-bot`
4. اضغط **"Create repository"**

### الخطوة 2: رفع Docker Image

#### 2.1 في جهازك، افتح Terminal:

```bash
# تسجيل دخول AWS
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com

# بناء Image
cd "c:\Users\Ahmed\OneDrive - Konecta\Documents\mcp\New folder\crewai-updated-tutorial-hierarchical"
docker build -t telegram-health-bot .

# Tag Image
docker tag telegram-health-bot:latest YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/telegram-health-bot:latest

# رفع Image
docker push YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/telegram-health-bot:latest
```

### الخطوة 3: إنشاء ECS Task

1. ابحث عن: **ECS**
2. اضغط **"Task Definitions"** → **"Create new Task Definition"**
3. اختر **"Fargate"**
4. Task name: `telegram-health-bot`
5. Container:
   - Name: `bot`
   - Image: `YOUR_ACCOUNT_ID.dkr.ecr.us-east-1.amazonaws.com/telegram-health-bot:latest`
   - Memory: 512 MB
   - Environment Variables: أضف TELEGRAM_BOT_TOKEN و GEMINI_API_KEY

### الخطوة 4: إنشاء Service

1. في ECS، اضغط **"Clusters"** → **"Create Cluster"**
2. اختر **"Networking only"** (Fargate)
3. Cluster name: `telegram-bot-cluster`
4. اضغط **"Create Service"**
5. اختر Task Definition
6. Service name: `telegram-health-bot`
7. Number of tasks: 1
8. اضغط **"Create Service"**

---

## الطريقة 3: AWS Lambda (الأوفر - لكن معقدة)

**ملحوظة:** Lambda ليست مثالية للـ Telegram bots لأنها تحتاج webhook بدلاً من polling.

---

## التوصية: استخدم App Runner ⭐

**لماذا App Runner؟**
- ✅ **الأسهل:** ربط GitHub مباشرة
- ✅ **Auto-deploy:** أي تغيير في GitHub ينشر تلقائياً
- ✅ **Always-on:** يعمل 24/7
- ✅ **Managed:** AWS تدير كل شيء
- ✅ **Free Tier:** 2000 build minutes مجاناً

---

## التكلفة المتوقعة

### App Runner:
- **Compute:** ~$5-7/شهر (1 vCPU, 2GB RAM)
- **Build:** مجاني (Free Tier)
- **إجمالي:** ~$5-7/شهر

### ECS Fargate:
- **Compute:** ~$8-10/شهر
- **Data transfer:** ~$1/شهر
- **إجمالي:** ~$9-11/شهر

---

## التحقق من النجاح

### في AWS Console:
1. افتح App Runner service
2. اضغط تبويب **"Logs"**
3. ابحث عن:
```
✅ Bot is ready!
🤖 You can now send messages to your bot on Telegram
```

### في Telegram:
1. ابحث عن: `@My_konecta_bot`
2. أرسل: **"مرحبا"**
3. البوت يرد! 🎉

---

## تحديث البوت

**لتحديث أي ملف:**
1. عدّل في GitHub
2. Commit changes
3. App Runner ينشر تلقائياً (2-3 دقائق)
4. البوت محدّث! ✅

---

## Troubleshooting

### البوت لا يرد؟
1. تحقق من Logs في App Runner
2. تأكد من Environment Variables صحيحة
3. تأكد من Service في حالة "Running"

### Deployment فشل؟
1. تحقق من `Dockerfile` في GitHub
2. تحقق من `requirements.txt`
3. شاهد Build logs

---

## ملف إضافي مطلوب: apprunner.yaml (اختياري)

إذا أردت تخصيص App Runner، أنشئ ملف `apprunner.yaml` في GitHub:

```yaml
version: 1.0
runtime: python3
build:
  commands:
    build:
      - pip install -r requirements.txt
run:
  command: python telegram_bot.py
  network:
    port: 8080
  env:
    - name: TELEGRAM_BOT_TOKEN
      value: ""
    - name: GEMINI_API_KEY
      value: ""
```

---

## 🎉 تم! البوت الآن على AWS!

**رابط Service:** سيظهر في App Runner Console
**رابط البوت:** https://t.me/My_konecta_bot

**استمتع! 🚀**
