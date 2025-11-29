# Tawanda.Ronald.Munyanyi
# ronaldtmunyanyi@gmail.com
# +26377280167

# AI Question-Answer Helper
An intelligent AI agent that answers user questions and uses a search tool for factual queries while maintaining conversation context.

## Project Overview
This project demonstrates core agentic AI concepts:
**Reasoning**: Detecting whether queries are factual or conversational
**Tool Use**: Calling a search tool when factual information is needed
**Memory**: Maintaining short-term conversation context

## Project Structure
ai-qa-helper/
├── .env                  # Environment variables (API keys)
├── .gitignore            # Git ignore file
├── requirements.txt      # Python dependencies
├── main.py               # FastAPI application
├── agent/
│   ├── __init__.py
│   ├── tools.py          # Search tool implementation
│   ├── agent_logic.py    # Core agent reasoning
│   └── memory.py         # Conversation memory
├── tests/
│   └── test_agent.py     # Test suite
└── README.md             # This file

## Installation & Setup
### Prerequisites
- Python 3.8+
- Groq API key (get it from [console.groq.com](https://console.groq.com))

### Step 1: Clone the Repository
```bash
git clone <your-repo-url>
cd ai-qa-helper
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Tests
```bash
python tests/test_agent.py
```

### Step 5: Start the API Server
```bash
python main.py
```

The server will start at `http://localhost:8000`

## API Endpoints

### 1. Root Endpoint
```http
GET /
```
Returns API information and available endpoints.

### 2. Chat Endpoint
```http
POST /chat
Content-Type: application/json

{
  "message": "What is Python?"
}
```

**Response:**
```json
{
  "response": "Python is a high-level programming language...",
  "tool_used": true,
  "tool_result": "Found: Python is a high-level programming language...",
  "is_factual": true,
  "message_count": 2
}
```

### 3. Memory Endpoint
```http
GET /memory
```
Returns current conversation history.

### 4. Clear Memory
```http
POST /clear
```
Clears the conversation memory.

### 5. Health Check
```http
GET /health
```
Returns service health status.


## Testing
### Run Unit Tests
```bash
python tests/test_agent.py
```


## How It Works
### 1. Search Tool (`tools.py`)
- Dictionary-based knowledge base
- Returns factual information about technology topics
- Simple keyword matching
### 2. Memory System (`memory.py`)
- Stores last 10 messages
- Maintains conversation context
- Provides formatted history for the LLM
### 3. Agent Logic (`agent_logic.py`)
**Decision Flow:**
1. **Analyze Query**: Detect if factual using keywords
2. **Tool Decision**: Call search tool if factual
3. **LLM Generation**: Create response using Groq API
4. **Memory Update**: Store conversation in memory

**Key Functions:**
- `is_factual_query()`: Detects factual questions
- `extract_search_query()`: Extracts search terms
- `process_user_query()`: Main agent orchestration
### 4. FastAPI Application (`main.py`)
- RESTful API endpoints
- Request/response validation
- Error handling
- Interactive documentation
