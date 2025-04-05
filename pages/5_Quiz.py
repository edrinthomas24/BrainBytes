# === pages/5_Quiz.py ===
import streamlit as st
import time
from utils.quiz_utils import save_quiz_to_db, insert_result

st.title("🧠 Quiz Generator")

username = st.text_input("Enter your username", key="quiz_user")
topic = st.text_input("Topic")
question = st.text_input("Question")
options = st.text_area("Options (comma separated)")
answer = st.text_input("Correct Answer")
source_model = st.selectbox("Source AI Model", ["GPT-4", "Gemini", "LLaMA", "DeepSeek", "Cohere"])

if st.button("Save Quiz"):
    save_quiz_to_db(topic, question, options.split(','), answer)
    st.success("Quiz saved!")

# Simulate quiz session (for testing result storage)
if st.button("Simulate Quiz Result"):
    with st.spinner("Evaluating..."):
        time.sleep(2)
        score = 4
        total_questions = 5
        time_taken = 42
        insert_result(username, topic, score, total_questions, time_taken, source_model)
        st.success("Sample result logged successfully!")
