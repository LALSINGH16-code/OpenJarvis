"""
Database management for OpenJarvis.

Handles SQLite database initialization, migrations, and connection management.
"""

import sqlite3
from pathlib import Path
from typing import Optional

from openjarvis.config import Config
from openjarvis.logging_config import get_logger

logger = get_logger(__name__)


class Database:
    """SQLite database connection and management."""

    def __init__(self, db_path: Optional[Path] = None):
        """Initialize database connection."""
        self.db_path = db_path or Config.DB_PATH
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.connection: Optional[sqlite3.Connection] = None

    def connect(self) -> None:
        """Connect to the database."""
        try:
            self.connection = sqlite3.connect(str(self.db_path))
            self.connection.row_factory = sqlite3.Row
            logger.info(f"Connected to database: {self.db_path}")
            self._initialize_schema()
        except sqlite3.Error as e:
            logger.error(f"Failed to connect to database: {e}")
            raise

    def disconnect(self) -> None:
        """Disconnect from the database."""
        if self.connection:
            self.connection.close()
            logger.info("Disconnected from database")

    def execute(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        """Execute a query and return cursor."""
        if not self.connection:
            raise RuntimeError("Database not connected")
        return self.connection.execute(query, params)

    def execute_many(self, query: str, params_list: list) -> None:
        """Execute a query multiple times with different parameters."""
        if not self.connection:
            raise RuntimeError("Database not connected")
        self.connection.executemany(query, params_list)

    def commit(self) -> None:
        """Commit changes to the database."""
        if self.connection:
            self.connection.commit()

    def rollback(self) -> None:
        """Rollback changes."""
        if self.connection:
            self.connection.rollback()

    def _initialize_schema(self) -> None:
        """Initialize database schema."""
        cursor = self.connection.cursor()

        # Conversations table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS conversations (
                id TEXT PRIMARY KEY,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                provider TEXT,
                model TEXT
            )
            """
        )

        # Messages table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS messages (
                id TEXT PRIMARY KEY,
                conversation_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (conversation_id) REFERENCES conversations (id)
            )
            """
        )

        # Memory table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS memory (
                id TEXT PRIMARY KEY,
                key TEXT UNIQUE NOT NULL,
                value TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        # Notes table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS notes (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        # Tasks table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                completed INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                completed_at TIMESTAMP
            )
            """
        )

        # Reminders table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS reminders (
                id TEXT PRIMARY KEY,
                message TEXT NOT NULL,
                scheduled_at TIMESTAMP NOT NULL,
                triggered INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        # Settings table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            )
            """
        )

        # Create indexes for faster queries
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_conversation_id ON messages (conversation_id)"
        )
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_message_timestamp ON messages (timestamp)"
        )
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_note_created ON notes (created_at)"
        )
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_task_completed ON tasks (completed)"
        )
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_reminder_scheduled ON reminders (scheduled_at)"
        )

        self.connection.commit()
        logger.info("Database schema initialized")

    def close(self) -> None:
        """Close the database connection."""
        self.disconnect()

    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()


# Global database instance
_db_instance: Optional[Database] = None


def get_db() -> Database:
    """Get or create the database instance."""
    global _db_instance
    if _db_instance is None:
        _db_instance = Database()
        _db_instance.connect()
    return _db_instance


def close_db() -> None:
    """Close the global database instance."""
    global _db_instance
    if _db_instance:
        _db_instance.close()
        _db_instance = None
