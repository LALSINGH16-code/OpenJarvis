# Changelog

All notable changes to OpenJarvis will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [1.0.0] - Development

### Stage 1: Foundation (Current)

#### Added

- Core project structure
- Configuration system with `python-dotenv` support
- SQLite database with migrations
- Structured logging system
- Rich CLI interface with command support
- Database schema for:
  - Conversations
  - Messages
  - Memory
  - Notes
  - Tasks
  - Reminders
  - Settings
- Command-line arguments (`--help`, `--version`)
- CLI commands:
  - `/help` - Show available commands
  - `/status` - System status
  - `/provider` - Show configured providers
  - `/settings` - Show configuration
  - `/exit` - Exit the application
- Platform detection (Linux, Windows, macOS)
- Path utilities
- Logging with sensitive info filtering
- Environment variable validation
- Project documentation:
  - README.md (existing)
  - CONTRIBUTING.md
  - SECURITY.md
  - This CHANGELOG

### Planned

#### Stage 2: AI Providers

- [ ] AI provider base interface
- [ ] Ollama integration
- [ ] OpenRouter integration
- [ ] Conversation history
- [ ] Message storage
- [ ] Provider registry

#### Stage 3: Computer Tools

- [ ] Application launcher
- [ ] File search
- [ ] File management (create, read, write)
- [ ] Safe terminal execution
- [ ] System monitoring
- [ ] Clipboard access
- [ ] Screenshot capability

#### Stage 4: Productivity

- [ ] Notes system
- [ ] Task management
- [ ] Reminders
- [ ] Long-term memory
- [ ] Search functionality

#### Stage 5: Document Support

- [ ] PDF reading
- [ ] DOCX reading
- [ ] Markdown reading
- [ ] Text file reading
- [ ] Document summarization
- [ ] Code explanation

#### Stage 6: Additional Providers

- [ ] OpenAI integration
- [ ] Google Gemini integration
- [ ] Anthropic Claude integration
- [ ] Groq integration

#### Stage 7: Plugins & Search

- [ ] Plugin system
- [ ] Plugin loader
- [ ] Web search integration
- [ ] Search provider interface

#### Stage 8: GUI

- [ ] PySide6 GUI (optional)
- [ ] Chat interface
- [ ] Settings panel
- [ ] Responsive design

#### Stage 9: Packaging

- [ ] GitHub Actions CI/CD
- [ ] Automated testing
- [ ] Build pipeline
- [ ] Release automation

#### Stage 10: Polish

- [ ] Security review
- [ ] Performance optimization
- [ ] Documentation completion
- [ ] Testing completion

## Notes

- Version 1.0.0 is currently in development
- Only Stage 1 is complete at this time
- This is an alpha release
- API and structure may change between stages
- Feedback and contributions are welcome

## Future Versions

### v1.1.0 (Planned)

- [ ] Voice support
- [ ] Additional providers
- [ ] GUI improvements
- [ ] Plugin ecosystem expansion

### v2.0.0 (Planned)

- [ ] Encryption at rest
- [ ] Advanced scheduling
- [ ] Multi-user support
- [ ] Web API
- [ ] Mobile companion app
