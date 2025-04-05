import streamlit as st
from utils.qa_utils import ask_question

st.title("❓ Q&A Assistant")
context = st.text_area("Paste your study notes:")
question = st.text_input("Ask a question:")
if st.button("Get Answer"):
    answer = ask_question(context, question)
    st.write(f"🧠 Answer: {answer}")
