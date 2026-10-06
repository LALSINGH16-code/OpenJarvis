"""
Logging configuration for OpenJarvis.

Provides structured logging with file and console output.
Never logs sensitive information like API keys, passwords, or private content.
"""

import logging
import logging.handlers
from pathlib import Path

from openjarvis.config import Config


class SensitiveInfoFilter(logging.Filter):
    """Filter to prevent logging of sensitive information."""

    SENSITIVE_PATTERNS = [
        "api_key",
        "apikey",
        "password",
        "token",
        "secret",
        "authorization",
        "credentials",
        "KEY",
        "PASSWORD",
        "TOKEN",
    ]

    def filter(self, record: logging.LogRecord) -> bool:
        """Filter out sensitive information from log records."""
        # Check if any sensitive pattern is in the log message
        message = record.getMessage().lower()
        for pattern in self.SENSITIVE_PATTERNS:
            if pattern in message:
                record.msg = "[REDACTED - SENSITIVE INFORMATION]"
                record.args = ()
        return True


def setup_logging(level: str = "INFO") -> None:
    """Set up logging for OpenJarvis."""
    # Get the root logger
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))

    # Create logs directory
    log_dir = Config.LOG_PATH
    log_dir.mkdir(parents=True, exist_ok=True)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, level.upper(), logging.INFO))
    console_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(console_format)
    console_handler.addFilter(SensitiveInfoFilter())

    # File handler (rotating)
    log_file = log_dir / "openjarvis.log"
    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5,
    )
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"
    )
    file_handler.setFormatter(file_format)
    file_handler.addFilter(SensitiveInfoFilter())

    # Add handlers to root logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Suppress noisy third-party loggers
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance."""
    return logging.getLogger(name)
