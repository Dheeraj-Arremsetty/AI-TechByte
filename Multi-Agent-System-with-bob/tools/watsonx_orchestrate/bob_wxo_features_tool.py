"""
Watsonx Orchestrate Features Tool

This tool fetches detailed feature information about IBM Watsonx Orchestrate
from multiple official IBM feature pages.
"""

import sys
import os

# Add shared utilities to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'shared'))

from ibm_watsonx_orchestrate.agent_builder.tools import tool
from web_scraper_utils import scrape_multiple_pages


@tool(name="bob_wxo_features_tool")
def get_watsonx_orchestrate_features() -> str:
    """
    Fetches comprehensive feature information about IBM Watsonx Orchestrate from multiple official IBM pages.
    
    This tool retrieves detailed information about Watsonx Orchestrate features including:
    - AI Agent Builder capabilities
    - Agent Catalog
    - Governance and Observability
    - Multi-agent Orchestration
    
    Use this tool when users ask about specific features, capabilities, or what
    Watsonx Orchestrate can do.
    
    Returns:
        str: Formatted Markdown content with comprehensive Watsonx Orchestrate features
    """
    urls = [
        "https://www.ibm.com/products/watsonx-orchestrate/ai-agent-builder",
        "https://www.ibm.com/products/watsonx-orchestrate/agent-catalog",
        "https://www.ibm.com/products/watsonx-orchestrate/governance-and-observability",
        "https://www.ibm.com/products/watsonx-orchestrate/multi-agent-orchestration"
    ]
    
    try:
        # Scrape all feature pages
        markdown = "# IBM Watsonx Orchestrate - Features & Capabilities\n\n"
        markdown += "This comprehensive guide covers all major features of Watsonx Orchestrate.\n\n"
        markdown += scrape_multiple_pages(urls)
        
        # Add source citations
        markdown += "\n\n---\n## Sources\n"
        for url in urls:
            markdown += f"- [{url}]({url})\n"
        markdown += "\n**Last Updated:** Information retrieved from IBM's official website\n"
        
        return markdown
        
    except Exception as e:
        return f"❌ **Error:** An unexpected error occurred while fetching Watsonx Orchestrate features: {str(e)}"

# Made with Bob
