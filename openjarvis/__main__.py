"""
OpenJarvis entry point.

Run with: python -m openjarvis
"""

import sys

from openjarvis.cli import CLI, print_help_short, print_version
from openjarvis.config import Config
from openjarvis.database import close_db
from openjarvis.logging_config import setup_logging


def main():
    """Main entry point for OpenJarvis."""
    # Parse command-line arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()

        if arg in ["-h", "--help"]:
            print_help_short()
            return 0

        elif arg in ["-v", "--version"]:
            print_version()
            return 0

        else:
            print(f"Unknown argument: {arg}")
            print_help_short()
            return 1

    # Initialize configuration and logging
    Config.initialize()
    setup_logging(Config.LOG_LEVEL)

    # Run the CLI
    try:
        cli = CLI()
        cli.run_interactive()
        return 0
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        return 1
    finally:
        close_db()


if __name__ == "__main__":
    sys.exit(main())
