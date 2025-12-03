"""
Telegram Health Insurance Bot - CrewAI Version
This bot uses the full CrewAI multi-agent system to answer queries.
"""

import os
import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from crewai import Crew, Process

# Import our CrewAI components
from health_insurance_agent import HealthInsuranceAgentConfig
from health_insurance_tasks import HealthInsuranceTasks
from knowledge_base import HealthInsuranceKnowledgeBase
from language_detector import LanguageDetector

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize components
kb = HealthInsuranceKnowledgeBase()
lang_detector = LanguageDetector()
agent_config = HealthInsuranceAgentConfig()
tasks_config = HealthInsuranceTasks(kb)

# Get Telegram token
TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

if not TELEGRAM_TOKEN:
    logger.error("TELEGRAM_BOT_TOKEN not found in .env file!")
    exit(1)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    await update.message.reply_text("مرحباً! أنا بوت التأمين الصحي الذكي (نسخة CrewAI).\nأستخدم فريقاً من العملاء الأذكياء للإجابة على استفساراتك.\n\nHello! I am the Smart Health Insurance Bot (CrewAI Version).\nI use a team of intelligent agents to answer your queries.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle regular text messages using CrewAI"""
    user_id = str(update.effective_user.id)
    message_text = update.message.text
    
    logger.info(f"Message from {user_id}: {message_text}")
    
    # Send a "typing" action or a "thinking" message because CrewAI takes time
    status_msg = await update.message.reply_text("🤔 جاري استشارة فريق العمل... (قد يستغرق بضع ثوانٍ)\n🤔 Consulting the team... (this may take a few seconds)")
    
    try:
        # 1. Detect language
        language = lang_detector.detect_language(message_text, user_id)
        
        # 2. Create Agents
        # We create fresh agents for each request to ensure no state leakage in this simple demo
        classifier_agent = agent_config.create_query_classifier_agent(language)
        insurance_agent = agent_config.create_insurance_agent(language)
        
        # 3. Define Tasks
        # First: Classify the query
        classify_task = tasks_config.classify_query_task(classifier_agent, message_text, language)
        
        # Second: We need to dynamically decide the next task based on classification, 
        # but for this simple CrewAI demo, we will create a generic "Answer" task 
        # that takes the classification context if possible, or just answers directly.
        # To keep it simple and robust, we'll ask the insurance agent to answer based on the query type.
        
        # Let's create a specialized task for the insurance agent
        # We'll use the 'answer_general_task' which is flexible enough
        answer_task = tasks_config.answer_general_task(insurance_agent, message_text, language)
        
        # 4. Create Crew
        # We put both agents in the crew. 
        # Note: In a more complex setup, we might pass the output of classify_task to answer_task
        crew = Crew(
            agents=[classifier_agent, insurance_agent],
            tasks=[classify_task, answer_task],
            process=Process.sequential, # Run sequentially: Classify -> Answer
            verbose=True
        )
        
        # 5. Kickoff!
        # Since CrewAI is blocking, we run it in a way that doesn't block the async Telegram loop
        # We use asyncio.to_thread to run the blocking kickoff
        result = await asyncio.to_thread(crew.kickoff)
        
        # 6. Send Response
        final_answer = str(result)
        
        # Delete the "thinking" message
        await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=status_msg.message_id)
        
        # Send the final answer
        await update.message.reply_text(final_answer)
            
    except Exception as e:
        logger.error(f"Error in CrewAI processing: {e}", exc_info=True)
        await update.message.reply_text("عذراً، حدث خطأ أثناء معالجة طلبك.\nSorry, an error occurred while processing your request.")

def main():
    """Start the bot"""
    logger.info("Starting Telegram Health Insurance Bot (CrewAI Version)...")
    
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    application.run_polling()

if __name__ == '__main__':
    main()
