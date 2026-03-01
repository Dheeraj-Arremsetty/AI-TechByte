"""
Watsonx Orchestrate Information Tool

This tool fetches general product information about IBM Watsonx Orchestrate
from the official IBM product page.
"""

import sys
import os

# Add shared utilities to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'shared'))

from ibm_watsonx_orchestrate.agent_builder.tools import tool
from web_scraper_utils import fetch_page_content, extract_structured_content, format_as_markdown


@tool(name="bob_wxo_info_tool")
def get_watsonx_orchestrate_info() -> str:
    """
    Fetches general information about IBM Watsonx Orchestrate from the official IBM product page.
    
    This tool retrieves the product overview, key benefits, use cases, and general
    information about Watsonx Orchestrate. Use this tool when users ask about what
    Watsonx Orchestrate is, its purpose, or general product information.
    
    Returns:
        str: Formatted Markdown content with Watsonx Orchestrate product information
    """
    url = "https://www.ibm.com/products/watsonx-orchestrate"
    
    try:
        # Fetch the page content
        html = fetch_page_content(url)
        
        if not html:
            return f"❌ **Error:** Unable to fetch information from {url}. The page may be temporarily unavailable."
        
        # Extract structured content
        content = extract_structured_content(html)
        
        # Format as Markdown
        markdown = format_as_markdown(
            content,
            title="IBM Watsonx Orchestrate - Product Information"
        )
        
        # Add source citation
        markdown += f"\n\n---\n**Source:** [{url}]({url})\n"
        markdown += "**Last Updated:** Information retrieved from IBM's official website\n"
        
        return markdown
        
    except Exception as e:
        return f"❌ **Error:** An unexpected error occurred while fetching Watsonx Orchestrate information: {str(e)}"

# Made with Bob
