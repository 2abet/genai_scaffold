import subprocess
import sys
from pathlib import Path

def test_module_execution_creates_project(tmp_path):
    project_path = tmp_path / 'proj'
    result = subprocess.run(
        [sys.executable, '-m', 'genai_scaffold', str(project_path), '--provider', 'claude'],
        capture_output=True, text=True
    )
    assert result.returncode == 0
    readme = (project_path / 'README.md')
    assert readme.exists()
    assert 'claude' in readme.read_text()

    # starter code checks
    cache_py = project_path / 'src' / 'utils' / 'cache.py'
    assert 'class Cache' in cache_py.read_text()

    base_llm_py = project_path / 'src' / 'llm' / 'base.py'
    assert 'class BaseLLMClient' in base_llm_py.read_text()

    handler_py = project_path / 'src' / 'handlers' / 'error_handler.py'
    assert 'class ErrorHandler' in handler_py.read_text()

# test_scaffold.py - part of genai_scaffold
