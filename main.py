from crewai import Crew, Process, LLM
from agents import AINewsLetterAgents
from tasks import AINewsLetterTasks
from file_io import save_markdown
import os

from dotenv import load_dotenv
load_dotenv()

# Initialize the agents and tasks
agents = AINewsLetterAgents()
tasks = AINewsLetterTasks()

from rate_limited_llm import RateLimitedLLM

# Initialize the Google Gemini language model with rate limiting
api_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
if not api_key:
    print("Error: GEMINI_API_KEY or GOOGLE_API_KEY not found in environment variables!")
    print("Please check your .env file.")
    exit(1)

# Use RateLimitedLLM to add 6-second delay between API calls
# This prevents quota exhaustion (10 requests/minute limit)
print("⚙️ Using rate-limited LLM (6s delay between calls to avoid quota limits)")
gemini_llm = RateLimitedLLM(
    model="gemini/gemini-2.0-flash-exp",
    api_key=api_key,
    delay_seconds=6  # Wait 6 seconds between each API call
)


# Instantiate the agents
# IMPORTANT: We must pass the LLM to each agent, otherwise they default to OpenAI
editor = agents.editor_agent(llm=gemini_llm)
news_fetcher = agents.news_fetcher_agent(llm=gemini_llm)
news_analyzer = agents.news_analyzer_agent(llm=gemini_llm)
newsletter_compiler = agents.newsletter_compiler_agent(llm=gemini_llm)

# Instantiate the tasks
fetch_news_task = tasks.fetch_news_task(news_fetcher)
analyze_news_task = tasks.analyze_news_task(news_analyzer, [fetch_news_task])
compile_newsletter_task = tasks.compile_newsletter_task(
    newsletter_compiler, [analyze_news_task], save_markdown)

# Form the crew
crew = Crew(
    agents=[editor, news_fetcher, news_analyzer, newsletter_compiler],
    tasks=[fetch_news_task, analyze_news_task, compile_newsletter_task],
    process=Process.hierarchical,
    manager_llm=gemini_llm,
    verbose=True
)

# Kick off the crew's work
results = crew.kickoff()

# Print the results
print("Crew Work Results:")
print(results)
