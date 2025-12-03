"""
اختبار سريع لـ Gemini API مع Application Default Credentials
"""
import os
from dotenv import load_dotenv

load_dotenv()

def test_gemini_simple():
    """اختبار بسيط لـ Gemini"""
    
    print("\n" + "=" * 60)
    print("🧪 اختبار Gemini API")
    print("=" * 60 + "\n")
    
    try:
        import google.generativeai as genai
        
        # محاولة استخدام API Key أولاً
        api_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
        
        if api_key:
            print(f"✅ تم العثور على API Key: {api_key[:20]}...")
            genai.configure(api_key=api_key)
        else:
            print("ℹ️  لم يتم العثور على API Key")
            print("   سيتم استخدام Application Default Credentials")
        
        print("\n🔄 جاري إنشاء Gemini model...")
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        print("✅ Model تم إنشاؤه بنجاح!")
        
        print("\n🧪 جاري اختبار استجابة بسيطة...")
        response = model.generate_content("قل مرحبا بالعربية في جملة واحدة")
        
        print(f"\n💬 الاستجابة من Gemini:")
        print(f"   {response.text}")
        
        print("\n" + "=" * 60)
        print("✅ Gemini API يعمل بنجاح!")
        print("=" * 60)
        
        return True
        
    except Exception as e:
        print(f"\n❌ خطأ: {e}")
        print("\n" + "=" * 60)
        
        error_str = str(e).lower()
        
        if 'api key' in error_str or 'invalid' in error_str:
            print("💡 الحل:")
            print("   1. أضف GOOGLE_API_KEY إلى ملف .env")
            print("   2. أو استخدم: gcloud auth application-default login")
            
        elif 'quota' in error_str or 'resource_exhausted' in error_str:
            print("💡 الحل:")
            print("   1. انتظر دقيقة (Rate Limit)")
            print("   2. أو جرب model آخر: gemini-1.5-flash")
            
        else:
            print("💡 تحقق من:")
            print("   1. الاتصال بالإنترنت")
            print("   2. تفعيل Generative Language API")
        
        print("=" * 60)
        
        return False

if __name__ == "__main__":
    test_gemini_simple()
