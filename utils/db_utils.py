# === utils/db_utils.py ===
import sqlite3
import pandas as pd

def get_connection():
    return sqlite3.connect("utils/database/user_data.db", check_same_thread=False)

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS quiz_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            subject TEXT,
            score INTEGER,
            total_questions INTEGER,
            time_taken INTEGER,
            source_model TEXT,
            date_taken TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def insert_result(username, subject, score, total, time_taken, source_model):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        INSERT INTO quiz_results (username, subject, score, total_questions, time_taken, source_model)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (username, subject, score, total, time_taken, source_model))
    conn.commit()
    conn.close()

def load_results(username):
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM quiz_results WHERE username=?", conn, params=(username,))
    conn.close()
    return df
