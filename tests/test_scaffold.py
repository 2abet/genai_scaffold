import subprocess
import sys
from pathlib import Path

def test_module_execution_creates_project(tmp_path):
    project_path = tmp_path / 'proj'
    result = subprocess.run(
        [sys.executable, '-m', 'genai_scaffold', 'create', str(project_path), 
         '--provider', 'anthropic', '--orchestrator', 'langchain', 
         '--vector-db', 'chromadb', '--ui', 'streamlit'],
        capture_output=True, text=True
    )
    assert result.returncode == 0, f"Command failed: {result.stderr}"
    
    # Check that the project was created
    assert project_path.exists(), "Project directory was not created"
    
    readme = (project_path / 'README.md')
    assert readme.exists(), "README.md not found"
    readme_content = readme.read_text()
    assert 'anthropic' in readme_content.lower(), "Provider not found in README"
    
    # Check key files exist
    assert (project_path / '.env.example').exists(), ".env.example not found"
    assert (project_path / 'Makefile').exists(), "Makefile not found"
    assert (project_path / 'requirements.txt').exists(), "requirements.txt not found"
    assert (project_path / 'docker-compose.yml').exists(), "docker-compose.yml not found"
    
    # Check source structure
    src_dir = project_path / 'src'
    assert src_dir.exists(), "src directory not found"
    assert (src_dir / 'llm' / 'client.py').exists(), "LLM client not found"
    assert (src_dir / 'prompts' / 'loader.py').exists(), "Prompt loader not found"
    assert (src_dir / 'vector_store.py').exists(), "Vector store not found"
    assert (src_dir / 'rag_pipeline.py').exists(), "RAG pipeline not found"
    
    # Check tests exist
    tests_dir = project_path / 'tests'
    assert tests_dir.exists(), "tests directory not found"
    assert (tests_dir / 'test_example.py').exists(), "test_example.py not found"
    assert (tests_dir / 'conftest.py').exists(), "conftest.py not found"

# test_scaffold.py - part of genai_scaffold
