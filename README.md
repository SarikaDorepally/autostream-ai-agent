# AutoStream AI Agent (Final Submission)

## Overview
Conversational AI agent that converts user queries into leads using intent detection, RAG, and tool execution.

## How to Run
pip install -r requirements.txt
python main.py

## Architecture
This system uses intent detection, RAG for knowledge retrieval, and state management to track conversation flow. Lead capture is triggered only after collecting required inputs.

## WhatsApp Integration
Use Twilio API with a webhook (Flask/FastAPI) to connect this agent to WhatsApp.
