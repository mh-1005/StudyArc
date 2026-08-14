import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).resolve().parents[3] / "studyarc.db"


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            subject TEXT NOT NULL,
            content TEXT NOT NULL
        )
        """)

    connection.commit()
    connection.close()
