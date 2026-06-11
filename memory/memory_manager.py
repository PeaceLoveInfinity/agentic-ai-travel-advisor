# Memory manager for LangGraph. 
# This module provides a simple interface to save and load memory data using the MemorySaver class from the langgraph.checkpoint.memory module.
from langgraph.checkpoint.memory import MemorySaver

# Create a global instance of MemorySaver to be used throughout the application.
memory = MemorySaver()

