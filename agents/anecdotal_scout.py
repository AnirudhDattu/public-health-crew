#agents/anecdotal_scout.py

from crewai import Agent
from .tools import search_tool  # <-- Note: llm is removed here

def create_anecdotal_scout_agent(llm):  # <-- This is now a function
    return Agent(  # <-- It returns the agent
        role="Anecdotal Health Data Scout",
        goal="Scan social media (e.g., Reddit, X/Twitter) and forums for "
             "anecdotal reports of '{disease}' in '{region}'. "
             "Look for keywords like 'sick', 'outbreak', 'flu', 'symptoms' "
             "and specific locations.",
        backstory="You are a digital sleuth, an expert in Open Source "
                  "Intelligence (OSINT). Your specialty is navigating "
                  "the 'digital chatter' of the internet to find early, "
                  "unofficial signals of public health trends. You "
                  "understand slang, sarcasm, and how people "
                  "casually describe being sick online.",
        verbose=True,
        allow_delegation=False,
        tools=[search_tool],
        llm=llm  # <-- The passed-in llm is used here
    )