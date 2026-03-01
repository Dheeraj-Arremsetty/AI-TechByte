# IBM Product Specialist Multi-Agent System

A sophisticated multi-agent system built on IBM watsonx Orchestrate that provides comprehensive information about IBM products through intelligent agent coordination and real-time web crawling.

## Overview

This system uses a supervisor agent to coordinate three specialized sub-agents, each expert in a specific IBM product. The agents use web crawling tools to fetch the latest information directly from IBM's official website, ensuring accurate and up-to-date responses.

### Products Covered

1. **IBM Cognos Analytics** - Business intelligence and analytics platform
2. **IBM Watsonx Orchestrate** - AI-powered automation and agent orchestration
3. **IBM Watsonx.ai** - Enterprise AI platform for building and deploying AI models

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│         bob_ibm_product_specialist_agent (Supervisor)       │
│                    Routes user queries                       │
└────────────────────┬────────────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│   Cognos     │ │   Watsonx    │ │  Watsonx.ai  │
│  Analytics   │ │  Orchestrate │ │    Agent     │
│    Agent     │ │    Agent     │ │              │
└──────┬───────┘ └──────┬───────┘ └──────┬───────┘
       │                │                │
   ┌───┴───┐        ┌───┴───┐      ┌────┴────┐
   │ Tools │        │ Tools │      │  Tools  │
   │ (3)   │        │ (3)   │      │  (4)    │
   └───────┘        └───────┘      └─────────┘
```

### Components

- **1 Supervisor Agent**: Intelligent routing and coordination
- **3 Sub-Agents**: Product specialists with domain expertise
- **10 Web Crawling Tools**: Real-time information retrieval from IBM websites
- **Shared Utilities**: Common web scraping functionality

## Features

✅ **Real-time Information**: Fetches latest data from IBM's official website  
✅ **Multi-Agent Coordination**: Intelligent routing to appropriate specialists  
✅ **Comprehensive Coverage**: Product info, features, pricing, and more  
✅ **GPT-OSS-120b Optimized**: Uses advanced reasoning capabilities  
✅ **Error Handling**: Robust error handling and retry logic  
✅ **Rate Limiting**: Respectful web crawling with built-in delays  
✅ **Markdown Formatting**: Clean, readable responses  
✅ **Source Citations**: Includes URLs for verification  

## Project Structure

```
orchestrate-project/
├── agents/                                    # Agent specifications
│   ├── bob_ibm_product_specialist_agent.yaml # Supervisor agent
│   ├── bob_cognos_analytics_agent.yaml       # Cognos specialist
│   ├── bob_watsonx_orchestrate_agent.yaml    # Orchestrate specialist
│   └── bob_watsonx_ai_agent.yaml             # Watsonx.ai specialist
├── tools/                                     # Web crawling tools
│   ├── shared/                                # Shared utilities
│   │   └── web_scraper_utils.py              # Python stdlib only!
│   ├── cognos_analytics/                      # Cognos tools (3)
│   │   ├── bob_cognos_info_tool.py
│   │   ├── bob_cognos_features_tool.py
│   │   └── bob_cognos_pricing_tool.py
│   ├── watsonx_orchestrate/                   # Orchestrate tools (3)
│   │   ├── bob_wxo_info_tool.py
│   │   ├── bob_wxo_features_tool.py
│   │   └── bob_wxo_pricing_tool.py
│   └── watsonx_ai/                            # Watsonx.ai tools (4)
│       ├── bob_wxai_info_tool.py
│       ├── bob_wxai_features_tool.py
│       ├── bob_wxai_models_tool.py
│       └── bob_wxai_pricing_tool.py
├── deploy.sh                                  # Automated deployment script
├── IMPLEMENTATION_PLAN.md                     # Detailed architecture plan
├── DEPLOYMENT.md                              # Deployment instructions
└── README.md                                  # This file
```

## Quick Start

### Prerequisites

- IBM watsonx Orchestrate instance
- IBM watsonx Orchestrate ADK installed
- Python 3.8 or higher
- Internet access for web crawling
- **No external dependencies required!** Uses only Python standard library

### Installation

1. **Install the ADK**:
   ```bash
   pip install ibm-watsonx-orchestrate
   ```

2. **Configure the ADK**:
   ```bash
   orchestrate configure
   ```

3. **Deploy the system**:
   ```bash
   cd orchestrate-project
   chmod +x deploy.sh
   ./deploy.sh
   orchestrate agents import -f agents/bob_watsonx_ai_agent.yaml
   
   # Import supervisor agent
   orchestrate agents import -f agents/bob_ibm_product_specialist_agent.yaml
   ```

4. **Test the system**:
   ```bash
   orchestrate agents chat -n bob_ibm_product_specialist_agent
   ```

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

## Usage Examples

### Single Product Query

```
User: "What is Cognos Analytics?"

System: [Routes to bob_cognos_analytics_agent]
→ Calls bob_cognos_info_tool
→ Returns comprehensive product information
```

### Feature Query

```
User: "Tell me about the AI agent builder in Watsonx Orchestrate"

System: [Routes to bob_watsonx_orchestrate_agent]
→ Calls bob_wxo_features_tool
→ Returns detailed feature information
```

### Model Query

```
User: "What foundation models are available in Watsonx.ai?"

System: [Routes to bob_watsonx_ai_agent]
→ Calls bob_wxai_models_tool
→ Returns list of available models
```

### Comparison Query

```
User: "Compare Watsonx Orchestrate and Watsonx.ai"

System: [Routes to both agents sequentially]
→ Gathers information from both
→ Provides comparative summary
```

## Agent Specifications

### Supervisor Agent: `bob_ibm_product_specialist_agent`

- **Role**: Routes queries to appropriate specialist agents
- **LLM**: groq/openai/gpt-oss-120b
- **Style**: Default (for routing)
- **Collaborators**: All 3 sub-agents
- **Tools**: None (delegates to sub-agents)

### Sub-Agent: `bob_cognos_analytics_agent`

- **Expertise**: IBM Cognos Analytics
- **LLM**: groq/openai/gpt-oss-120b
- **Style**: React (for tool reasoning)
- **Tools**: 
  - bob_cognos_info_tool
  - bob_cognos_features_tool
  - bob_cognos_pricing_tool

### Sub-Agent: `bob_watsonx_orchestrate_agent`

- **Expertise**: IBM Watsonx Orchestrate
- **LLM**: groq/openai/gpt-oss-120b
- **Style**: React (for tool reasoning)
- **Tools**:
  - bob_wxo_info_tool
  - bob_wxo_features_tool (crawls 4 pages)
  - bob_wxo_pricing_tool

### Sub-Agent: `bob_watsonx_ai_agent`

- **Expertise**: IBM Watsonx.ai
- **LLM**: groq/openai/gpt-oss-120b
- **Style**: React (for tool reasoning)
- **Tools**:
  - bob_wxai_info_tool
  - bob_wxai_features_tool (crawls 4 pages)
  - bob_wxai_models_tool
  - bob_wxai_pricing_tool

## Web Crawling Tools

All tools use the shared `web_scraper_utils.py` module which provides:

- HTTP request handling with retry logic
- HTML parsing with BeautifulSoup
- Structured content extraction
- Markdown formatting
- Multi-page crawling support
- Rate limiting and error handling

### Tool Dependencies

```
requests>=2.31.0
beautifulsoup4>=4.12.0
lxml>=4.9.0
```

## Configuration

### Model Configuration

The system uses `groq/openai/gpt-oss-120b` by default. To use a different model:

1. Edit the agent YAML files
2. Change the `llm` field to your preferred model
3. Re-import the agents

Example:
```yaml
llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
```

### Tool Configuration

Tools can be customized by editing the Python files:

- **Timeout**: Adjust `timeout` parameter in `fetch_page_content()`
- **Retries**: Adjust `retries` parameter in `fetch_page_content()`
- **Rate Limiting**: Adjust `time.sleep()` calls in `scrape_multiple_pages()`

## Monitoring and Maintenance

### Check System Status

```bash
# List all tools
orchestrate tools list

# List all agents
orchestrate agents list

# Get agent details
orchestrate agents get -n bob_ibm_product_specialist_agent -k native
```

### Update Components

```bash
# Update a tool
orchestrate tools remove -n bob_cognos_info_tool
orchestrate tools import -k python -f tools/cognos_analytics/bob_cognos_info_tool.py -r tools/cognos_analytics/requirements.txt

# Update an agent
orchestrate agents remove -n bob_cognos_analytics_agent -k native
orchestrate agents import -f agents/bob_cognos_analytics_agent.yaml
```

## Troubleshooting

### Common Issues

1. **Tool import fails**: Ensure shared utilities are accessible
2. **Agent import fails**: Ensure tools are imported first
3. **Web crawling errors**: Check internet connectivity and IBM website accessibility
4. **Model not found**: Verify GPT-OSS-120b is available or change to another model

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed troubleshooting.

## Performance Considerations

- **Response Time**: 10-30 seconds per query (includes web crawling)
- **Rate Limiting**: Built-in delays prevent overwhelming IBM servers
- **Caching**: Consider implementing caching for frequently accessed pages
- **Concurrent Requests**: Tools handle multiple pages efficiently

## Security Considerations

- **Web Scraping**: Tools identify themselves with proper User-Agent headers
- **Data Privacy**: No user data is stored; all information is fetched in real-time
- **API Keys**: No API keys required for public IBM website crawling
- **Rate Limiting**: Respectful crawling with delays between requests

## Future Enhancements

Potential improvements:

1. **Knowledge Base Integration**: Cache crawled data for faster retrieval
2. **Scheduled Updates**: Periodic re-crawling to keep information current
3. **Additional Products**: Expand to cover more IBM products
4. **Analytics**: Track query patterns and popular topics
5. **Multi-language Support**: Crawl and support multiple language versions
6. **PDF Support**: Extract information from PDF documents
7. **Semantic Search**: Use embeddings for better information retrieval

## Contributing

To extend this system:

1. **Add a new product**:
   - Create tools in `tools/new_product/`
   - Create agent specification in `agents/`
   - Add as collaborator to supervisor agent

2. **Add a new tool**:
   - Create Python file with `@tool` decorator
   - Add to appropriate agent's tools list
   - Import the tool

3. **Modify agent behavior**:
   - Edit agent YAML instructions
   - Re-import the agent

## Documentation

- [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) - Detailed architecture and design
- [DEPLOYMENT.md](DEPLOYMENT.md) - Step-by-step deployment guide
- [watsonx Orchestrate ADK Docs](https://developer.watson-orchestrate.ibm.com) - Official documentation

## License

This project is provided as-is for use with IBM watsonx Orchestrate.

## Support

For issues or questions:
- Review the documentation in this repository
- Check the [watsonx Orchestrate ADK documentation](https://developer.watson-orchestrate.ibm.com)
- Contact IBM support for platform-specific issues

## Acknowledgments

Built using:
- IBM watsonx Orchestrate Agent Development Kit (ADK)
- GPT-OSS-120b language model
- Python web scraping libraries (requests, BeautifulSoup)

---

**Version**: 1.0.0  
**Last Updated**: 2026-02-18  
**Author**: Bob (AI Software Engineer)