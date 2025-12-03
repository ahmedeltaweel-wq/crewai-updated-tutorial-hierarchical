from crewai.tools import BaseTool
from duckduckgo_search import DDGS

class SearchInternetTool(BaseTool):
    name: str = "Search the internet"
    description: str = "Useful to search the internet about a given topic and return relevant results"

    def _run(self, query: str) -> str:
        """Execute the search using DuckDuckGo."""
        print(f"Searching the internet for: {query}")
        try:
            # Use DuckDuckGo directly (no API key needed)
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=5))
            
            if not results:
                return "Sorry, I couldn't find anything about that."
            
            string = []
            for result in results:
                string.append('\n'.join([
                    f"Title: {result.get('title', '')}",
                    f"Link: {result.get('href', '')}",
                    f"Snippet: {result.get('body', '')}",
                    "\n-----------------"
                ]))
            
            return '\n'.join(string)
        except Exception as e:
            return f"Error searching: {str(e)}"

# Create an instance to be imported
search_tool = SearchInternetTool()
