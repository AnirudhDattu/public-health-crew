# 🏥 Public Health Crew - AI-Powered Disease Surveillance System

## 📋 Project Overview

**Public Health Crew** is an intelligent multi-agent system designed for early detection and monitoring of disease outbreaks using AI-powered agents. The system leverages the CrewAI framework to orchestrate multiple specialized agents that work collaboratively to gather, validate, and analyze public health data from both official and anecdotal sources.

The system automatically generates comprehensive Situation Reports (SitReps) that provide actionable intelligence for public health officials and decision-makers.

## 🎯 Key Features

- **Multi-Agent Intelligence**: Six specialized AI agents working in parallel and sequential workflows
- **Dual-Source Data Collection**: Combines official health data with social media anecdotal reports
- **Data Validation & Triangulation**: Cross-references findings to eliminate noise and false information
- **Automated Threat Assessment**: Assigns threat levels (Low, Elevated, High, Severe) based on validated data
- **Professional Reporting**: Generates formatted Markdown and PDF situation reports
- **Real-time OSINT**: Leverages Open Source Intelligence techniques for early outbreak detection

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Public Health Crew System                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │         Main Orchestrator (main.py)      │
        │    - Initializes LLM (Gemini 2.0)       │
        │    - Configures agents & tasks           │
        │    - Executes workflow                   │
        └─────────────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              │                               │
              ▼                               ▼
    ┌──────────────────┐          ┌──────────────────┐
    │  PARALLEL PHASE  │          │ SEQUENTIAL PHASE │
    └──────────────────┘          └──────────────────┘
              │                             │
    ┌─────────┴─────────┐                   │
    ▼                   ▼                   │
┌─────────┐      ┌─────────────┐            │
│ Agent 1 │      │  Agent 2    │            │
│Anecdotal│      │  Official   │            │
│ Scout   │      │   Scout     │            │
└─────────┘      └─────────────┘            │
    │                   │                   │
    └─────────┬─────────┘                   │
              ▼                             │
        ┌──────────┐                        │
        │ Agent 3  │                        │
        │   Data   │                        │
        │Validator │                        │
        └──────────┘                        │
              │                             │
              ▼                             │
        ┌──────────────┐                    │
        │   Agent 4    │                    │
        │Epidemiologist│                    │
        └──────────────┘                    │
              │                             │
              ▼                             │
        ┌──────────────┐                    │
        │   Agent 5    │                    │
        │    Alert     │                    │
        │   Drafter    │                    │
        └──────────────┘                    │
              │                             │
              ▼                             │
        ┌──────────────┐                    │
        │   Agent 6    │                    │
        │    SitRep    │                    │
        │  Generator   │                    │
        └──────────────┘                    │
              │                             │
              ▼                             │
        ┌──────────────┐                    │
        │  Final SitRep│                    │
        │ (.md & .pdf) │                    │
        └──────────────┘                    │
                                            │
```

## 🤖 Agent Descriptions

| Agent | Role | Responsibilities | Tools Used |
|-------|------|------------------|------------|
| **Anecdotal Scout** | Digital Sleuth | Scans social media (Reddit, Twitter/X) and forums for early unofficial signals of outbreaks. Specializes in OSINT and understanding informal health discussions. | SerperDevTool |
| **Official Scout** | Health Data Researcher | Searches official public health sources (CDC, WHO, local health departments) and reputable news outlets for verified reports. | SerperDevTool |
| **Data Validator** | Intelligence Analyst | Cross-references anecdotal and official reports to identify corroborations. Filters out rumors and unverified information. | None (Analysis only) |
| **Epidemiologist** | Senior Public Health Expert | Analyzes validated findings to assess threat levels based on symptom severity, case velocity, and geographic spread. Assigns threat level (Low/Elevated/High/Severe). | None (Analysis only) |
| **Alert Drafter** | Crisis Communications Officer | Creates concise, professional alert bulletins (max 150 words) summarizing key trends and threat levels for public health officials. | None (Writing only) |
| **SitRep Generator** | Report Compiler | Compiles all information into a structured Markdown report with tables, threat assessments, and validated findings. Saves final report to file. | FileWriterTool |

## 📊 Task Workflow

| Task # | Task Name | Agent | Execution Mode | Dependencies | Output |
|--------|-----------|-------|----------------|--------------|--------|
| 1 | Find Anecdotal Reports | Anecdotal Scout | Parallel (Async) | None | 5-10 anecdotal findings with sources |
| 2 | Find Official Reports | Official Scout | Parallel (Async) | None | 3-5 official reports with sources |
| 3 | Validate Data | Data Validator | Sequential | Tasks 1 & 2 | List of validated findings |
| 4 | Assess Threat Level | Epidemiologist | Sequential | Task 3 | Threat level + justification |
| 5 | Draft Alert | Alert Drafter | Sequential | Task 4 | Alert bulletin (≤150 words) |
| 6 | Generate SitRep | SitRep Generator | Sequential | Tasks 3, 4, 5 | Final Markdown report file |

### Workflow Execution Process

```
START
  ↓
[Task 1: Anecdotal Scout] ←──┐
         ↓                     ├─── Execute in Parallel
[Task 2: Official Scout]  ←──┘
         ↓
[Task 3: Data Validator]
         ↓
[Task 4: Epidemiologist]
         ↓
[Task 5: Alert Drafter]
         ↓
[Task 6: SitRep Generator]
         ↓
      OUTPUT
(SitRep_Disease_Region.md)
```

## 📦 Project Structure

```
public-health-crew/
│
├── main.py                          # Main orchestrator script
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── .env                             # API keys (not in repo)
│
├── agents/                          # Agent definitions
│   ├── __init__.py                  # Package initializer
│   ├── anecdotal_scout.py          # Social media scout agent
│   ├── official_scout.py           # Official sources scout agent
│   ├── data_validator.py           # Data validation agent
│   ├── epidemiologist.py           # Threat assessment agent
│   ├── alert_drafter.py            # Alert bulletin writer agent
│   ├── sitrep_generator.py         # Final report generator agent
│   └── tools.py                     # Shared tools configuration
│
├── tasks/                           # Task definitions
│   ├── __init__.py                  # Package initializer
│   └── task_definitions.py         # All task configurations
│
└── SitRep_Dengue_Fever_Outbreak_Delhi,_India.md  # Example output
```

## 🔧 Requirements

| Package | Purpose |
|---------|---------|
| `crewai` | Multi-agent AI framework |
| `crewai_tools` | Tools for agents (SerperDev, FileWriter) |
| `python-dotenv` | Environment variable management |
| `langchain-openai` | LangChain OpenAI integration |
| `langchain-groq` | LangChain Groq integration |
| `google-search-results` | Google search API wrapper |
| `langchain-google-genai` | Google Gemini AI integration |


**API Key Sources:**
- **Google Gemini API**: [Get API Key](https://ai.google.dev/)
- **Serper Dev API**: [Get API Key](https://serper.dev/)

## 🚀 Usage

### Basic Usage

```bash
python main.py
```

### Customizing Disease and Region

Edit `main.py` to modify the target disease and region:

```python
# Line 54-56 in main.py
disease = "Dengue Fever Outbreak"  # Change disease here
region = "Delhi, India"             # Change region here
```

### Expected Output

The system will:
1. Display verbose agent activity and reasoning
2. Execute all 6 tasks in order
3. Generate a Markdown file: `SitRep_[Disease]_[Region].md`

## 📄 Example Output

The system generates comprehensive Situation Reports in Markdown format. Here's the structure:

### SitRep Format

```markdown
# Situation Report: [Disease] in [Region]

**PUBLIC HEALTH ALERT BULLETIN**
[Date, Subject, Threat Level, Summary, Key Trends]

## Emerging Threat Level: [Level]
[Justification for threat level]

## Summary of Validated Findings
| Source | Location | Key Finding |
|--------|----------|-------------|
| ...    | ...      | ...         |
```

**Real Example**: See `SitRep_Dengue_Fever_Outbreak_Delhi,_India.md` for actual output from the system.

## 🎓 Use Cases

- **Early Outbreak Detection**: Monitor social media for disease signals before official reports
- **Public Health Surveillance**: Automated monitoring of disease trends in specific regions
- **Academic Research**: Study disease outbreak patterns and information propagation
- **Emergency Response**: Rapid situation assessment for health departments
- **Training & Education**: Demonstrate AI applications in public health

## 🔑 Key Technologies

| Technology | Version/Model | Purpose |
|------------|---------------|---------|
| **CrewAI** | Latest | Multi-agent orchestration framework |
| **Google Gemini** | gemini-2.0-flash-lite | Large Language Model for agent intelligence |
| **Serper API** | Latest | Real-time web search capabilities |
| **Python** | 3.8+ | Core programming language |
| **LangChain** | Latest | LLM integration and tooling |

### Process Type
- **Sequential Processing**: Tasks execute in order, with context passing between agents
- **Parallel Execution**: Scout tasks run simultaneously for efficiency

## 🎯 Threat Level Classification

| Level | Criteria | Response |
|-------|----------|----------|
| **Low** | Isolated reports, no corroboration | Monitor situation |
| **Elevated** | Multiple reports, some validation | Increase surveillance |
| **High** | Confirmed cases, severe symptoms, geographic spread | Activate response protocols |
| **Severe** | Widespread outbreak, high mortality, rapid transmission | Emergency response required |

## 📊 System Performance

- **Parallel Tasks**: 2 agents (scouts) run simultaneously
- **Sequential Tasks**: 4 agents run in order
- **Average Runtime**: 2-5 minutes (depends on API response times)
- **Output Format**: Markdown (.md), PDF available

## 👨‍💻 Author

**Anirudh Dattu**
- GitHub: [@AnirudhDattu](https://github.com/AnirudhDattu)

**Note**: This system is designed for educational and research purposes. It should complement, not replace, official public health surveillance systems.
