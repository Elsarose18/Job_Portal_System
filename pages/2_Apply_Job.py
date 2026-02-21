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

    # Create readable job options
    job_options = jobs.apply(
        lambda row: f"{row['title']} at {row['company']} (ID: {row['job_id']})",
        axis=1
    )

    selected_job = st.selectbox("Select Job", job_options)

    # Extract job_id
    selected_job_id = int(selected_job.split("ID: ")[1].replace(")", ""))

    st.markdown(f"### 📌 Applying for: {selected_job}")

    st.divider()

    name = st.text_input("👤 Your Name")

    resume = st.file_uploader(
        "📄 Upload Resume (PDF only)",
        type=["pdf"]
    )

    if st.button("🚀 Submit Application"):

        if name and resume:

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO apply_job (emp_name, job_id, resume, status)
                VALUES (?, ?, ?, ?)
            """, (
                name,
                selected_job_id,
                resume.read(),   # Store file as BLOB
                "Pending"
            ))

            conn.commit()
            conn.close()

            st.success("✅ Application Submitted Successfully!")

        else:
            st.warning("⚠ Please fill all fields and upload your resume.")

else:
    st.info("🚫 No jobs available at the moment.")