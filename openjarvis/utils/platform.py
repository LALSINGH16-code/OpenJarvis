"""Platform detection and utilities."""

import platform as stdlib_platform
from enum import Enum


class Platform(Enum):
    """Supported platforms."""

    LINUX = "linux"
    WINDOWS = "windows"
    MACOS = "macos"
    UNKNOWN = "unknown"


def get_platform() -> Platform:
    """Detect the current platform."""
    system = stdlib_platform.system().lower()

    if system == "linux":
        return Platform.LINUX
    elif system == "windows":
        return Platform.WINDOWS
    elif system == "darwin":
        return Platform.MACOS
    else:
        return Platform.UNKNOWN


def is_linux() -> bool:
    """Check if running on Linux."""
    return get_platform() == Platform.LINUX


def is_windows() -> bool:
    """Check if running on Windows."""
    return get_platform() == Platform.WINDOWS


def is_macos() -> bool:
    """Check if running on macOS."""
    return get_platform() == Platform.MACOS


def get_platform_name() -> str:
    """Get human-readable platform name."""
    platform = get_platform()
    if platform == Platform.LINUX:
        return "Linux"
    elif platform == Platform.WINDOWS:
        return "Windows"
    elif platform == Platform.MACOS:
        return "macOS"
    else:
        return "Unknown"
