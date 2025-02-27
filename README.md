# English to Telugu Translator Chatbot 🌍➡️🇮🇳
This is a Streamlit-based chatbot that translates English text into Telugu using the Langflow API and OpenAI's GPT-4o-mini model.
You can view the live app here : https://english-to-telugu-2owwt8jgteyfom9uf9aj3k.streamlit.app/

# Features
✅ Real-time translation from English to Telugu
✅ User-friendly Streamlit interface
✅ AI-powered translation with Langflow API
✅ Error handling for API responses
✅ Interactive and easy to use

# Tech Stack
Python 🐍
Streamlit 🎨 (for UI)
Langflow API ⚡ (for AI translation)
OpenAI GPT-4o-mini 🤖 (for generating translations)
REST API requests 📡

# Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-repo/english-to-telugu-translator.git
cd english-to-telugu-translator

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Set Up API Token
Obtain your APPLICATION_TOKEN from your Langflow API account.
Store it in your Streamlit secrets (.streamlit/secrets.toml):
[secrets]
APPLICATION_TOKEN = "your_actual_application_token_here"

4️⃣ Run the Translator App

streamlit run app.py

# Usage

1️⃣ Enter English text in the input box.

2️⃣ Click "Translate" to get the Telugu translation.

3️⃣ View the translated text instantly.

# API Integration

This app integrates with the Langflow API to generate translations. The API request follows this structure:

Base URL: https://api.langflow.astra.datastax.com

Flow ID: fcd9e235-d213-41f1-b1da-f8536bd3872b

Authorization: Requires APPLICATION_TOKEN

# Error Handling
The app handles:

Invalid API responses
JSON parsing errors
Empty input warnings
Future Enhancements 🚀
🔹 Support for multiple languages
🔹 Voice input for translation
🔹 Save translation history

