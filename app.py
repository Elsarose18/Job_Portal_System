import streamlit as st
from database import create_tables

create_tables()

st.set_page_config(page_title="Job Portal System", layout="wide")

st.markdown("<h1 style='text-align:center;'>💼 Job Portal System</h1>", unsafe_allow_html=True)
st.markdown("### Welcome to Recruitment Platform")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/1_Post_Job.py", label="🏢 Post Job")
    st.page_link("pages/3_Validate_Applications.py", label="✔ Validate Applications")
    st.page_link("pages/5_View_Applications.py", label="📄 View Applications")

with col2:
    st.page_link("pages/2_Apply_Job.py", label="📝 Apply Job")
    st.page_link("pages/4_View_Jobs.py", label="📄 View Jobs")