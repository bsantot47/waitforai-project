import unittest
from utils.helpers import get_response_with_retries, generate_sub_questions

# Créez une classe pour simuler le client InferenceClient
class MockInferenceClient:
    def chat_completion(self, model, messages, max_tokens, temperature):
        # Simulez une réponse de l'API
        return {
            'choices': [
                {'message': {'content': "Ceci est une réponse simulée"}}
            ]
        }

class TestAppFunctions(unittest.TestCase):

    def test_get_response_with_retries(self):
        # Utilisation de MockInferenceClient au lieu d'InferenceClient réel
        client = MockInferenceClient()
        prompt = "Quelle est la capitale de la France ?"
        language_code = "fr"
        response = get_response_with_retries(client, prompt, language_code)
        self.assertEqual(response, "Ceci est une réponse simulée")

    def test_generate_sub_questions(self):
        question = "Comment améliorer la qualité de l'air en ville ?"
        main_response = "Améliorer les transports publics, réduire l'utilisation de voitures."
        sub_questions = generate_sub_questions(question, main_response)
        self.assertEqual(len(sub_questions), 2)
        self.assertIn("Sous-question 1", sub_questions)
        self.assertIn("Sous-question 2", sub_questions)

if __name__ == "__main__":
    unittest.main()

