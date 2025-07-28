"""
Main medical diagnostic agent using LangGraph
"""
import os
import time
import json
import re
from typing import Dict, Any, List, Optional, TypedDict, Annotated
from functools import wraps

from langgraph.graph import StateGraph, START, END
from langgraph.errors import GraphRecursionError
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool

# Import utility functions
from ..utils.text_processing import (
    format_conversation_history,
    extract_user_messages,
    beautify_text
)
from ..utils.conversation_state import ConversationSession, parse_structured_response

# Import model clients
from ..models.perplexity_client import perplexity_research


# State Management for the Agent
class State(TypedDict):
    """State definition for the medical diagnostic agent"""
    messages: Annotated[List[Dict[str, Any]], "Chat messages"]
    research_results: Annotated[Dict[str, Any], "Medical research data"]
    analysis_complete: Annotated[bool, "Whether analysis is complete"]
    report: Annotated[Dict[str, Any], "Final medical analysis report"]
    conversation_stage: Annotated[str, "Current stage: conversation, research, complete"]
    symptom_details: Annotated[Dict[str, Any], "Collected symptom information"]
    question_count: Annotated[int, "Number of questions asked so far"]


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


# System Prompt
SYSTEM_PROMPT = """
You are an advanced AI medical assistant with access to up-to-date medical literature, expert guidelines, and peer-reviewed studies. Your role is to:
1. Conduct a structured diagnostic evaluation, mimicking a board-certified physician's approach.
2. Use differential diagnosis methods, listing probable conditions with confidence scores assessing the likelihood of each condition.
3. Prioritize high-accuracy, medically reviewed sources (such as but not limited to PubMed, Mayo Clinic, NIH, UpToDate).
4. Clearly communicate **when emergency medical care might be required**.
5. Provide a clear, structured medical report summarizing likely conditions with citations to justify the evaluation, risk assessments, and next steps.

IMPORTANT: If a user describes symptoms that suggest a medical emergency (such as signs of heart attack, stroke, severe bleeding, difficulty breathing, or severe allergic reaction), immediately advise them to seek emergency medical care.
"""


class MedicalAgent:
    """Medical diagnostic agent implementation"""
    
    def __init__(self, gemini_api_key: str, perplexity_api_key: str, model_name: str = "gemini-1.5-pro"):
        """Initialize the medical agent"""
        # LLM Configuration
        self.llm = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=gemini_api_key,
            temperature=0.3
        )
        
        # Bind tools
        self.tools = [perplexity_research]
        self.llm_with_tools = self.llm.bind_tools(tools=self.tools)
        
        # Build the graph
        self.graph = self._build_graph()
    
    def _extract_symptom_details(self, messages: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Extract structured symptom information from conversation"""
        # Combine all user messages to analyze
        all_user_input = " ".join([
            msg["content"] for msg in messages 
            if msg.get("role") == "user"
        ])

        extract_prompt = f"""
        Based on the following user messages, extract key symptom information:

        {all_user_input}

        Extract and organize these details into a structured format:
        - Primary symptoms (list each with severity and duration)
        - Secondary/associated symptoms
        - Timing and patterns
        - Aggravating or relieving factors
        - Relevant medical history mentioned

        Return as a concise, structured text summary.
        """

        try:
            response = self.llm.invoke(extract_prompt)
            return {
                "extracted_data": response.content,
                "last_updated": len(messages)
            }
        except Exception as e:
            print(f"Error extracting symptom details: {str(e)}")
            return {
                "extracted_data": "Error processing symptoms",
                "last_updated": len(messages)
            }
    
    @api_rate_limit(1)
    def _interactive_conversation(self, state: State) -> Dict[str, Any]:
        """
        Handle multi-turn conversation using structured JSON output from LLM
        to dynamically decide when enough detail is present.
        """
        print("PROCESSING: Entering interactive_conversation node...")
        current_messages = state["messages"]
        question_count = state.get("question_count", 0) + 1
        symptom_details = state.get("symptom_details", {})

        # Failsafe check to prevent infinite loops
        FAILSAFE_LIMIT = 10
        if question_count > FAILSAFE_LIMIT:
            print(f"DEBUG: Failsafe question limit ({FAILSAFE_LIMIT}) reached. Forcing research.")
            return {
                "messages": current_messages + [{
                    "role": "assistant", 
                    "content": "Based on the information gathered so far, I will now proceed with the analysis."
                }],
                "question_count": question_count,
                "conversation_stage": "research",
                "symptom_details": symptom_details
            }

        # Update symptom details if new user message arrived
        if current_messages and current_messages[-1].get("role") == "user":
            last_updated = symptom_details.get("last_updated", -1)
            if len(current_messages) > last_updated:
                print("PROCESSING: Extracting details from latest user message...")
                symptom_details = self._extract_symptom_details(current_messages)

        # Prompt requesting JSON output for decision making
        prompt = f"""
        {SYSTEM_PROMPT}

        You are in the **information gathering** stage of a medical consultation. Your goal is to gather sufficient detail to perform a preliminary analysis following a standard procedure.
        
        Conversation History:
        {format_conversation_history(current_messages)}

        Current Symptom Understanding (internal summary - may be incomplete):
        {symptom_details.get("extracted_data", "No structured summary yet.")}

        Based on the conversation history and your understanding:

        1. **Assess Sufficiency:** Do you have enough detail about the main complaints? Consider key aspects like:
           * Onset & Duration
           * Location & Radiation
           * Quality/Character (e.g., sharp, dull, pressure)
           * Severity
           * Timing/Frequency
           * Aggravating/Alleviating Factors
           * Associated Symptoms
           * Relevant Medical History

        2. **Decide Action and Format Output:** Respond ONLY with a valid JSON object containing two keys:
           * `"proceed_to_research"`: A boolean value (`true` if you have sufficient detail, `false` otherwise).
           * `"assistant_message"`: The message to display to the user.
             - If proceeding to research, a brief, empathetic confirmation.
             - If continuing conversation, the single most important follow-up question.

        Do not include any emergency recommendations in the `assistant_message` at this stage.
        This is conversation turn {question_count}.

        Example of valid JSON output if continuing conversation:
        {{
          "proceed_to_research": false,
          "assistant_message": "When you feel short of breath, does anything seem to make it better or worse?"
        }}

        Example of valid JSON output if ready for research:
        {{
          "proceed_to_research": true,
          "assistant_message": "Thank you. I have enough information to analyze your symptoms now."
        }}

        Ensure your entire response is ONLY the JSON object without any explanation.
        """

        try:
            print(f"DEBUG: Invoking LLM for conversation (Turn {question_count})")
            response = self.llm.invoke(prompt)
            response_content = response.content

            # Parse JSON response
            try:
                # Clean potential code fences
                if response_content.strip().startswith("```json"):
                    response_content = response_content.strip()[7:-3].strip()
                elif response_content.strip().startswith("```"):
                     response_content = response_content.strip()[3:-3].strip()
                
                # Parse JSON
                parsed_data = json.loads(response_content)
                
                # Validate expected keys and types
                if not isinstance(parsed_data, dict) or \
                   "proceed_to_research" not in parsed_data or \
                   "assistant_message" not in parsed_data:
                    raise ValueError("Parsed JSON missing required keys.")

                has_enough_info = parsed_data["proceed_to_research"]
                assistant_content = parsed_data["assistant_message"]
                
            except (json.JSONDecodeError, ValueError) as json_error:
                print(f"ERROR: Failed to parse JSON: {json_error}")
                has_enough_info = False
                assistant_content = "I seem to be having trouble. Could you please clarify your symptoms?"
        
        except Exception as llm_error:
            print(f"ERROR: LLM invocation failed: {llm_error}")
            has_enough_info = False
            assistant_content = "I encountered an issue. Could you please try again?"

        # Determine the next stage
        new_stage = "research" if has_enough_info else "conversation"
        
        # Create response
        new_message = {"role": "assistant", "content": assistant_content}
        updated_messages = current_messages + [new_message]
        
        return {
            "messages": updated_messages,
            "question_count": question_count,
            "conversation_stage": new_stage,
            "symptom_details": symptom_details
        }
    
    @api_rate_limit(2)
    def _determine_research_needs(self, state: State) -> Dict[str, Any]:
        """Determine what conditions to research based on conversation"""
        print("DEBUG: Entering determine_research_needs node...")
        messages = state["messages"]
        symptom_details = state.get("symptom_details", {})

        # Use structured details if available, otherwise fall back to user messages
        extracted_data = symptom_details.get("extracted_data", "No structured data.")
        if "Error processing symptoms" in extracted_data or extracted_data == "No structured data.":
            # Fallback to raw user input
            user_inputs = extract_user_messages(messages)
            symptom_summary = "\n".join(user_inputs)
        else:
            symptom_summary = extracted_data

        research_prompt = f"""
        Based on the following symptom information:
        {symptom_summary}

        Perform medical research focusing on:
        1. Most probable conditions (ranked).
        2. Brief explanation, causes, risk factors for each.
        3. Cite relevant, authoritative sources (e.g., Mayo Clinic, NIH, PubMed links).
        4. Suggest potential diagnostic steps.
        """

        print("RESPONSE: Starting Perplexity research...")
        results = perplexity_research(research_prompt)
        print("RESPONSE: Perplexity research complete.")

        return {"research_results": {"medical_research": results}}

    @api_rate_limit(1)
    def _generate_analysis(self, state: State) -> Dict[str, Any]:
        """Generate medical analysis incorporating research"""
        print("DEBUG: Entering generate_analysis node...")
        research_data = state.get('research_results', {}).get('medical_research', 'No research data available.')
        messages = state["messages"]
        symptom_details = state.get("symptom_details", {})

        # Prepare symptom summary
        extracted_data = symptom_details.get("extracted_data", "No structured data.")
        if "Error processing symptoms" in extracted_data or extracted_data == "No structured data.":
            user_inputs = extract_user_messages(messages)
            symptom_summary = "\n".join(user_inputs)
        else:
            symptom_summary = extracted_data

        analysis_prompt = f"""
        {SYSTEM_PROMPT}
        Generate a detailed medical analysis based on the conversation and research.
        Format the entire report using Markdown syntax. Use headings, bullet points, and
        bold text for clarity and readability.

        SYMPTOM SUMMARY:
        {symptom_summary}

        RESEARCH FINDINGS:
        {research_data}

        Your analysis report should include:
        1. Summary of key symptoms and risk factors (from conversation).
        2. Differential diagnosis: Ranked list of probable conditions with confidence scores.
        3. Explanation of top 2-3 conditions (causes, symptoms matching/not matching).
        4. Recommended next steps (e.g., see primary care, specialist, diagnostics).
        5. Reiterate if any symptoms warrant immediate emergency care. Include medical disclaimers.
        """

        print("DEBUG: Invoking LLM for analysis generation...")
        analysis_response = self.llm.invoke(analysis_prompt)
        analysis_content = analysis_response.content
        print("DEBUG: Analysis generation complete.")
        
        return {"analysis_complete": True, "report": {"content": analysis_content}}

    def _final_response(self, state: State) -> Dict[str, Any]:
        """Format the final report for the user"""
        print("DEBUG: Entering final_response node...")
        report_content = state.get("report", {}).get("content", "Analysis could not be generated.")
        final_message = {
            "role": "assistant",
            "content": f"--- Medical Analysis Report ---\n\n{report_content}\n\n--- End of Report ---"
        }

        return {
            "messages": state["messages"] + [final_message],
            "conversation_stage": "complete",
            "analysis_complete": True,
            "report": state["report"]
        }

    def _determine_next_stage(self, state: State) -> str:
        """Determine the next node or END the current invocation to wait for user"""
        print(f"THINKING: Determining next stage... Current stage: {state.get('conversation_stage')}")
        messages = state["messages"]
        current_stage = state.get("conversation_stage", "conversation")
        last_message_role = messages[-1].get("role") if messages else None

        # Check if analysis is complete
        if current_stage == "complete":
             if last_message_role == "user":
                 last_user_message = str(messages[-1].get("content", "")).lower()
                 if any(phrase in last_user_message for phrase in ["new symptom", "different issue", "another problem"]):
                     print("RESTART: Routing to restart_conversation.")
                     return "restart_conversation"
                 else:
                     print("END: Routing to END graph (conversation complete, no new topic).")
                     return END
             else:
                 print("END: Routing to END graph (final report sent).")
                 return END

        # If interactive_conversation decided we need to research
        if current_stage == "research":
            print("PROCESSING: Routing to start_research.")
            return "start_research"

        # If we are in the conversation stage
        if current_stage == "conversation":
            if last_message_role == "assistant":
                if "enough information" not in str(messages[-1].get("content", "")).lower():
                     print("PROCESSING: Routing to END (yielding for user input).")
                     return END
                else:
                     print("DEBUG: Routing to END (yielding before research stage starts on next invoke).")
                     return END

            elif last_message_role == "user":
                print("DEBUG: Routing to continue_conversation.")
                return "continue_conversation"
            else:
                print("DEBUG: Routing to continue_conversation (initial state).")
                return "continue_conversation"

        # Fallback case
        print("ERROR: determine_next_stage fell through. Routing to END.")
        return END

    def _reset_conversation(self, state: State) -> Dict[str, Any]:
        """Reset the state for a new topic, keeping only the last user message"""
        print("RESTART: Entering reset_conversation node...")
        last_user_message = None
        if state["messages"] and state["messages"][-1].get("role") == "user":
             last_user_message = state["messages"][-1]

        # Acknowledge the reset
        acknowledgment = {
            "role": "assistant",
            "content": "Okay, let's focus on this new topic. Please tell me about the new symptoms or concerns you have."
        }

        # Start new history
        new_messages = [last_user_message, acknowledgment] if last_user_message else [acknowledgment]

        return {
            "messages": new_messages,
            "research_results": {},
            "analysis_complete": False,
            "report": {},
            "conversation_stage": "conversation",
            "symptom_details": {},
            "question_count": 0
        }

    def _build_graph(self) -> StateGraph:
        """Build the LangGraph state graph"""
        graph_builder = StateGraph(State)

        # Add nodes
        graph_builder.add_node("interactive_conversation", self._interactive_conversation)
        graph_builder.add_node("determine_research_needs", self._determine_research_needs)
        graph_builder.add_node("generate_analysis", self._generate_analysis)
        graph_builder.add_node("final_response", self._final_response)
        graph_builder.add_node("reset_conversation", self._reset_conversation)

        # Starting edge
        graph_builder.add_edge(START, "interactive_conversation")

        # Add conditional edges for the conversation flow
        graph_builder.add_conditional_edges(
            "interactive_conversation",
            self._determine_next_stage,
            {
                "continue_conversation": "interactive_conversation",
                "start_research": "determine_research_needs",
                "restart_conversation": "reset_conversation",
                END: END
            }
        )

        # Connect research flow
        graph_builder.add_edge("determine_research_needs", "generate_analysis")
        graph_builder.add_edge("generate_analysis", "final_response")
        graph_builder.add_edge("final_response", END)
        graph_builder.add_edge("reset_conversation", "interactive_conversation")

        # Compile the graph
        return graph_builder.compile()
    
    def start_chat(self, initial_message: str) -> Dict[str, Any]:
        """Start a new chat with an initial user message"""
        initial_state = {
            "messages": [{"role": "user", "content": initial_message}],
            "research_results": {},
            "analysis_complete": False,
            "report": {},
            "conversation_stage": "conversation",
            "symptom_details": {},
            "question_count": 0
        }
        
        try:
            result_state = self.graph.invoke(initial_state, {"recursion_limit": 10})
        except GraphRecursionError:
            return self._handle_recursion_limit(initial_state)
        
        return result_state
    
    def continue_chat(self, state: Dict[str, Any], user_message: str) -> Dict[str, Any]:
        """Continue an existing chat with a new user message"""
        # Add the new message
        updated_messages = state.get("messages", []) + [{"role": "user", "content": user_message}]
        updated_state = {**state, "messages": updated_messages}
        
        try:
            result_state = self.graph.invoke(updated_state, {"recursion_limit": 10})
        except GraphRecursionError:
            return self._handle_recursion_limit(updated_state)
        
        return result_state
    
    def _handle_recursion_limit(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """Force final report generation when recursion limit is hit"""
        warning = {"role": "assistant", "content": "[SYSTEM] Generating final analysis report due to complexity..."}
        updated_state = {**state, "messages": state.get("messages", []) + [warning]}
        
        # Force analysis
        analyzed_state = self._generate_analysis(updated_state)
        final_state = self._final_response({**updated_state, **analyzed_state})
        
        return final_state
