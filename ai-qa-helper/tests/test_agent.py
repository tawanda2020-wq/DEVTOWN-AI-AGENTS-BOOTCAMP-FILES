# tests/test_agent.py

"""
Test suite for the AI Question-Answer Helper
"""

import sys
import os

# Add parent directory to path to import agent modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent.tools import search_tool
from agent.memory import ConversationMemory
from agent.agent_logic import is_factual_query, extract_search_query


def test_search_tool():
    """Test the search tool functionality"""
    print("\n=== Testing Search Tool ===")
    
    # Test 1: Known topic
    result1 = search_tool("python")
    print(f"Test 1 - Search 'python': {result1}")
    assert "Python is a high-level programming language" in result1
    
    # Test 2: Case insensitive
    result2 = search_tool("FASTAPI")
    print(f"Test 2 - Search 'FASTAPI': {result2}")
    assert "FastAPI" in result2
    
    # Test 3: Unknown topic
    result3 = search_tool("blockchain")
    print(f"Test 3 - Search 'blockchain': {result3}")
    assert "No information found" in result3
    
    print("✓ All search tool tests passed!\n")


def test_memory_system():
    """Test the conversation memory"""
    print("=== Testing Memory System ===")
    
    memory = ConversationMemory(max_messages=3)
    
    # Test 1: Add messages
    memory.add_message("user", "Hello")
    memory.add_message("assistant", "Hi there!")
    print(f"Test 1 - Added 2 messages, count: {memory.get_message_count()}")
    assert memory.get_message_count() == 2
    
    # Test 2: Get last user message
    last_msg = memory.get_last_user_message()
    print(f"Test 2 - Last user message: {last_msg}")
    assert last_msg == "Hello"
    
    # Test 3: Memory limit
    memory.add_message("user", "Message 3")
    memory.add_message("assistant", "Response 3")
    memory.add_message("user", "Message 4")
    print(f"Test 3 - After adding 3 more messages, count: {memory.get_message_count()}")
    assert memory.get_message_count() == 3  # Should keep only last 3
    
    # Test 4: Clear memory
    memory.clear()
    print(f"Test 4 - After clear, count: {memory.get_message_count()}")
    assert memory.get_message_count() == 0
    
    print("✓ All memory tests passed!\n")


def test_factual_detection():
    """Test factual query detection"""
    print("=== Testing Factual Query Detection ===")
    
    # Test 1: Factual queries
    factual_queries = [
        "What is Python?",
        "Tell me about FastAPI",
        "Explain machine learning",
        "Define API"
    ]
    
    for query in factual_queries:
        result = is_factual_query(query)
        print(f"Test - '{query}': {result}")
        assert result == True
    
    # Test 2: Conversational queries
    conversational_queries = [
        "Hello",
        "How are you?",
        "Thanks for your help",
        "Can you help me?"
    ]
    
    for query in conversational_queries:
        result = is_factual_query(query)
        print(f"Test - '{query}': {result}")
        assert result == False
    
    print("✓ All factual detection tests passed!\n")


def test_query_extraction():
    """Test search query extraction"""
    print("=== Testing Query Extraction ===")
    
    test_cases = [
        ("What is Python?", "python"),
        ("Tell me about FastAPI", "fastapi"),
        ("Explain machine learning", "machine learning"),
    ]
    
    for input_query, expected in test_cases:
        result = extract_search_query(input_query)
        print(f"Test - '{input_query}' -> '{result}'")
        assert expected in result.lower()
    
    print("✓ All query extraction tests passed!\n")


def run_all_tests():
    """Run all tests"""
    print("\n" + "="*50)
    print("Running AI Question-Answer Helper Tests")
    print("="*50)
    
    try:
        test_search_tool()
        test_memory_system()
        test_factual_detection()
        test_query_extraction()
        
        print("="*50)
        print("✓ ALL TESTS PASSED!")
        print("="*50 + "\n")
        
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}\n")
        raise
    except Exception as e:
        print(f"\n✗ ERROR: {e}\n")
        raise


if __name__ == "__main__":
    run_all_tests()