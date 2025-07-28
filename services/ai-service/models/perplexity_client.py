"""
Perplexity API client for medical research
"""
import os
import time
import requests
from functools import wraps
from typing import Dict, Any
from langchain_core.tools import tool

# Rate Limiting Decorator
def api_rate_limit(seconds: int = 1):
    """Decorator to add sleep time between API calls"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(seconds)  # Wait before making the API call
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Medical Research Tool
@tool
@api_rate_limit(1)
def perplexity_research(query: str) -> str:
    """Research medical conditions using Perplexity API. Provide citations and links to reliable, authentic research sources."""
    api_key = os.getenv("PERPLEXITY_API_KEY")
    if not api_key:
        return "Error: PERPLEXITY_API_KEY environment variable not set"
        
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "system",
             "content": "You are a medical research assistant. Provide precise and well-sourced responses, along with citations, and links for resources"},
            {"role": "user", "content": query}
        ],
        "temperature": 0.3,
        "max_tokens": 2048,
        "top_p": 0.8,
        "frequency_penalty": 0.0,
    }

    try:
        print("RESPONSE: Sending request to Perplexity API...")
        response = requests.post("https://api.perplexity.ai/chat/completions", json=payload, headers=headers)
        response.raise_for_status()

        json_response = response.json()
        return json_response["choices"][0].get("message", {}).get("content", "No content found.")

    except requests.RequestException as e:
        print(f"RESPONSE: API Error Details: {str(e)}")
        return f"Error researching topic: {str(e)}"

# Function to get research on specific medical conditions
def get_medical_research(condition: str) -> Dict[str, Any]:
    """
    Get detailed research information about a specific medical condition
    
    Args:
        condition: The medical condition to research
        
    Returns:
        Dictionary containing research results
    """
    query = f"""
    Provide a comprehensive research summary on {condition}, including:
    1. Definition and overview
    2. Common symptoms and progression
    3. Causes and risk factors
    4. Diagnostic approaches
    5. Treatment options
    6. Prognosis
    7. Recent research developments
    
    Include citations to medical journals, trusted health organizations (NIH, CDC, WHO, Mayo Clinic),
    and peer-reviewed research where possible.
    """
    
    research_data = perplexity_research(query)
    
    return {
        "condition": condition,
        "research": research_data,
        "source": "Perplexity AI"
    }

# Function to search medical literature with specific terms
def search_medical_literature(search_terms: str, max_results: int = 5) -> Dict[str, Any]:
    """
    Search medical literature for specific terms or conditions
    
    Args:
        search_terms: Terms to search for
        max_results: Maximum number of results to return
        
    Returns:
        Dictionary containing search results
    """
    query = f"""
    Search medical literature for: {search_terms}
    
    Return the {max_results} most relevant results with:
    1. Title of research paper or article
    2. Authors and publication date
    3. Brief summary of findings
    4. Link to the source
    
    Focus on peer-reviewed sources and major medical institutions.
    """
    
    search_results = perplexity_research(query)
    
    return {
        "query": search_terms,
        "results": search_results,
        "source": "Perplexity AI"
    }
