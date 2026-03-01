# IBM Product Specialist Multi-Agent System - Deployment Guide

This guide provides step-by-step instructions for deploying the IBM Product Specialist multi-agent system to IBM watsonx Orchestrate.

## Prerequisites

Before deploying, ensure you have:

1. **IBM watsonx Orchestrate instance** - Access to a watsonx Orchestrate SaaS or on-premises instance
2. **ADK installed** - IBM watsonx Orchestrate Agent Development Kit (ADK)
   ```bash
   pip install ibm-watsonx-orchestrate
   ```
3. **ADK configured** - Connected to your watsonx Orchestrate instance
   ```bash
   orchestrate configure
   ```
4. **Internet access** - Required for web crawling tools to fetch IBM product information

## System Overview

The system consists of:
- **1 Supervisor Agent**: `bob_ibm_product_specialist_agent`
- **3 Sub-Agents**: 
  - `bob_cognos_analytics_agent`
  - `bob_watsonx_orchestrate_agent`
  - `bob_watsonx_ai_agent`
- **10 Web Crawling Tools**: 3 for Cognos, 3 for Watsonx Orchestrate, 4 for Watsonx.ai

## Deployment Steps

### Step 1: Import Tools

Tools must be imported before agents since agents depend on them.

#### 1.1 Cognos Analytics Tools

```bash
# Navigate to project directory
cd orchestrate-project

# Import Cognos info tool
orchestrate tools import -k python \
  -f tools/cognos_analytics/bob_cognos_info_tool.py \
  -r tools/cognos_analytics/requirements.txt

# Import Cognos features tool
orchestrate tools import -k python \
  -f tools/cognos_analytics/bob_cognos_features_tool.py \
  -r tools/cognos_analytics/requirements.txt

# Import Cognos pricing tool
orchestrate tools import -k python \
  -f tools/cognos_analytics/bob_cognos_pricing_tool.py \
  -r tools/cognos_analytics/requirements.txt
```

#### 1.2 Watsonx Orchestrate Tools

```bash
# Import Watsonx Orchestrate info tool
orchestrate tools import -k python \
  -f tools/watsonx_orchestrate/bob_wxo_info_tool.py \
  -r tools/watsonx_orchestrate/requirements.txt

# Import Watsonx Orchestrate features tool
orchestrate tools import -k python \
  -f tools/watsonx_orchestrate/bob_wxo_features_tool.py \
  -r tools/watsonx_orchestrate/requirements.txt

# Import Watsonx Orchestrate pricing tool
orchestrate tools import -k python \
  -f tools/watsonx_orchestrate/bob_wxo_pricing_tool.py \
  -r tools/watsonx_orchestrate/requirements.txt
```

#### 1.3 Watsonx.ai Tools

```bash
# Import Watsonx.ai info tool
orchestrate tools import -k python \
  -f tools/watsonx_ai/bob_wxai_info_tool.py \
  -r tools/watsonx_ai/requirements.txt

# Import Watsonx.ai features tool
orchestrate tools import -k python \
  -f tools/watsonx_ai/bob_wxai_features_tool.py \
  -r tools/watsonx_ai/requirements.txt

# Import Watsonx.ai models tool
orchestrate tools import -k python \
  -f tools/watsonx_ai/bob_wxai_models_tool.py \
  -r tools/watsonx_ai/requirements.txt

# Import Watsonx.ai pricing tool
orchestrate tools import -k python \
  -f tools/watsonx_ai/bob_wxai_pricing_tool.py \
  -r tools/watsonx_ai/requirements.txt
```

#### 1.4 Verify Tool Import

```bash
# List all imported tools
orchestrate tools list

# You should see all 10 tools listed:
# - bob_cognos_info_tool
# - bob_cognos_features_tool
# - bob_cognos_pricing_tool
# - bob_wxo_info_tool
# - bob_wxo_features_tool
# - bob_wxo_pricing_tool
# - bob_wxai_info_tool
# - bob_wxai_features_tool
# - bob_wxai_models_tool
# - bob_wxai_pricing_tool
```

### Step 2: Import Sub-Agents

Sub-agents must be imported before the supervisor agent since the supervisor depends on them as collaborators.

```bash
# Import Cognos Analytics agent
orchestrate agents import -f agents/bob_cognos_analytics_agent.yaml

# Import Watsonx Orchestrate agent
orchestrate agents import -f agents/bob_watsonx_orchestrate_agent.yaml

# Import Watsonx.ai agent
orchestrate agents import -f agents/bob_watsonx_ai_agent.yaml
```

#### 2.1 Verify Sub-Agent Import

```bash
# List all imported agents
orchestrate agents list

# You should see the three sub-agents:
# - bob_cognos_analytics_agent
# - bob_watsonx_orchestrate_agent
# - bob_watsonx_ai_agent
```

### Step 3: Import Supervisor Agent

```bash
# Import the supervisor agent
orchestrate agents import -f agents/bob_ibm_product_specialist_agent.yaml
```

#### 3.1 Verify Supervisor Agent Import

```bash
# List all agents
orchestrate agents list

# You should now see all four agents:
# - bob_ibm_product_specialist_agent (supervisor)
# - bob_cognos_analytics_agent
# - bob_watsonx_orchestrate_agent
# - bob_watsonx_ai_agent
```

### Step 4: Test the System

#### 4.1 Test Individual Sub-Agents

Test each sub-agent independently before testing the full system:

```bash
# Test Cognos Analytics agent
orchestrate agents chat -n bob_cognos_analytics_agent

# Try these test queries:
# - "What is Cognos Analytics?"
# - "What are the key features?"
# - "How much does it cost?"
```

```bash
# Test Watsonx Orchestrate agent
orchestrate agents chat -n bob_watsonx_orchestrate_agent

# Try these test queries:
# - "What is Watsonx Orchestrate?"
# - "Tell me about the AI agent builder"
# - "What are the pricing options?"
```

```bash
# Test Watsonx.ai agent
orchestrate agents chat -n bob_watsonx_ai_agent

# Try these test queries:
# - "What is Watsonx.ai?"
# - "What foundation models are available?"
# - "Tell me about RAG development"
```

#### 4.2 Test Supervisor Agent

Test the full multi-agent system:

```bash
# Start chat with supervisor agent
orchestrate agents chat -n bob_ibm_product_specialist_agent

# Try these test queries:
# - "What is Cognos Analytics?"
# - "Tell me about Watsonx Orchestrate features"
# - "What models are available in Watsonx.ai?"
# - "Compare Watsonx Orchestrate and Watsonx.ai"
# - "Tell me about all three products"
```

## Deployment Script

For convenience, here's a complete deployment script:

```bash
#!/bin/bash

# IBM Product Specialist Multi-Agent System Deployment Script

set -e  # Exit on error

echo "Starting deployment of IBM Product Specialist Multi-Agent System..."

# Navigate to project directory
cd orchestrate-project

echo ""
echo "Step 1: Importing Cognos Analytics tools..."
orchestrate tools import -k python -f tools/cognos_analytics/bob_cognos_info_tool.py -r tools/cognos_analytics/requirements.txt
orchestrate tools import -k python -f tools/cognos_analytics/bob_cognos_features_tool.py -r tools/cognos_analytics/requirements.txt
orchestrate tools import -k python -f tools/cognos_analytics/bob_cognos_pricing_tool.py -r tools/cognos_analytics/requirements.txt

echo ""
echo "Step 2: Importing Watsonx Orchestrate tools..."
orchestrate tools import -k python -f tools/watsonx_orchestrate/bob_wxo_info_tool.py -r tools/watsonx_orchestrate/requirements.txt
orchestrate tools import -k python -f tools/watsonx_orchestrate/bob_wxo_features_tool.py -r tools/watsonx_orchestrate/requirements.txt
orchestrate tools import -k python -f tools/watsonx_orchestrate/bob_wxo_pricing_tool.py -r tools/watsonx_orchestrate/requirements.txt

echo ""
echo "Step 3: Importing Watsonx.ai tools..."
orchestrate tools import -k python -f tools/watsonx_ai/bob_wxai_info_tool.py -r tools/watsonx_ai/requirements.txt
orchestrate tools import -k python -f tools/watsonx_ai/bob_wxai_features_tool.py -r tools/watsonx_ai/requirements.txt
orchestrate tools import -k python -f tools/watsonx_ai/bob_wxai_models_tool.py -r tools/watsonx_ai/requirements.txt
orchestrate tools import -k python -f tools/watsonx_ai/bob_wxai_pricing_tool.py -r tools/watsonx_ai/requirements.txt

echo ""
echo "Step 4: Importing sub-agents..."
orchestrate agents import -f agents/bob_cognos_analytics_agent.yaml
orchestrate agents import -f agents/bob_watsonx_orchestrate_agent.yaml
orchestrate agents import -f agents/bob_watsonx_ai_agent.yaml

echo ""
echo "Step 5: Importing supervisor agent..."
orchestrate agents import -f agents/bob_ibm_product_specialist_agent.yaml

echo ""
echo "Deployment complete!"
echo ""
echo "Verify deployment with:"
echo "  orchestrate tools list"
echo "  orchestrate agents list"
echo ""
echo "Test the system with:"
echo "  orchestrate agents chat -n bob_ibm_product_specialist_agent"
```

Save this as `deploy.sh` and run:

```bash
chmod +x deploy.sh
./deploy.sh
```

## Troubleshooting

### Tool Import Failures

**Issue**: Tool import fails with "module not found" error

**Solution**: Ensure the shared utilities are accessible. The tools use relative imports to access `web_scraper_utils.py`. If this fails, you may need to adjust the Python path or copy the shared utilities to each tool directory.

### Agent Import Failures

**Issue**: Agent import fails with "tool not found" error

**Solution**: Ensure all tools are imported before importing agents. Tools must exist before agents that use them can be imported.

**Issue**: Supervisor agent import fails with "collaborator not found" error

**Solution**: Ensure all sub-agents are imported before importing the supervisor agent.

### Web Crawling Issues

**Issue**: Tools return errors about unable to fetch pages

**Solution**: 
- Check internet connectivity
- Verify IBM website URLs are accessible
- Check for rate limiting (wait a few minutes and try again)
- Ensure firewall/proxy settings allow outbound HTTPS connections

### Model Issues

**Issue**: Agent fails with "model not found" error

**Solution**: Ensure `groq/openai/gpt-oss-120b` model is available in your environment:

```bash
orchestrate models list
```

If not available, you can either:
1. Add the model (if you have Groq API access)
2. Change the LLM in agent YAML files to an available model like `watsonx/meta-llama/llama-3-2-90b-vision-instruct`

## Updating the System

### Updating Tools

To update a tool:

```bash
# Remove the old tool
orchestrate tools remove -n bob_cognos_info_tool

# Import the updated tool
orchestrate tools import -k python \
  -f tools/cognos_analytics/bob_cognos_info_tool.py \
  -r tools/cognos_analytics/requirements.txt
```

### Updating Agents

To update an agent:

```bash
# Remove the old agent
orchestrate agents remove -n bob_cognos_analytics_agent -k native

# Import the updated agent
orchestrate agents import -f agents/bob_cognos_analytics_agent.yaml
```

**Note**: When updating the supervisor agent, you may need to remove and re-import it if collaborator relationships change.

## Monitoring and Maintenance

### Check Tool Status

```bash
# List all tools
orchestrate tools list

# Get details of a specific tool
orchestrate tools get -n bob_cognos_info_tool
```

### Check Agent Status

```bash
# List all agents
orchestrate agents list

# Get details of a specific agent
orchestrate agents get -n bob_ibm_product_specialist_agent -k native
```

### View Logs

Check logs for debugging:

```bash
# View agent execution logs (if available in your environment)
orchestrate logs --agent bob_ibm_product_specialist_agent
```

## Best Practices

1. **Test incrementally**: Test each tool and agent individually before testing the full system
2. **Monitor performance**: Track response times and adjust timeout settings if needed
3. **Update regularly**: Keep tools updated to ensure they work with any IBM website changes
4. **Rate limiting**: Be respectful of IBM's servers; the tools include built-in delays
5. **Error handling**: Tools include comprehensive error handling, but monitor for issues
6. **Documentation**: Keep this deployment guide updated with any customizations

## Support

For issues or questions:
- Check the [watsonx Orchestrate ADK documentation](https://developer.watson-orchestrate.ibm.com)
- Review the [IMPLEMENTATION_PLAN.md](IMPLEMENTATION_PLAN.md) for architecture details
- Contact IBM support for platform-specific issues

## Next Steps

After successful deployment:
1. Test with various queries to ensure proper routing
2. Monitor tool performance and response quality
3. Gather user feedback
4. Consider adding more products or features
5. Implement caching for frequently accessed information
6. Add analytics to track usage patterns

---

**Deployment Date**: [Add date when deployed]  
**Deployed By**: [Add your name]  
**Environment**: [Add environment details]