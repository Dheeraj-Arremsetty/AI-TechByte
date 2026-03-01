"""
Watsonx Orchestrate Pricing Tool

This tool fetches pricing information about IBM Watsonx Orchestrate
from the official IBM pricing page.
"""

import sys
import os

# Add shared utilities to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'shared'))

from ibm_watsonx_orchestrate.agent_builder.tools import tool
from web_scraper_utils import fetch_page_content, extract_structured_content, format_as_markdown


@tool(name="bob_wxo_pricing_tool")
def get_watsonx_orchestrate_pricing() -> str:
    """
    Fetches pricing information about IBM Watsonx Orchestrate from the official IBM pricing page.
    
    This tool retrieves information about Watsonx Orchestrate pricing plans, tiers,
    and cost details. Use this tool when users ask about pricing, costs, plans,
    or subscription options for Watsonx Orchestrate.
    
    Returns:
        str: Formatted Markdown content with Watsonx Orchestrate pricing information
    """
    url = "https://www.ibm.com/products/watsonx-orchestrate/pricing"
    
    try:
        # Fetch the page content
        html = fetch_page_content(url)
        
        if not html:
            return f"❌ **Error:** Unable to fetch pricing information from {url}. The page may be temporarily unavailable."
        
        # Extract structured content
        content = extract_structured_content(html)
        
        # Format as Markdown
        markdown = format_as_markdown(
            content,
            title="IBM Watsonx Orchestrate - Pricing Information"
        )
        
        # Add source citation
        markdown += f"\n\n---\n**Source:** [{url}]({url})\n"
        markdown += "**Last Updated:** Information retrieved from IBM's official website\n"
        markdown += "\n**Note:** For the most accurate and up-to-date pricing, please contact IBM sales or visit the official website.\n"
        
        return markdown
        
    except Exception as e:
        return f"❌ **Error:** An unexpected error occurred while fetching Watsonx Orchestrate pricing: {str(e)}"

# Made with Bob
