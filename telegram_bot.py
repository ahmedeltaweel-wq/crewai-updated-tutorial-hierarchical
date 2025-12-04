"""
Telegram Health Insurance Bot - AWS App Runner Compatible
Adds a simple health check endpoint for AWS
"""

import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import google.generativeai as genai
from threading import Thread
from flask import Flask

from knowledge_base import HealthInsuranceKnowledgeBase
from language_detector import LanguageDetector
from response_formatter import ResponseFormatter
from company_loader import CompanyKnowledge

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Configure Gemini - Support both API Key and Vertex AI
api_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
use_vertex_ai = os.getenv('USE_VERTEX_AI', 'false').lower() == 'true'

if api_key and not use_vertex_ai:
    logger.info("🔑 Using Gemini API Key")
    genai.configure(api_key=api_key)
    # Using gemini-1.5-flash as recommended for production
    gemini_model = genai.GenerativeModel('gemini-1.5-flash')
elif use_vertex_ai or (not api_key and os.getenv('GOOGLE_CLOUD_PROJECT')):
    # Use Vertex AI (Service Account)
    try:
        logger.info("☁️ Using Google Cloud Vertex AI (Service Account)")
        from vertexai.preview.generative_models import GenerativeModel
        import vertexai
        
        project_id = os.getenv('GOOGLE_CLOUD_PROJECT', 'eg-konecta-sandbox')
        location = os.getenv('VERTEX_AI_LOCATION', 'us-central1')
        
        vertexai.init(project=project_id, location=location)
        gemini_model = GenerativeModel('gemini-1.5-flash')
        logger.info(f"✅ Vertex AI initialized: {project_id} / {location}")
    except Exception as e:
        logger.error(f"❌ Failed to initialize Vertex AI: {e}")
        gemini_model = None
        logger.warning("Falling back to knowledge base only")
else:
    gemini_model = None
    logger.warning("No Gemini API key or Vertex AI config found - using knowledge base only")

# Initialize components
kb = HealthInsuranceKnowledgeBase()
lang_detector = LanguageDetector()
formatter = ResponseFormatter()
company_kb = CompanyKnowledge()  # Load company-specific knowledge

logger.info(f"📚 Company knowledge loaded from: {company_kb.company_info['file_path']}")

# Store conversation history per user
conversation_history = {}

def get_conversation_history(user_id: str) -> list:
    """Get or create conversation history for a user"""
    if user_id not in conversation_history:
        conversation_history[user_id] = []
    return conversation_history[user_id]

def add_to_history(user_id: str, role: str, content: str):
    """Add message to conversation history"""
    history = get_conversation_history(user_id)
    history.append({"role": role, "content": content})
    
    # Keep only last 10 messages (5 exchanges)
    if len(history) > 10:
        conversation_history[user_id] = history[-10:]

def clear_history(user_id: str):
    """Clear conversation history for a user"""
    if user_id in conversation_history:
        conversation_history[user_id] = []

# Get Telegram token
TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

if not TELEGRAM_TOKEN:
    logger.error("TELEGRAM_BOT_TOKEN not found in .env file!")
    logger.error("Please add: TELEGRAM_BOT_TOKEN=your_token_here")
    exit(1)

# Flask app for health check (AWS App Runner requirement)
flask_app = Flask(__name__)

@flask_app.route('/')
@flask_app.route('/health')
def health_check():
    """Health check endpoint for AWS"""
    return {'status': 'healthy', 'service': 'telegram-health-bot'}, 200

def run_flask():
    """Run Flask in a separate thread"""
    port = int(os.getenv('PORT', 8080))
    flask_app.run(host='0.0.0.0', port=port, debug=False)

# Telegram bot handlers (same as before)
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    user_id = str(update.effective_user.id)
    user_lang = update.effective_user.language_code
    language = "ar" if user_lang and user_lang.startswith("ar") else "en"
    
    greeting = lang_detector.get_greeting(language)
    help_msg = lang_detector.get_help_message(language)
    response = f"{greeting}\n\n{help_msg}"
    await update.message.reply_text(response)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    user_id = str(update.effective_user.id)
    language = lang_detector.user_languages.get(user_id, "ar")
    help_msg = lang_detector.get_help_message(language)
    await update.message.reply_text(help_msg)

async def coverage_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /coverage command"""
    user_id = str(update.effective_user.id)
    language = lang_detector.user_languages.get(user_id, "ar")
    
    basic = kb.get_coverage_info("basic", language)
    premium = kb.get_coverage_info("premium", language)
    response = f"{basic}\n\n{premium}"
    response = formatter.add_context_header(response, "coverage", language)
    
    messages = formatter.split_long_message(response)
    for msg in messages:
        await update.message.reply_text(msg)

async def claims_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /claims command"""
    user_id = str(update.effective_user.id)
    language = lang_detector.user_languages.get(user_id, "ar")
    
    response = kb.get_claims_process(language)
    response = formatter.add_context_header(response, "claim", language)
    
    messages = formatter.split_long_message(response)
    for msg in messages:
        await update.message.reply_text(msg)

async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /contact command"""
    user_id = str(update.effective_user.id)
    language = lang_detector.user_languages.get(user_id, "ar")
    
    response = kb.get_contact_info(language)
    await update.message.reply_text(response)

async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /clear command - clear conversation history"""
    user_id = str(update.effective_user.id)
    language = lang_detector.user_languages.get(user_id, "ar")
    
    clear_history(user_id)
    
    if language == "ar":
        response = "✅ تم مسح سجل المحادثة!\n\nيمكنك الآن بدء محادثة جديدة."
    else:
        response = "✅ Conversation history cleared!\n\nYou can now start a fresh conversation."
    
    await update.message.reply_text(response)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle regular text messages"""
    try:
        user_id = str(update.effective_user.id)
        message_text = update.message.text
        
        logger.info(f"Message from {user_id}: {message_text}")
        
        # Detect language
        language = lang_detector.detect_language(message_text, user_id)
        
        # Check for greetings
        message_lower = message_text.lower().strip()
        if message_lower in ['hi', 'hello', 'مرحبا', 'السلام عليكم', 'أهلا']:
            response = lang_detector.get_greeting(language)
            await update.message.reply_text(response)
            return
        
        # Check for quick info requests
        query_lower = message_text.lower()
        
        # Coverage request
        if any(word in query_lower for word in ['coverage', 'تغطية', 'باقة', 'package']):
            if any(word in query_lower for word in ['premium', 'ممتازة', 'مميزة']):
                response = kb.get_coverage_info("premium", language)
            else:
                basic = kb.get_coverage_info("basic", language)
                premium = kb.get_coverage_info("premium", language)
                response = f"{basic}\n\n{premium}"
            response = formatter.add_context_header(response, "coverage", language)
            
        # Claims request
        elif any(word in query_lower for word in ['claim', 'مطالبة', 'تقديم']):
            response = kb.get_claims_process(language)
            response = formatter.add_context_header(response, "claim", language)
            
        # Provider request
        elif any(word in query_lower for word in ['provider', 'hospital', 'مستشفى', 'مقدم', 'عيادة']):
            response = kb.get_providers(language)
            response = formatter.add_context_header(response, "provider", language)
            
        # Contact request
        elif any(word in query_lower for word in ['contact', 'phone', 'تواصل', 'هاتف', 'رقم']):
            response = kb.get_contact_info(language)
            
        # Complex query - use AI
        else:
            response = await process_with_ai(message_text, language, user_id)
        
        # Format and send response
        messages = formatter.split_long_message(response)
        for msg in messages:
            await update.message.reply_text(msg)
            
    except Exception as e:
        logger.error(f"Error handling message: {e}", exc_info=True)
        error_msg = formatter.format_error_message(language)
        await update.message.reply_text(error_msg)

async def process_with_ai(query: str, language: str, user_id: str) -> str:
    """Process query using Gemini AI with conversation history"""
    try:
        if not gemini_model:
            raise Exception("Gemini API not configured")
        
        # Get conversation history
        history = get_conversation_history(user_id)
        
        # Build context from history
        context_messages = ""
        if history:
            context_messages = "\n\nPrevious conversation:\n"
            for msg in history[-6:]:  # Last 3 exchanges
                role = "User" if msg["role"] == "user" else "Assistant"
                context_messages += f"{role}: {msg['content']}\n"
        
        # Get company knowledge summary
        company_context = company_kb.get_summary()
        
        # Build prompt with history and personality
        if language == "ar":
            prompt = f"""أنت موظف خدمة عملاء محترف وودود في شركة تأمين صحي. اسمك "أحمد" وأنت هنا لمساعدة العملاء.

🎯 شخصيتك:
- ودود ومرحب
- صبور ومتفهم
- واضح ومباشر
- متحمس لمساعدة العملاء
- تستخدم الإيموجي بشكل مناسب

📚 معلومات الشركة المتاحة لديك:
{company_context}

{context_messages}

💬 استفسار العميل الحالي: {query}

📋 تعليمات الرد:
1. ابدأ بتحية ودية إذا كانت أول رسالة
2. أجب على السؤال بوضوح وبساطة
3. قدم أمثلة عملية عند الحاجة
4. اقترح معلومات إضافية مفيدة
5. اختم بسؤال "هل تحتاج مساعدة أخرى؟"
6. إذا لم تكن متأكداً، وجه العميل لخدمة العملاء: 19123

تذكر: أنت تتحدث مع إنسان، كن طبيعياً وودوداً! 😊"""
        else:
            prompt = f"""You are a professional and friendly customer service representative at a health insurance company. Your name is "Ahmed" and you're here to help customers.

🎯 Your Personality:
- Warm and welcoming
- Patient and understanding
- Clear and direct
- Enthusiastic about helping
- Use emojis appropriately

📚 Company Information Available to You:
{company_context}

{context_messages}

💬 Current Customer Query: {query}

📋 Response Instructions:
1. Start with a friendly greeting if it's the first message
2. Answer the question clearly and simply
3. Provide practical examples when needed
4. Suggest additional helpful information
5. End with "Is there anything else I can help you with?"
6. If unsure, direct customer to support: 19123

Remember: You're talking to a human, be natural and friendly! 😊"""
        
        # Show what we're sending to Gemini
        logger.info("=" * 60)
        logger.info("🤖 GEMINI AI CONVERSATION")
        logger.info("=" * 60)
        logger.info(f"👤 USER ID: {user_id}")
        logger.info(f"📤 USER QUERY ({language.upper()}):")
        logger.info(f"   {query}")
        logger.info(f"📚 CONVERSATION HISTORY: {len(history)} messages")
        logger.info("-" * 60)
        logger.info("📤 SENDING TO GEMINI:")
        logger.info(f"   Model: gemini-1.5-flash")
        logger.info(f"   Language: {language}")
        logger.info(f"   Prompt length: {len(prompt)} characters")
        logger.info("-" * 60)
        
        # Call Gemini
        response = gemini_model.generate_content(prompt)
        answer = response.text
        
        # Show what Gemini responded
        logger.info("📥 GEMINI RESPONSE:")
        logger.info(f"   {answer[:200]}..." if len(answer) > 200 else f"   {answer}")
        logger.info(f"   Response length: {len(answer)} characters")
        logger.info("=" * 60)
        
        # Add to history
        add_to_history(user_id, "user", query)
        add_to_history(user_id, "assistant", answer)
        
        # Clean formatting
        answer = formatter.clean_ai_formatting(answer)
        
        return answer
        
    except Exception as e:
        logger.error(f"❌ Error in AI processing: {e}")
        logger.error("=" * 60)
        # Fallback to knowledge base
        faq_answer = kb.search_faq(query, language)
        if faq_answer:
            return faq_answer
        else:
            if language == "ar":
                return f"شكراً لسؤالك. للحصول على مساعدة أفضل، يرجى التواصل مع خدمة العملاء على:\n📞 19123\n📧 support@insurance.com"
            else:
                return f"Thank you for your question. For better assistance, please contact customer service:\n📞 19123\n📧 support@insurance.com"

def main():
    """Start the bot"""
    logger.info("=" * 60)
    logger.info("Starting Telegram Health Insurance Bot...")
    logger.info("=" * 60)
    
    # Start Flask health check server in background
    flask_thread = Thread(target=run_flask, daemon=True)
    flask_thread.start()
    logger.info("✅ Health check server started on port 8080")
    
    # Create application
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("coverage", coverage_command))
    application.add_handler(CommandHandler("claims", claims_command))
    application.add_handler(CommandHandler("contact", contact_command))
    application.add_handler(CommandHandler("clear", clear_command))
    
    # Add message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start bot
    logger.info("✅ Bot is ready!")
    logger.info("🤖 You can now send messages to your bot on Telegram")
    logger.info("=" * 60)
    
    # Run the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
