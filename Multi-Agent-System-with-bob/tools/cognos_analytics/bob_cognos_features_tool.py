"""
Cognos Analytics Features Tool

This tool fetches detailed feature information about IBM Cognos Analytics
from the official IBM features page.
"""

import sys
import os

# Add shared utilities to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'shared'))

from ibm_watsonx_orchestrate.agent_builder.tools import tool
from web_scraper_utils import fetch_page_content, extract_structured_content, format_as_markdown


@tool(name="bob_cognos_features_tool")
def get_cognos_analytics_features() -> str:
    """
    Fetches detailed feature information about IBM Cognos Analytics from the official IBM features page.
    
    This tool retrieves comprehensive information about Cognos Analytics features,
    capabilities, and technical specifications. Use this tool when users ask about
    specific features, capabilities, or what Cognos Analytics can do.
    
    Returns:
        str: Formatted Markdown content with Cognos Analytics features and capabilities
    """
    url = "https://www.ibm.com/products/cognos-analytics/features"
    
    try:
        # Fetch the page content
        html = fetch_page_content(url)
        
        if not html:
            return f"❌ **Error:** Unable to fetch features information from {url}. The page may be temporarily unavailable."
        
        # Extract structured content
        content = extract_structured_content(html)
        
        # Format as Markdown
        markdown = format_as_markdown(
            content,
            title="IBM Cognos Analytics - Features & Capabilities"
        )
        
        # Add source citation
        markdown += f"\n\n---\n**Source:** [{url}]({url})\n"
        markdown += "**Last Updated:** Information retrieved from IBM's official website\n"
        
        return markdown
        
    except Exception as e:
        return f"❌ **Error:** An unexpected error occurred while fetching Cognos Analytics features: {str(e)}"

# Made with Bob
