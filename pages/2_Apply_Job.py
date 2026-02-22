import streamlit as st
import pandas as pd
from database import get_connection

st.set_page_config(page_title="Apply Job", layout="centered")
st.title("📝 Apply for a Job")

# Get jobs from database
conn = get_connection()
jobs = pd.read_sql_query("SELECT job_id, title, company FROM job", conn)
conn.close()

if not jobs.empty:
    job_options = jobs["title"] + " (" + jobs["company"] + ")"
    selected_job = st.selectbox("Select Job", job_options)

    selected_job_id = jobs.loc[jobs["title"] + " (" + jobs["company"] + ")" == selected_job, "job_id"].values[0]

    st.markdown(f"**Applying for:** {selected_job}")

    # Employee input fields
    name = st.text_input("Your Name")
    qualifications = st.text_area("Qualifications (e.g., B.Tech, MBA, etc.)")
    experience = st.text_area("Experience (e.g., 2 years at XYZ)")

    if st.button("Apply"):
        if name and qualifications and experience:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO apply_job (emp_name, qualifications, experience, job_id, status)
                VALUES (?, ?, ?, ?, ?)
            """, (name, qualifications, experience, selected_job_id, "Pending"))

            conn.commit()
            conn.close()

            st.success("✅ Application submitted successfully!")
        else:
            st.warning("Please fill in all fields.")
else:
    st.info("No jobs available.")