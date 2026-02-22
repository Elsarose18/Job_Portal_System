import sqlite3

def get_connection():
    return sqlite3.connect("job_portal.db", check_same_thread=False)

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Jobs table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS job (
        job_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        company TEXT NOT NULL,
        salary REAL NOT NULL
    )
    """)

    # Applications table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS apply_job (
        app_id INTEGER PRIMARY KEY AUTOINCREMENT,
        emp_name TEXT NOT NULL,
        qualifications TEXT,
        experience TEXT,
        job_id INTEGER,
        status TEXT DEFAULT 'Pending',
        FOREIGN KEY (job_id) REFERENCES job(job_id)
    )
    """)

    conn.commit()
    conn.close()