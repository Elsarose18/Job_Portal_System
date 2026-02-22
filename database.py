import sqlite3

# ---------- Database Connection ----------
def get_connection():
    conn = sqlite3.connect("job_portal.db", check_same_thread=False)
    return conn

# ---------- Create Tables ----------
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Jobs table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job (
            job_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            salary REAL NOT NULL
        )
    """)

    # Applications table with new fields
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS apply_job (
            app_id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_name TEXT NOT NULL,
            qualifications TEXT,
            experience TEXT,
            education TEXT,
            job_id INTEGER,
            status TEXT DEFAULT 'Pending'
        )
    """)

    conn.commit()
    conn.close()

# Run this automatically
create_tables()