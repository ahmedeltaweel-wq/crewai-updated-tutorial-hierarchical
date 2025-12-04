"""
List Available Vertex AI Models
"""
import os
from google.cloud import aiplatform
from dotenv import load_dotenv

load_dotenv()

if os.getenv('GOOGLE_APPLICATION_CREDENTIALS'):
    print(f"🔑 Using Credentials: {os.getenv('GOOGLE_APPLICATION_CREDENTIALS')}")
else:
    print("⚠️ WARNING: GOOGLE_APPLICATION_CREDENTIALS not found!")

# Configuration
PROJECT_ID = "eg-konecta-sandbox"
LOCATION = "us-central1"

def list_models():
    print("\n" + "=" * 60)
    print("📋 Listing Available Vertex AI Models")
    print("=" * 60 + "\n")
    
    try:
        aiplatform.init(project=PROJECT_ID, location=LOCATION)
        
        # List all models
        print(f"🔍 Searching in project: {PROJECT_ID}, location: {LOCATION}...")
        
        from vertexai.preview.generative_models import GenerativeModel
        import vertexai
        vertexai.init(project=PROJECT_ID, location=LOCATION)
        
        # List actual models from the API
        print(f"🔍 Fetching available models from Vertex AI API...")
        
        # Use the Model Garden listing
        from google.cloud import aiplatform
        
        # This lists custom models, but let's try to list publisher models if possible
        # or just try to generate with a very simple prompt to test availability
        
        test_models = [
            "gemini-1.5-flash-001",
            "gemini-1.5-flash",
            "gemini-1.0-pro",
            "gemini-1.0-pro-001"
        ]
        
        print("\n🧪 Testing actual generation (True Availability):")
        for model_name in test_models:
            try:
                print(f"   Testing {model_name}...", end=" ", flush=True)
                model = GenerativeModel(model_name)
                # Try a minimal generation to confirm access
                response = model.generate_content("Hi")
                print(f"✅ Working!")
            except Exception as e:
                print(f"❌ Failed")
                # print(f"      Error: {e}") # Uncomment for details

    except Exception as e:
        print(f"\n❌ Error initializing Vertex AI: {e}")

if __name__ == "__main__":
    list_models()
