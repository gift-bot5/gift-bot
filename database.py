import sqlite3
import os

DB_PATH = "data/gifts.db"

def init_db():
    if not os.path.exists("data"):
        os.makedirs("data")
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS gifts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                from_user_id TEXT NOT NULL,
                to_user_id TEXT NOT NULL,
                gift_type TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()

def save_gift(from_user, to_user, gift):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO gifts (from_user_id, to_user_id, gift_type)
            VALUES (?, ?, ?)
        """, (from_user, to_user, gift))
        conn.commit()

def get_gifts(user_id):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM gifts WHERE to_user_id = ?", (user_id,))
        return cur.fetchall()