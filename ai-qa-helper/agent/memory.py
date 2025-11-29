# agent/memory.py

"""
Simple short-term memory system for maintaining conversation context
"""

from typing import List, Dict
from datetime import datetime


class ConversationMemory:
    """
    A simple in-memory storage for conversation history.
    Keeps track of recent messages to maintain context.
    """
    
    def __init__(self, max_messages: int = 10):
        """
        Initialize the memory system.
        
        Args:
            max_messages (int): Maximum number of messages to keep in memory
        """
        self.max_messages = max_messages
        self.messages: List[Dict] = []
    
    def add_message(self, role: str, content: str):
        """
        Add a message to the conversation history.
        
        Args:
            role (str): The role of the message sender ('user' or 'assistant')
            content (str): The message content
        """
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        
        self.messages.append(message)
        
        # Keep only the last N messages to prevent memory overflow
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]
    
    def get_messages(self) -> List[Dict]:
        """
        Get all messages in the conversation history.
        
        Returns:
            List[Dict]: List of message dictionaries
        """
        return self.messages
    
    def get_context(self) -> str:
        """
        Get formatted conversation context for the AI.
        
        Returns:
            str: Formatted conversation history
        """
        if not self.messages:
            return "No previous conversation."
        
        context = "Recent conversation:\n"
        for msg in self.messages:
            role = msg['role'].capitalize()
            content = msg['content']
            context += f"{role}: {content}\n"
        
        return context
    
    def clear(self):
        """Clear all messages from memory."""
        self.messages = []
    
    def get_last_user_message(self) -> str:
        """
        Get the most recent user message.
        
        Returns:
            str: The last user message or empty string if none exists
        """
        for msg in reversed(self.messages):
            if msg['role'] == 'user':
                return msg['content']
        return ""
    
    def get_message_count(self) -> int:
        """
        Get the total number of messages in memory.
        
        Returns:
            int: Number of messages
        """
        return len(self.messages)


# Global memory instance for the application
conversation_memory = ConversationMemory(max_messages=10)


# Test the memory system
if __name__ == "__main__":
    memory = ConversationMemory(max_messages=5)
    
    print("Testing ConversationMemory:")
    memory.add_message("user", "Hello, what is Python?")
    memory.add_message("assistant", "Python is a programming language.")
    memory.add_message("user", "Tell me more")
    
    print("\nContext:")
    print(memory.get_context())
    
    print(f"\nMessage count: {memory.get_message_count()}")
    print(f"Last user message: {memory.get_last_user_message()}")