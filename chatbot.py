import streamlit as st
import requests
from streamlit_chat import message

# GeminiAI API details
API_KEY = "AIzaSyCQxZYa_je4v5OLZQk-tWJunHiCIyohCGo"
API_URL = "https://api.gemini.ai/v1/chat"

# Function to send user input to GeminiAI API
def get_response_from_geminiai(user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "message": user_input,
    }
    try:
        response = requests.post(API_URL, json=data, headers=headers)
        if response.status_code == 200:
            return response.json().get("response", "Sorry, I didn't understand that.")
        else:
            return f"Error: {response.status_code}, {response.text}"
    except Exception as e:
        return f"Connection error: {e}"

# Streamlit app
def main():
    st.title("Chatbot with GeminiAI")
    st.write("This is a chatbot powered by GeminiAI API. Ask me anything!")

    # Initialize session state for chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # User input
    with st.form(key="chat_form"):
        user_input = st.text_input("You:", placeholder="Type your message here...")
        submit_button = st.form_submit_button(label="Send")

    # Process user input
    if submit_button and user_input:
        # Append user message to chat
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Get response from GeminiAI
        bot_response = get_response_from_geminiai(user_input)
        
        # Append bot response to chat
        st.session_state.messages.append({"role": "bot", "content": bot_response})

    # Display chat messages
    for message_data in st.session_state.messages:
        if message_data["role"] == "user":
            message(message_data["content"], is_user=True)
        else:
            message(message_data["content"], is_user=False)

if __name__ == "__main__":
    main()
