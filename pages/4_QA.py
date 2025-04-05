import streamlit as st
from utils.qa_utils import ask_question
from utils.quiz_utils import log_user_prompt

st.title("🤖 AI Q&A")

question = st.text_input("Ask a question")

if st.button("Get Answer") and question:
    answer = ask_question(question)
    st.success(answer)
    log_user_prompt("edrin", "Q&A", question)
