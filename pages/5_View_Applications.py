import streamlit as st
import pandas as pd
from database import get_connection

st.title("📄 All Applications")

conn = get_connection()
df = pd.read_sql_query("""
    SELECT a.app_id, a.emp_name, j.title, a.status
    FROM apply_job a
    JOIN job j ON a.job_id = j.job_id
""", conn)
conn.close()

st.dataframe(df)