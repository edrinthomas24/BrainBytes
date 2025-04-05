import streamlit as st
from utils.summary_utils import offline_summary, online_summary
from utils.quiz_utils import log_user_prompt

st.title("📝 Summarize Notes")

text = st.text_area("Paste your text to summarize")
mode = st.selectbox("Choose mode", ["Offline", "Online"])

if st.button("Summarize") and text:
    if mode == "Offline":
        result = offline_summary(text)
    else:
        result = online_summary(text)
    st.success(result)
    log_user_prompt("edrin", "Summarizer", text)
