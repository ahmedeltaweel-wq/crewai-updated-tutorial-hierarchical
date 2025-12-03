"""
اختبار بسيط لـ Gemini API باستخدام API Key
"""
import os
from dotenv import load_dotenv

# تحميل متغيرات البيئة
load_dotenv()

def test_gemini_api_key():
    """اختبار Gemini API Key"""
    
    print("\n" + "=" * 60)
    print("🔑 اختبار Gemini API Key")
    print("=" * 60 + "\n")
    
    # فحص API Key
    api_key = os.getenv('GOOGLE_API_KEY') or os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        print("❌ لم يتم العثور على API Key في .env")
        print("\n📋 الخطوات المطلوبة:")
        print("1. افتح: https://aistudio.google.com/app/apikey")
        print("2. اضغط 'Create API Key'")
        print("3. اختر المشروع: eg-konecta-sandbox")
        print("4. انسخ المفتاح")
        print("5. أضف إلى .env:")
        print("   GOOGLE_API_KEY=your-api-key-here")
        return False
    
    print(f"✅ تم العثور على API Key: {api_key[:20]}...")
    
    # اختبار الاتصال
    try:
        print("\n🔌 جاري اختبار الاتصال مع Gemini...")
        
        from langchain_google_genai import ChatGoogleGenerativeAI
        
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-exp",
            temperature=0.7,
            google_api_key=api_key
        )
        
        print("✅ تم إنشاء Gemini model بنجاح!")
        
        # اختبار استجابة بسيطة
        print("\n🧪 جاري اختبار استجابة بسيطة...")
        response = llm.invoke("قل مرحبا بالعربية في جملة واحدة")
        
        print(f"\n💬 الاستجابة من Gemini:")
        print(f"   {response.content}")
        
        print("\n✅ جميع الاختبارات نجحت!")
        print("\n📊 معلومات:")
        print(f"   🤖 Model: gemini-2.0-flash-exp")
        print(f"   🔑 API Key: {api_key[:10]}...{api_key[-4:]}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ خطأ في الاتصال: {e}")
        
        error_str = str(e).lower()
        
        if 'invalid' in error_str or 'api key' in error_str:
            print("\n💡 الحل:")
            print("   1. تأكد من نسخ API Key كاملاً")
            print("   2. تأكد من عدم وجود مسافات في البداية أو النهاية")
            print("   3. جرب إنشاء API Key جديد")
            
        elif 'quota' in error_str or 'resource_exhausted' in error_str:
            print("\n💡 الحل:")
            print("   1. انتظر دقيقة واحدة (Rate Limit)")
            print("   2. جرب model آخر: gemini-1.5-flash")
            print("   3. تحقق من Quota: https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/quotas")
            
        else:
            print("\n💡 تحقق من:")
            print("   1. الاتصال بالإنترنت")
            print("   2. تفعيل Generative Language API")
            print("   3. صلاحيات المشروع")
        
        return False

def show_available_models():
    """عرض Models المتاحة"""
    
    print("\n" + "=" * 60)
    print("📋 Gemini Models المتاحة")
    print("=" * 60 + "\n")
    
    models = [
        {
            'name': 'gemini-2.0-flash-exp',
            'description': 'أحدث وأسرع model (تجريبي)',
            'rpm': '15',
            'tpm': '1,000,000'
        },
        {
            'name': 'gemini-1.5-flash',
            'description': 'سريع ومستقر',
            'rpm': '15',
            'tpm': '1,000,000'
        },
        {
            'name': 'gemini-1.5-pro',
            'description': 'الأقوى (أبطأ)',
            'rpm': '2',
            'tpm': '32,000'
        }
    ]
    
    for model in models:
        print(f"🤖 {model['name']}")
        print(f"   📝 {model['description']}")
        print(f"   ⚡ Rate Limits: {model['rpm']} req/min, {model['tpm']} tokens/min")
        print()

if __name__ == "__main__":
    # اختبار API Key
    success = test_gemini_api_key()
    
    if success:
        # عرض Models المتاحة
        show_available_models()
        
        print("=" * 60)
        print("✅ كل شيء جاهز! يمكنك الآن استخدام تطبيقاتك")
        print("=" * 60 + "\n")
    else:
        print("\n" + "=" * 60)
        print("❌ يرجى إصلاح المشاكل أعلاه ثم إعادة المحاولة")
        print("=" * 60 + "\n")
