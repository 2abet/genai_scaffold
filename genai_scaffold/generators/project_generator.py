"""Project generator implementation."""

from pathlib import Path
from typing import Dict, Any
from jinja2 import Environment, FileSystemLoader, select_autoescape

from ..core.config import ProjectConfig


class ProjectGenerator:
    """Generates a GenAI project based on configuration."""
    
    def __init__(self, config: ProjectConfig):
        """Initialize the project generator.
        
        Args:
            config: Project configuration object
        """
        self.config = config
        self.templates_dir = Path(__file__).parent.parent / "templates"
        self.env = Environment(
            loader=FileSystemLoader(str(self.templates_dir)),
            autoescape=select_autoescape(enabled_extensions=(), default=False),
            trim_blocks=True,
            lstrip_blocks=True
        )
    
    def generate(self, destination: Path) -> None:
        """Generate the project at the destination path.
        
        Args:
            destination: Path where the project will be created
        """
        destination.mkdir(parents=True, exist_ok=True)
        
        # Create context for templates
        context = self._build_context()
        
        # Render base structure
        self._render_base_structure(destination, context)
        
        # Render tech-stack specific files
        self._render_llm_provider(destination, context)
        self._render_orchestrator(destination, context)
        self._render_vector_db(destination, context)
        self._render_ui_framework(destination, context)
        
        # Render additional files
        self._render_dependency_files(destination, context)
        self._render_docker_files(destination, context)
        self._render_observability(destination, context)
    
    def _build_context(self) -> Dict[str, Any]:
        """Build template context from configuration."""
        return {
            "project_name": self.config.project_name,
            "llm_provider": self.config.llm_provider,
            "orchestrator": self.config.orchestrator,
            "vector_db": self.config.vector_db,
            "ui_framework": self.config.ui_framework,
            "dependency_manager": self.config.dependency_manager,
            "enable_observability": self.config.enable_observability,
            "observability_tool": self.config.observability_tool,
            "enable_docker": self.config.enable_docker,
            # Helper booleans for templates
            "use_langchain": self.config.orchestrator == "langchain",
            "use_llamaindex": self.config.orchestrator == "llamaindex",
            "use_dspy": self.config.orchestrator == "dspy",
            "use_openai": self.config.llm_provider == "openai",
            "use_anthropic": self.config.llm_provider == "anthropic",
            "use_azure": self.config.llm_provider == "azure",
            "use_ollama": self.config.llm_provider == "ollama",
            "use_pinecone": self.config.vector_db == "pinecone",
            "use_chromadb": self.config.vector_db == "chromadb",
            "use_qdrant": self.config.vector_db == "qdrant",
            "use_pgvector": self.config.vector_db == "pgvector",
            "use_streamlit": self.config.ui_framework == "streamlit",
            "use_gradio": self.config.ui_framework == "gradio",
            "use_fastapi": self.config.ui_framework == "fastapi",
            "use_poetry": self.config.dependency_manager == "poetry",
            "use_langsmith": self.config.observability_tool == "langsmith",
            "use_wandb": self.config.observability_tool == "wandb",
        }
    
    def _render_template(self, template_name: str, destination: Path, context: Dict[str, Any]) -> None:
        """Render a single template file.
        
        Args:
            template_name: Name of the template file (relative to templates dir)
            destination: Destination file path
            context: Template context dictionary
        """
        template = self.env.get_template(template_name)
        content = template.render(**context)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content)
    
    def _render_base_structure(self, destination: Path, context: Dict[str, Any]) -> None:
        """Render base project structure."""
        # Create directory structure
        dirs = [
            "src",
            "src/llm",
            "src/prompts",
            "src/utils",
            "src/handlers",
            "tests",
            "config",
            "data/cache",
            "data/outputs",
            "data/embeddings",
            "notebooks",
        ]
        
        for dir_path in dirs:
            (destination / dir_path).mkdir(parents=True, exist_ok=True)
        
        # Render common files
        self._render_template("new/README.md.j2", destination / "README.md", context)
        self._render_template("new/.env.example.j2", destination / ".env.example", context)
        self._render_template("new/.gitignore.j2", destination / ".gitignore", context)
        self._render_template("new/Makefile.j2", destination / "Makefile", context)
        
        # Source files
        self._render_template("new/src/__init__.py.j2", destination / "src/__init__.py", context)
        self._render_template("new/src/config.py.j2", destination / "src/config.py", context)
        
        # Prompt management
        self._render_template("new/src/prompts/__init__.py.j2", destination / "src/prompts/__init__.py", context)
        self._render_template("new/src/prompts/loader.py.j2", destination / "src/prompts/loader.py", context)
        self._render_template("new/src/prompts/templates.yaml.j2", destination / "src/prompts/templates.yaml", context)
        
        # Utils
        self._render_template("new/src/utils/__init__.py.j2", destination / "src/utils/__init__.py", context)
        self._render_template("new/src/utils/logger.py.j2", destination / "src/utils/logger.py", context)
        
        # Tests
        self._render_template("new/tests/__init__.py.j2", destination / "tests/__init__.py", context)
        self._render_template("new/tests/conftest.py.j2", destination / "tests/conftest.py", context)
        self._render_template("new/tests/test_example.py.j2", destination / "tests/test_example.py", context)
        self._render_template("new/pytest.ini.j2", destination / "pytest.ini", context)
        
        # Empty gitkeep files
        for keep_dir in ["data/cache", "data/outputs", "data/embeddings", "notebooks"]:
            (destination / keep_dir / ".gitkeep").touch()
    
    def _render_llm_provider(self, destination: Path, context: Dict[str, Any]) -> None:
        """Render LLM provider-specific files."""
        self._render_template("new/src/llm/__init__.py.j2", destination / "src/llm/__init__.py", context)
        self._render_template("new/src/llm/client.py.j2", destination / "src/llm/client.py", context)
    
    def _render_orchestrator(self, destination: Path, context: Dict[str, Any]) -> None:
        """Render orchestrator-specific files."""
        if self.config.orchestrator != "none":
            self._render_template("new/src/rag_pipeline.py.j2", destination / "src/rag_pipeline.py", context)
    
    def _render_vector_db(self, destination: Path, context: Dict[str, Any]) -> None:
        """Render vector database-specific files."""
        self._render_template("new/src/vector_store.py.j2", destination / "src/vector_store.py", context)
    
    def _render_ui_framework(self, destination: Path, context: Dict[str, Any]) -> None:
        """Render UI framework files."""
        if self.config.ui_framework == "streamlit":
            self._render_template("new/app_streamlit.py.j2", destination / "app.py", context)
        elif self.config.ui_framework == "gradio":
            self._render_template("new/app_gradio.py.j2", destination / "app.py", context)
        elif self.config.ui_framework == "fastapi":
            self._render_template("new/app_fastapi.py.j2", destination / "app.py", context)
    
    def _render_dependency_files(self, destination: Path, context: Dict[str, Any]) -> None:
        """Render dependency management files."""
        if self.config.dependency_manager == "poetry":
            self._render_template("new/pyproject.toml.j2", destination / "pyproject.toml", context)
        else:  # pip
            self._render_template("new/requirements.txt.j2", destination / "requirements.txt", context)
            self._render_template("new/requirements-dev.txt.j2", destination / "requirements-dev.txt", context)
    
    def _render_docker_files(self, destination: Path, context: Dict[str, Any]) -> None:
        """Render Docker-related files."""
        if self.config.enable_docker:
            self._render_template("new/Dockerfile.j2", destination / "Dockerfile", context)
            self._render_template("new/docker-compose.yml.j2", destination / "docker-compose.yml", context)
    
    def _render_observability(self, destination: Path, context: Dict[str, Any]) -> None:
        """Render observability-related files."""
        if self.config.enable_observability:
            self._render_template("new/src/observability.py.j2", destination / "src/observability.py", context)
