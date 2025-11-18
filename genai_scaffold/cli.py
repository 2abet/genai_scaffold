"""Interactive CLI for genai_scaffold using Typer and InquirerPy."""

from pathlib import Path
from typing import Optional
import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from InquirerPy import prompt
from InquirerPy.base.control import Choice

from .core.config import ProjectConfig
from .generators.project_generator import ProjectGenerator

app = typer.Typer(
    name="genai-scaffold",
    help="Interactive CLI tool to scaffold production-ready Generative AI projects",
    add_completion=False
)
console = Console()


def interactive_config() -> ProjectConfig:
    """Prompt user for project configuration interactively."""
    console.print("\n[bold cyan]🚀 GenAI Project Scaffold - Interactive Setup[/bold cyan]\n")
    
    questions = [
        {
            "type": "input",
            "name": "project_name",
            "message": "Project name:",
            "default": "my-genai-app",
            "validate": lambda x: len(x) > 0 or "Project name cannot be empty",
        },
        {
            "type": "list",
            "name": "llm_provider",
            "message": "Select LLM Provider:",
            "choices": [
                Choice(value="openai", name="OpenAI (GPT-4, GPT-3.5)"),
                Choice(value="anthropic", name="Anthropic (Claude)"),
                Choice(value="azure", name="Azure OpenAI"),
                Choice(value="ollama", name="Ollama (Local)"),
                Choice(value="local", name="Local (OpenAI-compatible endpoint)"),
            ],
            "default": "openai",
        },
        {
            "type": "list",
            "name": "orchestrator",
            "message": "Select Orchestration Framework:",
            "choices": [
                Choice(value="langchain", name="LangChain"),
                Choice(value="llamaindex", name="LlamaIndex"),
                Choice(value="dspy", name="DSPy"),
                Choice(value="none", name="None (Raw Python)"),
            ],
            "default": "langchain",
        },
        {
            "type": "list",
            "name": "vector_db",
            "message": "Select Vector Database:",
            "choices": [
                Choice(value="chromadb", name="ChromaDB (Local)"),
                Choice(value="pinecone", name="Pinecone (Cloud)"),
                Choice(value="qdrant", name="Qdrant"),
                Choice(value="pgvector", name="PostgreSQL + pgvector"),
            ],
            "default": "chromadb",
        },
        {
            "type": "list",
            "name": "ui_framework",
            "message": "Select UI Framework:",
            "choices": [
                Choice(value="streamlit", name="Streamlit"),
                Choice(value="gradio", name="Gradio"),
                Choice(value="fastapi", name="FastAPI (API only)"),
                Choice(value="none", name="None"),
            ],
            "default": "streamlit",
        },
        {
            "type": "list",
            "name": "dependency_manager",
            "message": "Select Dependency Manager:",
            "choices": [
                Choice(value="pip", name="pip (requirements.txt)"),
                Choice(value="poetry", name="Poetry (pyproject.toml)"),
            ],
            "default": "pip",
        },
        {
            "type": "confirm",
            "name": "enable_docker",
            "message": "Include Docker configuration?",
            "default": True,
        },
        {
            "type": "confirm",
            "name": "enable_observability",
            "message": "Enable observability/tracing?",
            "default": False,
        },
    ]
    
    answers = prompt(questions)
    
    # If observability is enabled, ask which tool
    observability_tool = None
    if answers["enable_observability"]:
        obs_question = [
            {
                "type": "list",
                "name": "observability_tool",
                "message": "Select Observability Tool:",
                "choices": [
                    Choice(value="langsmith", name="LangSmith"),
                    Choice(value="wandb", name="Weights & Biases"),
                ],
                "default": "langsmith",
            }
        ]
        obs_answer = prompt(obs_question)
        observability_tool = obs_answer["observability_tool"]
    
    return ProjectConfig(
        project_name=answers["project_name"],
        llm_provider=answers["llm_provider"],
        orchestrator=answers["orchestrator"],
        vector_db=answers["vector_db"],
        ui_framework=answers["ui_framework"],
        dependency_manager=answers["dependency_manager"],
        enable_docker=answers["enable_docker"],
        enable_observability=answers["enable_observability"],
        observability_tool=observability_tool,
    )


@app.command()
def create(
    project_name: Optional[str] = typer.Argument(
        None,
        help="Name of the project to create (if not provided, interactive mode is used)"
    ),
    llm_provider: Optional[str] = typer.Option(
        None,
        "--provider",
        help="LLM Provider (openai, anthropic, azure, ollama, local)"
    ),
    orchestrator: Optional[str] = typer.Option(
        None,
        "--orchestrator",
        help="Orchestration framework (langchain, llamaindex, dspy, none)"
    ),
    vector_db: Optional[str] = typer.Option(
        None,
        "--vector-db",
        help="Vector database (pinecone, chromadb, qdrant, pgvector)"
    ),
    ui_framework: Optional[str] = typer.Option(
        None,
        "--ui",
        help="UI framework (streamlit, gradio, fastapi, none)"
    ),
    dependency_manager: str = typer.Option(
        "pip",
        "--deps",
        help="Dependency manager (pip, poetry)"
    ),
    enable_docker: bool = typer.Option(
        True,
        "--docker/--no-docker",
        help="Include Docker configuration"
    ),
    interactive: bool = typer.Option(
        False,
        "--interactive",
        "-i",
        help="Use interactive mode"
    ),
):
    """Create a new GenAI project with customizable tech stack.
    
    Examples:
    
        # Interactive mode (recommended)
        genai-scaffold create --interactive
        
        # Quick start with defaults
        genai-scaffold create my-rag-app
        
        # Specify all options
        genai-scaffold create my-app --provider openai --orchestrator langchain --vector-db chromadb --ui streamlit
    """
    # Determine if we should use interactive mode
    use_interactive = interactive or (
        project_name is None or 
        llm_provider is None or 
        orchestrator is None or 
        vector_db is None or 
        ui_framework is None
    )
    
    if use_interactive:
        config = interactive_config()
    else:
        # Use provided arguments
        config = ProjectConfig(
            project_name=project_name,
            llm_provider=llm_provider,
            orchestrator=orchestrator,
            vector_db=vector_db,
            ui_framework=ui_framework,
            dependency_manager=dependency_manager,
            enable_docker=enable_docker,
            enable_observability=False,
            observability_tool=None,
        )
    
    # Display configuration
    console.print("\n[bold green]📋 Project Configuration:[/bold green]")
    config_panel = Panel(
        f"""[cyan]Project Name:[/cyan] {config.project_name}
[cyan]LLM Provider:[/cyan] {config.llm_provider}
[cyan]Orchestrator:[/cyan] {config.orchestrator}
[cyan]Vector DB:[/cyan] {config.vector_db}
[cyan]UI Framework:[/cyan] {config.ui_framework}
[cyan]Dependency Manager:[/cyan] {config.dependency_manager}
[cyan]Docker:[/cyan] {'Yes' if config.enable_docker else 'No'}
[cyan]Observability:[/cyan] {config.observability_tool if config.enable_observability else 'No'}""",
        title="Configuration",
        border_style="green"
    )
    console.print(config_panel)
    
    # Generate project
    destination = Path(config.project_name)
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Generating project...", total=None)
        
        try:
            generator = ProjectGenerator(config)
            generator.generate(destination)
            progress.update(task, completed=True)
        except Exception as e:
            console.print(f"\n[bold red]❌ Error generating project:[/bold red] {e}")
            raise typer.Exit(1)
    
    # Success message
    console.print(f"\n[bold green]✅ Project created successfully at:[/bold green] {destination.resolve()}")
    
    # Next steps
    next_steps = f"""
[bold cyan]Next steps:[/bold cyan]

1. Navigate to your project:
   [yellow]cd {config.project_name}[/yellow]

2. Set up environment variables:
   [yellow]cp .env.example .env[/yellow]
   [dim]Then edit .env with your API keys[/dim]

3. Install dependencies:"""
    
    if config.dependency_manager == "poetry":
        next_steps += """
   [yellow]poetry install[/yellow]"""
    else:
        next_steps += """
   [yellow]make setup[/yellow]
   [dim]or: pip install -r requirements.txt[/dim]"""
    
    if config.enable_docker:
        next_steps += """

4. Start services with Docker:
   [yellow]docker-compose up -d[/yellow]"""
    
    if config.ui_framework in ["streamlit", "gradio"]:
        next_steps += """

5. Run the application:
   [yellow]make run[/yellow]"""
    elif config.ui_framework == "fastapi":
        next_steps += """

5. Run the API server:
   [yellow]make run[/yellow]"""
    
    next_steps += """

6. Run tests:
   [yellow]make test[/yellow]
"""
    
    console.print(Panel(next_steps, title="Getting Started", border_style="cyan"))


@app.command()
def version():
    """Show version information."""
    console.print("[bold cyan]genai-scaffold[/bold cyan] version [green]0.2.0[/green]")


def main():
    """Main entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
