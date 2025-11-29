# agent/agent_logic.py

"""
Core agent logic for processing queries and deciding when to use tools
"""

import os
from groq import Groq
from dotenv import load_dotenv
from .tools import search_tool, get_tool_description
from .memory import conversation_memory

# Load environment variables
load_dotenv()

# Initialize Groq client
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def is_factual_query(user_message: str) -> bool:
    """
    Determine if the user's message is asking for factual information.
    
    Args:
        user_message (str): The user's input message
        
    Returns:
        bool: True if the query appears to be factual, False otherwise
    """
    factual_keywords = [
        "what is", "what are", "define", "explain", "tell me about",
        "how does", "describe", "who is", "where is", "when was",
        "information about", "details about", "facts about"
    ]
    
    message_lower = user_message.lower()
    
    # Check if any factual keyword is in the message
    for keyword in factual_keywords:
        if keyword in message_lower:
            return True
    
    return False


def extract_search_query(user_message: str) -> str:
    """
    Extract the key topic/term to search for from the user's message.
    
    Args:
        user_message (str): The user's input message
        
    Returns:
        str: Extracted search query
    """
    # Simple extraction - remove common question words
    remove_words = ["what is", "what are", "tell me about", "explain", "define", 
                    "describe", "information about", "details about", "?", "the"]
    
    query = user_message.lower()
    for word in remove_words:
        query = query.replace(word, "")
    
    return query.strip()


def generate_response_with_groq(user_message: str, context: str, tool_result: str = None) -> str:
    """
    Generate a response using Groq's LLM API.
    
    Args:
        user_message (str): The user's current message
        context (str): Previous conversation context
        tool_result (str): Result from tool call (if any)
        
    Returns:
        str: Generated response from the LLM
    """
    # Build the prompt
    if tool_result:
        system_message = f"""You are a helpful AI assistant. You have access to factual information.

{context}

Tool search result: {tool_result}

Based on the tool result above, provide a clear and helpful answer to the user's question."""
    else:
        system_message = f"""You are a helpful, friendly AI assistant. Engage in natural conversation.

{context}

Respond to the user in a conversational and helpful manner."""
    
    try:
        # Call Groq API
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            model="mixtral-8x7b-32768",  # Fast and capable model
            temperature=0.7,
            max_tokens=500
        )
        
        return chat_completion.choices[0].message.content
    
    except Exception as e:
        return f"Error generating response: {str(e)}"


def process_user_query(user_message: str) -> dict:
    """
    Main agent function that processes user queries.
    
    This function:
    1. Checks if the query is factual
    2. Uses the search tool if needed
    3. Generates a response using the LLM
    4. Updates conversation memory
    
    Args:
        user_message (str): The user's input message
        
    Returns:
        dict: Response containing the answer and metadata
    """
    # Get conversation context
    context = conversation_memory.get_context()
    
    # Step 1: Determine if this is a factual query
    is_factual = is_factual_query(user_message)
    
    tool_used = False
    tool_result = None
    
    # Step 2: Use search tool if factual
    if is_factual:
        search_query = extract_search_query(user_message)
        tool_result = search_tool(search_query)
        tool_used = True
    
    # Step 3: Generate response using LLM
    response = generate_response_with_groq(user_message, context, tool_result)
    
    # Step 4: Update memory
    conversation_memory.add_message("user", user_message)
    conversation_memory.add_message("assistant", response)
    
    # Return structured response
    return {
        "response": response,
        "tool_used": tool_used,
        "tool_result": tool_result if tool_used else None,
        "is_factual": is_factual,
        "message_count": conversation_memory.get_message_count()
    }


# Test the agent
if __name__ == "__main__":
    print("Testing Agent Logic:\n")
    
    # Test factual query
    result1 = process_user_query("What is Python?")
    print(f"Query: What is Python?")
    print(f"Response: {result1['response']}")
    print(f"Tool used: {result1['tool_used']}\n")
    
    # Test conversational query
    result2 = process_user_query("Hello, how are you?")
    print(f"Query: Hello, how are you?")
    print(f"Response: {result2['response']}")
    print(f"Tool used: {result2['tool_used']}")