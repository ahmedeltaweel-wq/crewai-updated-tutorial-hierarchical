"""
Gemini example using direct REST API calls with service account.

This approach provides:
- More control over API parameters
- Direct HTTP request/response handling
- Useful for debugging or custom integrations
"""

import json
import requests
from google.oauth2 import service_account
import google.auth.transport.requests


def get_access_token(service_account_file):
    """Get an access token from service account credentials."""
    credentials = service_account.Credentials.from_service_account_file(
        service_account_file,
        scopes=['https://www.googleapis.com/auth/cloud-platform']
    )
    
    # Refresh to get an access token
    auth_req = google.auth.transport.requests.Request()
    credentials.refresh(auth_req)
    
    return credentials.token


def call_gemini_api(access_token, project_id, prompt, location="us-central1"):
    """
    Call Gemini API using REST endpoint.
    
    Args:
        access_token: OAuth access token
        project_id: GCP project ID
        prompt: Text prompt for Gemini
        location: GCP region
        
    Returns:
        Generated text response
    """
    # Gemini API endpoint
    url = f"https://{location}-aiplatform.googleapis.com/v1/projects/{project_id}/locations/{location}/publishers/google/models/gemini-2.0-flash-001:generateContent"
    
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "contents": [{
            "role": "user",
            "parts": [{"text": prompt}]
        }],
        "generation_config": {
            "temperature": 0.7,
            "maxOutputTokens": 1024,
            "topP": 0.95,
            "topK": 40
        }
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        if 'candidates' in result and len(result['candidates']) > 0:
            return result['candidates'][0]['content']['parts'][0]['text']
        else:
            return "No response generated"
    else:
        raise Exception(f"API Error {response.status_code}: {response.text}")


def main():
    """Main function demonstrating Gemini API usage with service account."""
    SERVICE_ACCOUNT_KEY_FILE = "service-account-key.json"
    
    # Load project ID
    with open(SERVICE_ACCOUNT_KEY_FILE, 'r') as f:
        sa_data = json.load(f)
        PROJECT_ID = sa_data['project_id']
    
    print(f"🔐 Loading service account credentials...")
    access_token = get_access_token(SERVICE_ACCOUNT_KEY_FILE)
    print(f"✅ Access token obtained")
    
    print(f"🚀 Calling Gemini API for project: {PROJECT_ID}\n")
    
    # Example 1: Creative Story Generation
    print("="*60)
    print("📝 Example 1: Creative Story Generation")
    print("="*60)
    
    prompt1 = "Write a short, creative story (3-4 sentences) about a robot who discovers it can paint beautiful landscapes."
    print(f"\n💭 Prompt: {prompt1}\n")
    print("⏳ Generating response...")
    
    try:
        response1 = call_gemini_api(access_token, PROJECT_ID, prompt1)
        print(f"\n🤖 Gemini Response:\n{response1}")
        print("\n" + "="*60)
        print("✅ Success!")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nTrying alternative region...")
        
        # Try europe-west1 as alternative
        try:
            response1 = call_gemini_api(access_token, PROJECT_ID, prompt1, location="europe-west1")
            print(f"\n🤖 Gemini Response:\n{response1}")
            print("\n" + "="*60)
            print("✅ Success with europe-west1 region!")
        except Exception as e2:
            print(f"❌ Also failed with europe-west1: {str(e2)}")
            return 1
    
    # Example 2: Question Answering
    print("\n" + "="*60)
    print("❓ Example 2: Question Answering")
    print("="*60)
    
    prompt2 = "What are the three primary colors? Answer in one concise sentence."
    print(f"\n💭 Prompt: {prompt2}\n")
    print("⏳ Generating response...")
    
    try:
        response2 = call_gemini_api(access_token, PROJECT_ID, prompt2)
        print(f"\n🤖 Gemini Response:\n{response2}")
        print("\n" + "="*60)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return 1
    
    # Example 3: Code Generation
    print("\n" + "="*60)
    print("💻 Example 3: Simple Code Generation")
    print("="*60)
    
    prompt3 = "Write a Python function that calculates the factorial of a number. Include docstring."
    print(f"\n💭 Prompt: {prompt3}\n")
    print("⏳ Generating response...")
    
    try:
        response3 = call_gemini_api(access_token, PROJECT_ID, prompt3)
        print(f"\n🤖 Gemini Response:\n{response3}")
        print("\n" + "="*60)
        print("✅ All examples completed successfully!")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
