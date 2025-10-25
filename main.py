
from dotenv import load_dotenv
load_dotenv() # This MUST be the first thing to run
from crewai import LLM, Crew, Process
import os


# --- API KEY VALIDATION ---
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") 
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("Error: GOOGLE_API_KEY not found. "
                     "Make sure it's set in your .env file.")
if not SERPER_API_KEY:
    raise ValueError("Error: SERPER_API_KEY not found. "
                     "Make sure it's set in your .env file.")
# ---------------------------------



# 1. Import all agent-creation FUNCTIONS from the 'agents' package
from agents import (
    create_anecdotal_scout_agent,
    create_official_scout_agent,
    create_data_validator_agent,
    create_epidemiologist_agent,
    create_alert_drafter_agent,
    create_sitrep_generator_agent
)

# 2. Import the task creation class from the 'tasks' package
from tasks import PublicHealthTasks

# --- Initialize the LLM ---
from crewai import LLM

llm = LLM(
    model="gemini/gemini-2.0-flash-lite",
    api_key=GOOGLE_API_KEY,  
    temperature=0.7
)


# --- 3. Instantiate all Agents (by calling their functions) ---
anecdotal_scout_agent = create_anecdotal_scout_agent(llm)
official_scout_agent = create_official_scout_agent(llm)
data_validator_agent = create_data_validator_agent(llm)
epidemiologist_agent = create_epidemiologist_agent(llm)
alert_drafter_agent = create_alert_drafter_agent(llm)
sitrep_generator_agent = create_sitrep_generator_agent(llm)


# --- Define Your Inputs ---
disease = "Dengue Fever Outbreak"
region = "Delhi, India"

# 4. Instantiate your task class
tasks = PublicHealthTasks()

# --- 5. Define All Tasks ---

# Task 1 & 2: The parallel scouting tasks
task_find_anecdotal_reports = tasks.find_anecdotal_reports_task(
    agent=anecdotal_scout_agent,
    disease=disease,
    region=region
)

task_find_official_reports = tasks.find_official_reports_task(
    agent=official_scout_agent,
    disease=disease,
    region=region
)

# Task 3: The validation task
task_validate_data = tasks.validate_data_task(
    agent=data_validator_agent,
    context=[task_find_anecdotal_reports, task_find_official_reports]
)

# Task 4: The assessment task
task_assess_threat_level = tasks.assess_threat_level_task(
    agent=epidemiologist_agent,
    context=[task_validate_data]
)

# Task 5: The alert drafting task
task_draft_alert = tasks.draft_alert_task(
    agent=alert_drafter_agent,
    context=[task_assess_threat_level]
)

# Task 6: The final report generation task
task_generate_sitrep = tasks.generate_sitrep_task(
    agent=sitrep_generator_agent,
    context=[
        task_validate_data,
        task_assess_threat_level,
        task_draft_alert
    ],
    disease=disease,
    region=region
)

# --- 6. Assemble the Crew ---

crew_agents = [
    anecdotal_scout_agent,
    official_scout_agent,
    data_validator_agent,
    epidemiologist_agent,
    alert_drafter_agent,
    sitrep_generator_agent
]

crew_tasks = [
    task_find_anecdotal_reports,
    task_find_official_reports,
    task_validate_data,
    task_assess_threat_level,
    task_draft_alert,
    task_generate_sitrep
]

crew = Crew(
    agents=crew_agents,
    tasks=crew_tasks,
    process=Process.sequential,
    verbose=True
)

# --- 7. Run the Crew ---

print("========================================")
print(f"🚀 Launching Public Health Crew for:")
print(f"   Disease: {disease}")
print(f"   Region:  {region}")
print("========================================")

result = crew.kickoff()

print("\n========================================")
print("✅ Crew run completed.")
print("Final Result:")
print(result)
print("========================================")
print(f"Check your project folder for the final report: SitRep_{disease.replace(' ', '_')}_{region.replace(' ', '_')}.md")