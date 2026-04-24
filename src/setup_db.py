import sqlite3

conn=sqlite3.connect("jobss.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    job_id INTEGER PRIMARY KEY,
    company_name TEXT,
    industry TEXT,
    job_title TEXT,
    skills_required TEXT,
    experience_level TEXT,
    employment_type TEXT,
    location TEXT,
    salary_range_usd TEXT,
    posted_date TEXT,
    company_size TEXT,
    tools_preferred TEXT,
    ingestion_timestamp TEXT
)
""")


conn.commit()
conn.close()

conn=sqlite3.connect("jobss.db")
cursor = conn.cursor()

cursor.execute("""
Create TABLE IF NOT EXISTS alerts(
      alert_id INTEGER PRIMARY KEY AUTOINCREMENT,
      alert_msg TEXT,
      alert_time TEXT,
      alert_type TEXT
)
""")
conn.commit()
conn.close()



print("Database and table created")