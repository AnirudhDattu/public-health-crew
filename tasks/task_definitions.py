#tasks/task_definitions.py

from crewai import Task
from textwrap import dedent

# This class will hold all the task definitions
class PublicHealthTasks():

    def find_anecdotal_reports_task(self, agent, disease, region):
        """
        Task for the Anecdotal Scout Agent.
        This is a parallel task.
        """
        return Task(
            description=dedent(f"""
                Search social media (Reddit, X/Twitter) and forums for 
                anecdotal reports of '{disease}' in '{region}'. 
                Focus on keywords like 'sick', 'outbreak', 'symptoms', 
                and any specific local chatter.
            """),
            expected_output=dedent("""
                A bullet-point list of 5-10 relevant anecdotal findings, 
                each with a source (URL) and a brief quote or summary.
            """),
            agent=agent,
            async_execution=True  # This makes it run in parallel
        )

    def find_official_reports_task(self, agent, disease, region):
        """
        Task for the Official Scout Agent.
        This is also a parallel task.
        """
        return Task(
            description=dedent(f"""
                Search official public health websites (like CDC, local 
                health depts) and reputable news outlets for formal 
                reports on '{disease}' in '{region}'.
            """),
            expected_output=dedent("""
                A bullet-point list of 3-5 official reports or data points, 
                each with a source (URL) and a key summary.
            """),
            agent=agent,
            async_execution=True  # This also runs in parallel
        )

    def validate_data_task(self, agent, context):
        """
        Task for the Validator Agent.
        This task depends on the two scout tasks.
        """
        return Task(
            description=dedent("""
                Analyze the reports from both the Anecdotal Scout and the 
                Official Scout. Cross-reference the findings to identify 
                corroboration. For example, if an anecdotal report mentions 
                school closures, see if a official news source confirms it.
            """),
            expected_output=dedent("""
                A list of 'Validated Findings' where anecdotal reports 
                are supported by official data, or where official data 
                provides context to anecdotal chatter. Filter out and 
                discard any purely speculative rumors.
            """),
            agent=agent,
            context=context  # This tells the task to use the output 
                             # from the scout tasks
        )

    def assess_threat_level_task(self, agent, context):
        """
        Task for the Epidemiologist Agent.
        This task depends on the validation task.
        """
        return Task(
            description=dedent("""
                Analyze the 'Validated Findings' to assess the public 
                health situation. Consider the severity of symptoms 
                reported, the number of reports, and the geographic 
                spread. Assign an 'Emerging Threat Level' using one of 
                these four levels: Low, Elevated, High, Severe.
            """),
            expected_output=dedent("""
                A final 'Emerging Threat Level' (e.g., 'High') and a 
                2-3 sentence justification for this assessment.
            """),
            agent=agent,
            context=context  # This uses the output from the validator task
        )

    def draft_alert_task(self, agent, context):
        """
        Task for the Alert Drafter Agent.
        This task depends on the epidemiologist's assessment.
        """
        return Task(
            description=dedent("""
                Draft a concise, formal alert bulletin (max 150 words) 
                based on the Epidemiologist's assessment. The bulletin 
                must include the 'Emerging Threat Level' and a brief 
                summary of the key trends.
            """),
            expected_output=dedent("""
                A single, professionally written alert bulletin.
            """),
            agent=agent,
            context=context  # This uses the output from the assessment task
        )

    def generate_sitrep_task(self, agent, context, disease, region):
        """
        Task for the SitRep Generator Agent.
        This is the final task, compiling everything.
        """
        return Task(
            description=dedent(f"""
                Compile all the information into a final Situation Report 
                (SitRep) for '{disease}' in '{region}'. The report must 
                be a single Markdown file. It must include:
                1. A Title: "Situation Report: [Disease] in [Region]"
                2. The 'Alert Bulletin' at the top.
                3. The 'Emerging Threat Level' and its justification.
                4. A section titled 'Summary of Validated Findings' 
                   presented as a Markdown table.

                The filename must be: 'SitRep_{disease.replace(' ', '_')}_{region.replace(' ', '_')}.md'
            """),
            expected_output=dedent(f"""
                The final, complete Markdown report saved to a file named 
                'SitRep_{disease.replace(' ', '_')}_{region.replace(' ', '_')}.md'.
            """),
            agent=agent,
            context=context  # This uses the output from all previous tasks
        )