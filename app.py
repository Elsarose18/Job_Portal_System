import streamlit as st
from database import reset_database

st.set_page_config(page_title="Job Portal", layout="wide")

st.title("💼 Job Portal System")

if st.button("Reset Database"):
    reset_database()
    st.success("Database reset successfully!")