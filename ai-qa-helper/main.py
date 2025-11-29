# main.py

"""
FastAPI application for the AI Question-Answer Helper
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from agent.agent_logic import process_user_query
from agent.memory import conversation_memory
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="AI Question-Answer Helper",
    description="An AI agent that answers questions and uses search tools for factual queries",
    version="1.0.0"
)


# Request model
class ChatRequest(BaseModel):
    message: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "message": "What is FastAPI?"
            }
        }


# Response model
class ChatResponse(BaseModel):
    response: str
    tool_used: bool
    tool_result: Optional[str]
    is_factual: bool
    message_count: int
    
    class Config:
        json_schema_extra = {
            "example": {
                "response": "FastAPI is a modern, fast web framework...",
                "tool_used": True,
                "tool_result": "Found: FastAPI is a modern web framework...",
                "is_factual": True,
                "message_count": 2
            }
        }


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to AI Question-Answer Helper API",
        "version": "1.0.0",
        "endpoints": {
            "/chat": "POST - Send a message to the AI agent",
            "/memory": "GET - View conversation history",
            "/clear": "POST - Clear conversation memory",
            "/docs": "GET - API documentation"
        }
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Main chat endpoint - send a message and get a response from the AI agent.
    
    The agent will:
    - Detect if your question is factual
    - Use the search tool for factual queries
    - Generate conversational responses otherwise
    - Maintain conversation context
    """
    try:
        if not request.message or request.message.strip() == "":
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        # Process the query using the agent
        result = process_user_query(request.message)
        
        return ChatResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")


@app.get("/memory")
async def get_memory():
    """Get the current conversation history"""
    return {
        "message_count": conversation_memory.get_message_count(),
        "messages": conversation_memory.get_messages(),
        "context": conversation_memory.get_context()
    }


@app.post("/clear")
async def clear_memory():
    """Clear the conversation memory"""
    conversation_memory.clear()
    return {
        "message": "Conversation memory cleared successfully",
        "message_count": conversation_memory.get_message_count()
    }


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "AI Question-Answer Helper"
    }


# Run the application
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )