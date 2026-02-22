import streamlit as st
import pandas as pd
from utils.db import get_connection

st.title("✅ Validate Applications")

conn = get_connection()
applications = pd.read_sql_query("""
    SELECT a.application_id, a.applicant_name, a.email, j.title AS job_title, a.status
    FROM application a
    JOIN job j ON a.job_id = j.job_id
    WHERE a.status='Pending'
""", conn)

if applications.empty:
    st.info("No pending applications.")
else:
    for idx, row in applications.iterrows():
        col1, col2, col3, col4 = st.columns([2, 3, 3, 2])
        col1.write(row['applicant_name'])
        col2.write(row['email'])
        col3.write(row['job_title'])
        if col4.button(f"Validate {row['application_id']}", key=row['application_id']):
            cursor = conn.cursor()
            cursor.execute("UPDATE application SET status='Validated' WHERE application_id=?", (row['application_id'],))
            conn.commit()
            st.success(f"{row['applicant_name']} validated!")
st.experimental_rerun()