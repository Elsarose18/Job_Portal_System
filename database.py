import sqlite3

def get_connection():
    return sqlite3.connect("job_portal.db")

def reset_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Drop existing tables
    cursor.execute("DROP TABLE IF EXISTS applications")
    cursor.execute("DROP TABLE IF EXISTS job")
    cursor.execute("DROP TABLE IF EXISTS employer")
    cursor.execute("DROP TABLE IF EXISTS users")

    # Create tables
    cursor.execute("""
    CREATE TABLE employer (
        employer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE job (
        job_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        salary REAL,
        employer_id INTEGER,
        FOREIGN KEY (employer_id) REFERENCES employer(employer_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE applications (
        application_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        job_id INTEGER,
        application_date TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (job_id) REFERENCES job(job_id)
    )
    """)

    conn.commit()
    conn.close()
    print("✅ Database reset and tables created successfully!")