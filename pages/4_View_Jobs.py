import streamlit as st
import pandas as pd
from database import get_connection

st.title("📄 Available Jobs")

conn = get_connection()
df = pd.read_sql_query("SELECT * FROM job", conn)
conn.close()

st.dataframe(df)