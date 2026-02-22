# pages/2_Apply_Job.py
import streamlit as st
import pandas as pd
from database import get_connection  # Make sure database.py has get_connection() function

st.set_page_config(page_title="Apply Job", layout="centered")
st.title("📝 Apply for a Job")

# Connect to database
conn = get_connection()

# Fetch jobs
try:
    jobs = pd.read_sql_query("SELECT job_id, title, salary FROM job", conn)
except Exception as e:
    st.error(f"Error fetching jobs: {e}")
    jobs = pd.DataFrame()  # empty

conn.close()

if not jobs.empty:
    job_options = jobs["title"] + " (Salary: ₹" + jobs["salary"].astype(str) + ")"
    selected_job = st.selectbox("Select Job", job_options)
    selected_job_id = int(selected_job.split("(")[0].strip())  # get job_id from string

    st.markdown(f"**Applying for:** {selected_job}")

    # Applicant info
    name = st.text_input("Full Name")
    qualification = st.text_input("Qualification")
    experience = st.text_input("Experience")
    skills = st.text_input("Skills")

    if st.button("Apply"):
        if name and qualification and experience and skills:
            try:
                conn = get_connection()
                cursor = conn.cursor()

                cursor.execute("""
                    INSERT INTO apply_job (emp_name, qualification, experience, skills, job_id, status)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (name, qualification, experience, skills, selected_job_id, "Pending"))

                conn.commit()
                conn.close()
                st.success("✅ Application Submitted Successfully!")
            except Exception as e:
                st.error(f"Error submitting application: {e}")
        else:
            st.warning("Please fill all fields before submitting.")

else:
    st.info("No jobs available at the moment. Please check back later.")