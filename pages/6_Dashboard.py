import streamlit as st
import sqlite3

def fetch_all(table):
    conn = sqlite3.connect("studymate.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table} ORDER BY timestamp DESC")
    return cursor.fetchall()

st.title("📊 Dashboard")

st.subheader("📝 Quizzes")
for row in fetch_all("quizzes"):
    st.write(row)

st.subheader("📥 Uploaded Files")
for row in fetch_all("uploaded_files"):
    st.write(row)

st.subheader("📜 Prompts")
for row in fetch_all("user_prompts"):
    st.write(row)

st.subheader("🔐 Login/Logout")
for row in fetch_all("user_activity"):
    st.write(row)
