import streamlit as st
import logging
from huggingface_hub import InferenceClient
import time
from src.config.config import LANGUAGES, TITLES
from src.utils.helpers import get_response_with_retries, generate_sub_questions, generate_sub_sub_questions

# Configuration du logger
logging.basicConfig(level=logging.DEBUG)

# Initialisation du client Hugging Face
client = InferenceClient(api_key=st.secrets["HUGGINGFACE_API_KEY"])

# Sélecteur de langue
selected_language = st.selectbox("Sélectionnez la langue", list(LANGUAGES.keys()))
selected_language_code = LANGUAGES[selected_language]

# Titre dynamique selon la langue
st.title(TITLES[selected_language])

# Interface utilisateur
st.write("### Entrez une question principale :")
question = st.text_input("", placeholder="Votre question")

# Affichage des sous-questions et gestion des réponses
if question:
    main_response = get_response_with_retries(client, question, selected_language_code)
    st.write("**Réponse initiale :**", main_response)
    
    # Génération et affichage des sous-questions
    sub_questions = generate_sub_questions(question, main_response)
    for i, sub_question in enumerate(sub_questions):
        st.write(f"**Sous-question {i+1} :** {sub_question}")

