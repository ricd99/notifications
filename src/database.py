"""
Database functions
"""

import sqlite3

def get_unscreened_jobs(db_path: str) -> list[dict]:
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row  # each row becomes a Row object (dictionary-like)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM jobs WHERE screened = 0")
        return [dict(row) for row in cursor.fetchall()] # unpack the Row objects into python dictionaries
    
def mark_job_screened(db_path:str, job_id: str) -> None:
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            "UPDATE jobs SET screened = 1 WHERE job_id = ?",
            (job_id,), # tuples with one element require trailing comma
        )
        conn.commit()