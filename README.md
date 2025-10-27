# 🤖 Local LLM Text Generation Service

A full-stack Local LLM Text Generation Service built with FastAPI, LangChain, and LlamaIndex, featuring a Streamlit conversational UI. Deployed as a single Docker container on AWS EC2 for scalable and secure API access.

---

## 🚀 Features

- 💬 Conversational chatbot UI powered by Streamlit  
- 🧠 Toggle between LangChain and LlamaIndex backend APIs  
- ⚡️ FastAPI endpoints running internally on ports 8000 (LangChain) and 8001 (LlamaIndex)  
- 🐳 Single Docker container runs Streamlit UI + both APIs together  
- 🌐 Secure API key handling via Streamlit secrets  

---

## 📦 Setup & Deployment

1. **Configure API Key**  

  Add your OpenAI API key to `.streamlit/secrets.toml`:
  OPENAI_API_KEY = "YOUR_API_KEY"
   
2. **Build Docker Image**  
 
 docker build -t local-llm-chatbot .

3. **Run Docker Container**  

 docker run -p 8501:8501 -p 8000:8000 -p 8001:8001 local-llm-chatbot

4. **Access the Chatbot**  

 Visit `http://localhost:8501` in your browser.  
 Select LangChain or LlamaIndex from the dropdown menu.  
 Start chatting!

---

## 📚 Project Structure


├── app.py # Streamlit UI with backend selection

├── lang_chat.py # LangChain FastAPI API (port 8000)

├── llamaindex_chat.py # LlamaIndex FastAPI API (port 8001)

├── requirements.txt # Python dependencies

├── Dockerfile # Single Dockerfile running all services with supervisord

├── supervisord.conf # Supervisor config managing multi-process

└── README.md # This file


---

## 🛡️ Security

- API keys securely loaded from Streamlit secrets and never hardcoded.
- One container approach simplifies deployment while isolating via process separation.

---

## ☁️ Cloud Deployment (AWS EC2)

- Ensure ports 8501, 8000, and 8001 are open in AWS security group rules.
- For production consider adding TLS / HTTPS and authentication.

---

## 🏁 License

MIT License  
