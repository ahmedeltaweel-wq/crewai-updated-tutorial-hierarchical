"""
Company Knowledge Loader
Loads company information from Markdown file for easy customization
"""

import os
from pathlib import Path

class CompanyKnowledge:
    def __init__(self, knowledge_file="company_knowledge.md"):
        """Initialize with company knowledge file"""
        self.knowledge_file = knowledge_file
        self.company_info = self._load_knowledge()
    
    def _load_knowledge(self):
        """Load knowledge from Markdown file"""
        try:
            file_path = Path(__file__).parent / self.knowledge_file
            
            if not file_path.exists():
                print(f"Warning: {self.knowledge_file} not found. Using default knowledge.")
                return self._get_default_knowledge()
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            return {
                "full_content": content,
                "file_path": str(file_path),
                "loaded": True
            }
        except Exception as e:
            print(f"Error loading knowledge file: {e}")
            return self._get_default_knowledge()
    
    def _get_default_knowledge(self):
        """Fallback default knowledge"""
        return {
            "full_content": "Default health insurance information.",
            "file_path": "built-in",
            "loaded": False
        }
    
    def get_full_knowledge(self):
        """Get complete knowledge base"""
        return self.company_info["full_content"]
    
    def get_summary(self):
        """Get knowledge base summary"""
        content = self.company_info["full_content"]
        lines = content.split('\n')
        
        # Extract key sections
        summary = []
        in_section = False
        
        for line in lines[:100]:  # First 100 lines for summary
            if line.startswith('##'):
                summary.append(line)
                in_section = True
            elif in_section and line.strip() and not line.startswith('#'):
                summary.append(line)
                in_section = False
        
        return '\n'.join(summary[:20])  # First 20 relevant lines
    
    def search_section(self, keyword):
        """Search for specific section in knowledge base"""
        content = self.company_info["full_content"]
        lines = content.split('\n')
        
        results = []
        capture = False
        section_lines = []
        
        for line in lines:
            if keyword.lower() in line.lower():
                capture = True
                section_lines = [line]
            elif capture:
                if line.startswith('##') or line.startswith('---'):
                    results.append('\n'.join(section_lines))
                    capture = False
                    section_lines = []
                else:
                    section_lines.append(line)
        
        if section_lines:
            results.append('\n'.join(section_lines))
        
        return '\n\n'.join(results) if results else None
    
    def reload(self):
        """Reload knowledge from file (useful when file is updated)"""
        self.company_info = self._load_knowledge()
        return self.company_info["loaded"]
