"""Tests for the ProjectGenerator class."""

import pytest
from pathlib import Path
from genai_scaffold.core.config import ProjectConfig
from genai_scaffold.generators.project_generator import ProjectGenerator


def test_project_generator_basic(tmp_path):
    """Test basic project generation."""
    config = ProjectConfig(
        project_name="test-app",
        llm_provider="openai",
        orchestrator="langchain",
        vector_db="chromadb",
        ui_framework="streamlit",
        dependency_manager="pip",
        enable_docker=True,
        enable_observability=False,
    )
    
    generator = ProjectGenerator(config)
    destination = tmp_path / "test-app"
    
    generator.generate(destination)
    
    # Check that the directory was created
    assert destination.exists()
    
    # Check key files
    assert (destination / "README.md").exists()
    assert (destination / ".env.example").exists()
    assert (destination / "Makefile").exists()
    assert (destination / "requirements.txt").exists()
    assert (destination / "docker-compose.yml").exists()
    
    # Check source structure
    assert (destination / "src" / "__init__.py").exists()
    assert (destination / "src" / "config.py").exists()
    assert (destination / "src" / "llm" / "client.py").exists()
    assert (destination / "src" / "prompts" / "loader.py").exists()
    assert (destination / "src" / "vector_store.py").exists()
    
    # Check tests
    assert (destination / "tests" / "test_example.py").exists()


def test_project_generator_with_poetry(tmp_path):
    """Test project generation with Poetry."""
    config = ProjectConfig(
        project_name="test-app",
        llm_provider="openai",
        orchestrator="langchain",
        vector_db="chromadb",
        ui_framework="streamlit",
        dependency_manager="poetry",
        enable_docker=False,
        enable_observability=False,
    )
    
    generator = ProjectGenerator(config)
    destination = tmp_path / "test-app"
    
    generator.generate(destination)
    
    # Should have pyproject.toml instead of requirements.txt
    assert (destination / "pyproject.toml").exists()
    assert not (destination / "requirements.txt").exists()


def test_project_generator_without_docker(tmp_path):
    """Test project generation without Docker."""
    config = ProjectConfig(
        project_name="test-app",
        llm_provider="openai",
        orchestrator="langchain",
        vector_db="chromadb",
        ui_framework="streamlit",
        enable_docker=False,
        enable_observability=False,
    )
    
    generator = ProjectGenerator(config)
    destination = tmp_path / "test-app"
    
    generator.generate(destination)
    
    # Should not have Docker files
    assert not (destination / "Dockerfile").exists()
    assert not (destination / "docker-compose.yml").exists()


def test_project_generator_with_observability(tmp_path):
    """Test project generation with observability."""
    config = ProjectConfig(
        project_name="test-app",
        llm_provider="openai",
        orchestrator="langchain",
        vector_db="chromadb",
        ui_framework="streamlit",
        enable_observability=True,
        observability_tool="langsmith",
    )
    
    generator = ProjectGenerator(config)
    destination = tmp_path / "test-app"
    
    generator.generate(destination)
    
    # Should have observability file
    assert (destination / "src" / "observability.py").exists()


def test_project_generator_fastapi(tmp_path):
    """Test project generation with FastAPI."""
    config = ProjectConfig(
        project_name="test-app",
        llm_provider="openai",
        orchestrator="langchain",
        vector_db="chromadb",
        ui_framework="fastapi",
    )
    
    generator = ProjectGenerator(config)
    destination = tmp_path / "test-app"
    
    generator.generate(destination)
    
    # Should have app.py for FastAPI
    assert (destination / "app.py").exists()
    
    # Check that app.py contains FastAPI code
    content = (destination / "app.py").read_text()
    assert "FastAPI" in content


def test_project_generator_context_building(tmp_path):
    """Test that the context is built correctly."""
    config = ProjectConfig(
        project_name="test-app",
        llm_provider="openai",
        orchestrator="langchain",
        vector_db="chromadb",
        ui_framework="streamlit",
    )
    
    generator = ProjectGenerator(config)
    context = generator._build_context()
    
    # Check basic fields
    assert context["project_name"] == "test-app"
    assert context["llm_provider"] == "openai"
    assert context["orchestrator"] == "langchain"
    assert context["vector_db"] == "chromadb"
    
    # Check helper booleans
    assert context["use_openai"] is True
    assert context["use_langchain"] is True
    assert context["use_chromadb"] is True
    assert context["use_streamlit"] is True
    assert context["use_anthropic"] is False


def test_project_generator_readme_content(tmp_path):
    """Test that README contains correct information."""
    config = ProjectConfig(
        project_name="my-rag-app",
        llm_provider="anthropic",
        orchestrator="llamaindex",
        vector_db="pinecone",
        ui_framework="gradio",
    )
    
    generator = ProjectGenerator(config)
    destination = tmp_path / "my-rag-app"
    
    generator.generate(destination)
    
    readme_content = (destination / "README.md").read_text()
    
    # Check that all the config is mentioned
    assert "my-rag-app" in readme_content
    assert "anthropic" in readme_content
    assert "llamaindex" in readme_content
    assert "pinecone" in readme_content
    assert "gradio" in readme_content
