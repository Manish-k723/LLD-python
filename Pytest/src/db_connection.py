import sqlite3

db_connection = "sqlite:///test.db"

def save_user(name, age):
    conn = sqlite3.connect(db_connection)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()