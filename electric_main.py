from crewai import Crew, Process, LLM
from electric_agents import SaudiElectricAgents
from electric_tasks import SaudiElectricTasks
from electric_file_io import save_service_report
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    """Run customer service system without web interface"""
    
    print("🏢 Customer Service System - Saudi Electric Company")
    print("=" * 60)
    
    # Customer request
    customer_request = input("\n📝 Enter customer request:\n> ")
    
    if not customer_request.strip():
        customer_request = "I want to inquire about my last electricity bill, the amount is very high"
        print(f"Using default example: {customer_request}")
    
    print("\n⚡ Processing request...\n")
    
    # Initialize agents and tasks
    agents = SaudiElectricAgents()
    tasks = SaudiElectricTasks()
    
    # Initialize Gemini LLM
    gemini_llm = LLM(
        model="gemini/gemini-flash-latest",
        api_key=os.environ.get("GOOGLE_API_KEY")
    )
    
    # Create agents
    call_receiver = agents.call_receiver_agent(llm=gemini_llm)
    billing_specialist = agents.billing_specialist_agent(llm=gemini_llm)
    technical_support = agents.technical_support_agent(llm=gemini_llm)
    service_coordinator = agents.service_coordinator_agent(llm=gemini_llm)
    
    # Create tasks
    receive_task = tasks.receive_customer_request_task(call_receiver, customer_request)
    billing_task = tasks.handle_billing_inquiry_task(billing_specialist, [receive_task])
    technical_task = tasks.handle_technical_issue_task(technical_support, [receive_task])
    compile_task = tasks.compile_service_report_task(
        service_coordinator, [receive_task, billing_task, technical_task], save_service_report)
    
    # Form the crew
    crew = Crew(
        agents=[call_receiver, billing_specialist, technical_support, service_coordinator],
        tasks=[receive_task, billing_task, technical_task, compile_task],
        process=Process.hierarchical,
        manager_llm=gemini_llm,
        verbose=True
    )
    
    # Start the work
    print("\n🚀 Starting work...\n")
    results = crew.kickoff()
    
    print("\n" + "=" * 60)
    print("✅ Service completed successfully!")
    print("=" * 60)
    print("\n📄 Final Report:\n")
    print(results)

if __name__ == '__main__':
    main()
