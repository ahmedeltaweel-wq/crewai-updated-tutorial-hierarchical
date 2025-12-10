from datetime import datetime
from crewai import Task


class SaudiElectricTasks():
    """Customer Service Tasks for Saudi Electric Company"""
    
    def receive_customer_request_task(self, agent, customer_request):
        """Task to receive and classify customer request"""
        return Task(
            description=f"""Receive and classify the following customer request:
            
            Customer Request: {customer_request}
            
            Please do the following:
            1. Accurately understand the customer's request
            2. Determine the request type (billing / technical fault / general inquiry / complaint)
            3. Determine priority level (urgent / normal / low)
            4. Extract important information (account number, location, problem details)
            """,
            agent=agent,
            expected_output="""Request classification report containing:
            - Request type
            - Priority level
            - Extracted information
            - Appropriate department to handle the request
            
            Example:
            {
                "request_type": "Billing inquiry",
                "priority": "Normal",
                "account_number": "123456789",
                "assigned_department": "Billing Department"
            }
            """
        )

    def handle_billing_inquiry_task(self, agent, context):
        """Task to handle billing inquiries"""
        return Task(
            description="""Handle the billing inquiry based on the received information.
            
            Please do the following:
            1. Clearly explain bill details
            2. Clarify how consumption is calculated
            3. Explain progressive tariffs if applicable
            4. Answer any additional inquiries
            5. Provide tips for saving consumption
            """,
            agent=agent,
            context=context,
            async_execution=True,  # Run in parallel
            expected_output="""Detailed bill explanation including:
            - Monthly consumption details
            - Tariff tiers and prices explanation
            - Total amount and its breakdown
            - Tips for reducing consumption
            - Available payment methods
            """
        )

    def handle_technical_issue_task(self, agent, context):
        """Task to handle technical faults"""
        return Task(
            description="""Handle the technical report based on the received information.
            
            Please do the following:
            1. Diagnose the technical problem
            2. Determine fault severity level
            3. Provide immediate solutions if possible
            4. Necessary safety instructions
            5. Determine need for technician visit
            6. Estimate repair time
            """,
            agent=agent,
            context=context,
            async_execution=True,  # Run in parallel with billing
            expected_output="""Technical report including:
            - Problem diagnosis
            - Severity level (high/medium/low)
            - Proposed immediate solutions
            - Safety instructions
            - Need for technician visit (yes/no)
            - Expected repair time
            - Report number for follow-up
            """
        )

    def compile_service_report_task(self, agent, context, callback_function):
        """Task to compile final customer report"""
        return Task(
            description="""Gather all information from different departments and prepare a comprehensive customer report.
            
            Please do the following:
            1. Compile all information from other agents
            2. Ensure all customer request points are addressed
            3. Prepare a clear and organized summary
            4. Add follow-up steps if necessary
            5. Add support contact information
            """,
            agent=agent,
            context=context,
            expected_output=f"""Comprehensive customer service report including:
            
            # Customer Service Report - Saudi Electric Company
            Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}
            
            ## Request Summary
            - Request type
            - Priority
            - Status
            
            ## Details
            - Information provided by each department
            - Proposed solutions
            - Actions taken
            
            ## Follow-up Steps
            - What the customer should do
            - Follow-up numbers
            - Expected resolution time
            
            ## Contact Information
            - Technical Support Number: 920000222
            - Website: www.se.com.sa
            - App: Saudi Electric Company App
            """,
            callback=callback_function
        )
