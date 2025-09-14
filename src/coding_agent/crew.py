from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class Coder:
    """Coder crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def coder(self) -> Agent:
        return Agent(
            config=self.agents_config["coder"],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_execution_time=120,
            max_retry_limit=3,
        )

    @agent
    def tester(self) -> Agent:
        return Agent(
            config=self.agents_config["tester"],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_execution_time=120,
            max_retry_limit=3,
        )

    @agent
    def documenter(self) -> Agent:
        return Agent(
            config=self.agents_config["documenter"],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_execution_time=120,
            max_retry_limit=3,
        )

    @task
    def development_task(self) -> Task:
        return Task(
            config=self.tasks_config["development_task"],
        )

    @task
    def testing_and_review_task(self) -> Task:
        return Task(
            config=self.tasks_config["testing_and_review_task"],
        )

    @task
    def documentation_and_deps_task(self) -> Task:
        return Task(
            config=self.tasks_config["documentation_and_deps_task"],
        )
    
    @task
    def finalization_task(self) -> Task:
        return Task(
            config=self.tasks_config["finalization_task"],
        )

    @task
    def execution_validation_task(self) -> Task:
        return Task(
            config=self.tasks_config["execution_validation_task"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Coder crew with sequential process for reliable task execution"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # More reliable for initial setup
            verbose=True,
        )
