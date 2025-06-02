"""
Entry point for the genai_scaffold CLI.
"""

import sys
from .scaffold import scaffold_project

def main():
    if len(sys.argv) != 2:
        print("Usage: genai-scaffold <project_name>")
        sys.exit(1)
    scaffold_project(sys.argv[1])
