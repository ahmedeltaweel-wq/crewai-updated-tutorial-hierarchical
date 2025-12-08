"""
Test which Vertex AI models are available in the project
"""
import os

# Set project info
os.environ["GOOGLE_CLOUD_PROJECT"] = "eg-konecta-sandbox"

def test_vertex_models():
    """Test available Vertex AI models"""
    
    print("=" * 60)
    print("🔍 Testing Vertex AI Models Availability")
    print("=" * 60)
    
    try:
        import vertexai
        from vertexai.generative_models import GenerativeModel
        
        project_id = os.environ.get("GOOGLE_CLOUD_PROJECT", "eg-konecta-sandbox")
        location = "us-central1"
        
        print(f"\n📌 Project: {project_id}")
        print(f"📍 Location: {location}")
        
        vertexai.init(project=project_id, location=location)
        
        # Models to test
        models_to_test = [
            "gemini-1.5-flash-001",
            "gemini-1.5-flash",
            "gemini-1.5-pro-001", 
            "gemini-1.5-pro",
            "gemini-1.0-pro-001",
            "gemini-1.0-pro",
            "gemini-pro",
            "gemini-2.0-flash-exp",
        ]
        
        working_models = []
        
        print("\n🔄 Testing models...\n")
        
        for model_name in models_to_test:
            try:
                print(f"Testing: {model_name}...", end=" ")
                model = GenerativeModel(model_name)
                response = model.generate_content("Say 'Hello' in one word")
                print(f"✅ WORKS! Response: {response.text[:50]}...")
                working_models.append(model_name)
            except Exception as e:
                error_msg = str(e)[:80]
                print(f"❌ FAILED: {error_msg}")
        
        print("\n" + "=" * 60)
        print("📊 SUMMARY")
        print("=" * 60)
        
        if working_models:
            print(f"\n✅ Working models ({len(working_models)}):")
            for m in working_models:
                print(f"   - {m}")
            print(f"\n💡 Use this in your code: vertex_ai/{working_models[0]}")
        else:
            print("\n❌ No Vertex AI models available!")
            print("   You need to use Gemini API Key instead.")
        
        return working_models
        
    except ImportError:
        print("❌ vertexai not installed. Run: pip install google-cloud-aiplatform")
        return []
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

if __name__ == "__main__":
    # Install required package if needed
    try:
        import vertexai
    except ImportError:
        print("Installing google-cloud-aiplatform...")
        import subprocess
        subprocess.check_call(["pip", "install", "google-cloud-aiplatform", "-q"])
    
    working = test_vertex_models()
