"""
اختبار Service Account للتأكد من عمله بشكل صحيح
"""
import os
from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()

def test_service_account():
    """اختبار Service Account credentials"""
    
    print("🔍 جاري فحص Service Account...")
    print("-" * 50)
    
    # فحص متغير البيئة
    creds_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    
    if not creds_path:
        print("⚠️  متغير GOOGLE_APPLICATION_CREDENTIALS غير موجود في .env")
        print("📝 جاري البحث عن service-account-key.json...")
        
        # البحث عن الملف في المجلد الحالي
        if os.path.exists('service-account-key.json'):
            creds_path = 'service-account-key.json'
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = creds_path
            print(f"✅ تم العثور على الملف: {creds_path}")
        else:
            print("❌ لم يتم العثور على ملف service-account-key.json")
            print("\n📋 الخطوات المطلوبة:")
            print("1. قم بتنزيل JSON key من Google Cloud Console")
            print("2. ضعه في مجلد المشروع باسم: service-account-key.json")
            print("3. أضف إلى .env: GOOGLE_APPLICATION_CREDENTIALS=service-account-key.json")
            return False
    else:
        print(f"✅ متغير البيئة موجود: {creds_path}")
    
    # فحص وجود الملف
    if not os.path.exists(creds_path):
        print(f"❌ الملف غير موجود: {creds_path}")
        return False
    
    print(f"✅ الملف موجود: {creds_path}")
    
    # محاولة قراءة الملف
    try:
        import json
        with open(creds_path, 'r') as f:
            creds_data = json.load(f)
        
        print("\n📊 معلومات Service Account:")
        print(f"   📧 Email: {creds_data.get('client_email', 'N/A')}")
        print(f"   🆔 Project ID: {creds_data.get('project_id', 'N/A')}")
        print(f"   🔑 Type: {creds_data.get('type', 'N/A')}")
        
    except Exception as e:
        print(f"⚠️  خطأ في قراءة الملف: {e}")
        return False
    
    # اختبار الاتصال مع Google Cloud
    try:
        print("\n🔌 جاري اختبار الاتصال مع Google Cloud...")
        from google.oauth2 import service_account
        from google.auth.transport.requests import Request
        
        credentials = service_account.Credentials.from_service_account_file(
            creds_path,
            scopes=['https://www.googleapis.com/auth/cloud-platform']
        )
        
        # محاولة refresh للتأكد من صحة credentials
        credentials.refresh(Request())
        
        print("✅ الاتصال ناجح!")
        print(f"   📧 Service Account: {credentials.service_account_email}")
        
        # اختبار Vertex AI
        try:
            print("\n🤖 جاري اختبار Vertex AI...")
            from google.cloud import aiplatform
            
            aiplatform.init(
                project=creds_data.get('project_id'),
                credentials=credentials
            )
            
            print("✅ Vertex AI جاهز للاستخدام!")
            
        except Exception as e:
            print(f"⚠️  تحذير Vertex AI: {e}")
            print("   (قد تحتاج إلى تفعيل Vertex AI API)")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في الاتصال: {e}")
        print("\n💡 تأكد من:")
        print("   1. Service Account لديه صلاحيات Vertex AI User")
        print("   2. Vertex AI API مفعّل في المشروع")
        return False

def test_gemini_api():
    """اختبار Gemini API مع Service Account"""
    
    print("\n" + "=" * 50)
    print("🧪 اختبار Gemini API")
    print("=" * 50)
    
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        
        print("🔄 جاري إنشاء Gemini model...")
        
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-exp",
            temperature=0.7
        )
        
        print("✅ Gemini model تم إنشاؤه بنجاح!")
        
        # اختبار بسيط
        print("🧪 جاري اختبار استجابة بسيطة...")
        response = llm.invoke("قل مرحبا")
        
        print(f"✅ الاستجابة: {response.content}")
        
        return True
        
    except Exception as e:
        print(f"❌ خطأ في Gemini API: {e}")
        return False

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("🔐 اختبار Google Cloud Service Account")
    print("=" * 50 + "\n")
    
    # اختبار Service Account
    if test_service_account():
        print("\n✅ جميع الاختبارات نجحت!")
        
        # اختبار Gemini (اختياري)
        try:
            test_gemini_api()
        except Exception as e:
            print(f"\n⚠️  تخطي اختبار Gemini: {e}")
    else:
        print("\n❌ فشل الاختبار - راجع الخطوات أعلاه")
    
    print("\n" + "=" * 50)
