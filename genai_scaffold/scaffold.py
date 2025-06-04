"""
Handles project scaffolding for generative AI applications.
"""

from pathlib import Path
from .template_structure import structure, core_files

def scaffold_project(name: str):
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

    for folder, files in structure.items():
        folder_path = project_root / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        for file in files:
            (folder_path / file).touch()

    for filename, content in core_files.items():
        (project_root / filename).write_text(content)

    print(f"✅ Project created at {project_root.resolve()}")
