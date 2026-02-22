# database.py
import sqlite3

# Name of your SQLite database file
DB_FILE = "job_portal.db"

def get_connection():
    """Connect to the SQLite database and return the connection object."""
    conn = sqlite3.connect(DB_FILE)
    return conn

def create_tables():
    """Create all necessary tables for the job portal app."""
    conn = get_connection()
    cursor = conn.cursor()

    # -----------------------------
    # Employer table
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employer (
            employer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT NOT NULL
        )
    """)

    # -----------------------------
    # Job table
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job (
            job_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT NOT NULL,
            salary INTEGER
        )
    """)

    # -----------------------------
    # Apply Job table
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS apply_job (
            app_id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_name TEXT NOT NULL,
            qualification TEXT,
            experience TEXT,
            skills TEXT,
            job_id INTEGER,
            status TEXT DEFAULT 'Pending',
            FOREIGN KEY(job_id) REFERENCES job(job_id)
        )
    """)

    # Commit changes and close connection
    conn.commit()
    conn.close()

# -----------------------------
# Optional: initialize the DB when running this file
# -----------------------------
if __name__ == "__main__":
    create_tables()
    print("✅ All tables created successfully in job_portal.db")