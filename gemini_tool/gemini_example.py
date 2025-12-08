"""
Simple example demonstrating Gemini 2.0 Flash usage with GCP service account.

This script shows:
- Service account authentication
- Vertex AI initialization
- Text generation with Gemini
- Question answering
"""

import json
from google.oauth2 import service_account
import vertexai
from vertexai.generative_models import GenerativeModel


def load_service_account_credentials(key_file_path):
    """
    Load service account credentials from JSON file.
    
    Args:
        key_file_path: Path to the service account JSON key file
        
    Returns:
        Credentials object
    """
    credentials = service_account.Credentials.from_service_account_file(
        key_file_path,
        scopes=['https://www.googleapis.com/auth/cloud-platform']
    )
    return credentials


def initialize_vertex_ai(credentials, project_id, location="us-central1"):
    """
    Initialize Vertex AI with service account credentials.
    
    Args:
        credentials: Service account credentials
        project_id: GCP project ID
        location: GCP region (default: us-central1, where Gemini models are available)
    """
    vertexai.init(
        project=project_id,
        location=location,
        credentials=credentials
    )


def generate_text_with_gemini(prompt):
    """
    Generate text using Gemini Pro model.
    
    Args:
        prompt: The text prompt to send to the model
        
    Returns:
        Generated text response
    """
    # Initialize the Gemini 2.0 Flash model
    model = GenerativeModel("gemini-2.0-flash-001")
    
    # Generate content
    response = model.generate_content(prompt)
    
    return response.text


def main():
    """
    Main function demonstrating Gemini API usage with service account.
    """
    # Configuration
    SERVICE_ACCOUNT_KEY_FILE = "service-account-key.json"
    
    # Load project ID from service account file
    with open(SERVICE_ACCOUNT_KEY_FILE, 'r') as f:
        sa_data = json.load(f)
        PROJECT_ID = sa_data['project_id']
    
    print(f"Loading service account credentials...")
    credentials = load_service_account_credentials(SERVICE_ACCOUNT_KEY_FILE)
    
    print(f"Initializing Vertex AI for project: {PROJECT_ID}")
    initialize_vertex_ai(credentials, PROJECT_ID)
    
    # Example task: Generate a creative story
    print("\n" + "="*60)
    print(" Example Task: Creative Story Generation")
    print("="*60)
    
    prompt = """Write a short, creative story (3-4 sentences) about a robot 
    who discovers it can paint beautiful landscapes."""
    
    print(f"\n Prompt: {prompt}\n")
    print(" Generating response...")
    
    try:
        response = generate_text_with_gemini(prompt)
        print(f"\nGemini Response:\n{response}")
        print("\n" + "="*60)
        print("Success! Gemini model executed successfully.")
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Ensure Vertex AI API is enabled in your GCP project")
        print("2. Verify service account has necessary permissions")
        print("3. Check that the project ID is correct")
        return 1
    
    # Additional example: Simple Q&A
    print("\n" + "="*60)
    print(" Example Task: Question Answering")
    print("="*60)
    
    qa_prompt = "What are the three primary colors? Answer in one sentence."
    print(f"\n Prompt: {qa_prompt}\n")
    print(" Generating response...")
    
    try:
        qa_response = generate_text_with_gemini(qa_prompt)
        print(f"\n Gemini Response:\n{qa_response}")
        print("\n" + "="*60)
        
    except Exception as e:
        print(f"\n Error: {str(e)}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
