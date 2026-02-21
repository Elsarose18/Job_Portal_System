import sqlite3

# ---------- Database Connection ----------
def get_connection():
    conn = sqlite3.connect("job_portal.db", check_same_thread=False)
    return conn


# ---------- Create Tables ----------
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Company Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS company (
            company_id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT NOT NULL
        )
    """)

    # Job Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job (
            job_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            salary REAL NOT NULL,
            company_id INTEGER,
            FOREIGN KEY (company_id) REFERENCES company(company_id)
        )
    """)

    # Applications Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS apply_job (
            app_id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_name TEXT NOT NULL,
            job_id INTEGER,
            resume BLOB,
            status TEXT DEFAULT 'Pending',
            FOREIGN KEY (job_id) REFERENCES job(job_id)
        )
    """)

    conn.commit()
    conn.close()