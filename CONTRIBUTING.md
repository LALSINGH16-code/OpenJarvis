# Contributing to OpenJarvis

Thank you for your interest in contributing to OpenJarvis!

OpenJarvis is a community-driven, open-source project. All contributions are welcome.

## How to Contribute

### Reporting Bugs

- Use GitHub Issues to report bugs
- Provide a clear description of the problem
- Include steps to reproduce
- Include your environment (OS, Python version, etc.)

### Suggesting Features

- Use GitHub Issues to suggest features
- Describe the use case
- Explain the expected behavior

### Code Contributions

1. **Fork the repository**

```bash
git clone https://github.com/LALSINGH16-code/OpenJarvis.git
cd OpenJarvis
```

2. **Create a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

3. **Install development dependencies**

```bash
pip install -r requirements.txt
pip install pytest pytest-cov mypy black flake8
```

4. **Create a feature branch**

```bash
git checkout -b feature/your-feature-name
```

5. **Make your changes**

- Follow the coding standards (see below)
- Write tests for new functionality
- Update documentation if needed

6. **Run tests**

```bash
pytest
pytest --cov=openjarvis  # with coverage
```

7. **Check code quality**

```bash
flake8 openjarvis tests
black --check openjarvis tests
mypy openjarvis
```

8. **Commit your changes**

```bash
git add .
git commit -m "feat: description of your changes"
```

Follow conventional commits:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation
- `test:` for tests
- `refactor:` for code refactoring
- `chore:` for maintenance

9. **Push to your fork**

```bash
git push origin feature/your-feature-name
```

10. **Submit a Pull Request**

- Describe what your PR does
- Reference any related issues
- Wait for review and feedback

## Coding Standards

### Python Style

- Python 3.11+
- Follow PEP 8
- Use type hints for public APIs
- Write docstrings for classes and functions

### Code Quality

- No hardcoded secrets or API keys
- No fake/placeholder implementations
- Keep functions small and focused
- Write meaningful error messages

### Security

- Never log sensitive information (API keys, passwords, tokens)
- Validate user input
- Use confirmation for dangerous operations
- Follow the principle of least privilege

### Testing

- Write tests for new features
- Run `pytest` before submitting
- Aim for good coverage
- Test both happy paths and error cases

## Development Guidelines

### Stage-based Development

OpenJarvis is developed in stages. Check the master development prompt for the current stage.

When adding features:
1. Implement the core functionality
2. Add tests
3. Update documentation
4. Ensure all tests pass before committing

### No Fake Functionality

- Do not create placeholder implementations
- Do not add fake API responses
- Mark unimplemented features as unavailable

### Keep It Runnable

After every major change:
1. Run syntax checks
2. Run tests
3. Start the application
4. Fix any errors

Never leave the project in a broken state.

## Adding New Providers

To add a new AI provider:

1. Create a new file in `openjarvis/providers/`
2. Inherit from `AIProvider` base class
3. Implement required methods
4. Add to provider registry
5. Add tests
6. Update documentation

Example:

```python
from openjarvis.providers.base import AIProvider

class MyProvider(AIProvider):
    name = "myprovider"
    
    def generate(self, messages, model, temperature=0.7, max_tokens=None):
        # Implementation
        pass
```

## Adding New Tools

To add a new tool:

1. Create a new file in `openjarvis/tools/`
2. Define the tool class
3. Add security classification (LOW, MEDIUM, HIGH)
4. Add tests
5. Update documentation

## Adding Plugins

To add plugin support:

1. Create plugin in `plugins/your-plugin/`
2. Follow the plugin interface
3. Add tests
4. Update documentation

## Pull Request Process

1. Update documentation
2. Run all tests
3. Ensure code quality checks pass
4. Write a clear PR description
5. Be open to feedback

## Questions?

- Open an issue for questions
- Check existing documentation
- Review the main development prompt

## Code of Conduct

- Be respectful
- Be constructive
- Focus on ideas, not people
- Welcome diverse perspectives

Thank you for contributing!
