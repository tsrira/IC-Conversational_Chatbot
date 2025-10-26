import streamlit as st
import requests

# Streamlit App settings
st.set_page_config(page_title="Conversational Chatbot", layout="centered")
st.title("🤖 Conversational Chatbot")

# --- Securely load API key from Streamlit secrets ---
OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.warning("⚠️ No API key found. Please set it in Streamlit Secrets.")
else:
    st.success("🗝️ API key loaded securely.")

# Backend endpoints
API_OPTIONS = {
    "LangChain": "http://localhost:8000/api/chat",
    "LlamaIndex": "http://localhost:8001/api/chat"
}

# Model selection
selected_model = st.selectbox("Select Model Backend:", ["LangChain", "LlamaIndex"])
api_url = API_OPTIONS[selected_model]

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
if "selected_model" not in st.session_state:
    st.session_state.selected_model = selected_model
elif st.session_state.selected_model != selected_model:
    st.session_state.messages = []
    st.session_state.selected_model = selected_model

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = requests.post(api_url, json={"message": prompt})
        if response.status_code == 200:
            bot_reply = response.json().get("response", "⚠️ No response received.")
        else:
            bot_reply = f"Error {response.status_code}: {response.text}"
    except Exception as e:
        bot_reply = f"❌ Connection error: {e}"

    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
