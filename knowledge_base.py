"""
Health Insurance Knowledge Base
Bilingual (Arabic/English) knowledge base for health insurance chatbot
"""

class HealthInsuranceKnowledgeBase:
    def __init__(self):
        self.knowledge = {
            "coverages": {
                "ar": {
                    "basic": """
التغطية الأساسية للتأمين الصحي الشامل:
• الفحوصات الطبية والاستشارات
• الأدوية الموصوفة
• الإقامة في المستشفى
• العمليات الجراحية
• الفحوصات المخبرية والأشعة
• رعاية الطوارئ
• رعاية الأمومة (حسب الباقة)
                    """,
                    "premium": """
التغطية الممتازة للتأمين الصحي الشامل:
✨ جميع مزايا الباقة الأساسية
• غرف خاصة في المستشفى
• تغطية الأسنان الشاملة
• النظارات والعدسات اللاصقة
• العلاج الطبيعي
• الطب البديل
• فحوصات دورية مجانية
• تأمين سفر دولي
                    """
                },
                "en": {
                    "basic": """
Basic Comprehensive Health Insurance Coverage:
• Medical examinations and consultations
• Prescribed medications
• Hospital accommodation
• Surgical operations
• Laboratory tests and X-rays
• Emergency care
• Maternity care (depending on package)
                    """,
                    "premium": """
Premium Comprehensive Health Insurance Coverage:
✨ All basic package benefits
• Private hospital rooms
• Comprehensive dental coverage
• Glasses and contact lenses
• Physiotherapy
• Alternative medicine
• Free periodic checkups
• International travel insurance
                    """
                }
            },
            "claims": {
                "ar": """
خطوات تقديم مطالبة التأمين:

1️⃣ احصل على التقارير الطبية
   • تقرير الطبيب المعالج
   • الفواتير الأصلية
   • نتائج الفحوصات

2️⃣ املأ نموذج المطالبة
   • متوفر في الموقع الإلكتروني
   • أو من مكاتب الخدمة

3️⃣ قدم المستندات
   • عبر البوابة الإلكترونية
   • أو بالبريد الإلكتروني: claims@insurance.com
   • أو شخصياً في الفروع

4️⃣ المتابعة
   • ستتلقى رقم مرجعي
   • المراجعة خلال 3-5 أيام عمل
   • الدفع خلال 10 أيام من الموافقة

📞 للاستفسار: 19123
                """,
                "en": """
Steps to File an Insurance Claim:

1️⃣ Obtain Medical Reports
   • Treating physician's report
   • Original invoices
   • Test results

2️⃣ Fill Out Claim Form
   • Available on website
   • Or from service offices

3️⃣ Submit Documents
   • Via online portal
   • Or email: claims@insurance.com
   • Or in person at branches

4️⃣ Follow Up
   • You'll receive a reference number
   • Review within 3-5 business days
   • Payment within 10 days of approval

📞 For inquiries: 19123
                """
            },
            "providers": {
                "ar": """
شبكة مقدمي الخدمة الصحية:

🏥 المستشفيات الرئيسية:
• مستشفى النيل التخصصي
• مستشفى السلام الدولي
• مستشفى الشفاء المركزي
• مستشفى دار الفؤاد

🔬 المعامل والأشعة:
• معامل البرج
• الفا لاب
• مختبرات المستقبل

💊 الصيدليات:
• صيدليات 19011
• العزبي
• صيدليات النهدي

📍 للبحث عن أقرب مقدم خدمة:
• الموقع الإلكتروني: www.insurance.com/providers
• التطبيق المحمول
• اتصل بـ 19123
                """,
                "en": """
Healthcare Provider Network:

🏥 Major Hospitals:
• Al Nile Specialized Hospital
• Al Salam International Hospital
• Al Shifa Central Hospital
• Dar Al Fouad Hospital

🔬 Labs and Radiology:
• Al Borg Laboratories
• Alpha Lab
• Future Laboratories

💊 Pharmacies:
• 19011 Pharmacies
• Al Ezaby
• Nahdi Pharmacies

📍 To find the nearest provider:
• Website: www.insurance.com/providers
• Mobile app
• Call 19123
                """
            },
            "faq": {
                "ar": [
                    {
                        "q": "كيف أضيف أفراد عائلتي للتأمين؟",
                        "a": "يمكنك إضافة الزوج/الزوجة والأطفال حتى 21 سنة (أو 25 سنة إذا كانوا طلاباً). قدم طلب عبر الموقع الإلكتروني أو اتصل بخدمة العملاء."
                    },
                    {
                        "q": "ما هي فترة الانتظار للأمراض المزمنة؟",
                        "a": "فترة الانتظار 6 أشهر للأمراض المزمنة المُشخصة قبل التأمين. الحالات الطارئة مغطاة فوراً."
                    },
                    {
                        "q": "هل يغطي التأمين العلاج في الخارج؟",
                        "a": "الباقة الممتازة تشمل تغطية دولية في حالات الطوارئ أثناء السفر. للعلاج المخطط بالخارج، يلزم موافقة مسبقة."
                    },
                    {
                        "q": "كيف أجدد اشتراكي؟",
                        "a": "التجديد تلقائي قبل انتهاء الفترة بـ 30 يوم. ستصلك رسالة تأكيد. يمكنك أيضاً التجديد يدوياً عبر الموقع."
                    }
                ],
                "en": [
                    {
                        "q": "How do I add family members to insurance?",
                        "a": "You can add spouse and children up to 21 years (or 25 if students). Submit a request via website or call customer service."
                    },
                    {
                        "q": "What is the waiting period for chronic diseases?",
                        "a": "Waiting period is 6 months for chronic diseases diagnosed before insurance. Emergency cases are covered immediately."
                    },
                    {
                        "q": "Does insurance cover treatment abroad?",
                        "a": "Premium package includes international coverage for emergencies during travel. For planned treatment abroad, prior approval is required."
                    },
                    {
                        "q": "How do I renew my subscription?",
                        "a": "Renewal is automatic 30 days before expiration. You'll receive a confirmation message. You can also renew manually via website."
                    }
                ]
            },
            "contact": {
                "ar": """
📞 معلومات الاتصال:

الخط الساخن: 19123
📧 البريد: support@insurance.com
💬 الدردشة المباشرة: www.insurance.com/chat

⏰ أوقات العمل:
الأحد - الخميس: 9 صباحاً - 6 مساءً
السبت: 10 صباحاً - 3 مساءً
الجمعة: مغلق

🚨 الطوارئ: متاح 24/7
                """,
                "en": """
📞 Contact Information:

Hotline: 19123
📧 Email: support@insurance.com
💬 Live Chat: www.insurance.com/chat

⏰ Working Hours:
Sunday - Thursday: 9 AM - 6 PM
Saturday: 10 AM - 3 PM
Friday: Closed

🚨 Emergency: Available 24/7
                """
            }
        }
    
    def get_coverage_info(self, coverage_type="basic", language="ar"):
        """Get coverage information"""
        return self.knowledge["coverages"].get(language, {}).get(coverage_type, "معلومات غير متوفرة")
    
    def get_claims_process(self, language="ar"):
        """Get claims filing process"""
        return self.knowledge["claims"].get(language, "معلومات غير متوفرة")
    
    def get_providers(self, language="ar"):
        """Get provider network information"""
        return self.knowledge["providers"].get(language, "معلومات غير متوفرة")
    
    def get_contact_info(self, language="ar"):
        """Get contact information"""
        return self.knowledge["contact"].get(language, "معلومات غير متوفرة")
    
    def search_faq(self, query, language="ar"):
        """Search FAQ by query"""
        faqs = self.knowledge["faq"].get(language, [])
        query_lower = query.lower()
        
        # Simple keyword matching
        for faq in faqs:
            if any(word in faq["q"].lower() for word in query_lower.split()):
                return f"❓ {faq['q']}\n\n✅ {faq['a']}"
        
        return None
    
    def get_all_faqs(self, language="ar"):
        """Get all FAQs"""
        faqs = self.knowledge["faq"].get(language, [])
        result = "الأسئلة الشائعة:\n\n" if language == "ar" else "Frequently Asked Questions:\n\n"
        
        for i, faq in enumerate(faqs, 1):
            result += f"{i}. ❓ {faq['q']}\n   ✅ {faq['a']}\n\n"
        
        return result
    
    def get_context_for_agent(self, language="ar"):
        """Get comprehensive context for the agent"""
        context = f"""
You are a helpful health insurance assistant supporting customers in {'Arabic' if language == 'ar' else 'English'}.

Available Information:
1. Coverage types: basic and premium
2. Claims process
3. Provider network
4. FAQs
5. Contact information

Always be helpful, professional, and empathetic. If you don't know something, direct the customer to contact support at 19123.
"""
        return context
