import streamlit as st

# Page configuration
st.set_page_config(page_title="Job Portal", page_icon="📝")

# Sidebar menu
st.sidebar.title("Job Portal")
menu = [
    "Home",
    "Post Job",
    "Apply Job",
    "View Jobs",
    "View Applications",
    "Validate Applications"
]
choice = st.sidebar.selectbox("Menu", menu)

# Home Page
if choice == "Home":
    st.title("🏠 Welcome to Job Portal")
    st.write("Use the sidebar to navigate to Post Job, Apply Job, or view applications.")

# Post Job Page
elif choice == "Post Job":
    st.experimental_set_query_params(page="post_job")
    st.write("Go to: Pages → 1_Post_Job")

# Apply Job Page
elif choice == "Apply Job":
    st.experimental_set_query_params(page="apply_job")
    st.write("Go to: Pages → 2_Apply_Job")

# View Jobs Page
elif choice == "View Jobs":
    st.experimental_set_query_params(page="view_jobs")
    st.write("Go to: Pages → 3_View_Jobs")

# View Applications Page
elif choice == "View Applications":
    st.experimental_set_query_params(page="view_applications")
    st.write("Go to: Pages → 4_View_Applications")

# Validate Applications Page
elif choice == "Validate Applications":
    st.experimental_set_query_params(page="validate_applications")
    st.write("Go to: Pages → 5_Validate_Applications")

# Admin Option: Reset Database
st.markdown("---")
st.subheader("⚠️ Admin Options")
if st.button("Reset Database"):
    from database import reset_database
    reset_database()
    st.success("✅ Database has been reset and tables recreated!")