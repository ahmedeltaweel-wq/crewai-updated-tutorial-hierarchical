"""
Response Formatter for WhatsApp Messages
Formats AI responses for optimal WhatsApp display
"""

class ResponseFormatter:
    def __init__(self):
        self.max_message_length = 4000  # WhatsApp limit is ~4096
    
    def format_for_whatsapp(self, text, language="ar"):
        """Format text for WhatsApp with emojis and structure"""
        # Clean up extra whitespace
        text = text.strip()
        
        # Add language-specific formatting
        if language == "ar":
            # Ensure proper Arabic text flow
            text = self._format_arabic(text)
        
        return text
    
    def _format_arabic(self, text):
        """Special formatting for Arabic text"""
        # Arabic text is already right-to-left in most clients
        # Just ensure clean formatting
        return text
    
    def split_long_message(self, text):
        """Split long messages into multiple parts"""
        if len(text) <= self.max_message_length:
            return [text]
        
        messages = []
        current_message = ""
        
        # Split by paragraphs first
        paragraphs = text.split('\n\n')
        
        for para in paragraphs:
            if len(current_message) + len(para) + 2 <= self.max_message_length:
                current_message += para + '\n\n'
            else:
                if current_message:
                    messages.append(current_message.strip())
                current_message = para + '\n\n'
        
        if current_message:
            messages.append(current_message.strip())
        
        return messages
    
    def add_context_header(self, text, context_type, language="ar"):
        """Add a header based on context type"""
        headers = {
            "coverage": {
                "ar": "📋 معلومات التغطية",
                "en": "📋 Coverage Information"
            },
            "claim": {
                "ar": "📝 معلومات المطالبة",
                "en": "📝 Claim Information"
            },
            "provider": {
                "ar": "🏥 مقدمو الخدمة",
                "en": "🏥 Healthcare Providers"
            },
            "faq": {
                "ar": "❓ الأسئلة الشائعة",
                "en": "❓ FAQ"
            },
            "contact": {
                "ar": "📞 معلومات التواصل",
                "en": "📞 Contact Information"
            },
            "general": {
                "ar": "💡 معلومات عامة",
                "en": "💡 General Information"
            }
        }
        
        header = headers.get(context_type, headers["general"]).get(language, "")
        return f"{header}\n\n{text}"
    
    def format_error_message(self, language="ar"):
        """Format error message"""
        messages = {
            "ar": """
😔 عذراً، حدث خطأ ما.

يرجى المحاولة مرة أخرى أو التواصل مع خدمة العملاء:
📞 19123
📧 support@insurance.com
            """,
            "en": """
😔 Sorry, something went wrong.

Please try again or contact customer service:
📞 19123
📧 support@insurance.com
            """
        }
        return messages.get(language, messages["ar"])
    
    def format_typing_indicator(self, language="ar"):
        """Format typing indicator message"""
        messages = {
            "ar": "⏳ جاري البحث عن المعلومات...",
            "en": "⏳ Searching for information..."
        }
        return messages.get(language, messages["ar"])
    
    def add_footer(self, text, language="ar"):
        """Add helpful footer to message"""
        footers = {
            "ar": "\n\n━━━━━━━━━━━━━━\n💬 هل تحتاج مساعدة إضافية؟\nاكتب 'مساعدة' لمزيد من الخيارات",
            "en": "\n\n━━━━━━━━━━━━━━\n💬 Need more help?\nType 'help' for more options"
        }
        return text + footers.get(language, footers["ar"])
    
    def clean_ai_formatting(self, text):
        """Remove AI-specific formatting that doesn't work in WhatsApp"""
        # Remove markdown headers (###, ##, etc) but keep bold (**)
        import re
        
        # Keep bullet points
        text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
        
        # Convert markdown bold to WhatsApp bold
        text = text.replace('**', '*')
        
        # Keep emoji and other formatting
        return text
