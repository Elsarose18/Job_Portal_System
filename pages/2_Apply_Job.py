import streamlit as st
import pandas as pd
import sqlite3

from utils.db import get_connection

st.title("📝 Apply for a Job")

# Connect to DB
conn = get_connection()
jobs = pd.read_sql_query("SELECT job_id, title FROM job", conn)
conn.close()

if jobs.empty:
    st.warning("No jobs available currently.")
else:
    with st.form("apply_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        qualification = st.text_input("Qualification")
        experience = st.text_input("Experience (years)")
        job_choice = st.selectbox("Select Job", jobs['title'].tolist())
        submit = st.form_submit_button("Apply")

        if submit:
            selected_job_id = jobs[jobs['title'] == job_choice]['job_id'].values[0]
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO application 
                (applicant_name, email, phone, qualification, experience, job_id, status)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (name, email, phone, qualification, experience, selected_job_id, "Pending"))
            conn.commit()
            conn.close()
            st.success("Application submitted successfully!")