"""
Shared web scraping utilities for IBM product information tools.

This module provides common functions for fetching and parsing web pages
from IBM product websites using only Python standard library.
"""

import urllib.request
import urllib.error
from html.parser import HTMLParser
from typing import Dict, List, Optional
import time
import re


class SimpleHTMLParser(HTMLParser):
    """Simple HTML parser to extract text content."""
    
    def __init__(self):
        super().__init__()
        self.content = {
            'headings': [],
            'paragraphs': [],
            'lists': []
        }
        self.current_tag = None
        self.current_data = []
    
    def handle_starttag(self, tag, attrs):
        if tag in ['h1', 'h2', 'h3', 'p', 'li']:
            self.current_tag = tag
            self.current_data = []
    
    def handle_endtag(self, tag):
        if self.current_tag and tag == self.current_tag:
            text = ''.join(self.current_data).strip()
            if text and len(text) > 10:
                if tag in ['h1', 'h2', 'h3']:
                    self.content['headings'].append(text)
                elif tag == 'p':
                    self.content['paragraphs'].append(text)
                elif tag == 'li':
                    self.content['lists'].append(text)
            self.current_tag = None
            self.current_data = []
    
    def handle_data(self, data):
        if self.current_tag:
            self.current_data.append(data)


def fetch_page_content(url: str, timeout: int = 30, retries: int = 3) -> Optional[str]:
    """
    Fetch HTML content from a URL with retry logic.
    
    Args:
        url (str): The URL to fetch
        timeout (int): Request timeout in seconds
        retries (int): Number of retry attempts
    
    Returns:
        Optional[str]: HTML content or None if failed
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; IBMProductBot/1.0)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return response.read().decode('utf-8')
        except urllib.error.URLError as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
                continue
            return None
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            return None
    
    return None


def parse_html_content(html: str) -> Dict[str, List[str]]:
    """
    Parse HTML content and extract structured data.
    
    Args:
        html (str): HTML content to parse
    
    Returns:
        Dict[str, List[str]]: Structured content organized by type
    """
    parser = SimpleHTMLParser()
    try:
        parser.feed(html)
    except Exception:
        pass  # Ignore parsing errors
    
    return parser.content


def extract_structured_content(html: str) -> Dict[str, List[str]]:
    """
    Extract structured content (headings, paragraphs, lists) from HTML.
    
    Args:
        html (str): HTML content string
    
    Returns:
        Dict[str, List[str]]: Structured content organized by type
    """
    return parse_html_content(html)


def format_as_markdown(content: Dict[str, List[str]], title: str = "") -> str:
    """
    Format extracted content as Markdown.
    
    Args:
        content (Dict[str, List[str]]): Structured content
        title (str): Optional title for the document
    
    Returns:
        str: Formatted Markdown content
    """
    markdown = []
    
    if title:
        markdown.append(f"# {title}\n")
    
    # Add headings
    if content.get('headings'):
        for heading in content['headings'][:10]:  # Limit to first 10
            markdown.append(f"## {heading}\n")
    
    # Add paragraphs
    if content.get('paragraphs'):
        markdown.append("\n### Key Information\n")
        for para in content['paragraphs'][:15]:  # Limit to first 15
            markdown.append(f"{para}\n")
    
    # Add list items
    if content.get('lists'):
        markdown.append("\n### Features & Highlights\n")
        for item in content['lists'][:20]:  # Limit to first 20
            markdown.append(f"- {item}")
    
    return "\n".join(markdown)


def scrape_multiple_pages(urls: List[str]) -> str:
    """
    Scrape multiple pages and combine their content.
    
    Args:
        urls (List[str]): List of URLs to scrape
    
    Returns:
        str: Combined Markdown content from all pages
    """
    all_content = []
    
    for i, url in enumerate(urls):
        html = fetch_page_content(url)
        if html:
            content = parse_html_content(html)
            
            # Create a title from the URL
            page_title = f"Page {i+1}: {url.split('/')[-1].replace('-', ' ').title()}"
            markdown = format_as_markdown(content, page_title)
            all_content.append(markdown)
            
            # Rate limiting - be respectful to IBM servers
            if i < len(urls) - 1:
                time.sleep(1)
        else:
            all_content.append(f"\n## Error\nFailed to fetch content from: {url}\n")
    
    return "\n\n---\n\n".join(all_content)


def clean_text(text: str) -> str:
    """
    Clean and normalize text content.
    
    Args:
        text (str): Text to clean
    
    Returns:
        str: Cleaned text
    """
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    # Remove common unwanted patterns
    text = text.replace('\n\n\n', '\n\n')
    text = text.replace('  ', ' ')
    
    return text.strip()

# Made with Bob
