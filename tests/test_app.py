import unittest
from src.utils.helpers import get_response_with_retries, generate_sub_questions

class TestAppFunctions(unittest.TestCase):

    def test_generate_sub_questions(self):
        question = "How to reduce CO₂ emissions?"
        main_response = "The best ways to reduce CO₂ involve..."
        sub_questions = generate_sub_questions(question, main_response)
        self.assertTrue(len(sub_questions) > 0)

    def test_get_response_with_retries(self):
        client = MockInferenceClient()
        response = get_response_with_retries(client, "Hello", "en")
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()

