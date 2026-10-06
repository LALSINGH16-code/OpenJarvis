# Security Policy for OpenJarvis

## Overview

OpenJarvis is a desktop assistant that can control your computer. Security is a critical part of the project.

## Threat Model

### What OpenJarvis Can Do

OpenJarvis can:
- Execute shell commands
- Delete files
- Launch applications
- Access system information
- Read and write clipboard contents
- Take screenshots
- Restart or shutdown the system
- Modify system files

Because of this capability, it must be treated as a security-sensitive application.

### Risk Levels

Operations are classified by risk:

#### LOW Risk
- Reading files
- Listing directories
- Getting system information
- Non-destructive commands

#### MEDIUM Risk
- Creating or modifying files
- Installing packages
- Changing permissions

#### HIGH Risk
- Deleting files
- Executing shell commands
- Restarting/shutting down
- Killing processes
- System modifications

## Confirmation System

HIGH-risk operations require explicit user confirmation.

Example:

```
OpenJarvis wants to delete:
/path/to/file.txt

Continue? [y/N]
```

Never allow an AI model to silently perform dangerous operations.

## API Key Security

### Never
- Hardcode API keys in source code
- Commit .env files with real keys
- Print API keys in logs or errors
- Store API keys in plain text
- Expose API keys in exceptions
- Send API keys over unencrypted connections

### Always
- Use environment variables
- Use .env files (never committed)
- Store keys in secure configuration
- Redact keys from logs
- Use HTTPS for API calls
- Validate API responses

## Dangerous Tools

### Terminal Execution

Shell command execution is powerful but dangerous.

Commands are classified:

**Safe:**
```
pwd, ls, dir, whoami, python --version, git status
```

**Potentially Dangerous:**
```
rm, del, format, shutdown, reboot, kill, chmod, sudo
```

Dangerous commands require confirmation.

### File Operations

Deletion always requires confirmation.

Example:

```
OpenJarvis wants to delete:
/home/user/important.txt

Continue? [y/N]
```

### System Operations

- Shutdown/restart require confirmation
- Process killing requires confirmation
- Permission changes require confirmation

## Plugins

### Plugin Security

Plugins can extend OpenJarvis with new capabilities.

Plugins are loaded from:
```
~/.openjarvis/plugins/
```

Plugin security:

1. **No automatic execution** - Plugins don't run automatically
2. **Sandbox consideration** - Plugins run in the same Python process
3. **Validation** - Validate plugin code before loading
4. **Permissions** - Plugins inherit OpenJarvis permissions
5. **Documentation** - Plugin capabilities should be clear

### Plugin Restrictions

Plugins should not:
- Silently perform dangerous operations
- Bypass confirmation systems
- Steal API keys or credentials
- Modify system files without confirmation
- Run arbitrary code without disclosure

## Local vs Cloud

### Local-First Principle

- Local AI (Ollama) is the default option
- Cloud providers are optional
- User data doesn't leave the computer unless explicitly configured

### Cloud Providers

If using cloud providers:

1. Only configured providers are used
2. Sensitive data is NOT sent without user awareness
3. User has control over which data is sent
4. No automatic telemetry or data collection

## Privacy

### What Data Is Stored

OpenJarvis stores locally:
- Conversation history (SQLite)
- Notes and tasks
- Memory entries
- Settings
- Logs

### What Data Is NOT Stored

- API keys (use environment variables)
- Passwords
- Clipboard contents (unless user requests)
- Screenshots (unless user requests)

### What Data Is NOT Sent

By default, nothing is sent to external services unless:
1. User explicitly configures a cloud AI provider
2. User requests an operation that requires external access
3. The operation is clearly logged

## Reporting Security Issues

If you discover a security vulnerability:

1. **Do NOT** disclose it publicly
2. **Do NOT** open a GitHub issue
3. **Do** report to: [security contact will be provided]

Include:
- Description of the vulnerability
- Affected versions
- Proof of concept (if possible)
- Steps to reproduce

The security team will:
- Acknowledge receipt within 48 hours
- Investigate the issue
- Develop a patch
- Coordinate disclosure

## Security Best Practices

### For Users

1. Keep OpenJarvis updated
2. Use strong API keys
3. Never share .env files
4. Review AI-generated commands before execution
5. Only install trusted plugins
6. Keep Python updated

### For Developers

1. Validate all user input
2. Use type hints
3. Write tests for security features
4. Never hardcode secrets
5. Redact sensitive info from logs
6. Use HTTPS for API calls
7. Keep dependencies updated
8. Review code for security issues

## Dependency Security

OpenJarvis uses:
- `rich` - CLI rendering
- `python-dotenv` - Configuration
- `httpx` - HTTP requests
- `psutil` - System monitoring
- `pypdf` - PDF reading
- `python-docx` - DOCX reading
- `pytest` - Testing

All dependencies are verified for security.

Dependency vulnerabilities should be reported and patched promptly.

## Logging

### What Is Logged

- Application events
- Errors
- Configuration status
- Provider status

### What Is NOT Logged

- API keys or tokens
- Passwords
- Clipboard contents
- Private document contents
- User credentials

## Encryption

Current version:
- No encryption at rest (database is local SQLite)
- HTTPS for API calls to providers
- Environment variables for secrets

Future versions may include:
- Encryption at rest for sensitive data
- Encrypted credential storage
- Secure plugin sandboxing

## Testing

Security features are tested:
- Configuration tests
- Path validation tests
- Permission tests
- Command classification tests
- API key handling tests

## Responsible Disclosure

If you find a security issue:

1. Report privately
2. Give the team time to respond
3. Work collaboratively on a fix
4. Agree on disclosure timing
5. Receive credit (optional)

## Version History

### v1.0.0

Initial version with:
- Confirmation system for dangerous operations
- API key protection
- Local-first architecture
- Command classification
- Secure logging
