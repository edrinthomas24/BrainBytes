import streamlit as st
from utils.quiz_utils import save_quiz_to_db

st.title("🧠 Quiz Generator")

topic = st.text_input("Topic")
question = st.text_input("Question")
options = st.text_area("Options (comma separated)")
answer = st.text_input("Correct Answer")

if st.button("Save Quiz"):
    save_quiz_to_db(topic, question, options.split(','), answer)
    st.success("Quiz saved!")
