import streamlit as st
import json
import requests

# Constants (replace with your actual values)
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "664e2890-0079-4091-88d4-68d3da05aa38"
FLOW_ID = "fcd9e235-d213-41f1-b1da-f8536bd3872b"

APPLICATION_TOKEN = st.secrets["APPLICATION_TOKEN"] # Update with your token

# Tweaks for the flow (ensure no "input_value" for ChatInput to avoid conflict)
TWEAKS = {
    "ChatInput-zQIS4": {
        "background_color": "",
        "chat_icon": "",
        "files": "",
        "sender": "User",
        "sender_name": "User",
        "session_id": "",
        "should_store_message": True,
        "text_color": ""
    },
    "Prompt-yP9dB": {
        "template": (
            "You are a proficient telugu translator. So, whatever is the speech that will be given to you translate it to telugu.\n\n"
            "speech: {Speech}"
        ),
        "Speech": "ASTRA_DB_NEW"
    },
    "OpenAIModel-fbfjY": {
        "api_key": "NEW_VARIABLE",
        "input_value": "",
        "json_mode": False,
        "max_tokens": None,
        "model_kwargs": {},
        "model_name": "gpt-4o-mini",
        "openai_api_base": "",
        "output_schema": {},
        "seed": 1,
        "stream": False,
        "system_message": "",
        "temperature": 0.5
    },
    "ChatOutput-5kxVW": {
        "background_color": "",
        "chat_icon": "",
        "data_template": "{text}",
        "input_value": "",
        "sender": "Machine",
        "sender_name": "AI",
        "session_id": "",
        "should_store_message": True,
        "text_color": ""
    }
}

def run_flow(message: str,
             endpoint: str,
             output_type: str = "chat",
             input_type: str = "chat",
             tweaks: dict = None,
             application_token: str = None) -> dict:
    """
    Run the flow by sending the message and tweaks to the API.
    """
    # Construct the API URL
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint or FLOW_ID}"
    st.write("Calling API URL:", api_url)  # Debug: print the URL being used
    
    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    if tweaks:
        payload["tweaks"] = tweaks

    headers = {}
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}

    response = requests.post(api_url, json=payload, headers=headers)

    # Check for a successful response
    if response.status_code != 200:
        st.error(f"Error: Received status code {response.status_code}")
        st.write("Response content:", response.text)
        return {}

    # Attempt to parse JSON, with error handling
    try:
        return response.json()
    except json.JSONDecodeError:
        st.error("Failed to decode JSON. Response content:")
        st.write(response.text)
        return {}

def main():
    st.title("English to Telugu Translator Chatbot")
    st.markdown("Enter English text below, and the chatbot will translate it to Telugu.")

    message = st.text_area("Enter text to translate:", height=150)

    if st.button("Translate"):
        if not message.strip():
            st.warning("Please enter some text to translate.")
        else:
            with st.spinner("Translating..."):
                response = run_flow(
                    message=message,
                    endpoint=FLOW_ID,
                    tweaks=TWEAKS,
                    application_token=APPLICATION_TOKEN
                )

            # Extract and display only the translated text if available
            if response:
                try:
                    translated_text = response["outputs"][0]["outputs"][0]["results"]["message"]["data"]["text"]
                    st.success("Translation received!")
                    st.write("Translated Text:", translated_text)
                except (IndexError, KeyError) as e:
                    st.error("Error extracting translated text from the response.")
                    st.json(response)

if __name__ == "__main__":
    main()