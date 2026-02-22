import streamlit as st
import pandas as pd
from database import get_connection

st.set_page_config(page_title="Apply Job", layout="centered")
st.title("📝 Apply for a Job")

# ---------- Get Jobs from Database ----------
conn = get_connection()
try:
    jobs = pd.read_sql_query("SELECT job_id, title FROM job", conn)
finally:
    conn.close()

if not jobs.empty:
    # Create options like: "Software Engineer (ID: 1)"
    job_options = jobs["title"] + " (ID: " + jobs["job_id"].astype(str) + ")"
    selected_job = st.selectbox("Select Job", job_options)

    selected_job_id = int(selected_job.split("ID: ")[1].replace(")", ""))

    st.markdown(f"**Applying for:** {selected_job}")

    # ---------- Applicant Details ----------
    name = st.text_input("Your Name")
    qualifications = st.text_input("Qualifications")
    experience = st.text_input("Experience (years)")
    education = st.text_input("Education")

    if st.button("Apply"):
        if name and qualifications and experience and education:
            conn = get_connection()
            cursor = conn.cursor()
            try:
                # Insert application into apply_job table
                cursor.execute("""
                    INSERT INTO apply_job (emp_name, qualifications, experience, education, job_id, status)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (name, qualifications, experience, education, selected_job_id, "Pending"))
                conn.commit()
                st.success("✅ Application Submitted Successfully!")
            except Exception as e:
                st.error(f"Error submitting application: {e}")
            finally:
                conn.close()
        else:
            st.warning("Please fill in all fields.")
else:
    st.info("No jobs available to apply for.")