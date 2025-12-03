from crewai import Agent

class SaudiElectricAgents():
    """Customer Service Agents for Saudi Electric Company"""
    
    def call_receiver_agent(self, llm=None):
        """Call Receiver - Receives and classifies customer requests"""
        return Agent(
            role='Call Receiver',
            goal='Accurately receive and classify customer requests and route them to the appropriate department',
            backstory="""You are a professional receptionist at Saudi Electric Company.
            You have 10 years of experience in customer service and are skilled in handling all types of inquiries.
            You are characterized by patience, professionalism, and the ability to calm angry customers.""",
            allow_delegation=True,
            verbose=True,
            max_iter=10,
            llm=llm
        )

    def billing_specialist_agent(self, llm=None):
        """Billing Specialist - Handles billing and payment inquiries"""
        return Agent(
            role='Billing Specialist',
            goal='Answer all billing inquiries and clearly explain consumption details',
            backstory="""You are an expert in the Saudi electrical billing system.
            You understand all the details of consumption calculation, progressive tariffs, and additional fees.
            You can explain complex bills in a simple and understandable way for customers.""",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def technical_support_agent(self, llm=None):
        """Technical Support - Handles technical fault reports"""
        return Agent(
            role='Technical Support Specialist',
            goal='Receive fault reports and provide immediate solutions or escalate to technical teams',
            backstory="""You are an expert electrical technician with 15 years of experience in the Saudi electrical grid.
            You know all types of common faults and their solutions.
            You can diagnose problems remotely and guide customers to safe solutions.
            You always prioritize safety.""",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    def service_coordinator_agent(self, llm=None):
        """Service Coordinator - Compiles information and prepares final report"""
        return Agent(
            role='Customer Service Coordinator',
            goal='Gather all information from different departments and prepare a comprehensive and satisfactory report for the customer',
            backstory="""You are a professional customer service manager at Saudi Electric Company.
            You excel at coordinating between different departments and providing comprehensive solutions.
            You are committed to customer satisfaction and providing excellent service worthy of the company's reputation.""",
            verbose=True,
            allow_delegation=True,
            llm=llm
        )
