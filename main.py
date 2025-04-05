import streamlit as st
from utils.quiz_utils import init_db

# Initialize DB on first run
init_db()

st.set_page_config(page_title="Smart StudyMate", layout="centered")
st.title("📚 Smart StudyMate")
st.markdown("AI-powered Study Assistant to help you learn better!")

st.sidebar.success("Select a page from the left 👈")

