import streamlit as st
import pandas as pd
from database import get_connection

st.title("✔ Validate Applications")

conn = get_connection()
df = pd.read_sql_query("""
    SELECT a.app_id, a.emp_name, a.resume, j.title, a.status
    FROM apply_job a
    JOIN job j ON a.job_id = j.job_id
""", conn)
conn.close()

if not df.empty:
    selected_app = st.selectbox("Select Application", df["app_id"])

    app_data = df[df["app_id"] == selected_app].iloc[0]

    st.write("### Applicant:", app_data["emp_name"])
    st.write("### Job:", app_data["title"])
    st.write("### Resume:")
    st.text(app_data["resume"])

    col1, col2 = st.columns(2)

    if col1.button("Approve"):
        conn = get_connection()
        conn.execute("UPDATE apply_job SET status='Approved' WHERE app_id=?", (selected_app,))
        conn.commit()
        conn.close()
        st.success("Approved ✅")

    if col2.button("Reject"):
        conn = get_connection()
        conn.execute("UPDATE apply_job SET status='Rejected' WHERE app_id=?", (selected_app,))
        conn.commit()
        conn.close()
        st.error("Rejected ❌")
else:
    st.info("No applications found")