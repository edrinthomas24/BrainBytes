# === pages/6_Dashboard.py ===
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_extras.metric_cards import style_metric_cards
from utils.db_utils import load_results

def dashboard(username):
    st.title("📊 Personalized Quiz Dashboard")
    df = load_results(username)

    if df.empty:
        st.warning("No quiz data found.")
        return

    df['accuracy'] = df['score'] / df['total_questions'] * 100
    avg_accuracy = df['accuracy'].mean()
    avg_time = df['time_taken'].mean()

    st.subheader("🧾 Summary Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("📝 Quizzes Taken", len(df))
    col2.metric("✅ Avg Accuracy", f"{avg_accuracy:.2f}%")
    col3.metric("⏱️ Avg Time", f"{avg_time:.1f} sec")
    style_metric_cards()

    st.divider()

    st.subheader("📚 Accuracy by Subject")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(data=df, x='subject', y='accuracy', ax=ax, palette="coolwarm")
    ax.set_ylabel("Accuracy (%)")
    ax.set_xlabel("")
    st.pyplot(fig)

    st.subheader("⏲️ Time Taken per Subject")
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    sns.boxplot(data=df, x='subject', y='time_taken', ax=ax2, palette="Set2")
    ax2.set_ylabel("Time (sec)")
    ax2.set_xlabel("")
    st.pyplot(fig2)

    st.subheader("🤖 Performance by AI Model")
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    sns.barplot(data=df, x='source_model', y='accuracy', ax=ax3, palette="viridis")
    ax3.set_ylabel("Accuracy (%)")
    ax3.set_xlabel("")
    st.pyplot(fig3)

# Example:
# from utils.db_utils import init_db, insert_result
# init_db()
# insert_result("john", "Math", 8, 10, 63, "GPT-4")
# dashboard("john")
