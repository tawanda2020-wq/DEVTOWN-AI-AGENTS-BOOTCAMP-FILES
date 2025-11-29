# Complete Step-by-Step Execution Guide

## 📋 Pre-Execution Checklist

- [ ] Python 3.8+ installed
- [ ] VS Code installed
- [ ] Git installed
- [ ] Groq API account created
- [ ] Groq API key obtained

---

## 🚀 Step-by-Step Execution

### Step 1: Create Project Directory

```bash
# Create project folder
mkdir ai-qa-helper
cd ai-qa-helper

# Initialize git repository
git init

# Create folder structure
mkdir agent
mkdir tests
```

### Step 2: Create Files

Create all the following files in your project:

#### 1. Create `requirements.txt`
```txt
fastapi==0.104.1
uvicorn==0.24.0
python-dotenv==1.0.0
groq==0.4.1
langchain==0.1.0
langgraph==0.0.20
pydantic==2.5.0
```

#### 2. Create `.env`
```
GROQ_API_KEY=your_actual_groq_api_key_here
```

#### 3. Create `.gitignore`
```
.env
__pycache__/
*.pyc
.vscode/
venv/
*.log
.DS_Store
```

#### 4. Create `agent/__init__.py`
```python
# This file makes the agent folder a Python package
```

#### 5. Copy the artifact files
- `agent/tools.py` (from artifact)
- `agent/memory.py` (from artifact)
- `agent/agent_logic.py` (from artifact)
- `main.py` (from artifact)
- `tests/test_agent.py` (from artifact)
- `README.md` (from artifact)

### Step 3: Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 4: Configure Groq API Key

1. Go to https://console.groq.com
2. Sign up/log in
3. Navigate to API Keys
4. Create a new API key
5. Copy the key
6. Paste it in your `.env` file

### Step 5: Run Tests

```bash
# Run the test suite
python tests/test_agent.py
```

**Expected Output:**
```
==================================================
Running AI Question-Answer Helper Tests
==================================================

=== Testing Search Tool ===
Test 1 - Search 'python': Found: Python is a high-level...
Test 2 - Search 'FASTAPI': Found: FastAPI is a modern...
Test 3 - Search 'blockchain': No information found...
✓ All search tool tests passed!

=== Testing Memory System ===
Test 1 - Added 2 messages, count: 2
Test 2 - Last user message: Hello
Test 3 - After adding 3 more messages, count: 3
Test 4 - After clear, count: 0
✓ All memory tests passed!

... (more tests)

==================================================
✓ ALL TESTS PASSED!
==================================================
```

### Step 6: Start the API Server

```bash
# Run the FastAPI application
python main.py
```

**Expected Output:**
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 7: Test the API

Open a new terminal and run these tests:

#### Test 1: Root Endpoint
```bash
curl http://localhost:8000/
```

#### Test 2: Factual Query
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Python?"}'
```

**Expected Response:**
```json
{
  "response": "Python is a high-level programming language...",
  "tool_used": true,
  "tool_result": "Found: Python is a high-level programming language...",
  "is_factual": true,
  "message_count": 2
}
```

#### Test 3: Conversational Query
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello! How are you today?"}'
```

**Expected Response:**
```json
{
  "response": "Hello! I'm doing well, thank you for asking...",
  "tool_used": false,
  "tool_result": null,
  "is_factual": false,
  "message_count": 4
}
```

#### Test 4: Check Memory
```bash
curl http://localhost:8000/memory
```

#### Test 5: Clear Memory
```bash
curl -X POST "http://localhost:8000/clear"
```

### Step 8: Access Interactive Documentation

Open your browser and go to:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

Here you can:
- See all endpoints
- Test the API interactively
- View request/response schemas

### Step 9: Take Screenshots for Report

Take screenshots of:

1. **Project Folder Structure** (in VS Code file explorer)
2. **Agent Flow Diagram** (from the Mermaid artifact)
3. **Test Results** (terminal output)
4. **API Response - Factual Query** (from browser or Postman)
5. **API Response - Conversational Query**
6. **Memory Endpoint** (showing conversation history)
7. **Swagger UI Documentation**

### Step 10: Deploy to GitHub

```bash
# Add all files
git add .

# Commit
git commit -m "Initial commit: AI Question-Answer Helper"

# Create repository on GitHub
# Then push
git remote add origin https://github.com/yourusername/ai-qa-helper.git
git branch -M main
git push -u origin main
```

---

## 🧪 Testing Scenarios

### Scenario 1: Factual Questions
Test with these queries:
- "What is FastAPI?"
- "Explain machine learning"
- "Tell me about Python"
- "What is an API?"

**Expected**: Tool should be used, factual information returned

### Scenario 2: Conversational Queries
Test with these queries:
- "Hello"
- "How are you?"
- "Thanks for your help"
- "Can you help me?"

**Expected**: No tool use, conversational response

### Scenario 3: Context Awareness
1. Send: "What is Python?"
2. Send: "Tell me more about it"
3. Send: "What are its benefits?"

**Expected**: Agent should understand context from memory

### Scenario 4: Memory Management
Send 15 messages and check `/memory` endpoint

**Expected**: Only last 10 messages retained

---

## 📊 Creating Your PDF Report

Your report should include:

### 1. Cover Page
- Project Title
- Your Name
- Date
- Course/Assignment Info

### 2. Introduction (1 page)
- What is agentic AI?
- Project objectives
- Technologies used

### 3. Project Structure (1 page)
- Folder structure screenshot
- Brief description of each file
- Architecture diagram

### 4. Implementation Details (3-4 pages)

#### 4.1 Search Tool
- Screenshot of `tools.py` code
- Explanation of knowledge base
- How matching works

#### 4.2 Memory System
- Screenshot of `memory.py` code
- Explanation of memory management
- Max message limit implementation

#### 4.3 Agent Logic
- Screenshot of `agent_logic.py` code
- Factual query detection algorithm
- Query extraction process
- LLM integration with Groq

#### 4.4 FastAPI Application
- Screenshot of `main.py` code
- Endpoint descriptions
- Request/response models

### 5. Agent Flow Diagram (1 page)
- Include the Mermaid diagram
- Explain the decision flow
- Highlight tool calling mechanism

### 6. Testing & Results (2-3 pages)
- Unit test screenshots
- API test screenshots (Postman or cURL)
- Different query type results:
  - Factual query example
  - Conversational query example
  - Context-aware conversation
- Memory endpoint screenshot

### 7. GitHub Repository (1 page)
- Repository link
- Repository screenshot
- Commit history

### 8. Challenges & Learning (1 page)
- Challenges faced
- How you solved them
- Key learnings about agentic AI

### 9. Conclusion (1 page)
- Project summary
- Understanding of agent behavior
- Future improvements

### 10. Appendix
- Full code listings (if required)
- Environment setup details
- API documentation

---

## 🎯 Verification Checklist

Before submitting, verify:

- [ ] All code files created and working
- [ ] Tests passing successfully
- [ ] API server starts without errors
- [ ] All endpoints responding correctly
- [ ] Screenshots taken and organized
- [ ] GitHub repository created and pushed
- [ ] PDF report complete with all sections
- [ ] Agent flow diagram included
- [ ] Code is well-commented
- [ ] README.md is comprehensive

---

## 💡 Pro Tips

1. **Code Comments**: Add detailed comments explaining your logic
2. **Error Handling**: Test error cases (empty messages, invalid API key)
3. **Documentation**: Keep your README clear and detailed
4. **Git Commits**: Make meaningful commit messages
5. **Screenshots**: Use high-quality screenshots with good visibility
6. **Report**: Keep explanations clear and concise

---

## 🆘 Troubleshooting

### Issue: Import errors
**Solution**: Make sure `agent/__init__.py` exists and you're in the right directory

### Issue: Groq API errors
**Solution**: 
- Check your API key in `.env`
- Verify you have credits in your Groq account
- Check internet connection

### Issue: Port 8000 already in use
**Solution**: 
```bash
# Use a different port
uvicorn main:app --port 8001
```

### Issue: Module not found
**Solution**:
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

---

## 📝 Sample API Test Commands

Save these in a file called `api_tests.sh`:

```bash
#!/bin/bash

echo "Testing AI Question-Answer Helper API"
echo "======================================"

echo "\n1. Testing Root Endpoint..."
curl http://localhost:8000/

echo "\n\n2. Testing Factual Query..."
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "What is FastAPI?"}'

echo "\n\n3. Testing Conversational Query..."
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello!"}'

echo "\n\n4. Checking Memory..."
curl http://localhost:8000/memory

echo "\n\n5. Testing Health Check..."
curl http://localhost:8000/health

echo "\n\nAll tests completed!"
```

Make it executable and run:
```bash
chmod +x api_tests.sh
./api_tests.sh
```

---

Good luck with your project! 🚀
