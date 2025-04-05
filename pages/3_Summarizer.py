import streamlit as st
from utils.summary_utils import summarize_text_sumy

st.title("📄 Summarizer")
text = st.text_area("Paste your text below:", height=300)
if st.button("Summarize"):
    summary = summarize_text_sumy(text)
    st.success("Summary:")
    st.write(summary)
