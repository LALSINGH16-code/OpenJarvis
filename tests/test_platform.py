"""Tests for platform utilities."""

from unittest.mock import patch

from openjarvis.utils.platform import Platform, get_platform, is_linux, is_macos, is_windows


class TestPlatform:
    """Test platform detection."""

    def test_platform_enum_values(self):
        """Test that platform enum has expected values."""
        assert Platform.LINUX.value == "linux"
        assert Platform.WINDOWS.value == "windows"
        assert Platform.MACOS.value == "macos"
        assert Platform.UNKNOWN.value == "unknown"

    @patch("openjarvis.utils.platform.stdlib_platform.system")
    def test_detect_linux(self, mock_system):
        """Test Linux detection."""
        mock_system.return_value = "Linux"
        assert get_platform() == Platform.LINUX

    @patch("openjarvis.utils.platform.stdlib_platform.system")
    def test_detect_windows(self, mock_system):
        """Test Windows detection."""
        mock_system.return_value = "Windows"
        assert get_platform() == Platform.WINDOWS

    @patch("openjarvis.utils.platform.stdlib_platform.system")
    def test_detect_macos(self, mock_system):
        """Test macOS detection."""
        mock_system.return_value = "Darwin"
        assert get_platform() == Platform.MACOS

    @patch("openjarvis.utils.platform.stdlib_platform.system")
    def test_detect_unknown(self, mock_system):
        """Test unknown platform detection."""
        mock_system.return_value = "UnknownOS"
        assert get_platform() == Platform.UNKNOWN

    @patch("openjarvis.utils.platform.get_platform")
    def test_is_linux(self, mock_get_platform):
        """Test is_linux helper."""
        mock_get_platform.return_value = Platform.LINUX
        assert is_linux() is True
        mock_get_platform.return_value = Platform.WINDOWS
        assert is_linux() is False

    @patch("openjarvis.utils.platform.get_platform")
    def test_is_windows(self, mock_get_platform):
        """Test is_windows helper."""
        mock_get_platform.return_value = Platform.WINDOWS
        assert is_windows() is True
        mock_get_platform.return_value = Platform.LINUX
        assert is_windows() is False

    @patch("openjarvis.utils.platform.get_platform")
    def test_is_macos(self, mock_get_platform):
        """Test is_macos helper."""
        mock_get_platform.return_value = Platform.MACOS
        assert is_macos() is True
        mock_get_platform.return_value = Platform.LINUX
        assert is_macos() is False
