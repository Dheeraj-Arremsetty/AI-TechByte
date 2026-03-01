"""
Watsonx.ai Models Tool

This tool fetches information about foundation models available in IBM Watsonx.ai
from the official IBM models page.
"""

import sys
import os

# Add shared utilities to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'shared'))

from ibm_watsonx_orchestrate.agent_builder.tools import tool
from web_scraper_utils import fetch_page_content, extract_structured_content, format_as_markdown


@tool(name="bob_wxai_models_tool")
def get_watsonx_ai_models() -> str:
    """
    Fetches information about foundation models available in IBM Watsonx.ai.
    
    This tool retrieves information about the foundation models, their capabilities,
    specifications, and use cases. Use this tool when users ask about available models,
    model capabilities, or which models are supported in Watsonx.ai.
    
    Returns:
        str: Formatted Markdown content with Watsonx.ai foundation models information
    """
    url = "https://www.ibm.com/products/watsonx-ai/foundation-models"
    
    try:
        # Fetch the page content
        html = fetch_page_content(url)
        
        if not html:
            return f"❌ **Error:** Unable to fetch models information from {url}. The page may be temporarily unavailable."
        
        # Extract structured content
        content = extract_structured_content(html)
        
        # Format as Markdown
        markdown = format_as_markdown(
            content,
            title="IBM Watsonx.ai - Foundation Models"
        )
        
        # Add source citation
        markdown += f"\n\n---\n**Source:** [{url}]({url})\n"
        markdown += "**Last Updated:** Information retrieved from IBM's official website\n"
        
        return markdown
        
    except Exception as e:
        return f"❌ **Error:** An unexpected error occurred while fetching Watsonx.ai models information: {str(e)}"

# Made with Bob
