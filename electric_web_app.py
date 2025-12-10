# Eventlet monkey patching must be first!
print("🚀 Starting Electric Web App...")
import eventlet
print("  ✓ eventlet imported")
eventlet.monkey_patch()
print("  ✓ monkey_patch done")

import os
print("  ✓ os imported")
# Auto-detect service account JSON for local deployment
_service_account_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'service-account-key.json')
if os.path.exists(_service_account_path) and not os.getenv('GOOGLE_APPLICATION_CREDENTIALS'):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = _service_account_path
    print(f"  🔑 Auto-loaded Service Account: {_service_account_path}")

from flask import Flask, render_template, jsonify, request
print("  ✓ flask imported")
from flask_socketio import SocketIO, emit
print("  ✓ flask_socketio imported")
from flask_cors import CORS
print("  ✓ flask_cors imported")
from crewai import Crew, Process, LLM
print("  ✓ crewai imported")
from electric_agents import SaudiElectricAgents
print("  ✓ electric_agents imported")
from electric_tasks import SaudiElectricTasks
print("  ✓ electric_tasks imported")
from electric_file_io import save_service_report
print("  ✓ electric_file_io imported")
from dotenv import load_dotenv
print("  ✓ dotenv imported")
import threading
print("  ✓ All imports complete!")

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'saudi-electric-secret-key'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Global variables to track agent status
agent_status = {
    'call_receiver': {'status': 'idle', 'message': 'Ready to receive requests...', 'progress': 0},
    'billing_specialist': {'status': 'idle', 'message': 'Ready to answer billing inquiries...', 'progress': 0},
    'technical_support': {'status': 'idle', 'message': 'Ready to receive fault reports...', 'progress': 0},
    'service_coordinator': {'status': 'idle', 'message': 'Ready to coordinate service...', 'progress': 0}
}

crew_running = False
crew_results = None
customer_request = "I want to inquire about my last electricity bill, the amount is very high"

def update_agent_status(agent_name, status, message, progress=None):
    """Update agent status and emit to all connected clients"""
    global agent_status
    
    if agent_name in agent_status:
        agent_status[agent_name]['status'] = status
        agent_status[agent_name]['message'] = message
        if progress is not None:
            agent_status[agent_name]['progress'] = progress
        
        socketio.emit('agent_update', {
            'agent': agent_name,
            'status': status,
            'message': message,
            'progress': agent_status[agent_name]['progress']
        })

def run_customer_service_workflow(request_text):
    """Run the customer service workflow"""
    global crew_running, crew_results, agent_status, customer_request
    
    customer_request = request_text
    
    try:
        crew_running = True
        
        # Reset all agents
        for agent in agent_status:
            update_agent_status(agent, 'idle', 'Preparing...', 0)
        
        socketio.emit('workflow_started', {'message': 'Starting customer service...'})
        
        # Initialize agents and tasks
        update_agent_status('call_receiver', 'working', 'Initializing system...', 10)
        agents = SaudiElectricAgents()
        tasks = SaudiElectricTasks()
        
        # Initialize Gemini LLM
        update_agent_status('call_receiver', 'working', 'Connecting to AI system...', 20)
        
        api_key = os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY")
        use_vertex = os.environ.get("USE_VERTEX_AI", "false").lower() == "true"
        
        gemini_llm = None
        
        if use_vertex:
            print("☁️ Using Google Cloud Vertex AI (Service Account)")
            project_id = os.environ.get("GOOGLE_CLOUD_PROJECT", "eg-konecta-sandbox")
            location = os.environ.get("VERTEX_AI_LOCATION", "us-central1")
            
            # Initialize Vertex AI first
            try:
                import vertexai
                vertexai.init(project=project_id, location=location)
                print(f"✅ Vertex AI initialized: {project_id} / {location}")
            except Exception as e:
                print(f"⚠️ Vertex AI init warning: {e}")
            
            # Use Vertex AI model with CrewAI (optimized for speed)
            gemini_llm = LLM(
                model="vertex_ai/gemini-2.0-flash-001",
                vertex_project=project_id,
                vertex_location=location,
                max_rpm=60  # 60 requests per minute for faster processing
            )
            print("✅ Vertex AI LLM ready (optimized)!")
        
        # Fallback to API Key if Vertex AI not configured or failed
        if gemini_llm is None and api_key:
            print("🔑 Using Gemini API Key")
            gemini_llm = LLM(
                model="gemini/gemini-2.0-flash-001",
                api_key=api_key,
                max_rpm=60  # 60 requests per minute
            )
        
        if gemini_llm is None:
            raise Exception("No AI model available. Set USE_VERTEX_AI=true or provide GEMINI_API_KEY.")

        
        # Create agents
        update_agent_status('call_receiver', 'working', 'Preparing service team...', 30)
        call_receiver = agents.call_receiver_agent(llm=gemini_llm)
        billing_specialist = agents.billing_specialist_agent(llm=gemini_llm)
        technical_support = agents.technical_support_agent(llm=gemini_llm)
        service_coordinator = agents.service_coordinator_agent(llm=gemini_llm)
        
        # Create tasks
        update_agent_status('call_receiver', 'working', 'Receiving customer request...', 40)
        receive_task = tasks.receive_customer_request_task(call_receiver, customer_request)
        
        update_agent_status('billing_specialist', 'working', 'Analyzing request...', 50)
        billing_task = tasks.handle_billing_inquiry_task(billing_specialist, [receive_task])
        
        update_agent_status('technical_support', 'working', 'Checking technical aspects...', 60)
        technical_task = tasks.handle_technical_issue_task(technical_support, [receive_task])
        
        update_agent_status('service_coordinator', 'working', 'Preparing final report...', 70)
        compile_task = tasks.compile_service_report_task(
            service_coordinator, [receive_task, billing_task, technical_task], save_service_report)
        
        # Form the crew (optimized with caching)
        update_agent_status('service_coordinator', 'working', 'Forming service team...', 80)
        crew = Crew(
            agents=[call_receiver, billing_specialist, technical_support, service_coordinator],
            tasks=[receive_task, billing_task, technical_task, compile_task],
            process=Process.sequential,
            cache=True,    # Cache repeated queries
            verbose=True
        )
        
        # Start the work
        update_agent_status('call_receiver', 'working', 'Processing request...', 90)
        results = crew.kickoff()
        
        # Update all agents to completed
        update_agent_status('call_receiver', 'completed', 'Request received successfully!', 100)
        update_agent_status('billing_specialist', 'completed', 'Billing processed!', 100)
        update_agent_status('technical_support', 'completed', 'Technical check completed!', 100)
        update_agent_status('service_coordinator', 'completed', 'Report prepared!', 100)
        
        crew_results = str(results)
        socketio.emit('workflow_completed', {'results': crew_results})
        
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print(f"Workflow Error: {error_msg}")
        for agent in agent_status:
            update_agent_status(agent, 'error', error_msg, 0)
        socketio.emit('workflow_error', {'error': error_msg})
    
    finally:
        crew_running = False

@app.route('/')
def index():
    """Serve the main web interface"""
    return render_template('electric_index.html')

@app.route('/api/status')
def get_status():
    """Get current status of all agents"""
    return jsonify({
        'agents': agent_status,
        'running': crew_running,
        'results': crew_results
    })

@socketio.on('connect')
def handle_connect():
    """Handle client connection"""
    emit('connected', {'agents': agent_status, 'running': crew_running})

@socketio.on('start_service')
def handle_start_service(data):
    """Handle request to start customer service"""
    global crew_running
    
    if not crew_running:
        request_text = data.get('request', customer_request)
        thread = threading.Thread(target=run_customer_service_workflow, args=(request_text,))
        thread.daemon = True
        thread.start()
        emit('workflow_starting', {'message': 'Starting customer service...'})
    else:
        emit('workflow_error', {'error': 'System is currently processing another request!'})

if __name__ == '__main__':
    print("🏢 Starting Saudi Electric Company Customer Service System...")
    port = int(os.environ.get('PORT', 8080))
    print(f"📡 Open your browser at: http://localhost:{port}")
    # In production, debug must be False. eventlet will be used if installed.
    socketio.run(app, debug=False, host='0.0.0.0', port=port, allow_unsafe_werkzeug=True)
