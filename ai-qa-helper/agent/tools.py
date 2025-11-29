# agent/tools.py

"""
Simple dictionary-based search tool for factual queries
"""

# Knowledge base - a simple dictionary with factual information
KNOWLEDGE_BASE = {
    "python": "Python is a high-level programming language known for its simplicity and readability. Created by Guido van Rossum in 1991.",
    "fastapi": "FastAPI is a modern, fast web framework for building APIs with Python based on standard Python type hints.",
    "ai": "Artificial Intelligence (AI) refers to computer systems that can perform tasks requiring human intelligence, such as learning and problem-solving.",
    "machine learning": "Machine Learning is a subset of AI that enables systems to learn and improve from experience without being explicitly programmed.",
    "langchain": "LangChain is a framework for developing applications powered by language models, providing tools for chaining LLM calls.",
    "langgraph": "LangGraph is a library for building stateful, multi-actor applications with LLMs, built on top of LangChain.",
    "groq": "Groq provides fast AI inference with its LPU (Language Processing Unit) technology, offering high-speed LLM API access.",
    "api": "API (Application Programming Interface) is a set of rules that allows different software applications to communicate with each other.",
    "rest": "REST (Representational State Transfer) is an architectural style for designing networked applications using HTTP methods.",
    "json": "JSON (JavaScript Object Notation) is a lightweight data-interchange format that is easy to read and write."
}


def search_tool(query: str) -> str:
    """
    Simple search tool that looks up information in the knowledge base.
    
    Args:
        query (str): The search query (topic to look up)
        
    Returns:
        str: Information about the query if found, otherwise a not-found message
    """
    query_lower = query.lower().strip()
    
    # Direct match
    if query_lower in KNOWLEDGE_BASE:
        return f"Found: {KNOWLEDGE_BASE[query_lower]}"
    
    # Partial match - check if query is contained in any key
    for key, value in KNOWLEDGE_BASE.items():
        if query_lower in key or key in query_lower:
            return f"Found: {value}"
    
    # No match found
    return f"No information found for '{query}'. This tool has limited knowledge about: {', '.join(KNOWLEDGE_BASE.keys())}"


def get_tool_description() -> dict:
    """
    Returns metadata about the search tool for the agent to understand when to use it.
    
    Returns:
        dict: Tool description including name, description, and parameters
    """
    return {
        "name": "search_tool",
        "description": "Searches a knowledge base for factual information about technology topics. Use this when the user asks factual questions about Python, AI, APIs, FastAPI, LangChain, or related topics.",
        "parameters": {
            "query": "The topic or term to search for (string)"
        }
    }


# Test the tool
if __name__ == "__main__":
    print("Testing search_tool:")
    print(search_tool("python"))
    print(search_tool("FastAPI"))
    print(search_tool("blockchain"))