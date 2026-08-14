import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).resolve().parents[3] / "studyarc.db"


def get_connection():
    return sqlite3.connect(DATABASE_PATH)
