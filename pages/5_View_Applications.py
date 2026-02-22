import streamlit as st
import pandas as pd
from utils.db import get_connection

st.title("📄 View Applications")

conn = get_connection()
applications = pd.read_sql_query("""
    SELECT a.application_id, a.applicant_name, a.email, a.phone, a.qualification,
           a.experience, j.title AS job_title, a.status
    FROM application a
    JOIN job j ON a.job_id = j.job_id
""", conn)
conn.close()

if applications.empty:
    st.info("No applications found.")
else:
    st.dataframe(applications)