"""
Test Google Cloud Vertex AI Connection (English)
"""
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Force configuration for this test
os.environ['USE_VERTEX_AI'] = 'true'
os.environ['GOOGLE_CLOUD_PROJECT'] = 'eg-konecta-sandbox'
os.environ['VERTEX_AI_LOCATION'] = 'us-central1'

# Ensure GOOGLE_APPLICATION_CREDENTIALS is set
if not os.getenv('GOOGLE_APPLICATION_CREDENTIALS'):
    print("⚠️ WARNING: GOOGLE_APPLICATION_CREDENTIALS not found in environment!")
else:
    print(f"🔑 Using Credentials: {os.getenv('GOOGLE_APPLICATION_CREDENTIALS')}")

# Clear any old API keys to ensure we use Vertex AI
if 'GOOGLE_API_KEY' in os.environ: del os.environ['GOOGLE_API_KEY']
if 'GEMINI_API_KEY' in os.environ: del os.environ['GEMINI_API_KEY']

def test_vertex_ai():
    print("\n" + "=" * 60)
    print("🧪 Testing Google Cloud Vertex AI Connection")
    print("=" * 60 + "\n")

    print("📋 Configuration:")
    print(f"   Project:  {os.environ['GOOGLE_CLOUD_PROJECT']}")
    print(f"   Location: {os.environ['VERTEX_AI_LOCATION']}")
    print(f"   Mode:     Vertex AI (Service Account)")
    print("-" * 60)

    try:
        print("\n🔄 Initializing Vertex AI...")
        import vertexai
        from vertexai.preview.generative_models import GenerativeModel
        
        # Initialize Vertex AI
        vertexai.init(
            project=os.environ['GOOGLE_CLOUD_PROJECT'],
            location=os.environ['VERTEX_AI_LOCATION']
        )
        print("✅ Vertex AI Initialized successfully!")

        print("\n🤖 Creating Gemini Model...")
        # Using specific version 001
        model = GenerativeModel("gemini-1.5-flash-001")
        print("✅ Model created!")

        print("\n💬 Sending test prompt: 'Say Hello in English'...")
        response = model.generate_content("Say Hello in English")
        
        print("\n" + "=" * 60)
        print("📥 RESPONSE FROM VERTEX AI:")
        print("-" * 60)
        print(f"{response.text.strip()}")
        print("-" * 60)
        print("✅ SUCCESS! Your Service Account setup is working perfectly.")
        print("=" * 60 + "\n")
        return True

    except Exception as e:
        print("\n❌ ERROR:")
        print(f"{str(e)}")
        print("\n💡 Troubleshooting:")
        print("1. Ensure you ran: gcloud auth application-default login")
        print("2. Ensure the API 'aiplatform.googleapis.com' is enabled in Console")
        print("3. Ensure your account has 'Vertex AI User' role")
        return False

if __name__ == "__main__":
    test_vertex_ai()
