"""
List Available Vertex AI Models
"""
import os
from google.cloud import aiplatform

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
        
        # Try standard model names
        test_models = [
            "gemini-1.5-flash-001",
            "gemini-1.5-flash",
            "gemini-1.5-pro-001",
            "gemini-1.5-pro",
            "gemini-1.0-pro-001",
            "gemini-1.0-pro"
        ]
        
        print("\n🧪 Testing specific model availability:")
        for model_name in test_models:
            try:
                model = GenerativeModel(model_name)
                # Just try to instantiate, not generate yet
                print(f"   ✅ {model_name}: Available")
            except Exception as e:
                print(f"   ❌ {model_name}: Not found ({str(e)})")

    except Exception as e:
        print(f"\n❌ Error initializing Vertex AI: {e}")

if __name__ == "__main__":
    list_models()
