# MedLama AI Service Implementation

## Overview
This directory contains the AI/ML service implementation for the MedLama medical diagnostics platform. The service is built as a microservice using FastAPI and LangGraph, providing medical diagnostic reasoning capabilities.

## Implementation Status

### ✅ Completed
- Package structure implementation with proper modules
- Migration of LangGraph agent from original implementation
- JSON-based decision logic for conversation state management
- Perplexity API integration for medical research
- FastAPI endpoints for chat interaction

### ⏳ In Progress
- NVIDIA NIM client integration (placeholder implemented)
- Integration tests for API endpoints
- Error handling improvements

## Structure
```
ai-service/
├── api/                   # FastAPI HTTP endpoints
│   ├── __init__.py
│   ├── main.py           # API server entry point
│   └── routes/           # API route handlers
│       ├── __init__.py
│       └── chat.py       # Chat endpoints
├── agents/               # LangGraph agent implementations
│   ├── __init__.py
│   └── medical_agent.py  # Main medical reasoning agent
├── models/               # Model integrations
│   ├── __init__.py
│   ├── nim_client.py     # NVIDIA NIM client
│   └── perplexity_client.py # Perplexity API client
├── utils/                # Utility functions
│   ├── __init__.py
│   ├── text_processing.py
│   └── conversation_state.py
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
└── README.md           # This file
```

## Key Components

### 1. `agents/medical_agent.py`
- Core LangGraph agent implementation
- Multi-turn conversation management
- Decision logic for when to research vs continue gathering information
- Analysis generation from research data

### 2. `models/perplexity_client.py`
- Integration with Perplexity API for medical research
- Tool implementation for LangGraph agent to use

### 3. `models/nim_client.py`
- Placeholder client for NVIDIA NIM with Gemma 2
- Currently falls back to Gemini API

### 4. `utils/conversation_state.py`
- Session management for conversations
- State tracking and persistence

### 5. `utils/text_processing.py`
- Utilities for processing medical text
- Formatting conversation history

### 6. `api/routes/chat.py`
- FastAPI routes for chat interactions
- Session management endpoints

## Technology Stack
- **Framework**: FastAPI for high-performance async API
- **AI/ML**: LangGraph, LangChain for agent workflows
- **Inference**: NVIDIA NIM with Gemma 2 model (planned)
- **Research**: Perplexity API for medical literature
- **Database**: MongoDB for conversation storage (planned)

## Running the Service

### Prerequisites
- Python 3.10+
- API keys for Gemini and Perplexity
- Environment variables set up (see `.env.example`)

### Setup
1. Create a virtual environment: `python -m venv venv`
2. Activate the environment: 
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Create `.env` file from `.env.example` and add your API keys

### Starting the API Server
```bash
cd services/ai-service
python -m uvicorn api.main:app --reload
```

The service will be available at http://localhost:8001

## API Endpoints

### `GET /`
- Root endpoint returning service information

### `GET /health`
- Health check endpoint

### `POST /api/chat`
- Process a chat message
- Request body:
  ```json
  {
    "message": "string",
    "session_id": "string (optional)"
  }
  ```
- Returns chat response with session ID, messages, and report if complete

### `DELETE /api/chat/{session_id}`
- Delete a chat session

### `GET /api/sessions`
- List all active sessions

## Next Steps
1. Complete NVIDIA NIM integration with Gemma 2 model
2. Add comprehensive error handling and logging
3. Implement database persistence for session storage
4. Add authentication and rate limiting
5. Create Kubernetes deployment configurations
