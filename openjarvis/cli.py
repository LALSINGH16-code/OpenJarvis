"""
CLI interface for OpenJarvis.

Rich-powered terminal user interface for the assistant.
"""

import sys
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from openjarvis import __version__
from openjarvis.config import Config
from openjarvis.logging_config import get_logger

logger = get_logger(__name__)


class CLI:
    """OpenJarvis CLI interface."""

    def __init__(self):
        """Initialize the CLI."""
        self.console = Console()
        self.running = False

    def print_welcome(self) -> None:
        """Display welcome message."""
        welcome_text = f"""[bold cyan]OpenJarvis[/bold cyan] {__version__}
[dim]Open-source AI desktop assistant[/dim]"""

        self.console.print(
            Panel(
                welcome_text,
                border_style="cyan",
                padding=(1, 2),
            )
        )

    def print_help(self) -> None:
        """Display help message."""
        help_text = """[bold]Available Commands[/bold]

[cyan]/help[/cyan]            Show this help message
[cyan]/status[/cyan]          Show system and provider status
[cyan]/provider[/cyan]        Show configured AI providers
[cyan]/model[/cyan]           Set or show current AI model
[cyan]/tools[/cyan]           List available tools
[cyan]/plugins[/cyan]         List installed plugins
[cyan]/history[/cyan]         Show conversation history
[cyan]/clear[/cyan]           Clear conversation history
[cyan]/notes[/cyan]           Manage notes
[cyan]/tasks[/cyan]           Manage tasks
[cyan]/memory[/cyan]          Manage long-term memory
[cyan]/settings[/cyan]        Show configuration settings
[cyan]/exit[/cyan]            Exit OpenJarvis

[dim]Type a message to chat with the AI.[/dim]"""

        self.console.print(Panel(help_text, border_style="cyan"))

    def print_status(self) -> None:
        """Display system status."""
        providers = Config.get_provider_status()

        table = Table(title="OpenJarvis Status", border_style="cyan")
        table.add_column("Component", style="cyan")
        table.add_column("Status", style="green")

        table.add_row("Version", __version__)
        table.add_row("Database", "✓")

        # Provider status
        self.console.print("\n[bold]Available AI Providers[/bold]")
        provider_table = Table(border_style="cyan")
        provider_table.add_column("Provider", style="cyan")
        provider_table.add_column("Status", style="green")

        for provider, available in providers.items():
            status = "✓" if available else "✗"
            status_style = "green" if available else "red"
            provider_table.add_row(provider.capitalize(), Text(status, style=status_style))

        self.console.print(provider_table)

    def print_providers(self) -> None:
        """Display configured providers."""
        providers = Config.get_provider_status()

        table = Table(title="Configured AI Providers", border_style="cyan")
        table.add_column("Provider", style="cyan")
        table.add_column("Status", style="green")

        for provider, available in providers.items():
            status = "✓" if available else "✗"
            status_style = "green" if available else "red"
            provider_table_row = Text(status, style=status_style)
            table.add_row(provider.capitalize(), provider_table_row)

        self.console.print(table)

    def print_info(self, message: str) -> None:
        """Print an info message."""
        self.console.print(f"[cyan]ℹ[/cyan]  {message}")

    def print_error(self, message: str) -> None:
        """Print an error message."""
        self.console.print(f"[red]✗[/red]  {message}")

    def print_success(self, message: str) -> None:
        """Print a success message."""
        self.console.print(f"[green]✓[/green]  {message}")

    def print_warning(self, message: str) -> None:
        """Print a warning message."""
        self.console.print(f"[yellow]⚠[/yellow]  {message}")

    def handle_command(self, command: str) -> bool:
        """Handle a CLI command. Return True to continue, False to exit."""
        command = command.strip().lower()

        if command == "/exit":
            self.console.print("[yellow]Goodbye![/yellow]")
            return False

        elif command == "/help":
            self.print_help()

        elif command == "/status":
            self.print_status()

        elif command == "/provider":
            self.print_providers()

        elif command == "/model":
            current_model = Config.DEFAULT_MODEL or "Not set"
            self.console.print(f"Current model: [cyan]{current_model}[/cyan]")
            self.console.print("Model configuration not yet implemented in v1.0")

        elif command == "/tools":
            self.console.print("[yellow]Tools not yet implemented in v1.0[/yellow]")

        elif command == "/plugins":
            self.console.print("[yellow]Plugins not yet implemented in v1.0[/yellow]")

        elif command == "/history":
            self.console.print("[yellow]Conversation history not yet implemented in v1.0[/yellow]")

        elif command == "/clear":
            self.console.print("[yellow]Clear not yet implemented in v1.0[/yellow]")

        elif command == "/notes":
            self.console.print("[yellow]Notes not yet implemented in v1.0[/yellow]")

        elif command == "/tasks":
            self.console.print("[yellow]Tasks not yet implemented in v1.0[/yellow]")

        elif command == "/memory":
            self.console.print("[yellow]Memory not yet implemented in v1.0[/yellow]")

        elif command == "/settings":
            self.print_settings()

        elif command == "":
            pass  # Empty input

        else:
            self.print_error(f"Unknown command: {command}")
            self.print_info("Type '/help' for available commands")

        return True

    def print_settings(self) -> None:
        """Display configuration settings."""
        table = Table(title="Configuration Settings", border_style="cyan")
        table.add_column("Setting", style="cyan")
        table.add_column("Value", style="green")

        table.add_row("Version", __version__)
        table.add_row("Log Level", Config.LOG_LEVEL)
        table.add_row("Database Path", str(Config.DB_PATH))
        table.add_row("Ollama Host", Config.OLLAMA_HOST)
        table.add_row("Require Confirmation", str(Config.REQUIRE_CONFIRMATION))

        self.console.print(table)

    def run_interactive(self) -> None:
        """Run the interactive CLI loop."""
        self.running = True
        Config.initialize()

        self.print_welcome()
        self.console.print(
            "[dim]Type '/help' for available commands or start typing to chat.[/dim]\n"
        )

        while self.running:
            try:
                user_input = self.console.input("[bold]You >[/bold] ")

                if user_input.startswith("/"):
                    continue_running = self.handle_command(user_input)
                    if not continue_running:
                        self.running = False
                elif user_input.strip():
                    # AI chat not yet implemented
                    self.console.print(
                        "[yellow]AI chat not yet implemented in Stage 1[/yellow]"
                    )
                    self.console.print(
                        "[dim]Providers and models are configured, but AI interaction will be added in Stage 2.[/dim]"
                    )

            except KeyboardInterrupt:
                self.console.print("\n[yellow]Interrupted. Type '/exit' to quit.[/yellow]")
            except EOFError:
                break
            except Exception as e:
                logger.error(f"Error in CLI loop: {e}")
                self.print_error(f"An error occurred: {e}")


def print_version() -> None:
    """Print version information."""
    console = Console()
    console.print(f"OpenJarvis {__version__}")


def print_help_short() -> None:
    """Print short help message."""
    console = Console()
    text = f"""OpenJarvis v{__version__}
Open-source AI desktop assistant

Usage:
  python -m openjarvis          Start interactive CLI
  python -m openjarvis --help   Show this help message
  python -m openjarvis --version Show version
"""
    console.print(text)
