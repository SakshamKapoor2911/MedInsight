"""
Conversation state management utilities
"""
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
import json
import uuid


@dataclass
class ConversationSession:
    """Represents a conversation session with a user"""
    session_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    messages: List[Dict[str, Any]] = field(default_factory=list)
    research_results: Dict[str, Any] = field(default_factory=dict)
    analysis_complete: bool = False
    report: Dict[str, Any] = field(default_factory=dict)
    conversation_stage: str = "conversation"  # conversation, research, complete
    symptom_details: Dict[str, Any] = field(default_factory=dict)
    question_count: int = 0
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert session to dictionary"""
        return {
            "session_id": self.session_id,
            "messages": self.messages,
            "research_results": self.research_results,
            "analysis_complete": self.analysis_complete,
            "report": self.report,
            "conversation_stage": self.conversation_stage,
            "symptom_details": self.symptom_details,
            "question_count": self.question_count,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ConversationSession':
        """Create session from dictionary"""
        return cls(**data)
    
    def add_message(self, role: str, content: str) -> None:
        """Add a message to the conversation"""
        self.messages.append({
            "role": role,
            "content": content
        })
    
    def get_latest_user_message(self) -> Optional[str]:
        """Get the most recent user message"""
        for msg in reversed(self.messages):
            if msg.get("role") == "user":
                return msg.get("content")
        return None
    
    def get_latest_assistant_message(self) -> Optional[str]:
        """Get the most recent assistant message"""
        for msg in reversed(self.messages):
            if msg.get("role") == "assistant":
                return msg.get("content")
        return None
    
    def should_proceed_to_research(self) -> bool:
        """Determine if conversation should move to research stage"""
        # Simple heuristic - can be improved with the notebook's JSON logic
        return (
            self.question_count >= 3 and 
            len(self.messages) >= 6 and
            self.conversation_stage == "conversation"
        )
    
    def reset(self) -> None:
        """Reset the conversation session"""
        self.messages.clear()
        self.research_results.clear()
        self.analysis_complete = False
        self.report.clear()
        self.conversation_stage = "conversation"
        self.symptom_details.clear()
        self.question_count = 0


class ConversationStateManager:
    """Manager for conversation sessions"""
    
    def __init__(self):
        self._sessions: Dict[str, ConversationSession] = {}
    
    def create_session(self) -> ConversationSession:
        """Create a new conversation session"""
        session = ConversationSession()
        self._sessions[session.session_id] = session
        return session
    
    def get_session(self, session_id: str) -> Optional[ConversationSession]:
        """Get an existing session by ID"""
        return self._sessions.get(session_id)
    
    def update_session(self, session: ConversationSession) -> None:
        """Update an existing session"""
        self._sessions[session.session_id] = session
    
    def delete_session(self, session_id: str) -> bool:
        """Delete a session"""
        if session_id in self._sessions:
            del self._sessions[session_id]
            return True
        return False
    
    def list_sessions(self) -> List[str]:
        """List all session IDs"""
        return list(self._sessions.keys())


def parse_structured_response(response: str) -> Dict[str, Any]:
    """
    Parse a structured JSON response from the LLM, with fallback handling.
    This function will be improved in later phases with the notebook's logic.
    
    Args:
        response: Raw response from LLM
    
    Returns:
        Parsed response dictionary
    """
    try:
        # Try to find JSON in the response
        import re
        json_match = re.search(r'\{.*\}', response, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        else:
            # Fallback: treat as regular text response
            return {
                "proceed_to_research": False,
                "assistant_message": response
            }
    except json.JSONDecodeError:
        # Fallback for invalid JSON
        return {
            "proceed_to_research": False,
            "assistant_message": response
        }
