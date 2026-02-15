import sys
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class JobHunterCrew:
    """JobHunter crew"""

    # Agent definitions
    @agent
    def job_search_agent(self) -> Agent:
        return Agent(config=self.agents_config['job_search_agent'], verbose=True)

    @agent
    def job_matching_agent(self) -> Agent:
        return Agent(config=self.agents_config['job_matching_agent'], verbose=True)

    @agent
    def resume_optimization_agent(self) -> Agent:
        return Agent(config=self.agents_config['resume_optimization_agent'], verbose=True)

    @agent
    def company_research_agent(self) -> Agent:
        return Agent(config=self.agents_config['company_research_agent'], verbose=True)

    @agent
    def interview_prep_agent(self) -> Agent:
        return Agent(config=self.agents_config['interview_prep_agent'], verbose=True)

    # Task definitions
    @task
    def job_extraction_task(self) -> Task:
        return Task(config=self.tasks_config['job_extraction_task'])

    @task
    def job_matching_task(self) -> Task:
        return Task(config=self.tasks_config['job_matching_task'])

    @task
    def job_selection_task(self) -> Task:
        return Task(config=self.tasks_config['job_selection_task'])

    @task
    def resume_rewriting_task(self) -> Task:
        return Task(config=self.tasks_config['resume_rewriting_task'])

    @task
    def company_research_task(self) -> Task:
        return Task(config=self.tasks_config['company_research_task'])

    @task
    def interview_prep_task(self) -> Task:
        return Task(config=self.tasks_config['interview_prep_task'])

    @crew
    def crew(self) -> Crew:
        """Creates the JobHunter crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

def main():
    # Replace with your inputs, ensuring they match what your tasks expect
    inputs = {
        'position': 'Senior Software Engineer',
        'level': 'Senior',
        'location': 'San Francisco, CA'
    }
    
    try:
        JobHunterCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        print(f"An error occurred while running the crew: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()