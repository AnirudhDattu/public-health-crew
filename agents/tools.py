import os
from crewai_tools import SerperDevTool, FileWriterTool
from dotenv import load_dotenv

# Load environment variables just for the tools if they need it
load_dotenv() 

# --- Initialize the Tools ---
search_tool = SerperDevTool()
file_write_tool = FileWriterTool()