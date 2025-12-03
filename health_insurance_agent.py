"""
Health Insurance Agent Configuration
CrewAI agent specialized in health insurance support
"""

from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

class HealthInsuranceAgentConfig:
    def __init__(self):
        self.llm = self._setup_llm()
    
    def _setup_llm(self):
        """Setup Gemini LLM"""
        api_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
        
        if not api_key:
            raise ValueError("GEMINI_API_KEY or GOOGLE_API_KEY not found in environment variables")
        
        # Using the standard LLM class from CrewAI for better compatibility
        from crewai import LLM
        return LLM(
            model="gemini/gemini-1.5-flash",
            api_key=api_key,
            temperature=0.7
        )
    
    def create_insurance_agent(self, language="ar"):
        """Create health insurance support agent"""
        
        if language == "ar":
            role = "مساعد التأمين الصحي"
            goal = "مساعدة العملاء في جميع استفساراتهم المتعلقة بالتأمين الصحي الشامل بطريقة واضحة ومهنية"
            backstory = """أنت مساعد خبير في التأمين الصحي الشامل، تعمل لصالح شركة تأمين رائدة.
لديك معرفة شاملة بجميع أنواع التغطيات، إجراءات المطالبات، وشبكة مقدمي الخدمة.
تتعامل مع العملاء بطريقة ودودة ومهنية، وتحرص على تقديم معلومات دقيقة ومفيدة.
إذا لم تكن متأكداً من معلومة معينة، توجه العميل للتواصل مع خدمة العملاء على 19123."""
        
        else:  # English
            role = "Health Insurance Assistant"
            goal = "Help customers with all their comprehensive health insurance inquiries in a clear and professional manner"
            backstory = """You are an expert health insurance assistant working for a leading insurance company.
You have comprehensive knowledge of all coverage types, claims procedures, and healthcare provider networks.
You interact with customers in a friendly and professional manner, ensuring accurate and helpful information.
If you're unsure about specific information, you direct customers to contact customer service at 19123."""
        
        return Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
            memory=True
        )
    
    def create_query_classifier_agent(self, language="ar"):
        """Create agent to classify query type"""
        
        if language == "ar":
            role = "محلل الاستفسارات"
            goal = "تحديد نوع استفسار العميل وتوجيهه للمعلومات المناسبة"
            backstory = """أنت خبير في تحليل استفسارات العملاء وتصنيفها.
تحدد بدقة ما إذا كان العميل يسأل عن التغطيات، المطالبات، مقدمي الخدمة، أو معلومات عامة."""
        
        else:
            role = "Query Analyzer"
            goal = "Identify customer query type and route to appropriate information"
            backstory = """You are an expert in analyzing and classifying customer queries.
You accurately determine if the customer is asking about coverage, claims, providers, or general information."""
        
        return Agent(
            role=role,
            goal=goal,
            backstory=backstory,
            llm=self.llm,
            verbose=True,
            allow_delegation=False
        )
