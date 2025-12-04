# 🚨 طلب عاجل جداً من Omar - Deployment Blocked

## 👋 مرحباً Omar،

أنا أحاول عمل Deployment لتطبيق CrewAI (Telegram Bot) على Cloud Run، لكنني **متوقف تماماً** بسبب مشاكل في الصلاحيات والحسابات.

حاولت طريقتين وفشلتا:

### 1. المحاولة الأولى: Deployment عبر GitHub (Cloud Build Trigger)
**النتيجة:** فشل.
**السبب:** حساب الخدمة الافتراضي **Default Compute Engine Service Account** محذوف أو غير موجود.
**الخطأ:**
```
ERROR: Build service account projects/112458895076/serviceAccounts/112458895076-compute@developer.gserviceaccount.com does not exist.
```

### 2. المحاولة الثانية: Deployment يدوي (gcloud CLI)
**النتيجة:** فشل.
**السبب:** حسابي الشخصي (`ahmed.eltaweel@konecta.com`) ليس لديه صلاحية الكتابة في Storage Bucket الخاص بـ Cloud Build.
**الخطأ:**
```
ERROR: The user is forbidden from accessing the bucket [eg-konecta-sandbox_cloudbuild].
```

---

## ✅ الحل المطلوب (يرجى تنفيذ واحد منها)

### الخيار الأفضل: إصلاح Default Service Account 🌟
يرجى استعادة أو إعادة إنشاء حساب الخدمة الافتراضي:
`112458895076-compute@developer.gserviceaccount.com`
ومنحه صلاحيات `Cloud Build Service Account`.

### الخيار البديل: منح صلاحيات لحسابي
منح حسابي `ahmed.eltaweel@konecta.com` الصلاحيات التالية:
- `roles/storage.admin` (لرفع الكود)
- `roles/cloudbuild.builds.editor` (لإنشاء Build)
- `roles/iam.serviceAccountUser` (لاستخدام sa-vertex)

---

بدون هذه الإصلاحات، لا يمكنني رفع أي كود على المشروع.

شكراً لتفهمك! 🙏
Ahmed
