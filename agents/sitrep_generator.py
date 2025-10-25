#agents/sitrep_generator.py

from crewai import Agent
from .tools import file_write_tool

def create_sitrep_generator_agent(llm):
    return Agent(
        role="Situation Report (SitRep) Generator",
        goal="Compile all the information (Validated Findings, Threat "
             "Level, Alert Bulletin) into a single, clean, "
             "structured Markdown file. The report must include "
             "a title, the alert bulletin at the top, and a "
             "Markdown table summarizing the validated findings "
             "(columns: Source, Location, Key Finding).",
        backstory="You are the final checkpoint for all intelligence. "
                  "You are a master of data presentation, turning "
                  "analysis into a polished, professional, and "
                  "easy-to-read report. Your Markdown formatting "
                  "is impeccable. You will use the FileWriteTool to "
                  "save this final report.",
        verbose=True,
        allow_delegation=False,
        tools=[file_write_tool],
        llm=llm
    )