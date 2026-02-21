import streamlit as st
import pandas as pd
from database import get_connection

st.title("📝 Apply Job")

emp_name = st.text_input("Your Name")
resume = st.text_area("Paste Resume Content")

conn = get_connection()
jobs = pd.read_sql_query("SELECT job_id, title FROM job", conn)
conn.close()

if not jobs.empty:
    job_options = jobs.set_index("title")["job_id"].to_dict()
    selected_job = st.selectbox("Select Job", list(job_options.keys()))
    job_id = job_options[selected_job]

    if st.button("Apply"):
        if emp_name and resume:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO apply_job (emp_name, resume, job_id)
                VALUES (?, ?, ?)
            """, (emp_name, resume, job_id))
            conn.commit()
            conn.close()
            st.success("Application Submitted ✅")
        else:
            st.warning("Fill all fields")
else:
    st.info("No jobs available")