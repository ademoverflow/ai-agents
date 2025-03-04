# AI Agents

Install python3.13 with homebrew:
```bash
brew install python@3.13
```

Install uv with homebrew:
```bash
brew install uv
```

Create your virtual environment and install the requirements:
```bash
uv sync
```

If you want to install a new package, you can do it with:
```bash
uv add <package>
```

Only for development, add --dev flag:
```bash
uv add --dev <package>
```

Run the main script:
```bash
uv run ai-agents
```
