import unittest
from utils.conversation_state import ConversationSession, ConversationStateManager, parse_structured_response

class TestConversationSession(unittest.TestCase):
    def test_add_and_get_latest_message(self):
        session = ConversationSession()
        session.add_message("user", "Hello")
        session.add_message("assistant", "Hi, how can I help?")
        self.assertEqual(session.get_latest_user_message(), "Hello")
        self.assertEqual(session.get_latest_assistant_message(), "Hi, how can I help?")

    def test_to_dict_and_from_dict(self):
        session = ConversationSession()
        session.add_message("user", "Test")
        d = session.to_dict()
        session2 = ConversationSession.from_dict(d)
        self.assertEqual(session2.messages, session.messages)

    def test_should_proceed_to_research(self):
        session = ConversationSession()
        session.question_count = 3
        session.messages = [{"role": "user", "content": "A"}] * 6
        self.assertTrue(session.should_proceed_to_research())

    def test_reset(self):
        session = ConversationSession()
        session.add_message("user", "Test")
        session.research_results = {"a": 1}
        session.analysis_complete = True
        session.report = {"r": 2}
        session.conversation_stage = "research"
        session.symptom_details = {"s": 3}
        session.question_count = 5
        session.reset()
        self.assertEqual(session.messages, [])
        self.assertEqual(session.research_results, {})
        self.assertFalse(session.analysis_complete)
        self.assertEqual(session.report, {})
        self.assertEqual(session.conversation_stage, "conversation")
        self.assertEqual(session.symptom_details, {})
        self.assertEqual(session.question_count, 0)

class TestConversationStateManager(unittest.TestCase):
    def test_create_get_update_delete_list(self):
        manager = ConversationStateManager()
        session = manager.create_session()
        sid = session.session_id
        self.assertIs(manager.get_session(sid), session)
        session.question_count = 42
        manager.update_session(session)
        self.assertEqual(manager.get_session(sid).question_count, 42)
        self.assertTrue(manager.delete_session(sid))
        self.assertIsNone(manager.get_session(sid))
        self.assertEqual(manager.list_sessions(), [])

class TestParseStructuredResponse(unittest.TestCase):
    def test_parse_valid_json(self):
        resp = '{"a": 1, "b": 2}'
        result = parse_structured_response(resp)
        self.assertEqual(result["a"], 1)
        self.assertEqual(result["b"], 2)
    def test_parse_invalid_json(self):
        resp = 'not a json'
        result = parse_structured_response(resp)
        self.assertIsInstance(result, dict)

if __name__ == "__main__":
    unittest.main()
