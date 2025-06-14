# genai-scaffold

**genai-scaffold** is a Python CLI tool that bootstraps production-ready Generative AI project structures with best practices and modular organization out-of-the-box.

![PyPI](https://img.shields.io/pypi/v/genai-scaffold)
![License](https://img.shields.io/pypi/l/genai-scaffold)

---

## ✨ Features

- 🔧 Clean and extensible project structure.
- 🧠 Pluggable design for adding custom LLM clients.
- 🧱 Placeholder modules for prompt engineering.
- 📦 Auto-generates config, data, notebooks, and examples.
- 🐍 Basic unit test setup and packaging workflow.
- ⚡ Fast to get started, easy to extend.

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

To scaffold a new Generative AI project:

```bash
genai-scaffold myproject --provider claude
```

The `--provider` flag selects the default LLM provider used in the generated
configuration files.

This creates:

```
myproject/
├── config/
├── src/
│   ├── llm/
│   ├── prompt_engineering/
│   ├── utils/
│   └── handlers/
├── data/
│   ├── cache/
│   ├── prompts/
│   ├── outputs/
│   └── embeddings/
├── examples/
├── notebooks/
├── requirements.txt
├── setup.py
├── Dockerfile
└── README.md
```

---

## 🧰 Project Structure

Your scaffolded project includes:

- `src/llm/`: placeholders for LLM client implementations (e.g. GPT, Claude)
- `src/prompt_engineering/`: starter templates and chaining helpers
- `src/utils/`: Rate limiting, caching, logging, token counting
- `config/`: YAML config for models, prompts, logging
- `data/`: Inputs, outputs, embeddings, cache
- `examples/`: Working usage examples
- `notebooks/`: Jupyter notebooks for prototyping

---

## 🔄 Updating Your Scaffold Tool

To update:

```bash
pip install --upgrade genai-scaffold
```

---

## 🛠 Roadmap

- [ ] Built-in LLM client implementations
- [ ] Rich prompt engineering utilities
- [ ] Interactive CLI with `typer`
- [ ] LangChain/LlamaIndex integration options
- [ ] Built-in Streamlit UI/ Gradio UI
- [ ] Prompt chaining module
- [ ] Test coverage + GitHub Actions

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

Inspired by real-world GenAI use cases in enterprise environments. Built for speed, clarity, and collaboration.
