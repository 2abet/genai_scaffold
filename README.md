# genai-scaffold

**genai-scaffold** is an interactive Python CLI tool that bootstraps production-ready Generative AI project structures with customizable tech stacks, best practices, and modular organization.

![PyPI](https://img.shields.io/pypi/v/genai-scaffold)
![License](https://img.shields.io/pypi/l/genai-scaffold)

---

## ✨ Features

- 🎯 **Interactive CLI**: Choose your tech stack interactively with a beautiful terminal UI
- 🧠 **Multiple LLM Providers**: OpenAI, Anthropic (Claude), Azure OpenAI, or Ollama (local)
- 🔧 **Orchestration Frameworks**: LangChain, LlamaIndex, DSPy, or raw Python
- 💾 **Vector Databases**: Pinecone, ChromaDB, Qdrant, or PostgreSQL with pgvector
- 🎨 **UI Frameworks**: Streamlit, Gradio, FastAPI, or headless
- 📦 **Dependency Management**: Poetry or pip (requirements.txt)
- 🐳 **Docker Support**: Automatic docker-compose configuration for local services
- 📊 **Observability**: Optional LangSmith or Weights & Biases integration
- 🧪 **Testing**: Pre-configured pytest setup with example tests
- 📝 **Prompt Management**: YAML-based prompt templates with versioning
- 🚀 **Production-Ready**: Makefile, .env management, logging, and best practices

---

## 📦 Installation

You can install it via [PyPI](https://pypi.org/project/genai-scaffold):

```bash
pip install genai-scaffold
```

Or using `pipx`:

```bash
pipx install genai-scaffold
```

---

## 🚀 Usage

### Interactive Mode (Recommended)

Simply run the create command with the `--interactive` flag or without any arguments:

```bash
genai-scaffold create --interactive
```

Or just:

```bash
genai-scaffold create
```

This will launch an interactive wizard that guides you through selecting:
- Project name
- LLM provider (OpenAI, Anthropic, Azure, Ollama)
- Orchestration framework (LangChain, LlamaIndex, DSPy, None)
- Vector database (ChromaDB, Pinecone, Qdrant, pgvector)
- UI framework (Streamlit, Gradio, FastAPI, None)
- Dependency manager (pip or Poetry)
- Docker configuration
- Observability tools

### Command-Line Mode

For automation or quick scaffolding, specify all options via flags:

```bash
genai-scaffold create my-rag-app \
  --provider openai \
  --orchestrator langchain \
  --vector-db chromadb \
  --ui streamlit \
  --deps pip
```

### Example: Create a RAG App with LangChain and Streamlit

```bash
genai-scaffold create my-chatbot \
  --provider anthropic \
  --orchestrator langchain \
  --vector-db pinecone \
  --ui streamlit
```

### Example: Create a DSPy App with Local Models

```bash
genai-scaffold create local-ai-app \
  --provider ollama \
  --orchestrator dspy \
  --vector-db chromadb \
  --ui gradio \
  --no-docker
```

### Generated Project Structure

```
my-rag-app/
├── src/
│   ├── llm/              # LLM client implementation
│   │   ├── __init__.py
│   │   └── client.py
│   ├── prompts/          # Prompt templates and management
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   └── templates.yaml
│   ├── utils/            # Utility functions (logging, etc.)
│   ├── config.py         # Configuration management
│   ├── vector_store.py   # Vector database interface
│   └── rag_pipeline.py   # RAG implementation (if orchestrator selected)
├── tests/                # Pytest test suite
│   ├── conftest.py
│   └── test_example.py
├── data/                 # Data directories
│   ├── cache/
│   ├── outputs/
│   └── embeddings/
├── notebooks/            # Jupyter notebooks (optional)
├── app.py                # UI application (Streamlit/Gradio/FastAPI)
├── docker-compose.yml    # Docker services (if enabled)
├── Dockerfile            # Application container
├── .env.example          # Environment variables template
├── Makefile              # Common tasks (setup, test, run, etc.)
├── requirements.txt      # Python dependencies (or pyproject.toml)
├── pytest.ini            # Pytest configuration
└── README.md             # Project documentation
```

---

## 🎯 Quick Start with Generated Project

After scaffolding your project:

```bash
# 1. Navigate to your project
cd my-rag-app

# 2. Set up environment variables
cp .env.example .env
# Edit .env with your API keys

# 3. Install dependencies
make setup
# or: pip install -r requirements.txt

# 4. Start services with Docker (if enabled)
docker-compose up -d

# 5. Run the application
make run

# 6. Run tests
make test
```

---

## 🛠️ Available Commands

### Create Command

```bash
genai-scaffold create [PROJECT_NAME] [OPTIONS]
```

**Options:**
- `--provider`: LLM provider (openai, anthropic, azure, ollama)
- `--orchestrator`: Framework (langchain, llamaindex, dspy, none)
- `--vector-db`: Vector database (pinecone, chromadb, qdrant, pgvector)
- `--ui`: UI framework (streamlit, gradio, fastapi, none)
- `--deps`: Dependency manager (pip, poetry)
- `--docker/--no-docker`: Enable/disable Docker configuration
- `--interactive, -i`: Use interactive mode

### Version Command

```bash
genai-scaffold version
```

---

## 🔧 Tech Stack Options

### LLM Providers
- **OpenAI**: GPT-4, GPT-3.5, and embedding models
- **Anthropic**: Claude 3 (Opus, Sonnet, Haiku)
- **Azure OpenAI**: Enterprise-grade OpenAI models
- **Ollama**: Local models (Llama 2, Mistral, etc.)

### Orchestration Frameworks
- **LangChain**: Full-featured LLM framework with chains and agents
- **LlamaIndex**: Data framework for LLM applications
- **DSPy**: Declarative language model programming
- **None**: Raw Python with custom implementation

### Vector Databases
- **ChromaDB**: Easy-to-use, local-first vector store
- **Pinecone**: Managed vector database service
- **Qdrant**: High-performance vector search engine
- **pgvector**: PostgreSQL extension for vector operations

### UI Frameworks
- **Streamlit**: Fast way to build data apps
- **Gradio**: Quick ML model interfaces
- **FastAPI**: Modern, fast API framework
- **None**: Headless/CLI application

---

## 📚 Generated Features

### Prompt Management

The generated projects include a sophisticated prompt management system:

```python
from src.prompts import load_prompt

# Load and format a prompt template
prompt = load_prompt("rag_query", context="...", question="...")
```

Prompts are stored in `src/prompts/templates.yaml` with versioning support.

### Configuration Management

Environment-based configuration with validation:

```python
from src.config import Config

# Access configuration
api_key = Config.OPENAI_API_KEY
model = Config.OPENAI_MODEL
```

### Logging

Pre-configured logging utilities:

```python
from src.utils import get_logger

logger = get_logger(__name__)
logger.info("Processing request...")
```

### Observability (Optional)

If enabled, automatic tracing with LangSmith or W&B:

```python
from src.observability import trace_llm_call

@trace_llm_call
def my_llm_function():
    # Automatically traced
    pass
```

---

## 🧪 Testing

Generated projects include a complete test setup:

```bash
# Run tests
make test

# Run with coverage
make test-coverage

# Run specific test
pytest tests/test_example.py -v
```

---

## 🐳 Docker Support

When Docker is enabled, projects include:

- `docker-compose.yml` with service definitions
- `Dockerfile` for the application
- Automatic configuration for:
  - ChromaDB server (if selected)
  - Qdrant server (if selected)
  - PostgreSQL with pgvector (if selected)

Start all services:

```bash
docker-compose up -d
```

---

## 🔄 Makefile Commands

Generated projects include a Makefile with common tasks:

```bash
make setup          # Install dependencies
make test           # Run tests
make test-coverage  # Run tests with coverage
make run            # Run the application
make format         # Format code (black, isort)
make lint           # Run linter (ruff)
make clean          # Clean build artifacts
make docker-up      # Start Docker services (if Docker enabled)
make docker-down    # Stop Docker services
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

Built for developers who want to quickly scaffold production-ready GenAI applications with best practices and flexibility.
