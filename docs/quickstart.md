# Quick Start Guide - OpenJarvis v1.0.0

## Installation (5 minutes)

### Prerequisites

- Python 3.11 or later
- Git
- ~500MB free disk space

### Step 1: Clone the Repository

```bash
git clone https://github.com/LALSINGH16-code/OpenJarvis.git
cd OpenJarvis
```

### Step 2: Create Virtual Environment

```bash
# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run OpenJarvis

```bash
python -m openjarvis
```

You should see:

```
╭──────────────────────────────────────────╮
│              OpenJarvis                  │
│      Open-source AI desktop assistant    │
╰──────────────────────────────────────────╯

Type '/help' for available commands or start typing to chat.

You >
```

## Configuration (Optional but Recommended)

### Setup Configuration File

Create `~/.openjarvis/.env` based on the template:

```bash
# Copy the example
cat .env.example > ~/.openjarvis/.env

# Edit with your favorite editor
nano ~/.openjarvis/.env
# or
code ~/.openjarvis/.env
```

### Add API Keys (If Using Cloud Providers)

#### OpenRouter

1. Go to https://openrouter.ai
2. Sign up for a free account
3. Get your API key
4. Add to `~/.openjarvis/.env`:

```env
OPENROUTER_API_KEY=your_key_here
```

#### Local AI with Ollama (Recommended)

1. Install Ollama from https://ollama.ai
2. Start Ollama
3. OpenJarvis will automatically detect it

```bash
# Start Ollama
ollama serve

# Pull a model (in another terminal)
ollama pull llama2  # or another model
```

## First Run

### Interactive Mode

```bash
python -m openjarvis
```

### Available Commands

Type these in the prompt:

```
/help       - Show all commands
/status     - Check configuration and provider status
/provider   - List available AI providers
/settings   - Show current settings
/exit       - Exit OpenJarvis
```

### Example Session

```
You > /status

OpenJarvis Status

Version: 1.0.0
Database: ✓

Available AI Providers
┏━━━━━━━━━━━━┳━━━━━━━━┓
┃ Provider   ┃ Status ┃
┡━━━━━━━━━━━━╇━━━━━━━━┩
│ Ollama     │ ✓      │
│ OpenRouter │ ✗      │
│ OpenAI     │ ✗      │
│ Gemini     │ ✗      │
│ Anthropic  │ ✗      │
│ Groq       │ ✗      │
└━━━━━━━━━━━━┴━━━━━━━━┘

You > /settings

Configuration Settings

┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Setting              ┃ Value            ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ Version              │ 1.0.0            │
│ Log Level            │ INFO             │
│ Ollama Host          │ http://localhost │
│ Require Confirmation │ True             │
└━━━━━━━━━━━━━━━━━━━━━┴━━━━━━━━━━━━━━━━━━┘

You > /exit
Goodbye!
```

## Running Tests

### Install Test Dependencies

```bash
pip install pytest pytest-cov
```

### Run Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=openjarvis --cov-report=html

# Run specific test file
pytest tests/test_config.py -v
```

### Expected Output

```
========================= 26 passed in 0.29s =========================
```

## Troubleshooting

### "Command not found: python"

Use `python3` instead:

```bash
python3 -m openjarvis
```

### "No module named openjarvis"

Make sure virtual environment is activated:

```bash
# Linux / macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### "Database error"

Delete the database and it will be recreated:

```bash
rm ~/.openjarvis/openjarvis.db
python -m openjarvis
```

### "Ollama not found"

Install Ollama from https://ollama.ai and start it:

```bash
ollama serve
```

### "API key not working"

1. Check `~/.openjarvis/.env` exists
2. Verify API key is correct
3. Check provider status with `/status`

## Directory Structure

Configuration and data are stored in:

```
~/.openjarvis/
├── .env                 (Your configuration)
├── openjarvis.db        (Database)
└── logs/
    └── openjarvis.log   (Application logs)
```

## Current Capabilities (v1.0.0 - Stage 1)

✅ Implemented:
- Configuration management
- Database storage
- CLI interface
- Provider detection
- Status monitoring
- Settings display

🚧 Coming in Stage 2:
- AI chat with various providers
- Conversation history
- Multiple model selection

🚧 Coming in Stage 3+:
- File operations
- Terminal execution
- Application launcher
- Notes and tasks
- Document reading
- Plugins

## Next Steps

1. **Try the CLI**: Get familiar with the interface
2. **Configure Ollama**: Set up local AI (recommended)
3. **Run Tests**: Ensure everything works
4. **Read Documentation**: Check `docs/` for detailed info
5. **Join Development**: Contribute on GitHub

## Documentation

- `README.md` - Project overview
- `docs/architecture.md` - System design
- `docs/stage-1-foundation.md` - Current features
- `SECURITY.md` - Security practices
- `CONTRIBUTING.md` - How to contribute

## Getting Help

### Documentation

- Check `CONTRIBUTING.md` for development setup
- Check `SECURITY.md` for security info
- Check `docs/` for detailed documentation

### Issues

- Report bugs on GitHub Issues
- Suggest features on GitHub Issues
- Follow the issue templates

### Community

- Discussions on GitHub Discussions
- Code of Conduct: Be respectful and constructive

## Development Setup

If you want to contribute:

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Format code
black openjarvis tests

# Check code quality
flake8 openjarvis tests

# Type checking
mypy openjarvis
```

## Version Information

- **OpenJarvis:** v1.0.0
- **Status:** Stage 1 - Foundation
- **Python:** 3.11+
- **Platforms:** Linux, Windows
- **License:** MIT

## What's Next?

After you've tried Stage 1 (Foundation), future stages will add:

- **Stage 2**: AI providers and chat
- **Stage 3**: Computer tools
- **Stage 4**: Productivity features
- **Stage 5**: Document support
- **Stage 6**: More AI providers
- **Stage 7**: Plugins
- **Stage 8**: GUI
- **Stage 9**: Packaging
- **Stage 10**: Polish

## Need Help?

1. Check documentation: `docs/`
2. Run help: `/help` in the CLI
3. Check logs: `~/.openjarvis/logs/openjarvis.log`
4. Check issues: GitHub Issues
5. Ask in Discussions: GitHub Discussions

---

**Welcome to OpenJarvis!**

Start with `/help` and explore. The foundation is solid and ready for the next stages of development.

Happy coding! 🚀
