import streamlit as st

st.title("📊 Dashboard")
st.markdown("Track your usage:")

# Static example stats
st.metric("Files Processed", 12)
st.metric("Summaries Created", 8)
st.metric("Quizzes Taken", 5)
