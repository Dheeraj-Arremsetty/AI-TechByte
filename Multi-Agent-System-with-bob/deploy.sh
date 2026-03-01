#!/bin/bash

# IBM Product Specialist Multi-Agent System - Deployment Script
# This script deploys all tools and agents to watsonx Orchestrate
# Uses only Python standard library - no external dependencies required

set -e  # Exit on any error

echo "=========================================="
echo "IBM Product Specialist Deployment"
echo "=========================================="
echo ""
echo "ℹ️  This system uses only Python standard library"
echo "ℹ️  No external dependencies required!"
echo ""

# Step 1: Import Cognos Analytics Tools
echo "=================================================="
echo "Step 1: Importing Cognos Analytics Tools"
echo "=================================================="
echo "📦 Importing bob_cognos_info_tool..."
orchestrate tools import -k python -f tools/cognos_analytics/bob_cognos_info_tool.py

echo "📦 Importing bob_cognos_features_tool..."
orchestrate tools import -k python -f tools/cognos_analytics/bob_cognos_features_tool.py

echo "📦 Importing bob_cognos_pricing_tool..."
orchestrate tools import -k python -f tools/cognos_analytics/bob_cognos_pricing_tool.py

echo "✅ Cognos Analytics tools imported successfully"
echo ""

# Step 2: Import Watsonx Orchestrate Tools
echo "=================================================="
echo "Step 2: Importing Watsonx Orchestrate Tools"
echo "=================================================="
echo "📦 Importing bob_wxo_info_tool..."
orchestrate tools import -k python -f tools/watsonx_orchestrate/bob_wxo_info_tool.py

echo "📦 Importing bob_wxo_features_tool..."
orchestrate tools import -k python -f tools/watsonx_orchestrate/bob_wxo_features_tool.py

echo "📦 Importing bob_wxo_pricing_tool..."
orchestrate tools import -k python -f tools/watsonx_orchestrate/bob_wxo_pricing_tool.py

echo "✅ Watsonx Orchestrate tools imported successfully"
echo ""

# Step 3: Import Watsonx.ai Tools
echo "=================================================="
echo "Step 3: Importing Watsonx.ai Tools"
echo "=================================================="
echo "📦 Importing bob_wxai_info_tool..."
orchestrate tools import -k python -f tools/watsonx_ai/bob_wxai_info_tool.py

echo "📦 Importing bob_wxai_features_tool..."
orchestrate tools import -k python -f tools/watsonx_ai/bob_wxai_features_tool.py

echo "📦 Importing bob_wxai_models_tool..."
orchestrate tools import -k python -f tools/watsonx_ai/bob_wxai_models_tool.py

echo "📦 Importing bob_wxai_pricing_tool..."
orchestrate tools import -k python -f tools/watsonx_ai/bob_wxai_pricing_tool.py

echo "✅ Watsonx.ai tools imported successfully"
echo ""

# Step 4: Import Sub-Agents
echo "=================================================="
echo "Step 4: Importing Sub-Agents"
echo "=================================================="
echo "🤖 Importing bob_cognos_analytics_agent..."
orchestrate agents import -f agents/bob_cognos_analytics_agent.yaml

echo "🤖 Importing bob_watsonx_orchestrate_agent..."
orchestrate agents import -f agents/bob_watsonx_orchestrate_agent.yaml

echo "🤖 Importing bob_watsonx_ai_agent..."
orchestrate agents import -f agents/bob_watsonx_ai_agent.yaml

echo "✅ Sub-agents imported successfully"
echo ""

# Step 5: Import Supervisor Agent
echo "=================================================="
echo "Step 5: Importing Supervisor Agent"
echo "=================================================="
echo "🎯 Importing bob_ibm_product_specialist_agent..."
orchestrate agents import -f agents/bob_ibm_product_specialist_agent.yaml

echo "✅ Supervisor agent imported successfully"
echo ""

echo "=================================================="
echo "✅ DEPLOYMENT COMPLETE!"
echo "=================================================="
echo ""
echo "📋 Deployment Summary:"
echo "   • 10 Tools imported (3 per product + 1 models tool)"
echo "   • 3 Sub-agents imported (product specialists)"
echo "   • 1 Supervisor agent imported (coordinator)"
echo ""
echo "🔍 Verify deployment:"
echo "   orchestrate tools list"
echo "   orchestrate agents list"
echo ""
echo "💬 Test the system:"
echo "   orchestrate agents chat -n bob_ibm_product_specialist_agent"
echo ""
echo "📖 Example questions to ask:"
echo "   • What is IBM Cognos Analytics?"
echo "   • What are the key features of Watsonx Orchestrate?"
echo "   • How much does Watsonx.ai cost?"
echo "   • What foundation models are available in Watsonx.ai?"
echo ""

# Made with Bob
