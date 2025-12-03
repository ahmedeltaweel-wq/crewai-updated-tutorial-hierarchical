import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    print("Error: GOOGLE_API_KEY not found in .env file")
    exit(1)

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"

try:
    response = requests.get(url)
    if response.status_code == 200:
        models = response.json().get('models', [])
        print("\nAvailable Models:")
        print("-" * 50)
        for model in models:
            if 'generateContent' in model.get('supportedGenerationMethods', []):
                print(f"Name: {model['name']}")
                print(f"Display Name: {model.get('displayName')}")
                print("-" * 50)
    else:
        print(f"Error: {response.status_code} - {response.text}")
except Exception as e:
    print(f"An error occurred: {e}")
