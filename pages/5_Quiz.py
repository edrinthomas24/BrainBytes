import streamlit as st
from utils.quiz_utils import generate_quiz

st.title("🧩 Quiz Generator")
topic = st.text_input("Enter topic or paragraph:")
if st.button("Generate Quiz"):
    quiz = generate_quiz(topic)
    for q in quiz:
        st.markdown(f"**Q: {q['question']}**")
        st.radio("Choose one:", q['options'], key=q['question'])
