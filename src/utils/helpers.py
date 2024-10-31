import time
import logging

def get_response_with_retries(client, prompt, language_code, max_retries=3):
    delay = 2
    for _ in range(max_retries):
        try:
            response = client.chat_completion(
                model="mistralai/Mistral-7B-Instruct-v0.3",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.2
            )
            if response and 'choices' in response and response['choices'][0]['message']['content'].strip():
                return response['choices'][0]['message']['content'].strip()
        except Exception as e:
            logging.error(f"Erreur : {e}")
        time.sleep(delay)
        delay *= 1.5
    return "Aucune réponse disponible après plusieurs tentatives."

def generate_sub_questions(question, main_response):
    # Logique pour générer les sous-questions
    return ["Sous-question 1", "Sous-question 2"]

