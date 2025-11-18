"""Tests for the core configuration module."""

import pytest
from genai_scaffold.core.config import ProjectConfig


def test_project_config_creation():
    """Test creating a valid project configuration."""
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
    
    assert config.project_name == "test-app"
    assert config.llm_provider == "openai"
    assert config.orchestrator == "langchain"
    assert config.vector_db == "chromadb"
    assert config.ui_framework == "streamlit"


def test_project_config_invalid_llm_provider():
    """Test that invalid LLM provider raises ValueError."""
    with pytest.raises(ValueError, match="Invalid LLM provider"):
        ProjectConfig(
            project_name="test-app",
            llm_provider="invalid",
            orchestrator="langchain",
            vector_db="chromadb",
            ui_framework="streamlit",
        )


def test_project_config_invalid_orchestrator():
    """Test that invalid orchestrator raises ValueError."""
    with pytest.raises(ValueError, match="Invalid orchestrator"):
        ProjectConfig(
            project_name="test-app",
            llm_provider="openai",
            orchestrator="invalid",
            vector_db="chromadb",
            ui_framework="streamlit",
        )


def test_project_config_invalid_vector_db():
    """Test that invalid vector DB raises ValueError."""
    with pytest.raises(ValueError, match="Invalid vector DB"):
        ProjectConfig(
            project_name="test-app",
            llm_provider="openai",
            orchestrator="langchain",
            vector_db="invalid",
            ui_framework="streamlit",
        )


def test_project_config_with_observability():
    """Test configuration with observability enabled."""
    config = ProjectConfig(
        project_name="test-app",
        llm_provider="openai",
        orchestrator="langchain",
        vector_db="chromadb",
        ui_framework="streamlit",
        enable_observability=True,
        observability_tool="langsmith",
    )
    
    assert config.enable_observability is True
    assert config.observability_tool == "langsmith"


def test_project_config_all_providers():
    """Test all valid LLM providers."""
    providers = ["openai", "anthropic", "azure", "ollama"]
    
    for provider in providers:
        config = ProjectConfig(
            project_name="test-app",
            llm_provider=provider,
            orchestrator="langchain",
            vector_db="chromadb",
            ui_framework="streamlit",
        )
        assert config.llm_provider == provider


def test_project_config_all_orchestrators():
    """Test all valid orchestrators."""
    orchestrators = ["langchain", "llamaindex", "dspy", "none"]
    
    for orch in orchestrators:
        config = ProjectConfig(
            project_name="test-app",
            llm_provider="openai",
            orchestrator=orch,
            vector_db="chromadb",
            ui_framework="streamlit",
        )
        assert config.orchestrator == orch


def test_project_config_all_vector_dbs():
    """Test all valid vector databases."""
    vector_dbs = ["pinecone", "chromadb", "qdrant", "pgvector"]
    
    for vdb in vector_dbs:
        config = ProjectConfig(
            project_name="test-app",
            llm_provider="openai",
            orchestrator="langchain",
            vector_db=vdb,
            ui_framework="streamlit",
        )
        assert config.vector_db == vdb


def test_project_config_all_ui_frameworks():
    """Test all valid UI frameworks."""
    ui_frameworks = ["streamlit", "gradio", "fastapi", "none"]
    
    for ui in ui_frameworks:
        config = ProjectConfig(
            project_name="test-app",
            llm_provider="openai",
            orchestrator="langchain",
            vector_db="chromadb",
            ui_framework=ui,
        )
        assert config.ui_framework == ui
