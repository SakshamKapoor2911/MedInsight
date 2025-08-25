import unittest
from unittest.mock import patch
from agents.medical_agent import *


class TestMedicalAgent(unittest.TestCase):
    class MockLLMResponse:
        def __init__(self, content):
            self.content = content

    def mock_llm_invoke(self, prompt, *args, **kwargs):
        # Return a plausible mock analysis for local tests
        return self.MockLLMResponse("Mocked analysis: Patient has fever.")
    def setUp(self):
        self.agent = MedicalAgent(gemini_api_key="dummy_key", perplexity_api_key="dummy_key")

    def test_start_chat(self):
        result = self.agent.start_chat("What are common symptoms of flu?")
        messages = result.get("messages", [])
        response_text = " ".join([m["content"] for m in messages if m["role"] == "assistant"])
        self.assertTrue(isinstance(messages, list))

    def test_continue_chat(self):
        state = self.agent.start_chat("What are common symptoms of flu?")
        result = self.agent.continue_chat(state, "What about fever?")
        self.assertIn("messages", result)

    def test_handle_recursion_limit(self):
        state = {"messages": [{"role": "user", "content": "test"}]}
        with patch.object(ChatGoogleGenerativeAI, "invoke", side_effect=self.mock_llm_invoke):
            result = self.agent._handle_recursion_limit(state)
            self.assertIn("report", result)
            self.assertIn("Mocked analysis", result["report"]["content"])

    def test_extract_symptom_details(self):
        messages = [{"role": "user", "content": "I have a fever and cough."}]
        details = self.agent._extract_symptom_details(messages)
        self.assertIn("extracted_data", details)

    def test_interactive_conversation(self):
        state = {
            "messages": [{"role": "user", "content": "I have a fever."}],
            "question_count": 0,
            "symptom_details": {}
        }
        result = self.agent._interactive_conversation(state)
        self.assertIn("messages", result)

    def test_determine_research_needs(self):
        state = {
            "messages": [{"role": "user", "content": "I have a fever."}],
            "symptom_details": {"extracted_data": "Fever"}
        }
        result = self.agent._determine_research_needs(state)
        self.assertIn("research_results", result)

    def test_generate_analysis(self):
        state = {
            "messages": [{"role": "user", "content": "I have a fever."}],
            "symptom_details": {"extracted_data": "Fever"},
            "research_results": {"medical_research": "Fever research"}
        }
        with patch.object(ChatGoogleGenerativeAI, "invoke", side_effect=self.mock_llm_invoke):
            result = self.agent._generate_analysis(state)
            self.assertIn("analysis_complete", result)
            self.assertIn("fever", result["report"]["content"].lower())

    def test_final_response(self):
        state = {
            "messages": [{"role": "user", "content": "I have a fever."}],
            "report": {"content": "Fever analysis"}
        }
        result = self.agent._final_response(state)
        self.assertIn("messages", result)

    def test_reset_conversation(self):
        state = {
            "messages": [{"role": "user", "content": "I have a fever."}]
        }
        result = self.agent._reset_conversation(state)
        self.assertIn("messages", result)

if __name__ == "__main__":
    unittest.main()
