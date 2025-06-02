"""
Template folder structure and core files for project generation.
"""

structure = {
    "config": ["__init__.py", "model_config.yaml", "prompt_templates.yaml", "logging_config.yaml"],
    "src/llm": ["__init__.py", "base.py", "claude_client.py", "gpt_client.py", "utils.py"],
    "src/prompt_engineering": ["__init__.py", "templates.py", "few_shot.py", "chainer.py"],
    "src/utils": ["__init__.py", "rate_limiter.py", "token_counter.py", "cache.py", "logger.py"],
    "src/handlers": ["__init__.py", "error_handler.py"],
    "data/cache": [],
    "data/prompts": [],
    "data/outputs": [],
    "data/embeddings": [],
    "examples": ["basic_completion.py", "chat_session.py"],
    "notebooks": ["prompt_testing.ipynb", "response_analysis.ipynb", "model_experimentation.ipynb"],
}

core_files = {
    "requirements.txt": "# Add your Python dependencies here\n",
    "setup.py": "# Optional setup.py file\n",
    "README.md": "# Project README\n",
    "Dockerfile": "# Dockerfile\nFROM python:3.10-slim\n"
}
