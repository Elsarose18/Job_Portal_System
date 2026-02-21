import sqlite3

def get_connection():
    conn = sqlite3.connect("job_portal.db", check_same_thread=False)
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Employer Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employer (
            employer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT NOT NULL
        )
    """)

    # Job Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job (
            job_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            salary REAL NOT NULL,
            employer_id INTEGER,
            FOREIGN KEY (employer_id) REFERENCES employer(employer_id)
        )
    """)

    # Applications Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS apply_job (
            app_id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_name TEXT NOT NULL,
            resume TEXT,
            job_id INTEGER,
            status TEXT DEFAULT 'Pending',
            FOREIGN KEY (job_id) REFERENCES job(job_id)
        )
    """)

    conn.commit()
    conn.close()