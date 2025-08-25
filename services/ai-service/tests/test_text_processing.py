import unittest
from utils.text_processing import beautify_text, format_conversation_history, extract_user_messages, extract_symptom_keywords

class TestTextProcessing(unittest.TestCase):
    def test_beautify_text(self):
        text = "**1. Fever**\n* Cough\n* Sore throat"
        result = beautify_text(text)
        self.assertIn("1. Fever", result)
        self.assertIn("-  Cough", result)
        self.assertIn("-  Sore throat", result)

    def test_format_conversation_history(self):
        messages = [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi!"}
        ]
        result = format_conversation_history(messages)
        self.assertIn("User: Hello", result)
        self.assertIn("Assistant: Hi!", result)

    def test_extract_user_messages(self):
        messages = [
            {"role": "user", "content": "A"},
            {"role": "assistant", "content": "B"},
            {"role": "user", "content": "C"}
        ]
        result = extract_user_messages(messages)
        self.assertEqual(result, ["A", "C"])

    def test_extract_symptom_keywords(self):
        text = "I have a fever and cough, and my chest hurts."
        result = extract_symptom_keywords(text)
        self.assertIn("fever", result)
        self.assertIn("cough", result)
        self.assertIn("chest", result)

if __name__ == "__main__":
    unittest.main()
