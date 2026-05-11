import sqlite3

conn = sqlite3.connect("upwork_jobs.db")
conn.execute("ALTER TABLE jobs DROP COLUMN screening_result_explanation")
conn.commit()
conn.close()

print("Done")