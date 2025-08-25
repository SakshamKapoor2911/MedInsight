"""
Chat API routes
"""
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional

from utils.conversation_state import ConversationStateManager
from agents.medical_agent import MedicalAgent

# Router
router = APIRouter(prefix="/api/chat", tags=["chat"])

# Shared instances
conversation_manager = None
medical_agent = None

# Models
class ChatRequest(BaseModel):
    """Chat request model"""
    message: str = Field(..., description="User message")
    session_id: Optional[str] = Field(None, description="Session ID for continuing conversation")

class ChatResponse(BaseModel):
    """Chat response model"""
    session_id: str = Field(..., description="Session ID for this conversation")
    messages: List[Dict[str, Any]] = Field(..., description="Message history")
    complete: bool = Field(False, description="Whether analysis is complete")
    report: Optional[Dict[str, Any]] = Field(None, description="Analysis report if complete")

# Set dependencies
def set_dependencies(manager: ConversationStateManager, agent: MedicalAgent):
    """Set dependencies for routes"""
    global conversation_manager, medical_agent
    conversation_manager = manager
    medical_agent = agent

# Routes
@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Process chat message and return response"""
    if not medical_agent:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Medical agent not initialized. Please check API keys."
        )
    
    # Get or create session
    session_id = request.session_id
    if session_id:
        session = conversation_manager.get_session(session_id)
        if not session:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Session {session_id} not found"
            )
        
        # Continue existing conversation
        state = session.to_dict()
        result = medical_agent.continue_chat(state, request.message)
    else:
        # Start new conversation
        session = conversation_manager.create_session()
        result = medical_agent.start_chat(request.message)
    
    # Update session with new state
    for key, value in result.items():
        setattr(session, key, value)
    conversation_manager.update_session(session)
    
    # Prepare response
    is_complete = session.conversation_stage == "complete"
    report = session.report if is_complete else None
    
    return ChatResponse(
        session_id=session.session_id,
        messages=session.messages,
        complete=is_complete,
        report=report
    )

@router.delete("/{session_id}")
async def delete_chat(session_id: str):
    """Delete a chat session"""
    success = conversation_manager.delete_session(session_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Session {session_id} not found"
        )
    
    return {"status": "success", "message": f"Session {session_id} deleted"}

@router.get("/sessions")
async def list_sessions():
    """List all active sessions"""
    return {
        "sessions": conversation_manager.list_sessions()
    }
