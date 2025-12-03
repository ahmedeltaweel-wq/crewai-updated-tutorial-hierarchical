# ✅ WhatsApp Bot - Quick Start

## المشكلة والحل:
- ❌ **المشكلة:** CrewAI يتطلب Microsoft Visual C++ Build Tools (ثقيل جداً)
- ✅ **الحل:** تبسيط النظام لاستخدام Gemini API مباشرة

## التشغيل السريع:

### 1️⃣ تأكد أن مفتاح Gemini موجود في `.env`:
```
GEMINI_API_KEY=your_key_here
```

### 2️⃣ شغّل البوت:

**الطريقة الأسهل - من File Explorer:**
- دبل كليك على `run_whatsapp_bot.bat`

**من Terminal:**
```bash
cd "c:\Users\Ahmed\OneDrive - Konecta\Documents\mcp\New folder\crewai-updated-tutorial-hierarchical"
.\run_whatsapp_bot.bat
```

### 3️⃣ امسح QR Code:
- ستفتح نافذتان
- في نافذة WhatsApp Handler سيظهر QR Code
- افتح واتساب → الإعدادات → الأجهزة المرتبطة
- امسح الكود

### 4️⃣ اختبر البوت:
أرسل للبوت:
- `مرحبا` (عربي)
- `hello` (English)
- `تغطية` أو `coverage`
- أي سؤال عن التأمين الصحي!

## الفرق الآن:
- ✅ **أخف:** بدون CrewAI والمكتبات الثقيلة
- ✅ **أسهل:** بدون حاجة لـ Visual C++ Build Tools
- ✅ **نفس الوظائف:** Gemini AI مباشرة، نفس الذكاء!

## إذا واجهت مشكلة:
1. تأكد من مفتاح Gemini في `.env`
2. تأكد من تثبيت Node.js
3. شاهد الأخطاء في `whatsapp_bot.log`
