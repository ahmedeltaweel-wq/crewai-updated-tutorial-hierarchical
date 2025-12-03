# 🤖 AI-Powered Multi-Agent Applications

A collection of intelligent applications powered by Google's Gemini AI, featuring Telegram bots and web interfaces with multi-agent workflows.

## 🌟 Features

- ✅ **Dual Authentication**: Supports both API Key and Google Cloud Vertex AI (Service Account)
- ✅ **Multi-Agent System**: Hierarchical CrewAI workflows
- ✅ **Telegram Bot**: Health insurance customer service
- ✅ **Web Interface**: Electric company customer service
- ✅ **Production Ready**: Optimized for Google Cloud Run deployment
- ✅ **Auto-Deploy**: Continuous deployment from GitHub

---

## 📦 Applications

### 1. Telegram Health Insurance Bot
Interactive bot for health insurance inquiries with AI-powered responses.

**Features:**
- Bilingual support (Arabic/English)
- Conversation history
- Knowledge base integration
- Real-time AI responses

### 2. Electric Company Customer Service
Web-based multi-agent system for electric company customer service.

**Features:**
- Real-time agent status visualization
- Hierarchical task processing
- Billing and technical support
- Service report generation

---

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env and add your credentials
   ```

4. **Run applications**
   ```bash
   # Telegram Bot
   python telegram_bot.py
   
   # Electric Web App
   python electric_web_app.py
   ```

---

## ☁️ Google Cloud Deployment

### Option 1: Using Service Account (Recommended for Production)

**Prerequisites:**
- Google Cloud Project: `eg-konecta-sandbox`
- Service Account: `sa-vertex@eg-konecta-sandbox.iam.gserviceaccount.com`
- Vertex AI API enabled

**Environment Variables:**
```bash
USE_VERTEX_AI=true
GOOGLE_CLOUD_PROJECT=eg-konecta-sandbox
VERTEX_AI_LOCATION=us-central1
TELEGRAM_BOT_TOKEN=your-token
```

**Deploy:**
```bash
gcloud run deploy telegram-health-bot \
  --source . \
  --region us-central1 \
  --service-account sa-vertex@eg-konecta-sandbox.iam.gserviceaccount.com \
  --set-env-vars USE_VERTEX_AI=true,GOOGLE_CLOUD_PROJECT=eg-konecta-sandbox
```

📖 **Full Guide:** [GOOGLE_CLOUD_RUN_DEPLOY.md](GOOGLE_CLOUD_RUN_DEPLOY.md)

### Option 2: Using API Key (Quick Deploy)

**Environment Variables:**
```bash
GOOGLE_API_KEY=your-api-key
TELEGRAM_BOT_TOKEN=your-token
```

---

## 🔧 Configuration

### Authentication Methods

The applications support **two authentication methods**:

#### 1. API Key (Local Development)
```bash
# .env
GOOGLE_API_KEY=your-gemini-api-key
```

#### 2. Vertex AI (Production)
```bash
# .env
USE_VERTEX_AI=true
GOOGLE_CLOUD_PROJECT=eg-konecta-sandbox
VERTEX_AI_LOCATION=us-central1
```

**Local with Service Account:**
```bash
gcloud auth application-default login
gcloud config set project eg-konecta-sandbox
```

---

## 📁 Project Structure

```
├── telegram_bot.py              # Telegram bot application
├── electric_web_app.py          # Electric company web app
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker configuration
├── .env.example                 # Environment variables template
│
├── knowledge_base.py            # Knowledge base system
├── language_detector.py         # Language detection
├── response_formatter.py        # Response formatting
├── company_loader.py            # Company knowledge loader
├── company_knowledge.md         # Company information
│
├── electric_agents.py           # Multi-agent definitions
├── electric_tasks.py            # Agent tasks
├── electric_file_io.py          # File operations
│
├── templates/                   # Web templates
│   └── electric_index.html
│
└── docs/                        # Documentation
    ├── GOOGLE_CLOUD_RUN_DEPLOY.md
    ├── QUICK_GCLOUD_SETUP.md
    ├── AUTH_COMPARISON.md
    └── ...
```

---

## 🛠️ Requirements

```
python-telegram-bot==20.7
google-generativeai>=0.8.0
google-cloud-aiplatform>=1.38.0
python-dotenv==1.0.0
requests>=2.32.0
Flask==3.0.0
crewai
flask-socketio
flask-cors
```

---

## 🔒 Security

- ✅ Never commit `.env` files
- ✅ Use Service Account for production
- ✅ Rotate API keys regularly
- ✅ Use Google Secret Manager for sensitive data
- ✅ Enable Cloud Armor for DDoS protection

---

## 📊 Cost Estimation

### Google Cloud Free Tier

**Cloud Run:**
- 2 million requests/month
- 360,000 GB-seconds
- 180,000 vCPU-seconds

**Vertex AI:**
- First 1,000 requests free
- ~$0.00025 per 1,000 characters after

**Estimated Cost for Small Bot:**
- **$0.00 - $0.50/month** (within free tier)

---

## 🧪 Testing

### Test Gemini API
```bash
python test_gemini_quick.py
```

### Test gcloud Authentication
```bash
python test_gcloud_auth.py
```

---

## 📚 Documentation

- [Google Cloud Run Deployment Guide](GOOGLE_CLOUD_RUN_DEPLOY.md)
- [Quick gcloud Setup](QUICK_GCLOUD_SETUP.md)
- [Authentication Comparison](AUTH_COMPARISON.md)
- [Service Account Setup](SERVICE_ACCOUNT_SETUP.md)
- [Setup Complete Guide](SETUP_COMPLETE.md)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📝 License

This project is licensed under the MIT License.

---

## 🆘 Support

For issues and questions:
- 📧 Email: support@example.com
- 📖 Documentation: [docs/](docs/)
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/your-repo/issues)

---

## 🙏 Acknowledgments

- Google Gemini AI
- CrewAI Framework
- Python Telegram Bot
- Flask & SocketIO

---

**Made with ❤️ using Google Cloud & Gemini AI**
