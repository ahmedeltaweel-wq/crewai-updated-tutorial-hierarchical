import os
# Auto-detect service account JSON for local deployment
_service_account_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'service-account-key.json')
if os.path.exists(_service_account_path) and not os.getenv('GOOGLE_APPLICATION_CREDENTIALS'):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = _service_account_path
    print(f"🔑 Auto-loaded Service Account: {_service_account_path}")

from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from crewai import Crew, Process
from agents import AINewsLetterAgents
from tasks import AINewsLetterTasks
from file_io import save_markdown
from rate_limited_llm import RateLimitedLLM
from dotenv import load_dotenv
import threading
import time
import os
import sys
from io import StringIO

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Global variables to track agent status
agent_status = {
    'editor': {'status': 'idle', 'message': 'Waiting to start...', 'progress': 0},
    'news_fetcher': {'status': 'idle', 'message': 'Waiting to start...', 'progress': 0},
    'news_analyzer': {'status': 'idle', 'message': 'Waiting to start...', 'progress': 0},
    'newsletter_compiler': {'status': 'idle', 'message': 'Waiting to start...', 'progress': 0}
}

crew_running = False
crew_results = None

class AgentLogger:
    """Custom logger to capture agent output and send to web interface"""
    def __init__(self, agent_name):
        self.agent_name = agent_name
        self.buffer = StringIO()
        
    def write(self, message):
        if message.strip():
            self.buffer.write(message)
            update_agent_status(self.agent_name, 'working', message.strip())
            
    def flush(self):
        pass

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

def run_crew_workflow():
    """Run the CrewAI workflow in a separate thread"""
    global crew_running, crew_results, agent_status
    
    try:
        crew_running = True
        
        # Reset all agents to idle
        for agent in agent_status:
            update_agent_status(agent, 'idle', 'Initializing...', 0)
        
        socketio.emit('workflow_started', {'message': 'Starting AI Newsletter Crew...'})
        
        # Initialize the agents and tasks
        update_agent_status('editor', 'working', 'Initializing Editor Agent...', 10)
        agents = AINewsLetterAgents()
        tasks = AINewsLetterTasks()
        
        # Initialize the Google Gemini language model
        update_agent_status('editor', 'working', 'Connecting to AI...', 20)
        
        api_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
        use_vertex = os.environ.get("USE_VERTEX_AI", "false").lower() == "true"
        
        from crewai import LLM
        gemini_llm = None
        
        if use_vertex:
            print("☁️ Using Google Cloud Vertex AI (Service Account)")
            project_id = os.environ.get("GOOGLE_CLOUD_PROJECT", "eg-konecta-sandbox")
            location = os.environ.get("VERTEX_AI_LOCATION", "us-central1")
            
            try:
                import vertexai
                vertexai.init(project=project_id, location=location)
                print(f"✅ Vertex AI initialized: {project_id} / {location}")
            except Exception as e:
                print(f"⚠️ Vertex AI init warning: {e}")
            
            gemini_llm = LLM(
                model="vertex_ai/gemini-2.0-flash-001",
                vertex_project=project_id,
                vertex_location=location,
                max_rpm=60  # Faster processing
            )
            print("✅ Vertex AI LLM ready (optimized)!")
        elif api_key:
            print("🔑 Using Gemini API Key")
            gemini_llm = RateLimitedLLM(
                model="gemini/gemini-2.0-flash-exp",
                api_key=api_key,
                delay_seconds=6
            )
        else:
            raise ValueError("No AI model available. Set USE_VERTEX_AI=true or provide GEMINI_API_KEY")
        
        # Instantiate the agents
        update_agent_status('editor', 'working', 'Setting up all agents...', 30)
        editor = agents.editor_agent(llm=gemini_llm)
        news_fetcher = agents.news_fetcher_agent(llm=gemini_llm)
        news_analyzer = agents.news_analyzer_agent(llm=gemini_llm)
        newsletter_compiler = agents.newsletter_compiler_agent(llm=gemini_llm)
        
        # Instantiate the tasks
        update_agent_status('news_fetcher', 'working', 'Preparing to fetch news...', 40)
        fetch_news_task = tasks.fetch_news_task(news_fetcher)
        
        update_agent_status('news_analyzer', 'working', 'Preparing to analyze news...', 50)
        analyze_news_task = tasks.analyze_news_task(news_analyzer, [fetch_news_task])
        
        update_agent_status('newsletter_compiler', 'working', 'Preparing to compile newsletter...', 60)
        compile_newsletter_task = tasks.compile_newsletter_task(
            newsletter_compiler, [analyze_news_task], save_markdown)
        
        # Form the crew (optimized)
        update_agent_status('editor', 'working', 'Forming the crew...', 70)
        crew = Crew(
            agents=[editor, news_fetcher, news_analyzer, newsletter_compiler],
            tasks=[fetch_news_task, analyze_news_task, compile_newsletter_task],
            process=Process.sequential,
            memory=True,
            cache=True,
            verbose=True
        )
        
        # Start the work
        update_agent_status('editor', 'working', 'Starting crew work...', 80)
        update_agent_status('news_fetcher', 'working', 'Fetching latest AI news...', 80)
        
        results = crew.kickoff()
        
        # Update all agents to completed
        update_agent_status('editor', 'completed', 'Newsletter creation completed!', 100)
        update_agent_status('news_fetcher', 'completed', 'News fetching completed!', 100)
        update_agent_status('news_analyzer', 'completed', 'News analysis completed!', 100)
        update_agent_status('newsletter_compiler', 'completed', 'Newsletter compilation completed!', 100)
        
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
    return render_template('index.html')

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

@socketio.on('start_crew')
def handle_start_crew():
    """Handle request to start the crew workflow"""
    global crew_running
    
    if not crew_running:
        thread = threading.Thread(target=run_crew_workflow)
        thread.daemon = True
        thread.start()
        emit('workflow_starting', {'message': 'Crew workflow is starting...'})
    else:
        emit('workflow_error', {'error': 'Crew is already running!'})

if __name__ == '__main__':
    print("🚀 Starting AI Newsletter Crew Web Interface...")
    print("📡 Open your browser at: http://localhost:5000")
    # In production, debug must be False. eventlet will be used if installed.
    socketio.run(app, debug=False, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
