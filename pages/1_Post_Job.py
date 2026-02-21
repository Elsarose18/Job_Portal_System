import streamlit as st
from database import get_connection

st.title("🏢 Post Job")

company_name = st.text_input("Company Name")
title = st.text_input("Job Title")
salary = st.number_input("Salary", min_value=0.0)

if st.button("Post Job"):
    if company_name and title:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO employer (company_name) VALUES (?)", (company_name,))
        employer_id = cursor.lastrowid

        cursor.execute(
            "INSERT INTO job (title, salary, employer_id) VALUES (?, ?, ?)",
            (title, salary, employer_id)
        )

        conn.commit()
        conn.close()
        st.success("Job Posted Successfully ✅")
    else:
        st.warning("All fields required")