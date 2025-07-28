"""
Text processing utilities for medical conversation handling
"""
import re
import textwrap
from typing import List, Dict, Any


def beautify_text(text: str, width: int = 80) -> str:
    """
    Format text for better readability by removing markdown formatting
    and wrapping lines appropriately.
    
    Args:
        text: Input text to format
        width: Maximum line width for text wrapping
    
    Returns:
        Formatted text string
    """
    # Remove ** from the text
    text = re.sub(r'\*\*', '', text)

    # Ensure numbered sections (1., 2., etc.) start on a new line
    text = re.sub(r'(\d+\.)', r'\n\1', text)

    # Ensure bullet points (*) start on a new line and replace them with "-"
    text = re.sub(r'\n?\s*\*', '\n- ', text)

    # Wrap text for better readability
    wrapped_lines = []
    for line in text.split("\n"):
        if line.strip():
            wrapped_lines.append(textwrap.fill(line, width))
        else:
            wrapped_lines.append(line)

    return "\n".join(wrapped_lines)


def format_conversation_history(messages: List[Dict[str, Any]]) -> str:
    """
    Format conversation history for LLM prompts.
    
    Args:
        messages: List of message dictionaries with 'role' and 'content' keys
    
    Returns:
        Formatted conversation history string
    """
    formatted = ""
    for msg in messages:
        content = msg.get("content", "")
        if not isinstance(content, str):
            content = str(content)
        
        role = "User" if msg.get("role") == "user" else "Assistant"
        formatted += f"{role}: {content}\n\n"
    
    return formatted.strip()


def extract_user_messages(messages: List[Dict[str, Any]]) -> List[str]:
    """
    Extract all user messages from conversation history.
    
    Args:
        messages: List of message dictionaries
    
    Returns:
        List of user message content strings
    """
    return [
        str(msg.get("content", ""))
        for msg in messages
        if msg.get("role") == "user"
    ]


def extract_symptom_keywords(text: str) -> List[str]:
    """
    Extract potential symptom keywords from user input.
    
    Args:
        text: User input text
    
    Returns:
        List of potential symptom keywords
    """
    # Common medical symptom keywords
    symptom_patterns = [
        r'\b(?:pain|ache|hurt|sore)\b',
        r'\b(?:fever|temperature|hot|cold)\b',
        r'\b(?:nausea|nauseous|sick|vomit)\b',
        r'\b(?:dizzy|dizziness|lightheaded)\b',
        r'\b(?:tired|fatigue|exhausted|weak)\b',
        r'\b(?:cough|sneeze|congestion)\b',
        r'\b(?:headache|migraine)\b',
        r'\b(?:shortness of breath|breathing|breath)\b',
        r'\b(?:chest|heart|cardiac)\b',
        r'\b(?:stomach|abdomen|belly)\b'
    ]
    
    keywords = []
    text_lower = text.lower()
    
    for pattern in symptom_patterns:
        matches = re.findall(pattern, text_lower)
        keywords.extend(matches)
    
    return list(set(keywords))  # Remove duplicates
