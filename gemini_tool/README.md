# Gemini API with GCP Service Account

Simple examples for using Google's Gemini 2.0 Flash model with service account authentication.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the example
python gemini_example.py
```

## Prerequisites

- Python 3.8+
- GCP service account key file (`service-account-key.json`)
- Vertex AI API enabled in your GCP project

## Files

| File | Description |
|------|-------------|
| `gemini_example.py` | **Main example** - SDK-based approach with service account |
| `gemini_rest_api_example.py` | REST API approach for more control |

## Configuration

Current working setup:
- **Model**: `gemini-2.0-flash-001`
- **Region**: `us-central1`
- **Service Account**: Loads from `service-account-key.json`

## Examples

### 1. Basic Text Generation

```python
from google.oauth2 import service_account
import vertexai
from vertexai.generative_models import GenerativeModel

# Load credentials
credentials = service_account.Credentials.from_service_account_file(
    'service-account-key.json',
    scopes=['https://www.googleapis.com/auth/cloud-platform']
)

# Initialize Vertex AI
vertexai.init(
    project='your-project-id',
    location='us-central1',
    credentials=credentials
)

# Generate content
model = GenerativeModel('gemini-2.0-flash-001')
response = model.generate_content('Write a haiku about coding')
print(response.text)
```

### 2. REST API Approach

```python
import requests
from google.oauth2 import service_account

# Get access token
credentials = service_account.Credentials.from_service_account_file(
    'service-account-key.json',
    scopes=['https://www.googleapis.com/auth/cloud-platform']
)
credentials.refresh(google.auth.transport.requests.Request())

# Call API
url = f"https://us-central1-aiplatform.googleapis.com/v1/projects/{project_id}/locations/us-central1/publishers/google/models/gemini-2.0-flash-001:generateContent"

response = requests.post(url, 
    headers={'Authorization': f'Bearer {credentials.token}'},
    json={'contents': [{'role': 'user', 'parts': [{'text': 'Hello!'}]}]}
)
```

## Security

⚠️ **Important**: Never commit `service-account-key.json` to version control!

The `.gitignore` file already excludes it.

## Troubleshooting

### "Model not found" errors
- Verify Vertex AI API is enabled
- Check service account has `aiplatform.admin` or `aiplatform.user` role
- Ensure billing is enabled on the project
- Confirm `gemini-2.0-flash-001` is available in your region

## Additional Resources

- [Vertex AI Documentation](https://cloud.google.com/vertex-ai/docs)
- [Gemini API Reference](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/gemini)
- [Service Account Best Practices](https://cloud.google.com/iam/docs/best-practices-service-accounts)
