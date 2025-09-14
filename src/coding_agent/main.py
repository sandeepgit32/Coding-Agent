#!/usr/bin/env python
import os
import warnings

from coding_agent.crew import Coder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


assignment = input("Enter the assignment: ")
project_dir = input("Enter the project directory (default: MyProject): ") or "MyProject"

# os.makedirs("output", exist_ok=True)
# os.makedirs(f"output/{project_dir}", exist_ok=True)


def run():
    """
    Run the crew.
    """
    inputs = {
        "assignment": assignment,
        "project_dir": project_dir,
    }

    result = Coder().crew().kickoff(inputs=inputs)
    print(result.raw)
