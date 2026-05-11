import os
import sqlite3


def connect_to_db(database_name='upwork_jobs.db'):
    # Get the full path to the database file
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    parent_dir = os.path.dirname(current_dir)  # Get the parent directory
    database_path = os.path.join(parent_dir, database_name)
    # Connect to database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    return conn, cursor


def create_db(conn, cursor):
    # Create the `jobs` table (if it doesn't exist)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            listing_id TEXT NOT NULL,
            listing_url TEXT,
            listing_title TEXT NOT NULL,
            posted_date DATETIME,
            listing_description TEXT NOT NULL,
            listing_tags TEXT,
            proposals TEXT,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            screened BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()

