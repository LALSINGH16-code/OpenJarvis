# OpenJarvis Architecture

## Overview

OpenJarvis is built with a modular, layered architecture that prioritizes:

1. **Clarity** - Clean separation of concerns
2. **Extensibility** - Easy to add providers, tools, and plugins
3. **Security** - No silent dangerous operations
4. **Privacy** - Local-first by design
5. **Maintainability** - Well-tested, documented code

## Layer Structure

```
┌─────────────────────────────────────┐
│     CLI / User Interface            │
├─────────────────────────────────────┤
│     Assistant Core                  │
│  (Conversation management)          │
├─────────────────────────────────────┤
│  Providers   Tools   Documents      │
│  (AI)        (Desktop) (Files)      │
├─────────────────────────────────────┤
│  Database   Config   Logging        │
│  (Storage)  (Setup)  (Diagnostics) │
├─────────────────────────────────────┤
│     Platform Utilities              │
│  (Linux/Windows adaptation)         │
└─────────────────────────────────────┘
```

## Core Components

### 1. CLI Layer (`openjarvis/cli.py`)

**Responsibility:** User interaction

Features:
- Rich terminal UI
- Command parsing
- User prompts and confirmations
- Output formatting

The CLI is command-based:
```
/help
/status
/settings
/exit
```

### 2. Configuration (`openjarvis/config.py`)

**Responsibility:** Application setup

Handles:
- Environment variables
- `.env` file loading
- Provider API keys
- Application settings
- Safe key management

Never hardcodes secrets.

### 3. Database (`openjarvis/database/`)

**Responsibility:** Persistent storage

Manages:
- SQLite connection
- Schema initialization
- Data transactions
- Query execution

Tables:
- Conversations & Messages
- Memory (long-term)
- Notes & Tasks
- Reminders
- Settings

### 4. Logging (`openjarvis/logging_config.py`)

**Responsibility:** Diagnostics and debugging

Features:
- Console logging
- File logging (rotating)
- Sensitive info filtering
- Level control

Never logs:
- API keys
- Passwords
- Tokens
- Private data

### 5. Utilities (`openjarvis/utils/`)

**Responsibility:** Cross-platform support

Provides:
- Path management
- Platform detection
- Directory initialization

### 6. Providers (Future: Stage 2)

**Responsibility:** AI model integration

Will support:
- Ollama (local)
- OpenRouter
- OpenAI
- Gemini
- Anthropic
- Groq

Architecture:
```
Assistant
    ↓
Provider Registry
    ↓
Selected Provider (Ollama, OpenRouter, etc)
    ↓
AI Model
```

### 7. Tools (Future: Stage 3)

**Responsibility:** Desktop automation

Will support:
- Application launching
- File operations
- Terminal execution
- System monitoring
- Screenshots
- Clipboard

Each tool has a risk classification:
- **LOW** - Always safe
- **MEDIUM** - Requires review
- **HIGH** - Requires confirmation

### 8. Documents (Future: Stage 5)

**Responsibility:** File processing

Will support:
- PDF reading
- DOCX reading
- Markdown reading
- Text reading
- Summarization
- Code explanation

### 9. Plugins (Future: Stage 7)

**Responsibility:** Extensibility

Will support:
- Custom tools
- Custom providers
- Custom integrations
- Custom commands

## Data Flow

### Conversation Flow (Stage 2+)

```
User Input
    ↓
CLI Parser
    ↓
Command Router
    ↓
Provider Interface
    ↓
Selected Provider
    ↓
AI Model
    ↓
Tool Requests (Optional)
    ↓
Tool Execution (with confirmation)
    ↓
Tool Results
    ↓
AI Response
    ↓
CLI Formatter
    ↓
User Output
```

### Tool Execution Flow (Stage 3+)

```
AI Request
    ↓
Tool Validation
    ↓
Risk Assessment
    ↓
Confirmation (if HIGH risk)
    ↓
Execution
    ↓
Result
    ↓
Response to AI
```

## Security Architecture

### API Key Management

```
.env (Local, private)
  ↓
Config.get_api_key()
  ↓
Provider.initialize()
  ↓
API Requests (HTTPS)
  
Never in:
- Source code
- Logs
- Exceptions
- Database
```

### Dangerous Operation Control

```
AI Request
  ↓
Classify Risk Level
  ↓
If HIGH:
  → Ask User for Confirmation
  → Only proceed if approved
  ↓
Execute
  ↓
Log (without sensitive data)
```

## Database Schema

```
Conversations
├── id (PK)
├── created_at
├── provider
└── model

Messages
├── id (PK)
├── conversation_id (FK)
├── role (user/assistant)
├── content
└── timestamp

Memory
├── id (PK)
├── key (UNIQUE)
├── value
├── created_at
└── updated_at

Notes
├── id (PK)
├── title
├── content
├── created_at
└── updated_at

Tasks
├── id (PK)
├── title
├── description
├── completed
├── created_at
└── completed_at

Reminders
├── id (PK)
├── message
├── scheduled_at
├── triggered
└── created_at

Settings
├── key (PK)
└── value
```

## Module Organization

### Current (Stage 1)

```
openjarvis/
├── __init__.py          (Package metadata)
├── __main__.py          (Entry point)
├── config.py            (Configuration)
├── cli.py               (Terminal UI)
├── logging_config.py    (Logging setup)
├── core/                (Reserved)
├── database/
│   ├── __init__.py
│   └── database.py
├── documents/           (Reserved)
├── plugins/             (Reserved)
├── providers/           (Reserved)
├── tools/               (Reserved)
└── utils/
    ├── __init__.py
    ├── paths.py
    └── platform.py
```

### Full (All Stages)

```
openjarvis/
├── core/
│   ├── assistant.py     (Main AI orchestration)
│   ├── router.py        (Command routing)
│   ├── context.py       (Conversation context)
│   ├── memory.py        (Long-term memory)
│   ├── tasks.py         (Task management)
│   ├── notes.py         (Notes management)
│   └── security.py      (Confirmation & validation)
├── providers/
│   ├── base.py          (Abstract interface)
│   ├── ollama.py        (Local AI)
│   ├── openrouter.py    (OpenRouter API)
│   ├── openai.py        (OpenAI API)
│   ├── gemini.py        (Google Gemini)
│   ├── anthropic.py     (Anthropic Claude)
│   ├── groq.py          (Groq API)
│   └── registry.py      (Provider discovery)
├── tools/
│   ├── base.py          (Abstract interface)
│   ├── launcher.py      (App launching)
│   ├── files.py         (File operations)
│   ├── terminal.py      (Shell execution)
│   ├── system.py        (System monitoring)
│   ├── clipboard.py     (Clipboard access)
│   └── screenshot.py    (Screen capture)
├── documents/
│   ├── reader.py        (File reader)
│   ├── pdf.py           (PDF support)
│   ├── docx.py          (DOCX support)
│   └── summarizer.py    (Summarization)
└── plugins/
    ├── base.py          (Plugin interface)
    ├── loader.py        (Plugin loading)
    └── registry.py      (Plugin discovery)
```

## Design Principles

### 1. Local-First

- Ollama is the default AI option
- Cloud providers are optional
- User data stays local by default

### 2. Provider-Neutral

- No hardcoded provider logic in core
- Providers implement a standard interface
- Easy to add new providers

### 3. Tool Safety

- No automatic execution of dangerous operations
- User confirmation for HIGH-risk actions
- Clear error messages
- Logging for audit trails

### 4. Extensibility

- Plugins can add capabilities
- Providers can be added without core changes
- Tools can be registered dynamically

### 5. Transparency

- User knows which provider is being used
- User knows which tools are enabled
- No silent network requests
- No hidden data collection

## Performance Considerations

### Current

- Lightweight CLI (no heavy UI framework in Stage 1)
- SQLite for local storage (sufficient for personal use)
- No background processes
- Fast startup time

### Future

- Connection pooling for API calls
- Caching for frequently used data
- Batch operations for efficiency
- Optional GPU support for local models

## Testing Strategy

### Unit Tests

- Configuration validation
- Database operations
- Platform detection
- Provider interface tests
- Tool risk classification
- Permission validation

### Integration Tests

- Provider + AI flow
- Tool execution flow
- Full conversation flow
- Permission confirmation flow

### Manual Tests

- Fresh installation
- CLI commands
- Database persistence
- Logging
- Provider configuration

## Deployment

### Installation

```bash
git clone https://github.com/LALSINGH16-code/OpenJarvis.git
cd OpenJarvis
pip install -e .
```

### Running

```bash
python -m openjarvis
```

### Configuration

```bash
# Edit ~/.openjarvis/.env
OPENROUTER_API_KEY=your-key
OLLAMA_HOST=http://localhost:11434
```

### Testing

```bash
pytest
pytest --cov=openjarvis
```

## Future Enhancements

### Planned

- GUI (PySide6)
- Voice interface
- Web API
- Docker containers
- Linux packages
- Windows installer

### Possible

- Mobile companion app
- Multi-user support
- Encryption at rest
- Advanced scheduling
- Web search integration
- Smart home control

## Version Compatibility

### Python

- Python 3.11+
- Type hints throughout
- Modern async patterns (future)

### OS

- Linux (primary)
- Windows (supported)
- macOS (future)

### Dependencies

- Minimal, focused dependencies
- Security-audited libraries
- Active maintenance required

---

This architecture supports OpenJarvis' goals:
1. **Open Source** - Transparent, community-driven
2. **Local-First** - Privacy by default
3. **Provider Freedom** - Not locked to one AI
4. **Safe** - User confirmation for dangerous ops
5. **Extensible** - Easy to add capabilities
