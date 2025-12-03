"""
Health Insurance Tasks
Task definitions for the health insurance agent
"""

from crewai import Task

class HealthInsuranceTasks:
    def __init__(self, knowledge_base):
        self.kb = knowledge_base
    
    def classify_query_task(self, agent, user_query, language="ar"):
        """Task to classify user query type"""
        
        if language == "ar":
            description = f"""
حلل الاستفسار التالي من العميل وحدد نوعه:

استفسار العميل: {user_query}

حدد إذا كان الاستفسار عن:
- التغطيات والباقات (coverage)
- تقديم مطالبة (claim)
- مقدمي الخدمة (provider)
- أسئلة شائعة (faq)
- معلومات التواصل (contact)
- عام (general)

أعطي نوع واحد فقط من الأنواع المذكورة أعلاه.
"""
            expected_output = "نوع الاستفسار (coverage أو claim أو provider أو faq أو contact أو general)"
        
        else:
            description = f"""
Analyze the following customer query and determine its type:

Customer Query: {user_query}

Determine if the query is about:
- Coverage and packages (coverage)
- Filing a claim (claim)
- Healthcare providers (provider)
- Frequently asked questions (faq)
- Contact information (contact)
- General (general)

Provide only one type from the above list.
"""
            expected_output = "Query type (coverage or claim or provider or faq or contact or general)"
        
        return Task(
            description=description,
            agent=agent,
            expected_output=expected_output
        )
    
    def answer_coverage_task(self, agent, user_query, language="ar"):
        """Task to answer coverage questions"""
        
        basic_coverage = self.kb.get_coverage_info("basic", language)
        premium_coverage = self.kb.get_coverage_info("premium", language)
        
        if language == "ar":
            description = f"""
أجب على استفسار العميل التالي عن التغطيات:

استفسار العميل: {user_query}

معلومات التغطية المتاحة:
{basic_coverage}

{premium_coverage}

قدم إجابة واضحة ومفيدة باللغة العربية.
"""
            expected_output = "إجابة شاملة ومفصلة عن التغطيات بالعربية"
        
        else:
            description = f"""
Answer the following customer query about coverage:

Customer Query: {user_query}

Available Coverage Information:
{basic_coverage}

{premium_coverage}

Provide a clear and helpful answer in English.
"""
            expected_output = "Comprehensive and detailed answer about coverage in English"
        
        return Task(
            description=description,
            agent=agent,
            expected_output=expected_output
        )
    
    def answer_claims_task(self, agent, user_query, language="ar"):
        """Task to answer claims questions"""
        
        claims_info = self.kb.get_claims_process(language)
        
        if language == "ar":
            description = f"""
أجب على استفسار العميل التالي عن المطالبات:

استفسار العميل: {user_query}

معلومات المطالبات:
{claims_info}

قدم إجابة واضحة ومفيدة باللغة العربية.
"""
            expected_output = "إجابة شاملة عن إجراءات المطالبات بالعربية"
        
        else:
            description = f"""
Answer the following customer query about claims:

Customer Query: {user_query}

Claims Information:
{claims_info}

Provide a clear and helpful answer in English.
"""
            expected_output = "Comprehensive answer about claims procedures in English"
        
        return Task(
            description=description,
            agent=agent,
            expected_output=expected_output
        )
    
    def answer_provider_task(self, agent, user_query, language="ar"):
        """Task to answer provider questions"""
        
        provider_info = self.kb.get_providers(language)
        
        if language == "ar":
            description = f"""
أجب على استفسار العميل التالي عن مقدمي الخدمة:

استفسار العميل: {user_query}

معلومات مقدمي الخدمة:
{provider_info}

قدم إجابة واضحة ومفيدة باللغة العربية.
"""
            expected_output = "إجابة شاملة عن مقدمي الخدمة بالعربية"
        
        else:
            description = f"""
Answer the following customer query about healthcare providers:

Customer Query: {user_query}

Provider Information:
{provider_info}

Provide a clear and helpful answer in English.
"""
            expected_output = "Comprehensive answer about healthcare providers in English"
        
        return Task(
            description=description,
            agent=agent,
            expected_output=expected_output
        )
    
    def answer_general_task(self, agent, user_query, language="ar"):
        """Task to answer general questions"""
        
        contact_info = self.kb.get_contact_info(language)
        context = self.kb.get_context_for_agent(language)
        
        # Try to find relevant FAQ
        faq_answer = self.kb.search_faq(user_query, language)
        faq_context = f"\n\nRelevant FAQ:\n{faq_answer}" if faq_answer else ""
        
        if language == "ar":
            description = f"""
أجب على استفسار العميل التالي:

استفسار العميل: {user_query}

السياق:
{context}

معلومات التواصل (للمساعدة في التوجيه):
{contact_info}{faq_context}

قدم إجابة مفيدة باللغة العربية. إذا لم تكن لديك معلومات كافية، وجه العميل للتواصل مع خدمة العملاء.
"""
            expected_output = "إجابة مفيدة بالعربية"
        
        else:
            description = f"""
Answer the following customer query:

Customer Query: {user_query}

Context:
{context}

Contact Information (for routing):
{contact_info}{faq_context}

Provide a helpful answer in English. If you don't have sufficient information, direct the customer to contact customer service.
"""
            expected_output = "Helpful answer in English"
        
        return Task(
            description=description,
            agent=agent,
            expected_output=expected_output
        )
