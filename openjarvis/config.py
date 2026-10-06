"""
Configuration management for OpenJarvis.

Handles environment variables, .env file loading, and configuration defaults.
"""

import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv


# Load .env file if it exists
def load_config() -> None:
    """Load environment variables from .env file."""
    env_path = Path.home() / ".openjarvis" / ".env"
    if env_path.exists():
        load_dotenv(env_path)


class Config:
    """OpenJarvis configuration."""

    # Version
    VERSION = "1.0.0"

    # Database
    DB_PATH = Path.home() / ".openjarvis" / "openjarvis.db"

    # Logging
    LOG_PATH = Path.home() / ".openjarvis" / "logs"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    # AI Providers
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

    # Ollama
    OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "")

    # Application settings
    DEFAULT_PROVIDER = os.getenv("DEFAULT_PROVIDER", "")
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "")

    # Security and confirmation
    REQUIRE_CONFIRMATION = os.getenv("REQUIRE_CONFIRMATION", "true").lower() == "true"

    @classmethod
    def initialize(cls) -> None:
        """Initialize configuration directories."""
        load_config()
        
        # Create .openjarvis directory
        openjarvis_dir = Path.home() / ".openjarvis"
        openjarvis_dir.mkdir(exist_ok=True)

        # Create logs directory
        cls.LOG_PATH.mkdir(parents=True, exist_ok=True)

        # Create .env.example if it doesn't exist
        env_example = openjarvis_dir / ".env.example"
        if not env_example.exists():
            env_example.write_text(
                """# OpenJarvis Configuration

# AI Provider API Keys
OPENROUTER_API_KEY=
OPENAI_API_KEY=
GEMINI_API_KEY=
ANTHROPIC_API_KEY=
GROQ_API_KEY=

# Ollama Configuration
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=

# Application Settings
DEFAULT_PROVIDER=
DEFAULT_MODEL=

# Logging
LOG_LEVEL=INFO

# Security
REQUIRE_CONFIRMATION=true
"""
            )

    @classmethod
    def get_api_key(cls, provider: str) -> Optional[str]:
        """Get API key for a given provider."""
        provider = provider.lower()
        if provider == "openrouter":
            return cls.OPENROUTER_API_KEY or None
        elif provider == "openai":
            return cls.OPENAI_API_KEY or None
        elif provider == "gemini":
            return cls.GEMINI_API_KEY or None
        elif provider == "anthropic":
            return cls.ANTHROPIC_API_KEY or None
        elif provider == "groq":
            return cls.GROQ_API_KEY or None
        return None

    @classmethod
    def get_provider_status(cls) -> dict:
        """Get configuration status for all providers."""
        return {
            "ollama": True,  # Always available locally
            "openrouter": bool(cls.OPENROUTER_API_KEY),
            "openai": bool(cls.OPENAI_API_KEY),
            "gemini": bool(cls.GEMINI_API_KEY),
            "anthropic": bool(cls.ANTHROPIC_API_KEY),
            "groq": bool(cls.GROQ_API_KEY),
        }
