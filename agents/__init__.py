# This file makes the 'agents' folder a Python package.
# We import the agent-creation FUNCTIONS here so they can be easily accessed

from .anecdotal_scout import create_anecdotal_scout_agent
from .official_scout import create_official_scout_agent
from .data_validator import create_data_validator_agent
from .epidemiologist import create_epidemiologist_agent
from .alert_drafter import create_alert_drafter_agent
from .sitrep_generator import create_sitrep_generator_agent