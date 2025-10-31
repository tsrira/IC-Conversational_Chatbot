# 🤖 Conversational Chatbot & Local LLM Text Generation Service

A full-stack **Conversational Chatbot** and **Text Generation Service** built using **LangChain**, **LlamaIndex**, and **FastAPI**, featuring a **Streamlit UI**.  
The entire solution is containerized with **Docker** and deployed on **AWS EC2** for scalable cloud-based inference.

---

## 🚀 Features

- 💬 Conversational chatbot UI powered by **Streamlit**
- 🧠 Toggle between **LangChain** and **LlamaIndex** backend APIs
- ⚡️ **FastAPI** microservices for each framework  
  - Port **8000** → LangChain  
  - Port **8001** → LlamaIndex  
- 🐳 Single **Docker container** runs both APIs + Streamlit UI
- 🔐 Secure **API key management** via `.streamlit/secrets.toml`
- ☁️ Fully **deployed on AWS EC2** with public endpoint

---

## 🧩 Technology Stack

| Layer | Technology | Description |
|-------|-------------|-------------|
| Frontend | Streamlit | Interactive chat UI |
| Backend APIs | FastAPI | RESTful microservices for chat endpoints |
| Frameworks | LangChain, LlamaIndex | Conversational memory & LLM orchestration |
| Model | OpenAI GPT-3.5-Turbo | Language generation |
| Packaging | Docker, Supervisor | Multi-service containerization |
| Cloud | AWS EC2 (Ubuntu 24.04) | Hosting and deployment |
| Environment | Python 3.11 | Runtime base |

---

## 🧱 Project Structure

```
├── app.py                  # Streamlit frontend with model switch
├── lang_chat.py            # FastAPI app for LangChain
├── llamaindex_chat.py      # FastAPI app for LlamaIndex
├── requirements.txt        # Dependencies
├── Dockerfile              # Container setup (Streamlit + APIs)
├── supervisord.conf        # Manages multiple processes
├── .streamlit/
│   └── secrets.toml        # Stores API keys securely
└── README.md               # Documentation
```

---

## ⚙️ Setup & Local Run

### 1️⃣ Add Your API Key
Create `.streamlit/secrets.toml` and include:
```toml
OPENAI_API_KEY = "YOUR_API_KEY"
```

### 2️⃣ Install Requirements
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Locally
```bash
python lang_chat.py    # Runs LangChain API on port 8000
python llamaindex_chat.py  # Runs LlamaIndex API on port 8001
streamlit run app.py   # Runs Streamlit UI on port 8501
```

Access at 👉 **http://localhost:8501**

---

## 🐳 Docker Deployment

### Build Image
```bash
docker build -t ai-frameworks-chatbot .
```

### Run Container
```bash
docker run -d -p 8501:8501 -p 8000:8000 -p 8001:8001 ai-frameworks-chatbot
```

Then open your browser at  
👉 **http://localhost:8501**

---

## ☁️ AWS EC2 Deployment (Free Tier Eligible)

1. Launch an **Ubuntu 24.04 EC2 Instance (t2.micro)**  
2. SSH into instance  
3. Install Docker  
   ```bash
   sudo apt update && sudo apt install docker.io -y
   ```
4. Copy project files using **WinSCP** or **git clone**  
5. Build & Run Docker  
   ```bash
   docker build -t ai-frameworks-chatbot .
   docker run -d -p 8501:8501 -p 8000:8000 -p 8001:8001 ai-frameworks-chatbot
   ```
6. Add **Inbound Rules** to Security Group  
   - TCP 22 → SSH (Your IP only)  
   - TCP 8501, 8000, 8001 → 0.0.0.0/0  

✅ Access at:  
**http://<your-ec2-public-ip>:8501**

---

## 🧠 Technical Architecture

### 📘 Architecture Overview

Below is the architecture representing:
- Streamlit UI
- LangChain & LlamaIndex FastAPI backends
- Docker container orchestration
- AWS EC2 deployment layer

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/43340618-4347-42b6-b40b-aab926dd1a0b" />

---


## 🏁 Live Demo

🌍 **Deployed Endpoint:**  
[http://34.228.167.130:8501](http://34.228.167.130:8501)

🧠 Try both **LangChain** and **LlamaIndex** models from the dropdown in the UI.


---

## 📚 Example Output

### 🔹 LangChain Chat
<img width="680" alt="LangChain Chat" src="https://github.com/user-attachments/assets/72998995-8d0d-40ba-ba5f-0be8970599a5" />

### 🔹 LlamaIndex Chat
<img width="660" alt="LlamaIndex Chat" src="https://github.com/user-attachments/assets/0f3081bc-c616-4b9c-bc7f-a545e3ff528a" />

---

## 🔐 Security Notes

- ✅ API Keys are **never hardcoded** (stored in `.streamlit/secrets.toml`)
- ✅ Isolated **multi-process container** with Supervisor
- ✅ AWS-level network security (controlled inbound rules)

---

## 📄 Repository & License

🧾 **Repository:** [GitHub Link Here](#)  
🛡️ **License:** MIT License © 2025 — Open for educational and research use

---
