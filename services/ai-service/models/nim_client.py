"""
NVIDIA NIM client for Gemma 2 model integration
"""
from typing import Dict, Any, List, Optional
import os
import requests
import json

class NIMClient:
    """
    Client for interacting with NVIDIA NIM service for Gemma 2 model.
    This is a placeholder implementation to be replaced with actual
    NVIDIA NIM integration in Phase 2.
    """
    
    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        """
        Initialize the NIM client
        
        Args:
            api_key: API key for authentication (can be set via environment variable)
            base_url: Base URL for the NIM API
        """
        self.api_key = api_key or os.getenv("NVIDIA_NIM_API_KEY")
        self.base_url = base_url or os.getenv("NVIDIA_NIM_URL", "http://nim-service:8000")
    
    def chat_completion(self, 
                         messages: List[Dict[str, str]], 
                         model: str = "gemma-2",
                         temperature: float = 0.3,
                         max_tokens: int = 2048) -> Dict[str, Any]:
        """
        Generate a chat completion using the Gemma 2 model
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: Model to use (default is gemma-2)
            temperature: Temperature for generation
            max_tokens: Maximum tokens to generate
            
        Returns:
            Response dictionary with generated content
        """
        # Placeholder implementation - will be replaced with actual NIM API call
        print("NOTE: Using placeholder NIM client - needs implementation in Phase 2")
        
        # For now, we'll use a fallback to Gemini API
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
            
            gemini_api_key = os.getenv("GEMINI_API_KEY")
            if not gemini_api_key:
                return {"error": "GEMINI_API_KEY environment variable not set for fallback"}
            
            # Use Gemini as fallback
            llm = ChatGoogleGenerativeAI(
                model="gemini-1.5-pro",
                google_api_key=gemini_api_key,
                temperature=temperature
            )
            
            # Format the messages for Gemini
            formatted_prompt = ""
            for msg in messages:
                role = "User" if msg["role"] == "user" else "Assistant"
                formatted_prompt += f"{role}: {msg['content']}\n\n"
            
            # Invoke Gemini
            response = llm.invoke(formatted_prompt)
            
            return {
                "id": "fallback-gemini",
                "object": "chat.completion",
                "created": 0,
                "model": "gemini-1.5-pro-fallback",
                "choices": [
                    {
                        "message": {
                            "role": "assistant",
                            "content": response.content
                        },
                        "finish_reason": "stop",
                        "index": 0
                    }
                ]
            }
            
        except Exception as e:
            return {
                "error": f"NIM client not implemented and fallback failed: {str(e)}"
            }
            
    def text_completion(self, 
                         prompt: str,
                         model: str = "gemma-2",
                         temperature: float = 0.3,
                         max_tokens: int = 2048) -> Dict[str, Any]:
        """
        Generate text completion using Gemma 2 model
        
        Args:
            prompt: Input prompt text
            model: Model to use
            temperature: Temperature for generation
            max_tokens: Maximum tokens to generate
            
        Returns:
            Response dictionary with generated content
        """
        # Convert to chat format and use chat_completion
        messages = [{"role": "user", "content": prompt}]
        return self.chat_completion(messages, model, temperature, max_tokens)
