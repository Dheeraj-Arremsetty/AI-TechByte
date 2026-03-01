"""
Watsonx.ai Features Tool

This tool fetches detailed feature information about IBM Watsonx.ai
from multiple official IBM feature pages.
"""

import sys
import os

# Add shared utilities to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'shared'))

from ibm_watsonx_orchestrate.agent_builder.tools import tool
from web_scraper_utils import scrape_multiple_pages


@tool(name="bob_wxai_features_tool")
def get_watsonx_ai_features() -> str:
    """
    Fetches comprehensive feature information about IBM Watsonx.ai from multiple official IBM pages.
    
    This tool retrieves detailed information about Watsonx.ai features including:
    - AI Agent Development
    - Model Customization
    - RAG Development
    - Knowledge Management
    
    Use this tool when users ask about specific features, capabilities, or what
    Watsonx.ai can do.
    
    Returns:
        str: Formatted Markdown content with comprehensive Watsonx.ai features
    """
    urls = [
        "https://www.ibm.com/products/watsonx-ai/ai-agent-development",
        "https://www.ibm.com/products/watsonx-ai/model-customization",
        "https://www.ibm.com/products/watsonx-ai/rag-development",
        "https://www.ibm.com/products/watsonx-ai/knowledge-management"
    ]
    
    try:
        # Scrape all feature pages
        markdown = "# IBM Watsonx.ai - Features & Capabilities\n\n"
        markdown += "This comprehensive guide covers all major features of Watsonx.ai.\n\n"
        markdown += scrape_multiple_pages(urls)
        
        # Add source citations
        markdown += "\n\n---\n## Sources\n"
        for url in urls:
            markdown += f"- [{url}]({url})\n"
        markdown += "\n**Last Updated:** Information retrieved from IBM's official website\n"
        
        return markdown
        
    except Exception as e:
        return f"❌ **Error:** An unexpected error occurred while fetching Watsonx.ai features: {str(e)}"

# Made with Bob
