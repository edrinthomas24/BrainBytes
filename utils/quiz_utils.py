import sqlite3
from datetime import datetime

DB_NAME = "studymate.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quizzes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT, question TEXT, options TEXT,
            answer TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT, action TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS uploaded_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT, filename TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_prompts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT, module TEXT, prompt TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
    ''')
    conn.commit()
    conn.close()

def save_quiz_to_db(topic, question, options, answer):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO quizzes (topic, question, options, answer)
        VALUES (?, ?, ?, ?)''', (topic, question, str(options), answer))
    conn.commit()
    conn.close()

def get_all_quizzes():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM quizzes ORDER BY timestamp DESC')
    return cursor.fetchall()

def log_user_action(username, action):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_activity (username, action) VALUES (?, ?)', (username, action))
    conn.commit()
    conn.close()

def log_file_upload(username, filename):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO uploaded_files (username, filename) VALUES (?, ?)', (username, filename))
    conn.commit()
    conn.close()

def log_user_prompt(username, module, prompt):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_prompts (username, module, prompt) VALUES (?, ?, ?)', (username, module, prompt))
    conn.commit()
    conn.close()
