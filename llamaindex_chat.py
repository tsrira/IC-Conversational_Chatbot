from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.chat_engine import SimpleChatEngine
from typing import Optional

app = FastAPI(
    title="LlamaIndex ChatBot API",
    description="A conversational AI chatbot using LlamaIndex and OpenAI",
    version="1.0.0"
)

# Single chat engine instance for one user
chat_engine: Optional[SimpleChatEngine] = None

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

class LlamaIndexChatbot:
    def __init__(self):
        # Configure LlamaIndex settings
        Settings.llm = OpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7,
            api_key="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"
        )
    
    def create_chat_engine(self) -> SimpleChatEngine:
        """Create a new chat engine with memory"""
        memory = ChatMemoryBuffer.from_defaults(token_limit=3000)
        return SimpleChatEngine.from_defaults(
            llm=Settings.llm,
            memory=memory
        )

# Initialize chatbot
chatbot = LlamaIndexChatbot()

@app.post("/api/chat", response_model=ChatResponse, tags=["Chat"])
async def chat(chat_request: ChatRequest):
    """
    Send a message to the AI chatbot
    
    - **message**: Your message to the AI
    """
    global chat_engine
    
    try:
        # Create chat engine if it doesn't exist
        if chat_engine is None:
            chat_engine = chatbot.create_chat_engine()
        
        # Get AI response
        response = chat_engine.chat(chat_request.message)
        
        return ChatResponse(response=str(response))
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)