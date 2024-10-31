languages = {
    "English": "en",
    "Français": "fr",
    "Español": "es",
    "Português": "pt",
    "العربية": "ar",
    "Русский": "ru",
    "हिन्दी": "hi",
    "Deutsch": "de",
    "日本語": "ja"
}
selected_language = st.selectbox("Sélectionnez la langue", list(languages.keys()))
selected_language_code = languages[selected_language]

# Dictionnaire des titres pour chaque langue
titles = {
    "English": "🧐 WaitForAI Beta Test: Experience the model with Mistral-7B-Instruct-v0.3 (test version, not fully functional)",
    "Français": "🧐 WaitForAI Bêta Test : Découvrez le modèle en action avec Mistral-7B-Instruct-v0.3 (version de test non finalisée)",
    "Español": "🧐 Prueba Beta de WaitForAI: Experimente el modelo con Mistral-7B-Instruct-v0.3 (versión de prueba, no completamente funcional)",
    "Português": "🧐 Teste Beta do WaitForAI: Experimente o modelo com Mistral-7B-Instruct-v0.3 (versão de teste, não totalmente funcional)",
    "العربية 🧐": "اختبار تجريبي لـ WaitForAI: جرب النموذج مع Mistral-7B-Instruct-v0.3 (نسخة تجريبية غير مكتملة)",
    "Русский": "🧐 Бета-тест WaitForAI: Оцените модель с Mistral-7B-Instruct-v0.3 (тестовая версия, не полностью функциональная)",
    "हिन्दी": "🧐 WaitForAI बीटा परीक्षण: Mistral-7B-Instruct-v0.3 के साथ मॉडल का अनुभव करें (टेस्ट संस्करण, पूरी तरह से कार्यात्मक नहीं)",
    "Deutsch": "🧐 WaitForAI Beta-Test: Erleben Sie das Modell mit Mistral-7B-Instruct-v0.3 (Testversion, noch nicht vollständig funktionsfähig)",
    "日本語": "🧐 WaitForAI ベータテスト：Mistral-7B-Instruct-v0.3 でモデルを体験 (完全に機能していないテストバージョン)"
}

# Sélection du titre en fonction de la langue choisie
selected_title = titles.get(selected_language, "WaitForAI Beta Test: Experience the model with Mistral-7B-Instruct-v0.3 (test version, not fully functional)")

# Application du titre multilingue
st.title(selected_title)

# Textes fixes traduits
translations = {
    "English": {
        "enter_question": "Enter a main question:",
        "initial_response": "Complete response generated:",
        "main_question": "Main question:",
        "response": "Response:",
        "your_response": "Your response to the main question:",
        "validate_response": "Validate main response",
        "sub_questions_1": "Sub-questions Level 1:",
        "sub_questions_2": "Sub-sub-questions Level 2:",
        "final_summary": "Final summary:",
        "compare_responses": "Compare responses:",
        "initial_response": "Initial response:",
        "final_response": "Final response:",
        "summary_details": "Summary details:",
        "generate_final_summary": "Generate final summary"
    },
    "Français": {
        "enter_question": "Entrez une question principale :",
        "initial_response": "Réponse complète générée :",
        "main_question": "Question principale :",
        "response": "Réponse :",
        "your_response": "Votre réponse à la question principale :",
        "validate_response": "Valider la réponse principale",
        "sub_questions_1": "Sous-questions de Niveau 1 :",
        "sub_questions_2": "Sous-sous-questions de Niveau 2 :",
        "final_summary": "Reformulation finale :",
        "compare_responses": "Comparaison des réponses :",
        "initial_response": "Réponse initiale :",
        "final_response": "Réponse reformulée :",
        "summary_details": "Détails des étapes de reformulation :",
        "generate_final_summary": "Générer la reformulation finale"
    },
    "Español": {
        "enter_question": "Introduce una pregunta principal:",
        "initial_response": "Respuesta completa generada:",
        "main_question": "Pregunta principal:",
        "response": "Respuesta:",
        "your_response": "Tu respuesta a la pregunta principal:",
        "validate_response": "Validar respuesta principal",
        "sub_questions_1": "Subpreguntas de Nivel 1:",
        "sub_questions_2": "Sub-subpreguntas de Nivel 2:",
        "final_summary": "Resumen final:",
        "compare_responses": "Comparar respuestas:",
        "initial_response": "Respuesta inicial:",
        "final_response": "Respuesta reformulada:",
        "summary_details": "Detalles del resumen:",
        "generate_final_summary": "Generar resumen final"
    },
    "Português": {
        "enter_question": "Insira uma pergunta principal:",
        "initial_response": "Resposta completa gerada:",
        "main_question": "Pergunta principal:",
        "response": "Resposta:",
        "your_response": "Sua resposta à pergunta principal:",
        "validate_response": "Validar resposta principal",
        "sub_questions_1": "Subperguntas de Nível 1:",
        "sub_questions_2": "Sub-subperguntas de Nível 2:",
        "final_summary": "Resumo final:",
        "compare_responses": "Comparar respostas:",
        "initial_response": "Resposta inicial:",
        "final_response": "Resposta reformulada:",
        "summary_details": "Detalhes do resumo:",
        "generate_final_summary": "Gerar resumo final"
    },
    "العربية": {
        "enter_question": "أدخل سؤالاً رئيسياً:",
        "initial_response": "الإجابة الكاملة المولدة:",
        "main_question": "السؤال الرئيسي:",
        "response": "الإجابة:",
        "your_response": "إجابتك على السؤال الرئيسي:",
        "validate_response": "تحقق من الإجابة الرئيسية",
        "sub_questions_1": "الأسئلة الفرعية مستوى 1:",
        "sub_questions_2": "الأسئلة الفرعية الفرعية مستوى 2:",
        "final_summary": "الملخص النهائي:",
        "compare_responses": "مقارنة الإجابات:",
        "initial_response": "الإجابة الأولية:",
        "final_response": "الإجابة المعدلة:",
        "summary_details": "تفاصيل الملخص:",
        "generate_final_summary": "إنشاء الملخص النهائي"
    },
    "Русский": {
        "enter_question": "Введите основной вопрос:",
        "initial_response": "Полный ответ сгенерирован:",
        "main_question": "Основной вопрос:",
        "response": "Ответ:",
        "your_response": "Ваш ответ на основной вопрос:",
        "validate_response": "Подтвердить основной ответ",
        "sub_questions_1": "Подвопросы Уровень 1:",
        "sub_questions_2": "Под-подвопросы Уровень 2:",
        "final_summary": "Итоговое резюме:",
        "compare_responses": "Сравнить ответы:",
        "initial_response": "Первоначальный ответ:",
        "final_response": "Переформулированный ответ:",
        "summary_details": "Детали резюме:",
        "generate_final_summary": "Сгенерировать итоговое резюме"
    },
    "हिन्दी": {
        "enter_question": "एक मुख्य सवाल दर्ज करें:",
        "initial_response": "पूरा उत्तर उत्पन्न:",
        "main_question": "मुख्य सवाल:",
        "response": "उत्तर:",
        "your_response": "आपका मुख्य सवाल का उत्तर:",
        "validate_response": "मुख्य उत्तर की पुष्टि करें",
        "sub_questions_1": "उप-सवाल स्तर 1:",
        "sub_questions_2": "उप-उप-सवाल स्तर 2:",
        "final_summary": "अंतिम सारांश:",
        "compare_responses": "उत्तरों की तुलना करें:",
        "initial_response": "प्रारंभिक उत्तर:",
        "final_response": "पुनर्व्यवस्थित उत्तर:",
        "summary_details": "सारांश विवरण:",
        "generate_final_summary": "अंतिम सारांश उत्पन्न करें"
    },
    "Deutsch": {
        "enter_question": "Geben Sie eine Hauptfrage ein:",
        "initial_response": "Vollständige Antwort generiert:",
        "main_question": "Hauptfrage:",
        "response": "Antwort:",
        "your_response": "Ihre Antwort auf die Hauptfrage:",
        "validate_response": "Hauptantwort überprüfen",
        "sub_questions_1": "Unterfragen Ebene 1:",
        "sub_questions_2": "Unter-Unterfragen Ebene 2:",
        "final_summary": "Endzusammenfassung:",
        "compare_responses": "Antworten vergleichen:",
        "initial_response": "Erste Antwort:",
        "final_response": "Umformulierte Antwort:",
        "summary_details": "Zusammenfassungsdetails:",
        "generate_final_summary": "Endzusammenfassung generieren"
    },
    "日本語": {
        "enter_question": "主要な質問を入力してください:",
        "initial_response": "完全な応答が生成されました:",
        "main_question": "主要な質問:",
        "response": "応答:",
        "your_response": "主要な質問へのあなたの応答:",
        "validate_response": "主要な応答を検証する",
        "sub_questions_1": "サブ質問レベル1:",
        "sub_questions_2": "サブサブ質問レベル2:",
        "final_summary": "最終的な要約:",
        "compare_responses": "応答を比較する:",
        "initial_response": "初期応答:",
        "final_response": "改訂された応答:",
        "summary_details": "要約の詳細:",
        "generate_final_summary": "最終的な要約を生成する"
    }
}

# Utilisation des traductions pour les textes de l'interface
t = translations[selected_language]

