"""Path utilities for OpenJarvis."""

from pathlib import Path


def get_openjarvis_dir() -> Path:
    """Get the OpenJarvis configuration directory."""
    return Path.home() / ".openjarvis"


def get_data_dir() -> Path:
    """Get the OpenJarvis data directory."""
    data_dir = get_openjarvis_dir() / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


def get_plugins_dir() -> Path:
    """Get the plugins directory."""
    plugins_dir = get_openjarvis_dir() / "plugins"
    plugins_dir.mkdir(parents=True, exist_ok=True)
    return plugins_dir


def get_logs_dir() -> Path:
    """Get the logs directory."""
    logs_dir = get_openjarvis_dir() / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    return logs_dir
