"""
Entry point for the genai_scaffold CLI.
"""

import sys
from .scaffold import scaffold_project

def main():
    if len(sys.argv) < 2:
        print("Usage: genai-scaffold <project_name> [--provider <llm_provider>]")
        sys.exit(1)
    name = sys.argv[1]
    provider = "gpt"
    if "--provider" in sys.argv:
        idx = sys.argv.index("--provider")
        if idx + 1 < len(sys.argv):
            provider = sys.argv[idx + 1]
    scaffold_project(name, llm_provider=provider)


if __name__ == "__main__":
    main()
