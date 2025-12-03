"""
اختبار Application Default Credentials من gcloud
"""
import os

def test_gcloud_auth():
    """اختبار المصادقة عبر gcloud"""
    
    print("\n" + "=" * 60)
    print("🔐 اختبار Google Cloud Authentication")
    print("=" * 60 + "\n")
    
    # فحص Application Default Credentials
    print("🔍 جاري فحص Application Default Credentials...")
    
    try:
        import google.auth
        from google.auth import default
        
        # الحصول على credentials
        credentials, project = default()
        
        print(f"✅ تم العثور على credentials!")
        print(f"   🆔 Project: {project}")
        
        # فحص نوع credentials
        print(f"   🔑 Type: {type(credentials).__name__}")
        
        # اختبار refresh
        print("\n🔌 جاري اختبار الاتصال...")
        from google.auth.transport.requests import Request
        
        if not credentials.valid:
            credentials.refresh(Request())
        
        print("✅ الاتصال ناجح!")
        
        # عرض معلومات إضافية
        if hasattr(credentials, 'service_account_email'):
            print(f"   📧 Service Account: {credentials.service_account_email}")
        
        return True, credentials, project
        
    except Exception as e:
        print(f"❌ خطأ: {e}")
        print("\n📋 الخطوات المطلوبة:")
        print("1. ثبّت Google Cloud SDK:")
        print("   https://cloud.google.com/sdk/docs/install")
        print("\n2. سجل الدخول:")
        print("   gcloud auth login")
        print("\n3. عيّن المشروع:")
        print("   gcloud config set project eg-konecta-sandbox")
        print("\n4. إعداد Application Default Credentials:")
        print("   gcloud auth application-default login")
        
        return False, None, None

def test_vertex_ai(credentials, project):
    """اختبار Vertex AI"""
    
    print("\n" + "=" * 60)
    print("🤖 اختبار Vertex AI")
    print("=" * 60 + "\n")
    
    try:
        from google.cloud import aiplatform
        
        print("🔄 جاري تهيئة Vertex AI...")
        
        aiplatform.init(
            project=project,
            credentials=credentials,
            location='us-central1'
        )
        
        print("✅ Vertex AI جاهز!")
        print(f"   🆔 Project: {project}")
        print(f"   📍 Location: us-central1")
        
        return True
        
    except Exception as e:
        print(f"⚠️  خطأ في Vertex AI: {e}")
        print("\n💡 قد تحتاج إلى:")
        print("1. تفعيل Vertex AI API:")
        print("   https://console.cloud.google.com/apis/library/aiplatform.googleapis.com")
        print("\n2. التأكد من صلاحيات Service Account")
        
        return False

def test_gemini_with_gcloud():
    """اختبار Gemini مع gcloud credentials"""
    
    print("\n" + "=" * 60)
    print("💬 اختبار Gemini API")
    print("=" * 60 + "\n")
    
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        
        print("🔄 جاري إنشاء Gemini model...")
        
        # سيستخدم Application Default Credentials تلقائياً
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-exp",
            temperature=0.7
        )
        
        print("✅ Gemini model تم إنشاؤه!")
        
        # اختبار استجابة بسيطة
        print("\n🧪 جاري اختبار استجابة...")
        response = llm.invoke("قل مرحبا بالعربية في جملة واحدة")
        
        print(f"\n💬 الاستجابة:")
        print(f"   {response.content}")
        
        print("\n✅ Gemini يعمل بنجاح مع gcloud credentials!")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ: {e}")
        
        error_str = str(e).lower()
        
        if 'api key' in error_str or 'credentials' in error_str:
            print("\n💡 الحل:")
            print("   قد تحتاج إلى استخدام GOOGLE_API_KEY بدلاً من ذلك")
            print("   أو استخدام Vertex AI API بدلاً من Gemini API")
        
        return False

def show_gcloud_info():
    """عرض معلومات gcloud الحالية"""
    
    print("\n" + "=" * 60)
    print("ℹ️  معلومات gcloud")
    print("=" * 60 + "\n")
    
    import subprocess
    
    commands = [
        ("gcloud --version", "إصدار gcloud"),
        ("gcloud config get-value project", "المشروع الحالي"),
        ("gcloud auth list", "الحسابات المصادق عليها"),
    ]
    
    for cmd, description in commands:
        try:
            print(f"📋 {description}:")
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=5
            )
            
            if result.returncode == 0:
                output = result.stdout.strip()
                if output:
                    for line in output.split('\n')[:5]:  # أول 5 أسطر فقط
                        print(f"   {line}")
            else:
                print(f"   ⚠️  {result.stderr.strip()}")
            
            print()
            
        except Exception as e:
            print(f"   ⚠️  خطأ: {e}\n")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🔐 اختبار Google Cloud Authentication عبر gcloud")
    print("=" * 60)
    
    # عرض معلومات gcloud
    show_gcloud_info()
    
    # اختبار Application Default Credentials
    success, credentials, project = test_gcloud_auth()
    
    if success:
        # اختبار Vertex AI
        test_vertex_ai(credentials, project)
        
        # اختبار Gemini
        test_gemini_with_gcloud()
        
        print("\n" + "=" * 60)
        print("✅ جميع الاختبارات اكتملت!")
        print("=" * 60)
        print("\n💡 يمكنك الآن استخدام تطبيقاتك:")
        print("   python telegram_bot.py")
        print("   python electric_web_app.py")
        print("   python web_app.py")
        
    else:
        print("\n" + "=" * 60)
        print("❌ يرجى إكمال إعداد gcloud أولاً")
        print("=" * 60)
        print("\n📖 راجع الدليل: GCLOUD_AUTH_SETUP.md")
    
    print()
