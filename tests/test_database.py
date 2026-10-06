"""Tests for database management."""

import sqlite3
import tempfile
from pathlib import Path

import pytest

from openjarvis.database import Database, close_db, get_db


class TestDatabase:
    """Test Database class."""

    def test_database_initialization(self):
        """Test database initialization."""
        with tempfile.TemporaryDirectory() as tmpdir:
            db_path = Path(tmpdir) / "test.db"
            db = Database(db_path)
            db.connect()
            
            # Verify database file was created
            assert db_path.exists()
            
            db.disconnect()

    def test_database_schema_creation(self):
        """Test that schema is created on connection."""
        with tempfile.TemporaryDirectory() as tmpdir:
            db_path = Path(tmpdir) / "test.db"
            db = Database(db_path)
            db.connect()
            
            cursor = db.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = {row[0] for row in cursor.fetchall()}
            
            # Verify expected tables are created
            expected_tables = {
                "conversations",
                "messages",
                "memory",
                "notes",
                "tasks",
                "reminders",
                "settings",
            }
            assert expected_tables.issubset(tables)
            
            db.disconnect()

    def test_database_query_execution(self):
        """Test query execution."""
        with tempfile.TemporaryDirectory() as tmpdir:
            db_path = Path(tmpdir) / "test.db"
            db = Database(db_path)
            db.connect()
            
            # Test INSERT
            db.execute(
                "INSERT INTO notes (id, title, content) VALUES (?, ?, ?)",
                ("test-id", "Test Note", "Test content")
            )
            db.commit()
            
            # Test SELECT
            cursor = db.execute("SELECT title FROM notes WHERE id = ?", ("test-id",))
            row = cursor.fetchone()
            assert row is not None
            assert row[0] == "Test Note"
            
            db.disconnect()

    def test_database_context_manager(self):
        """Test database as context manager."""
        with tempfile.TemporaryDirectory() as tmpdir:
            db_path = Path(tmpdir) / "test.db"
            
            with Database(db_path) as db:
                cursor = db.execute(
                    "SELECT name FROM sqlite_master WHERE type='table'"
                )
                tables = cursor.fetchall()
                assert len(tables) > 0

    def test_database_indices_created(self):
        """Test that indices are created."""
        with tempfile.TemporaryDirectory() as tmpdir:
            db_path = Path(tmpdir) / "test.db"
            db = Database(db_path)
            db.connect()
            
            cursor = db.execute(
                "SELECT name FROM sqlite_master WHERE type='index'"
            )
            indices = {row[0] for row in cursor.fetchall()}
            
            # Verify expected indices are created
            expected_indices = {
                "idx_conversation_id",
                "idx_message_timestamp",
                "idx_note_created",
                "idx_task_completed",
                "idx_reminder_scheduled",
            }
            assert expected_indices.issubset(indices)
            
            db.disconnect()

    def test_database_error_on_execute_without_connection(self):
        """Test that executing without connection raises error."""
        with tempfile.TemporaryDirectory() as tmpdir:
            db_path = Path(tmpdir) / "test.db"
            db = Database(db_path)
            
            with pytest.raises(RuntimeError):
                db.execute("SELECT * FROM notes")

    def test_database_transactions(self):
        """Test transaction support."""
        with tempfile.TemporaryDirectory() as tmpdir:
            db_path = Path(tmpdir) / "test.db"
            db = Database(db_path)
            db.connect()
            
            # Insert and commit
            db.execute(
                "INSERT INTO notes (id, title, content) VALUES (?, ?, ?)",
                ("test-id", "Test", "Content")
            )
            db.commit()
            
            # Verify insert
            cursor = db.execute("SELECT COUNT(*) FROM notes")
            count = cursor.fetchone()[0]
            assert count == 1
            
            db.disconnect()

    def test_database_rollback(self):
        """Test transaction rollback."""
        with tempfile.TemporaryDirectory() as tmpdir:
            db_path = Path(tmpdir) / "test.db"
            db = Database(db_path)
            db.connect()
            
            # Insert
            db.execute(
                "INSERT INTO notes (id, title, content) VALUES (?, ?, ?)",
                ("test-id", "Test", "Content")
            )
            db.commit()
            
            # Attempt rollback (should not affect committed data)
            db.execute(
                "INSERT INTO notes (id, title, content) VALUES (?, ?, ?)",
                ("test-id-2", "Test 2", "Content 2")
            )
            db.rollback()
            
            # Verify only first insert persists
            cursor = db.execute("SELECT COUNT(*) FROM notes")
            count = cursor.fetchone()[0]
            assert count == 1
            
            db.disconnect()
