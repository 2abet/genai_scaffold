"""Configuration models for project generation."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class ProjectConfig:
    """Configuration for a GenAI project."""
    
    project_name: str
    llm_provider: str  # openai, anthropic, azure, ollama, local
    orchestrator: str  # langchain, llamaindex, dspy, none
    vector_db: str  # pinecone, chromadb, qdrant, pgvector
    ui_framework: str  # streamlit, gradio, fastapi, none
    dependency_manager: str = "pip"  # poetry, pip
    enable_observability: bool = False
    observability_tool: Optional[str] = None  # langsmith, wandb
    enable_docker: bool = True
    
    def __post_init__(self):
        """Validate configuration."""
        valid_llm_providers = ["openai", "anthropic", "azure", "ollama", "local"]
        valid_orchestrators = ["langchain", "llamaindex", "dspy", "none"]
        valid_vector_dbs = ["pinecone", "chromadb", "qdrant", "pgvector"]
        valid_ui_frameworks = ["streamlit", "gradio", "fastapi", "none"]
        valid_dependency_managers = ["poetry", "pip"]
        valid_observability_tools = ["langsmith", "wandb", None]
        
        if self.llm_provider not in valid_llm_providers:
            raise ValueError(f"Invalid LLM provider: {self.llm_provider}")
        if self.orchestrator not in valid_orchestrators:
            raise ValueError(f"Invalid orchestrator: {self.orchestrator}")
        if self.vector_db not in valid_vector_dbs:
            raise ValueError(f"Invalid vector DB: {self.vector_db}")
        if self.ui_framework not in valid_ui_frameworks:
            raise ValueError(f"Invalid UI framework: {self.ui_framework}")
        if self.dependency_manager not in valid_dependency_managers:
            raise ValueError(f"Invalid dependency manager: {self.dependency_manager}")
        if self.observability_tool not in valid_observability_tools:
            raise ValueError(f"Invalid observability tool: {self.observability_tool}")
