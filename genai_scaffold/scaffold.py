"""
Handles project scaffolding for generative AI applications.
"""

from pathlib import Path
from .template_engine import render_templates

def scaffold_project(name: str, llm_provider: str = "gpt"):
    """
    Creates a structured generative AI project in the given directory.

    Args:
        name (str): The name of the project directory to create.

    This function will create the project directory along with any missing
    parent directories.
    """
    project_root = Path(name)
    # Create the project directory along with any required parent directories
    project_root.mkdir(parents=True, exist_ok=True)

    render_templates(project_root, project_name=name, llm_provider=llm_provider)

    print(f"✅ Project created at {project_root.resolve()}")
