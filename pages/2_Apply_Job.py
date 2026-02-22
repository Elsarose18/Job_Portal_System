import streamlit as st
import pandas as pd
from database import get_connection

st.title("📝 Apply for a Job")

conn = get_connection()

# Fetch jobs with company name
jobs = pd.read_sql_query("""
SELECT job.job_id, job.title, employer.company_name AS company
FROM job
JOIN employer ON job.employer_id = employer.employer_id
""", conn)

conn.close()

if not jobs.empty:
    job_options = [f"{row['title']} at {row['company']}" for index, row in jobs.iterrows()]
    selected_job = st.selectbox("Select a job to apply", job_options)

    if st.button("Apply"):
        st.success(f"You applied for '{selected_job}' successfully!")
else:
    st.info("No jobs available at the moment.")