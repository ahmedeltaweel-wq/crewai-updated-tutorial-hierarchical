"""
Language Detection for Bilingual WhatsApp Bot
Detects Arabic vs English and maintains conversation context
"""

import re
from collections import defaultdict

class LanguageDetector:
    def __init__(self):
        # Store language preference per user
        self.user_languages = defaultdict(lambda: "ar")  # Default to Arabic
        
        # Common English and Arabic words for detection
        self.english_words = {
            "hello", "hi", "help", "insurance", "coverage", "claim", "policy",
            "how", "what", "when", "where", "who", "why", "the", "is", "are",
            "can", "could", "would", "should", "please", "thank", "thanks"
        }
        
        self.arabic_words = {
            "مرحبا", "السلام", "أهلا", "تأمين", "تغطية", "مطالبة", "بوليصة",
            "كيف", "ماذا", "متى", "أين", "من", "لماذا", "هل", "ما", "في",
            "على", "من", "إلى", "هذا", "هذه", "ذلك", "شكرا", "مساعدة"
        }
    
    def detect_language(self, text, user_id=None):
        """
        Detect language of text
        Returns: 'ar' for Arabic, 'en' for English
        """
        if not text or not text.strip():
            return self.user_languages.get(user_id, "ar") if user_id else "ar"
        
        text_lower = text.lower().strip()
        
        # Check for explicit language switching commands
        if any(cmd in text_lower for cmd in ["english", "switch to english", "تحويل للإنجليزية"]):
            if user_id:
                self.user_languages[user_id] = "en"
            return "en"
        
        if any(cmd in text_lower for cmd in ["arabic", "عربي", "switch to arabic", "تحويل للعربية"]):
            if user_id:
                self.user_languages[user_id] = "ar"
            return "ar"
        
        # Detect Arabic characters
        arabic_chars = len(re.findall(r'[\u0600-\u06FF]', text))
        total_chars = len(re.sub(r'\s', '', text))
        
        if total_chars == 0:
            return self.user_languages.get(user_id, "ar") if user_id else "ar"
        
        arabic_ratio = arabic_chars / total_chars
        
        # If more than 30% Arabic characters, it's Arabic
        if arabic_ratio > 0.3:
            detected = "ar"
        # Check for English keywords
        elif any(word in text_lower for word in self.english_words):
            detected = "en"
        # Check for Arabic keywords
        elif any(word in text for word in self.arabic_words):
            detected = "ar"
        # Default to previous user language or Arabic
        else:
            detected = self.user_languages.get(user_id, "ar") if user_id else "ar"
        
        # Store user preference
        if user_id:
            self.user_languages[user_id] = detected
        
        return detected
    
    def get_user_language(self, user_id):
        """Get stored language preference for user"""
        return self.user_languages.get(user_id, "ar")
    
    def set_user_language(self, user_id, language):
        """Manually set user language preference"""
        if language in ["ar", "en"]:
            self.user_languages[user_id] = language
    
    def get_greeting(self, language):
        """Get greeting message in appropriate language"""
        greetings = {
            "ar": """
مرحباً بك في مساعد التأمين الصحي الشامل! 🏥

كيف يمكنني مساعدتك اليوم؟

يمكنك السؤال عن:
• التغطيات والباقات 📋
• تقديم مطالبة 📝
• مقدمي الخدمة 🏥
• الأسئلة الشائعة ❓
• معلومات التواصل 📞

أنا هنا للمساعدة! 😊
            """,
            "en": """
Welcome to Comprehensive Health Insurance Assistant! 🏥

How can I help you today?

You can ask about:
• Coverage and packages 📋
• Filing a claim 📝
• Healthcare providers 🏥
• FAQs ❓
• Contact information 📞

I'm here to help! 😊
            """
        }
        return greetings.get(language, greetings["ar"])
    
    def get_help_message(self, language):
        """Get help message in appropriate language"""
        help_messages = {
            "ar": """
📚 كيف يمكنني مساعدتك:

1️⃣ معلومات التغطية
   اكتب: "تغطية" أو "باقات"

2️⃣ تقديم مطالبة
   اكتب: "مطالبة" أو "كيف أقدم مطالبة"

3️⃣ مقدمي الخدمة
   اكتب: "مستشفيات" أو "مقدمي خدمة"

4️⃣ أسئلة شائعة
   اكتب: "أسئلة" أو "FAQ"

5️⃣ معلومات التواصل
   اكتب: "تواصل" أو "رقم الهاتف"

💡 يمكنك أيضاً كتابة سؤالك مباشرة!
            """,
            "en": """
📚 How I can help you:

1️⃣ Coverage Information
   Type: "coverage" or "packages"

2️⃣ File a Claim
   Type: "claim" or "how to file claim"

3️⃣ Healthcare Providers
   Type: "hospitals" or "providers"

4️⃣ FAQs
   Type: "faq" or "questions"

5️⃣ Contact Information
   Type: "contact" or "phone number"

💡 You can also type your question directly!
            """
        }
        return help_messages.get(language, help_messages["ar"])
