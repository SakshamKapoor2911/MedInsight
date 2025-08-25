import unittest
from models.nim_client import *

class TestNimClient(unittest.TestCase):
    def setUp(self):
        self.client = NIMClient(api_key="dummy_key", base_url="http://localhost")

    def test_chat_completion(self):
        # Test the chat_completion method with a real medical prompt
        messages = [{"role": "user", "content": "What are common symptoms of flu?"}]
        result = self.client.chat_completion(messages)
        # Check that the result contains plausible symptoms
        content = result.get("choices", [{}])[0].get("message", {}).get("content", "")
        self.assertTrue(any(symptom in content.lower() for symptom in ["fever", "cough", "sore throat"]), "NIMClient did not mention common flu symptoms.")

if __name__ == "__main__":
    unittest.main()
