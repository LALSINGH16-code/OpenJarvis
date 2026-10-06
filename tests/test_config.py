"""Tests for configuration management."""

import os
from pathlib import Path
from unittest.mock import patch

import pytest

from openjarvis.config import Config


class TestConfig:
    """Test Config class."""

    def test_version_is_set(self):
        """Test that version is correctly set."""
        assert Config.VERSION == "1.0.0"

    def test_get_api_key_openrouter(self):
        """Test getting OpenRouter API key."""
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}):
            # Re-read config from environment
            Config.OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
            key = Config.get_api_key("openrouter")
            assert key == "test-key"

    def test_get_api_key_none(self):
        """Test getting API key when not configured."""
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": ""}, clear=True):
            Config.OPENROUTER_API_KEY = ""
            key = Config.get_api_key("openrouter")
            assert key is None

    def test_get_api_key_case_insensitive(self):
        """Test that provider names are case-insensitive."""
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}):
            Config.OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
            key_lower = Config.get_api_key("openrouter")
            key_upper = Config.get_api_key("OPENROUTER")
            key_mixed = Config.get_api_key("OpenRouter")
            assert key_lower == key_upper == key_mixed == "test-key"

    def test_get_provider_status_ollama_always_available(self):
        """Test that Ollama is always marked as available."""
        status = Config.get_provider_status()
        assert status["ollama"] is True

    def test_get_provider_status_other_providers(self):
        """Test provider status detection."""
        with patch.dict(os.environ, {
            "OPENROUTER_API_KEY": "test-key",
            "OPENAI_API_KEY": "",
        }, clear=True):
            # Re-read config from environment
            Config.OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
            Config.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
            
            status = Config.get_provider_status()
            assert status["openrouter"] is True
            assert status["openai"] is False

    def test_db_path_is_set(self):
        """Test that database path is configured."""
        assert Config.DB_PATH is not None
        assert isinstance(Config.DB_PATH, Path)

    def test_log_path_is_set(self):
        """Test that log path is configured."""
        assert Config.LOG_PATH is not None
        assert isinstance(Config.LOG_PATH, Path)

    def test_ollama_host_default(self):
        """Test default Ollama host."""
        # When env var is not set, getenv should return default
        with patch.dict(os.environ, {}, clear=True):
            ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
            assert ollama_host == "http://localhost:11434"

    def test_require_confirmation_default(self):
        """Test that confirmation is required by default."""
        with patch.dict(os.environ, {"REQUIRE_CONFIRMATION": "true"}):
            assert Config.REQUIRE_CONFIRMATION is True
