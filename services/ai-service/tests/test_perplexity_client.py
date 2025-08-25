"""
Basic test for perplexity_research mock function in local dev mode.
"""
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'models')))
from perplexity_client import perplexity_research

def test_perplexity_research_mock():
    result = perplexity_research("What is diabetes?")
    assert result == "mock message for local dev, not an LLM response"
import unittest
from models.perplexity_client import *

class TestPerplexityClient(unittest.TestCase):
    def test_perplexity_search(self):
        # Test the perplexity_research function with a real medical query
        result = perplexity_research("What are common symptoms of flu?")
        self.assertTrue(any(symptom in result.lower() for symptom in ["fever", "cough", "sore throat"]), "Perplexity did not mention common flu symptoms.")

if __name__ == "__main__":
    unittest.main()
