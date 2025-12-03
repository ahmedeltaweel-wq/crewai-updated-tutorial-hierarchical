"""
Rate-Limited LLM Wrapper
Adds automatic delay between API calls to avoid quota exhaustion
"""
import time
from crewai import LLM

class RateLimitedLLM:
    """Wrapper around CrewAI LLM that adds delay between calls"""
    
    def __init__(self, model, api_key, delay_seconds=6):
        """
        Args:
            model: Gemini model name (e.g., "gemini/gemini-2.0-flash-exp")
            api_key: Google API key
            delay_seconds: Seconds to wait between API calls (default: 6)
        """
        self.llm = LLM(model=model, api_key=api_key)
        self.delay_seconds = delay_seconds
        self.last_call_time = 0
        
    def __getattr__(self, name):
        """Pass through all attributes to the underlying LLM"""
        return getattr(self.llm, name)
    
    def call(self, *args, **kwargs):
        """Override call method to add delay"""
        # Calculate time since last call
        current_time = time.time()
        time_since_last_call = current_time - self.last_call_time
        
        # If not enough time has passed, wait
        if time_since_last_call < self.delay_seconds:
            wait_time = self.delay_seconds - time_since_last_call
            print(f"⏰ Waiting {wait_time:.1f}s to avoid quota limit...")
            time.sleep(wait_time)
        
        # Make the actual call
        result = self.llm.call(*args, **kwargs)
        
        # Update last call time
        self.last_call_time = time.time()
        
        return result
