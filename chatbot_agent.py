import os
import multiprocessing as mp
import asyncio
from dotenv import load_dotenv
from agentspan.agents import Agent, AgentRuntime, ConversationMemory, tool
from tavily_agent_toolkit import search_and_format

load_dotenv()

# .env mein uppercase GROQ_API_KEY hai
groq_api_key = os.getenv("GROQ_API_KEY")

memory = ConversationMemory(max_messages=50)
session_id = "chatbot_session"

@tool
def say_hello() -> str:
    """Before answering any message, use this tool"""
    message = "HI, 12345"
    print(message)
    return message  # Model ko return value milna zaroori hai

@tool
def internet_search_tool(query: str) -> str:
    """Search the internet for latest information."""
    tavily_api_key = os.getenv("TAVILY_API_KEY")

    return asyncio.run(search_and_format(
        queries=[query],
        api_key=tavily_api_key,
        search_depth="basic",
        max_results=3,
    ))

# Agar Groq use kar rahe hain toh model "groq/..." format mein hona chahiye:
chatbot_agent = Agent(
    name="chatbot_agent",
    model="groq/llama-3.3-70b-versatile",  # OpenAI use karna ho to "openai/gpt-4o" rakhein aur .env mein OPENAI_API_KEY add karein
    instructions="You are a helpful agent named Alex. Use tools for better responses.",
    tools=[internet_search_tool, say_hello],
    memory=memory
)

def get_resp(query):
    with AgentRuntime() as runtime:
        result = runtime.run(chatbot_agent, query, session_id=session_id)
        return result

def main():
    while True:
        query = input("Ask Query: ")

        if query.strip().lower() == "q":
            break

        resp = get_resp(query)
        resp.print_result()

if __name__ == "__main__":
    # Windows par 'fork' nahi chalta, 'spawn' lazmi hai
    mp.set_start_method("spawn", force=True)
    main()