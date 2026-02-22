import streamlit as st

st.set_page_config(page_title="Job Portal", layout="wide")

st.title("📝 Job Portal System")

options = ["Home", "Post Job", "Apply Job", "View Jobs", "View Applications", "Validate Applications", "Reset Database"]
choice = st.sidebar.selectbox("Select an Option", options)

if choice == "Home":
    st.write("Welcome to Job Portal! Use the sidebar to navigate.")
elif choice == "Post Job":
    import pages.1_Post_Job
elif choice == "Apply Job":
    import pages.2_Apply_Job
elif choice == "View Jobs":
    import pages.3_View_Jobs
elif choice == "View Applications":
    import pages.4_View_Applications
elif choice == "Validate Applications":
    import pages.5_Validate_Applications
elif choice == "Reset Database":
    import pages.0_Reset_Database