import streamlit as st
from database import get_connection

st.title("📝 Post a Job")

# Input fields
title = st.text_input("Job Title")
salary = st.number_input("Salary", min_value=0.0, step=1000.0)
company = st.text_input("Company Name")

if st.button("Post Job"):
    if title and company:
        conn = get_connection()
        cursor = conn.cursor()

        # Add company if not exists
        cursor.execute("SELECT employer_id FROM employer WHERE company_name = ?", (company,))
        result = cursor.fetchone()
        if result:
            employer_id = result[0]
        else:
            cursor.execute("INSERT INTO employer (company_name) VALUES (?)", (company,))
            employer_id = cursor.lastrowid

        # Insert job
        cursor.execute(
            "INSERT INTO job (title, salary, employer_id) VALUES (?, ?, ?)",
            (title, salary, employer_id)
        )

        conn.commit()
        conn.close()
        st.success(f"Job '{title}' posted successfully!")
    else:
        st.error("Please fill in all fields!")